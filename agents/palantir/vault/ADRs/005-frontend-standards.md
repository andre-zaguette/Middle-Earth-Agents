# ADR-005: A Luz de Eärendil (Design System, Acessibilidade e Estilo)

## Status
Proposed

## Context
Galadriel (Design), Celebrimbor (React) e Elrond (Vue) criam as interfaces da Sociedade. Sem um padrão visual e de acessibilidade, o reino torna-se confuso e excludente.

## Decision
1.  **Vanilla CSS over Tailwind:** Priorizar CSS puro ou CSS Modules para máxima flexibilidade e controle, a menos que Tailwind seja explicitamente solicitado pelo Mago.
2.  **Acessibilidade (WCAG 2.1):** Todas as interfaces devem atingir o nível AA de acessibilidade. Uso obrigatório de ARIA labels e semântica HTML correta.
3.  **Design System:** Utilizar uma escala de cores, tipografia e espaçamento consistente baseada em variáveis CSS globais (tokens de design).
4.  **Responsividade:** Design mobile-first é mandatório.

## Consequences
- **Positivas:** Interfaces consistentes, belas e acessíveis a todos os povos da Terra Média.
- **Negativas:** Requer maior rigor no desenvolvimento de componentes base.

## Alternatives considered
- **Component Libraries (MUI, Shadcn):** Permitidos como base, mas devem ser estilizados para seguir a estética da Sociedade.
