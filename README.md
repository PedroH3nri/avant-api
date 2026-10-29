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
| `GET /auth/me/companies/{id}/image` | imagem de uma Empresa da pessoa, para o seletor | membro ativo |
| `GET /auth/invitations/{token}` | dados do convite para a tela do link | nenhuma |
| `POST /auth/invitations/{token}/accept` | aceita: cria conta (e a Empresa, no convite de dono) ou usa a sessão | conforme o caso |
| `POST /auth/mfa/verify` | código do 2FA depois da senha; troca a pré-sessão pela sessão | pré-sessão |
| `POST /auth/mfa/setup` e `/confirm` | ativa o 2FA; o confirm devolve os 10 códigos de recuperação | sessão |
| `POST /auth/mfa/recovery-codes` | gera novos códigos de recuperação | sessão + código |
| `DELETE /auth/mfa` | desliga o 2FA (só clientes) | sessão + código |
| `POST /auth/password/forgot` | manda o link de nova senha; responde 202 exista ou não a conta | nenhuma |
| `POST /auth/password/reset` | nova senha pelo link (com 2FA, pede o código); encerra todas as sessões | nenhuma |
| `POST /auth/password/change` | troca a senha; encerra as outras sessões | sessão |
| `GET /auth/sessions` | sessões ativas, com a atual marcada | sessão |
| `DELETE /auth/sessions/{id}` | encerra uma sessão | sessão |
| `POST /auth/sessions/revoke-others` | encerra todas menos a atual | sessão |
| `GET /auth/google/start?mode=login\|link` | manda para o Google; `link` liga a conta em Configurações | nenhuma ou sessão |
| `GET /auth/google/callback` | volta do Google e redireciona para o painel | nenhuma |
| `GET /auth/google` e `DELETE /auth/google` | se o Google está ligado; desligar | sessão |
| `GET /invitations` | convites pendentes da Empresa ativa | `team.view` |
| `POST /invitations` | convida por e-mail e papel | `team.invite` |
| `POST /invitations/{id}/resend` | token novo e mais 1 dia | `team.invite` |
| `DELETE /invitations/{id}` | cancela e libera a vaga | `team.invite` |
| `GET /company` | Empresa ativa, com vagas usadas | membro |
| `PATCH /company` | nome, cor e preferências | `company.edit` |
| `GET /company/image` | imagem da Empresa ativa em WebP 256x256, com `ETag` e cache pela URL `?v=` | membro |
| `PUT /company/image`, `DELETE /company/image` | troca (corpo = arquivo PNG, JPEG ou WebP até 2 MB) ou tira a imagem | `company.edit` |
| `GET /company/fiscal`, `PUT /company/fiscal` | dados fiscais de pagamento; só o cliente grava, todos juntos | `company.edit` |
| `GET /members` | equipe; filtros `status`, `role`, `q` | `team.view` |
| `GET /members/{id}` | detalhe com permissões diretas | `team.view` |
| `PATCH /members/{id}` | troca papel, suspende ou reativa | `team.manage` |
| `DELETE /members/{id}` | remove e libera a vaga | `team.manage` |
| `POST /members/me/leave` | sai da Empresa (o dono não pode) | membro |
| `PUT /members/{id}/permissions` | lista inteira de permissões diretas | `permissions.grant` |
| `GET /permissions` | catálogo de cliente com nomes PT/EN/ES | `roles.view` |
| `GET /roles` | predefinidos e personalizados, com contagem | `roles.view` |
| `POST /roles`, `PATCH /roles/{id}`, `DELETE /roles/{id}` | papéis personalizados | `roles.manage` |
| `GET /groups`, `GET /groups/{id}` | grupos de funcionários com as pessoas | `groups.view` |
| `POST /groups`, `PATCH /groups/{id}`, `DELETE /groups/{id}` | criar (com pelo menos uma pessoa), renomear, excluir | `groups.manage` |
| `POST /groups/{id}/members`, `DELETE /groups/{id}/members/{membership_id}` | pôr e tirar pessoas; a última não sai (409) | `groups.manage` |
| `GET /audit` | histórico; filtros `actor`, `action`, `from`, `to`; cursor | `audit.view` |
| `GET /networks` | networks do GAM com as últimas etapas e os sites ativos | `network.view` |
| `GET /networks/service-account` | e-mail da conta de serviço para o guia de conexão | `network.connect` |
| `POST /networks` | conecta pelo network code; 202, nasce `pending` e o worker testa | `network.connect` |
| `GET /networks/{id}`, `/sync-runs` | detalhe e histórico das etapas | `network.view` |
| `POST /networks/{id}/sync` | "sincronizar agora"; 1 vez a cada 10 minutos (429 com `Retry-After`) | `network.sync` |
| `POST /networks/{id}/disconnect` | para as sincronizações; o histórico fica | `network.disconnect` |
| `GET /api-keys` | chaves da Empresa (com `api_keys.manage`) ou só as próprias | membro |
| `POST /api-keys` | cria uma chave; o valor `avk_...` volta só nesta resposta; só pela sessão | `api_keys.manage` |
| `DELETE /api-keys/{id}` | revoga; a dona da chave ou quem gerencia | membro |
| `GET /sites` | sites da Empresa (filtros `network_id`, `approval_status`, `q`, `include_archived`); quem não vê todos recebe só os atribuídos | `sites.view` |
| `POST /sites` | cadastra site pelo domínio, aguardando o GAM (`awaiting_gam`); a importação junta ao site do GAM com o mesmo domínio | `sites.manage` |
| `GET /sites/{id}` | detalhe com os ad units; `assigned_to` só para quem atribui | `sites.view` |
| `DELETE /sites/{id}` | remove o site que ainda aguarda o GAM (o do GAM responde `site_from_gam`) | `sites.manage` |
| `GET /sites/{id}/members` | quem vê o site: atribuído ou por ver todos | `sites.assign` |
| `GET /ad-units` | lista plana (`parent_id` monta a árvore); filtros `network_id`, `site_id`, `status`, `unlinked` | `sites.view` |
| `PATCH /ad-units/{id}` | liga a um site à mão (os filhos seguem) ou volta ao automático | `sites.assign` |
| `GET /members/{id}/sites` | sites atribuídos ao membro | `team.view` |
| `PUT /members/{id}/sites` | troca a lista inteira de sites do membro | `sites.assign` |
| `GET /metrics/catalog` | métricas e dimensões que dá para pedir, com os textos em PT, EN e ES (sem as métricas internas da Groone), e as métricas personalizadas da Empresa (`custom_metrics`, com a `query_key` e as fontes) | `reports.view` |
| `GET /custom-metrics` | métricas personalizadas da Empresa, pelo nome, com a chave da consulta (`custom.<chave>`) e as fontes em que cada uma pode ser pedida | `reports.view` |
| `POST /custom-metrics`, `PUT /custom-metrics/{id}`, `DELETE /custom-metrics/{id}` | cadastra, edita ou apaga uma métrica personalizada (fórmula sobre as métricas do catálogo; erro `invalid_formula`; `409 custom_metric_in_use` se outra usa); a chave nasce do nome e não muda | `metrics.manage` |
| `POST /custom-metrics/validate` | confere o formulário como salvar faria, sem gravar: `valid`, `code`, `error` (com a posição) e as variáveis; com `sample` (valores de exemplo das métricas do catálogo; as personalizadas aninhadas são calculadas), devolve em `value` a fórmula calculada no core (vazio sem denominador) | `metrics.manage` |
| `POST /reports/query` | roda uma consulta sem salvar: métricas, período (fixo ou relativo), dimensões, filtros, comparação, ordem e limite; `currency` converte o dinheiro pela cotação de cada dia (padrão `USD`; sem cotação, `currency_unavailable`); decimais como texto; só os sites que a pessoa vê; 10 seguidas e depois 1 a cada 2 s (`rate_limited`); passou de 15 s no banco, `query_too_heavy` | `reports.view` |
| `POST /reports/query/export?locale=` | a mesma consulta em CSV, sites e networks pelo nome, texto que parece fórmula escapado com `'` | `reports.view` |
| `GET /reports`, `GET /reports/{id}` | relatórios salvos que a pessoa vê (os dela, os da Empresa e os dos papéis dela; o privado de outra pessoa é 404), com a consulta, o gráfico, a visibilidade e `editable` | `reports.view` |
| `POST /reports`, `PUT /reports/{id}`, `DELETE /reports/{id}` | salva, edita ou apaga um relatório: nome, descrição, consulta (a de `/reports/query`, sem a moeda), `chart_type` e opções (`stacked`; `metrics` com a cor de cada métrica, `lime`/`cyan`/`magenta`/`violet`/`orange`/`yellow`/`red`, e a aparência `green_red`/`red_green` com `from` < `to`), `visibility` (`private`, `company`, `roles` com `role_ids`); editar e apagar são do dono ou de quem tem `reports.manage` | `reports.manage` para criar |
| `POST /reports/{id}/duplicate` | cópia privada de quem duplica, com " (cópia)" no nome | `reports.manage` |
| `GET /reports/templates`, `POST /reports/templates/{key}` | modelos prontos da Groone (nome em PT, EN e ES) e um relatório privado novo a partir de um deles | `reports.view` / `reports.manage` |
| `POST /reports/{id}/run` | roda o relatório salvo na moeda de visualização de quem roda, só nos sites que a pessoa vê; mesmo limite de taxa de `/reports/query` | `reports.view` |
| `GET /reports/{id}/export?format=csv\|xlsx&locale=` | o relatório salvo em CSV ou XLSX (números como números, texto sempre como texto), personalizadas pelo nome | `reports.view` |
| `GET /currencies` | as moedas do painel, com `available` quando já há cotação | sessão |
| `GET /costs` | custos da aba Custos, do mês mais novo para o mais antigo | `costs.view` |
| `POST /costs`, `PUT /costs/{id}`, `DELETE /costs/{id}` | cadastra, troca ou apaga um custo: `one_time` (um mês), `recurring` (do início até o fim, se tiver) ou `formula` (sobre `faturamento` e `receita` do mês; erro `invalid_formula`) | `costs.manage` |
| `POST /costs/formula` | confere a fórmula e calcula com valores de exemplo, sem gravar | `costs.view` |
| `GET /results?start=&end=&currency=` | faturamento, deduções (parte do cliente), receita, custos e resultado de cada mês, até 24 meses (padrão: os 6 até o atual); `deductions_pending` enquanto o GAM não fecha o mês | `results.view` |
| `PUT /auth/preferences` | troca a moeda de visualização da pessoa (`display_currency`, que também vem em `/auth/me`) | sessão |
| `PATCH /auth/appearance` | tema (`light`, `dark`, `system`), cor (`default`, `blue`, `green`, `purple`, `orange`) e idioma (`pt`, `en`, `es`) da pessoa, também em `/auth/me` | sessão |
| `PUT /auth/me/image`, `DELETE /auth/me/image` | troca ou tira a foto de perfil (corpo é o arquivo PNG, JPEG ou WebP de até 2 MB) | sessão |
| `GET /users/{id}/image` | foto de perfil da própria pessoa ou de alguém da Empresa ativa (`user.image_url` nas respostas) | sessão |
| `GET /events` | avisos em tempo real (SSE) da Empresa ativa, filtrados pela permissão | membro |

