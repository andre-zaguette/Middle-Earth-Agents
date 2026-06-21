# Developer Guide — Palantír

## What this is

The Palantír is the shared second brain of the fellowship. It is not a coding agent — it is a living knowledge base that every agent consults before acting and updates after learning.

It contains reusable skill workflows, architectural decisions, project context, and routing rules. Think of it as the memory layer of the entire system.

## Structure

```
palantir/
  skills/           — reusable skill workflows (read before coding)
  vault/            — notes, decisions, project context (Obsidian-compatible)
  templates/        — reusable output formats (ADR, etc.)
  scripts/          — utilities for linking and syncing
  .codex-plugins/   — Codex plugin definitions
```

## How to use in a project

### Step 1 — Link the skills

```bash
./scripts/link-agents.sh
```

This links the Palantír `skills/` directory so all agents can resolve `../palantir/skills/` paths.

### Step 2 — Reference in each agent's CLAUDE.md

Each agent already has Palantír references wired in their `CLAUDE.md`. When opening a project in Claude Code, load the relevant agent `CLAUDE.md` and the Palantír paths resolve automatically.

### Step 3 — Sync the second brain

```bash
./scripts/sb-sync.sh
```

Syncs vault content. Use after updating notes or decisions in the vault.

## Skills reference

| Skill | Path | When to use |
|-------|------|-------------|
| Architecture | `skills/architecture/SKILL.md` | System design, module boundaries, migrations, ADRs |
| Code Review | `skills/code-review/SKILL.md` | PRs, diffs, refactors, architecture changes |
| Codex Routing | `skills/codex-routing/SKILL.md` | Choosing which agent or skill to invoke first |
| Debugging | `skills/debugging/SKILL.md` | Failing tests, regressions, runtime errors, flaky behavior |
| Refactoring | `skills/refactoring/SKILL.md` | Improving structure without changing behavior |
| Testing | `skills/testing/SKILL.md` | Test planning before merging, refactoring, or changing behavior |

## Vault

`vault/` is an Obsidian-compatible knowledge base. Open it directly in Obsidian for graph view and backlinks.

Key resources already present:

- `vault/Resources/Gandalf Guide.md` — Gandalf-style questioning, pattern selection, senior engineering guidance
- `vault/Resources/Codex Skills Caveman.md` — compressed skill reference for fast routing decisions

Add new resources as the project evolves: project decisions, lessons learned, dependency maps, API changelogs.

## Templates

| Template | Path | Use for |
|----------|------|---------|
| ADR | `templates/adr.md` | Recording architectural decisions that affect the project long-term |

Copy, fill in, and commit to `vault/Decisions/` or the relevant project directory.

## Codex plugin

`.codex-plugins/caveman/` defines the **Caveman** skill for Codex — a compression skill that strips filler language and produces dense, high-signal output. Load it when context window economy is critical.

## Core law

**Palantír First.** Every agent reads before acting. Every agent writes back after learning.

When a workflow repeats, update or add to `skills/`. When a decision matters, record it via `templates/adr.md`. When a lesson is hard-won, add it to `vault/`.

The archive is only as useful as the discipline to maintain it.
