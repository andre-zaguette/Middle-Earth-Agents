# Routing

Every UI quest follows this classification:

1. **Harness Check:** Does the project have design tokens defined?
   - If ✗: Route to `Token Definition`.
2. **Visual Quest?** Does this task touch layout, color, spacing, or interaction?
   - If ✓: Eye of Sauron first — transcribe the vision in text.
3. **Stack Check:** React (Celebrimbor) or Vue (Elrond)?
   - Route `SIGNAL_DESIGN_SPEC` to the correct frontend agent.
4. **Scope Check:** New component, modification, or full page/flow?

Roads:

- New Component -> Eye of Sauron -> Token Check -> Design Spec -> BDD States -> A11y Gate.
- Style Bug -> Transcribe current vs expected -> Token audit -> Surgical fix.
- UX Flow -> User journey map -> State diagram -> BDD -> Component breakdown.
- Accessibility Issue -> WCAG audit -> ARIA contract -> Test with screen reader.
- Design Token Request -> Palantír check -> Define token -> Publish to Palantír.
- Figma Spec -> Read with MCP Figma tool -> Transcribe -> Align tokens -> Signal frontend.
