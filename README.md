# avant-api

API REST do Groone Avant, em FastAPI. Todas as rotas ficam em `/api/v1`, e a
documentação OpenAPI em `/api/docs`. O domínio, os casos de uso e o banco vêm do
[avant-core](https://github.com/PedroH3nri/avant-core): esta API só traduz HTTP.

Outros repositórios: avant-core, avant-worker, avant-web, avant-infra.

## O que já tem

| Rota | Faz | Permissão |
| --- | --- | --- |
| `GET /health` | o processo está de pé | nenhuma |
| `GET /ready` | o banco responde | nenhuma |
| `GET /metrics` | Prometheus; bloqueado no nginx | rede interna |
| `POST /auth/login` | e-mail e senha; abre a sessão | nenhuma |
| `POST /auth/logout` | encerra a sessão | sessão |
| `GET /auth/me` | pessoa, Empresas, Empresa ativa e permissões | sessão |
| `POST /auth/me/active-company` | troca a Empresa ativa | sessão |
| `GET /auth/invitations/{token}` | dados do convite para a tela do link | nenhuma |
| `POST /auth/invitations/{token}/accept` | aceita: cria conta (e a Empresa, no convite de dono) ou usa a sessão | conforme o caso |
| `POST /auth/mfa/verify` | código do 2FA depois da senha; troca a pré-sessão pela sessão | pré-sessão |
| `POST /auth/mfa/setup` e `/confirm` | ativa o 2FA; o confirm devolve os 10 códigos de recuperação | sessão |
| `POST /auth/mfa/recovery-codes` | gera novos códigos de recuperação | sessão + código |
| `DELETE /auth/mfa` | desliga o 2FA (só clientes) | sessão + código |
| `GET /invitations` | convites pendentes da Empresa ativa | `team.view` |
| `POST /invitations` | convida por e-mail e papel | `team.invite` |
| `POST /invitations/{id}/resend` | token novo e mais 1 dia | `team.invite` |
| `DELETE /invitations/{id}` | cancela e libera a vaga | `team.invite` |
| `GET /company` | Empresa ativa, com vagas usadas | membro |
| `PATCH /company` | nome, cor e preferências | `company.edit` |
| `GET /members` | equipe; filtros `status`, `role`, `q` | `team.view` |
| `GET /members/{id}` | detalhe com permissões diretas | `team.view` |
| `PATCH /members/{id}` | troca papel, suspende ou reativa | `team.manage` |
| `DELETE /members/{id}` | remove e libera a vaga | `team.manage` |
| `POST /members/me/leave` | sai da Empresa (o dono não pode) | membro |
| `PUT /members/{id}/permissions` | lista inteira de permissões diretas | `permissions.grant` |
| `GET /permissions` | catálogo de cliente com nomes PT/EN/ES | `roles.view` |
| `GET /roles` | predefinidos e personalizados, com contagem | `roles.view` |
| `POST /roles`, `PATCH /roles/{id}`, `DELETE /roles/{id}` | papéis personalizados | `roles.manage` |
| `GET /audit` | histórico; filtros `actor`, `action`, `from`, `to`; cursor | `audit.view` |

Painel interno, em `/api/v1/internal` (Company Groone ativa e 2FA verificado na sessão):

| Rota | Faz | Permissão |
| --- | --- | --- |
| `GET /internal/clients`, `POST /internal/clients` | lista clientes; cadastra (convite de dono) | `internal.clients.view` / `.manage` |
| `GET /internal/clients/{id}`, `/audit` | página de suporte e histórico, só leitura | `internal.clients.view` |
| `PATCH /internal/clients/{id}` | vagas e plano | `internal.clients.manage` |
| `POST /internal/clients/{id}/suspend`, `/reactivate` | suspende ou reativa | `internal.clients.manage` |
| `POST /internal/clients/{id}/owner` | troca o dono | `internal.owner.change` |
| `GET /internal/owner-invitations`, `POST .../{id}/resend`, `DELETE .../{id}` | convites de dono | `internal.clients.view` / `.manage` |
| `GET /internal/users?q=`, `POST /internal/users/{id}/disable`, `/enable`, `/reset-mfa` | pessoas | `internal.users.manage` |
| `GET /internal/staff`, `POST /internal/staff/invitations` | equipe Groone | `internal.staff.manage` |

Ainda faltam o login com Google e o limite de requisições.

## Como funciona

- **Sessão**: cookie `avant_session` (`httpOnly`, `SameSite=Lax`, `Secure` fora do
  local). O banco guarda só o hash.
- **CSRF**: no login, a API grava também o cookie `avant_csrf`, que o Vue lê e manda no
  cabeçalho `X-CSRF-Token` em todo POST, PATCH, PUT e DELETE.
- **Empresa ativa**: vem da sessão, nunca da URL. Cada rota abre o Unit of Work do
  avant-core com essa Empresa, e o RLS do Postgres garante o isolamento.
- **2FA**: com o 2FA ligado, o login responde `{"mfa_required": true}` e o cookie leva
  só uma pré-sessão de 5 minutos. A equipe Groone sem 2FA recebe `mfa_required` (403) em
  tudo menos `/auth/me`, `/auth/logout` e `/auth/mfa/*`. O segredo é cifrado com
  `MFA_ENCRYPTION_KEY`.
- **E-mail**: com `RESEND_API_KEY`, os convites saem pelo Resend (remetente em
  `MAIL_FROM`), em português, inglês ou espanhol conforme o idioma da pessoa. Sem a chave,
  o `LogMailer` só registra o envio e, em local, mostra o link. A chave é obrigatória em
  staging e produção. Falha no envio vai para o log e para `avant_mail_failures_total`,
  e o convite continua pendente.
- **Permissão**: declarada na rota com `Depends(require("team.invite"))`.
- **Erros**: sempre `{"error": {"code", "message", "details"}}`; o mapa de código para
  status HTTP está em `errors.py`.
- **Logs**: JSON em uma linha por requisição, com `request_id` (também no cabeçalho
  `X-Request-Id`). Erro inesperado sai com o stack trace.

## Desenvolvimento

```bash
uv sync
uv run ruff format . && uv run ruff check . && uv run mypy
export AVANT_TEST_MIGRATIONS_URL=postgresql+psycopg://avant_owner:SENHA@localhost:5432/avant_test
export AVANT_TEST_DATABASE_URL=postgresql+psycopg://avant_app:SENHA@localhost:5432/avant_test
uv run pytest
```

Os testes recriam o schema do banco de testes com as migrations do avant-core.

A CI (`.github/workflows/ci.yml`) roda tudo isso em todo PR, com um Postgres 16. Para
baixar o avant-core, que é privado, ela usa o secret `AVANT_CORE_ACCESS`: um token
*fine-grained* só com leitura do avant-core.

Para rodar a API, com o compose do avant-infra no ar:

```bash
DATABASE_URL=postgresql+psycopg://avant_app:SENHA@localhost:5432/avant \
  uv run uvicorn avant_api.main:create_app --factory --reload
```

## Imagem

```bash
docker build --secret id=github_token,env=GITHUB_TOKEN -t ghcr.io/pedroh3nri/avant-api .
```

O token só precisa ler o avant-core e não fica na imagem.
