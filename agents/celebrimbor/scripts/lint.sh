#!/bin/bash
# Celebrimbor: React/Next.js Linter — runs on staged files only

set -e

STAGED=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(ts|tsx|js|jsx)$' || true)

if [ -z "$STAGED" ]; then
  echo "Celebrimbor: No staged .ts/.tsx/.js/.jsx files. Skipping lint."
  exit 0
fi

echo "Celebrimbor: Running Next.js ESLint..."
npx next lint --fix
if [ $? -ne 0 ]; then
  echo "ESLint failed. Fix errors before committing."
  exit 1
fi

echo "Celebrimbor: Running Prettier..."
npx prettier --write $STAGED

echo "Celebrimbor: Running TypeScript type check..."
npx tsc --noEmit
if [ $? -ne 0 ]; then
  echo "TypeScript type check failed. Fix type errors before committing."
  exit 1
fi

echo "Celebrimbor: Running Vitest (related tests)..."
npx vitest run --passWithNoTests --reporter=verbose $(echo $STAGED | tr ' ' '\n' | sed 's/\.[^.]*$/.test&/' | tr '\n' ' ')
if [ $? -ne 0 ]; then
  echo "Tests failed. Fix failing tests before committing."
  exit 1
fi

# Re-stage auto-fixed files
git add $STAGED

echo "Celebrimbor: Lint passed."
exit 0
