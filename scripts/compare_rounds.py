"""Freeze a small evidence index or compare a new novelty dossier with an earlier index."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

from check_dossier import digest, fields_file, inspect, records


def signature(value):
    value = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def checkpoint(file):
    root = file.resolve().parent
    data = json.loads(file.read_text(encoding="utf-8-sig"))
    fingerprint = digest(data, root)
    issues = inspect(data, root, fingerprint)
    cache = {}

    def attachment(name):
        if name not in cache:
            cache[name] = hashlib.sha256(fields_file(root, name)).hexdigest()
        return cache[name]

    papers = {key: signature([p, attachment(p["evidence_file"])])
              for key, p in records(data, "papers").items()}
    queries = records(data, "queries")
    state = {}
    for key, claim in records(data, "claims").items():
        state[key] = {
            "definition": [claim["text"], claim["falsifier"]],
            "verdict": claim["verdict"],
            "rationale": signature([claim["reason"], claim["comparisons"]]),
            "papers": {p: papers[p] for p in claim["papers"]},
            "queries": {q: signature([row, attachment(row["trace_file"])])
                        for q, row in queries.items() if key in row["claims"]},
        }
    scope = data["scope"]
    return {"format": "novelty-round-1", "as_of": data["as_of"], "evidence_digest": fingerprint,
            "claims": state, "scope": signature([scope, {k: attachment(v)
                                                      for k, v in scope["materials"].items()}]),
            "issues": issues, "review": data["review"].get("kind", "")}


def changed_keys(a, b):
    return sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k))


def compare(old, new):
    if not isinstance(old, dict) or old.get("format") != "novelty-round-1":
        raise ValueError("expected a checkpoint made by the snapshot command")
    past, now = old["claims"], new["claims"]
    report = []
    for key in sorted(set(past) | set(now)):
        if key not in past or key not in now:
            report.append({"id": key, "event": "added" if key in now else "removed"})
            continue
        a, b = past[key], now[key]
        papers = changed_keys(a["papers"], b["papers"])
        queries = changed_keys(a["queries"], b["queries"])
        if a["definition"] != b["definition"]:
            event = "scope_changed"
        elif papers:
            event = "prior_evidence_changed"
        elif a["verdict"] != b["verdict"] or a["rationale"] != b["rationale"]:
            event = "judgment_changed"
        elif queries:
            event = "search_changed"
        else:
            event = "unchanged"
        report.append({"id": key, "event": event, "previous_verdict": a["verdict"],
                       "current_verdict": b["verdict"], "affected_papers": papers,
                       "affected_queries": queries})
    return {"previous": old["evidence_digest"], "current": new["evidence_digest"], "claims": report,
            "scope_or_material_changed": old["scope"] != new["scope"],
            "current_review": new["review"], "current_limits": new["issues"]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    save = commands.add_parser("snapshot", help="create an immutable-by-convention checkpoint; refuses overwrite")
    save.add_argument("dossier", type=Path)
    save.add_argument("output", type=Path)
    diff = commands.add_parser("compare", help="show evidence, scope and verdict changes for every claim")
    diff.add_argument("previous", type=Path)
    diff.add_argument("dossier", type=Path)
    args = parser.parse_args()
    try:
        state = checkpoint(args.dossier)
        if args.command == "snapshot":
            with args.output.open("x", encoding="utf-8") as stream:
                json.dump(state, stream, ensure_ascii=False, indent=2)
                stream.write("\n")
        else:
            previous = json.loads(args.previous.read_text(encoding="utf-8-sig"))
            print(json.dumps(compare(previous, state), ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, TypeError, KeyError) as err:
        print(f"Invalid round: {err}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
