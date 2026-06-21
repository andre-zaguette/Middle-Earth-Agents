# ADR-007: A Espada Quebrada (Estratégia de Testes e Cobertura)

## Status
Proposed

## Context
A qualidade é a armadura da Sociedade. Sem testes, o código é frágil contra as sombras (bugs). Precisamos de uma estratégia clara para Boromir validar as obras dos outros agentes.

## Decision
1.  **Pirâmide de Testes:** Priorizar testes unitários (base), seguidos por integração e E2E (topo).
2.  **Cobertura Mínima:** Exigir 80% de cobertura de código para lógica de negócio crítica.
3.  **TDD (Test-Driven Development):** Encorajado para correções de bugs (reproduzir antes de fixar).
4.  **Mocks & Stubs:** Utilizar mocks para dependências externas (APIs de terceiros) para garantir testes determinísticos e rápidos.

## Consequences
- **Positivas:** Redução de regressões; confiança total nos deploys de Círdan.
- **Negativas:** Maior tempo de desenvolvimento inicial.

## Alternatives considered
- **Apenas Testes Manuais:** Rejeitado por ser lento e propenso a falhas.
