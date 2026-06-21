#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BILBO = ROOT / "packages" / "bilbo"
CORE = BILBO / "core"
PLUGIN = BILBO / "plugin"
TARGETS = BILBO / "targets"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.resolve() != dst.resolve():
        shutil.copyfile(src, dst)


def build_skill_md(meta: dict[str, str]) -> str:
    persona = read_text(CORE / "persona.md")
    patterns = read_text(CORE / "patterns.md")
    routing = read_text(CORE / "routing.md")
    dialogue = read_text(CORE / "dialogue.md")
    return f"""---
name: {meta['name']}
description: {meta['codex_plugin_description']}
---

# Bilbo Baggins

{persona}

## Core law

**The map must be drawn before the journey begins.**

No agent builds without `docs/contexto.md`. Bilbo writes it.

## Canonical patterns

Read `references/guiding-patterns.md` when pattern choice needs grounding.

{patterns}

## Routing

Read `references/routing-map.md` when task needs classification.

{routing}

## Dialogue

Read `references/dialogue-style.md` for communication style.

{dialogue}

## Output shape

- `docs/contexto.md` — project brief and context
- `docs/requirements.md` — structured requirements list
- `docs/user-stories.md` — user stories with acceptance criteria
- `docs/open-questions.md` — tracked open items
- `SIGNAL_PROJECT_SCOPED` payload for Gandalf
"""


def build_claude_skill_md(meta: dict[str, str]) -> str:
    persona = read_text(CORE / "persona.md")
    patterns = read_text(CORE / "patterns.md")
    routing = read_text(CORE / "routing.md")
    dialogue = read_text(CORE / "dialogue.md")
    return f"""---
name: {meta['name']}
description: {meta['claude_plugin_description']}
---

# Bilbo Baggins

{persona}

## Core law

**The map must be drawn before the journey begins.**

## Canonical patterns

Read `references/guiding-patterns.md` when pattern choice needs grounding.

{patterns}

## Routing

Read `references/routing-map.md` when task needs classification.

{routing}

## Palantír — Second Brain

Consult before acting:

| Situation | Skill |
|-----------|-------|
| Architecture constraint / ADR | `../../../../../palantir/skills/architecture/SKILL.md` |
| Code review of documentation PR | `../../../../../palantir/skills/code-review/SKILL.md` |
| Routing — which agent first? | `../../../../../palantir/skills/codex-routing/SKILL.md` |

## Dialogue

Read `references/dialogue-style.md` for communication style.

{dialogue}

## Fellowship Routing

After emitting `SIGNAL_PROJECT_SCOPED`, Gandalf routes based on `agents_required[]`:

| Requirement type | Agent | Signal |
|-----------------|-------|--------|
| UI, design, a11y, Figma | Galadriel | `SIGNAL_UI_TASK` |
| Python, FastAPI, data | Radagast | `SIGNAL_PYTHON_TASK` |
| Vue, Nuxt | Elrond | `SIGNAL_VUE_TASK` |
| React, Next.js | Celebrimbor | `SIGNAL_REACT_TASK` |
| Node, NestJS, API | Beorn | `SIGNAL_NODE_TASK` |
| Quality gate | Boromir | `SIGNAL_BREACH_DEFENSE` |

## Output shape

- `docs/contexto.md` — project brief and context
- `docs/requirements.md` — structured requirements list
- `docs/user-stories.md` — user stories with acceptance criteria
- `docs/open-questions.md` — tracked open items
- `SIGNAL_PROJECT_SCOPED` payload for Gandalf
"""


def build_claude_plugin_json(meta: dict[str, str]) -> str:
    data = {
        "name": meta["name"],
        "description": meta["claude_plugin_description"],
        "author": {"name": meta["author_name"], "url": meta["author_url"]},
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def build_claude_marketplace(meta: dict[str, str]) -> str:
    data = {
        "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
        "name": "bilbo",
        "description": meta["claude_plugin_description"],
        "owner": {"name": meta["author_name"], "url": meta["author_url"]},
        "plugins": [
            {
                "name": "bilbo",
                "description": "Bilbo Baggins PM/PO plugin. Requirements, scope, docs before any code.",
                "source": "./",
                "category": "productivity",
            }
        ],
    }
    return json.dumps(data, indent=2, ensure_ascii=False)


def generate():
    meta = json.loads((BILBO / "manifest.json").read_text(encoding="utf-8"))

    skill_md = build_skill_md(meta)
    claude_skill_md = build_claude_skill_md(meta)

    guiding = "# Guiding Patterns\n\n" + read_text(CORE / "patterns.md")
    routing = "# Routing Map\n\n" + read_text(CORE / "routing.md")
    dialogue = "# Dialogue Style\n\n" + read_text(CORE / "dialogue.md")

    templates_src = TARGETS / "claude" / "bilbo" / "assets" / "templates"
    template_files = [
        "contexto.md",
        "requirements.md",
        "user-stories.md",
        "open-questions.md",
    ]

    # Plugin target
    skill_root = PLUGIN / "skills" / "bilbo"
    write_text(skill_root / "SKILL.md", skill_md)
    write_text(skill_root / "references" / "guiding-patterns.md", guiding)
    write_text(skill_root / "references" / "routing-map.md", routing)
    write_text(skill_root / "references" / "dialogue-style.md", dialogue)

    # Claude target
    claude_root = TARGETS / "claude"
    write_text(claude_root / ".claude-plugin" / "plugin.json", build_claude_plugin_json(meta))
    write_text(claude_root / ".claude-plugin" / "marketplace.json", build_claude_marketplace(meta))
    write_text(claude_root / "bilbo" / "SKILL.md", claude_skill_md)
    write_text(claude_root / "bilbo" / "references" / "guiding-patterns.md", guiding)
    write_text(claude_root / "bilbo" / "references" / "routing-map.md", routing)
    write_text(claude_root / "bilbo" / "references" / "dialogue-style.md", dialogue)
    for f in template_files:
        if (templates_src / f).exists():
            copy_file(templates_src / f, claude_root / "bilbo" / "assets" / "templates" / f)


if __name__ == "__main__":
    generate()
    print("Generated Bilbo Baggins plugin and Claude target")
