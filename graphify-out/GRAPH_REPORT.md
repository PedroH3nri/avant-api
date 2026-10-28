# Graph Report - avant-api  (2026-10-28)

## Corpus Check
- 181 files · ~51,965 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2137 nodes · 5316 edges · 127 communities (72 shown, 55 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 851 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `11b1a9a9`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- sites/controller.py
- clients/controller.py
- Services
- google.py
- steps
- NetworkService
- Avant: models do MVP
- _member_client
- CompanyService
- .uow
- ItemsOut
- Groone Avant: contexto do projeto
- api_keys/controller.py
- avant_core_access_models
- Arquitetura do MVP do Avant
- client_info
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- shared/dto.py
- tasks.py
- Avant: conexão com o GAM
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- Settings
- health/controller.py
- main.py
- session-start.sh
- avant-api
- .of
- FakeGoogle
- profile/controller.py
- _onboard_owner
- conftest.py
- UnitOfWorkFactory
- test_costs_results.py
- errors.py
- .trusted_uow
- InvitationOut
- account/controller.py
- limits.py
- test_events.py
- members/controller.py
- csv_export.py
- ReportQueryIn
- edit
- currencies/controller.py
- test_account.py
- ClientOut
- test_api_keys.py
- events/controller.py
- TaskQueue
- CapturingMailer
- auth/controller.py
- reports/dto.py
- GoogleService
- people/controller.py
- mcm/controller.py
- .build
- login
- ReportService
- Limiter
- sync_runs
- networks/controller.py
- SessionCookies
- avant-api
- company/controller.py
- AuthService
- google_start
- reports/service.py
- Actor
- test_sites.py
- networks/service.py
- Counter
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- google_unlink
- image_response
- _staff
- image
- test_groups.py
- require
- edit_image
- users
- Bucket
- fiscal

## God Nodes (most connected - your core abstractions)
1. `Services` - 82 edges
2. `UnitOfWorkFactory` - 76 edges
3. `CapturingMailer` - 73 edges
4. `_onboard_owner()` - 65 edges
5. `_csrf()` - 58 edges
6. `ClientService` - 48 edges
7. `ItemsOut` - 48 edges
8. `SiteService` - 31 edges
9. `_member_client()` - 31 edges
10. `get_services()` - 29 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py
- `Pipeline` --references--> `main()`  [INFERRED]
  docs/decisoes/07-repositorios-e-plano.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (127 total, 55 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.25
Nodes (9): _csrf(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa() (+1 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (11): create(), edit(), index(), permissions(), remove(), role_service(), PermissionOut, RoleIn (+3 more)

### Community 3 - "sites/controller.py"
Cohesion: 0.05
Nodes (23): Atribuição de sites, GAM, Networks, Sites e ad units, ad_units(), assign_sites(), create(), delete() (+15 more)

### Community 4 - "clients/controller.py"
Cohesion: 0.10
Nodes (15): cancel_owner(), change_status(), edit_client_image(), invite_owner(), new_owner(), register_client(), remove_client_image(), resend_owner() (+7 more)

### Community 5 - "Services"
Cohesion: 0.06
Nodes (14): Services, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_services(), get_session_actor(), get_session_auth() (+6 more)

### Community 7 - "google.py"
Cohesion: 0.12
Nodes (6): GoogleFailed, challenge(), _claims(), identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "NetworkService"
Cohesion: 0.19
Nodes (3): index(), NetworkDetailOut, NetworkService

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.19
Nodes (10): _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _member_client(), test_audit_log(), test_company_and_members(), test_leave_company(), test_requires_session() (+2 more)

### Community 12 - "CompanyService"
Cohesion: 0.21
Nodes (3): show(), CompanyDetailOut, CompanyService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), remove(), remove_member(), show(), group_service() (+6 more)

### Community 14 - "ItemsOut"
Cohesion: 0.11
Nodes (6): index(), audit_service(), AuditService, audit(), AuditOut, ItemsOut

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "avant_core_access_models"
Cohesion: 0.07
Nodes (8): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, default_period(), ResultService

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 19 - "client_info"
Cohesion: 0.24
Nodes (3): do_reset_password(), forgot_password(), client_info()

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 23 - "shared/dto.py"
Cohesion: 0.08
Nodes (8): ClientMemberOut, ClientProfileOut, staff(), CompanyRefOut, FiscalDataOut, image_url(), MemberOut, RoleRefOut

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 26 - "clean_code.py"
Cohesion: 0.15
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.22
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "Settings"
Cohesion: 0.13
Nodes (4): Settings, account_service(), google_redirects(), GoogleRedirects

### Community 31 - "health/controller.py"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 32 - "main.py"
Cohesion: 0.10
Nodes (5): configure_logging(), JsonFormatter, observe(), _route_template(), create_app()

### Community 36 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 38 - "profile/controller.py"
Cohesion: 0.09
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService, UserOut

### Community 39 - "_onboard_owner"
Cohesion: 0.38
Nodes (7): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format()

### Community 40 - "conftest.py"
Cohesion: 0.17
Nodes (3): client(), engine(), mailer()

### Community 41 - "UnitOfWorkFactory"
Cohesion: 0.08
Nodes (5): UnitOfWorkFactory, invite(), staff_service(), StaffInviteIn, StaffService

### Community 42 - "test_costs_results.py"
Cohesion: 0.29
Nodes (4): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone()

### Community 43 - "errors.py"
Cohesion: 0.09
Nodes (10): CsrfFailed, error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), NoActiveCompany (+2 more)

### Community 44 - ".trusted_uow"
Cohesion: 0.11
Nodes (4): client(), ClientDetailOut, ClientService, owner_invitation_out()

### Community 45 - "InvitationOut"
Cohesion: 0.10
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService, InvitationOut

### Community 46 - "account/controller.py"
Cohesion: 0.10
Nodes (12): do_change_password(), get_sessions(), google_status(), revoke_others(), google_service(), ChangePasswordIn, ForgotPasswordIn, GoogleStatusOut (+4 more)

### Community 47 - "limits.py"
Cohesion: 0.09
Nodes (8): BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 48 - "test_events.py"
Cohesion: 0.10
Nodes (14): channel(), _parse(), RedisEvents, sse(), _collect(), _event(), ListEvents, test_events_route() (+6 more)

### Community 49 - "members/controller.py"
Cohesion: 0.07
Nodes (13): edit(), index(), leave(), remove(), set_permissions(), show(), member_service(), DirectPermissionIn (+5 more)

### Community 50 - "csv_export.py"
Cohesion: 0.15
Nodes (4): _number(), _safe_cell(), to_csv(), dimension_text()

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "test_account.py"
Cohesion: 0.35
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 57 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 58 - "events/controller.py"
Cohesion: 0.12
Nodes (4): EventSource, events(), event_service(), EventService

### Community 59 - "TaskQueue"
Cohesion: 0.12
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskQueue, enqueue_sync()

### Community 60 - "CapturingMailer"
Cohesion: 0.22
Nodes (9): CapturingMailer, Sent, _owner_invite(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company() (+1 more)

### Community 61 - "auth/controller.py"
Cohesion: 0.12
Nodes (8): get_auth(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut, MeOut

### Community 62 - "reports/dto.py"
Cohesion: 0.19
Nodes (9): DimensionOut, FilterIn, LabelOut, MetricOut, OrderIn, PeriodIn, ReportRangeOut, ReportResultOut (+1 more)

### Community 63 - "GoogleService"
Cohesion: 0.12
Nodes (4): GoogleUnavailable, GoogleAuth, google_callback(), GoogleService

### Community 64 - "people/controller.py"
Cohesion: 0.10
Nodes (7): disable(), enable(), reset_mfa(), people_service(), PersonOut, PeopleService, person_out()

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - ".build"
Cohesion: 0.09
Nodes (5): _google(), _mailer(), NoEvents, GoogleOAuth, MemoryCounter

### Community 67 - "login"
Cohesion: 0.12
Nodes (6): company_image(), do_logout(), get_invitation(), login(), me(), set_active_company()

### Community 68 - "ReportService"
Cohesion: 0.15
Nodes (6): catalog(), export(), query(), report_service(), MetricCatalogOut, ReportService

### Community 69 - "Limiter"
Cohesion: 0.18
Nodes (5): Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "networks/controller.py"
Cohesion: 0.16
Nodes (6): connect(), disconnect(), service_account(), show(), sync(), network_service()

### Community 72 - "SessionCookies"
Cohesion: 0.15
Nodes (3): SessionCookies, get_cookies(), delete_session()

### Community 74 - "company/controller.py"
Cohesion: 0.17
Nodes (5): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 77 - "reports/service.py"
Cohesion: 0.15
Nodes (3): QueryTooHeavy, RateLimited, _statement_timeout()

### Community 78 - "Actor"
Cohesion: 0.19
Nodes (4): client_image(), client_teams(), clients(), owner_invitations()

### Community 79 - "test_sites.py"
Cohesion: 0.29
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 82 - "test_company_image.py"
Cohesion: 0.36
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "_staff"
Cohesion: 0.57
Nodes (6): _staff(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_internal_clients(), test_internal_people_and_staff()

### Community 91 - "require"
Cohesion: 0.33
Nodes (3): require(), dependency(), require_session()

### Community 93 - "users"
Cohesion: 0.40
Nodes (3): Modelo de dados, Resumo, users()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1001 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **55 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `roles/controller.py`, `sites/controller.py`, `NetworkService`, `CompanyService`, `.uow`, `ItemsOut`, `api_keys/controller.py`, `avant_core_access_models`, `costs/controller.py`, `shared/dto.py`, `mfa/controller.py`, `profile/controller.py`, `.trusted_uow`, `InvitationOut`, `account/controller.py`, `members/controller.py`, `currencies/controller.py`, `TaskQueue`, `auth/controller.py`, `GoogleService`, `people/controller.py`, `mcm/controller.py`, `ReportService`, `AuthService`, `reports/service.py`, `networks/service.py`, `Counter`, `Bucket`, `.__init__`, `.__init__`, `.__init__`?**
  _High betweenness centrality (0.162) - this node is a cross-community bridge._
- **Are the 51 inferred relationships involving `Services` (e.g. with `Estrutura` and `EventSource`) actually correct?**
  _`Services` has 51 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06572769953051644 - nodes in this community are weakly interconnected._
- **Why does `Services` connect `Services` to `contracts/controller.py`, `roles/controller.py`, `sites/controller.py`, `clients/controller.py`, `.uow`, `.uow`, `ItemsOut`, `avant_core_access_models`, `costs/controller.py`, `tasks.py`, `mfa/controller.py`, `Settings`, `health/controller.py`, `main.py`, `conftest.py`, `UnitOfWorkFactory`, `errors.py`, `account/controller.py`, `limits.py`, `test_events.py`, `members/controller.py`, `currencies/controller.py`, `events/controller.py`, `TaskQueue`, `GoogleService`, `people/controller.py`, `mcm/controller.py`, `.build`, `ReportService`, `Limiter`, `networks/controller.py`, `SessionCookies`, `company/controller.py`, `Bucket`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Are the 24 inferred relationships involving `UnitOfWorkFactory` (e.g. with `GoogleService` and `AccountService`) actually correct?**
  _`UnitOfWorkFactory` has 24 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08392156862745098 - nodes in this community are weakly interconnected._