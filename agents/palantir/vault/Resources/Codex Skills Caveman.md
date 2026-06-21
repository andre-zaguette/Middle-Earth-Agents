# Codex Skills Caveman

Source: `/Users/andreaugustozaguettefernandes/.codex/skills`

Compiled: `2026-05-08`

Goal: few word. same meaning. fast route.

Total: `34` skills.

## Core rule

- Broad backend task -> start `backend-engineering`.
- Broad frontend task -> start `frontend-engineering`.
- Python general task -> start `python-engineering`.
- Test-level unclear -> start `unit-vs-integration-testing`.
- Figma write/read via JS -> load `figma-use` first. Always.
- Security skill only when user ask security/threat model/secure-by-default.

## Route map

### Architecture

- `architecture-and-testing`: boundaries, design quality, TDD, test strategy.
- `ddd-tactical-patterns`: aggregates, entities, value objects, invariants.

### Backend entry

- `backend-engineering`: choose backend path.
- `python-engineering`: choose Python path.
- `nodejs-backend`: Node/TS backend services.
- `node-nest-backend`: Node backend with Nest flavor.

### Python backend

- `python-backend`: services, APIs, repos, jobs.
- `fastapi-django-flask`: Python web stack, framework not narrowed yet.
- `fastapi`: routers, Pydantic, DI, async boundaries.
- `django`: ORM, DRF, forms, admin, signals.
- `flask`: blueprints, app factory, config, extensions.

### Nest backend

- `nestjs`: modules, controllers, providers, DTOs, guards, interceptors.
- `nestjs-testing`: Nest unit/integration coverage.

### Frontend entry

- `frontend-engineering`: choose frontend path.
- `frontend-react-next-vue`: broad React/Next/Vue work.

### React / Next / Vue

- `react`: components, hooks, state, forms, tests.
- `react-next`: React + Next mixed concern.
- `nextjs`: routes, server/client components, data, caching, server actions.
- `vue`: components, composables, stores, emits, watchers, tests.

### UI / design

- `design-engineering`: hierarchy, UX polish, design-to-code judgment.
- `frontend-skill`: bold landing page/app/prototype UI. no generic sludge.

### Testing

- `unit-vs-integration-testing`: choose smallest honest test.
- `pytest`: Python tests, fixtures, parametrization, regressions.
- `vitest-jest`: JS/TS tests, mocks, component tests.

### Figma / browser

- `figma`: read design context/assets/variables.
- `figma-use`: mandatory before `use_figma`.
- `figma-generate-design`: code/description -> Figma screen.
- `figma-implement-design`: Figma -> production UI code.
- `playwright`: browser automation, screenshots, UI debug.
- `playwright-interactive`: persistent browser/Electron debug loop.

### Docs / notebooks / security

- `doc`: `.docx` create/edit/review with render check.
- `jupyter-notebook`: create/edit notebook.
- `security-best-practices`: explicit secure coding review/guidance only.
- `security-threat-model`: explicit repo/path threat model only.

## Fast choose by ask

- "refactor backend" -> `backend-engineering`, then stack skill.
- "build API" -> `python-backend` or `nodejs-backend`, then framework skill.
- "fix Django query/view/admin" -> `django`.
- "fix FastAPI route/model/dependency" -> `fastapi`.
- "fix React state/render bug" -> `react`.
- "implement Next page/route/server action" -> `nextjs` or `react-next`.
- "build strong landing page" -> `frontend-skill` + `design-engineering`.
- "write tests but unsure level" -> `unit-vs-integration-testing`, then `pytest` or `vitest-jest` or `nestjs-testing`.
- "implement from Figma" -> `figma-implement-design`.
- "write/update screen in Figma" -> `figma-use` + `figma-generate-design`.
- "browser flow debug" -> `playwright` or `playwright-interactive`.
- "security review" -> `security-best-practices`.
- "threat model repo" -> `security-threat-model`.

## Second-brain use

- Keep this note as quick router.
- Keep source skills outside repo as full manual.
- Mirror only repeated rules into local `skills/`.
- Recompile when new folder appears under `/Users/andreaugustozaguettefernandes/.codex/skills`.
