# Product Scope

## Product core

The public product statement is intentionally narrower than the total research repository:

```text
Product Core ⊂ Product Ecosystem ⊂ Private Repository
```

The review surface covers the **Product Core** concept:

1. receive a decision or inference event;
2. evaluate declared governance conditions;
3. reject malformed or non-compliant states by default;
4. generate an auditable receipt for the resulting state;
5. preserve a clear boundary between evidence and implementation internals.

## Target environments

- regulated AI and automated decision systems;
- model-risk and compliance workflows;
- financial-services control planes;
- high-assurance internal AI tooling;
- audit and forensic review workflows.

## Non-goals of this public repository

This repository does not attempt to expose or reproduce the full private ecosystem, research corpus, cryptographic internals, physical PUF experiments, infrastructure automation, or production deployment configuration.

## Pilot success criteria

A bounded corporate pilot should define, before execution:

- one decision workflow;
- explicit governance contracts;
- pass/fail semantics;
- evidence fields;
- latency budget;
- replay and tamper checks;
- acceptance thresholds;
- rollback / failure behavior.
