# Routing

Every React/Next quest follows this classification:

1. **Harness Check:** Does the project use App Router and TypeScript strict mode?
   - If ✗: Route to `Harness Alignment`.
2. **Component Boundary:** Server Component or Client Component?
   - Default: Server. Justify `"use client"` with one concrete reason.
3. **Data Strategy:** Static / Dynamic / Cached / Server Action?
   - Classify before writing any fetch logic.
4. **Visual Check:** Is there a design spec from Galadriel?
   - If ✗: Request `SIGNAL_DESIGN_SPEC` before building visual components.
5. **API Check:** Is the contract in the Palantír?
   - If ✗: Wait for Beorn/Radagast to publish it.

Roads:

- New RSC -> Server/client classify -> Data strategy -> Type contract -> Tests -> Implement.
- New Client Component -> Justify `"use client"` -> State ownership (local/Zustand/React Query) -> Implement.
- Server Action -> Input type -> Server-side validation -> Error handling -> Test.
- New Page/Route -> Route type (static/dynamic) -> Data strategy -> Layout -> Components.
- Data Fetching -> React Query or Server fetch -> Cache strategy -> Type contract.
- Bug Hunt -> Reproduce with Vitest -> Fix under test protection.
- Performance -> Server Component migration audit -> Bundle analysis.
