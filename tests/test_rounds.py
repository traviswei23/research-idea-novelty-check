"""Round-to-round decisions must distinguish claim changes from unchanged identifiers."""
import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from check_dossier import initial
from compare_rounds import checkpoint, compare


class RoundTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.file = self.root / "dossier.json"
        self.note = self.root / "card.md"
        self.note.write_text("Original figure reading", encoding="utf-8")
        self.data = initial()
        self.data.update(papers=[{"id": "P1", "title": "Demonstration study",
                                   "identifier": "example", "identity": "verified", "reading": "original",
                                   "locator": "Figure 1", "evidence_file": "card.md"}],
                         claims=[{"id": "C1", "text": "A demonstration claim", "falsifier": "An earlier trial",
                                  "reason": "Original scope", "verdict": "partial", "papers": ["P1"],
                                  "comparisons": {"P1": {"relation": "partial", "basis": "Different output"}}}])
        self.before = self.state()

    def state(self):
        self.file.write_text(json.dumps(self.data), encoding="utf-8")
        return checkpoint(self.file)

    def test_same_id_and_file_new_reading(self):
        self.note.write_text("Corrected figure reading", encoding="utf-8")
        row = compare(self.before, self.state())["claims"][0]
        self.assertEqual((row["event"], row["affected_papers"]), ("prior_evidence_changed", ["P1"]))

    def test_scope_and_rationale_are_different_events(self):
        self.data["claims"][0]["reason"] = "New interpretation"
        self.assertEqual(compare(self.before, self.state())["claims"][0]["event"], "judgment_changed")
        self.data["claims"][0]["text"] = "New observable"
        self.assertEqual(compare(self.before, self.state())["claims"][0]["event"], "scope_changed")

    def test_replacement_keeps_removed_and_added_ids(self):
        self.data["claims"][0]["id"] = "C2"
        self.assertEqual([r["event"] for r in compare(self.before, self.state())["claims"]], ["removed", "added"])

    def test_query_only_change_and_unchanged_claim(self):
        after = copy.deepcopy(self.before)
        after["claims"]["C1"]["queries"]["Q2"] = "trace"
        self.assertEqual(compare(self.before, after)["claims"][0]["event"], "search_changed")
        self.assertEqual(compare(self.before, self.before)["claims"][0]["event"], "unchanged")


if __name__ == "__main__":
    unittest.main()
