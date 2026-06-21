#!/usr/bin/env bash
set -euo pipefail

ROOT="${SECOND_BRAIN_ROOT:-$HOME/SecondBrain}"
cd "$ROOT"

git add .
if git diff --cached --quiet; then
  echo "No changes."
  exit 0
fi

git commit -m "${1:-update second brain}"
git push
