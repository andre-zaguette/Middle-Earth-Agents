# Skill: Codex Routing

## When to use
Use when task mention Codex skills, agent routing, stack choice, or "which skill first?"

## Goal
Route fast. Few words. No reread 34 files unless needed.

## Procedure
1. Read `vault/Resources/Codex Skills Caveman.md`.
2. Pick broad entry skill first if stack/problem still fuzzy.
3. Narrow to framework skill when stack clear.
4. Add testing skill when coverage choice matter.
5. Add design, browser, Figma, doc, or security skill only if task truly need it.
6. If Figma use `use_figma`, load `figma-use` first. Mandatory.

## Routing rules
- Backend broad -> `backend-engineering`
- Frontend broad -> `frontend-engineering`
- Python broad -> `python-engineering`
- Test level unclear -> `unit-vs-integration-testing`
- React bug/UI work -> `react`
- Next route/render/data work -> `nextjs` or `react-next`
- Django work -> `django`
- FastAPI work -> `fastapi`
- Flask work -> `flask`
- Nest work -> `nestjs`
- Py tests -> `pytest`
- JS/TS tests -> `vitest-jest`
- Nest tests -> `nestjs-testing`
- Figma read/write -> `figma`, plus `figma-use` before `use_figma`
- Figma to code -> `figma-implement-design`
- Code to Figma screen -> `figma-generate-design`
- Browser automation/UI debug -> `playwright` or `playwright-interactive`
- Security review -> `security-best-practices`
- Threat model -> `security-threat-model`

## Output
- Chosen skill path
- Why this path
- What optional secondary skill join next
