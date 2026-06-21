# O Recrutador de Gondor (Legacy)

**Status:** Descomissionado (Removido por estar "meio falho").
**Data de Arquivamento:** 2026-05-24

## Propósito e Escopo
Automatizar a busca e o monitoramento de vagas de emprego (foco inicial no LinkedIn) para centralizar oportunidades em um único painel de controle.

## Regras de Negócio e Lógica
1. **Coleta:** Utiliza n8n para realizar o scraping ou integração com APIs de vagas.
2. **Armazenamento:** Os dados são salvos em um banco Postgres (`recrutador_gondor`).
3. **Distribuição:** Uma API Flask (`api-vagas`) fornece os dados em formato JSON.
4. **Visualização:** Um Dashboard (Recrutador UI) em Nginx exibe as vagas coletadas com filtros básicos.

## Infraestrutura Original
- Docker Compose com 4 serviços: n8n, postgres, recrutador-ui, api-vagas.
- Banco de dados acessível via `gandalf:mithril_shield`.

## Motivo da Remoção
O serviço apresentava falhas de estabilidade e a implementação estava obsoleta frente aos novos padrões da Fellowship. O escopo permanece válido para uma futura reconstrução (Quest "Narsil").
