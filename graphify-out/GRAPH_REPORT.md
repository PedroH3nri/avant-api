# Graph Report - avant-api  (2026-10-26)

## Corpus Check
- 63 files · ~40,220 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 1218 nodes · 2994 edges · 68 communities (51 shown, 17 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 457 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b7f034e5`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- CapturingMailer
- UUID
- edit
- assign_sites
- schemas.py
- main.py
- .uow
- google.py
- steps
- networks.py
- Avant: models do MVP
- Limiter
- edit
- avant_api/events.py
- audit.py
- Groone Avant: contexto do projeto
- api_keys.py
- account.py
- Arquitetura do MVP do Avant
- auth.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs.py
- internal.py
- tasks.py
- Avant: conexão com o GAM
- clean_code.py
- create_app
- get_actor
- Avant: repositório e plano do MVP
- Settings
- health.py
- logs.py
- session-start.sh
- avant-api
- show
- sites.py
- install
- RedisCounter
- Counter
- Services
- google_callback
- errors.py
- .trusted_uow
- MemoryCounter
- RedisEvents
- limits.py
- uuid
- Actor
- reports.py
- pytest
- Avant: endpoints da API do MVP
- invitations.py
- ad_units
- client
- GAM
- observe
- avant-api
- Acesso
- GoogleAuth
- Suporte
- Empresa e equipe
- NoEvents
- unassigned_networks
- source_files
- .of

## God Nodes (most connected - your core abstractions)
1. `Services` - 147 edges
2. `CapturingMailer` - 63 edges
3. `_onboard_owner()` - 55 edges
4. `_csrf()` - 48 edges
5. `ItemsOut` - 34 edges
6. `get_services()` - 22 edges
7. `_member_client()` - 21 edges
8. `create_app()` - 15 edges
9. `get_actor()` - 14 edges
10. `require()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/routes/company.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/routes/company.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/routes/internal.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/routes/internal.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (68 total, 17 thin omitted)

### Community 0 - "CapturingMailer"
Cohesion: 0.05
Nodes (60): CapturingMailer, mailer(), Sent, _csrf(), _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys() (+52 more)

### Community 1 - "UUID"
Cohesion: 0.11
Nodes (11): contract(), disable(), edit_contract(), finish_contract(), new_contract(), new_owner(), reactivate(), reset_mfa() (+3 more)

### Community 2 - "edit"
Cohesion: 0.11
Nodes (9): API first e chaves de API, create(), edit(), index(), permissions(), remove(), RoleIn, RoleOut (+1 more)

### Community 3 - "assign_sites"
Cohesion: 0.12
Nodes (6): assign_sites(), delete(), index(), members(), show(), sites_of_member()

### Community 4 - "schemas.py"
Cohesion: 0.08
Nodes (35): _person(), AssignNetworkIn, ClientIn, ClientPatchIn, CompanyOut, CompanyRefOut, ContractIn, ContractPatchIn (+27 more)

### Community 5 - "main.py"
Cohesion: 0.08
Nodes (11): get_services(), require(), CompanyDetailOut, CompanyPatchIn, CurrencyOut, InvitationOut, InviteIn, MemberPatchIn (+3 more)

### Community 6 - ".uow"
Cohesion: 0.12
Nodes (6): edit(), index(), leave(), remove(), set_permissions(), show()

### Community 7 - "google.py"
Cohesion: 0.07
Nodes (15): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), FakeGoogle, _google_round() (+7 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "networks.py"
Cohesion: 0.12
Nodes (12): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs(), NetworkDetailOut (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.18
Nodes (10): Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade, Invitation, Membership, User (+2 more)

### Community 11 - "Limiter"
Cohesion: 0.21
Nodes (6): TooManyAttempts, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 12 - "edit"
Cohesion: 0.20
Nodes (3): Catálogo de permissões, edit(), show()

### Community 13 - "avant_api/events.py"
Cohesion: 0.21
Nodes (4): channel(), EventSource, _parse(), sse()

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys.py"
Cohesion: 0.15
Nodes (6): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut

### Community 17 - "account.py"
Cohesion: 0.11
Nodes (14): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), google_status(), google_unlink(), revoke_others() (+6 more)

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 19 - "auth.py"
Cohesion: 0.07
Nodes (23): accept(), _client(), do_logout(), _end(), get_invitation(), login(), me(), set_active_company() (+15 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "costs.py"
Cohesion: 0.12
Nodes (10): check_formula(), create(), delete(), index(), _input(), update(), CostIn, CostOut (+2 more)

### Community 23 - "internal.py"
Cohesion: 0.13
Nodes (9): Modelo de dados, audit(), clients(), contract_networks(), contracts(), results(), staff(), users() (+1 more)

### Community 24 - "tasks.py"
Cohesion: 0.12
Nodes (3): CeleryQueue, RecordingQueue, TaskQueue

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 28 - "get_actor"
Cohesion: 0.13
Nodes (9): api_key_actor(), bearer_token(), get_actor(), get_auth(), get_session_auth(), optional_auth(), dependency(), require_session() (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "Settings"
Cohesion: 0.13
Nodes (6): create_app(), _google(), _mailer(), Settings, client(), engine()

### Community 31 - "health.py"
Cohesion: 0.20
Nodes (3): health(), metrics(), ready()

### Community 37 - "sites.py"
Cohesion: 0.22
Nodes (7): create(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut

### Community 38 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 41 - "Services"
Cohesion: 0.18
Nodes (5): list_currencies(), update_preferences(), assign_network(), enqueue_sync(), Services

### Community 42 - "google_callback"
Cohesion: 0.19
Nodes (6): GoogleUnavailable, _back(), _google(), google_callback(), google_start(), _session()

### Community 43 - "errors.py"
Cohesion: 0.16
Nodes (6): check_csrf(), get_session_actor(), CsrfFailed, NoActiveCompany, QueryTooHeavy, RateLimited

### Community 44 - ".trusted_uow"
Cohesion: 0.18
Nodes (5): avant-api, Contexto, issues e skills, cancel_owner(), enable(), remove_contract()

### Community 46 - "RedisEvents"
Cohesion: 0.47
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 47 - "limits.py"
Cohesion: 0.10
Nodes (8): Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 48 - "uuid"
Cohesion: 0.27
Nodes (6): _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 50 - "Actor"
Cohesion: 0.27
Nodes (5): create_client(), _owner_invitation(), owner_invitations(), resend_owner(), OwnerInvitationOut

### Community 51 - "reports.py"
Cohesion: 0.05
Nodes (10): catalog(), _csv(), export(), _number(), query(), _run(), _safe_cell(), _statement_timeout() (+2 more)

### Community 53 - "Avant: endpoints da API do MVP"
Cohesion: 0.20
Nodes (9): Atribuição de sites, Avant: endpoints da API do MVP, Convenções, Decisões de Pedro (23/10/2026), GAM, Networks, Painel interno, Sites e ad units (+1 more)

### Community 54 - "invitations.py"
Cohesion: 0.14
Nodes (6): invite(), cancel(), create_invitation(), invitation_out(), list_invitations(), resend()

### Community 55 - "ad_units"
Cohesion: 0.28
Nodes (3): ad_units(), link(), AdUnitOut

### Community 56 - "client"
Cohesion: 0.31
Nodes (4): client(), edit_client(), ClientDetailOut, ClientOut

### Community 57 - "GAM"
Cohesion: 0.33
Nodes (6): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment

### Community 59 - "avant-api"
Cohesion: 0.33
Nodes (5): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem

### Community 60 - "Acesso"
Cohesion: 0.40
Nodes (5): Acesso, MemberPermission, Permission, Role, RolePermission

### Community 62 - "Suporte"
Cohesion: 0.40
Nodes (5): ApiKey, AuditLog, PasswordReset, Session, Suporte

### Community 63 - "Empresa e equipe"
Cohesion: 0.40
Nodes (5): Convites, Empresa, Empresa e equipe, Membros, Papéis e permissões

### Community 68 - ".of"
Cohesion: 0.18
Nodes (5): ContractClientRefOut, ContractNetworkOut, ContractNetworkRefOut, ContractSummaryOut, _network_ref()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 539 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **17 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Services` connect `Services` to `UUID`, `edit`, `assign_sites`, `main.py`, `.uow`, `networks.py`, `Limiter`, `edit`, `avant_api/events.py`, `audit.py`, `api_keys.py`, `account.py`, `auth.py`, `costs.py`, `internal.py`, `tasks.py`, `create_app`, `get_actor`, `Settings`, `health.py`, `show`, `sites.py`, `RedisCounter`, `google_callback`, `errors.py`, `.trusted_uow`, `MemoryCounter`, `RedisEvents`, `limits.py`, `Actor`, `reports.py`, `invitations.py`, `ad_units`, `client`, `GoogleAuth`, `NoEvents`, `unassigned_networks`?**
  _High betweenness centrality (0.382) - this node is a cross-community bridge._
- **Are the 123 inferred relationships involving `Services` (e.g. with `api_key_actor()` and `check_csrf()`) actually correct?**
  _`Services` has 123 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `CapturingMailer` be split into smaller, more focused modules?**
  _Cohesion score 0.050354384851369935 - nodes in this community are weakly interconnected._
- **Why does `contracts()` connect `internal.py` to `UUID`, `Services`, `.trusted_uow`, `Groone Avant: contexto do projeto`, `Actor`?**
  _High betweenness centrality (0.042) - this node is a cross-community bridge._
- **Are the 45 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 45 INFERRED edges - model-reasoned connections that need verification._
- **Should `UUID` be split into smaller, more focused modules?**
  _Cohesion score 0.10826210826210826 - nodes in this community are weakly interconnected._