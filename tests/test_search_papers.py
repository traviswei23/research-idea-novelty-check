"""Offline CLI regression tests for both provider adapters and their request log."""

import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import ExitStack, redirect_stderr, redirect_stdout
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from unittest.mock import Mock, patch
from urllib.error import HTTPError
from urllib.parse import parse_qs, quote_plus, urlsplit


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "search_papers.py"
SPEC = spec_from_file_location("search_papers", SCRIPT)
papers = module_from_spec(SPEC)
SPEC.loader.exec_module(papers)


class Response(io.BytesIO):
    status = 200


def work(provider, number):
    doi = "10.1234/fixture" + str(number)
    title = "Wave measurement " + str(number)
    if provider == "crossref":
        return {"DOI": doi, "title": [title], "published": {"date-parts": [[2024, 2, 29]]}}
    return {"doi": "https://doi.org/" + doi, "id": "https://openalex.org/W"+str(number),
            "display_name": title, "publication_year": 2024}


def page(provider, total, numbers):
    records = [work(provider, n) for n in numbers]
    if provider == "crossref":
        return {"message": {"items": records, "total-results": total}}
    return {"results": records, "meta": {"count": total}}


class SearchPapersCLI(unittest.TestCase):
    def setUp(self):
        self.scratch = tempfile.TemporaryDirectory()
        self.addCleanup(self.scratch.cleanup)
        self.output = Path(self.scratch.name) / "result.json"

    def invoke(self, args, replies, key=""):
        requests = []
        queued = {name: list(payloads) for name, payloads in replies.items()}

        def respond(req, timeout):
            requests.append(req)
            host = urlsplit(req.full_url).hostname
            name = {"api.crossref.org": "crossref", "api.openalex.org": "openalex"}[host]
            payload = queued[name].pop(0)
            if isinstance(payload, int):
                raise HTTPError(req.full_url, payload, "fixture error", {"Retry-After": "0"}, None)
            if isinstance(payload, bytes):
                return Response(payload)
            return Response(json.dumps(payload).encode())

        opener = Mock()
        opener.open.side_effect = respond
        with ExitStack() as context:
            context.enter_context(patch.object(sys, "argv", ["search_papers.py"] + args + ["--output", str(self.output)]))
            context.enter_context(patch.dict(os.environ, {"OPENALEX_API_KEY": key}))
            context.enter_context(patch.object(papers, "build_opener", return_value=opener))
            context.enter_context(patch.object(papers.time, "sleep"))
            context.enter_context(redirect_stdout(io.StringIO()))
            context.enter_context(redirect_stderr(io.StringIO()))
            status = papers.main()
        self.assertTrue(all(not rest for rest in queued.values()), "fixture replies left over")
        return status, json.loads(self.output.read_text(encoding="utf-8")), requests

    def search(self, name, pages, *args, key=""):
        flags = ["search", "--public-query", "waves", "--source", name, *args]
        rc, result, requests = self.invoke(flags, {name: pages}, key)
        return rc, result["providers"][name], requests

    def test_both_providers_zero_hits_and_one_day_publication_filter(self):
        rc, result, requests = self.invoke(
            ["search", "--public-query", "waves", "--from-date", "2024-02-29",
             "--until-date", "2024-02-29"],
            {name: [page(name, 0, [])] for name in papers.APIS})
        self.assertEqual(rc, 0)
        expected_filters = {
            "crossref": "from-pub-date:2024-02-29,until-pub-date:2024-02-29",
            "openalex": "from_publication_date:2024-02-29,to_publication_date:2024-02-29"}
        for name, req in zip(papers.APIS, requests):
            record = result["providers"][name]
            self.assertEqual(record["status"], "zero_hits")
            self.assertEqual((record["provider_total_hits"], record["records_inspected"],
                              record["candidate_count"]), (0, 0, 0))
            self.assertEqual(parse_qs(urlsplit(req.full_url).query)["filter"], [expected_filters[name]])

    def test_zero_with_records_positive_with_no_records_and_invalid_responses(self):
        for name in papers.APIS:
            for payload, kind in [(page(name, 0, [1]), "inconsistent_total"),
                                  (page(name, 4, []), "incomplete_page"),
                                  (page(name, False, []), "unexpected_search_response"),
                                  ({}, "unexpected_schema"), (b"html", "invalid_json")]:
                with self.subTest(provider=name, kind=kind):
                    rc, record, _ = self.search(name, [payload])
                    self.assertEqual(rc, 2)
                    self.assertEqual(record["status"], "failed")
                    self.assertEqual(record["error"]["reason"], kind)
                    self.assertEqual(record["candidate_count"], 0)

    def test_short_page_with_records_keeps_them_and_marks_partial(self):
        for name in papers.APIS:
            with self.subTest(provider=name):
                rc, record, _ = self.search(name, [page(name, 10, [1])], "--page-size", "2")
                self.assertEqual((rc, record["status"]), (2, "partial"))
                self.assertEqual(record["error"]["reason"], "incomplete_page")
                self.assertEqual(record["candidates"][0]["doi"], "10.1234/fixture1")

    def test_failed_next_page_and_exhausted_retries_do_not_discard_first_page(self):
        for name in papers.APIS:
            with self.subTest(provider=name):
                rc, record, _ = self.search(name, [page(name, 8, [1]), 503, 503, 503],
                                            "--limit", "2", "--page-size", "1")
                self.assertEqual((rc, record["status"], record["candidate_count"]), (2, "partial", 1))
                self.assertEqual(record["records_inspected"], 1)
                self.assertEqual(record["candidates"][0]["doi"], "10.1234/fixture1")
                self.assertEqual([r["http_status"] for r in record["requests"]], [200, 503, 503, 503])

    def test_overlap_then_retry_same_page_and_fill_with_unique_candidates(self):
        for name in papers.APIS:
            with self.subTest(provider=name):
                replies = [page(name, 8, [1, 2]), 429, page(name, 8, [2, 3]), page(name, 8, [4, 5])]
                rc, record, requests = self.search(name, replies, "--limit", "4", "--page-size", "2")
                self.assertEqual((rc, record["status"]), (0, "ok"))
                self.assertEqual([c["doi"] for c in record["candidates"]],
                                 ["10.1234/fixture"+str(n) for n in range(1, 5)])
                self.assertEqual(record["records_inspected"], 5)
                params = [parse_qs(urlsplit(r.full_url).query) for r in requests]
                field = "offset" if name == "crossref" else "page"
                values = [q[field][0] for q in params]
                self.assertEqual(values, ["0", "2", "2", "4"] if name == "crossref"
                                 else ["1", "2", "2", "3"])

    def test_repeated_page_is_not_full_coverage(self):
        for name in papers.APIS:
            rc, record, _ = self.search(name, [page(name, 6, [1]), page(name, 6, [1])],
                                        "--limit", "2", "--page-size", "1")
            self.assertEqual((rc, record["status"], record["candidate_count"]), (2, "partial", 1))
            self.assertEqual(record["error"]["reason"], "repeated_page")

    def test_verify_checks_title_locally_and_treats_wrong_title_as_unverified(self):
        for name in papers.APIS:
            with self.subTest(provider=name):
                row = work(name, 123)
                payload = {"message": row} if name == "crossref" else row
                for title, status, rc in [("Wave measurement 123", "id_and_title_match", 0),
                                          ("Incorrect expected title", "unverified", 2)]:
                    actual, result, requests = self.invoke(
                        ["verify", "--source", name, "--id", "10.1234/fixture123", "--title", title],
                        {name: [payload]})
                    self.assertEqual((actual, result["providers"][name]["status"]), (rc, status))
                    self.assertNotIn("title", requests[0].full_url)
                    self.assertFalse(urlsplit(requests[0].full_url).query)

    def test_unresolved_id_is_not_a_content_result(self):
        rc, result, _ = self.invoke(["verify", "--id", "W123", "--source", "openalex"],
                                    {"openalex": [404]})
        self.assertEqual((rc, result["providers"]["openalex"]["status"]), (2, "unverified"))
        self.assertEqual(result["providers"]["openalex"]["error"]["reason"], "not_found")

    def test_key_is_sent_only_in_openalex_request_and_does_not_escape_on_failure(self):
        key = "synthetic+token/? suffix"
        rc, result, requests = self.invoke(["search", "--public-query", "waves"],
                                           {"crossref": [page("crossref", 0, [])], "openalex": [403]}, key)
        self.assertEqual(rc, 2)
        self.assertNotIn("api_key", requests[0].full_url)
        self.assertEqual(parse_qs(urlsplit(requests[1].full_url).query)["api_key"], [key])
        raw = self.output.read_text(encoding="utf-8")
        for forbidden in ("api_key", key, quote_plus(key)):
            self.assertNotIn(forbidden, raw)
        failed = result["providers"]["openalex"]
        self.assertEqual(failed["status"], "failed")
        self.assertIsNone(failed["provider_total_hits"])
        self.assertEqual(failed["error"]["http_status"], 403)

    def test_invalid_dates_are_rejected_before_network(self):
        for dates in (["--from-date", "2023-02-29"],
                      ["--from-date", "2024-03-01", "--until-date", "2024-02-29"]):
            with self.subTest(dates=dates), self.assertRaises(SystemExit) as err:
                self.invoke(["search", "--public-query", "waves", *dates], {})
            self.assertEqual(err.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
