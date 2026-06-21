# ADR-004: Os Olhos de Águia (Logging e Observabilidade)

## Status
Proposed

## Context
Para que Círdan (DevOps) possa administrar os servidores, ele precisa de visibilidade sobre o que Beorn e Radagast estão executando. Serviços silenciosos são perigosos.

## Decision
1.  **Structured Logging:** Todos os logs devem ser emitidos em formato estruturado (JSON) em ambiente de produção.
2.  **Níveis de Log:** Utilizar rigorosamente os níveis `DEBUG`, `INFO`, `WARN`, `ERROR` e `FATAL`.
3.  **Correlation ID:** Toda requisição deve carregar um `X-Correlation-ID` nos headers para rastrear o fluxo entre múltiplos serviços.
4.  **Health Checks:** Todo serviço deve expor um endpoint `/health` que retorne o estado de saúde do processo e suas dependências (DB, Cache).
5.  **Métricas:** Expor métricas básicas (Prometheus format) para monitoramento de latência e taxa de erro.

## Consequences
- **Positivas:** Diagnóstico rápido de falhas; integração nativa com o monitoramento de Círdan.
- **Negativas:** Leve overhead de performance e aumento no volume de armazenamento de logs.

## Alternatives considered
- **Plain Text Logs:** Rejeitado por ser difícil de analisar em escala.
