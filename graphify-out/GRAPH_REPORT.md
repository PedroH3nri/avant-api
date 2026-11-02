# Graph Report - avant-api  (2026-11-02)

## Corpus Check
- 238 files · ~75,407 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3210 nodes · 8727 edges · 174 communities (91 shown, 83 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1477 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d26dde3e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- DashboardService
- AlertService
- security.py
- commissions/controller.py
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
- AuthService
- avant_core_access_models
- Services
- .of
- UserOut
- edit
- currencies/controller.py
- members/controller.py
- test_mfa.py
- health/controller.py
- google/controller.py
- edit_fiscal
- account/controller.py
- ReportService
- typing
- Actor
- ItemsOut
- mcm/controller.py
- test_networks.py
- sites/controller.py
- reports/controller.py
- Limiter
- avant_core_shared_clock
- sqlalchemy
- google.py
- avant-api
- uuid
- people/controller.py
- Avant: conexão com o GAM
- networks/service.py
- .classify
- dollars
- google_callback
- mine
- test_dashboards.py
- GoogleAuth
- events.py
- company/controller.py
- Avant: grupos na Empresa e imagem da Empresa
- SiteService
- SessionCookies
- profile/controller.py
- .build
- ClientOut
- goals/controller.py
- GoalService
- update_item
- .assign
- people/service.py
- image
- MemoryCounter
- update_preferences
- test_alerts.py
- Actor
- image
- .owner_invitations
- reports/service.py
- SiteListOut
- TaskQueue
- shared/dto.py
- .show
- templates
- test_account.py
- Actor
- FakeGoogle
- .page_saved
- AuditOut
- google/controller.py
- members
- is_exempt
- new_owner
- delete_template
- .update_service
- create

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
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py
- `Pipeline` --references--> `main()`  [INFERRED]
  docs/decisoes/07-repositorios-e-plano.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (174 total, 83 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.09
Nodes (30): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+22 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (21): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+13 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "security.py"
Cohesion: 0.06
Nodes (19): EventSource, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor(), get_session_auth() (+11 more)

### Community 6 - "commissions/controller.py"
Cohesion: 0.05
Nodes (22): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+14 more)

### Community 7 - "conftest.py"
Cohesion: 0.09
Nodes (15): client(), engine(), mailer(), Sent, _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys() (+7 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "test_company_image.py"
Cohesion: 0.16
Nodes (5): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), _png()

### Community 12 - ".trusted_uow"
Cohesion: 0.12
Nodes (5): add_item(), pay(), update_item(), InvoiceOut, InvoiceService

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "networks/controller.py"
Cohesion: 0.15
Nodes (11): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+3 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "pydantic"
Cohesion: 0.09
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

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
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 23 - "GoalTemplateOut"
Cohesion: 0.14
Nodes (4): create_template(), template_options(), GoalTemplateIn, GoalTemplateOut

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 27 - "CapturingMailer"
Cohesion: 0.23
Nodes (12): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "get"
Cohesion: 0.10
Nodes (11): available_months(), delete(), delete_service(), get(), mine(), payment_details(), pdf(), remove_item() (+3 more)

### Community 31 - "clients/controller.py"
Cohesion: 0.24
Nodes (9): ClientIn, ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn, ManagerChangeOut, OwnerChangeIn (+1 more)

### Community 36 - "ClientService"
Cohesion: 0.21
Nodes (5): client_teams(), client_service(), ClientMemberOut, ClientService, CompanyRefOut

### Community 37 - "_member_client"
Cohesion: 0.14
Nodes (13): _membership_ids(), test_groups_lifecycle(), _inventory(), test_manual_site(), test_site_category_and_responsible(), test_sites_and_assignment(), _member_client(), test_audit_log() (+5 more)

### Community 38 - "invoices/controller.py"
Cohesion: 0.18
Nodes (10): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn (+2 more)

### Community 39 - "export.py"
Cohesion: 0.07
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 40 - "staff/controller.py"
Cohesion: 0.11
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 41 - "CompanyService"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 43 - "errors.py"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "limits.py"
Cohesion: 0.08
Nodes (8): BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 46 - "_onboard_owner"
Cohesion: 0.16
Nodes (19): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format() (+11 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "AuthService"
Cohesion: 0.09
Nodes (4): get_invitation(), auth_service(), InvitationPreviewOut, AuthService

### Community 49 - "avant_core_access_models"
Cohesion: 0.05
Nodes (11): results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut (+3 more)

### Community 50 - "Services"
Cohesion: 0.05
Nodes (10): Services, NoEvents, PillowImageProcessor, get_services(), create_app(), company_service(), cost_service(), commission_service() (+2 more)

### Community 52 - "UserOut"
Cohesion: 0.18
Nodes (4): edit_image(), remove_image(), ProfileService, UserOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.20
Nodes (5): list_currencies(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (16): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+8 more)

### Community 56 - "test_mfa.py"
Cohesion: 0.18
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 57 - "health/controller.py"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 58 - "google/controller.py"
Cohesion: 0.09
Nodes (9): CsrfFailed, GoogleUnavailable, NoActiveCompany, QueryTooHeavy, google_status(), google_unlink(), google_redirects(), google_service() (+1 more)

### Community 59 - "edit_fiscal"
Cohesion: 0.29
Nodes (3): edit_fiscal(), edit_image(), fiscal()

### Community 60 - "account/controller.py"
Cohesion: 0.10
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "ReportService"
Cohesion: 0.11
Nodes (7): Bucket, create(), pinned(), update(), SavedReportIn, SavedReportOut, ReportService

### Community 62 - "typing"
Cohesion: 0.09
Nodes (5): Settings, GoogleStatusOut, GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 63 - "Actor"
Cohesion: 0.11
Nodes (10): audit(), cancel_owner(), change_status(), client_image(), client_options(), edit_client_image(), invite_owner(), register_client() (+2 more)

### Community 64 - "ItemsOut"
Cohesion: 0.13
Nodes (8): ad_units(), assign_sites(), delete(), index(), show(), site_options(), sites_of_member(), ItemsOut

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "test_networks.py"
Cohesion: 0.47
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 67 - "sites/controller.py"
Cohesion: 0.19
Nodes (8): site_service(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "reports/controller.py"
Cohesion: 0.11
Nodes (12): create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), query(), run() (+4 more)

### Community 69 - "Limiter"
Cohesion: 0.11
Nodes (7): TooManyAttempts, Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "avant_core_shared_clock"
Cohesion: 0.13
Nodes (5): AcceptInvitationIn, ActiveCompanyIn, CompanyOut, LoginIn, LoginOut

### Community 71 - "sqlalchemy"
Cohesion: 0.15
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 72 - "google.py"
Cohesion: 0.12
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), _jwt(), test_id_token_claims()

### Community 75 - "uuid"
Cohesion: 0.14
Nodes (18): CapturingMailer, _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+10 more)

