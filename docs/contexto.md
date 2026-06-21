# Contexto: Desligamento para Manutenção de RAM
**Objetivo:** Preparar o servidor para desligamento seguro visando a instalação física de novos pentes de memória.
**Perigos:** 
- Perda de dados em serviços ativos (ComfyUI, Sunshine, etc.).
- Integridade de processos de background.
- Estado inconsistente do sistema de arquivos se não houver desligamento gracioso.

**Estratégia:**
1. Identificar processos críticos ativos.
2. Encerrar graciosamente os serviços de IA (ComfyUI, Ollama).
3. Encerrar serviços de streaming (Sunshine).
4. Sincronizar buffers de disco.
5. Executar o comando de desligamento.

**Status:** Concluído. Serviços encerrados e discos sincronizados. Pronto para intervenção física.

