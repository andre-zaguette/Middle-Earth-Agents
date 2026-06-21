# Developer Guide — Boromir

## When to use

Invoke Boromir to verify any change before it merges. No feature, fix, or refactor is complete until Boromir's suite passes. He is the final gate between implementation and main.

Gandalf triggers Boromir via the **Horn of Gondor** protocol. Any specialist agent signals him directly when their work is ready for review.

## Activating in a project

### With Claude Code

Add to your project `CLAUDE.md`:

```markdown
## Boromir — Quality Agent

When verifying any change, read:
- `<path-to-boromir>/GEMINI.md` or `README.md` for engagement protocol

Invoke via: `./scripts/horn-of-gondor.sh "<change description>"`
```

### Triggering the Horn of Gondor

```bash
./scripts/horn-of-gondor.sh "Add user authentication module to NestJS API"
```

Boromir receives the context, assesses impact, selects the relevant test harnesses, and reports.

## Bootstrap

```bash
./scripts/boromir-bootstrap.sh
```

Initializes Python (pytest), TypeScript (vitest), and E2E (playwright) test environments.

## Operating sequence

When invoked, Boromir:

1. **Impact assessment** — identifies which tests must run (unit / integration / E2E) based on the change context
2. **Execute** — runs the relevant harnesses in parallel where possible
3. **Report** — delivers a concise verdict:
   - Pass → `ACK_QUALITY_APPROVED` with coverage summary
   - Fail → surgical analysis of root cause, required fixes, and what to retest

## Test harnesses

| Stack | Tool | When |
|-------|------|------|
| Python (backend/services) | `pytest` | Any `SIGNAL_PYTHON_REVIEW_REQUEST` |
| Frontend (React / Vue / TS) | `vitest` | Any `SIGNAL_REACT_REVIEW_REQUEST` or `SIGNAL_VUE_REVIEW_REQUEST` |
| End-to-End (full stack) | `playwright` | Cross-stack features or user journey changes |

## Scripts

| Script | Command | Purpose |
|--------|---------|---------|
| Horn of Gondor | `./scripts/horn-of-gondor.sh "<context>"` | Entry point for all verification requests |
| Bootstrap | `./scripts/boromir-bootstrap.sh` | Initialize test environments |

## Signal protocols

| Signal | From / To | Payload |
|--------|-----------|---------|
| `SIGNAL_BREACH_DEFENSE` | Gandalf → Boromir | `context`, `artifacts[]`, `agent_source` |
| `SIGNAL_NODE_REVIEW_REQUEST` | Beorn → Boromir | module artifacts |
| `SIGNAL_REACT_REVIEW_REQUEST` | Celebrimbor → Boromir | feature artifacts |
| `SIGNAL_VUE_REVIEW_REQUEST` | Elrond → Boromir | feature artifacts |
| `SIGNAL_PYTHON_REVIEW_REQUEST` | Radagast → Boromir | module artifacts |
| `SIGNAL_UI_REVIEW_REQUEST` | Galadriel → Boromir | component artifacts |
| `ACK_QUALITY_APPROVED` | Boromir → Gandalf | `verdict`, `findings[]`, `coverage` |

## Engineering standards

- **Proof Before Alloy** — no merge until the suite passes
- **Test-First on bugs** — every bug fix starts with a failing test that reproduces the error
- **Incremental runs** — run the smallest relevant test set first; escalate to full suite only if needed
- **No vibes** — verdict is based on exit codes, not assessment

## Core law

**No code merges without Boromir's sign-off.**

The Horn of Gondor must be answered before any PR is considered complete.