### Community 76 - "people/controller.py"
Cohesion: 0.18
Nodes (5): disable(), enable(), reset_mfa(), people_service(), PeopleService

### Community 77 - "Avant: conexão com o GAM"
Cohesion: 0.17
Nodes (10): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+2 more)

### Community 78 - "networks/service.py"
Cohesion: 0.18
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 82 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 83 - "test_dashboards.py"
Cohesion: 0.32
Nodes (6): _form(), _kpi(), _run(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit()

### Community 85 - "events.py"
Cohesion: 0.14
Nodes (5): channel(), _parse(), sse(), configure_logging(), JsonFormatter

### Community 86 - "company/controller.py"
Cohesion: 0.32
Nodes (3): CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "SiteService"
Cohesion: 0.14
Nodes (4): link(), unlinked(), AdUnitOut, SiteService

### Community 89 - "SessionCookies"
Cohesion: 0.11
Nodes (9): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), login(), me(), set_active_company() (+1 more)

### Community 91 - "profile/controller.py"
Cohesion: 0.24
Nodes (3): edit_appearance(), AppearanceIn, AppearanceOut

### Community 92 - ".build"
Cohesion: 0.15
Nodes (6): _google(), _mailer(), RedisEvents, CeleryQueue, test_redis_source_delivers_published_messages(), run()

### Community 94 - "ClientOut"
Cohesion: 0.10
Nodes (4): clients(), edit_client(), ClientOut, image_url()

### Community 95 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 96 - "GoalService"
Cohesion: 0.23
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 98 - ".assign"
Cohesion: 0.40
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 131 - "test_alerts.py"
Cohesion: 0.35
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 136 - "reports/service.py"
Cohesion: 0.07
Nodes (14): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn (+6 more)

### Community 142 - "TaskQueue"
Cohesion: 0.08
Nodes (8): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, RecordingQueue, TaskQueue, enqueue_sync()

### Community 143 - "shared/dto.py"
Cohesion: 0.09
Nodes (5): index(), audit_service(), AuditService, page_out(), PageOut

### Community 146 - "test_account.py"
Cohesion: 0.40
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 148 - "Actor"
Cohesion: 0.22
Nodes (3): role_goals(), templates(), RoleGoalOut

### Community 155 - "google/controller.py"
Cohesion: 0.16
Nodes (3): client_info(), image_response(), image_upload()

### Community 165 - ".update_service"
Cohesion: 0.22
Nodes (4): create_service(), update_service(), InvoiceServiceIn, InvoiceServiceOut

### Community 171 - "create"
Cohesion: 0.29
Nodes (3): create(), issue(), return_to_draft()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1473 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **83 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `commissions/controller.py`, `reports/service.py`, `schedules/controller.py`, `.__init__`, `.trusted_uow`, `GroupService`, `TaskQueue`, `shared/dto.py`, `api_keys/controller.py`, `pydantic`, `networks/controller.py`, `custom_metrics/controller.py`, `.__init__`, `costs/controller.py`, `mfa/controller.py`, `.__init__`, `clients/controller.py`, `goals/service.py`, `.__init__`, `ClientService`, `invoices/controller.py`, `.__init__`, `staff/controller.py`, `CompanyService`, `.__init__`, `.__init__`, `.__init__`, `views/controller.py`, `AuthService`, `avant_core_access_models`, `UserOut`, `currencies/controller.py`, `members/controller.py`, `google/controller.py`, `account/controller.py`, `ReportService`, `mcm/controller.py`, `sites/controller.py`, `avant_core_shared_clock`, `people/controller.py`, `networks/service.py`, `GoogleAuth`, `company/controller.py`, `SiteService`, `profile/controller.py`, `GoalService`, `people/service.py`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **Are the 93 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 93 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.0898995240613432 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `shared/dto.py` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `Actor`, `.owner_invitations`, `reports/service.py`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `networks/controller.py`, `api_keys/controller.py`, `pydantic`, `Actor`, `costs/controller.py`, `GoalTemplateOut`, `.page_saved`, `get`, `goals/service.py`, `clients/controller.py`, `ClientService`, `.update_service`, `invoices/controller.py`, `staff/controller.py`, `avant_core_access_models`, `members/controller.py`, `Actor`, `ItemsOut`, `mcm/controller.py`, `sites/controller.py`, `.show`, `people/controller.py`, `Avant: conexão com o GAM`, `networks/service.py`, `SiteService`, `ClientOut`, `goals/controller.py`, `GoalService`, `people/service.py`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Are the 47 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 47 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06832298136645963 - nodes in this community are weakly interconnected._