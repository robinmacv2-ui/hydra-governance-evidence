# Evidence Policy

Every externally communicated technical claim should map to one of these evidence states:

- **REPRODUCED:** rerun against a pinned current commit/release and archived.
- **HISTORICAL:** valid for a previous pinned checkpoint but not automatically inherited by current HEAD.
- **EXPERIMENTAL:** research result not promoted to product qualification.
- **UNVERIFIED:** assertion without adequate current evidence; do not market as fact.

## Minimum evidence record

A promoted test result should capture:

- repository / component;
- commit SHA;
- environment;
- command executed;
- timestamp;
- result summary;
- artifact hash;
- operator / automation identity where appropriate.
