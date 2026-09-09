#!/usr/bin/env python3
"""Public reference demo for the ROMEO-HYDRA fail-closed + receipt pattern.

This is intentionally small and does NOT contain the private ROMEO-HYDRA core.
"""

from __future__ import annotations

import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = {
    "decision_id",
    "model_id",
    "risk_score",
    "required_controls",
    "observed_controls",
}
MAX_RISK_SCORE = Decimal("0.05")


@dataclass(frozen=True)
class GateResult:
    status: str
    reasons: tuple[str, ...]
    receipt: dict[str, Any]
    digest_sha256: str


def _canonical_json(value: Any) -> bytes:
    return json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
    ).encode("utf-8")


def _parse_risk_score(raw: Any) -> Decimal:
    if isinstance(raw, bool):
        raise ValueError("boolean risk_score is invalid")
    try:
        value = Decimal(str(raw))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError("risk_score is not a valid decimal") from exc
    if not value.is_finite() or value < 0:
        raise ValueError("risk_score must be finite and non-negative")
    return value


def evaluate(event: dict[str, Any], *, timestamp: str | None = None) -> GateResult:
    reasons: list[str] = []

    missing = sorted(REQUIRED_TOP_LEVEL - set(event))
    if missing:
        reasons.append("missing_fields:" + ",".join(missing))

    risk: Decimal | None = None
    if "risk_score" in event:
        try:
            risk = _parse_risk_score(event["risk_score"])
        except ValueError as exc:
            reasons.append(f"invalid_risk_score:{exc}")

    required = event.get("required_controls")
    observed = event.get("observed_controls")

    if required is not None and not (
        isinstance(required, list) and all(isinstance(x, str) and x for x in required)
    ):
        reasons.append("required_controls_must_be_nonempty_strings")

    if observed is not None and not (
        isinstance(observed, list) and all(isinstance(x, str) and x for x in observed)
    ):
        reasons.append("observed_controls_must_be_nonempty_strings")

    if isinstance(required, list) and isinstance(observed, list):
        missing_controls = sorted(set(required) - set(observed))
        if missing_controls:
            reasons.append("missing_controls:" + ",".join(missing_controls))

    if risk is not None and risk > MAX_RISK_SCORE:
        reasons.append(f"risk_exceeds_limit:{risk}>{MAX_RISK_SCORE}")

    status = "BLOCK" if reasons else "ALLOW"
    receipt = {
        "decision_id": event.get("decision_id"),
        "model_id": event.get("model_id"),
        "status": status,
        "reasons": reasons,
        "policy": {"max_risk_score": str(MAX_RISK_SCORE)},
        "evaluated_at": timestamp
        or datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    digest = hashlib.sha256(_canonical_json(receipt)).hexdigest()
    return GateResult(status, tuple(reasons), receipt, digest)


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {argv[0]} EVENT.json", file=sys.stderr)
        return 2

    path = Path(argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "BLOCK", "error": str(exc)}, indent=2))
        return 1

    if not isinstance(data, dict):
        print(json.dumps({"status": "BLOCK", "error": "top-level JSON must be an object"}, indent=2))
        return 1

    result = evaluate(data)
    output = dict(result.receipt)
    output["digest_sha256"] = result.digest_sha256
    print(json.dumps(output, indent=2, ensure_ascii=False))
    return 0 if result.status == "ALLOW" else 3


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
