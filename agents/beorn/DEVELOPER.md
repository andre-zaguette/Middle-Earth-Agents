# Developer Guide — Beorn

## When to use

Invoke Beorn when the task involves Node.js or NestJS: new modules, REST/GraphQL endpoints, queue jobs, database migrations, authentication guards, or backend TypeScript work.

Gandalf routes here via `SIGNAL_NODE_TASK`.

## Activating in a project

### With Claude Code

Add to your project `CLAUDE.md`:

```markdown
## Beorn — Node.js/NestJS Agent

Before any Node/NestJS decision, read:
- `<path-to-beorn>/packages/beorn/plugin/skills/beorn/SKILL.md`

Palantír second brain:
- Architecture / ADR → `<path-to-palantir>/skills/architecture/SKILL.md`
- Code review → `<path-to-palantir>/skills/code-review/SKILL.md`
- Debugging → `<path-to-palantir>/skills/debugging/SKILL.md`
- Refactoring → `<path-to-palantir>/skills/refactoring/SKILL.md`
- Test planning → `<path-to-palantir>/skills/testing/SKILL.md`
```

Or simply open a session inside `agents/beorn/` — the `CLAUDE.md` already wires everything.

## Bootstrap

Run at the start of every session to load project context:

```bash
./scripts/wizard-bootstrap.sh
```

Checks: Git, AGENT.md, QUEST_PROGRESS.md, contexto.md, package.json, NestJS config, TypeScript strict mode, Jest, published contracts.

## Operating sequence

1. **Palantír check** — consult existing contracts and modules before creating new ones
2. **Module boundary** — declare the NestJS module scope and its exports
3. **DTO design** — define input/output shapes with `class-validator` before any implementation
4. **Publish contract** — if creating a new endpoint, publish to `docs/archive/contracts/` before consumers build
5. **Tests first** — Jest unit test for the Service + integration test for the Controller
6. **Implement** — code under test protection
7. **Mithril Armor** — run security scan before signaling Boromir
8. **Signal Boromir** — `SIGNAL_NODE_REVIEW_REQUEST` with artifacts and API contracts

## Scripts

| Script | Command | Purpose |
|--------|---------|---------|
| Bootstrap | `./scripts/wizard-bootstrap.sh` | Load context and check harness health |
| Mirror | `python3 scripts/wizard-mirror.py` | Self-audit quality before delivery (5 criteria, score ≥ 80%) |
| Mithril Armor | `python3 scripts/mithril-armor.py` | Scan for auth gaps, secrets, SQL injection, `any` types |
| Gates of Argonath | `cp scripts/gates-of-argonath.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit` | Install git pre-commit hook |

## Mirror of Galadriel — audit criteria

Before signaling Boromir, score must be ≥ 80%:

1. **DTO-First** — all external input validated via DTO + class-validator
2. **Module Isolation** — no circular dependencies, explicit exports
3. **Contract Published** — API contract published before consumers build
4. **Proof Before Alloy** — Jest unit (service) + integration (controller) tests present
5. **Mithril Armor** — scan executed, no hardcoded secrets or unguarded endpoints

## Signal protocols

| Signal | From / To | Payload |
|--------|-----------|---------|
| `SIGNAL_NODE_TASK` | Gandalf → Beorn | `context`, `nestjs?`, `db_schema?` |
| `SIGNAL_API_NEEDED` | Celebrimbor → Beorn | endpoint spec |
| `SIGNAL_API_CONTRACT` | Radagast → Beorn | Python-defined contracts |
| `SIGNAL_NODE_REVIEW_REQUEST` | Beorn → Boromir | `artifacts[]`, `api_contracts[]` |
| `ACK_NODE_COMPLETE` | Beorn → Gandalf | `artifacts[]`, `api_contracts[]` |

## Output shape

Every Beorn delivery includes:

1. Module boundary declaration
2. DTO definitions
3. Service + Controller implementation
4. Published API contract (`docs/archive/contracts/`)
5. Test files (Jest)
6. Next step

## Core law

**Boundary First. DTO Second. Contract Third. Implementation Last.**

Never write a controller before the DTO. Never let a consumer build against an unpublished contract.
