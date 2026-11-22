#!/usr/bin/env python3
"""Search published metadata and verify identifiers. Python 3.8+, standard library.

Send only de-identified, public search terms using --public-query. No input
files or workspace context are read. In verify mode only the ID is transmitted;
the optional expected title is compared locally. An OpenAlex key, when available,
is read from OPENALEX_API_KEY. JSON output contains public request URLs only.
"""

import argparse
import json
import os
import re
import sys
import time
import unicodedata
from datetime import date, datetime, timezone
from difflib import SequenceMatcher
from email.utils import parsedate_to_datetime
from http.client import HTTPException
from html.parser import HTMLParser
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import quote, quote_plus, unquote, urlencode, urlsplit
from urllib.request import HTTPRedirectHandler, Request, build_opener


APIS = {
    "crossref": "https://api.crossref.org/works",
    "openalex": "https://api.openalex.org/works",
}
UA = "ResearchIdeaNoveltyCheck/1.0 (public bibliographic metadata client)"
MAX_BYTES = 16 * 1024 * 1024
RETRIES = 2
RETRYABLE = {408, 429, 500, 502, 503, 504}
DOI = re.compile(r"10\.\d{4,9}/[^\s\x00-\x1f\x7f]+", re.IGNORECASE)
WID = re.compile(r"W\d+", re.IGNORECASE)


def utc_now():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def iso_day(text):
    try:
        value = date.fromisoformat(text)
    except ValueError:
        raise argparse.ArgumentTypeError("expected a valid date in YYYY-MM-DD format") from None
    if value.isoformat() != text:
        raise argparse.ArgumentTypeError("expected YYYY-MM-DD")
    return text


def id_value(raw):
    text = raw.strip()
    if text.lower().startswith(("https://", "http://")):
        p = urlsplit(text)
        if p.hostname not in {"doi.org", "dx.doi.org", "openalex.org", "www.openalex.org"}:
            raise ValueError("Expected a doi.org or openalex.org identifier URL.")
        if p.query or p.fragment:
            raise ValueError("Remove query parameters or fragments from identifier URLs.")
        text = unquote(p.path.lstrip("/"))
        if p.hostname.endswith("openalex.org") and not WID.fullmatch(text):
            raise ValueError("Expected an OpenAlex W identifier.")
    elif text.lower().startswith("doi:"):
        text = text[4:].strip()
    if DOI.fullmatch(text):
        return "doi", text.lower()
    if WID.fullmatch(text):
        return "openalex", text.upper()
    raise ValueError("Expected DOI, doi.org URL or OpenAlex W identifier.")


def optional_id(value):
    try:
        return id_value(value)[1] if isinstance(value, str) else None
    except ValueError:
        return None


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.text = []

    def handle_data(self, data):
        self.text.append(data)


def plain_title(value):
    p = VisibleText()
    p.feed(value or "")
    p.close()
    return " ".join("".join(p.text).split())


def title_key(title):
    text = unicodedata.normalize("NFKC", title).casefold()
    # Keep mathematical operators and digits, both of which can change the paper.
    return " ".join("".join(" " if unicodedata.category(c).startswith("P")
                             else c for c in text).split())


def title_result(expected, actual):
    if not expected:
        return {"status": "not_requested"}
    left, right = title_key(plain_title(expected)), title_key(actual)
    if not left or not right:
        return {"status": "unverified", "reason": "missing_title"}
    if left == right:
        return {"status": "normalized_match"}
    return {"status": "title_differs_review_needed",
            "similarity_diagnostic": round(SequenceMatcher(None, left, right, autojunk=False).ratio(), 3)}


class NoRedirect(HTTPRedirectHandler):
    # Requests can carry an api_key; never forward that query to another host.
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


class Failure(Exception):
    def __init__(self, kind, code=None):
        super().__init__(kind)
        self.kind = kind
        self.code = code

    def record(self):
        info = {"reason": self.kind}
        if self.code is not None:
            info["http_status"] = self.code
        return info


def retry_wait(value, attempt):
    if not value:
        return 1.0 + attempt
    try:
        seconds = float(value)
    except (ValueError, OverflowError):
        try:
            seconds = parsedate_to_datetime(value).timestamp() - time.time()
        except (TypeError, ValueError, OverflowError):
            return 1.0 + attempt
    return max(0.0, seconds)


