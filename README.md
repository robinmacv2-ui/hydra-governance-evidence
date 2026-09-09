# Hydra Governance Systems — ROMEO-HYDRA Evidence Surface

**Purpose:** a public, review-oriented surface for corporate and technical evaluators. It exposes the product logic, validation posture, threat model, and an executable reference demonstration **without publishing the private ROMEO-HYDRA master repository**.

> This repository is an evidence and evaluation surface. It is **not** the full ROMEO-HYDRA source tree and the demonstration code is **not** the private production core.

## What ROMEO-HYDRA is intended to do

ROMEO-HYDRA is a governance architecture for high-stakes AI and automated decision systems. Its operating pattern is:

```text
Decision / inference
        ↓
Governance contract
        ↓
Policy + control evaluation
        ↓
PASS ───────────────→ auditable receipt
  │
  └─ FAIL-CLOSED ───→ blocked / rejected + auditable receipt
```

The product thesis is simple: a decision that cannot satisfy declared governance conditions should not silently proceed.

## 5-minute evaluator path

1. Read [`BIND_REVIEW_GUIDE.md`](BIND_REVIEW_GUIDE.md).
2. Inspect [`PRODUCT_SCOPE.md`](PRODUCT_SCOPE.md) and [`ARCHITECTURE.md`](ARCHITECTURE.md).
3. Review the current truth boundary in [`VALIDATION_STATUS.md`](VALIDATION_STATUS.md).
4. Inspect [`SECURITY_MODEL.md`](SECURITY_MODEL.md) and [`THREAT_MODEL.md`](THREAT_MODEL.md).
5. Run the public reference demo:

```bash
python demo/governance_gate.py demo/sample_input_pass.json
python demo/governance_gate.py demo/sample_input_fail.json
python -m unittest discover -s tests -v
```

6. Verify integrity of the public surface:

```bash
sha256sum -c SHA256SUMS
```

## What is deliberately not public

The private master remains the authority for implementation details, research modules, operational cryptographic material, complete test corpus, private evidence, and internal infrastructure. See [`PUBLIC_MANIFEST.md`](PUBLIC_MANIFEST.md).

## Evaluation access

A corporate evaluator that requires deeper technical due diligence can request controlled access to a narrowly scoped private review repository or supervised technical session. The full master should remain private by default.

## Ownership

ROMEO-HYDRA / Hydra Governance Systems — Luis Angel Vazquez Martinez.

GitHub: <https://github.com/robinmacv2-ui>
