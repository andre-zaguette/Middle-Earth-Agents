# Quest Progress: The Brotherhood of Agents

## Active Quests
- [x] **Ritual de Expansão: Upgrade de RAM:** Desligamento seguro e instalação física de novos módulos de memória. ✅ 2026-05-29
- [x] **Operação Resgate:** Migração de `/mnt/media` para `/mnt/reaper/SALVAMENTO` concluída com sucesso (100% dos dados salvos).
- [x] **Portões de Ferro (Coolify):** Instalação e configuração completa (SSH/GitHub).
- [x] **Game Streaming (Sunshine):** Fix de Captura X11/VAAPI, permissões GPU, e interface RetroArch (XMB). ✅ 2026-05-23
- [x] **Minas Tirith: N64 Config:** Core Mupen64Plus-Next instalado manualmente e integrado ao Sunshine. ✅ 2026-05-23
- [x] **Expansão de Minas Tirith:** HDD 1TB (hdd_new_1tb) + HDD rehabilitado ativos. Dock ORICO com USB1 (1TB) + USB2 (500GB) montados e no pool. ✅ 2026-05-23
- [x] **Ritual de Cura:** HDD original rehabilitado (hdd_rehabilitated, 916G) montado em /mnt/hdd_rehabilitated. ✅ 2026-05-23
- [x] **Reconfiguração do Pool:** MergerFS pool /mnt/storage = 4.1T (reaper + hdd_new + hdd_rehabilitated + USB1 + USB2). fstab atualizado com UUIDs corretos. ✅ 2026-05-23
- [x] **Upgrade do Cluster Chii:** Integração do Predator (RTX 3070), NoobAI XL e VRAM orchestration concluídos. Código Python cluster-aware e monitoramento de downloads ativos. ✅ 2026-05-25
- [ ] **A Biblioteca de Minas Tirith:** Kavita instalado (manga.orochidrake.com.br). Aguardando configuração de bibliotecas.
- [ ] **Os Portões de Moria:** Authentik instalado (auth.orochidrake.com.br). Aguardando setup inicial de SSO.
- [x] **O Vigia das Forjas (Scrutiny):** Monitoramento de saúde (SMART) e espaço em disco via Web (disk.orochidrake.com.br).
- [x] **Escudo de Mithril (Ubuntu Pro):** Ativação do ESM (Apps & Infra) para cobertura total de atualizações de segurança. ✅ 2026-05-23
- [x] ~~**O Recrutador de Gondor:** Automação de vagas LinkedIn com n8n, Postgres e Dashboard Web (porta 3050).~~ (Arquivado em Palantír - 2026-05-24) ✅ 2026-05-23
- [x] **Inspeção das Forjas:** Auditoria manual de espaço e integridade dos discos (lsblk/df). Concluído: hdd2 (sde1) remontado e pool MergerFS restaurado para 1.8T.
- [ ] **Projeto Escriba:** Agente literário isolado com RAG e gestão de projetos (Fase 1: Foundation).

## Planned Quests
- [ ] **A Crônica Unificada:** Serviço de lembretes centralizado (iPhone + n8n + CalDAV).
- [ ] **O Grande Arquivo de Memórias (Immich):** Backup e IA para fotos (Alternativa ao Google Photos/iCloud).

## The Road Traveled
- **GEMINI.md:** High Wizard's Mandate estabelecido no root.
- **Governança (Palantír):** ADRs 001 a 008 estabelecidas cobrindo todo o ciclo de vida do software.
- **Círdan (DevOps):** Integrado como submódulo com suporte multi-IA (Claude/Gemini).
- **Sincronia de Mandatos:** Todos os agentes (Beorn, Radagast, Boromir) atualizados para respeitar as ADRs.
- **Mithril Armor:** Scripts de segurança purificados e validados.
- **Submodules:** Todos os agentes vinculados aos seus respectivos repositórios GitHub.
- **Palantír Map:** Sincronizado com a estrutura real de todos os submodules.
- **blackchii (Mídia):** Unificação de storage (SSD/HDD), automação de seeding (ImortalSeed ratio 5.0, TorrentLeech protegido), aceleração HW (AMD VAAPI) no Jellyfin e SSO removido (revertido para login local).

## Next Steps
- [ ] Implementar suite de testes inicial para a codebase existente.
- [ ] Iniciar a segunda obra utilizando a Fellowship.

