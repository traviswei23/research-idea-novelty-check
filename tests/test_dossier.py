"""Regression checks for premature or stale novelty decisions. All records here are fictional."""

import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_dossier import digest, initial, inspect, main, reviewer_brief  # noqa: E402


class DossierTests(unittest.TestCase):
    def setUp(self):
        folder = tempfile.TemporaryDirectory()
        self.addCleanup(folder.cleanup)
        self.root = Path(folder.name).resolve()
        for name in ("notes", "raw", "receipt", "log"):
            (self.root / name).write_text(f"Fictional fixture {name}", encoding="utf-8")
        self.data = initial()
        self.data.update(as_of="2024-11-30", claims=[{
            "id": "C1", "text": "Example comparison", "falsifier": "An earlier comparison",
            "verdict": "covered", "reason": "Earlier comparison found", "papers": ["P1"],
            "comparisons": {"P1": {"relation": "direct", "basis": "Same scope and outcome"}},
        }], papers=[{"id": "P1", "title": "Fixture", "identifier": "fixture:1",
                     "identity": "verified", "reading": "original", "locator": "Figure 2",
                     "evidence_file": "notes"}])
        for index, source in enumerate(("Crossref", "OpenAlex", "Crossref"), start=1):
            self.data["queries"].append({
                "id": f"Q{index}", "source": source, "date": "2024-11-30", "status": "ok",
                "formulation": f"Strategy {index}", "query": f"Term {index}", "claims": ["C1"],
                "from": "2024-05-30" if index == 3 else None, "to": None, "screened": 1,
                "total": 1, "trace_file": "raw", "channel": "preprint" if index == 3 else "index",
            })
        self.data["scope"].update(seed_check="S1 found", citation_chase="P1 references checked",
                                  stop_reason="Verified direct counterexample",
                                  materials=dict.fromkeys(("protocol", "recall", "inventory",
                                                           "screening"), "log"))
        self.data["review"].update(kind="different_family", reviewer="Synthetic reviewer",
                                   author_family="Model A", reviewer_family="Model B",
                                   trace_file="receipt", reviewed_claims=["C1"], complete=True)
        self.sign()

    def sign(self):
        self.data["review"]["evidence_digest"] = digest(self.data, self.root)

    def issues(self):
        return "\n".join(inspect(self.data, self.root, digest(self.data, self.root)))

    def test_adequately_recorded_control(self):
        self.assertEqual(self.issues(), "")

    def test_reviewer_brief_omits_author_verdict_and_review(self):
        brief = reviewer_brief(self.data, digest(self.data, self.root))
        self.assertNotIn("review", brief)
        self.assertNotIn("verdict", brief["claims"][0])
        self.assertNotIn("comparisons", brief["claims"][0])
        self.assertEqual(brief["papers"][0]["evidence_file"], "notes")

    def test_refuses_to_overwrite_case_and_rejects_invalid_json(self):
        file = self.root / "case.json"
        with contextlib.redirect_stderr(io.StringIO()), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(main(["init", str(file)]), 0)
            self.assertEqual(main(["check", str(file)]), 1)
            self.assertEqual(main(["init", str(file)]), 2)
            file.write_text("bad JSON", encoding="utf-8")
            self.assertEqual(main(["check", str(file)]), 2)

    def test_changed_excerpt_stales_review_with_same_identifier(self):
        (self.root / "notes").write_text("Figure corrected: absolute error", encoding="utf-8")
        self.assertIn("evidence changed", self.issues())

    def test_changed_screening_stales_review(self):
        (self.root / "log").write_text("Eligibility correction", encoding="utf-8")
        self.assertIn("evidence changed", self.issues())

    def test_failed_query_is_not_a_zero_and_cannot_cover_second_source(self):
        query = self.data["queries"][1]
        query.update(status="unavailable", error="rate limited", total=None, screened=0)
        self.assertIn("two successful sources", self.issues())
        query.update(total=0)
        with self.assertRaises(ValueError):
            self.issues()

    def test_genuine_zero_is_allowed(self):
        self.data["queries"][1].update(total=0, screened=0)
        self.sign()
        self.assertEqual(self.issues(), "")

    def test_record_must_match_saved_provider_receipt(self):
        row = self.data["queries"][1]
        row.update(trace_file="query.json", total=0, screened=0)
        receipt = {"action": "search", "parameters": {"public_query": row["query"]},
                   "providers": {"openalex": {"status": "zero_hits", "provider_total_hits": 0,
                                             "candidates": []}}}
        (self.root / "query.json").write_text(json.dumps(receipt), encoding="utf-8")
        self.sign()
        self.assertEqual(self.issues(), "")
        row.update(total=1)
        with self.assertRaisesRegex(ValueError, "disagrees with search receipt"):
            self.issues()

    def test_unread_hits_do_not_count_as_screening(self):
        self.data["queries"][1].update(total=4, screened=0)
        self.assertIn("none screened", self.issues())

    def test_current_index_search_cannot_stand_in_for_preprint_coverage(self):
        self.data["queries"][2]["channel"] = "index"
        self.assertIn("online-first", self.issues())

    def test_historical_search_can_be_executed_later(self):
        self.data["queries"][2].update(date="2024-12-01", to="2024-11-30")
        self.sign()
        self.assertEqual(self.issues(), "")

    def test_abstract_only_or_unverified_limits_claim(self):
        self.data["papers"][0].update(reading="abstract")
        self.assertIn("original evidence", self.issues())
        self.data["papers"][0].update(reading="original", identity="unverified")
        self.assertIn("verified identity", self.issues())

    def test_critical_gap_or_missing_recall_limits_case(self):
        self.data["scope"]["critical_gaps"] = ["P2 supplement could change C1"]
        self.assertIn("unresolved issues", self.issues())
        del self.data["scope"]["materials"]["recall"]
        self.assertIn("supporting record for recall", self.issues())

    def test_proximity_cannot_reject(self):
        self.data["claims"][0]["comparisons"]["P1"]["relation"] = "neighbor"
        self.assertIn("no named direct counterexample", self.issues())

    def test_direct_match_conflicts_with_negative_verdict(self):
        self.data["claims"][0]["verdict"] = "no_direct_match"
        self.assertIn("conflicts with a direct counterexample", self.issues())

    def test_repeated_queries_single_index_and_short_window(self):
        rows = self.data["queries"]
        rows[1].update(source="Crossref API", query=" TERM 1 ")
        rows[2].update(**{"from": "2024-11-01"})
        issues = self.issues()
        for phrase in ("two successful sources", "three distinct", "six-month"):
            self.assertIn(phrase, issues)

    def test_self_same_family_and_unavailable_do_not_pass_full_review(self):
        for kind in ("self", "same_family_fresh", "unavailable"):
            self.data["review"]["kind"] = kind
            self.assertIn("different-family review missing", self.issues())
        self.data["review"].update(kind="different_family", reviewer_family="model a")
        self.assertIn("families are identical", self.issues())

    def test_partial_reviewer_reply_cannot_certify_all_claims(self):
        self.data["review"].update(reviewed_claims=[], complete=False)
        self.assertIn("missing claim-level review", self.issues())

    def test_path_escape_and_missing_references_fail(self):
        self.data["papers"][0]["evidence_file"] = "../elsewhere"
        with self.assertRaises(ValueError):
            self.issues()
        self.data["papers"][0]["evidence_file"] = "notes"
        self.data["claims"][0]["papers"] = ["P404"]
        with self.assertRaises(ValueError):
            self.issues()


if __name__ == "__main__":
    unittest.main()
