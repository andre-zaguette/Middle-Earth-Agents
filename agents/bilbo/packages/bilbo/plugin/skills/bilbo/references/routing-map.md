# Routing Map

# Routing — Bilbo Baggins

## Incoming signals

| Signal | From | Trigger |
|--------|------|---------|
| `SIGNAL_SCOPE_QUEST` | Gandalf or user | New project or feature needs scoping and documentation |
| `SIGNAL_REDOC_REQUEST` | Gandalf | Existing project needs documentation update or requirements review |

## Outgoing signals

| Signal | To | Payload |
|--------|-----|---------|
| `SIGNAL_PROJECT_SCOPED` | Gandalf | `context`, `requirements[]`, `acceptance_criteria[]`, `agents_required[]`, `open_questions[]` |

## Classification sequence

Before acting, Bilbo classifies the quest:

1. **New project?** → Full journey (all 8 patterns)
2. **New feature on existing project?** → Abbreviated journey (Riddles + Map + Red Book)
3. **Documentation update?** → Red Book only
4. **Scope dispute?** → One Ring Test + There and Back Again

## Routing rules after scoping

Once `SIGNAL_PROJECT_SCOPED` is emitted, Gandalf routes based on `agents_required[]`:

| Need identified | Agent |
|-----------------|-------|
| UI/UX requirements | Galadriel |
| Python backend | Radagast |
| Vue/Nuxt frontend | Elrond |
| React/Next frontend | Celebrimbor |
| Node/NestJS API | Beorn |
| Quality verification | Boromir |
| Cross-stack | Gandalf coordinates |

## What Bilbo does NOT route

Bilbo does not route technical decisions. He documents them after they are made by the specialist agents.
