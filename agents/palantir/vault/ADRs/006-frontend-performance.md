# ADR-006: As Asas de Gwaihir (Performance e Web Vitals)

## Status
Proposed

## Context
Interfaces lentas frustram a Sociedade e dificultam a Missão. Precisamos de velocidade e fluidez.

## Decision
1.  **Core Web Vitals:** Mirar em pontuações de 90+ no Lighthouse para LCP, FID e CLS.
2.  **Asset Optimization:** Imagens devem ser servidas em formatos modernos (WebP/AVIF) com carregamento preguiçoso (lazy loading).
3.  **Code Splitting:** Implementar carregamento sob demanda para reduzir o bundle inicial.
4.  **Caching Strategy:** Utilizar Service Workers e políticas de cache eficientes via Cloudflare (sob orientação de Círdan).

## Consequences
- **Positivas:** Experiência de usuário fluida; melhor ranqueamento e acessibilidade em redes lentas.
- **Negativas:** Aumenta a complexidade de build e otimização.

## Alternatives considered
- **SPA vs SSR:** A decisão entre Single Page Application ou Server-Side Rendering deve ser tomada caso a caso, priorizando performance.