class Client:
    def __init__(self, name, timeout):
        self.name = name
        self.timeout = timeout
        self.log = []
        self.opener = build_opener(NoRedirect())
        self.last_request = 0.0

    def get(self, path="", params=None):
        params = dict(params or {})
        public = APIS[self.name] + path
        clean_url = public + ("?" + urlencode(params) if params else "")
        if self.name == "openalex" and os.getenv("OPENALEX_API_KEY"):
            params["api_key"] = os.environ["OPENALEX_API_KEY"]
        target = public + ("?" + urlencode(params) if params else "")
        for attempt in range(RETRIES + 1):
            time.sleep(max(0, self.last_request + 0.3 - time.monotonic()))
            self.last_request = time.monotonic()
            event = {"time_utc": utc_now(), "url": clean_url, "attempt": attempt + 1}
            self.log.append(event)
            delay = 1.0 + attempt
            req = Request(target, headers={"User-Agent": UA, "Accept": "application/json"})
            try:
                with self.opener.open(req, timeout=self.timeout) as res:
                    event["http_status"] = res.status
                    buf = res.read(MAX_BYTES + 1)
                if len(buf) > MAX_BYTES:
                    raise Failure("response_too_large")
                value = json.loads(buf)
                if not isinstance(value, dict):
                    raise Failure("unexpected_response")
                return value
            except HTTPError as exc:
                event["http_status"] = exc.code
                delay = retry_wait(exc.headers.get("Retry-After"), attempt)
                code = exc.code
                exc.close()
                kind = {401: "authentication_required", 403: "access_denied",
                        404: "not_found", 429: "rate_limited"}.get(code, "http_error")
                failure = Failure(kind, code)
                if code not in RETRYABLE or delay > 12:
                    raise failure from None
            except (URLError, OSError, HTTPException):
                failure = Failure("network_or_timeout")
            except (ValueError, UnicodeError):
                raise Failure("invalid_json") from None
            if attempt == RETRIES:
                raise failure from None
            time.sleep(delay)


def metadata(source, item):
    if not isinstance(item, dict):
        raise Failure("unexpected_record")
    if source == "crossref":
        titles = item.get("title", [])
        title = titles[0] if isinstance(titles, list) and titles else ""
        parts = (item.get("published") or {}).get("date-parts") or [[]]
        year = parts[0][0] if parts and parts[0] else None
        doi = optional_id(item.get("DOI"))
        wid = None
    else:
        title = item.get("display_name") or item.get("title") or ""
        year = item.get("publication_year")
        doi = optional_id(item.get("doi"))
        wid = optional_id(item.get("id"))
    return {"title": plain_title(title), "year": year, "doi": doi,
            "openalex_id": wid, "doi_url": "https://doi.org/" + quote(doi, safe="/") if doi else None,
            "openalex_url": "https://openalex.org/" + wid if wid else None}


def search(client, args):
    found = {"status": "failed", "provider_total_hits": None, "records_inspected": 0,
             "candidates": [], "requests": client.log}
    page_size = min(args.page_size, args.limit)
    page = 1
    seen = set()
    pages_seen = set()
    # Offset-based rankings can overlap during a query. Allow a little extra
    # paging to fill the requested unique sample, but keep network work bounded.
    page_budget = (args.limit + page_size - 1) // page_size + 2
    while len(found["candidates"]) < args.limit:
        offset = (page - 1) * page_size
        params = ({"query.bibliographic": args.public_query, "rows": page_size, "offset": offset,
                   "select": "DOI,title,published"}
                  if client.name == "crossref" else
                  {"search": args.public_query, "per_page": page_size, "page": page,
                   "select": "id,doi,display_name,publication_year"})
        date_fields = (("from-pub-date", "until-pub-date") if client.name == "crossref"
                       else ("from_publication_date", "to_publication_date"))
        filters = [field + ":" + day for field, day in
                   zip(date_fields, (args.from_date, args.until_date)) if day]
        if filters:
            params["filter"] = ",".join(filters)
        try:
            data = client.get(params=params)
            if client.name == "crossref":
                records = data["message"]["items"]
                total = data["message"]["total-results"]
            else:
                records = data["results"]
                total = data["meta"]["count"]
            if not isinstance(records, list) or type(total) is not int or total < 0:
                raise Failure("unexpected_search_response")
            if total == 0 and (records or page != 1):
                raise Failure("inconsistent_total")
            if page == 1:
                found["provider_total_hits"] = total
            page_ids = []
            for row in records:
                candidate = metadata(client.name, row)
                found["records_inspected"] += 1
                identity = candidate["openalex_id"] or candidate["doi"]
                if identity is None:
                    raise Failure("missing_record_identifier")
                page_ids.append(identity)
                if identity in seen:
                    continue
                seen.add(identity)
                found["candidates"].append(candidate)
                if len(found["candidates"]) == args.limit:
                    break
            if len(found["candidates"]) == args.limit:
                break
            if len(records) < page_size and offset + len(records) < total:
                raise Failure("incomplete_page")
            if page_ids and tuple(page_ids) in pages_seen:
                raise Failure("repeated_page")
            pages_seen.add(tuple(page_ids))
            if offset + len(records) >= total:
                break
            if page >= page_budget:
                raise Failure("page_budget_exhausted")
        except (Failure, KeyError, TypeError, AttributeError, IndexError) as exc:
            found["error"] = exc.record() if isinstance(exc, Failure) else {"reason": "unexpected_schema"}
            found["status"] = "partial" if found["candidates"] else "failed"
            return found
        page += 1
    found["status"] = "zero_hits" if found["provider_total_hits"] == 0 else "ok"
    return found


