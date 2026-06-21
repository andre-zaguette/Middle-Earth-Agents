# ADR-002: Os Portões de Moria (Gestão de Identidade e Acesso - IAM)

## Status
Accepted

## Context
O acesso aos servidores deve ser restrito e auditável. O uso de senhas fracas ou chaves SSH compartilhadas é como deixar os portões de Moria abertos para os orcs.

## Decision
1.  **Chaves SSH Individuais:** Proibido o uso de senhas. Acesso apenas via chaves SSH (ED25519) individuais.
2.  **Princípio do Menor Privilégio:** Ninguém (exceto Círdan em emergências) deve logar como `root`. Use `sudo` para tarefas administrativas.
3.  **Cloudflare Access/Zero Trust:** Sempre que possível, utilize túneis e autenticação de borda (Zero Trust) antes de permitir a conexão direta ao servidor.
4.  **Rotação:** Chaves de acesso e segredos de API devem ser rotacionados a cada 90 dias.
5.  **Bastion Host:** Para servidores em redes privadas, o acesso deve ser feito via um "Salão de Entrada" (Bastion Host) altamente vigiado.

## Consequences
- **Positivas:** Redução drástica da superfície de ataque; trilha de auditoria clara.
- **Negativas:** Maior complexidade inicial no setup de novos desenvolvedores.

## Alternatives considered
- **Acesso Direto via IP Público:** Rejeitado por facilitar ataques de força bruta.
- **Shared Admin Account:** Rejeitado por falta de responsabilidade (accountability).
