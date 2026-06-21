---
name: lint-and-precommit
description: Vue/Nuxt lint and pre-commit quality gate. Use before every commit on an Elrond project. Runs ESLint (Vue 3 + TypeScript rules), Prettier, vue-tsc type check, and Vitest on staged files. Blocks the commit if any check fails.
---

# Skill: Lint and Pre-commit — Elrond (Vue 3 / Nuxt)

## When to use

Run before every commit on a Vue 3 or Nuxt project. This skill enforces:
- ESLint with Vue 3 and TypeScript rules
- Composition API only (`vue/component-api-style`)
- No `v-html` without explicit comment
- No `any` types
- Prettier formatting
- `vue-tsc --noEmit` type check
- Vitest unit tests for staged components

## Setup

### 1. Install dependencies

```bash
npm install --save-dev \
  eslint \
  eslint-plugin-vue \
  @typescript-eslint/eslint-plugin \
  @typescript-eslint/parser \
  vue-eslint-parser \
  prettier \
  eslint-config-prettier \
  vue-tsc
```

For Nuxt 3, prefer `@nuxt/eslint`:

```bash
npm install --save-dev @nuxt/eslint
```

### 2. Copy config templates

```bash
cp scripts/lint-templates/eslint.config.mjs .
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
    "lint": "eslint . --fix",
    "lint:check": "eslint .",
    "format": "prettier --write 'src/**/*.{ts,vue}'",
    "type-check": "vue-tsc --noEmit"
  }
}
```

## Procedure

The `scripts/lint.sh` runs automatically via the pre-commit hook:

1. Detect staged `.ts` / `.js` / `.vue` files
2. Run `eslint --fix` on staged files
3. Run `prettier --write` on staged files
4. Run `vue-tsc --noEmit` (full project type check)
5. Run `vitest run --passWithNoTests` on related test files
6. Re-stage auto-fixed files
7. Block commit if any step fails

## Rules enforced

| Rule | Level |
|------|-------|
| `vue/component-api-style` — Composition API only | error |
| `vue/no-v-html` | warn |
| `vue/define-props-declaration` | error |
| `vue/define-emits-declaration` | error |
| `@typescript-eslint/no-explicit-any` | error |
| `@typescript-eslint/no-floating-promises` | error |
| Prettier formatting | error |

## Output

- Auto-fixed files re-staged
- Type errors printed to stderr
- Commit blocked on any error