def verify(client, kind, identifier, expected_title):
    result = {"status": "unverified", "requests": client.log}
    if client.name == "crossref" and kind == "openalex":
        result["reason"] = "openalex_id_not_supported_by_crossref"
        return result
    lookup = identifier if kind == "openalex" or client.name == "crossref" else "https://doi.org/"+identifier
    try:
        data = client.get(path="/"+quote(lookup, safe="/:" if client.name == "openalex" else "/"))
        row = metadata(client.name, data["message"] if client.name == "crossref" else data)
    except (Failure, KeyError, TypeError, AttributeError, IndexError) as exc:
        result["error"] = exc.record() if isinstance(exc, Failure) else {"reason": "unexpected_schema"}
        return result
    result["record"] = row
    actual = row["doi"] if kind == "doi" else row["openalex_id"]
    result["identifier_matches"] = actual == identifier
    result["title_comparison"] = title_result(expected_title, row["title"])
    if not result["identifier_matches"]:
        result["reason"] = "returned_id_differs"
    elif result["title_comparison"]["status"] == "normalized_match":
        result["status"] = "id_and_title_match"
    elif expected_title:
        result["reason"] = "title_unverified_or_differs"
    else:
        result["status"] = "id_resolved_title_unchecked"
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    s = sub.add_parser("search", help="send only the supplied PUBLIC query to selected providers")
    s.add_argument("--public-query", required=True, help="public terms only, never a private research brief")
    s.add_argument("--limit", type=int, default=10, help="maximum candidates per provider (1–200)")
    s.add_argument("--page-size", type=int, default=25, help="records per API page (1–100)")
    s.add_argument("--from-date", type=iso_day, help="inclusive publication date, YYYY-MM-DD")
    s.add_argument("--until-date", type=iso_day, help="inclusive publication date, YYYY-MM-DD")
    v = sub.add_parser("verify", help="resolve a DOI or W identifier; compare an optional title locally")
    v.add_argument("--id", required=True)
    v.add_argument("--title", help="expected published title, compared locally")
    for cmd in (s, v):
        cmd.add_argument("--source", choices=("both", "crossref", "openalex"), default="both")
        cmd.add_argument("--timeout", type=float, default=15, help="per-request timeout in seconds")
        cmd.add_argument("--output", type=Path, help="write JSON to this path; default is stdout")
    args = parser.parse_args()
    if not 0.5 <= args.timeout <= 120:
        parser.error("--timeout must be between 0.5 and 120 seconds")
    if args.action == "search":
        args.public_query = args.public_query.strip()
        if not 1 <= args.limit <= 200 or not 1 <= args.page_size <= 100 or not args.public_query:
            parser.error("supply a nonempty public query, limit 1–200 and page size 1–100")
        if args.from_date and args.until_date and args.from_date > args.until_date:
            parser.error("--from-date must not follow --until-date")
        parameters = {"public_query": args.public_query, "limit_per_provider": args.limit,
                      "page_size": args.page_size, "from_date": args.from_date,
                      "until_date": args.until_date}
    else:
        try:
            kind, identifier = id_value(args.id)
        except ValueError as exc:
            parser.error(str(exc))
        parameters = {"id": identifier, "expected_title_local": args.title}
    key = os.environ.get("OPENALEX_API_KEY") or ""
    if key and any(key in val for val in parameters.values() if isinstance(val, str)):
        parser.error("credential found in input; remove it before continuing")
    report = {"action": args.action, "parameters": parameters, "started_utc": utc_now(),
              "scope": "bibliographic metadata only", "providers": {}}
    start = time.monotonic()
    providers = tuple(APIS) if args.source == "both" else (args.source,)
    for provider in providers:
        client = Client(provider, args.timeout)
        result = (search(client, args) if args.action == "search"
                  else verify(client, kind, identifier, args.title))
        if args.action == "search":
            result["candidate_count"] = len(result["candidates"])
        report["providers"][provider] = result
    report["finished_utc"] = utc_now()
    report["elapsed_seconds"] = round(time.monotonic()-start, 3)
    output = json.dumps(report, indent=2, ensure_ascii=False)
    if key:
        for form in {key, quote(key, safe=""), quote_plus(key)}:
            output = output.replace(form, "[REDACTED]")
    if args.output:
        args.output.write_text(output + "\n", encoding="utf-8")
    else:
        if hasattr(sys.stdout, "reconfigure"):
            sys.stdout.reconfigure(encoding="utf-8")
        print(output)
    successful = {"ok", "zero_hits", "id_and_title_match", "id_resolved_title_unchecked"}
    return 0 if all(r["status"] in successful for r in report["providers"].values()) else 2


if __name__ == "__main__":
    sys.exit(main())
