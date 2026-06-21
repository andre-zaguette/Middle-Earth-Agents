# ADR-003: Os Pergaminhos de Isildur (Padrões de API e Contratos)

## Status
Proposed

## Context
Beorn (Node.js) e Radagast (Python) constroem os serviços de backend da Sociedade. Sem um padrão de contrato, a comunicação entre frontend e backend (ou entre serviços) torna-se caótica, como as línguas de Babel.

## Decision
1.  **OpenAPI (Swagger) First:** Todo novo serviço de backend deve definir seu contrato via OpenAPI 3.0 antes da implementação completa.
2.  **RESTful Maturity:** Seguir o Modelo de Maturidade de Richardson (Nível 2 no mínimo - Recursos e Verbos HTTP corretos).
3.  **JSON Standard:** Todas as respostas devem ser em JSON, utilizando `snake_case` para chaves (padrão Radagast) ou `camelCase` (padrão Beorn), mas deve ser consistente dentro do mesmo serviço.
4.  **Versionamento:** APIs devem ser versionadas via URL (ex: `/api/v1/...`).
5.  **Erro Standard:** Respostas de erro devem seguir um formato padrão: `{ "error": { "code": "STRING_CODE", "message": "Human readable message" } }`.

## Consequences
- **Positivas:** Facilita a integração com Celebrimbor (React) e Elrond (Vue); permite geração automática de clientes de API.
- **Negativas:** Requer tempo inicial de design antes da codificação.

## Alternatives considered
- **GraphQL:** Considerado para o futuro, mas mantido REST para simplicidade inicial e compatibilidade universal.
