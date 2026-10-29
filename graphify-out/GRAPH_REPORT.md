# Graph Report - avant-api  (2026-10-29)

## Corpus Check
- 201 files · ~59,005 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2475 nodes · 6325 edges · 142 communities (72 shown, 70 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1019 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8fae80b2`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_internal.py
- contracts/controller.py
- roles/controller.py
- sites/controller.py
- ClientService
- security.py
- events.py
- google/controller.py
- steps
- NetworkService
- Avant: models do MVP
- _member_client
- company/controller.py
- .uow
- MemberOut
- Groone Avant: contexto do projeto
- api_keys/controller.py
- avant_core_access_models
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- goals/controller.py
- shared/dto.py
- Avant: conexão com o GAM
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- test_internal.py
- ready
- BaseModel
- session-start.sh
- avant-api
- Settings
- _onboard_owner
- main.py
- AuthService
- test_account.py
- verify
- test_costs_results.py
- install
- ReportService
- invitations/controller.py
- AccountService
- limits.py
- google.py
- set_active_company
- export.py
- .uow
- CompanyDetailOut
- edit
- currencies/controller.py
- account/controller.py
- container.py
- conftest.py
- avant_core_access_models
- delete_session
- test_events.py
- fastapi_testclient
- reports/service.py
- RedisCounter
- people/controller.py
- mcm/controller.py
- TaskQueue
- reports/controller.py
- Limiter
- .uow
- connect
- auth/controller.py
- avant-api
- MemoryBucket
- uuid
- audit/controller.py
- test_report_export.py
- ports.py
- _xlsx_cell
- networks/service.py
- UnitOfWorkFactory
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- fiscal
- image
- CompanyService
- .authenticate
- image_response
- profile/controller.py
- test_sites.py
- edit_fiscal
- .build
- GoogleOAuth
- MemoryCounter
- events
- clients
- images.py
- templates
- image
- edit_image
- do_reset_password
- RateLimited
- source_files

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 94 edges
2. `Services` - 87 edges
3. `_onboard_owner()` - 86 edges
4. `UnitOfWorkFactory` - 82 edges
5. `_csrf()` - 75 edges
6. `ReportService` - 49 edges
7. `ClientService` - 48 edges
8. `ItemsOut` - 47 edges
9. `_member_client()` - 36 edges
10. `PageOut` - 34 edges

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

## Communities (142 total, 70 thin omitted)

### Community 0 - "test_internal.py"
Cohesion: 0.20
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (24): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, contract(), contract_networks() (+16 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "sites/controller.py"
Cohesion: 0.06
Nodes (23): Atribuição de sites, GAM, Networks, Sites e ad units, ad_units(), assign_sites(), create(), delete() (+15 more)

### Community 4 - "ClientService"
Cohesion: 0.08
Nodes (17): audit(), cancel_owner(), change_status(), client(), client_image(), client_teams(), edit_client(), edit_client_image() (+9 more)

### Community 5 - "security.py"
Cohesion: 0.06
Nodes (21): Services, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth() (+13 more)

### Community 6 - "events.py"
Cohesion: 0.19
Nodes (4): channel(), EventSource, _parse(), sse()

### Community 7 - "google/controller.py"
Cohesion: 0.05
Nodes (11): GoogleUnavailable, GoogleAuth, google_callback(), google_start(), google_status(), google_unlink(), google_redirects(), google_service() (+3 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.14
Nodes (12): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _member_client(), test_audit_log(), test_company_and_members() (+4 more)

### Community 12 - "company/controller.py"
Cohesion: 0.22
Nodes (3): CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+6 more)

### Community 14 - "MemberOut"
Cohesion: 0.10
Nodes (6): invite(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "avant_core_access_models"
Cohesion: 0.06
Nodes (10): results(), client_result_service(), ClientResultService, show(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut (+2 more)

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), templates() (+10 more)

### Community 24 - "shared/dto.py"
Cohesion: 0.10
Nodes (17): client_service(), ClientDetailOut, ClientIn, ClientMemberOut, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+9 more)

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "test_reports.py"
Cohesion: 0.20
Nodes (12): CapturingMailer, _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "test_internal.py"
Cohesion: 0.25
Nodes (9): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal(), _staff(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_internal_clients() (+1 more)

### Community 31 - "ready"
Cohesion: 0.10
Nodes (4): health(), metrics(), ready(), HealthService

### Community 32 - "BaseModel"
Cohesion: 0.11
Nodes (6): FilterIn, OrderIn, PeriodIn, ReportRangeOut, ReportRowOut, SavedQueryOut

### Community 36 - "Settings"
Cohesion: 0.11
Nodes (5): Settings, client(), engine(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 37 - "_onboard_owner"
Cohesion: 0.21
Nodes (14): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format() (+6 more)

### Community 38 - "main.py"
Cohesion: 0.13
Nodes (5): configure_logging(), JsonFormatter, observe(), _route_template(), create_app()

### Community 39 - "AuthService"
Cohesion: 0.15
Nodes (4): get_invitation(), auth_service(), InvitationPreviewOut, AuthService

### Community 40 - "test_account.py"
Cohesion: 0.40
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 42 - "test_costs_results.py"
Cohesion: 0.15
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "ReportService"
Cohesion: 0.15
Nodes (4): create(), update(), SavedReportIn, SavedReportOut

### Community 45 - "invitations/controller.py"
Cohesion: 0.10
Nodes (6): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InvitationService

### Community 47 - "limits.py"
Cohesion: 0.15
Nodes (4): TooManyAttempts, Bucket, BucketResult, BucketRule

### Community 48 - "google.py"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), identity_from_id_token(), new_verifier(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 49 - "set_active_company"
Cohesion: 0.19
Nodes (4): company_image(), do_logout(), me(), set_active_company()

### Community 50 - "export.py"
Cohesion: 0.15
Nodes (6): dimension_text(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx()

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "account/controller.py"
Cohesion: 0.17
Nodes (8): get_sessions(), account_service(), ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut, SessionOut, AccountService

### Community 57 - "conftest.py"
Cohesion: 0.15
Nodes (7): mailer(), Sent, _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 60 - "test_events.py"
Cohesion: 0.28
Nodes (6): _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 61 - "fastapi_testclient"
Cohesion: 0.29
Nodes (4): test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_role_options_are_light(), test_team_lists_come_in_pages()

### Community 62 - "reports/service.py"
Cohesion: 0.08
Nodes (6): catalog(), CustomCatalogMetricOut, DimensionOut, LabelOut, MetricCatalogOut, MetricOut

### Community 64 - "people/controller.py"
Cohesion: 0.08
Nodes (10): Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService (+2 more)

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 68 - "reports/controller.py"
Cohesion: 0.12
Nodes (11): create_from_template(), delete(), duplicate(), export(), export_saved(), index(), query(), run() (+3 more)

### Community 69 - "Limiter"
Cohesion: 0.13
Nodes (6): Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - ".uow"
Cohesion: 0.06
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 71 - "connect"
Cohesion: 0.14
Nodes (9): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs(), network_service() (+1 more)

### Community 72 - "auth/controller.py"
Cohesion: 0.16
Nodes (9): SessionCookies, get_cookies(), login(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, LoginIn, LoginOut (+1 more)

### Community 74 - "MemoryBucket"
Cohesion: 0.22
Nodes (5): MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 75 - "uuid"
Cohesion: 0.29
Nodes (15): _csrf(), test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused() (+7 more)

### Community 76 - "audit/controller.py"
Cohesion: 0.11
Nodes (4): index(), audit_service(), AuditService, page_out()

### Community 77 - "test_report_export.py"
Cohesion: 0.24
Nodes (3): _result(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 80 - "networks/service.py"
Cohesion: 0.16
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 82 - "test_company_image.py"
Cohesion: 0.24
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 89 - "image_response"
Cohesion: 0.18
Nodes (3): client_info(), image_response(), image_upload()

### Community 91 - "profile/controller.py"
Cohesion: 0.20
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 92 - "test_sites.py"
Cohesion: 0.39
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 94 - "edit_fiscal"
Cohesion: 0.25
Nodes (3): edit_fiscal(), edit_image(), remove_image()

### Community 95 - ".build"
Cohesion: 0.16
Nodes (5): _mailer(), NoEvents, RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 131 - "templates"
Cohesion: 0.29
Nodes (3): templates(), ReportTemplateOut, ReportService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1156 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **70 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `.__init__`, `templates`, `.trusted_uow`, `ClientService`, `roles/controller.py`, `google/controller.py`, `sites/controller.py`, `.__init__`, `company/controller.py`, `.uow`, `MemberOut`, `api_keys/controller.py`, `avant_core_access_models`, `custom_metrics/controller.py`, `costs/controller.py`, `goals/controller.py`, `shared/dto.py`, `mfa/controller.py`, `AuthService`, `invitations/controller.py`, `.uow`, `currencies/controller.py`, `account/controller.py`, `reports/service.py`, `people/controller.py`, `mcm/controller.py`, `TaskQueue`, `.uow`, `connect`, `audit/controller.py`, `ports.py`, `networks/service.py`, `CompanyService`, `profile/controller.py`?**
  _High betweenness centrality (0.146) - this node is a cross-community bridge._
- **Are the 69 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 69 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.057942057942057944 - nodes in this community are weakly interconnected._
- **Why does `Services` connect `security.py` to `contracts/controller.py`, `images.py`, `roles/controller.py`, `sites/controller.py`, `events.py`, `google/controller.py`, `.uow`, `MemberOut`, `api_keys/controller.py`, `avant_core_access_models`, `custom_metrics/controller.py`, `costs/controller.py`, `goals/controller.py`, `shared/dto.py`, `mfa/controller.py`, `Settings`, `main.py`, `AuthService`, `invitations/controller.py`, `limits.py`, `currencies/controller.py`, `account/controller.py`, `container.py`, `avant_core_access_models`, `RedisCounter`, `people/controller.py`, `mcm/controller.py`, `TaskQueue`, `Limiter`, `.uow`, `connect`, `auth/controller.py`, `MemoryBucket`, `audit/controller.py`, `CompanyService`, `profile/controller.py`, `.build`, `MemoryCounter`?**
  _High betweenness centrality (0.065) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Services` (e.g. with `Estrutura` and `EventSource`) actually correct?**
  _`Services` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07344632768361582 - nodes in this community are weakly interconnected._