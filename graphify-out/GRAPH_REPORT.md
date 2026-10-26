# Graph Report - avant-api  (2026-10-26)

## Corpus Check
- 60 files · ~38,646 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 1139 nodes · 2805 edges · 71 communities (52 shown, 19 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 429 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4c4e113d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- Services
- edit
- sites.py
- schemas.py
- networks.py
- .uow
- google.py
- steps
- networks.py
- Avant: models do MVP
- Limiter
- company.py
- avant_api/events.py
- audit.py
- Groone Avant: contexto do projeto
- api_keys.py
- account.py
- Arquitetura do MVP do Avant
- auth.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- test_account.py
- .uow
- tasks.py
- Avant: conexão com o GAM
- clean_code.py
- create_app
- deps.py
- Avant: repositório e plano do MVP
- Settings
- health.py
- main.py
- session-start.sh
- avant-api
- services.py
- catalog
- install
- RedisCounter
- Counter
- MemoryBucket
- google_callback
- errors.py
- limits.py
- MemoryCounter
- RedisEvents
- limits.py
- uuid
- test_reports.py
- UserOut
- reports.py
- pytest
- require
- invitations.py
- permissions
- .of
- _run
- observe
- CapturingMailer
- _onboard_owner
- GoogleAuth
- test_networks.py
- _contract_fields
- FakeGoogle
- McmCandidateOut
- currencies.py
- test_api_keys.py
- .of
- test_sites.py
- is_exempt

## God Nodes (most connected - your core abstractions)
1. `Services` - 139 edges
2. `CapturingMailer` - 59 edges
3. `_onboard_owner()` - 52 edges
4. `_csrf()` - 44 edges
5. `ItemsOut` - 31 edges
6. `_member_client()` - 21 edges
7. `get_services()` - 20 edges
8. `delete()` - 17 edges
9. `get_actor()` - 14 edges
10. `create_app()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/routes/company.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/routes/internal.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/routes/internal.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (71 total, 19 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.17
Nodes (13): _csrf(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _staff(), test_client_owner_cannot_reach_internal(), test_internal_clients(), test_internal_people_and_staff() (+5 more)

### Community 1 - "Services"
Cohesion: 0.06
Nodes (39): avant-api, Contexto, issues e skills, Modelo de dados, list_currencies(), update_preferences(), assign_network(), audit(), cancel_owner() (+31 more)

### Community 2 - "edit"
Cohesion: 0.17
Nodes (5): create(), edit(), index(), remove(), RoleOut

### Community 3 - "sites.py"
Cohesion: 0.09
Nodes (13): ad_units(), assign_sites(), create(), index(), link(), members(), show(), sites_of_member() (+5 more)

### Community 4 - "schemas.py"
Cohesion: 0.08
Nodes (33): AcceptInvitationIn, ActiveCompanyIn, AdUnitPatchIn, ApiKeyIn, AssignNetworkIn, ClientIn, ClientPatchIn, CompanyOut (+25 more)

### Community 6 - ".uow"
Cohesion: 0.11
Nodes (9): edit(), index(), leave(), remove(), set_permissions(), show(), MemberDetailOut, MemberOut (+1 more)

### Community 7 - "google.py"
Cohesion: 0.12
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), _jwt(), test_id_token_claims()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "networks.py"
Cohesion: 0.13
Nodes (8): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs(), SyncRunOut

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "Limiter"
Cohesion: 0.33
Nodes (4): Limiter, Rule, _limiter_round(), test_memory_limiter()

### Community 12 - "company.py"
Cohesion: 0.06
Nodes (24): Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+16 more)

### Community 13 - "avant_api/events.py"
Cohesion: 0.15
Nodes (5): channel(), EventSource, NoEvents, _parse(), sse()

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys.py"
Cohesion: 0.17
Nodes (5): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyOut

### Community 17 - "account.py"
Cohesion: 0.10
Nodes (15): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), google_status(), google_unlink(), revoke_others() (+7 more)

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 19 - "auth.py"
Cohesion: 0.08
Nodes (18): accept(), _client(), do_logout(), get_invitation(), login(), me(), set_active_company(), _set_cookies() (+10 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "test_account.py"
Cohesion: 0.27
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 24 - "tasks.py"
Cohesion: 0.10
Nodes (3): CeleryQueue, RecordingQueue, TaskQueue

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 26 - "clean_code.py"
Cohesion: 0.18
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 28 - "deps.py"
Cohesion: 0.19
Nodes (8): api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_session_actor(), optional_auth(), CsrfFailed, NoActiveCompany

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "Settings"
Cohesion: 0.18
Nodes (3): _google(), _mailer(), Settings

### Community 31 - "health.py"
Cohesion: 0.20
Nodes (3): health(), metrics(), ready()

### Community 32 - "main.py"
Cohesion: 0.24
Nodes (3): configure_logging(), JsonFormatter, create_app()

### Community 36 - "services.py"
Cohesion: 0.12
Nodes (3): Sent, _event(), test_events_route()

### Community 37 - "catalog"
Cohesion: 0.16
Nodes (4): catalog(), DimensionOut, LabelOut, MetricOut

### Community 38 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 41 - "MemoryBucket"
Cohesion: 0.28
Nodes (4): MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 42 - "google_callback"
Cohesion: 0.25
Nodes (5): GoogleUnavailable, _back(), _google(), google_callback(), google_start()

### Community 43 - "errors.py"
Cohesion: 0.16
Nodes (3): QueryTooHeavy, RateLimited, TooManyAttempts

### Community 46 - "RedisEvents"
Cohesion: 0.47
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 47 - "limits.py"
Cohesion: 0.21
Nodes (3): Bucket, BucketResult, BucketRule

### Community 48 - "uuid"
Cohesion: 0.39
Nodes (4): _collect(), ListEvents, test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 49 - "test_reports.py"
Cohesion: 0.21
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 50 - "UserOut"
Cohesion: 0.33
Nodes (4): _person(), CompanyRefOut, PersonOut, UserOut

### Community 51 - "reports.py"
Cohesion: 0.11
Nodes (4): _number(), _safe_cell(), _statement_timeout(), MetricCatalogOut

### Community 52 - "pytest"
Cohesion: 0.16
Nodes (5): client(), engine(), mailer(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 53 - "require"
Cohesion: 0.29
Nodes (3): dependency(), require_session(), require_staff()

### Community 54 - "invitations.py"
Cohesion: 0.19
Nodes (7): cancel(), create_invitation(), invitation_out(), list_invitations(), resend(), InvitationOut, InviteIn

### Community 56 - ".of"
Cohesion: 0.18
Nodes (4): dimension_text(), ReportRangeOut, ReportResultOut, ReportRowOut

### Community 57 - "_run"
Cohesion: 0.18
Nodes (5): _csv(), export(), query(), _run(), ReportQueryIn

### Community 59 - "CapturingMailer"
Cohesion: 0.29
Nodes (8): CapturingMailer, _member_client(), test_audit_log(), test_company_and_members(), test_leave_company(), test_requires_session(), test_resend_and_cancel_invitation(), test_roles_and_direct_permissions()

### Community 60 - "_onboard_owner"
Cohesion: 0.30
Nodes (7): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format()

### Community 62 - "test_networks.py"
Cohesion: 0.42
Nodes (7): _owner_invite(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 67 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 68 - ".of"
Cohesion: 0.15
Nodes (7): ContractClientRefOut, ContractNetworkOut, ContractNetworkRefOut, ContractSummaryOut, _network_ref(), NetworkDetailOut, NetworkOut

### Community 69 - "test_sites.py"
Cohesion: 0.39
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 500 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **19 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Services` connect `Services` to `edit`, `sites.py`, `networks.py`, `.uow`, `networks.py`, `Limiter`, `company.py`, `avant_api/events.py`, `audit.py`, `api_keys.py`, `account.py`, `auth.py`, `.uow`, `tasks.py`, `create_app`, `deps.py`, `Settings`, `health.py`, `main.py`, `services.py`, `RedisCounter`, `MemoryBucket`, `google_callback`, `limits.py`, `MemoryCounter`, `RedisEvents`, `limits.py`, `reports.py`, `pytest`, `invitations.py`, `_run`, `GoogleAuth`, `currencies.py`?**
  _High betweenness centrality (0.412) - this node is a cross-community bridge._
- **Are the 117 inferred relationships involving `Services` (e.g. with `api_key_actor()` and `check_csrf()`) actually correct?**
  _`Services` has 117 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Services` be split into smaller, more focused modules?**
  _Cohesion score 0.05958485958485959 - nodes in this community are weakly interconnected._
- **Why does `edit()` connect `company.py` to `Services`, `Avant: models do MVP`, `.uow`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Are the 42 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 42 INFERRED edges - model-reasoned connections that need verification._
- **Should `sites.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08773784355179703 - nodes in this community are weakly interconnected._