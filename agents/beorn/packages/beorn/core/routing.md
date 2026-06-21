# Routing

Every Node/NestJS quest follows this classification:

1. **Harness Check:** Does the project have NestJS modules, DTOs, and a test suite?
   - If ✗: Route to `Harness Construction`.
2. **Boundary Check:** Which module owns this feature? Is it a new module or an existing one?
   - New module → Define boundary and imports first.
   - Existing → Check for circular dependency risk.
3. **Contract Check:** Is the API contract published to the Palantír?
   - If ✗: Design DTO and publish before building.
4. **Consumer Check:** Who consumes this endpoint? Celebrimbor? Elrond? Radagast?
   - Signal consuming agents after contract is published.

Roads:

- New Endpoint -> DTO design -> Auth guard -> Controller -> Service -> Tests -> Publish contract.
- New Module -> Boundary definition -> Module imports/exports -> Service + Controller -> Tests.
- New Queue Job -> DTO -> Processor -> Dead-letter policy -> Idempotency -> Tests.
- Database Migration -> Schema design -> Migration file -> Seed if needed -> Integration tests.
- Bug Hunt -> Reproduce with tests -> Fix under test protection -> Red Book if lesson learned.
- Refactor -> TDD protection first -> Module isolation audit -> Strangler Fig if legacy.
- Security Audit -> Mithril Armor scan -> Auth guard audit -> Input validation check.
