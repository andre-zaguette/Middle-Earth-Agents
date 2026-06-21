# Developer Guide — Middle-Earth Agents

Practical guide for using the fellowship in a project. For a system overview see `README.md`. For agent-specific guides see `agents/<agent>/DEVELOPER.md`.

## Prerequisites

```bash
git clone --recurse-submodules https://github.com/andre-zaguette/Middle-Earth-Agents.git
cd Middle-Earth-Agents
```

If you cloned without `--recurse-submodules`:

```bash
git submodule update --init --recursive
```

## Setting up a new project

### 1. Link the Palantír (second brain)

```bash
./agents/palantir/scripts/link-agents.sh
```

This makes `skills/` available to all agents via relative paths.

### 2. Install the Wizard Harness in your project

Copy the bootstrap templates from Gandalf into your project root:

```bash
cp agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/WIZARD.md <your-project>/
cp agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/QUEST_PROGRESS.md <your-project>/
cp agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/wizard-bootstrap.sh <your-project>/scripts/
cp agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/wizard-mirror.py <your-project>/scripts/
cp agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/mithril-armor.py <your-project>/scripts/
```

### 3. Add Gandalf to your project CLAUDE.md

```markdown
## Gandalf the White — Orchestrator

Before any decision, read:
- `<path>/agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/SKILL.md`
- `<path>/agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/references/guiding-patterns.md`
- `<path>/agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/references/routing-map.md`

Palantír second brain — consult before acting:
- `<path>/agents/palantir/skills/architecture/SKILL.md`
- `<path>/agents/palantir/skills/code-review/SKILL.md`
- `<path>/agents/palantir/skills/debugging/SKILL.md`
- `<path>/agents/palantir/skills/refactoring/SKILL.md`
- `<path>/agents/palantir/skills/testing/SKILL.md`
- `<path>/agents/palantir/skills/codex-routing/SKILL.md`
```

### 4. Add the Git hook (Gates of Argonath)

```bash
cp agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/gates-of-argonath.sh <your-project>/.git/hooks/pre-commit
chmod +x <your-project>/.git/hooks/pre-commit
```

## Running a quest

Every session starts with Gandalf. He names the quest, identifies the danger, and routes to the right agent.

### Step 1 — Bootstrap

```bash
./scripts/wizard-bootstrap.sh
```

Checks harness health: Git, mandates, progress log, context file.

### Step 2 — Map the quest

For non-trivial work, create `docs/contexto.md`:

```markdown
## Quest
One sentence describing what we're building.

## Danger
What breaks if this ships wrong.

## Scope
Which agent(s) own this.

## Proof
How we will know this works.
```

### Step 3 — Route to the right agent

| Task | Agent | How to activate |
|------|-------|-----------------|
| UI, design, Figma, a11y | Galadriel | Open `agents/galadriel/` in Claude Code |
| Python, FastAPI, data | Radagast | Open `agents/radagast/` in Claude Code |
| Vue, Nuxt, Pinia | Elrond | Open `agents/elrond/` in Claude Code |
| React, Next.js | Celebrimbor | Open `agents/celebrimbor/` in Claude Code |
| Node.js, NestJS, APIs | Beorn | Open `agents/beorn/` in Claude Code |
| Tests, quality gate | Boromir | Run `./scripts/horn-of-gondor.sh "<context>"` |

Each agent's `CLAUDE.md` loads its skill and Palantír references automatically when you open that directory in Claude Code.

### Step 4 — Quality gate

When an agent finishes, signal Boromir:

```bash
./agents/boromir/scripts/horn-of-gondor.sh "Feature X complete — NestJS auth module with JWT guards"
```

No merge until Boromir approves.

### Step 5 — Close the quest

Update `QUEST_PROGRESS.md` before ending the session. Record what was built, decisions made (ADRs), and lessons learned.

## Cross-stack quests

When a quest spans multiple agents (e.g. a new feature needs UI + API + backend), Gandalf coordinates:

1. Galadriel defines design spec → emits `SIGNAL_DESIGN_SPEC`
2. Beorn/Radagast define API contract → publish to `docs/archive/contracts/`
3. Celebrimbor/Elrond consume contract + design spec → implement
4. Boromir verifies all layers → approves merge

## Agent developer guides

| Agent | Guide |
|-------|-------|
| Gandalf | `agents/gandalf/DEVELOPER.md` |
| Galadriel | `agents/galadriel/DEVELOPER.md` |
| Radagast | `agents/radagast/DEVELOPER.md` |
| Elrond | `agents/elrond/DEVELOPER.md` |
| Celebrimbor | `agents/celebrimbor/DEVELOPER.md` |
| Beorn | `agents/beorn/DEVELOPER.md` |
| Boromir | `agents/boromir/DEVELOPER.md` |
| Palantír | `agents/palantir/DEVELOPER.md` |

## Core laws (enforced)

| Law | Enforcement |
|-----|-------------|
| Palantír First | CLAUDE.md loads Palantír skills before any action |
| Context First | `docs/contexto.md` required for non-trivial quests |
| Proof Before Alloy | Boromir's horn must be answered before merge |
| Harness Integrity | `QUEST_PROGRESS.md` updated every session |
| Mithril Armor | Security scan runs before any `SIGNAL_*_REVIEW_REQUEST` |
