# Palantír — Universal Archive

The all-seeing stone. The Palantír is the shared second brain of the fellowship — a living memory of skills, decisions, contracts, and knowledge that every agent consults before acting.

## Structure

```
palantir/
  skills/           — reusable skill workflows (consulted before coding)
  vault/            — notes, decisions, project context (Obsidian-compatible)
  templates/        — reusable output formats
  scripts/          — local utilities
  .codex-plugins/   — Codex plugin definitions (caveman compression)
```

## Skills

Six transversal skills available to all agents:

| Skill | When to use |
|-------|-------------|
| `skills/architecture/` | System design, module boundaries, migrations, technical decisions → produces ADRs |
| `skills/code-review/` | Reviewing PRs, diffs, refactors, architecture changes → surgical risk report |
| `skills/codex-routing/` | Choosing which skill or agent to invoke first for a given task |
| `skills/debugging/` | Diagnosing failures, regressions, flaky behavior, production bugs |
| `skills/refactoring/` | Improving structure without changing behavior, under test protection |
| `skills/testing/` | Test planning before merging, refactoring, or changing behavior |

## Codex Routing Map

The `skills/codex-routing/SKILL.md` maps task types to skill paths:

| Task type | Route |
|-----------|-------|
| Backend broad | `backend-engineering` |
| Frontend broad | `frontend-engineering` |
| Python broad | `python-engineering` |
| React bug / UI | `react` |
| Next.js routing / data | `nextjs` or `react-next` |
| Django | `django` |
| FastAPI | `fastapi` |
| NestJS | `nestjs` |
| Python tests | `pytest` |
| JS/TS tests | `vitest-jest` |
| Figma read/write | `figma` + `figma-use` |
| Figma to code | `figma-implement-design` |
| Browser automation | `playwright` |
| Security review | `security-best-practices` |

## Vault

`vault/` is an Obsidian-compatible knowledge base for programming notes, decisions, and reusable context. Suggested folders: Projects, Areas, Resources, Daily, Decisions.

Key resources:
- `vault/Resources/Gandalf Guide.md` — guide behavior, pattern selection, Socratic questioning
- `vault/Resources/Codex Skills Caveman.md` — compressed skill reference for fast routing

## Templates

- `templates/adr.md` — Architectural Decision Record template

## Scripts

| Script | Purpose |
|--------|---------|
| `scripts/link-agents.sh` | Link agent skill directories |
| `scripts/sb-sync.sh` | Sync second brain content |

## Core Law

**Palantír First.** Every agent checks relevant skills in `skills/` before coding. Recurring workflows must be recorded or updated back into `skills/` or `vault/`. The archive grows with every quest.

## How Agents Use the Palantír

1. **Before acting** — read the relevant `skills/` entry for the task type
2. **For routing decisions** — consult `skills/codex-routing/SKILL.md`
3. **For Gandalf-style guidance** — consult `vault/Resources/Gandalf Guide.md`
4. **After learning** — document recurring lessons back into `skills/` or `vault/`