Painel interno, em `/api/v1/internal` (Company Groone ativa e 2FA verificado na sessão):

| Rota | Faz | Permissão |
| --- | --- | --- |
| `GET /internal/clients`, `POST /internal/clients` | lista clientes; cadastra o cliente pendente, com contato e indicação, sem mandar e-mail | `internal.clients.view` / `.manage` |
| `POST /internal/clients/{id}/owner-invitation` | envia (ou manda de novo) o convite de dono para o e-mail do cadastro | `internal.clients.manage` |
| `GET /internal/clients/{id}`, `/audit` | página de suporte e histórico, só leitura | `internal.clients.view` |
| `PATCH /internal/clients/{id}` | nome, vagas e cadastro (contato e indicação; os fiscais só o cliente muda) | `internal.clients.manage` |
| `GET`, `PUT`, `DELETE /internal/clients/{id}/image` | imagem do cliente (ver, trocar, tirar) | `internal.clients.view` / `.manage` |
| `PUT /internal/clients/{id}/status` | situação `active`, `inactive` ou `banned`; as networks acompanham | `internal.clients.manage` |
| `POST /internal/clients/{id}/owner` | troca o dono | `internal.owner.change` |
| `GET /internal/owner-invitations`, `POST .../{id}/resend`, `DELETE .../{id}` | convites de dono | `internal.clients.view` / `.manage` |
| `GET /internal/teams?q=&company_id=` | pessoas das equipes das Empresas cliente (sem a equipe Groone) | `internal.clients.view` |
| `GET /internal/users?q=`, `POST /internal/users/{id}/disable`, `/enable`, `/reset-mfa` | pessoas | `internal.users.manage` |
| `GET /internal/staff`, `POST /internal/staff/invitations` | equipe Groone | `internal.staff.manage` |
| `GET /internal/networks/unassigned`, `POST .../{id}/assign` | MCM sem dono: a Groone escolhe a Empresa | `internal.networks.assign` |
| `GET /internal/results?start=&end=&currency=` | o resultado de cada Empresa cliente no período, por nome | `internal.results.view` |
| `GET /internal/contracts`, `GET .../{id}` | contratos, com filtros `company_id`, `network_id` e `status` | `internal.contracts.view` |
| `GET /internal/contracts/networks` | networks MCM com o contrato ativo e se aceitam contrato à mão | `internal.contracts.view` |
| `POST /internal/contracts` | contrato à mão (só MCM Manage Inventory; encerra o ativo) | `internal.contracts.create` |
| `PATCH /internal/contracts/{id}`, `POST .../{id}/end` | observação e encerramento (o revshare nunca muda) | `internal.contracts.update` |
| `DELETE /internal/contracts/{id}` | exclui contrato feito à mão | `internal.contracts.delete` |

