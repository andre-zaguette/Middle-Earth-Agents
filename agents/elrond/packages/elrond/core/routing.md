# Routing

Every Vue quest follows this classification:

1. **Harness Check:** Does the project use Composition API and Pinia?
   - If ✗: Route to `Harness Alignment` (migrate Options API if needed).
2. **State Check:** Who owns the state this component needs?
   - Local → `ref`/`reactive`. Shared → Pinia. Server → `useAsyncData`.
3. **Visual Check:** Does this component have a design spec from Galadriel?
   - If ✗: Request `SIGNAL_DESIGN_SPEC` before building.
4. **API Check:** Does this component fetch data? Is the contract in the Palantír?
   - If ✗: Wait for Beorn/Radagast to publish contract.

Roads:

- New Component -> State ownership -> Design spec -> API contract -> Composables -> Tests -> Implement.
- New Page (Nuxt) -> Route classification (SSR/SSG/CSR) -> Data strategy -> Layout -> Components.
- New Store (Pinia) -> Define state shape -> Actions -> Getters -> Tests -> Implement.
- Composable -> Define interface (params, return type) -> Tests -> Implement.
- Bug Hunt -> Reproduce with Vitest -> Fix under test protection.
- SSR/Hydration Issue -> Classify data strategy -> useAsyncData/useLazyAsyncData.
