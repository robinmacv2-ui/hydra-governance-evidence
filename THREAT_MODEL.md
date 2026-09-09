# Threat Model

| Threat | Public control / design response | Residual risk |
|---|---|---|
| Malformed decision input | strict schema/field checks; fail closed | semantic attacks still require domain policy |
| Missing mandatory controls | explicit required-control set | policy configuration errors |
| Risk score parsing ambiguity | decimal arithmetic in public demo | source-data quality |
| Receipt tampering | SHA-256 digest over canonical receipt | hash does not authenticate actor identity |
| Secret leakage through public repo | public/private manifest + preflight scanner | manual review still required |
| Overclaiming maturity | validation-status truth boundary | evidence can become stale |
| Compromise of private master | master remains private; least disclosure | GitHub/account security remains external dependency |
| Replay of valid evidence | decision identifiers + timestamp field | production anti-replay requires stronger state controls |

## Explicit exclusions

The public demo is not a complete production security boundary. It does not claim to solve identity, HSM/KMS key custody, distributed consensus, secure enclaves, supply-chain attestation, or end-to-end production authorization on its own.
