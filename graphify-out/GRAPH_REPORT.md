# Graph Report - avant-api  (2026-11-02)

## Corpus Check
- 232 files · ~74,240 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3138 nodes · 8537 edges · 173 communities (91 shown, 82 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1445 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `029e6a00`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- DashboardService
- AlertService
- security.py
- .save_rule
- conftest.py
- steps
- schedules/controller.py
- Avant: models do MVP
- test_company_image.py
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
- GoalTemplateOut
- invoice_pdf.py
- UnitOfWorkFactory
- clean_code.py
- CapturingMailer
- mfa/controller.py
- Avant: repositório e plano do MVP
- get
- clients/controller.py
- .uow
- session-start.sh
- avant-api
- ClientService
- _member_client
- invoices/controller.py
- export.py
- staff/controller.py
- CompanyService
- main.py
- errors.py
- limits.py
- InvoiceService
- CapturingMailer
- shared/dto.py
- .authenticate
- avant_core_access_models
- Services
- ReportResultOut
- UserOut
- edit
- currencies/controller.py
- members/controller.py
- test_mfa.py
- health/controller.py
- _month
- company/controller.py
- AccountService
- typing
- clients/controller.py
- ItemsOut
- mcm/controller.py
- test_networks.py
- sites/controller.py
- reports/controller.py
- Limiter
- auth/controller.py
- sqlalchemy
- google.py
- avant-api
- account/controller.py
- uuid
- people/controller.py
- Avant: conexão com o GAM
- commissions/dto.py
- test_api.py
- .available_months
- google/controller.py
- mine
- test_dashboards.py
- do_reset_password
- events.py
- FiscalDataIn
- Avant: grupos na Empresa e imagem da Empresa
- SiteService
- SessionCookies
- profile/controller.py
- container.py
- ClientOut
- goals/controller.py
- GoalService
- update_item
- .assign
- people/service.py
- image
- CommissionRuleOut
- mine
- test_alerts.py
- Actor
- image
- Actor
- reports/service.py
- SiteListOut
- CommissionService
- shared/dto.py
- dollars
- templates
- test_account.py
- AdUnitOut
- Actor
- person
- .page_saved
- google/controller.py
- delete_session
- members
- client_image
- new_owner
- delete_template
- .update_service
- manager_change
- .first_day

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 124 edges
2. `PageOut` - 116 edges
3. `_csrf()` - 110 edges
4. `_onboard_owner()` - 110 edges
5. `get()` - 100 edges
6. `Services` - 98 edges
7. `UnitOfWorkFactory` - 97 edges
8. `ReportService` - 75 edges
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

## Communities (173 total, 82 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.10
Nodes (27): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+19 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.05
Nodes (24): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem, metrics(), contract(), contract_networks() (+16 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (20): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+12 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (16): create(), delete(), events(), index(), mute(), preview(), show(), update() (+8 more)

### Community 5 - "security.py"
Cohesion: 0.08
Nodes (18): CsrfFailed, NoActiveCompany, RateLimited, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth() (+10 more)

### Community 6 - ".save_rule"
Cohesion: 0.14
Nodes (6): adjust(), create_rule(), delete_rule(), settings(), update_rule(), CommissionRuleIn

### Community 7 - "conftest.py"
Cohesion: 0.09
Nodes (16): client(), engine(), mailer(), Sent, _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys() (+8 more)

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

### Community 14 - "networks/controller.py"
Cohesion: 0.06
Nodes (16): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+8 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "pydantic"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

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

### Community 23 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "CapturingMailer"
Cohesion: 0.23
Nodes (12): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "get"
Cohesion: 0.09
Nodes (14): add_item(), create_service(), delete(), delete_service(), get(), issue(), mine(), pay() (+6 more)

### Community 31 - "clients/controller.py"
Cohesion: 0.19
Nodes (11): client_service(), ClientDetailOut, ClientIn, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+3 more)

### Community 32 - ".uow"
Cohesion: 0.07
Nodes (4): duplicate(), pinned(), SavedReportOut, ReportService

### Community 36 - "ClientService"
Cohesion: 0.24
Nodes (4): client_teams(), ClientMemberOut, ClientService, CompanyRefOut

### Community 37 - "_member_client"
Cohesion: 0.14
Nodes (13): _membership_ids(), test_groups_lifecycle(), _inventory(), test_manual_site(), test_site_category_and_responsible(), test_sites_and_assignment(), _member_client(), test_audit_log() (+5 more)

### Community 38 - "invoices/controller.py"
Cohesion: 0.21
Nodes (9): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceSummaryOut, ReturnedOut, ReturnIn (+1 more)

### Community 39 - "export.py"
Cohesion: 0.08
Nodes (11): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+3 more)

