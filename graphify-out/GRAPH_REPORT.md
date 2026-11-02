# Graph Report - avant-api  (2026-11-02)

## Corpus Check
- 220 files · ~71,110 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 2964 nodes · 8035 edges · 161 communities (87 shown, 74 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1355 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b35b6002`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- ContractService
- roles/controller.py
- DashboardService
- UserOut
- security.py
- .save_rule
- conftest.py
- steps
- _month
- Avant: models do MVP
- test_client_changes_the_company_image
- .trusted_uow
- GroupService
- networks/controller.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- pydantic
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- GoalService
- invoice_pdf.py
- contracts
- clean_code.py
- CapturingMailer
- mfa/controller.py
- Avant: repositório e plano do MVP
- get
- ReportService
- .uow
- session-start.sh
- avant-api
- ClientService
- _member_client
- invoices/controller.py
- export.py
- contracts/controller.py
- CompanyService
- main.py
- errors.py
- limits.py
- InvoiceService
- CapturingMailer
- ContractClientRefOut
- AuthService
- datetime
- security.py
- ReportResultOut
- require_staff
- edit
- currencies/controller.py
- members/controller.py
- _xlsx_cell
- health/controller.py
- mine
- company/controller.py
- account/controller.py
- Actor
- google/controller.py
- clients/controller.py
- ItemsOut
- mcm/controller.py
- test_networks.py
- do_reset_password
- reports/controller.py
- Limiter
- auth/controller.py
- sqlalchemy
- google.py
- avant-api
- test_report_export.py
- uuid
- people/controller.py
- Avant: conexão com o GAM
- commissions/dto.py
- image
- dollars
- GoogleService
- .networks
- test_dashboards.py
- RedisCounter
- events.py
- edit_image
- Avant: grupos na Empresa e imagem da Empresa
- test_events.py
- middleware.py
- profile/controller.py
- CeleryQueue
- ClientOut
- .page_saved
- source_files
- test_permissions_on_keys
- logs.py
- delete_session
- client_image
- MemoryCounter
- Actor
- image
- Actor
- events/controller.py
- reports/service.py
- CommissionRuleOut
- CommissionService
- avant-api
- PageOut
- person
- templates
- test_goal_progress_routes
- RedisEvents
- ReportPreviewOut
- clients
- test_groups_lifecycle
- ClientProfileIn
- google/controller.py
- NoEvents
- RateLimited

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 115 edges
2. `PageOut` - 107 edges
3. `_csrf()` - 103 edges
4. `_onboard_owner()` - 103 edges
5. `get()` - 95 edges
6. `Services` - 94 edges
7. `UnitOfWorkFactory` - 91 edges
8. `ReportService` - 70 edges
9. `InvoiceService` - 58 edges
10. `ClientService` - 54 edges

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

## Communities (161 total, 74 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.10
Nodes (29): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+21 more)

### Community 1 - "ContractService"
Cohesion: 0.16
Nodes (4): O que já tem, contract(), ContractOut, ContractService

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (21): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+13 more)

### Community 4 - "UserOut"
Cohesion: 0.14
Nodes (3): edit_image(), remove_image(), UserOut

### Community 5 - "security.py"
Cohesion: 0.13
Nodes (9): api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor(), get_session_auth(), optional_auth() (+1 more)

### Community 6 - ".save_rule"
Cohesion: 0.16
Nodes (6): adjust(), create_rule(), delete_rule(), rules(), update_rule(), CommissionRuleIn

### Community 7 - "conftest.py"
Cohesion: 0.09
Nodes (5): client(), engine(), mailer(), _event(), test_events_route()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "test_client_changes_the_company_image"
Cohesion: 0.39
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "networks/controller.py"
Cohesion: 0.06
Nodes (16): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+8 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "pydantic"
Cohesion: 0.08
Nodes (9): invite(), StaffInviteIn, cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService (+1 more)

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

### Community 23 - "GoalService"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+10 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "contracts"
Cohesion: 0.14
Nodes (6): contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract()

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "CapturingMailer"
Cohesion: 0.23
Nodes (12): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (9): auth_service(), confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "get"
Cohesion: 0.08
Nodes (15): add_item(), available_months(), create(), delete(), delete_service(), get(), issue(), mine() (+7 more)

### Community 31 - "ReportService"
Cohesion: 0.10
Nodes (8): create(), create_from_template(), duplicate(), pinned(), show(), SavedReportIn, SavedReportOut, ReportService

### Community 36 - "ClientService"
Cohesion: 0.16
Nodes (8): client_teams(), client_service(), ClientDetailOut, ClientMemberOut, ClientOptionOut, ManagerChangeOut, ClientService, CompanyRefOut

### Community 37 - "_member_client"
Cohesion: 0.14
Nodes (14): _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_site_category_and_responsible(), test_sites_and_assignment(), _member_client() (+6 more)

### Community 38 - "invoices/controller.py"
Cohesion: 0.14
Nodes (12): save_payment_details(), update_item(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut (+4 more)

### Community 39 - "export.py"
Cohesion: 0.15
Nodes (6): dimension_text(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx()

### Community 40 - "contracts/controller.py"
Cohesion: 0.22
Nodes (6): _contract_fields(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut

### Community 41 - "CompanyService"
Cohesion: 0.18
Nodes (4): show(), company_service(), CompanyDetailOut, CompanyService

### Community 42 - "main.py"
Cohesion: 0.09
Nodes (6): _google(), _mailer(), Settings, create_app(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 43 - "errors.py"
Cohesion: 0.13
Nodes (10): CsrfFailed, error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), NoActiveCompany (+2 more)

### Community 44 - "limits.py"
Cohesion: 0.11
Nodes (7): BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 45 - "InvoiceService"
Cohesion: 0.17
Nodes (6): create_service(), services(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 46 - "CapturingMailer"
Cohesion: 0.17
Nodes (23): CapturingMailer, _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited(), _onboard_owner() (+15 more)

### Community 47 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 48 - "AuthService"
Cohesion: 0.08
Nodes (9): get_invitation(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut, AuthService (+1 more)

### Community 49 - "datetime"
Cohesion: 0.06
Nodes (8): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, default_period(), ResultService

### Community 50 - "security.py"
Cohesion: 0.08
Nodes (11): Services, PillowImageProcessor, get_services(), google_redirects(), google_service(), contract_service(), goal_service(), staff_service() (+3 more)

### Community 51 - "ReportResultOut"
Cohesion: 0.15
Nodes (4): query(), ReportQueryIn, ReportResultOut, ReportRowOut

### Community 52 - "require_staff"
Cohesion: 0.20
Nodes (5): dependency(), require_report(), require_session(), require_staff(), require_staff_member()

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): API first e chaves de API, Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.05
Nodes (16): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+8 more)

### Community 57 - "health/controller.py"
Cohesion: 0.11
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 59 - "company/controller.py"
Cohesion: 0.20
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 60 - "account/controller.py"
Cohesion: 0.13
Nodes (9): get_sessions(), revoke_others(), account_service(), ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut, SessionOut (+1 more)

### Community 63 - "clients/controller.py"
Cohesion: 0.12
Nodes (13): audit(), cancel_owner(), change_status(), client(), client_options(), edit_client_image(), invite_owner(), manager_change() (+5 more)

### Community 64 - "ItemsOut"
Cohesion: 0.05
Nodes (25): ad_units(), assign_sites(), classify(), classify_many(), create(), delete(), index(), link() (+17 more)

### Community 65 - "mcm/controller.py"
Cohesion: 0.11
Nodes (6): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService

### Community 66 - "test_networks.py"
Cohesion: 0.40
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 67 - "do_reset_password"
Cohesion: 0.20
Nodes (3): do_change_password(), do_reset_password(), forgot_password()

### Community 68 - "reports/controller.py"
Cohesion: 0.11
Nodes (9): catalog(), delete(), export(), export_saved(), pin(), run(), unpin(), update() (+1 more)

### Community 69 - "Limiter"
Cohesion: 0.11
Nodes (6): Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "auth/controller.py"
Cohesion: 0.09
Nodes (12): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), login(), me(), set_active_company() (+4 more)

### Community 71 - "sqlalchemy"
Cohesion: 0.11
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 72 - "google.py"
Cohesion: 0.09
Nodes (9): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), FakeGoogle, _jwt() (+1 more)

### Community 74 - "test_report_export.py"
Cohesion: 0.24
Nodes (3): _result(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 75 - "uuid"
Cohesion: 0.19
Nodes (17): Sent, _owner_invite(), test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx() (+9 more)

### Community 76 - "people/controller.py"
Cohesion: 0.09
Nodes (10): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PersonOut (+2 more)

### Community 77 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 78 - "commissions/dto.py"
Cohesion: 0.17
Nodes (5): AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn

### Community 81 - "GoogleService"
Cohesion: 0.08
Nodes (6): GoogleUnavailable, GoogleAuth, google_start(), google_status(), google_unlink(), GoogleService

### Community 83 - "test_dashboards.py"
Cohesion: 0.32
Nodes (6): _form(), _kpi(), _run(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit()

### Community 85 - "events.py"
Cohesion: 0.18
Nodes (4): channel(), EventSource, _parse(), sse()

### Community 86 - "edit_image"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "test_events.py"
Cohesion: 0.43
Nodes (4): _collect(), ListEvents, test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 91 - "profile/controller.py"
Cohesion: 0.20
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 94 - "ClientOut"
Cohesion: 0.15
Nodes (6): edit_client(), register_client(), ClientIn, ClientOut, ClientPatchIn, ClientProfileOut

### Community 95 - ".page_saved"
Cohesion: 0.22
Nodes (3): index(), ReportCountsOut, ReportPageOut

### Community 98 - "test_permissions_on_keys"
Cohesion: 0.50
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 134 - "Actor"
Cohesion: 0.23
Nodes (3): owner_invitations(), OwnerInvitationOut, owner_invitation_out()

### Community 135 - "events/controller.py"
Cohesion: 0.17
Nodes (3): events(), event_service(), EventService

### Community 136 - "reports/service.py"
Cohesion: 0.05
Nodes (14): Bucket, TaskQueue, CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut (+6 more)

### Community 139 - "CommissionService"
Cohesion: 0.18
Nodes (3): set_settings(), commission_service(), CommissionService

### Community 142 - "avant-api"
Cohesion: 0.33
Nodes (5): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem

### Community 143 - "PageOut"
Cohesion: 0.05
Nodes (10): UnitOfWorkFactory, require(), index(), audit_service(), AuditService, options(), staff(), StaffService (+2 more)

### Community 146 - "test_goal_progress_routes"
Cohesion: 0.53
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 147 - "RedisEvents"
Cohesion: 0.47
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1365 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **74 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `PageOut` to `ContractService`, `roles/controller.py`, `DashboardService`, `.__init__`, `reports/service.py`, `.__init__`, `CommissionService`, `.trusted_uow`, `GroupService`, `networks/controller.py`, `api_keys/controller.py`, `pydantic`, `custom_metrics/controller.py`, `.__init__`, `costs/controller.py`, `GoalService`, `mfa/controller.py`, `ReportService`, `.uow`, `.__init__`, `ClientService`, `invoices/controller.py`, `contracts/controller.py`, `CompanyService`, `InvoiceService`, `AuthService`, `datetime`, `currencies/controller.py`, `members/controller.py`, `company/controller.py`, `account/controller.py`, `ItemsOut`, `mcm/controller.py`, `Limiter`, `people/controller.py`, `commissions/dto.py`, `GoogleService`, `profile/controller.py`?**
  _High betweenness centrality (0.110) - this node is a cross-community bridge._
- **Are the 87 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 87 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.096045197740113 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `ContractService`, `roles/controller.py`, `DashboardService`, `Actor`, `Actor`, `reports/service.py`, `.trusted_uow`, `GroupService`, `networks/controller.py`, `api_keys/controller.py`, `pydantic`, `costs/controller.py`, `GoalService`, `clients`, `contracts`, `get`, `ClientService`, `invoices/controller.py`, `contracts/controller.py`, `InvoiceService`, `datetime`, `members/controller.py`, `clients/controller.py`, `ItemsOut`, `mcm/controller.py`, `people/controller.py`, `.page_saved`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **Are the 43 inferred relationships involving `PageOut` (e.g. with `index()` and `ApiKeyService`) actually correct?**
  _`PageOut` has 43 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07441016333938294 - nodes in this community are weakly interconnected._