# Signal Protocol — Middle-Earth Agents

Protocolo de comunicação entre todos os agentes da Terra Média.

---

## Regra Universal
**Todo agente DEVE consultar o Palantír antes de iniciar qualquer tarefa.** Sem contexto, não há ação.

---

## Sinais de Gandalf (Orquestrador)

### Gandalf → Galadriel
- **Sinal:** `SIGNAL_UI_TASK`
- **Payload:** `context`, `stack` (react|vue), `figma_url?`, `requirements`
- **Trigger:** Tarefa envolve design, UI, UX, acessibilidade, ou estilização

### Gandalf → Radagast
- **Sinal:** `SIGNAL_PYTHON_TASK`
- **Payload:** `context`, `requirements`, `api_contracts?`
- **Trigger:** Tarefa envolve Python, dados, ML, scripts, ou backend Python

### Gandalf → Elrond
- **Sinal:** `SIGNAL_VUE_TASK`
- **Payload:** `context`, `nuxt?`, `api_contracts?`
- **Trigger:** Tarefa envolve Vue.js ou Nuxt

### Gandalf → Celebrimbor
- **Sinal:** `SIGNAL_REACT_TASK`
- **Payload:** `context`, `nextjs?`, `api_contracts?`
- **Trigger:** Tarefa envolve React, Next.js, ou JSX/TSX

### Gandalf → Beorn
- **Sinal:** `SIGNAL_NODE_TASK`
- **Payload:** `context`, `nestjs?`, `db_schema?`
- **Trigger:** Tarefa envolve Node.js, NestJS, APIs backend, ou infraestrutura

### Gandalf → Boromir
- **Sinal:** `SIGNAL_BREACH_DEFENSE`
- **Payload:** `context`, `impact`, `severity` (Alta|Média|Baixa)
- **Trigger:** Risco de integridade detectado

---

## Sinais de Retorno ao Gandalf

| Agente       | Sinal de ACK                | Payload                          |
|--------------|-----------------------------|----------------------------------|
| Galadriel    | `ACK_UI_COMPLETE`           | `artifacts[]`                    |
| Radagast     | `ACK_PYTHON_COMPLETE`       | `artifacts[]`, `contracts[]`     |
| Elrond       | `ACK_VUE_COMPLETE`          | `artifacts[]`                    |
| Celebrimbor  | `ACK_REACT_COMPLETE`        | `artifacts[]`                    |
| Beorn        | `ACK_NODE_COMPLETE`         | `artifacts[]`, `api_contracts[]` |
| Boromir      | `ACK_DEFENSE_ACTIVE`        | `test_results`, `status`         |

---

## Sinais Inter-Agente

### Galadriel → Celebrimbor / Elrond
- **Sinal:** `SIGNAL_DESIGN_SPEC`
- **Payload:** `tokens`, `component_spec`, `a11y_notes`
- **Quando:** Galadriel finaliza spec de componente visual

### Galadriel → Boromir
- **Sinal:** `SIGNAL_UI_REVIEW_REQUEST`
- **Payload:** `component`, `a11y_checklist`

### Celebrimbor → Beorn
- **Sinal:** `SIGNAL_API_NEEDED`
- **Payload:** `endpoint_spec`, `method`, `payload_schema`
- **Quando:** Celebrimbor precisa de endpoint que ainda não existe

### Radagast → Beorn
- **Sinal:** `SIGNAL_API_CONTRACT`
- **Payload:** `endpoints[]`, `schemas[]`
- **Quando:** Radagast define endpoints Python que Beorn precisa conhecer

### Beorn → Palantír
- **Ação:** Publicar contratos de API após cada endpoint novo
- **Formato:** `api_contracts/{service}/{version}.md`

### Qualquer Agente → Boromir
- **Sinal:** `SIGNAL_{AGENT}_REVIEW_REQUEST`
- **Payload:** `artifacts[]`, `context`
- **Quando:** Agente finaliza entrega e precisa de verificação

### Boromir → Gandalf
- **Sinal:** `ACK_DEFENSE_ACTIVE`
- **Payload:** `test_results`, `coverage`, `status` (PASS|FAIL)