## Estrutura

Organizado por domínio (objeto → arquivos), com a regra de negócio no avant-core:

```
src/avant_api/
  main.py              monta a aplicação e inclui o router de cada domínio
  app/                 infraestrutura: settings, container (Services), security
                       (autenticação e permissões), cookies, errors, middleware,
                       logs, limits, events, tasks, google e ports
  shared/              DTOs usados por mais de um domínio (dto.py) e leitura do pedido (http.py)
  modules/<recurso>/    um módulo por recurso (members, roles, networks, google...), com
    controller.py      um só: as rotas do recurso, só HTTP (validação, status, cookies,
                       redirecionamento)
    dto.py             um só: modelos Pydantic de entrada e saída (sem DTO, não tem o arquivo)
    service.py         um só: chama os casos de uso do avant-core e devolve os DTOs
    dependencies.py    um só: monta o service com os adaptadores do container
    <assunto>.py       apoio só deste módulo, com o nome do assunto (google/redirects.py,
                       reports/export.py, results/period.py); nunca um segundo controller
                       ou service: recurso novo é módulo novo
  modules/internal/    painel interno, um subdomínio por assunto (clients, people,
                       staff, mcm, results, contracts), cada um com os mesmos arquivos, e
                       router.py que junta todos
```

- **Model e repository** ficam no avant-core, organizado por domínio: entidades em
  `<domínio>/models/`, interfaces em `<domínio>/interfaces/`, implementação SQL em
  `<domínio>/repositories/` e casos de uso em `<domínio>/services/`. A API e o worker usam
  os mesmos.
