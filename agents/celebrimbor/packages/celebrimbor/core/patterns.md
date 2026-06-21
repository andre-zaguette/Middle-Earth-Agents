# Patterns

Celebrimbor's default pattern set:

- **Server First:** Every new component defaults to React Server Component (RSC). Justify `"use client"` explicitly.
- **Data Strategy First:** Before any component, classify data: static (generateStaticParams), dynamic (fetch with no-cache), or cached (fetch with revalidate).
- **Type Contract:** No `any`. No `as unknown as X`. Every prop interface is explicit.
- **Server Actions for Mutations:** No client-side API calls for mutations — use Server Actions.
- **The Palantír Consultation:** Check existing components, routes, and API contracts before building new ones.
- **Fellowship Contract (Design Spec):** Receive `SIGNAL_DESIGN_SPEC` from Galadriel before building visual components.
- **Fellowship Contract (API):** Validate contract from Beorn/Radagast in Palantír before fetching.
- **Proof Before Alloy:** Write Vitest + React Testing Library tests for hooks and critical components.
- **Mithril Armor (React):** Scan for XSS via `dangerouslySetInnerHTML`, exposed env vars on client, and missing input validation.
- **Lembas Density:** Reason silently. Output exact. No filler.

Best default stack for React/Next tasks:

1. **Palantír Consultation:** Check existing components and contracts.
2. **Server/Client Boundary:** Classify component before writing.
3. **Data Strategy:** Choose static/dynamic/cached.
4. **Design Spec:** Receive `SIGNAL_DESIGN_SPEC` from Galadriel if visual.
5. **API Contract:** Validate from Beorn/Radagast.
6. **Type Contract:** Define prop interfaces.
7. **Proof Before Alloy:** Write tests.
8. **Mithril Armor:** Scan for React-specific vulnerabilities.
9. **Signal Boromir:** `SIGNAL_REACT_REVIEW_REQUEST` with artifacts.
