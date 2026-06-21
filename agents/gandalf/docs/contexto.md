# Contexto: Expansão do Cluster e Governança

## Objetivo
Manter a sincronia entre a infraestrutura de hardware (Homelab/Cluster) e os protocolos da Fellowship.

## Ações Realizadas
1.  **Upgrade do Cluster Chii:** Integração do Predator (RTX 3070) via SSH/PowerShell concluída.
    - Implementação de `gpu_swap.py` para gestão de VRAM (Ollama vs ComfyUI).
    - Suporte a NoobAI XL e Qwen2.5 7B integrado em `app.py`.
    - Configuração de firewall e downloads via BITS finalizados no nó remoto.
2.  **Governança Local:** Criado `chii/GEMINI.md` para mandatos específicos do projeto.
3.  **Sincronização:** `QUEST_PROGRESS.md` atualizado com o status real do Homelab.

## Perigos Identificados
- **Shadow IT:** Risco de mudanças manuais no Windows (Predator). Mitigado pelo registro de procedimentos em `chii/GEMINI.md`.
- **VRAM Contention:** Risco de OOM mitigado por protocolo de swap forçado em `app.py`.

## Próximos Passos
- Iniciar configuração das bibliotecas no Kavita.
- Validar o fluxo de SSO no Authentik.
