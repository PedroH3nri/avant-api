# Graph Report - avant-api  (2026-10-28)

## Corpus Check
- 193 files · ~55,940 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2323 nodes · 5860 edges · 147 communities (80 shown, 67 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 941 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `784aebd4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- sites/controller.py
- Actor
- Services
- Services
- google/controller.py
- steps
- NetworkService
- Avant: models do MVP
- _member_client
- CompanyService
- .uow
- audit/controller.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- avant_core_access_models
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- users
- UnitOfWorkFactory
- Avant: conexão com o GAM
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- google/controller.py
- health/controller.py
- main.py
- session-start.sh
- avant-api
- clients/controller.py
- _onboard_owner
- UserOut
- test_internal_assigns_unowned_mcm_network
- test_account.py
- MemberOut
- test_costs_results.py
- install
- ClientOut
- InvitationOut
- AccountService
- limits.py
- test_events.py
- MemberService
- export.py
- .uow
- conftest.py
- edit
- currencies/controller.py
- auth/controller.py
- test_api_keys.py
- ReportQueryIn
- TaskQueue
- GoogleService
- google/controller.py
- reports/service.py
- images.py
- people/controller.py
- mcm/controller.py
- .build
- AuthService
- reports/controller.py
- Limiter
- BaseModel
- connect
- SessionCookies
- avant-api
- company/service.py
- uuid
- google_status
- errors.py
- ItemsOut
- account/controller.py
- networks/service.py
- Counter
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- clients
- auth/service.py
- shared/dto.py
- image_response
- ProfileService
- company/controller.py
- currencies/controller.py
- google_start
- image
- .of
- sync_runs
- SavedReportIn
- templates
- ClientService
- delete_session
- _staff
- MemoryCounter
- image
- verify
- forgot_password
- test_groups_lifecycle
- is_exempt

## God Nodes (most connected - your core abstractions)
1. `Services` - 85 edges
2. `CapturingMailer` - 83 edges
3. `UnitOfWorkFactory` - 79 edges
4. `_onboard_owner()` - 75 edges
5. `_csrf()` - 68 edges
6. `ItemsOut` - 53 edges
7. `ReportService` - 49 edges
8. `ClientService` - 48 edges
9. `_member_client()` - 34 edges
10. `get_services()` - 31 edges

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

## Communities (147 total, 67 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.22
Nodes (9): _csrf(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa() (+1 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (24): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, contract(), contract_networks() (+16 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (11): create(), edit(), index(), permissions(), remove(), role_service(), PermissionOut, RoleIn (+3 more)

### Community 3 - "sites/controller.py"
Cohesion: 0.06
Nodes (23): Atribuição de sites, GAM, Networks, Sites e ad units, ad_units(), assign_sites(), create(), delete() (+15 more)

### Community 4 - "Actor"
Cohesion: 0.17
Nodes (6): cancel_owner(), change_status(), edit_client(), edit_client_image(), invite_owner(), remove_client_image()

### Community 5 - "Services"
Cohesion: 0.09
Nodes (12): api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor(), get_session_auth(), optional_auth() (+4 more)

### Community 6 - "Services"
Cohesion: 0.09
Nodes (6): Services, get_services(), account_service(), currency_service(), event_service(), client_result_service()

### Community 7 - "google/controller.py"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.15
Nodes (12): _event(), test_events_route(), _inventory(), test_manual_site(), test_sites_and_assignment(), _member_client(), test_audit_log(), test_company_and_members() (+4 more)

### Community 12 - "CompanyService"
Cohesion: 0.20
Nodes (3): remove_image(), CompanyDetailOut, CompanyService

### Community 13 - ".uow"
Cohesion: 0.08
Nodes (14): add_members(), create(), edit(), index(), remove(), remove_member(), show(), group_service() (+6 more)

### Community 14 - "audit/controller.py"
Cohesion: 0.14
Nodes (3): index(), audit_service(), AuditService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "avant_core_access_models"
Cohesion: 0.05
Nodes (10): results(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut (+2 more)

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
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

### Community 23 - "users"
Cohesion: 0.22
Nodes (4): Resumo, users(), PersonOut, person_out()

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.20
Nodes (12): CapturingMailer, _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "google/controller.py"
Cohesion: 0.14
Nodes (3): Settings, google_redirects(), GoogleRedirects

### Community 31 - "health/controller.py"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 32 - "main.py"
Cohesion: 0.15
Nodes (3): observe(), _route_template(), create_app()

### Community 36 - "clients/controller.py"
Cohesion: 0.14
Nodes (9): new_owner(), register_client(), client_service(), ClientIn, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn (+1 more)

### Community 37 - "_onboard_owner"
Cohesion: 0.23
Nodes (10): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format(), _png() (+2 more)

### Community 38 - "UserOut"
Cohesion: 0.17
Nodes (3): edit_image(), remove_image(), UserOut

### Community 39 - "test_internal_assigns_unowned_mcm_network"
Cohesion: 0.50
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 40 - "test_account.py"
Cohesion: 0.31
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 41 - "MemberOut"
Cohesion: 0.12
Nodes (5): invite(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 42 - "test_costs_results.py"
Cohesion: 0.16
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "ClientOut"
Cohesion: 0.16
Nodes (3): client(), ClientDetailOut, ClientOut

### Community 45 - "InvitationOut"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 46 - "AccountService"
Cohesion: 0.16
Nodes (4): do_change_password(), get_sessions(), revoke_others(), AccountService

### Community 47 - "limits.py"
Cohesion: 0.08
Nodes (9): Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket() (+1 more)

### Community 48 - "test_events.py"
Cohesion: 0.06
Nodes (15): channel(), EventSource, _parse(), RedisEvents, sse(), configure_logging(), JsonFormatter, events() (+7 more)

### Community 49 - "MemberService"
Cohesion: 0.09
Nodes (8): edit(), index(), leave(), remove(), set_permissions(), show(), MemberDetailOut, MemberService

### Community 50 - "export.py"
Cohesion: 0.14
Nodes (7): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx()

### Community 51 - ".uow"
Cohesion: 0.11
Nodes (4): index(), SavedReportOut, ReportService, _statement_timeout()

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.16
Nodes (3): list_currencies(), update_preferences(), CurrencyService

### Community 55 - "auth/controller.py"
Cohesion: 0.15
Nodes (8): accept(), company_image(), do_logout(), login(), me(), set_active_company(), auth_service(), MeOut

### Community 57 - "test_api_keys.py"
Cohesion: 0.17
Nodes (10): client(), engine(), mailer(), _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit() (+2 more)

### Community 58 - "ReportQueryIn"
Cohesion: 0.15
Nodes (4): query(), ReportQueryIn, ReportResultOut, ReportRowOut

### Community 60 - "GoogleService"
Cohesion: 0.13
Nodes (3): GoogleUnavailable, GoogleAuth, GoogleService

### Community 61 - "google/controller.py"
Cohesion: 0.16
Nodes (3): new_verifier(), google_service(), GoogleStatusOut

### Community 62 - "reports/service.py"
Cohesion: 0.08
Nodes (6): RateLimited, CustomCatalogMetricOut, DimensionOut, LabelOut, MetricCatalogOut, MetricOut

### Community 64 - "people/controller.py"
Cohesion: 0.14
Nodes (5): disable(), enable(), reset_mfa(), people_service(), PeopleService

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - ".build"
Cohesion: 0.08
Nodes (5): _google(), _mailer(), NoEvents, CeleryQueue, RecordingQueue

### Community 67 - "AuthService"
Cohesion: 0.11
Nodes (3): get_invitation(), InvitationPreviewOut, AuthService

### Community 68 - "reports/controller.py"
Cohesion: 0.11
Nodes (10): catalog(), create_from_template(), delete(), duplicate(), export(), export_saved(), run(), show() (+2 more)

### Community 69 - "Limiter"
Cohesion: 0.19
Nodes (5): Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "BaseModel"
Cohesion: 0.15
Nodes (5): FilterIn, OrderIn, PeriodIn, ReportRangeOut, SavedQueryOut

### Community 71 - "connect"
Cohesion: 0.17
Nodes (6): connect(), disconnect(), index(), service_account(), show(), sync()

### Community 72 - "SessionCookies"
Cohesion: 0.12
Nodes (4): SessionCookies, get_cookies(), do_reset_password(), google_callback()

### Community 74 - "company/service.py"
Cohesion: 0.23
Nodes (3): CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 75 - "uuid"
Cohesion: 0.34
Nodes (8): _report(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_saved_report_crud_run_and_duplicate(), test_saved_reports_need_permission(), test_templates_list_and_create(), test_visibility_private_company_and_roles()

### Community 77 - "errors.py"
Cohesion: 0.19
Nodes (4): CsrfFailed, NoActiveCompany, QueryTooHeavy, TooManyAttempts

### Community 78 - "ItemsOut"
Cohesion: 0.20
Nodes (7): audit(), client_teams(), ClientMemberOut, ClientService, AuditOut, CompanyRefOut, ItemsOut

### Community 79 - "account/controller.py"
Cohesion: 0.32
Nodes (5): ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut, SessionOut

### Community 80 - "networks/service.py"
Cohesion: 0.18
Nodes (3): network_service(), NetworkIn, ServiceAccountOut

### Community 82 - "test_company_image.py"
Cohesion: 0.39
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 84 - "clients"
Cohesion: 0.15
Nodes (3): client_image(), clients(), owner_invitations()

### Community 85 - "auth/service.py"
Cohesion: 0.26
Nodes (5): AcceptInvitationIn, ActiveCompanyIn, CompanyOut, LoginIn, LoginOut

### Community 86 - "shared/dto.py"
Cohesion: 0.13
Nodes (7): member_service(), DirectPermissionIn, DirectPermissionOut, MemberPatchIn, MemberPermissionsIn, image_url(), MemberOut

### Community 89 - "image_response"
Cohesion: 0.16
Nodes (3): client_info(), image_response(), image_upload()

### Community 91 - "ProfileService"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 92 - "company/controller.py"
Cohesion: 0.18
Nodes (5): edit_fiscal(), edit_image(), fiscal(), show(), company_service()

### Community 132 - "ClientService"
Cohesion: 0.13
Nodes (3): resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 134 - "_staff"
Cohesion: 0.57
Nodes (6): _staff(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_internal_clients(), test_internal_people_and_staff()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1086 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **67 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `roles/controller.py`, `sites/controller.py`, `ClientService`, `.__init__`, `NetworkService`, `CompanyService`, `.uow`, `audit/controller.py`, `api_keys/controller.py`, `avant_core_access_models`, `.__init__`, `custom_metrics/controller.py`, `costs/controller.py`, `mfa/controller.py`, `MemberOut`, `InvitationOut`, `AccountService`, `MemberService`, `.uow`, `currencies/controller.py`, `TaskQueue`, `GoogleService`, `google/controller.py`, `reports/service.py`, `people/controller.py`, `mcm/controller.py`, `AuthService`, `company/service.py`, `ItemsOut`, `account/controller.py`, `networks/service.py`, `auth/service.py`, `shared/dto.py`, `.__init__`, `.__init__`, `.__init__`, `ProfileService`, `currencies/controller.py`, `.__init__`, `.__init__`, `.__init__`?**
  _High betweenness centrality (0.137) - this node is a cross-community bridge._
- **Are the 52 inferred relationships involving `Services` (e.g. with `Estrutura` and `EventSource`) actually correct?**
  _`Services` has 52 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05744888023369036 - nodes in this community are weakly interconnected._
- **Why does `Services` connect `Services` to `contracts/controller.py`, `roles/controller.py`, `sites/controller.py`, `Services`, `MemoryCounter`, `.uow`, `audit/controller.py`, `api_keys/controller.py`, `avant_core_access_models`, `custom_metrics/controller.py`, `costs/controller.py`, `mfa/controller.py`, `google/controller.py`, `health/controller.py`, `main.py`, `clients/controller.py`, `MemberOut`, `InvitationOut`, `limits.py`, `test_events.py`, `auth/controller.py`, `test_api_keys.py`, `TaskQueue`, `GoogleService`, `google/controller.py`, `images.py`, `people/controller.py`, `mcm/controller.py`, `.build`, `reports/controller.py`, `Limiter`, `SessionCookies`, `networks/service.py`, `shared/dto.py`, `ProfileService`, `company/controller.py`?**
  _High betweenness centrality (0.062) - this node is a cross-community bridge._
- **Are the 60 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 60 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07896575821104122 - nodes in this community are weakly interconnected._