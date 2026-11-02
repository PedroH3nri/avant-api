# Graph Report - avant-api  (2026-11-02)

## Corpus Check
- 238 files · ~75,580 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3214 nodes · 8744 edges · 184 communities (104 shown, 80 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1483 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0a12a43e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- ContractService
- roles/controller.py
- DashboardService
- AlertService
- currencies/controller.py
- .save_rule
- test_events.py
- steps
- schedules/controller.py
- Avant: models do MVP
- test_client_changes_the_company_image
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
- GoalTemplateOut
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
- middleware.py
- errors.py
- limits.py
- _onboard_owner
- views/controller.py
- auth/controller.py
- avant_core_access_models
- security.py
- ReportResultOut
- UserOut
- edit
- currencies/controller.py
- members/controller.py
- conftest.py
- health/controller.py
- GoogleService
- edit_fiscal
- account/controller.py
- ._out
- typing
- Actor
- Actor
- mcm/controller.py
- test_networks.py
- sites/controller.py
- reports/controller.py
- Limiter
- avant_core_shared_clock
- sqlalchemy
- google.py
- avant-api
- .show
- uuid
- people/controller.py
- Avant: conexão com o GAM
- networks/service.py
- costs/service.py
- dollars
- require
- mine
- test_dashboards.py
- commissions/controller.py
- events.py
- company/controller.py
- Avant: grupos na Empresa e imagem da Empresa
- AdUnitOut
- profile/controller.py
- .build
- ClientOut
- goals/controller.py
- team
- SiteOut
- ContractClientRefOut
- image
- contracts/controller.py
- CommissionService
- test_alerts.py
- Actor
- image
- .owner_invitations
- reports/service.py
- SiteListOut
- Actor
- edit_contract
- container.py
- shared/dto.py
- logs.py
- templates
- test_account.py
- SiteService
- GoalService
- to_csv
- .page_saved
- AuditOut
- google/controller.py
- goals/service.py
- members
- contracts
- mine
- test_api_keys.py
- io
- .networks
- person
- clients
- client_image
- MfaService
- test_goal_progress_routes
- set_settings
- _contract_fields
- RateLimited
- enqueue_sync

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 126 edges
2. `PageOut` - 116 edges
3. `_csrf()` - 113 edges
4. `_onboard_owner()` - 112 edges
5. `get()` - 102 edges
6. `Services` - 100 edges
7. `UnitOfWorkFactory` - 100 edges
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

## Communities (184 total, 80 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.08
Nodes (35): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+27 more)

### Community 1 - "ContractService"
Cohesion: 0.17
Nodes (3): contract(), ContractOut, ContractService

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (21): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+13 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "currencies/controller.py"
Cohesion: 0.09
Nodes (14): CsrfFailed, NoActiveCompany, QueryTooHeavy, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth() (+6 more)

### Community 6 - ".save_rule"
Cohesion: 0.16
Nodes (5): create_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 7 - "test_events.py"
Cohesion: 0.28
Nodes (6): _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "test_client_changes_the_company_image"
Cohesion: 0.39
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+6 more)