- **Inversão de dependência**: o service recebe interfaces (`app/ports.UnitOfWorkFactory`,
  `Clock`, `Mailer`, `TaskQueue`...) pelo construtor, nunca o container. Só o
  `dependencies.py` conhece o `Services`; nos testes, dá para montar o service com fakes.
- O controller não chama caso de uso nem abre Unit of Work: fala só com o service.

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
- **Limite de tentativas**: 5 senhas erradas por e-mail e 20 por IP em 15 minutos no
  login; 20 pedidos por IP em 15 minutos em `/auth/password/*`. Passou, 429
  `too_many_attempts` com `Retry-After`. Os contadores ficam no Redis (`REDIS_URL`,
  obrigatória em staging e produção) e, sem ele, na memória do processo.
- **Google**: OpenID Connect com PKCE, tratado aqui (`GOOGLE_OAUTH_CLIENT_ID` e
  `GOOGLE_OAUTH_CLIENT_SECRET`; URI de redirecionamento
  `{APP_BASE_URL}/api/v1/auth/google/callback`). Só entra com Google quem ligou a conta
  em Configurações. O callback sempre redireciona para o painel: `/` ou `/entrar/2fa`
  quando deu certo, `/entrar?erro=<code>` ou `/configuracoes/conta?erro=<code>` quando
  não.
