"""Check the recorded scope and provenance of a research novelty assessment."""

import argparse
import calendar
import hashlib
import json
import sys
from datetime import date, timedelta
from pathlib import Path


def initial():
    return {
        "schema": 1, "as_of": date.today().isoformat(), "claims": [], "queries": [],
        "papers": [], "scope": {"seed_check": "", "citation_chase": "", "stop_reason": "",
                                "critical_gaps": [], "materials": {}},
        "review": {"kind": "", "reviewer": "", "evidence_digest": "", "trace_file": "",
                   "reviewed_claims": [], "complete": False},
    }


def required(record, fields, label):
    for field in fields.split():
        if not isinstance(record.get(field), str) or not record[field].strip():
            raise ValueError(f"{label}: missing text field {field}")


def records(data, key):
    rows = data.get(key)
    if not isinstance(rows, list):
        raise ValueError(f"{key}: expected an array")
    result = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{key}: expected an object")
        required(row, "id", key)
        if row["id"] in result:
            raise ValueError(f"{key}: duplicate ID {row['id']}")
        result[row["id"]] = row
    return result


def reference_list(row, key, known):
    refs = row.get(key)
    if not isinstance(refs, list) or any(not isinstance(v, str) or v not in known for v in refs):
        raise ValueError(f"{row['id']}: invalid {key} reference")
    if len(refs) != len(set(refs)):
        raise ValueError(f"{row['id']}: duplicate {key} reference")
    return refs


def iso(value):
    if not isinstance(value, str):
        raise ValueError("date must use YYYY-MM-DD")
    parsed = date.fromisoformat(value)
    if value != parsed.isoformat():
        raise ValueError("date must use YYYY-MM-DD")
    return parsed


def fields_file(root, name):
    if not isinstance(name, str) or not name.strip() or Path(name).is_absolute():
        raise ValueError(f"expected a case-relative evidence file: {name!r}")
    path = (root / name).resolve()
    if root not in path.parents or not path.is_file():
        raise ValueError(f"missing or out-of-case file: {name}")
    content = path.read_bytes()
    if not content.strip():
        raise ValueError(f"empty evidence file: {name}")
    return content


