---
name: lint-and-precommit
description: React/Next.js lint and pre-commit quality gate. Use before every commit on a Celebrimbor project. Runs ESLint (Next.js rules), Prettier, TypeScript type check, and Vitest on staged files. Blocks the commit if any check fails.
---

# Skill: Lint and Pre-commit — Celebrimbor (React / Next.js)

## When to use

Run before every commit on a React or Next.js project. This skill enforces:
- ESLint with Next.js rules (`eslint-config-next`)
- No `dangerouslySetInnerHTML` without explicit comment
- No `any` types
- Prettier formatting
- TypeScript compilation (`tsc --noEmit`)
- Vitest unit tests for staged components

## Setup

### 1. Install dependencies

```bash
npm install --save-dev \
  eslint \
  eslint-config-next \
  @typescript-eslint/eslint-plugin \
  @typescript-eslint/parser \
  prettier \
  eslint-config-prettier
```

### 2. Copy config templates

```bash
cp scripts/lint-templates/.eslintrc.json .
cp scripts/lint-templates/.prettierrc .
```

### 3. Install the pre-commit hook

```bash
cp scripts/gates-of-argonath.sh .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit
```

### 4. Add lint script to package.json

```json
{
  "scripts": {
    "lint": "next lint --fix",
    "lint:check": "next lint",
    "format": "prettier --write 'src/**/*.{ts,tsx}'",
    "type-check": "tsc --noEmit"
  }
}
```

## Procedure

The `scripts/lint.sh` runs automatically via the pre-commit hook:

1. Detect staged `.ts` / `.tsx` / `.js` / `.jsx` files
2. Run `next lint --fix` on staged files
3. Run `prettier --write` on staged files
4. Run `tsc --noEmit` (full project type check)
5. Run `vitest run --passWithNoTests` on related test files
6. Re-stage auto-fixed files
7. Block commit if any step fails

## Rules enforced

| Rule | Level |
|------|-------|
| `@typescript-eslint/no-explicit-any` | error |
| `@next/next/no-img-element` | error |
| `react-hooks/rules-of-hooks` | error |
| `react-hooks/exhaustive-deps` | warn |
| `@typescript-eslint/no-floating-promises` | error |
| `no-console` | warn |
| Prettier formatting | error |

## Output

- Auto-fixed files re-staged
- Type errors printed to stderr
- Commit blocked on any error