- **Avisos por e-mail**: senha trocada, Google ligado e 2FA zerado pela Groone. Os
  e-mails vêm de `avant_core.mail`, o mesmo módulo do worker.
- **GAM**: a API não fala com o Ad Manager. Conectar, "sincronizar agora" e atribuir uma
  network MCM gravam o pedido e enfileiram `avant.gam.sync_network` no RabbitMQ
  (`CELERY_BROKER_URL`, obrigatória em staging e produção) depois do commit. Se o
  RabbitMQ não responder, a rota não falha: o erro vai para o log e o agendador do worker
  passa pela network no ciclo seguinte. O guia mostra `GAM_SERVICE_ACCOUNT_EMAIL`.
- **Tempo real**: `GET /events` é um `text/event-stream`. O worker publica
  `{"type", "data"}` no canal Redis `avant:events:{company_id}` e qualquer instância da
  API repassa; cada tipo de evento exige uma permissão (`app/events.PERMISSION_FOR`) e o que
  não está no mapa não sai. Heartbeat a cada 15 s; depois de 30 minutos a API fecha e o
  EventSource reconecta, conferindo a sessão de novo. O proxy precisa de
  `proxy_buffering off` nessa rota (a resposta também manda `X-Accel-Buffering: no`).
  Eventos de agora: `network.updated` (`network.view`), com `network_id`.
- **Chaves de API**: `Authorization: Bearer avk_...` vale nas rotas de Empresa, sem CSRF,
  com as permissões da chave que o membro ainda tem. Login, 2FA, conta, sessões, criar
  chave, sair da Empresa e o painel interno são só pela sessão. Cada chave tem um balde de
  2 requisições por segundo com rajada de 20 (`X-RateLimit-Limit` e
  `X-RateLimit-Remaining`); passou, 429 `rate_limited` com `Retry-After`, e mais de 20
  recusas em um minuto bloqueiam a chave por 30 s. O balde fica no Redis.
- **Permissão**: declarada na rota com `Depends(require("team.invite"))`.
- **Erros**: sempre `{"error": {"code", "message", "details"}}`; o mapa de código para
  status HTTP está em `app/errors.py`.
- **Logs**: JSON em uma linha por requisição, com `request_id` (também no cabeçalho
  `X-Request-Id`). Erro inesperado sai com o stack trace.

## Desenvolvimento

Para subir o Avant inteiro na máquina (banco, API, worker e painel), siga o [guia de desenvolvimento](https://github.com/PedroH3nri/avant-infra/blob/develop/docs/desenvolvimento.md) do avant-infra.

```bash
uv sync
uv run ruff format . && uv run ruff check . && uv run mypy
export AVANT_TEST_MIGRATIONS_URL=postgresql+psycopg://avant_owner:SENHA@localhost:5432/avant_test
export AVANT_TEST_DATABASE_URL=postgresql+psycopg://avant_app:SENHA@localhost:5432/avant_test
export AVANT_TEST_REDIS_URL=redis://localhost:6379/0  # opcional: testa o contador no Redis
uv run pytest
```

Os testes recriam o schema do banco de testes com as migrations do avant-core.

A CI (`.github/workflows/ci.yml`) roda tudo isso em todo PR, com um Postgres 16 e um
Redis 7. Para
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
