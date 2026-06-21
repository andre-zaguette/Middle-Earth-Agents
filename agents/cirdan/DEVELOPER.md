# Guia do Desenvolvedor: Círdan

## Stack Recomendada
- **Provisionamento:** Terraform / OpenTofu.
- **Configuração:** Ansible.
- **Orquestração:** Kubernetes / Docker Swarm.
- **CI/CD:** GitHub Actions / GitLab CI.
- **Scripts:** Bash / Python.

## Padrões de Código
- Siga os princípios DRY em módulos Terraform.
- Documente todas as variáveis e outputs.
- Utilize linters para todas as ferramentas (tflint, ansible-lint, shellcheck).

## Fluxo de Trabalho
1. Criar branch para a mudança de infraestrutura.
2. Validar localmente (ex: `terraform validate`, `ansible-playbook --syntax-check`).
3. Abrir PR e aguardar validação da pipeline e do Gandalf.
4. Aplicar em ambiente de staging antes da produção.
