#!/usr/bin/env bash
set -euo pipefail

REPO="${REPO:-robinmacv2-ui/hydra-governance-evidence}"
DESCRIPTION="Public technical evidence surface for Hydra Governance Systems / ROMEO-HYDRA"

command -v git >/dev/null || { echo 'git is required'; exit 2; }
command -v gh >/dev/null || { echo 'GitHub CLI (gh) is required'; exit 2; }
command -v python >/dev/null || { echo 'python is required'; exit 2; }

bash scripts/public_preflight.sh .

git init -b main >/dev/null 2>&1 || true

if ! git config user.name >/dev/null 2>&1; then
  git config user.name "LUIS ANGEL VAZQUEZ MARTINEZ"
fi
if ! git config user.email >/dev/null 2>&1; then
  git config user.email "304690313+robinmacv2-ui@users.noreply.github.com"
fi

git add .
if ! git diff --cached --quiet; then
  git commit -m "chore: publish ROMEO-HYDRA public evidence surface"
fi

if gh repo view "$REPO" >/dev/null 2>&1; then
  echo "Repository $REPO already exists; refusing to change visibility automatically."
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "https://github.com/${REPO}.git"
  fi
  git push -u origin main
else
  gh repo create "$REPO" \
    --public \
    --description "$DESCRIPTION" \
    --source=. \
    --remote=origin \
    --push
fi

echo "PUBLISHED=https://github.com/${REPO}"
