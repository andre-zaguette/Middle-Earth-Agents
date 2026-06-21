# Developer Guide — Elrond

## When to use

Invoke Elrond when the task involves Vue.js or Nuxt: components, composables, Pinia stores, Vue Router, SSR/SSG pages, or any Vue 3 Composition API work.

Gandalf routes here via `SIGNAL_VUE_TASK`. Galadriel sends design specs via `SIGNAL_DESIGN_SPEC`.

## Activating in a project

### With Claude Code

Add to your project `CLAUDE.md`:

```markdown
## Elrond — Vue/Nuxt Agent

Before any Vue/Nuxt decision, read:
- `<path-to-elrond>/packages/elrond/plugin/skills/elrond/SKILL.md`

Palantír second brain:
- Architecture / ADR → `<path-to-palantir>/skills/architecture/SKILL.md`
- Code review → `<path-to-palantir>/skills/code-review/SKILL.md`
- Debugging → `<path-to-palantir>/skills/debugging/SKILL.md`
- Refactoring → `<path-to-palantir>/skills/refactoring/SKILL.md`
- Test planning → `<path-to-palantir>/skills/testing/SKILL.md`
```

Or open a session inside `agents/elrond/` — the `CLAUDE.md` already wires everything.

## Bootstrap

```bash
./scripts/wizard-bootstrap.sh
```

Checks: Git, AGENT.md, QUEST_PROGRESS.md, contexto.md, package.json, Nuxt config, TypeScript strict mode, Vitest.

## Operating sequence

1. **Palantír check** — consult existing composables and stores before creating new ones
2. **State ownership** — decide: local ref / shared Pinia store / server state before writing any code
3. **Data strategy** — decide: `useAsyncData` / `useLazyAsyncData` / `$fetch` with explicit justification
4. **Design spec** — wait for `SIGNAL_DESIGN_SPEC` from Galadriel if the task has UI requirements
5. **API contract** — validate the endpoint contract before consuming
6. **Tests first** — Vitest + Vue Testing Library before implementation
7. **Implement** — `<script setup>` only, no Options API, no `v-html` without explicit sanitization
8. **Mithril Armor** — scan before signaling Boromir
9. **Signal Boromir** — `SIGNAL_VUE_REVIEW_REQUEST` with artifacts

## Scripts

| Script | Command | Purpose |
|--------|---------|---------|
| Bootstrap | `./scripts/wizard-bootstrap.sh` | Load context and check harness health |
| Mirror | `python3 scripts/wizard-mirror.py` | Self-audit quality before delivery |
| Mithril Armor | `python3 scripts/mithril-armor.py` | Scan for `v-html`, `any` types, fetch without SSR guard |
| Gates of Argonath | `cp scripts/gates-of-argonath.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit` | Install git pre-commit hook |

## Mirror of Galadriel — audit criteria

Score must be ≥ 80% before signaling Boromir:

1. **Composition API Only** — `<script setup>` used, no Options API
2. **State Ownership** — state location explicitly decided (local / Pinia / server)
3. **Reactivity Discipline** — correct use of `ref`, `reactive`, `computed`; no unnecessary watchers
4. **Contract-First** — props, emits, and slots typed and documented
5. **Proof Before Alloy** — Vitest + Vue Testing Library tests cover key behavior

## Signal protocols

| Signal | From / To | Payload |
|--------|-----------|---------|
| `SIGNAL_VUE_TASK` | Gandalf → Elrond | `context`, `nuxt?`, `api_contracts?` |
| `SIGNAL_DESIGN_SPEC` | Galadriel → Elrond | `tokens`, `component_spec`, `a11y_notes` |
| `SIGNAL_VUE_REVIEW_REQUEST` | Elrond → Boromir | `artifacts[]` |
| `ACK_VUE_COMPLETE` | Elrond → Gandalf | `artifacts[]` |

## Output shape

Every Elrond delivery includes:

1. State ownership decision
2. Data strategy (`useAsyncData` / `useLazyAsyncData` / `$fetch`)
3. Component with `<script setup>`
4. Composables / Pinia store (if applicable)
5. Test file (Vitest)
6. Next step

## Core law

**State Ownership First. Contract Second. Composition Third. Implementation Last.**

Never write a component without declaring where its state lives. Never use Options API.
