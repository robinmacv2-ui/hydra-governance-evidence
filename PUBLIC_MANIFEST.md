# Public Manifest

## Included by design

- high-level product scope;
- architecture and control-flow description;
- security and threat models;
- validation-status truth boundary;
- small executable reference demo;
- public integrity hashes;
- publication preflight tooling;
- corporate review guide.

## Explicitly excluded

- full ROMEO-HYDRA master repository;
- private cryptographic implementation details not needed for review;
- production keys, secrets, credentials, tokens, salts, or seed material;
- private WORM/ledger databases and customer evidence;
- internal deployment topology and operational access paths;
- unpublished research modules;
- raw experimental physical evidence where disclosure is unnecessary;
- third-party confidential material;
- files not individually reviewed for public release.

## Disclosure rule

No file should be copied from the private master into this repository merely because it appears non-sensitive. It must pass both:

1. technical secret scanning; and
2. human IP / confidentiality review.
