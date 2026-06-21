#!/bin/bash
# Beorn: Node.js/NestJS Linter — runs on staged files only

set -e

STAGED=$(git diff --cached --name-only --diff-filter=ACM | grep -E '\.(ts|js)$' || true)

if [ -z "$STAGED" ]; then
  echo "Beorn: No staged .ts/.js files. Skipping lint."
  exit 0
fi

echo "Beorn: Running ESLint..."
npx eslint $STAGED --fix --max-warnings=0
if [ $? -ne 0 ]; then
  echo "ESLint failed. Fix errors before committing."
  exit 1
fi

echo "Beorn: Running Prettier..."
npx prettier --write $STAGED

echo "Beorn: Running TypeScript type check..."
npx tsc --noEmit
if [ $? -ne 0 ]; then
  echo "TypeScript type check failed. Fix type errors before committing."
  exit 1
fi

echo "Beorn: Running Jest (staged modules)..."
npx jest --passWithNoTests --bail --findRelatedTests $STAGED
if [ $? -ne 0 ]; then
  echo "Tests failed. Fix failing tests before committing."
  exit 1
fi

# Re-stage auto-fixed files
git add $STAGED

echo "Beorn: Lint passed."
exit 0
