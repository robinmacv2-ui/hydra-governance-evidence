import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "demo"))

from governance_gate import evaluate  # noqa: E402


FIXED_TS = "2026-09-09T00:00:00+00:00"


class GovernanceGateTests(unittest.TestCase):
    def test_allows_valid_event(self):
        event = {
            "decision_id": "d1",
            "model_id": "m1",
            "risk_score": "0.05",
            "required_controls": ["a", "b"],
            "observed_controls": ["b", "a"],
        }
        result = evaluate(event, timestamp=FIXED_TS)
        self.assertEqual(result.status, "ALLOW")
        self.assertEqual(result.reasons, ())

    def test_blocks_over_limit(self):
        event = {
            "decision_id": "d2",
            "model_id": "m1",
            "risk_score": "0.0500001",
            "required_controls": [],
            "observed_controls": [],
        }
        result = evaluate(event, timestamp=FIXED_TS)
        self.assertEqual(result.status, "BLOCK")
        self.assertTrue(any(x.startswith("risk_exceeds_limit:") for x in result.reasons))

    def test_blocks_missing_control(self):
        event = {
            "decision_id": "d3",
            "model_id": "m1",
            "risk_score": "0.01",
            "required_controls": ["human_review"],
            "observed_controls": [],
        }
        result = evaluate(event, timestamp=FIXED_TS)
        self.assertEqual(result.status, "BLOCK")
        self.assertIn("missing_controls:human_review", result.reasons)

    def test_blocks_malformed_risk(self):
        event = {
            "decision_id": "d4",
            "model_id": "m1",
            "risk_score": "NaN",
            "required_controls": [],
            "observed_controls": [],
        }
        result = evaluate(event, timestamp=FIXED_TS)
        self.assertEqual(result.status, "BLOCK")
        self.assertTrue(any(x.startswith("invalid_risk_score:") for x in result.reasons))

    def test_receipt_digest_is_deterministic_for_fixed_timestamp(self):
        event = {
            "decision_id": "d5",
            "model_id": "m1",
            "risk_score": "0.01",
            "required_controls": ["a"],
            "observed_controls": ["a"],
        }
        a = evaluate(event, timestamp=FIXED_TS)
        b = evaluate(event, timestamp=FIXED_TS)
        self.assertEqual(a.digest_sha256, b.digest_sha256)


if __name__ == "__main__":
    unittest.main()
