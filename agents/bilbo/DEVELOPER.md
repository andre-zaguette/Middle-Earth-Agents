# Developer Guide — Bilbo Baggins

## When to use

Invoke Bilbo at the start of every non-trivial project or feature. He must run before any specialist agent acts.

Gandalf routes here via `SIGNAL_SCOPE_QUEST`. Users can also invoke Bilbo directly with a project brief.

## Activating in a project

### With Claude Code

Add to your project `CLAUDE.md`:

```markdown
## Bilbo Baggins — PM/PO Agent

Before any scoping or documentation decision, read:
- `<path-to-bilbo>/packages/bilbo/targets/claude/bilbo/SKILL.md`
- `<path-to-bilbo>/packages/bilbo/targets/claude/bilbo/references/guiding-patterns.md`
- `<path-to-bilbo>/packages/bilbo/targets/claude/bilbo/references/routing-map.md`

Palantír second brain:
- Architecture / ADR → `<path-to-palantir>/skills/architecture/SKILL.md`
- Routing → `<path-to-palantir>/skills/codex-routing/SKILL.md`
```

Or open a session inside `agents/bilbo-baggins/` — the `CLAUDE.md` already wires everything.

## Bootstrap

```bash
./scripts/wizard-bootstrap.sh
```

Checks: Git, AGENT.md, QUEST_PROGRESS.md, contexto.md, requirements.md, user-stories.md, open-questions.md, Palantír link.

## Operating sequence

1. **The Unexpected Journey** — surface assumptions, question the brief
2. **Riddles in the Dark** — one clarifying question at a time
3. **The Burglar's Eye** — find implicit requirements and unstated constraints
4. **The Map of Erebor** — define scope: IN / OUT / DEFERRED
5. **The One Ring Test** — validate each requirement against the project objective
6. **There and Back Again** — confirm understanding with stakeholder
7. **The Red Book** — write `docs/contexto.md`, `docs/requirements.md`, `docs/user-stories.md`, `docs/open-questions.md`
8. **Mirror of Galadriel** — self-audit (score ≥ 80%)
9. **Signal Gandalf** — emit `SIGNAL_PROJECT_SCOPED`

## Scripts

| Script | Command | Purpose |
|--------|---------|---------|
| Bootstrap | `./scripts/wizard-bootstrap.sh` | Load context and check documentation health |
| Mirror | `python3 scripts/wizard-mirror.py` | Self-audit before signaling Gandalf |
| Gates of Argonath | `cp scripts/gates-of-argonath.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit` | Install pre-commit hook |

## Mirror of Galadriel — audit criteria

Score must be ≥ 80% before signaling Gandalf:

1. **contexto.md** — exists and defines quest, objective, danger, scope, and agents required
2. **Requirements** — all have ID, description, priority, and responsible agent
3. **Acceptance Criteria** — each requirement has ≥ 1 Given/When/Then condition
4. **Scope Boundary** — IN / OUT / DEFERRED lists are explicit and unambiguous
5. **Open Questions** — all tracked with owner and deadline

## Templates

Copy to your project `docs/`:

```bash
cp packages/bilbo/targets/claude/bilbo/assets/templates/contexto.md docs/
cp packages/bilbo/targets/claude/bilbo/assets/templates/requirements.md docs/
cp packages/bilbo/targets/claude/bilbo/assets/templates/user-stories.md docs/
cp packages/bilbo/targets/claude/bilbo/assets/templates/open-questions.md docs/
```

## Signal protocols

| Signal | From / To | Payload |
|--------|-----------|---------|
| `SIGNAL_SCOPE_QUEST` | Gandalf → Bilbo | initial brief |
| `SIGNAL_REDOC_REQUEST` | Gandalf → Bilbo | documentation update request |
| `SIGNAL_PROJECT_SCOPED` | Bilbo → Gandalf | `context`, `requirements[]`, `acceptance_criteria[]`, `agents_required[]`, `open_questions[]` |

## Output shape

1. `docs/contexto.md` — project brief and context
2. `docs/requirements.md` — structured requirements with priorities
3. `docs/user-stories.md` — user stories with acceptance criteria
4. `docs/open-questions.md` — tracked open items with owners
5. `SIGNAL_PROJECT_SCOPED` payload for Gandalf
6. Next step

## Core law

**The map must be drawn before the journey begins.**

Without `docs/contexto.md`, no agent in the fellowship has a foundation. Bilbo writes it first.
