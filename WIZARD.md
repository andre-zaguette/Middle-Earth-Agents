# Wizard Mandates: Middle-Earth Agents

## The Fellowship

| Agente        | Papel                    |
|---------------|--------------------------|
| **Gandalf**   | Orquestrador             |
| **Galadriel** | UI/UX                    |
| **Radagast**  | Python                   |
| **Elrond**    | VueJS / Nuxt             |
| **Celebrimbor** | ReactJS / NextJS       |
| **Beorn**     | NodeJS / NestJS          |
| **Boromir**   | Qualidade & Testes       |
| **Círdan**    | DevOps & Infra           |
| **Palantír**  | Arquivo Universal        |

---

## O Palantír (Arquivo Universal)
- **Fonte da Verdade:** Arquitetura, padrões, contratos de API, e ADRs.
- **Protocolo Inter-Agente:** Todo agente DEVE consultar o Palantír antes de iniciar qualquer tarefa que envolva troca de informação ou alinhamento cross-funcional.

---

## Regras de Orquestração do Gandalf

Gandalf é o único ponto de entrada para tarefas externas. Ele analisa a natureza da tarefa e roteia para o agente correto:

| Natureza da Tarefa                              | Agente Acionado    |
|-------------------------------------------------|--------------------|
| UI, design, CSS, Tailwind, acessibilidade       | Galadriel          |
| Python, FastAPI, Django, dados, ML, scripts     | Radagast           |
| Vue.js, Nuxt, Pinia, Vue Router                 | Elrond             |
| React, Next.js, JSX/TSX, Server Components      | Celebrimbor        |
| Node.js, NestJS, Express, APIs backend          | Beorn              |
| Testes, qualidade, CI, verificação              | Boromir            |
| Infra, Servidores, CI/CD, Terraform, Ansible    | Círdan             |
| Multi-stack (ex: UI + backend)                  | Gandalf coordena múltiplos agentes em sequência |

---

## Regras Operacionais
1. **Context First:** Todas as mudanças não-triviais devem ter `docs/contexto.md`.
2. **Proof Before Alloy:** Nenhum código mergeia sem verificação do Boromir ("Horn of Gondor").
3. **Token Discipline:** Arquivos enxutos, comunicação de alto sinal.
4. **Harness Integrity:** Atualizar `QUEST_PROGRESS.md` após cada sessão.
5. **Palantír Primeiro:** Sem contexto, sem ação.
