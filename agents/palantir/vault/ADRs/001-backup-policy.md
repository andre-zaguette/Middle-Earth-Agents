# ADR-001: As Criptas de Erebor (Política de Backup e Disaster Recovery)

## Status
Accepted

## Context
A Sociedade opera serviços críticos que residem em servidores geridos por Círdan. A perda de dados (seja por falha de hardware, erro humano ou ataque) representaria o fim da Missão. Precisamos de uma política resiliente que garanta a sobrevivência do reino.

## Decision
1.  **Backup 3-2-1:** Manter 3 cópias dos dados, em 2 tipos diferentes de mídia, com 1 cópia off-site (em região geográfica distinta).
2.  **Frequência:** 
    *   Dados de aplicação (DB): Diário (Snapshot) + Logs de transação a cada hora.
    *   Configuração de Infra (IaC): Versão em Git é a fonte da verdade.
3.  **Retenção:** Backups diários por 30 dias; Mensais por 1 ano.
4.  **Teste de Restauração:** Círdan deve realizar um rito de restauração (Restore Test) a cada trimestre para garantir que o ouro de Erebor ainda pode ser recuperado.

## Consequences
- **Positivas:** Alta resiliência; paz de espírito para o Mago.
- **Negativas:** Custo adicional de armazenamento em nuvem.

## Alternatives considered
- **Backup Manual:** Rejeitado por ser propenso a erro humano.
- **Single Region Backup:** Rejeitado pelo risco de desastres naturais na região do data center.
