# Middle-Earth Agents

Command and control repository for the agentic development workflow. Orchestrates collaboration between specialized agents to deliver high-quality, scalable software.

**Orchestrator:** Gandalf the White — routes quests, enforces protocols, coordinates the fellowship.

## The Fellowship

| Agent | Role | Domain | Signal |
|-------|------|--------|--------|
| [**Gandalf**](agents/gandalf/README.md) | Orchestrator | Architecture, routing, harness | — |
| [**Bilbo**](agents/bilbo/README.md) | PM/PO | Requirements, scope, user stories, documentation | `SIGNAL_SCOPE_QUEST` |
| [**Galadriel**](agents/galadriel/README.md) | UI/UX | Design system, a11y, CSS/Tailwind, Figma | `SIGNAL_UI_TASK` |
| [**Radagast**](agents/radagast/README.md) | Python | FastAPI, Django, data, automation | `SIGNAL_PYTHON_TASK` |
| [**Elrond**](agents/elrond/README.md) | Vue.js / Nuxt | Vue 3, Composition API, Pinia, Nuxt 3 | `SIGNAL_VUE_TASK` |
| [**Celebrimbor**](agents/celebrimbor/README.md) | React / Next.js | React 18, Next.js App Router, Server Components | `SIGNAL_REACT_TASK` |
| [**Beorn**](agents/beorn/README.md) | Node.js / NestJS | NestJS, APIs, queues, WebSockets | `SIGNAL_NODE_TASK` |
| [**Boromir**](agents/boromir/README.md) | Quality & Tests | Autonomous verification, CI/CD gate | `SIGNAL_BREACH_DEFENSE` |
| [**Narvi**](agents/narvi/README.md) | Craft & Alliances | BDD, TDD, Harness, cross-project impact mapping | `SIGNAL_CRAFT_FORGE` |
| [**Palantír**](agents/palantir/README.md) | Universal Archive | API contracts, patterns, ADRs | — |

## Core Laws

- **Palantír First.** Every agent consults the archive before acting.
- **Context First.** All non-trivial changes require `docs/contexto.md`.
- **Proof Before Alloy.** No code is merged without Boromir's sign-off.
- **Harness Integrity.** Every session ends with an updated `QUEST_PROGRESS.md`.

## Quest Lifecycle

```
Gandalf receives quest
  → routes to Bilbo (scope + requirements)
  → Bilbo emits SIGNAL_PROJECT_SCOPED
  → Gandalf routes to specialist agent(s)
  → agent delivers + signals Boromir
  → Boromir gates the merge
  → Gandalf logs to QUEST_PROGRESS.md
```

## Getting Started

Invoke Gandalf to map your quest. He will classify the scope and route to the appropriate specialist agent.

```
Quest → Gandalf → [Galadriel | Radagast | Elrond | Celebrimbor | Beorn] → Boromir → merge
               ↘ Narvi (harness audit, BDD setup, cross-project impact map)
```
