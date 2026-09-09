#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

PATTERNS='(ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----|sk-[A-Za-z0-9_-]{20,}|AIza[0-9A-Za-z_-]{20,}|password[[:space:]]*[:=][[:space:]]*[^[:space:]]+)'

printf '%s\n' '[1/4] Checking tracked candidate files for obvious secret patterns...'
if grep -RInE --exclude-dir=.git --exclude='SHA256SUMS' "$PATTERNS" .; then
  echo 'PREFLIGHT=FAIL: possible secret material detected.' >&2
  exit 10
fi

printf '%s\n' '[2/4] Rejecting dangerous private-key / database file extensions...'
if find . -type f \( -name '*.pem' -o -name '*.key' -o -name '*.p12' -o -name '*.pfx' -o -name '*.db' -o -name '*.sqlite' \) -print | grep -q .; then
  echo 'PREFLIGHT=FAIL: sensitive file type present.' >&2
  exit 11
fi

printf '%s\n' '[3/4] Running demo unit tests...'
python -m unittest discover -s tests -v

printf '%s\n' '[4/4] Verifying integrity manifest...'
sha256sum -c SHA256SUMS

echo 'PUBLIC_PREFLIGHT=PASS'
