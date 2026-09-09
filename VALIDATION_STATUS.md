# Validation Status — Truth Boundary

This file is intentionally conservative. It separates **reproduced/current evidence**, **historical checkpoints**, and **experimental work**.

## Current public statement

| Component | Status | Public claim boundary |
|---|---|---|
| Governance / control-plane contracts | PASS checkpoint reported | fail-closed / geometry / polarity contract suite reported as 13 tests passing |
| Cryptographic envelope | HISTORICAL PASS checkpoint | 60-test checkpoint reported; current HEAD reproduction should be treated separately until rerun and archived |
| Public reference demo in this repository | REPRODUCIBLE | runnable with Python stdlib and included tests |
| Physical PUF / key derivation research | EXPERIMENTAL / NOT PROMOTED | prior experimental gate produced negative residual; key derivation remains forbidden for that dataset/state |

## Important interpretation

A historical passing checkpoint is evidence of a past state, not proof that every later commit remains valid. Any BIND or corporate pilot should pin a commit/release, reproduce its tests, and archive the resulting evidence.

## Promotion rule

No component should be represented as production-qualified solely because a previous checkpoint passed. Promotion requires a pinned version, reproducible test evidence, defined operating assumptions, and an explicit acceptance decision.