### Community 40 - "staff/controller.py"
Cohesion: 0.11
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 41 - "CompanyService"
Cohesion: 0.21
Nodes (3): show(), CompanyDetailOut, CompanyService

### Community 42 - "main.py"
Cohesion: 0.10
Nodes (5): configure_logging(), JsonFormatter, observe(), _route_template(), create_app()

### Community 43 - "errors.py"
Cohesion: 0.15
Nodes (8): error_body(), GoogleUnavailable, install(), domain_error(), http_error(), unexpected(), validation_error(), QueryTooHeavy

### Community 44 - "limits.py"
Cohesion: 0.07
Nodes (10): TooManyAttempts, Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise() (+2 more)

### Community 46 - "CapturingMailer"
Cohesion: 0.21
Nodes (10): CapturingMailer, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_option_lists_keep_the_permissions() (+2 more)

### Community 49 - "avant_core_access_models"
Cohesion: 0.05
Nodes (11): results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut (+3 more)

### Community 50 - "Services"
Cohesion: 0.09
Nodes (11): Estrutura, Services, get_services(), TaskQueue, alert_service(), audit_service(), dashboard_service(), google_redirects() (+3 more)

### Community 51 - "ReportResultOut"
Cohesion: 0.16
Nodes (3): query(), ReportQueryIn, ReportResultOut

### Community 52 - "UserOut"
Cohesion: 0.14
Nodes (3): edit_image(), remove_image(), UserOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (16): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+8 more)

### Community 56 - "test_mfa.py"
Cohesion: 0.14
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 57 - "health/controller.py"
Cohesion: 0.15
Nodes (4): health(), ready(), health_service(), HealthService

### Community 59 - "company/controller.py"
Cohesion: 0.16
Nodes (4): edit_image(), fiscal(), remove_image(), company_service()

### Community 60 - "AccountService"
Cohesion: 0.18
Nodes (4): do_change_password(), get_sessions(), revoke_others(), AccountService

### Community 62 - "typing"
Cohesion: 0.12
Nodes (4): Settings, GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 63 - "clients/controller.py"
Cohesion: 0.10
Nodes (8): audit(), cancel_owner(), change_status(), client_options(), clients(), edit_client_image(), remove_client_image(), AuditOut

### Community 64 - "ItemsOut"
Cohesion: 0.14
Nodes (7): classify(), classify_many(), delete(), index(), show(), sites_of_member(), unlinked()

### Community 65 - "mcm/controller.py"
Cohesion: 0.13
Nodes (6): assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService, PageOut

