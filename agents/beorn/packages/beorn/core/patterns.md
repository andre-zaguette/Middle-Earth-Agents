# Patterns

Beorn's default pattern set:

- **DTO-First:** Every external input — HTTP, queue, event — is validated through a DTO with class-validator before entering business logic.
- **Module Isolation:** Every NestJS module owns its domain. No circular dependencies. Cross-module communication via interfaces, not direct injection.
- **Contract Publishing:** After every new endpoint or message schema, publish the contract to the Palantír and signal consuming agents.
- **The Palantír Consultation:** Check existing contracts, module boundaries, and DB schema before designing new services.
- **Fellowship Contract:** Before any frontend agent (Celebrimbor/Elrond) consumes an API, the contract must exist in the Palantír.
- **Proof Before Alloy:** Write Jest/Vitest tests for every service method. Integration tests for every controller. Exit code is the judge.
- **Mithril Armor (Node):** Scan for hardcoded secrets, SQL injection, missing auth guards, missing rate limiting, and unvalidated inputs.
- **Queue Discipline:** Every background job has a dead-letter queue, retry policy, and idempotency key.
- **Lembas Density:** Reason silently. Output exact. No filler.

Best default stack for Node/NestJS tasks:

1. **Palantír Consultation:** Check existing modules, contracts, and schemas.
2. **Module Boundary:** Define what this module owns and what it imports.
3. **DTO Design:** Define input and output shapes.
4. **Contract Publishing:** Publish to Palantír, signal Celebrimbor/Elrond/Radagast.
5. **Proof Before Alloy:** Write service unit tests + controller integration tests.
6. **Implementation:** Build under DTO + module isolation.
7. **Mithril Armor:** Scan for Node security shadows.
8. **Signal Boromir:** `SIGNAL_NODE_REVIEW_REQUEST` with artifacts and contracts.
