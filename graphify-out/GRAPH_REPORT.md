# Graph Report - avant-api  (2026-11-03)

## Corpus Check
- 244 files · ~76,981 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3296 nodes · 8977 edges · 170 communities (89 shown, 81 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1523 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d4d2dc37`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- DashboardService
- AlertService
- currencies/controller.py
- commissions/controller.py
- test_events.py
- steps
- schedules/controller.py
- Avant: models do MVP
- test_company_image.py
- .trusted_uow
- GroupService
- sync_runs
- Groone Avant: contexto do projeto
- api_keys/controller.py
- pydantic
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- dashboard_templates/controller.py
- invoice_pdf.py
- UnitOfWorkFactory
- clean_code.py
- CapturingMailer
- mfa/controller.py
- Avant: repositório e plano do MVP
- get
- clients/controller.py
- Actor
- session-start.sh
- avant-api
- ClientService
- _member_client
- invoices/controller.py
- export.py
- staff/controller.py
- CompanyService
- AuthService
- errors.py
- limits.py
- CostService
- _onboard_owner
- views/controller.py
- auth/controller.py
- datetime
- security.py
- ReportResultOut
- UserOut
- edit
- currencies/controller.py
- members/controller.py
- conftest.py
- health/controller.py
- google/controller.py
- edit_fiscal
- account/controller.py
- main.py
- Actor
- Actor
- mcm/controller.py
- CapturingMailer
- sites/controller.py
- reports/controller.py
- Limiter
- auth/service.py
- sqlalchemy
- FakeGoogle
- avant-api
- .show
- uuid
- people/controller.py
- Avant: conexão com o GAM
- networks/service.py
- costs/service.py
- modules/results/controller.py
- InvoiceService
- test_dashboards.py
- InvoiceServiceOut
- events.py
- company/controller.py
- Avant: grupos na Empresa e imagem da Empresa
- AdUnitOut
- test_members_without_schedules_manage_only_see_what_they_receive
- profile/controller.py
- .show
- GoalService
- update_item
- SiteOut
- images.py
- image
- test_alerts.py
- image
- .owner_invitations
- reports/service.py
- SiteListOut
- QueryTooHeavy
- new_owner
- TaskQueue
- shared/dto.py
- ReportService
- test_account.py
- SiteService
- AuditOut
- google/controller.py
- members
- clients
- client_image
- test_goal_progress_routes

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 129 edges
2. `PageOut` - 116 edges
3. `_csrf()` - 116 edges
4. `_onboard_owner()` - 115 edges
5. `get()` - 105 edges
6. `UnitOfWorkFactory` - 103 edges
7. `Services` - 102 edges
8. `ReportService` - 75 edges
9. `InvoiceService` - 58 edges
10. `ClientService` - 54 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/modules/internal/people/controller.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (170 total, 81 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.10
Nodes (25): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+17 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.05
Nodes (25): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+17 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (21): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+13 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "currencies/controller.py"
Cohesion: 0.08
Nodes (16): CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor() (+8 more)

### Community 6 - "commissions/controller.py"
Cohesion: 0.05
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 7 - "test_events.py"
Cohesion: 0.15
Nodes (12): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit(), _collect(), _event(), ListEvents (+4 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "test_company_image.py"
Cohesion: 0.16
Nodes (7): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture()

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "sync_runs"
Cohesion: 0.18
Nodes (7): connect(), disconnect(), options(), service_account(), show(), sync(), sync_runs()

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "pydantic"
Cohesion: 0.10
Nodes (8): require(), cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService, InvitationOut

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
Cohesion: 0.19
Nodes (4): delete(), index(), update(), cost_service()

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "CapturingMailer"
Cohesion: 0.36
Nodes (9): _day(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour(), test_query_needs_permission(), test_query_refuses_bad_definitions_and_internal_metrics(), test_query_totals_rows_and_member_sites() (+1 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "get"
Cohesion: 0.09
Nodes (14): add_item(), available_months(), create_service(), delete(), delete_service(), get(), issue(), pay() (+6 more)

### Community 31 - "clients/controller.py"
Cohesion: 0.24
Nodes (9): ClientIn, ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn, ManagerChangeOut, OwnerChangeIn (+1 more)

### Community 36 - "ClientService"
Cohesion: 0.21
Nodes (6): client_teams(), manager_change(), client_service(), ClientMemberOut, ClientService, CompanyRefOut

### Community 37 - "_member_client"
Cohesion: 0.14
Nodes (13): _membership_ids(), test_groups_lifecycle(), _inventory(), test_manual_site(), test_site_category_and_responsible(), test_sites_and_assignment(), _member_client(), test_audit_log() (+5 more)

### Community 38 - "invoices/controller.py"
Cohesion: 0.20
Nodes (11): update_item(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut (+3 more)

### Community 39 - "export.py"
Cohesion: 0.07
Nodes (12): JsonFormatter, dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx() (+4 more)

### Community 40 - "staff/controller.py"
Cohesion: 0.10
Nodes (9): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, ItemsOut, MemberOut (+1 more)

### Community 41 - "CompanyService"
Cohesion: 0.21
Nodes (3): show(), CompanyDetailOut, CompanyService

### Community 43 - "errors.py"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "limits.py"
Cohesion: 0.06
Nodes (10): TooManyAttempts, BucketResult, BucketRule, MemoryBucket, MemoryCounter, RedisBucket, RedisCounter, _exercise() (+2 more)

### Community 45 - "CostService"
Cohesion: 0.26
Nodes (4): check_formula(), FormulaCheckIn, FormulaCheckOut, CostService

### Community 46 - "_onboard_owner"
Cohesion: 0.22
Nodes (16): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format(), test_costs_and_reports_come_in_pages() (+8 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "auth/controller.py"
Cohesion: 0.09
Nodes (10): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), login(), me(), set_active_company() (+2 more)

### Community 49 - "datetime"
Cohesion: 0.06
Nodes (8): results(), ClientResultService, show(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut, default_period()

### Community 50 - "security.py"
Cohesion: 0.05
Nodes (13): Services, get_services(), audit_service(), auth_service(), company_service(), dashboard_service(), commission_service(), goal_service() (+5 more)

### Community 51 - "ReportResultOut"
Cohesion: 0.18
Nodes (4): query(), ReportQueryIn, ReportResultOut, ReportRowOut

### Community 52 - "UserOut"
Cohesion: 0.13
Nodes (4): person_out(), edit_image(), remove_image(), UserOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (13): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+5 more)

### Community 56 - "conftest.py"
Cohesion: 0.10
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 57 - "health/controller.py"
Cohesion: 0.15
Nodes (4): health(), ready(), health_service(), HealthService

### Community 58 - "google/controller.py"
Cohesion: 0.04
Nodes (18): GoogleFailed, GoogleUnavailable, challenge(), _claims(), GoogleAuth, GoogleOAuth, identity_from_id_token(), new_verifier() (+10 more)

### Community 59 - "edit_fiscal"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 60 - "account/controller.py"
Cohesion: 0.10
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 62 - "main.py"
Cohesion: 0.04
Nodes (15): _google(), _mailer(), RedisEvents, configure_logging(), observe(), _route_template(), Settings, CeleryQueue (+7 more)

### Community 63 - "Actor"
Cohesion: 0.12
Nodes (9): audit(), cancel_owner(), change_status(), client_options(), edit_client(), edit_client_image(), invite_owner(), remove_client_image() (+1 more)

### Community 64 - "Actor"
Cohesion: 0.12
Nodes (8): ad_units(), assign_sites(), classify(), classify_many(), delete(), link(), site_options(), unlinked()

### Community 65 - "mcm/controller.py"
Cohesion: 0.12
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "CapturingMailer"
Cohesion: 0.13
Nodes (14): CapturingMailer, mailer(), Sent, test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_internal_clients(), test_internal_people_and_staff() (+6 more)

### Community 67 - "sites/controller.py"
Cohesion: 0.24
Nodes (5): AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 68 - "reports/controller.py"
Cohesion: 0.09
Nodes (14): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned() (+6 more)

### Community 69 - "Limiter"
Cohesion: 0.13
Nodes (5): Counter, Limiter, Rule, _limiter_round(), test_memory_limiter()

### Community 70 - "auth/service.py"
Cohesion: 0.15
Nodes (8): get_invitation(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut, image_url()

### Community 71 - "sqlalchemy"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 74 - ".show"
Cohesion: 0.19
Nodes (3): index(), NetworkDetailOut, NetworkService

### Community 75 - "uuid"
Cohesion: 0.16
Nodes (19): _owner_invite(), test_csv_header_escapes_formulas(), _metrics(), _row(), test_export_csv_uses_names_and_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles() (+11 more)

### Community 76 - "people/controller.py"
Cohesion: 0.13
Nodes (8): Modelo de dados, disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService

### Community 77 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 78 - "networks/service.py"
Cohesion: 0.17
Nodes (4): network_service(), NetworkIn, ServiceAccountOut, SyncRunOut

### Community 79 - "costs/service.py"
Cohesion: 0.22
Nodes (4): create(), CostIn, CostOut, _input()

### Community 82 - "InvoiceService"
Cohesion: 0.20
Nodes (4): mine(), service_options(), invoice_service(), InvoiceService

### Community 83 - "test_dashboards.py"
Cohesion: 0.28
Nodes (7): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit()

### Community 85 - "events.py"
Cohesion: 0.07
Nodes (8): channel(), EventSource, NoEvents, _parse(), sse(), events(), event_service(), EventService

### Community 86 - "company/controller.py"
Cohesion: 0.20
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 89 - "test_members_without_schedules_manage_only_see_what_they_receive"
Cohesion: 0.24
Nodes (3): _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 91 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 95 - "GoalService"
Cohesion: 0.06
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+10 more)

### Community 98 - "SiteOut"
Cohesion: 0.21
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 131 - "test_alerts.py"
Cohesion: 0.35
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 136 - "reports/service.py"
Cohesion: 0.06
Nodes (14): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+6 more)

### Community 137 - "SiteListOut"
Cohesion: 0.14
Nodes (3): create(), index(), SiteListOut

### Community 143 - "shared/dto.py"
Cohesion: 0.09
Nodes (3): index(), page_out(), PageOut

### Community 145 - "ReportService"
Cohesion: 0.13
Nodes (7): Bucket, index(), templates(), LabelOut, ReportPageOut, ReportTemplateOut, ReportService

### Community 146 - "test_account.py"
Cohesion: 0.31
Nodes (7): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited(), test_redis_limiter()

### Community 147 - "SiteService"
Cohesion: 0.23
Nodes (4): show(), site_service(), SiteDetailOut, SiteService

### Community 155 - "google/controller.py"
Cohesion: 0.18
Nodes (3): client_info(), image_response(), image_upload()

### Community 167 - "clients"
Cohesion: 0.18
Nodes (3): clients(), register_client(), ClientOut

### Community 175 - "test_goal_progress_routes"
Cohesion: 0.53
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1514 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **81 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `.__init__`, `contracts/controller.py`, `DashboardService`, `AlertService`, `roles/controller.py`, `commissions/controller.py`, `reports/service.py`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `TaskQueue`, `shared/dto.py`, `api_keys/controller.py`, `pydantic`, `ReportService`, `custom_metrics/controller.py`, `SiteService`, `.__init__`, `.__init__`, `dashboard_templates/controller.py`, `.__init__`, `mfa/controller.py`, `.__init__`, `clients/controller.py`, `ClientService`, `invoices/controller.py`, `staff/controller.py`, `CompanyService`, `AuthService`, `.__init__`, `CostService`, `views/controller.py`, `datetime`, `currencies/controller.py`, `members/controller.py`, `google/controller.py`, `account/controller.py`, `mcm/controller.py`, `sites/controller.py`, `auth/service.py`, `.show`, `people/controller.py`, `networks/service.py`, `modules/results/controller.py`, `InvoiceService`, `company/controller.py`, `profile/controller.py`, `costs/service.py`, `GoalService`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Are the 95 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 95 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.10431372549019607 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `shared/dto.py` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `Actor`, `.owner_invitations`, `reports/service.py`, `schedules/controller.py`, `SiteListOut`, `.trusted_uow`, `GroupService`, `sync_runs`, `api_keys/controller.py`, `pydantic`, `ReportService`, `SiteService`, `costs/controller.py`, `UnitOfWorkFactory`, `get`, `clients/controller.py`, `ClientService`, `invoices/controller.py`, `clients`, `staff/controller.py`, `CostService`, `datetime`, `members/controller.py`, `Actor`, `Actor`, `mcm/controller.py`, `sites/controller.py`, `.show`, `people/controller.py`, `networks/service.py`, `costs/service.py`, `InvoiceService`, `InvoiceServiceOut`, `AdUnitOut`, `costs/service.py`, `GoalService`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Are the 47 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 47 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05432098765432099 - nodes in this community are weakly interconnected._