### Community 66 - "test_networks.py"
Cohesion: 0.47
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 67 - "sites/controller.py"
Cohesion: 0.19
Nodes (8): site_service(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "reports/controller.py"
Cohesion: 0.09
Nodes (11): create(), create_from_template(), delete(), export(), export_saved(), pin(), run(), show() (+3 more)

### Community 69 - "Limiter"
Cohesion: 0.14
Nodes (6): Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "auth/controller.py"
Cohesion: 0.14
Nodes (10): get_cookies(), get_invitation(), auth_service(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn (+2 more)

### Community 71 - "sqlalchemy"
Cohesion: 0.18
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 72 - "google.py"
Cohesion: 0.10
Nodes (6): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle

### Community 74 - "account/controller.py"
Cohesion: 0.23
Nodes (6): account_service(), ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut, SessionOut

### Community 75 - "uuid"
Cohesion: 0.17
Nodes (20): _onboard_owner(), _owner_invite(), test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx() (+12 more)

### Community 76 - "people/controller.py"
Cohesion: 0.11
Nodes (7): Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PeopleService

### Community 77 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 78 - "commissions/dto.py"
Cohesion: 0.31
Nodes (6): AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn, PersonMonthOut

### Community 79 - "test_api.py"
Cohesion: 0.33
Nodes (6): test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format()

### Community 81 - "google/controller.py"
Cohesion: 0.06
Nodes (8): GoogleAuth, new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), GoogleStatusOut, GoogleService

### Community 82 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 83 - "test_dashboards.py"
Cohesion: 0.32
Nodes (6): _form(), _kpi(), _run(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit()

### Community 85 - "events.py"
Cohesion: 0.10
Nodes (7): channel(), EventSource, _parse(), sse(), events(), event_service(), EventService

### Community 86 - "FiscalDataIn"
Cohesion: 0.23
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 89 - "SessionCookies"
Cohesion: 0.10
Nodes (8): SessionCookies, accept(), do_logout(), login(), me(), set_active_company(), MeOut, verify()

### Community 91 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 92 - "container.py"
Cohesion: 0.06
Nodes (9): _google(), _mailer(), NoEvents, RedisEvents, PillowImageProcessor, MemoryCounter, CeleryQueue, RecordingQueue (+1 more)

### Community 95 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 96 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 97 - "update_item"
Cohesion: 0.19
Nodes (3): save_payment_details(), update_item(), PayeeDetailsOut

### Community 98 - ".assign"
Cohesion: 0.25
Nodes (5): Atribuição de sites, GAM, Networks, Sites e ad units, assign_sites()

### Community 131 - "test_alerts.py"
Cohesion: 0.25
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 134 - "Actor"
Cohesion: 0.17
Nodes (5): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 136 - "reports/service.py"
Cohesion: 0.05
Nodes (17): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn (+9 more)

### Community 137 - "SiteListOut"
Cohesion: 0.20
Nodes (4): create(), site_options(), SiteListOut, ItemsOut

### Community 139 - "CommissionService"
Cohesion: 0.18
Nodes (3): set_settings(), commission_service(), CommissionService

### Community 143 - "shared/dto.py"
Cohesion: 0.11
Nodes (3): index(), AuditService, page_out()

### Community 146 - "test_account.py"
Cohesion: 0.32
Nodes (8): _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_id_token_claims(), test_login_attempts_are_limited()

### Community 147 - "AdUnitOut"
Cohesion: 0.16
Nodes (3): ad_units(), link(), AdUnitOut

### Community 155 - "google/controller.py"
Cohesion: 0.15
Nodes (3): client_info(), image_response(), image_upload()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1441 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **82 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `reports/service.py`, `schedules/controller.py`, `.__init__`, `CommissionService`, `.trusted_uow`, `GroupService`, `networks/controller.py`, `shared/dto.py`, `api_keys/controller.py`, `pydantic`, `custom_metrics/controller.py`, `.__init__`, `costs/controller.py`, `mfa/controller.py`, `clients/controller.py`, `.uow`, `goals/service.py`, `ClientService`, `.__init__`, `invoices/controller.py`, `staff/controller.py`, `CompanyService`, `.__init__`, `limits.py`, `InvoiceService`, `shared/dto.py`, `avant_core_access_models`, `currencies/controller.py`, `members/controller.py`, `AccountService`, `mcm/controller.py`, `sites/controller.py`, `auth/controller.py`, `account/controller.py`, `people/controller.py`, `commissions/dto.py`, `google/controller.py`, `SiteService`, `profile/controller.py`, `GoalService`, `people/service.py`?**
  _High betweenness centrality (0.137) - this node is a cross-community bridge._
- **Are the 92 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 92 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.10235690235690235 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `mcm/controller.py` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `Actor`, `Actor`, `reports/service.py`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `networks/controller.py`, `shared/dto.py`, `api_keys/controller.py`, `pydantic`, `costs/controller.py`, `GoalTemplateOut`, `.page_saved`, `UnitOfWorkFactory`, `get`, `goals/service.py`, `clients/controller.py`, `ClientService`, `.update_service`, `invoices/controller.py`, `staff/controller.py`, `InvoiceService`, `shared/dto.py`, `avant_core_access_models`, `members/controller.py`, `clients/controller.py`, `ItemsOut`, `sites/controller.py`, `people/controller.py`, `SiteService`, `goals/controller.py`, `GoalService`, `people/service.py`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 47 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 47 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.053297199638663056 - nodes in this community are weakly interconnected._