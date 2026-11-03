# Graph Report - avant-api  (2026-11-03)

## Corpus Check
- 273 files · ~82,107 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3610 nodes · 9803 edges · 197 communities (101 shown, 96 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1634 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `45cd9202`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- DashboardService
- AlertService
- require_staff
- .save_rule
- test_api_keys.py
- steps
- schedules/controller.py
- Avant: models do MVP
- test_company_image.py
- .trusted_uow
- GroupService
- inventory/controller.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- pydantic
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- security.py
- dashboard_templates/controller.py
- invoice_pdf.py
- PageOut
- clean_code.py
- CapturingMailer
- mfa/controller.py
- Avant: repositório e plano do MVP
- InvoiceService
- clients/controller.py
- ReportResultOut
- session-start.sh
- avant-api
- shared/dto.py
- BaseModel
- invoices/controller.py
- export.py
- ItemsOut
- CompanyService
- AuthService
- install
- MemoryBucket
- commissions/dto.py
- _onboard_owner
- views/controller.py
- Settings
- avant_core_access_models
- client_notes/controller.py
- TaskQueue
- ProfileService
- edit
- currencies/controller.py
- members/controller.py
- conftest.py
- goals/controller.py
- GoogleService
- edit_image
- AccountService
- SupportTaskService
- health/controller.py
- Actor
- sites/controller.py
- mcm/controller.py
- CapturingMailer
- sites/service.py
- documents/controller.py
- Limiter
- UnitOfWorkFactory
- sqlalchemy
- google.py
- avant-api
- networks/controller.py
- uuid
- people/controller.py
- Avant: conexão com o GAM
- GoalService
- costs/controller.py
- _month
- CommissionService
- test_dashboards.py
- .update_service
- test_events.py
- download
- Avant: grupos na Empresa e imagem da Empresa
- tasks/controller.py
- test_members_without_schedules_manage_only_see_what_they_receive
- UUID
- Actor
- GoalTemplateOut
- .of
- update_item
- TaskDetailOut
- MonthIn
- tasks/dto.py
- do_reset_password
- test_alerts.py
- ClientService
- mine
- account/dto.py
- Counter
- reports/service.py
- SiteService
- person
- Services
- company/controller.py
- test_contract_crud
- networks/service.py
- test_account.py
- .of
- delete_template
- Actor
- TaskPatchIn
- ItemsOut
- members
- test_staff_opens_assigns_and_comments_on_tasks
- google/dto.py
- google_status
- download
- google_start
- .build
- clients
- middleware.py
- QueryTooHeavy
- owner_invitation_out
- document_response
- enqueue_sync
- logs.py
- MemoryCounter
- events/controller.py
- test_staff_sees_client_networks_sites_and_revenue_status
- RedisEvents
- images.py
- test_goal_progress_routes
- FakeGoogle

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 138 edges
2. `PageOut` - 133 edges
3. `_csrf()` - 123 edges
4. `_onboard_owner()` - 123 edges
5. `UnitOfWorkFactory` - 118 edges
6. `get()` - 114 edges
7. `Services` - 112 edges
8. `ReportService` - 75 edges
9. `InvoiceService` - 58 edges
10. `_staff()` - 56 edges

## Surprising Connections (you probably didn't know these)
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/modules/internal/people/controller.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py
- `Pipeline` --references--> `main()`  [INFERRED]
  docs/decisoes/07-repositorios-e-plano.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (197 total, 96 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.08
Nodes (33): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+25 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.05
Nodes (25): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+17 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.09
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (22): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+14 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "require_staff"
Cohesion: 0.22
Nodes (4): require(), dependency(), require_session(), require_staff()

### Community 6 - ".save_rule"
Cohesion: 0.17
Nodes (4): create_rule(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 7 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (22): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+14 more)

### Community 11 - "test_company_image.py"
Cohesion: 0.08
Nodes (20): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person() (+12 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/controller.py"
Cohesion: 0.09
Nodes (6): networks(), sites(), ClientNetworkOut, ClientRefOut, ClientSiteOut, ClientInventoryService

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
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "security.py"
Cohesion: 0.06
Nodes (13): SessionCookies, get_auth(), get_cookies(), get_session_auth(), require_staff_member(), account_service(), auth_service(), google_redirects() (+5 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "PageOut"
Cohesion: 0.10
Nodes (6): index(), AuditService, audit(), owner_invitations(), AuditOut, PageOut

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "CapturingMailer"
Cohesion: 0.22
Nodes (12): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "InvoiceService"
Cohesion: 0.17
Nodes (3): service_options(), invoice_service(), InvoiceService

### Community 31 - "clients/controller.py"
Cohesion: 0.14
Nodes (14): edit_client(), client_service(), ClientDetailOut, ClientIn, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn (+6 more)

### Community 32 - "ReportResultOut"
Cohesion: 0.08
Nodes (11): create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), query(), run() (+3 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - "invoices/controller.py"
Cohesion: 0.19
Nodes (11): create_service(), services(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceServiceOut, InvoiceSummaryOut (+3 more)

### Community 39 - "export.py"
Cohesion: 0.08
Nodes (11): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+3 more)

### Community 40 - "ItemsOut"
Cohesion: 0.11
Nodes (7): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, ItemsOut

### Community 41 - "CompanyService"
Cohesion: 0.17
Nodes (4): show(), CompanyDetailOut, CompanyPatchIn, CompanyService

### Community 42 - "AuthService"
Cohesion: 0.06
Nodes (16): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), AcceptInvitationIn (+8 more)

### Community 43 - "install"
Cohesion: 0.20
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "MemoryBucket"
Cohesion: 0.09
Nodes (8): TooManyAttempts, BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 45 - "commissions/dto.py"
Cohesion: 0.18
Nodes (3): CommissionMonthOut, CommissionSettingsIn, dollars()

### Community 46 - "_onboard_owner"
Cohesion: 0.22
Nodes (14): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format() (+6 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "Settings"
Cohesion: 0.07
Nodes (5): Settings, google_callback(), GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 49 - "avant_core_access_models"
Cohesion: 0.05
Nodes (11): results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut (+3 more)

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 52 - "ProfileService"
Cohesion: 0.07
Nodes (7): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.15
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.08
Nodes (13): edit(), index(), leave(), options(), remove(), set_permissions(), show(), MemberDetailOut (+5 more)

### Community 56 - "conftest.py"
Cohesion: 0.10
Nodes (8): client(), engine(), mailer(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 57 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 58 - "GoogleService"
Cohesion: 0.11
Nodes (3): GoogleUnavailable, GoogleAuth, GoogleService

### Community 59 - "edit_image"
Cohesion: 0.16
Nodes (4): edit_image(), fiscal(), image(), remove_image()

### Community 60 - "AccountService"
Cohesion: 0.14
Nodes (5): do_change_password(), get_sessions(), revoke_others(), SessionOut, AccountService

### Community 61 - "SupportTaskService"
Cohesion: 0.15
Nodes (4): tasks(), support_task_service(), TaskOut, SupportTaskService

### Community 62 - "health/controller.py"
Cohesion: 0.17
Nodes (3): ready(), health_service(), HealthService

### Community 63 - "Actor"
Cohesion: 0.09
Nodes (12): cancel_owner(), change_status(), client(), client_image(), client_options(), edit_client_image(), invite_owner(), manager_change() (+4 more)

### Community 64 - "sites/controller.py"
Cohesion: 0.10
Nodes (10): ad_units(), assign_sites(), classify(), classify_many(), create(), delete(), index(), sites_of_member() (+2 more)

### Community 65 - "mcm/controller.py"
Cohesion: 0.11
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "CapturingMailer"
Cohesion: 0.17
Nodes (11): CapturingMailer, Sent, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten() (+3 more)

### Community 67 - "sites/service.py"
Cohesion: 0.13
Nodes (7): link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 68 - "documents/controller.py"
Cohesion: 0.14
Nodes (4): document_service(), document_upload(), DocumentOut, DocumentsOut

### Community 69 - "Limiter"
Cohesion: 0.21
Nodes (5): Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "sqlalchemy"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 72 - "google.py"
Cohesion: 0.13
Nodes (7): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 74 - "networks/controller.py"
Cohesion: 0.16
Nodes (11): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+3 more)

### Community 75 - "uuid"
Cohesion: 0.24
Nodes (15): test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+7 more)

### Community 76 - "people/controller.py"
Cohesion: 0.10
Nodes (9): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+1 more)

### Community 77 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 78 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 79 - "costs/controller.py"
Cohesion: 0.09
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 81 - "CommissionService"
Cohesion: 0.24
Nodes (3): set_settings(), CommissionSettingsOut, CommissionService

### Community 83 - "test_dashboards.py"
Cohesion: 0.17
Nodes (8): _form(), _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit()

### Community 85 - "test_events.py"
Cohesion: 0.14
Nodes (9): channel(), _parse(), sse(), _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit() (+1 more)

### Community 86 - "download"
Cohesion: 0.12
Nodes (4): documents(), download(), upload(), DocumentService

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "tasks/controller.py"
Cohesion: 0.22
Nodes (4): change(), comment(), create(), task()

### Community 89 - "test_members_without_schedules_manage_only_see_what_they_receive"
Cohesion: 0.38
Nodes (3): _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 91 - "UUID"
Cohesion: 0.09
Nodes (14): add_item(), available_months(), create(), delete(), delete_service(), get(), issue(), mine() (+6 more)

### Community 95 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 96 - ".of"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 97 - "update_item"
Cohesion: 0.19
Nodes (3): save_payment_details(), update_item(), PayeeDetailsOut

### Community 130 - "do_reset_password"
Cohesion: 0.18
Nodes (3): delete_session(), do_reset_password(), forgot_password()

### Community 131 - "test_alerts.py"
Cohesion: 0.35
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 132 - "ClientService"
Cohesion: 0.10
Nodes (4): client_teams(), ClientMemberOut, ClientService, CompanyRefOut

### Community 134 - "account/dto.py"
Cohesion: 0.31
Nodes (4): ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut

### Community 136 - "reports/service.py"
Cohesion: 0.05
Nodes (29): Bucket, alert_service(), catalog(), create(), pinned(), templates(), update(), report_service() (+21 more)

### Community 137 - "SiteService"
Cohesion: 0.08
Nodes (10): Atribuição de sites, GAM, Networks, Sites e ad units, show(), site_options(), SiteDetailOut, SiteListOut (+2 more)

### Community 142 - "Services"
Cohesion: 0.04
Nodes (21): Services, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_services() (+13 more)

### Community 143 - "company/controller.py"
Cohesion: 0.14
Nodes (3): edit_fiscal(), CompanyFiscalOut, FiscalDataIn

### Community 144 - "test_contract_crud"
Cohesion: 0.38
Nodes (3): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission()

### Community 146 - "test_account.py"
Cohesion: 0.40
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 158 - "ItemsOut"
Cohesion: 0.19
Nodes (5): adjust(), delete_rule(), person(), rules(), settings()

### Community 164 - "download"
Cohesion: 0.16
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 166 - ".build"
Cohesion: 0.06
Nodes (8): _google(), _mailer(), NoEvents, RedisCounter, CeleryQueue, RecordingQueue, create_app(), health()

### Community 184 - "events/controller.py"
Cohesion: 0.15
Nodes (4): EventSource, events(), event_service(), EventService

### Community 185 - "test_staff_sees_client_networks_sites_and_revenue_status"
Cohesion: 0.38
Nodes (3): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 188 - "RedisEvents"
Cohesion: 0.47
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 190 - "test_goal_progress_routes"
Cohesion: 0.43
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1659 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **96 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `tasks/dto.py`, `.__init__`, `contracts/controller.py`, `DashboardService`, `AlertService`, `ClientService`, `roles/controller.py`, `reports/service.py`, `schedules/controller.py`, `person`, `goals/service.py`, `.trusted_uow`, `GroupService`, `inventory/controller.py`, `SiteService`, `api_keys/controller.py`, `pydantic`, `custom_metrics/controller.py`, `.__init__`, `dashboard_templates/controller.py`, `PageOut`, `mfa/controller.py`, `InvoiceService`, `clients/controller.py`, `shared/dto.py`, `download`, `invoices/controller.py`, `.__init__`, `CompanyService`, `AuthService`, `ItemsOut`, `.__init__`, `views/controller.py`, `.__init__`, `avant_core_access_models`, `client_notes/controller.py`, `.__init__`, `ProfileService`, `TaskQueue`, `currencies/controller.py`, `members/controller.py`, `GoogleService`, `AccountService`, `SupportTaskService`, `mcm/controller.py`, `.__init__`, `sites/service.py`, `documents/controller.py`, `networks/controller.py`, `people/controller.py`, `GoalService`, `costs/controller.py`, `CommissionService`, `download`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 101 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 101 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.0819252432155658 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `tasks/dto.py`, `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `ClientService`, `reports/service.py`, `schedules/controller.py`, `SiteService`, `goals/service.py`, `.trusted_uow`, `GroupService`, `inventory/controller.py`, `api_keys/controller.py`, `pydantic`, `.show`, `InvoiceService`, `clients/controller.py`, `shared/dto.py`, `invoices/controller.py`, `clients`, `ItemsOut`, `avant_core_access_models`, `client_notes/controller.py`, `members/controller.py`, `goals/controller.py`, `SupportTaskService`, `sites/controller.py`, `mcm/controller.py`, `sites/service.py`, `UnitOfWorkFactory`, `networks/controller.py`, `people/controller.py`, `GoalService`, `costs/controller.py`, `tasks/controller.py`, `UUID`, `GoalTemplateOut`?**
  _High betweenness centrality (0.089) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05443037974683544 - nodes in this community are weakly interconnected._