### Community 14 - "sync_runs"
Cohesion: 0.21
Nodes (5): disconnect(), service_account(), show(), sync(), sync_runs()

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.12
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "pydantic"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (11): check(), create(), delete(), index(), update(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn (+3 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "costs/controller.py"
Cohesion: 0.14
Nodes (8): check_formula(), delete(), index(), update(), cost_service(), FormulaCheckIn, FormulaCheckOut, CostService

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "UnitOfWorkFactory"
Cohesion: 0.06
Nodes (3): UnitOfWorkFactory, AuditService, CurrencyService

### Community 26 - "clean_code.py"
Cohesion: 0.15
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "CapturingMailer"
Cohesion: 0.22
Nodes (12): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (7): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "get"
Cohesion: 0.10
Nodes (22): add_item(), available_months(), create(), create_service(), delete(), delete_service(), get(), issue() (+14 more)

### Community 31 - "clients/controller.py"
Cohesion: 0.24
Nodes (9): ClientIn, ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn, ManagerChangeOut, OwnerChangeIn (+1 more)

### Community 36 - "ClientService"
Cohesion: 0.21
Nodes (5): client_teams(), manager_change(), client_service(), ClientMemberOut, ClientService

### Community 37 - "_member_client"
Cohesion: 0.14
Nodes (10): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_site_category_and_responsible() (+2 more)

### Community 38 - "invoices/controller.py"
Cohesion: 0.15
Nodes (11): AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceServiceOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut (+3 more)

### Community 40 - "staff/controller.py"
Cohesion: 0.11
Nodes (7): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 41 - "CompanyService"
Cohesion: 0.21
Nodes (3): show(), CompanyDetailOut, CompanyService

### Community 42 - "middleware.py"
Cohesion: 0.15
Nodes (4): observe(), _route_template(), create_app(), health()

### Community 43 - "errors.py"
Cohesion: 0.13
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "limits.py"
Cohesion: 0.09
Nodes (8): BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 46 - "_onboard_owner"
Cohesion: 0.14
Nodes (23): CapturingMailer, _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format() (+15 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "auth/controller.py"
Cohesion: 0.07
Nodes (16): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+8 more)

### Community 49 - "avant_core_access_models"
Cohesion: 0.10
Nodes (6): require_staff(), results(), client_result_service(), ClientResultService, ResultsOut, default_period()

### Community 50 - "security.py"
Cohesion: 0.06
Nodes (12): Estrutura, Services, get_services(), audit_service(), company_service(), currency_service(), custom_metric_service(), dashboard_service() (+4 more)

### Community 51 - "ReportResultOut"
Cohesion: 0.18
Nodes (4): query(), ReportQueryIn, ReportResultOut, ReportRowOut

### Community 52 - "UserOut"
Cohesion: 0.17
Nodes (3): edit_image(), remove_image(), UserOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (4): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+6 more)

### Community 56 - "conftest.py"
Cohesion: 0.11
Nodes (3): client(), engine(), mailer()

### Community 57 - "health/controller.py"
Cohesion: 0.16
Nodes (3): ready(), health_service(), HealthService

### Community 58 - "GoogleService"
Cohesion: 0.07
Nodes (6): GoogleUnavailable, GoogleAuth, google_callback(), google_status(), google_unlink(), GoogleService

### Community 59 - "edit_fiscal"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 62 - "typing"
Cohesion: 0.09
Nodes (6): Settings, google_redirects(), google_service(), GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 63 - "Actor"
Cohesion: 0.13
Nodes (9): audit(), cancel_owner(), change_status(), client_options(), edit_client_image(), invite_owner(), new_owner(), remove_client_image() (+1 more)

### Community 64 - "Actor"
Cohesion: 0.17
Nodes (5): assign_sites(), classify(), classify_many(), delete(), unlinked()

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "test_networks.py"
Cohesion: 0.26
Nodes (8): Sent, _owner_invite(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 67 - "sites/controller.py"
Cohesion: 0.19
Nodes (7): site_options(), AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn, ItemsOut

### Community 68 - "reports/controller.py"
Cohesion: 0.11
Nodes (13): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned() (+5 more)

### Community 69 - "Limiter"
Cohesion: 0.08
Nodes (7): TooManyAttempts, Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "avant_core_shared_clock"
Cohesion: 0.08
Nodes (7): SessionCookies, new_verifier(), get_cookies(), google_start(), GoogleStatusOut, verify(), client_info()

### Community 71 - "sqlalchemy"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 72 - "google.py"
Cohesion: 0.11
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 74 - ".show"
Cohesion: 0.16
Nodes (5): connect(), index(), options(), NetworkDetailOut, NetworkService

### Community 75 - "uuid"
Cohesion: 0.19
Nodes (17): _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency(), test_pinned_reports_and_preview_refresh() (+9 more)

### Community 76 - "people/controller.py"
Cohesion: 0.11
Nodes (9): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+1 more)

### Community 77 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 78 - "networks/service.py"
Cohesion: 0.24
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 79 - "costs/service.py"
Cohesion: 0.15
Nodes (4): create(), CostIn, CostOut, _input()

### Community 81 - "require"
Cohesion: 0.11
Nodes (6): require(), dependency(), require_session(), show(), result_service(), ResultService

### Community 82 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 83 - "test_dashboards.py"
Cohesion: 0.32
Nodes (6): _form(), _kpi(), _run(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit()

### Community 84 - "commissions/controller.py"
Cohesion: 0.22
Nodes (6): commission_service(), AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn

### Community 85 - "events.py"
Cohesion: 0.10
Nodes (7): channel(), EventSource, _parse(), sse(), events(), event_service(), EventService

### Community 86 - "company/controller.py"
Cohesion: 0.20
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "AdUnitOut"
Cohesion: 0.21
Nodes (3): ad_units(), link(), AdUnitOut

### Community 91 - "profile/controller.py"
Cohesion: 0.20
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 92 - ".build"
Cohesion: 0.08
Nodes (7): _google(), _mailer(), NoEvents, RedisEvents, MemoryCounter, test_redis_source_delivers_published_messages(), run()

### Community 94 - "ClientOut"
Cohesion: 0.14
Nodes (4): edit_client(), register_client(), ClientOut, image_url()

### Community 95 - "goals/controller.py"
Cohesion: 0.18
Nodes (5): delete_template(), role_goals(), set_role_goal(), update_template(), RoleGoalIn

### Community 96 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 98 - "SiteOut"
Cohesion: 0.13
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 127 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 129 - "contracts/controller.py"
Cohesion: 0.24
Nodes (6): contract_service(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut

### Community 130 - "CommissionService"
Cohesion: 0.18
Nodes (4): _month(), team(), PersonMonthOut, CommissionService

### Community 131 - "test_alerts.py"
Cohesion: 0.25
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 136 - "reports/service.py"
Cohesion: 0.05
Nodes (15): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn (+7 more)

### Community 137 - "SiteListOut"
Cohesion: 0.15
Nodes (3): create(), index(), SiteListOut

### Community 138 - "Actor"
Cohesion: 0.15
Nodes (3): adjust(), delete_rule(), settings()

### Community 139 - "edit_contract"
Cohesion: 0.16
Nodes (5): contract_networks(), edit_contract(), finish_contract(), new_contract(), remove_contract()

### Community 142 - "container.py"
Cohesion: 0.07
Nodes (5): PillowImageProcessor, Bucket, CeleryQueue, RecordingQueue, TaskQueue

### Community 143 - "shared/dto.py"
Cohesion: 0.09
Nodes (4): index(), page_out(), PageOut, RoleRefOut

### Community 144 - "logs.py"
Cohesion: 0.17
Nodes (3): configure_logging(), JsonFormatter, _csv_cell()

### Community 146 - "test_account.py"
Cohesion: 0.40
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 147 - "SiteService"
Cohesion: 0.20
Nodes (4): show(), site_service(), SiteDetailOut, SiteService

### Community 148 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 150 - "to_csv"
Cohesion: 0.27
Nodes (5): _header(), _metric_label(), _rows(), to_csv(), to_xlsx()

### Community 152 - ".page_saved"
Cohesion: 0.22
Nodes (3): index(), ReportCountsOut, ReportPageOut

### Community 161 - "contracts"
Cohesion: 0.17
Nodes (7): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem, metrics(), contracts()

### Community 163 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 164 - "io"
Cohesion: 0.31
Nodes (4): _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 175 - "test_goal_progress_routes"
Cohesion: 0.53
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1475 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **80 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `CommissionService`, `DashboardService`, `AlertService`, `ContractService`, `roles/controller.py`, `reports/service.py`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `container.py`, `shared/dto.py`, `api_keys/controller.py`, `pydantic`, `custom_metrics/controller.py`, `GoalService`, `.__init__`, `costs/controller.py`, `SiteService`, `.__init__`, `clients/controller.py`, `Actor`, `goals/service.py`, `get`, `ClientService`, `invoices/controller.py`, `staff/controller.py`, `CompanyService`, `.__init__`, `.__init__`, `MfaService`, `views/controller.py`, `auth/controller.py`, `avant_core_access_models`, `currencies/controller.py`, `.__init__`, `members/controller.py`, `GoogleService`, `account/controller.py`, `mcm/controller.py`, `sites/controller.py`, `Limiter`, `avant_core_shared_clock`, `.show`, `people/controller.py`, `networks/service.py`, `costs/service.py`, `require`, `commissions/controller.py`, `company/controller.py`, `profile/controller.py`?**
  _High betweenness centrality (0.111) - this node is a cross-community bridge._
- **Are the 93 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 93 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.07869742198100407 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `shared/dto.py` to `contracts/controller.py`, `ContractService`, `DashboardService`, `AlertService`, `roles/controller.py`, `.owner_invitations`, `reports/service.py`, `schedules/controller.py`, `SiteListOut`, `.trusted_uow`, `GroupService`, `sync_runs`, `api_keys/controller.py`, `pydantic`, `SiteService`, `GoalService`, `costs/controller.py`, `.page_saved`, `AuditOut`, `UnitOfWorkFactory`, `get`, `goals/service.py`, `clients/controller.py`, `contracts`, `ClientService`, `invoices/controller.py`, `clients`, `staff/controller.py`, `avant_core_access_models`, `members/controller.py`, `Actor`, `Actor`, `mcm/controller.py`, `sites/controller.py`, `.show`, `people/controller.py`, `networks/service.py`, `costs/service.py`, `goals/controller.py`, `SiteOut`?**
  _High betweenness centrality (0.086) - this node is a cross-community bridge._
- **Are the 47 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 47 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07581453634085213 - nodes in this community are weakly interconnected._