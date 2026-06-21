# ADR-008: O Portão Negro (Gates de CI/CD e Verificação)

## Status
Proposed

## Context
O código não deve entrar na branch principal (`main`) sem ser verificado. Precisamos de guardiões automáticos.

## Decision
1.  **CI Mandatória:** Todo PR deve disparar uma pipeline de verificação (Lint + Testes + Security Scan).
2.  **Horn of Gondor Protocol:** O merge só é permitido se Boromir (via automação) der o sinal de "Green".
3.  **Linting Estrito:** Proibido código com erros de lint ou warnings ignorados sem justificativa técnica no Palantír.
4.  **Security Gates:** Falha automática em segredos expostos (Mithril Armor) ou vulnerabilidades críticas de dependências.

## Consequences
- **Positivas:** Integridade constante da branch `main`.
- **Negativas:** Requer infraestrutura de CI robusta gerida por Círdan.

## Alternatives considered
- **Merge Direto:** Rejeitado por ser o caminho para o caos.
