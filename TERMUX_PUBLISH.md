# Termux publication procedure

The GitHub connector used to prepare this package could verify the GitHub identity and public repositories, but it did not expose repository-creation or private-master access for this session. Therefore publication of the new public repository must be executed from your authenticated Termux environment.

## Commands

After downloading and extracting this folder in Termux:

```bash
cd hydra-governance-evidence
bash scripts/public_preflight.sh .
bash scripts/publish_termux.sh
```

The script creates **only** `robinmacv2-ui/hydra-governance-evidence` as public when that repository does not already exist. It does not modify the visibility of the private master.

If the repository already exists, the script refuses to change its visibility automatically and only attempts to push the prepared surface.
