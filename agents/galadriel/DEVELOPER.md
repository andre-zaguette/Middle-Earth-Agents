# Developer Guide — Galadriel

## When to use

Invoke Galadriel for all UI/UX decisions: design system tokens, component specs, accessibility audits, Figma-to-code translation, CSS/Tailwind architecture, and UX flow definition.

Gandalf routes here via `SIGNAL_UI_TASK`. Galadriel delivers to Celebrimbor/Elrond via `SIGNAL_DESIGN_SPEC`.

## Activating in a project

### With Claude Code

Add to your project `CLAUDE.md`:

```markdown
## Galadriel — UI/UX Agent

Before any design decision, read:
- `<path-to-galadriel>/packages/galadriel/plugin/skills/galadriel/SKILL.md`

Palantír second brain:
- Architecture / ADR → `<path-to-palantir>/skills/architecture/SKILL.md`
- Code review → `<path-to-palantir>/skills/code-review/SKILL.md`
- Test planning (a11y) → `<path-to-palantir>/skills/testing/SKILL.md`
```

Or open a session inside `agents/galadriel/` — the `CLAUDE.md` already wires everything.

### With Figma MCP

Galadriel reads design specs directly from Figma. When a `figma_url` is provided in the signal payload, load `figma-use` skill first and use `get_design_context` to extract tokens, components, and layout before writing any CSS.

## Bootstrap

```bash
./scripts/wizard-bootstrap.sh
```

Checks: Git, AGENT.md, QUEST_PROGRESS.md, contexto.md, design token file presence.

## Operating sequence

1. **Eye of Sauron** — transcribe the vision textually first: components, colors, layout, spacing, states. Never write CSS before this step.
2. **Palantír check** — consult existing design tokens and component specs before creating new ones
3. **Token audit** — identify gaps between the design and the existing token system; never hardcode values
4. **Component states** — list all states: default, hover, focus, loading, error, empty, disabled
5. **Accessibility gate** — define WCAG 2.1 AA requirements: contrast, focus ring, ARIA roles, keyboard navigation
6. **Fellowship Contract** — emit `SIGNAL_DESIGN_SPEC` to Celebrimbor or Elrond with tokens, component spec, and a11y notes
7. **Mirror of Galadriel** — self-audit before signaling Boromir
8. **Signal Boromir** — `SIGNAL_UI_REVIEW_REQUEST` with artifacts

## Scripts

| Script | Command | Purpose |
|--------|---------|---------|
| Bootstrap | `./scripts/wizard-bootstrap.sh` | Load context and check harness health |
| Mirror | `python3 scripts/wizard-mirror.py` | Self-audit quality before delivery |
| Mithril Armor | `python3 scripts/mithril-armor.py` | Scan for hardcoded tokens, CSS shadows, XSS in rendered content |
| Gates of Argonath | `cp scripts/gates-of-argonath.sh .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit` | Install git pre-commit hook |

## Mirror of Galadriel — audit criteria

Score must be ≥ 80% before signaling Boromir:

1. **Vision Transcribed** — Eye of Sauron step completed before any CSS
2. **Token-First** — no hardcoded hex values, no magic numbers
3. **All States Covered** — default, hover, focus, loading, error, empty states documented
4. **Accessibility Gate** — WCAG 2.1 AA passed: contrast ratio, focus indicators, ARIA roles
5. **Design Spec Emitted** — `SIGNAL_DESIGN_SPEC` sent to implementation agents with full token map

## Signal protocols

| Signal | From / To | Payload |
|--------|-----------|---------|
| `SIGNAL_UI_TASK` | Gandalf → Galadriel | `context`, `stack`, `figma_url?` |
| `SIGNAL_DESIGN_SPEC` | Galadriel → Celebrimbor/Elrond | `tokens`, `component_spec`, `a11y_notes` |
| `SIGNAL_UI_REVIEW_REQUEST` | Galadriel → Boromir | `artifacts[]` |
| `ACK_UI_COMPLETE` | Galadriel → Gandalf | `artifacts[]` |

## Output shape

Every Galadriel delivery includes:

1. Visual transcription (Eye of Sauron)
2. Token map (new or updated)
3. Component states (all variants)
4. Accessibility requirements
5. `SIGNAL_DESIGN_SPEC` for implementation agents
6. Next step

## Core law

**Vision First. Then Tokens. Then Contract. Then Code.**

Never write CSS before transcribing the design. Never hardcode a value that belongs in the token system.
