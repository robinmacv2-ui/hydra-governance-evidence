# Security Model

## Security objectives

1. **Default deny / fail closed:** malformed or incomplete governance state is rejected.
2. **Evidence integrity:** audit outputs are hash-verifiable.
3. **Separation of concerns:** public evidence is separated from private implementation and operational secrets.
4. **No implicit trust:** a decision is not accepted merely because upstream software produced it.
5. **Reproducibility:** public demo behavior is deterministic for the same normalized input.

## Public/private boundary

The public surface MUST NOT contain:

- API keys, access tokens, passwords, or private keys;
- production cryptographic secrets;
- raw private customer data;
- full private master source;
- internal infrastructure credentials or deployment configuration;
- private evidence whose disclosure would weaken security or confidentiality;
- material that is contractually restricted.

## Cryptographic statement

SHA-256 is used in the public reference demo as an integrity digest over canonicalized receipt data. This alone does not provide confidentiality, authenticity, non-repudiation, or key management. Those properties require additional primitives and operational controls.

## Disclosure model

Corporate due diligence should advance through controlled layers:

```text
Public evidence → executable demo → scoped private review → supervised deep review
```
