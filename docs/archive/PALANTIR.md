# The Palantír Map: Middle-Earth-Agents

## 🏰 Citadel Pillars (God Nodes)
These files are central to the realm's architecture:
- `__future__`
- `importlib.util`

## 🗺️ Territory Map
- **Root**: WIZARD.md, DEVELOPER.md, .gitmodules, README.md, GEMINI.md, QUEST_PROGRESS.md, CLAUDE.md
- **.claude/**: settings.local.json
- **agents/**: 
  - **agents/beorn/**: AGENT.md, DEVELOPER.md, README.md, GEMINI.md, .git, CLAUDE.md
    - **agents/beorn/packages/**: 
      - **agents/beorn/packages/beorn/**: 
        - **agents/beorn/packages/beorn/core/**: routing.md, dialogue.md, patterns.md, persona.md
        - **agents/beorn/packages/beorn/plugin/**: 
          - **agents/beorn/packages/beorn/plugin/skills/**: 
            - **agents/beorn/packages/beorn/plugin/skills/beorn/**: SKILL.md
            - **agents/beorn/packages/beorn/plugin/skills/lint-and-precommit/**: SKILL.md
    - **agents/beorn/scripts/**: gates-of-argonath.sh, mithril-armor.py, lint.sh, wizard-mirror.py, wizard-bootstrap.sh
      - **agents/beorn/scripts/lint-templates/**: .prettierrc, .eslintignore, .eslintrc.json
  - **agents/bilbo/**: DEVELOPER.md, README.md, GEMINI.md, QUEST_PROGRESS.md
    - **agents/bilbo/agents/**: 
      - **agents/bilbo/agents/bilbo-baggins/**: AGENT.md, CLAUDE.md
    - **agents/bilbo/docs/**: 
      - **agents/bilbo/docs/archive/**: 
    - **agents/bilbo/packages/**: 
      - **agents/bilbo/packages/bilbo/**: manifest.json
        - **agents/bilbo/packages/bilbo/core/**: routing.md, dialogue.md, patterns.md, persona.md
        - **agents/bilbo/packages/bilbo/plugin/**: 
          - **agents/bilbo/packages/bilbo/plugin/skills/**: 
            - **agents/bilbo/packages/bilbo/plugin/skills/bilbo/**: SKILL.md
              - **agents/bilbo/packages/bilbo/plugin/skills/bilbo/references/**: routing-map.md, guiding-patterns.md, dialogue-style.md
        - **agents/bilbo/packages/bilbo/targets/**: 
          - **agents/bilbo/packages/bilbo/targets/claude/**: 
            - **agents/bilbo/packages/bilbo/targets/claude/.claude-plugin/**: marketplace.json, plugin.json
            - **agents/bilbo/packages/bilbo/targets/claude/bilbo/**: SKILL.md
              - **agents/bilbo/packages/bilbo/targets/claude/bilbo/assets/**: 
                - **agents/bilbo/packages/bilbo/targets/claude/bilbo/assets/templates/**: requirements.md, user-stories.md, contexto.md, open-questions.md
              - **agents/bilbo/packages/bilbo/targets/claude/bilbo/references/**: routing-map.md, guiding-patterns.md, dialogue-style.md
          - **agents/bilbo/packages/bilbo/targets/gemini/**: 
            - **agents/bilbo/packages/bilbo/targets/gemini/bilbo/**: 
    - **agents/bilbo/scripts/**: gates-of-argonath.sh, wizard-mirror.py, build-bilbo.py, wizard-bootstrap.sh
  - **agents/boromir/**: .gitkeep, DEVELOPER.md, README.md, GEMINI.md, .git
    - **agents/boromir/scripts/**: boromir-bootstrap.sh, horn-of-gondor.sh
  - **agents/celebrimbor/**: AGENT.md, DEVELOPER.md, README.md, GEMINI.md, .git, CLAUDE.md
    - **agents/celebrimbor/packages/**: 
      - **agents/celebrimbor/packages/celebrimbor/**: 
        - **agents/celebrimbor/packages/celebrimbor/core/**: routing.md, dialogue.md, patterns.md, persona.md
        - **agents/celebrimbor/packages/celebrimbor/plugin/**: 
          - **agents/celebrimbor/packages/celebrimbor/plugin/skills/**: 
            - **agents/celebrimbor/packages/celebrimbor/plugin/skills/celebrimbor/**: SKILL.md
            - **agents/celebrimbor/packages/celebrimbor/plugin/skills/lint-and-precommit/**: SKILL.md
    - **agents/celebrimbor/scripts/**: gates-of-argonath.sh, mithril-armor.py, lint.sh, wizard-mirror.py, wizard-bootstrap.sh
      - **agents/celebrimbor/scripts/lint-templates/**: .prettierrc, .eslintrc.json
  - **agents/cirdan/**: AGENT.md, DEVELOPER.md, README.md, GEMINI.md, CLAUDE.md
    - **agents/cirdan/packages/**: 
      - **agents/cirdan/packages/cirdan/**: 
        - **agents/cirdan/packages/cirdan/core/**: 
        - **agents/cirdan/packages/cirdan/plugin/**: 
    - **agents/cirdan/scripts/**: wizard-bootstrap.sh
  - **agents/elrond/**: AGENT.md, DEVELOPER.md, .gitmodules, README.md, GEMINI.md, .git, CLAUDE.md
    - **agents/elrond/packages/**: 
      - **agents/elrond/packages/elrond/**: 
        - **agents/elrond/packages/elrond/core/**: routing.md, dialogue.md, patterns.md, persona.md
        - **agents/elrond/packages/elrond/plugin/**: 
          - **agents/elrond/packages/elrond/plugin/skills/**: 
            - **agents/elrond/packages/elrond/plugin/skills/elrond/**: SKILL.md
            - **agents/elrond/packages/elrond/plugin/skills/lint-and-precommit/**: SKILL.md
    - **agents/elrond/scripts/**: gates-of-argonath.sh, mithril-armor.py, lint.sh, wizard-mirror.py, wizard-bootstrap.sh
      - **agents/elrond/scripts/lint-templates/**: .prettierrc, eslint.config.mjs
  - **agents/galadriel/**: AGENT.md, DEVELOPER.md, README.md, GEMINI.md, .git, CLAUDE.md
    - **agents/galadriel/packages/**: 
      - **agents/galadriel/packages/galadriel/**: 
        - **agents/galadriel/packages/galadriel/core/**: routing.md, dialogue.md, patterns.md, persona.md
        - **agents/galadriel/packages/galadriel/plugin/**: 
          - **agents/galadriel/packages/galadriel/plugin/skills/**: 
            - **agents/galadriel/packages/galadriel/plugin/skills/galadriel/**: SKILL.md
            - **agents/galadriel/packages/galadriel/plugin/skills/lint-and-precommit/**: SKILL.md
    - **agents/galadriel/scripts/**: gates-of-argonath.sh, mithril-armor.py, lint.sh, wizard-mirror.py, wizard-bootstrap.sh
      - **agents/galadriel/scripts/lint-templates/**: .stylelintrc.json, .prettierrc
  - **agents/gandalf/**: DEVELOPER.md, README.md, .gitignore, GEMINI.md, .git, QUEST_PROGRESS.md
    - **agents/gandalf/agents/**: 
      - **agents/gandalf/agents/gandalf-the-white/**: AGENT.md, CLAUDE.md
        - **agents/gandalf/agents/gandalf-the-white/references/**: operating-model.md
    - **agents/gandalf/docs/**: contexto.md
      - **agents/gandalf/docs/archive/**: PALANTIR.md, MAP.json
    - **agents/gandalf/packages/**: 
      - **agents/gandalf/packages/gandalf-the-grey/**: manifest.json
        - **agents/gandalf/packages/gandalf-the-grey/core/**: routing.md, dialogue.md, patterns.md, persona.md
          - **agents/gandalf/packages/gandalf-the-grey/core/assets/**: gandalf-grey-small.svg, gandalf-grey.svg
            - **agents/gandalf/packages/gandalf-the-grey/core/assets/templates/**: gates-of-argonath.sh, WIZARD.md, mithril-armor.py, RED_BOOK.md, CHRONICLE.md, wizard-archivist.py, wizard-mirror.py, CONTRACT.yaml, QUEST_PROGRESS.md, wizard-bootstrap.sh
        - **agents/gandalf/packages/gandalf-the-grey/plugin/**: 
          - **agents/gandalf/packages/gandalf-the-grey/plugin/skills/**: 
            - **agents/gandalf/packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/**: SKILL.md
              - **agents/gandalf/packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/agents/**: openai.yaml
              - **agents/gandalf/packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/assets/**: gandalf-grey-small.svg, gandalf-grey.svg
                - **agents/gandalf/packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/assets/templates/**: gates-of-argonath.sh, WIZARD.md, mithril-armor.py, RED_BOOK.md, CHRONICLE.md, wizard-archivist.py, wizard-mirror.py, CONTRACT.yaml, QUEST_PROGRESS.md, wizard-bootstrap.sh
              - **agents/gandalf/packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/references/**: routing-map.md, guiding-patterns.md, dialogue-style.md
        - **agents/gandalf/packages/gandalf-the-grey/targets/**: 
          - **agents/gandalf/packages/gandalf-the-grey/targets/claude/**: 
            - **agents/gandalf/packages/gandalf-the-grey/targets/claude/.claude-plugin/**: marketplace.json, plugin.json
            - **agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/**: SKILL.md
              - **agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/**: gandalf-grey-small.svg, gandalf-grey.svg
                - **agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/**: gates-of-argonath.sh, WIZARD.md, mithril-armor.py, RED_BOOK.md, CHRONICLE.md, wizard-archivist.py, wizard-mirror.py, CONTRACT.yaml, QUEST_PROGRESS.md, wizard-bootstrap.sh
              - **agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/references/**: routing-map.md, guiding-patterns.md, dialogue-style.md
          - **agents/gandalf/packages/gandalf-the-grey/targets/codex/**: 
            - **agents/gandalf/packages/gandalf-the-grey/targets/codex/.agents/**: 
              - **agents/gandalf/packages/gandalf-the-grey/targets/codex/.agents/plugins/**: marketplace.json
            - **agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/**: 
              - **agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/**: 
                - **agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/.codex-plugin/**: plugin.json
                - **agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/assets/**: gandalf-grey-small.svg, gandalf-grey.svg
                  - **agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/assets/templates/**: gates-of-argonath.sh, WIZARD.md, mithril-armor.py, RED_BOOK.md, CHRONICLE.md, wizard-archivist.py, wizard-mirror.py, CONTRACT.yaml, QUEST_PROGRESS.md, wizard-bootstrap.sh
                - **agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/**: 
                  - **agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/**: SKILL.md
                    - **agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/agents/**: openai.yaml
                    - **agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/assets/**: gandalf-grey-small.svg, gandalf-grey.svg
                      - **agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/assets/templates/**: gates-of-argonath.sh, WIZARD.md, mithril-armor.py, RED_BOOK.md, CHRONICLE.md, wizard-archivist.py, wizard-mirror.py, CONTRACT.yaml, QUEST_PROGRESS.md, wizard-bootstrap.sh
                    - **agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/references/**: routing-map.md, guiding-patterns.md, dialogue-style.md
          - **agents/gandalf/packages/gandalf-the-grey/targets/gemini/**: DEVELOPER.md, README.md
            - **agents/gandalf/packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/**: SKILL.md
              - **agents/gandalf/packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/**: 
                - **agents/gandalf/packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/templates/**: gates-of-argonath.sh, WIZARD.md, mithril-armor.py, RED_BOOK.md, CHRONICLE.md, wizard-archivist.py, wizard-mirror.py, CONTRACT.yaml, QUEST_PROGRESS.md, wizard-bootstrap.sh
              - **agents/gandalf/packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/bin/**: gandalf-check-update.sh
              - **agents/gandalf/packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/references/**: routing-map.md, guiding-patterns.md, dialogue-style.md
    - **agents/gandalf/scripts/**: build-gandalf.py, wizard-bootstrap.sh
    - **agents/gandalf/tests/**: test_archivist.py
  - **agents/narvi/**: DEVELOPER.md, README.md, SKILL.md, .git, CLAUDE.md
    - **agents/narvi/scripts/**: narvi-discover-allies.sh
    - **agents/narvi/templates/**: progress.md, bootstrap.sh, AGENTS.md
  - **agents/palantir/**: DEVELOPER.md, README.md, .gitignore, AGENTS.md, .git, CLAUDE.md
    - **agents/palantir/.agents/**: 
      - **agents/palantir/.agents/plugins/**: marketplace.json
    - **agents/palantir/.codex-plugins/**: 
      - **agents/palantir/.codex-plugins/caveman/**: 
        - **agents/palantir/.codex-plugins/caveman/.codex-plugin/**: plugin.json
        - **agents/palantir/.codex-plugins/caveman/assets/**: caveman-small.svg, caveman.svg
        - **agents/palantir/.codex-plugins/caveman/skills/**: 
          - **agents/palantir/.codex-plugins/caveman/skills/caveman/**: SKILL.md
            - **agents/palantir/.codex-plugins/caveman/skills/caveman/agents/**: openai.yaml
            - **agents/palantir/.codex-plugins/caveman/skills/caveman/assets/**: caveman-small.svg, caveman.svg
          - **agents/palantir/.codex-plugins/caveman/skills/compress/**: scripts, SKILL.md
    - **agents/palantir/.obsidian/**: app.json, core-plugins.json, graph.json, appearance.json
    - **agents/palantir/scripts/**: sb-sync.sh, link-agents.sh
    - **agents/palantir/skills/**: 
      - **agents/palantir/skills/architecture/**: SKILL.md
      - **agents/palantir/skills/code-review/**: SKILL.md
      - **agents/palantir/skills/codex-routing/**: SKILL.md
      - **agents/palantir/skills/debugging/**: SKILL.md
      - **agents/palantir/skills/refactoring/**: SKILL.md
      - **agents/palantir/skills/testing/**: SKILL.md
    - **agents/palantir/templates/**: adr.md
    - **agents/palantir/vault/**: README.md
      - **agents/palantir/vault/ADRs/**: 004-logging-observability.md, 002-access-policy.md, 008-quality-gates.md, 003-api-standards.md, 006-frontend-performance.md, 007-testing-strategy.md, 001-backup-policy.md, 005-frontend-standards.md
      - **agents/palantir/vault/Resources/**: Gandalf Guide.md, Codex Skills Caveman.md
  - **agents/radagast/**: AGENT.md, DEVELOPER.md, README.md, GEMINI.md, .git, CLAUDE.md
    - **agents/radagast/packages/**: 
      - **agents/radagast/packages/radagast/**: 
        - **agents/radagast/packages/radagast/core/**: routing.md, dialogue.md, patterns.md, persona.md
        - **agents/radagast/packages/radagast/plugin/**: 
          - **agents/radagast/packages/radagast/plugin/skills/**: 
            - **agents/radagast/packages/radagast/plugin/skills/lint-and-precommit/**: SKILL.md
            - **agents/radagast/packages/radagast/plugin/skills/radagast/**: SKILL.md
    - **agents/radagast/scripts/**: gates-of-argonath.sh, mithril-armor.py, lint.sh, wizard-mirror.py, wizard-bootstrap.sh
      - **agents/radagast/scripts/lint-templates/**: .pre-commit-config.yaml, pyproject.toml
- **docs/**: 
  - **docs/archive/**: PALANTIR.md, MAP.json
- **protocols/**: signals.md

## ⛓️ Ley Lines (Dependencies)
- `agents/radagast/scripts/mithril-armor.py` depends on: os
- `agents/radagast/scripts/wizard-mirror.py` depends on: sys
- `agents/galadriel/scripts/mithril-armor.py` depends on: os
- `agents/galadriel/scripts/wizard-mirror.py` depends on: sys
- `agents/celebrimbor/scripts/mithril-armor.py` depends on: os
- `agents/celebrimbor/scripts/wizard-mirror.py` depends on: sys
- `agents/elrond/scripts/mithril-armor.py` depends on: os
- `agents/elrond/scripts/wizard-mirror.py` depends on: sys
- `agents/gandalf/tests/test_archivist.py` depends on: tempfile, json, importlib.util, pathlib, unittest
- `agents/gandalf/scripts/build-gandalf.py` depends on: json, __future__, shutil, pathlib
- `agents/gandalf/packages/gandalf-the-grey/core/assets/templates/mithril-armor.py` depends on: os, re
- `agents/gandalf/packages/gandalf-the-grey/core/assets/templates/wizard-archivist.py` depends on: os, sys, json, pathlib, re
- `agents/gandalf/packages/gandalf-the-grey/core/assets/templates/wizard-mirror.py` depends on: sys
- `agents/gandalf/packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/templates/mithril-armor.py` depends on: os, re
- `agents/gandalf/packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/templates/wizard-archivist.py` depends on: os, sys, json, pathlib, re
- `agents/gandalf/packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/templates/wizard-mirror.py` depends on: sys
- `agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/mithril-armor.py` depends on: os, re
- `agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/wizard-archivist.py` depends on: os, sys, json, pathlib, re
- `agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/wizard-mirror.py` depends on: sys
- `agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/assets/templates/mithril-armor.py` depends on: os, re

## 📜 Rune Signatures (APIs)
### `agents/radagast/scripts/mithril-armor.py`
- `def scan(directory=".")`

### `agents/radagast/scripts/wizard-mirror.py`
- `def self_audit()`

### `agents/galadriel/scripts/mithril-armor.py`
- `def scan(directory=".")`

### `agents/galadriel/scripts/wizard-mirror.py`
- `def self_audit()`

### `agents/celebrimbor/scripts/mithril-armor.py`
- `def scan(directory=".")`

### `agents/celebrimbor/scripts/wizard-mirror.py`
- `def self_audit()`

### `agents/elrond/scripts/mithril-armor.py`
- `def scan(directory=".")`

### `agents/elrond/scripts/wizard-mirror.py`
- `def self_audit()`

### `agents/gandalf/tests/test_archivist.py`
- `class TestShouldIgnore(unittest.TestCase):`
- `class TestAnalyzeFile(unittest.TestCase):`
- `class TestIdentifyGodNodes(unittest.TestCase):`
- `class TestGenerateReports(unittest.TestCase):`
- `class TestScanIntegration(unittest.TestCase):`
- `def setUp(self)`
- `def test_ignores_git(self)`
- `def test_ignores_node_modules(self)`
- `def test_ignores_pycache(self)`
- `def test_does_not_ignore_src(self)`
- `def test_does_not_ignore_docs(self)`
- `def setUp(self)`
- `def tearDown(self)`
- `def _write(self, name, content)`
- `def test_python_class_and_def_extracted(self)`

### `agents/gandalf/scripts/build-gandalf.py`
- `def read_text(path: Path) -> str`
- `def write_text(path: Path, content: str) -> None`
- `def copy_file(src: Path, dst: Path) -> None`
- `def build_skill_md(meta: dict[str, str]) -> str`
- `def build_openai_yaml(meta: dict[str, str]) -> str`
- `def build_codex_plugin_json(meta: dict[str, str]) -> str`
- `def build_codex_marketplace() -> str`
- `def build_claude_plugin_json(meta: dict[str, str]) -> str`
- `def build_claude_marketplace(meta: dict[str, str]) -> str`
- `def build_gemini_readme() -> str`
- `def build_gemini_developer() -> str`
- `def build_gemini_update_script() -> str`
- `def generate()`

### `agents/gandalf/packages/gandalf-the-grey/core/assets/templates/mithril-armor.py`
- `def scan_for_shadows(directory=".")`

### `agents/gandalf/packages/gandalf-the-grey/core/assets/templates/wizard-archivist.py`
- `class WizardArchivist:`
- `def __init__(self, root_dir)`
- `def should_ignore(self, path)`
- `def scan(self)`
- `def analyze_file(self, rel_path)`
- `def identify_god_nodes(self)`
- `def generate_reports(self)`

### `agents/gandalf/packages/gandalf-the-grey/core/assets/templates/wizard-mirror.py`
- `def self_audit()`

### `agents/gandalf/packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/templates/mithril-armor.py`
- `def scan_for_shadows(directory=".")`

### `agents/gandalf/packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/templates/wizard-archivist.py`
- `class WizardArchivist:`
- `def __init__(self, root_dir)`
- `def should_ignore(self, path)`
- `def scan(self)`
- `def analyze_file(self, rel_path)`
- `def identify_god_nodes(self)`
- `def generate_reports(self)`

### `agents/gandalf/packages/gandalf-the-grey/targets/gemini/gandalf-the-grey/assets/templates/wizard-mirror.py`
- `def self_audit()`

### `agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/mithril-armor.py`
- `def scan_for_shadows(directory=".")`

### `agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/wizard-archivist.py`
- `class WizardArchivist:`
- `def __init__(self, root_dir)`
- `def should_ignore(self, path)`
- `def scan(self)`
- `def analyze_file(self, rel_path)`
- `def identify_god_nodes(self)`
- `def generate_reports(self)`

### `agents/gandalf/packages/gandalf-the-grey/targets/claude/gandalf-the-grey/assets/templates/wizard-mirror.py`
- `def self_audit()`

### `agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/assets/templates/mithril-armor.py`
- `def scan_for_shadows(directory=".")`

### `agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/assets/templates/wizard-archivist.py`
- `class WizardArchivist:`
- `def __init__(self, root_dir)`
- `def should_ignore(self, path)`
- `def scan(self)`
- `def analyze_file(self, rel_path)`
- `def identify_god_nodes(self)`
- `def generate_reports(self)`

### `agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/skills/gandalf-the-grey/assets/templates/wizard-mirror.py`
- `def self_audit()`

### `agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/assets/templates/mithril-armor.py`
- `def scan_for_shadows(directory=".")`

### `agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/assets/templates/wizard-archivist.py`
- `class WizardArchivist:`
- `def __init__(self, root_dir)`
- `def should_ignore(self, path)`
- `def scan(self)`
- `def analyze_file(self, rel_path)`
- `def identify_god_nodes(self)`
- `def generate_reports(self)`

### `agents/gandalf/packages/gandalf-the-grey/targets/codex/plugins/gandalf-the-grey/assets/templates/wizard-mirror.py`
- `def self_audit()`

### `agents/gandalf/packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/assets/templates/mithril-armor.py`
- `def scan_for_shadows(directory=".")`

### `agents/gandalf/packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/assets/templates/wizard-archivist.py`
- `class WizardArchivist:`
- `def __init__(self, root_dir)`
- `def should_ignore(self, path)`
- `def scan(self)`
- `def analyze_file(self, rel_path)`
- `def identify_god_nodes(self)`
- `def generate_reports(self)`

### `agents/gandalf/packages/gandalf-the-grey/plugin/skills/gandalf-the-grey/assets/templates/wizard-mirror.py`
- `def self_audit()`

### `agents/bilbo/scripts/wizard-mirror.py`
- `def self_audit()`

### `agents/bilbo/scripts/build-bilbo.py`
- `def read_text(path: Path) -> str`
- `def write_text(path: Path, content: str) -> None`
- `def copy_file(src: Path, dst: Path) -> None`
- `def build_skill_md(meta: dict[str, str]) -> str`
- `def build_claude_skill_md(meta: dict[str, str]) -> str`
- `def build_claude_plugin_json(meta: dict[str, str]) -> str`
- `def build_claude_marketplace(meta: dict[str, str]) -> str`
- `def generate()`

