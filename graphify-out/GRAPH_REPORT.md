# Graph Report - avant-api  (2026-10-26)

## Corpus Check
- 63 files · ~40,998 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 1248 nodes · 3062 edges · 75 communities (55 shown, 20 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 469 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3af8579c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts
- edit
- sites.py
- schemas.py
- Services
- .uow
- google.py
- steps
- networks.py
- Avant: models do MVP
- CapturingMailer
- edit
- avant_api/events.py
- audit.py
- Groone Avant: contexto do projeto
- create
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
- test_reports.py
- get_actor
- Avant: repositório e plano do MVP
- Settings
- health.py
- main.py
- session-start.sh
- avant-api
- results
- GoogleFailed
- install
- _onboard_owner
- conftest.py
- Services
- test_costs_results.py
- errors.py
- .trusted_uow
- MemoryCounter
- RedisEvents
- limits.py
- uuid
- edit
- reports.py
- _run
- catalog
- Avant: endpoints da API do MVP
- invitations.py
- test_account.py
- ItemsOut
- test_api_keys.py
- observe
- avant-api
- test_networks.py
- edit_fiscal
- .of
- Empresa e equipe
- users
- unassigned_networks
- source_files
- contract_networks
- show
- sync_runs
- _csv
- .format
- avant-api

## God Nodes (most connected - your core abstractions)
1. `Services` - 149 edges
2. `CapturingMailer` - 64 edges
3. `_onboard_owner()` - 56 edges
4. `_csrf()` - 49 edges
5. `ItemsOut` - 34 edges
6. `_member_client()` - 23 edges
7. `get_services()` - 22 edges
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

## Communities (75 total, 20 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.14
Nodes (14): _csrf(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _staff(), test_client_owner_cannot_reach_internal(), test_fiscal_data_only_by_the_client(), test_internal_clients() (+6 more)

### Community 1 - "contracts"
Cohesion: 0.14
Nodes (7): contract(), contracts(), edit_contract(), new_contract(), _contract_fields(), ContractOut, ContractPatchIn

### Community 2 - "edit"
Cohesion: 0.11
Nodes (9): API first e chaves de API, create(), edit(), index(), permissions(), remove(), RoleIn, RoleOut (+1 more)

### Community 3 - "sites.py"
Cohesion: 0.08
Nodes (16): ad_units(), assign_sites(), create(), delete(), index(), link(), members(), show() (+8 more)

### Community 4 - "schemas.py"
Cohesion: 0.07
Nodes (31): AdUnitPatchIn, ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ClientProfileIn, ClientProfileOut, CompanyOut, CompanyPatchIn (+23 more)

### Community 5 - "Services"
Cohesion: 0.15
Nodes (4): get_services(), require(), revoke(), Services

### Community 6 - ".uow"
Cohesion: 0.13
Nodes (5): index(), leave(), remove(), set_permissions(), show()

### Community 7 - "google.py"
Cohesion: 0.15
Nodes (6): challenge(), _claims(), identity_from_id_token(), new_verifier(), _jwt(), test_id_token_claims()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "networks.py"
Cohesion: 0.14
Nodes (10): connect(), disconnect(), enqueue_sync(), index(), service_account(), show(), sync(), NetworkDetailOut (+2 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "CapturingMailer"
Cohesion: 0.20
Nodes (11): CapturingMailer, _inventory(), test_manual_site(), test_sites_and_assignment(), _member_client(), test_audit_log(), test_company_and_members(), test_leave_company() (+3 more)

### Community 12 - "edit"
Cohesion: 0.24
Nodes (4): Catálogo de permissões, edit(), show(), CompanyDetailOut

### Community 13 - "avant_api/events.py"
Cohesion: 0.21
Nodes (4): channel(), EventSource, _parse(), sse()

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 17 - "account.py"
Cohesion: 0.08
Nodes (20): _back(), delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), _google(), google_callback() (+12 more)

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 19 - "auth.py"
Cohesion: 0.07
Nodes (22): accept(), _client(), do_logout(), get_invitation(), login(), me(), set_active_company(), _set_cookies() (+14 more)

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
Cohesion: 0.12
Nodes (10): audit(), change_status(), invite(), AssignNetworkIn, AuditOut, ClientStatusIn, ContractIn, InvitationOut (+2 more)

### Community 24 - "tasks.py"
Cohesion: 0.12
Nodes (4): Bucket, CeleryQueue, RecordingQueue, TaskQueue

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "test_reports.py"
Cohesion: 0.21
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "get_actor"
Cohesion: 0.11
Nodes (10): api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_auth(), optional_auth(), dependency() (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "Settings"
Cohesion: 0.10
Nodes (5): NoEvents, GoogleAuth, _google(), _mailer(), Settings

### Community 31 - "health.py"
Cohesion: 0.20
Nodes (3): health(), metrics(), ready()

### Community 32 - "main.py"
Cohesion: 0.10
Nodes (3): configure_logging(), create_app(), events()

### Community 36 - "results"
Cohesion: 0.11
Nodes (6): results(), ContractClientRefOut, CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut

### Community 37 - "GoogleFailed"
Cohesion: 0.14
Nodes (3): GoogleFailed, GoogleOAuth, FakeGoogle

### Community 38 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 39 - "_onboard_owner"
Cohesion: 0.26
Nodes (8): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format()

### Community 40 - "conftest.py"
Cohesion: 0.16
Nodes (4): client(), engine(), mailer(), Sent

### Community 42 - "test_costs_results.py"
Cohesion: 0.21
Nodes (4): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone()

### Community 43 - "errors.py"
Cohesion: 0.18
Nodes (5): get_session_actor(), CsrfFailed, GoogleUnavailable, NoActiveCompany, RateLimited

### Community 44 - ".trusted_uow"
Cohesion: 0.13
Nodes (13): assign_network(), cancel_owner(), disable(), enable(), finish_contract(), invite_owner(), new_owner(), _owner_invitation() (+5 more)

### Community 46 - "RedisEvents"
Cohesion: 0.24
Nodes (5): RedisEvents, test_redis_source_delivers_published_messages(), run(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 47 - "limits.py"
Cohesion: 0.05
Nodes (15): TooManyAttempts, BucketResult, BucketRule, Counter, Limiter, MemoryBucket, RedisBucket, RedisCounter (+7 more)

### Community 48 - "uuid"
Cohesion: 0.27
Nodes (6): _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 50 - "reports.py"
Cohesion: 0.15
Nodes (3): QueryTooHeavy, _number(), _statement_timeout()

### Community 51 - "_run"
Cohesion: 0.21
Nodes (4): export(), query(), _run(), ReportQueryIn

### Community 53 - "Avant: endpoints da API do MVP"
Cohesion: 0.20
Nodes (9): Atribuição de sites, Avant: endpoints da API do MVP, Convenções, Decisões de Pedro (23/10/2026), GAM, Networks, Painel interno, Sites e ad units (+1 more)

### Community 54 - "invitations.py"
Cohesion: 0.16
Nodes (5): cancel(), create_invitation(), invitation_out(), list_invitations(), resend()

### Community 55 - "test_account.py"
Cohesion: 0.35
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 56 - "ItemsOut"
Cohesion: 0.12
Nodes (13): client(), clients(), edit_client(), register_client(), staff(), ClientDetailOut, ClientIn, ClientOut (+5 more)

### Community 57 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 59 - "avant-api"
Cohesion: 0.33
Nodes (5): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem

### Community 60 - "test_networks.py"
Cohesion: 0.47
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 61 - "edit_fiscal"
Cohesion: 0.25
Nodes (3): edit_fiscal(), fiscal(), CompanyFiscalOut

### Community 63 - "Empresa e equipe"
Cohesion: 0.40
Nodes (5): Convites, Empresa, Empresa e equipe, Membros, Papéis e permissões

### Community 64 - "users"
Cohesion: 0.29
Nodes (5): Modelo de dados, _person(), users(), CompanyRefOut, PersonOut

### Community 68 - "contract_networks"
Cohesion: 0.33
Nodes (3): contract_networks(), ContractNetworkOut, ContractSummaryOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 554 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **20 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Services` connect `Services` to `contracts`, `edit`, `sites.py`, `.uow`, `networks.py`, `edit`, `avant_api/events.py`, `audit.py`, `create`, `account.py`, `auth.py`, `costs.py`, `internal.py`, `tasks.py`, `get_actor`, `Settings`, `health.py`, `main.py`, `results`, `conftest.py`, `Services`, `.trusted_uow`, `MemoryCounter`, `RedisEvents`, `limits.py`, `edit`, `reports.py`, `_run`, `invitations.py`, `ItemsOut`, `edit_fiscal`, `users`, `unassigned_networks`, `contract_networks`, `show`, `sync_runs`?**
  _High betweenness centrality (0.397) - this node is a cross-community bridge._
- **Are the 125 inferred relationships involving `Services` (e.g. with `api_key_actor()` and `check_csrf()`) actually correct?**
  _`Services` has 125 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.1443850267379679 - nodes in this community are weakly interconnected._
- **Why does `edit()` connect `edit` to `schemas.py`, `Services`, `.uow`, `Avant: models do MVP`, `avant-api`, `edit_fiscal`, `Empresa e equipe`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Are the 46 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 46 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts` be split into smaller, more focused modules?**
  _Cohesion score 0.1437908496732026 - nodes in this community are weakly interconnected._