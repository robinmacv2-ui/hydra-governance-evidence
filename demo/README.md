# Public Reference Demo

This demonstration makes the governance pattern inspectable without exposing the private ROMEO-HYDRA core.

Expected behavior:

```bash
python demo/governance_gate.py demo/sample_input_pass.json
# status: ALLOW

python demo/governance_gate.py demo/sample_input_fail.json
# status: BLOCK
```

The second command intentionally exits non-zero because a blocked decision is not a successful authorization.
