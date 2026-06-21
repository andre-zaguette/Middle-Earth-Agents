# Developer Guide — Celebrimbor

## When to use

Invoke Celebrimbor when the task involves React or Next.js: components, pages, Server Components, Server Actions, Route Handlers, or any frontend TypeScript work in the App Router.

Gandalf routes here via `SIGNAL_REACT_TASK`. Galadriel sends design specs via `SIGNAL_DESIGN_SPEC`.

## Activating in a project

### With Claude Code

Add to your project `CLAUDE.md`:

```markdown
## Celebrimbor — React/Next.js Agent

Before any React/Next decision, read:
- `<path-to-celebrimbor>/packages/celebrimbor/plugin/skills/celebrimbor/SKILL.md`

Palantír second brain:
- Architecture / ADR → `<path-to-palantir>/skills/architecture/SKILL.md`
- Code review → `<path-to-palantir>/skills/code-review/SKILL.md`
- Debugging → `<path-to-palantir>/skills/debugging/SKILL.md`
- Refactoring → `<path-to-palantir>/skills/refactoring/SKILL.md`
- Test planning → `<path-to-palantir>/skills/testing/SKILL.md`
```

Or open a session inside `agents/celebrimbor/` — the `CLAUDE.md` already wires everything.

## Bootstrap

```bash
./scripts/wizard-bootstrap.sh
```

Checks: Git, AGENT.md, QUEST_PROGRESS.md, contexto.md, package.json, Next.js config, TypeScript strict mode, Vitest.

## Operating sequence

1. **Palantír check** — consult existing component contracts before creating new ones
2. **Boundary classification** — declare server or client component with explicit justification
3. **Data strategy** — decide: static / dynamic / cached / streaming before writing any fetch
4. **Design spec** — wait for `SIGNAL_DESIGN_SPEC` from Galadriel if the task has UI requirements
5. **API contract** — validate the endpoint contract from Beorn or Radagast before consuming
6. **TypeScript interfaces** — define props, return types, and server/client boundaries
7. **Tests first** — Vitest + React Testing Library before implementation
8. **Implement** — code under test protection, no `any`, no `dangerouslySetInnerHTML`
9. **Mithril Armor** — scan before signaling Boromir
10. **Signal Beorn** — `SIGNAL_API_NEEDED` if a new endpoint is required
11. **Signal Boromir** — `SIGNAL_REACT_REVIEW_REQUEST` with artifacts

## Scripts

| Script | Command | Purpose |
|--------|---------|---------|
| Bootstrap | `./scripts/wizard-bootstrap.sh` | Load context and check harness health |
| Mirror | `python3 scripts/wizard-mirror.py` | Self-audit quality before delivery |
| Mithril Armor | `python3 scripts/mithril-armor.py` | Scan for `dangerouslySetInnerHTML`, exposed env vars, uncached fetch, `any` |
| Gates of Argonath | `cp scripts/gates-of-argonath.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit` | Install git pre-commit hook |

## Mirror of Galadriel — audit criteria

Score must be ≥ 80% before signaling Boromir:

1. **Server-First** — every component defaults to Server Component; `"use client"` has written justification
2. **Data Strategy** — fetch strategy explicitly decided (static/dynamic/cached)
3. **Type Contract** — no `any`, no unnecessary type assertions
4. **Proof Before Alloy** — Vitest + RTL tests cover happy path and key edge cases
5. **Mithril Armor** — scan executed, no XSS vectors, no exposed secrets

## Signal protocols

| Signal | From / To | Payload |
|--------|-----------|---------|
| `SIGNAL_REACT_TASK` | Gandalf → Celebrimbor | `context`, `nextjs?`, `api_contracts?` |
| `SIGNAL_DESIGN_SPEC` | Galadriel → Celebrimbor | `tokens`, `component_spec`, `a11y_notes` |
| `SIGNAL_REACT_REVIEW_REQUEST` | Celebrimbor → Boromir | `artifacts[]` |
| `SIGNAL_API_NEEDED` | Celebrimbor → Beorn | endpoint spec |
| `ACK_REACT_COMPLETE` | Celebrimbor → Gandalf | `artifacts[]` |

## Output shape

Every Celebrimbor delivery includes:

1. Boundary classification (server/client + justification)
2. Data strategy decision
3. TypeScript interfaces
4. Component implementation
5. Test file (Vitest + RTL)
6. Next step

## Core law

**Classify the Boundary First. Data Strategy Second. Type Contract Third. Implementation Last.**

Never write `"use client"` without justification. Never fetch without a declared strategy.