def digest(data, root):
    if not isinstance(data, dict) or type(data.get("schema")) is not int or data["schema"] != 1:
        raise ValueError("expected dossier schema 1")
    evidence = {key: data[key] for key in ("schema", "as_of", "claims", "queries", "papers", "scope")}
    attachments = {}
    for group, key in (("papers", "evidence_file"), ("queries", "trace_file")):
        for row in records(data, group).values():
            required(row, key, row["id"])
            name = row[key]
            if name not in attachments:
                attachments[name] = hashlib.sha256(fields_file(root, name)).hexdigest()
    if not isinstance(data["scope"], dict) or not isinstance(data["scope"].get("materials"), dict):
        raise ValueError("scope.materials must map supporting records to case-relative files")
    for name in data["scope"]["materials"].values():
        content = fields_file(root, name)
        attachments[name] = hashlib.sha256(content).hexdigest()
    payload = json.dumps([evidence, attachments], ensure_ascii=False, sort_keys=True,
                         separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def clean(text):
    return " ".join(text.casefold().split())


def source_name(name):
    compact = "".join(c for c in name.casefold() if c.isalnum())
    common = {"crossrefapi": "crossref", "apicrossreforg": "crossref",
              "openalexapi": "openalex", "apiopenalexorg": "openalex",
              "arxivorg": "arxiv", "arxivapi": "arxiv"}
    return common.get(compact, compact)


def half_year_before(day):
    month_index = day.year * 12 + day.month - 1 - 6
    year, month = divmod(month_index, 12)
    return date(year, month + 1, min(day.day, calendar.monthrange(year, month + 1)[1]))


def check_search_receipt(row, root):
    name = row["trace_file"]
    if not name.lower().endswith(".json"):
        return
    receipt = json.loads(fields_file(root, name).decode("utf-8-sig"))
    if not isinstance(receipt, dict) or receipt.get("action") != "search" or "providers" not in receipt:
        return
    source = source_name(row["source"])
    if source not in receipt["providers"]:
        raise ValueError(f"{row['id']}: source not in search receipt")
    actual = receipt["providers"][source]
    expected = {"ok": "ok", "zero_hits": "ok", "failed": "unavailable", "partial": "partial"}
    parameters = receipt["parameters"]
    for field, parameter in (("query", "public_query"), ("from", "from_date"), ("to", "until_date")):
        if row.get(field) != parameters.get(parameter):
            raise ValueError(f"{row['id']}: {field} disagrees with search receipt")
    if row["status"] != expected.get(actual["status"]):
        raise ValueError(f"{row['id']}: status disagrees with search receipt")
    if row["status"] != "unavailable" and row.get("total") != actual["provider_total_hits"]:
        raise ValueError(f"{row['id']}: total disagrees with search receipt")
    if (row.get("screened") or 0) > len(actual["candidates"]):
        raise ValueError(f"{row['id']}: claimed screening exceeds exported candidates")


def query_groups(data, claims, problems, root):
    cutoff = iso(data.get("as_of"))
    if cutoff > date.today():
        raise ValueError("as_of is in the future")
    groups = {key: [] for key in claims}
    for key, row in records(data, "queries").items():
        required(row, "source formulation query status date operation", key)
        if row["operation"] not in ("search", "lookup", "read", "citation"):
            raise ValueError(f"{key}: invalid operation")
        claim_ids = reference_list(row, "claims", claims)
        if not claim_ids:
            raise ValueError(f"{key}: link query to at least one claim")
        day = iso(row["date"])
        if day > date.today():
            raise ValueError(f"{key}: query date in the future")
        channel = row.get("channel", "index")
        if channel not in ("index", "specialist", "preprint", "online_first", "citation"):
            raise ValueError(f"{key}: invalid channel")
        if row["status"] not in ("ok", "unavailable", "partial"):
            raise ValueError(f"{key}: invalid query status")
        check_search_receipt(row, root)
        if row["status"] == "unavailable":
            required(row, "error", key)
            if row.get("total") is not None or row.get("screened") not in (0, None):
                raise ValueError(f"{key}: failed request cannot establish hit counts")
            continue
        screened, total = row.get("screened"), row.get("total")
        if type(screened) is not int or screened < 0:
            raise ValueError(f"{key}: screened must be a nonnegative integer")
        if total is not None and (type(total) is not int or total < screened):
            raise ValueError(f"{key}: total smaller than screened or invalid")
        if row["status"] == "partial":
            required(row, "error", key)
            continue
        if row["operation"] != "search":
            continue
        if screened == 0 and total != 0:
            problems.append(f"{key}: results exist or count unknown, none screened")
        start = iso(row["from"]) if row.get("from") else None
        end = iso(row["to"]) if row.get("to") else None
        if (end and start and end < start) or (end and end > day):
            raise ValueError(f"{key}: invalid publication date interval")
        recent = (start is not None and half_year_before(cutoff) - timedelta(days=7)
                  <= start <= half_year_before(cutoff) and (end or day) == cutoff)
        earliest = start is None and (end == cutoff or (end is None and day <= cutoff))
        for claim in claim_ids:
            groups[claim].append((source_name(row["source"]), clean(row["formulation"]),
                                  clean(row["query"]), recent, earliest, channel))
    return groups


def inspect(data, root, fingerprint):
    problems = []
    claims, papers = records(data, "claims"), records(data, "papers")
    if not claims:
        problems.append("no claims")
    queries = query_groups(data, claims, problems, root)
    for key, row in papers.items():
        required(row, "title identifier identity reading locator", key)
        if row["identity"] not in ("verified", "unverified"):
            raise ValueError(f"{key}: invalid identity status")
        if row["reading"] not in ("original", "abstract", "metadata"):
            raise ValueError(f"{key}: invalid reading level")
    for key, claim in claims.items():
        required(claim, "text falsifier verdict reason", key)
        verdict = claim["verdict"]
        if verdict not in ("covered", "partial", "no_direct_match", "insufficient"):
            raise ValueError(f"{key}: invalid verdict")
        refs = reference_list(claim, "papers", papers)
        comparisons = claim.get("comparisons")
        if not isinstance(comparisons, dict) or set(comparisons) != set(refs):
            raise ValueError(f"{key}: provide one comparison for each decisive paper")
        relations = set()
        for paper_id, entry in comparisons.items():
            if not isinstance(entry, dict):
                raise ValueError(f"{key}/{paper_id}: expected comparison object")
            required(entry, "relation basis", f"{key}/{paper_id}")
            if entry["relation"] not in ("direct", "partial", "neighbor", "unknown"):
                raise ValueError(f"{key}/{paper_id}: invalid comparison")
            relations.add(entry["relation"])
        if verdict == "covered" and "direct" not in relations:
            problems.append(f"{key}: no named direct counterexample for covered claim")
        if verdict == "partial" and "partial" not in relations:
            problems.append(f"{key}: missing evidence for partial overlap")
        if "direct" in relations and verdict in ("partial", "no_direct_match"):
            problems.append(f"{key}: verdict conflicts with a direct counterexample")
        if "unknown" in relations:
            problems.append(f"{key}: unresolved comparison with decisive prior work")
        rows = queries[key]
        if len({r[0] for r in rows}) < 2:
            problems.append(f"{key}: fewer than two successful sources")
        if min(len({r[1] for r in rows}), len({r[2] for r in rows})) < 3:
            problems.append(f"{key}: fewer than three distinct successful search formulations")
        if not any(r[3] for r in rows) or not any(r[4] for r in rows):
            problems.append(f"{key}: missing current six-month or unrestricted search")
        if not any(r[3] and r[5] in ("preprint", "online_first") for r in rows):
            problems.append(f"{key}: missing recent preprint or online-first search")
        if not refs or any(papers[p]["identity"] != "verified" or
                           papers[p]["reading"] != "original" for p in refs):
            problems.append(f"{key}: decisive prior work lacks verified identity or original evidence")
        if verdict == "insufficient":
            problems.append(f"{key}: insufficient evidence for this claim")
    scope = data.get("scope")
    if not isinstance(scope, dict) or not isinstance(scope.get("critical_gaps"), list):
        raise ValueError("scope must include a critical_gaps array")
    for field in ("seed_check", "citation_chase", "stop_reason"):
        if not isinstance(scope.get(field), str) or not scope[field].strip():
            problems.append(f"scope: missing {field}")
    if scope["critical_gaps"]:
        problems.append("scope: unresolved issues can change the verdict")
    for item in ("protocol", "recall", "inventory", "screening"):
        if item not in scope["materials"]:
            problems.append(f"scope: missing supporting record for {item}")
    review = data.get("review")
    if not isinstance(review, dict):
        raise ValueError("review must be an object")
    if review.get("kind") not in ("different_family", "independent_human", "same_family_fresh",
                                  "self", "unavailable", ""):
        raise ValueError("unknown reviewer kind")
    if review.get("kind") in ("different_family", "independent_human", "same_family_fresh"):
        required(review, "reviewer trace_file evidence_digest", "review")
        fields_file(root, review["trace_file"])
        reviewed = reference_list(dict(review, id="review"), "reviewed_claims", claims)
        if review.get("complete") is not True or set(reviewed) != set(claims):
            problems.append("review: incomplete or missing claim-level review")
        if review["evidence_digest"] != fingerprint:
            problems.append("review: evidence changed since review")
        if review["kind"] == "different_family":
            required(review, "author_family reviewer_family", "review")
            if clean(review["author_family"]) == clean(review["reviewer_family"]):
                problems.append("review: recorded author and reviewer families are identical")
    if review.get("kind") not in ("different_family", "independent_human"):
        problems.append("review: independent human or verified different-family review missing")
    return problems


def reviewer_brief(data, fingerprint):
    claims = []
    for row in records(data, "claims").values():
        required(row, "text falsifier", row["id"])
        claims.append({key: row[key] for key in ("id", "text", "falsifier")})
    return {
        "as_of": data["as_of"], "evidence_digest": fingerprint, "claims": claims,
        "queries": data["queries"], "papers": data["papers"],
        "supporting_files": data["scope"]["materials"],
        "questions": [
            "Name the strongest counterexample for each claim and locate the original evidence.",
            "Distinguish equivalent mechanisms, changed conditions and different observables.",
            "Identify the delta that survives, the limits of the search and the claims actually reviewed.",
        ],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["init", "fingerprint", "brief", "check"])
    parser.add_argument("file", type=Path, help="case dossier JSON file")
    args = parser.parse_args(argv)
    path = args.file.resolve()
    try:
        if args.command == "init":
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("x", encoding="utf-8") as stream:
                json.dump(initial(), stream, ensure_ascii=False, indent=2)
                stream.write("\n")
            return 0
        data = json.loads(path.read_text(encoding="utf-8-sig"))
        fingerprint = digest(data, path.parent)
        if args.command == "brief":
            print(json.dumps(reviewer_brief(data, fingerprint), indent=2, ensure_ascii=False))
            return 0
        if args.command == "fingerprint":
            print(fingerprint)
            return 0
        issues = inspect(data, path.parent, fingerprint)
        print("LIMITED" if issues else "RECORDED CHECKS PASSED")
        for issue in issues:
            print(f"- {issue}")
        return int(bool(issues))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"Invalid dossier: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
