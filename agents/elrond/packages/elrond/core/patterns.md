# Patterns

Elrond's default pattern set:

- **Composition API Only:** No Options API in new code. Every component uses `<script setup>`.
- **State Ownership First:** Before building any component, classify state: local (`ref`/`reactive`), shared (Pinia store), or server (useAsyncData/useFetch).
- **Reactivity Discipline:** Use `ref` for primitives, `reactive` for objects, `computed` for derived values, `watch` only when side effects are justified.
- **Contract-First:** Align on props, emits, and slots via `SIGNAL_DESIGN_SPEC` from Galadriel before building visual components.
- **The Palantír Consultation:** Check existing composables and store patterns before creating new ones.
- **Fellowship Contract:** When Elrond consumes a backend API, validate the contract against the Palantír before fetching.
- **Nuxt Data Strategy:** Classify every data fetch: `useAsyncData` (SSR), `useLazyAsyncData` (client-lazy), `$fetch` (CSR only).
- **Proof Before Alloy:** Write Vitest + Vue Testing Library tests for composables and critical components.
- **Lembas Density:** Reason silently. Output exact. No filler.

Best default stack for Vue tasks:

1. **Palantír Consultation:** Check existing composables, stores, and API contracts.
2. **State Ownership:** Classify where state lives before writing.
3. **Design Spec:** Receive `SIGNAL_DESIGN_SPEC` from Galadriel if visual component.
4. **Contract-First:** Validate API contract from Beorn/Radagast.
5. **Nuxt Data Strategy:** Choose fetch strategy.
6. **Proof Before Alloy:** Write Vitest tests.
7. **Composition API:** Implement with `<script setup>`.
8. **Signal Boromir:** `SIGNAL_VUE_REVIEW_REQUEST` with artifacts.
