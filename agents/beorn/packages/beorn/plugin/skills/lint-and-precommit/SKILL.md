---
name: lint-and-precommit
description: Node.js/NestJS lint and pre-commit quality gate. Use before every commit on a Beorn project. Runs ESLint, Prettier, TypeScript type check, and unit tests on staged files. Blocks the commit if any check fails.
---

# Skill: Lint and Pre-commit — Beorn (Node.js / NestJS)

## When to use

Run before every commit on a Node.js or NestJS project. This skill enforces:
- ESLint rules (TypeScript strict, no `any`, import discipline)
- Prettier formatting
- TypeScript compilation (`tsc --noEmit`)
- Jest unit tests for staged modules

## Setup

### 1. Install dependencies

```bash
npm install --save-dev \
  eslint \
  @typescript-eslint/eslint-plugin \
  @typescript-eslint/parser \
  eslint-plugin-import \
  prettier \
  eslint-config-prettier
```

### 2. Copy config templates

```bash
cp scripts/lint-templates/.eslintrc.json .
cp scripts/lint-templates/.prettierrc .
cp scripts/lint-templates/.eslintignore .
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
    "lint": "eslint 'src/**/*.ts' --fix",
    "lint:check": "eslint 'src/**/*.ts'",
    "format": "prettier --write 'src/**/*.ts'",
    "type-check": "tsc --noEmit"
  }
}
```

## Procedure

The `scripts/lint.sh` runs automatically via the pre-commit hook:

1. Detect staged `.ts` / `.js` files
2. Run `eslint --fix` on staged files
3. Run `prettier --write` on staged files
4. Run `tsc --noEmit` (full project type check)
5. Run `jest --passWithNoTests` on files related to staged modules
6. Re-stage auto-fixed files
7. Block commit if any step fails

## Rules enforced

| Rule | Level |
|------|-------|
| `@typescript-eslint/no-explicit-any` | error |
| `@typescript-eslint/explicit-function-return-type` | warn |
| `@typescript-eslint/no-floating-promises` | error |
| `import/no-cycle` | error |
| `no-console` | warn |
| Prettier formatting | error |

## Output

- Auto-fixed files re-staged
- Type errors printed to stderr
- Commit blocked on any error
- Warning printed (non-blocking) for console usage
