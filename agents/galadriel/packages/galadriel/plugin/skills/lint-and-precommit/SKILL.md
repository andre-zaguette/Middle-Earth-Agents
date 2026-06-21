---
name: lint-and-precommit
description: UI/UX lint and pre-commit quality gate. Use before every commit on a Galadriel project. Runs Stylelint (CSS/SCSS/Tailwind), ESLint, and Prettier on staged files. Blocks the commit if hardcoded tokens, invalid CSS, or formatting issues are found.
---

# Skill: Lint and Pre-commit — Galadriel (UI / UX)

## When to use

Run before every commit on any project with CSS, SCSS, or Tailwind. This skill enforces:
- Stylelint rules (no invalid hex, no `!important`, token naming convention)
- Tailwind class ordering (if `prettier-plugin-tailwindcss` is installed)
- No hardcoded color/spacing values (caught by Stylelint custom rules)
- Prettier formatting for all style and markup files

## Setup

### 1. Install dependencies

```bash
npm install --save-dev \
  stylelint \
  stylelint-config-standard \
  stylelint-config-standard-scss \
  stylelint-config-tailwindcss \
  prettier \
  prettier-plugin-tailwindcss
```

### 2. Copy config templates

```bash
cp scripts/lint-templates/.stylelintrc.json .
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
    "lint:css": "stylelint '**/*.{css,scss}' --fix",
    "lint:check:css": "stylelint '**/*.{css,scss}'",
    "format": "prettier --write '**/*.{css,scss,html,tsx,vue}'"
  }
}
```

## Procedure

The `scripts/lint.sh` runs automatically via the pre-commit hook:

1. Detect staged `.css` / `.scss` / `.sass` files
2. Run `stylelint --fix` on staged style files
3. Detect staged `.ts` / `.tsx` / `.vue` / `.html` files
4. Run `prettier --write` on all staged markup and style files
5. Re-stage auto-fixed files
6. Block commit if any step fails

## Rules enforced

| Rule | Level |
|------|-------|
| `color-no-invalid-hex` | error |
| `declaration-no-important` | error |
| `value-keyword-case` | error |
| `custom-property-pattern` — must match `^[a-z][a-z0-9-]*$` | warn |
| `color-named` — no named colors, use tokens | error |
| `unit-allowed-list` | warn |
| Prettier formatting | error |

## Output

- Auto-fixed files re-staged
- Invalid CSS rules printed to stderr
- Commit blocked on any error
