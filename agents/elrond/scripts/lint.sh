#!/bin/bash
# Elrond: Vue 3/Nuxt Linter — runs on staged files only

set -e

STAGED=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(ts|js|vue)$' || true)

if [ -z "$STAGED" ]; then
  echo "Elrond: No staged .ts/.js/.vue files. Skipping lint."
  exit 0
fi

echo "Elrond: Running ESLint..."
npx eslint $STAGED --fix --max-warnings=0
if [ $? -ne 0 ]; then
  echo "ESLint failed. Fix errors before committing."
  exit 1
fi

echo "Elrond: Running Prettier..."
npx prettier --write $STAGED

echo "Elrond: Running vue-tsc type check..."
npx vue-tsc --noEmit
if [ $? -ne 0 ]; then
  echo "vue-tsc type check failed. Fix type errors before committing."
  exit 1
fi

echo "Elrond: Running Vitest (related tests)..."
npx vitest run --passWithNoTests --reporter=verbose $(echo $STAGED | tr ' ' '\n' | sed 's/\.[^.]*$/.test&/' | tr '\n' ' ')
if [ $? -ne 0 ]; then
  echo "Tests failed. Fix failing tests before committing."
  exit 1
fi

# Re-stage auto-fixed files
git add $STAGED

echo "Elrond: Lint passed."
exit 0
