# Graph Report - avant-api  (2026-10-24)

## Corpus Check
- 56 files · ~34,998 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 5, .rdb 1, .lock 1)

## Summary
- 998 nodes · 2396 edges · 52 communities (35 shown, 17 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 373 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2a3def9b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- CapturingMailer
- Services
- deps.py
- sites.py
- schemas.py
- main.py
- .uow
- google.py
- steps
- .uow
- Avant: models do MVP
- Limiter
- roles.py
- test_events.py
- audit.py
- Groone Avant: contexto do projeto
- api_keys.py
- account.py
- Arquitetura do MVP do Avant
- login
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- services.py
- mfa.py
- tasks.py
- Avant: conexão com o GAM
- clean_code.py
- .build
- get_actor
- Avant: repositório e plano do MVP
- middleware.py
- health.py
- logs.py
- session-start.sh
- avant-api
- pytest
- require
- install
- RedisCounter
- Counter
- MemoryBucket
- google_start
- limits.py
- RedisBucket
- MemoryCounter
- RedisEvents
- .take
- events
- NoEvents
- GoogleAuth
- is_exempt

## God Nodes (most connected - your core abstractions)
1. `Services` - 125 edges
2. `CapturingMailer` - 47 edges
3. `_onboard_owner()` - 40 edges
4. `_csrf()` - 33 edges
5. `ItemsOut` - 29 edges
6. `get_services()` - 18 edges
7. `_member_client()` - 18 edges
8. `delete()` - 16 edges
9. `get_actor()` - 14 edges
10. `create_app()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/routes/company.py
- `Catálogo de permissões` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/routes/company.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/routes/company.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/routes/internal.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (52 total, 17 thin omitted)

### Community 0 - "CapturingMailer"
Cohesion: 0.08
Nodes (40): CapturingMailer, _csrf(), _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit(), _onboard_owner() (+32 more)

### Community 1 - "Services"
Cohesion: 0.06
Nodes (37): avant-api, Contexto, issues e skills, Modelo de dados, assign_network(), audit(), cancel_owner(), client(), clients() (+29 more)

### Community 2 - "deps.py"
Cohesion: 0.20
Nodes (4): get_session_actor(), CsrfFailed, NoActiveCompany, RateLimited

### Community 3 - "sites.py"
Cohesion: 0.07
Nodes (22): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem, ad_units(), assign_sites(), create() (+14 more)

### Community 4 - "schemas.py"
Cohesion: 0.14
Nodes (12): get_invitation(), AcceptInvitationIn, ActiveCompanyIn, ChangePasswordIn, CompanyPatchIn, DirectPermissionIn, InvitationPreviewOut, LoginIn (+4 more)

### Community 6 - ".uow"
Cohesion: 0.10
Nodes (12): edit(), index(), leave(), remove(), set_permissions(), show(), DirectPermissionOut, MemberDetailOut (+4 more)

### Community 7 - "google.py"
Cohesion: 0.08
Nodes (14): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _google_round(), _jwt() (+6 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - ".uow"
Cohesion: 0.05
Nodes (24): edit(), show(), cancel(), create_invitation(), invitation_out(), list_invitations(), resend(), connect() (+16 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "Limiter"
Cohesion: 0.33
Nodes (4): Limiter, Rule, _limiter_round(), test_memory_limiter()

### Community 12 - "roles.py"
Cohesion: 0.07
Nodes (24): API first e chaves de API, Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa (+16 more)

### Community 13 - "test_events.py"
Cohesion: 0.13
Nodes (10): channel(), EventSource, _parse(), sse(), _collect(), _event(), ListEvents, test_events_route() (+2 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys.py"
Cohesion: 0.16
Nodes (6): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut

### Community 17 - "account.py"
Cohesion: 0.09
Nodes (17): GoogleUnavailable, delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), _google(), google_callback() (+9 more)

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 19 - "login"
Cohesion: 0.14
Nodes (10): accept(), do_logout(), login(), me(), set_active_company(), _set_cookies(), _start(), CompanyOut (+2 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "services.py"
Cohesion: 0.13
Nodes (4): client(), engine(), mailer(), Sent

### Community 23 - "mfa.py"
Cohesion: 0.16
Nodes (8): confirm(), disable(), new_recovery_codes(), setup(), verify(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut

### Community 24 - "tasks.py"
Cohesion: 0.12
Nodes (3): CeleryQueue, RecordingQueue, TaskQueue

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 26 - "clean_code.py"
Cohesion: 0.18
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 27 - ".build"
Cohesion: 0.15
Nodes (4): create_app(), _google(), _mailer(), Settings

### Community 28 - "get_actor"
Cohesion: 0.20
Nodes (6): bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_auth(), optional_auth()

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "middleware.py"
Cohesion: 0.19
Nodes (3): api_key_actor(), observe(), _route_template()

### Community 31 - "health.py"
Cohesion: 0.22
Nodes (3): health(), metrics(), ready()

### Community 37 - "require"
Cohesion: 0.24
Nodes (4): require(), dependency(), require_session(), require_staff()

### Community 38 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 41 - "MemoryBucket"
Cohesion: 0.28
Nodes (4): MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 42 - "google_start"
Cohesion: 0.32
Nodes (3): new_verifier(), _back(), google_start()

### Community 46 - "RedisEvents"
Cohesion: 0.47
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 446 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **17 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Services` connect `Services` to `deps.py`, `sites.py`, `schemas.py`, `main.py`, `.uow`, `.uow`, `Limiter`, `roles.py`, `test_events.py`, `audit.py`, `api_keys.py`, `account.py`, `login`, `services.py`, `mfa.py`, `tasks.py`, `.build`, `get_actor`, `middleware.py`, `health.py`, `RedisCounter`, `Counter`, `MemoryBucket`, `google_start`, `RedisBucket`, `MemoryCounter`, `RedisEvents`, `events`, `NoEvents`, `GoogleAuth`?**
  _High betweenness centrality (0.376) - this node is a cross-community bridge._
- **Are the 105 inferred relationships involving `Services` (e.g. with `api_key_actor()` and `check_csrf()`) actually correct?**
  _`Services` has 105 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `CapturingMailer` be split into smaller, more focused modules?**
  _Cohesion score 0.08220415537488708 - nodes in this community are weakly interconnected._
- **Why does `edit()` connect `.uow` to `Services`, `sites.py`, `schemas.py`, `main.py`, `Avant: models do MVP`, `roles.py`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Are the 32 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 32 INFERRED edges - model-reasoned connections that need verification._
- **Should `Services` be split into smaller, more focused modules?**
  _Cohesion score 0.061668289516390785 - nodes in this community are weakly interconnected._