#!/bin/bash
# Galadriel: UI/UX Linter — runs on staged CSS/SCSS and markup files only

set -e

STAGED_CSS=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(css|scss|sass)$' || true)
STAGED_ALL=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(css|scss|sass|ts|tsx|js|jsx|vue|html)$' || true)

if [ -z "$STAGED_ALL" ]; then
  echo "Galadriel: No staged style or markup files. Skipping lint."
  exit 0
fi

if [ -n "$STAGED_CSS" ]; then
  echo "Galadriel: Running Stylelint..."
  npx stylelint $STAGED_CSS --fix
  if [ $? -ne 0 ]; then
    echo "Stylelint failed. Fix CSS/SCSS errors before committing."
    exit 1
  fi
fi

echo "Galadriel: Running Prettier..."
npx prettier --write $STAGED_ALL

# Re-stage auto-fixed files
git add $STAGED_ALL

echo "Galadriel: Lint passed."
exit 0
