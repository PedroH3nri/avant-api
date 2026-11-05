# Graph Report - avant-api  (2026-11-05)

## Corpus Check
- 297 files · ~91,741 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4033 nodes · 11088 edges · 200 communities (108 shown, 92 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1849 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2218ab20`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- conftest.py
- test_alerts.py
- roles/controller.py
- DashboardService
- Actor
- UnitOfWorkFactory
- test_account.py
- GamToolService
- steps
- _month
- Avant: models do MVP
- test_gam_tools.py
- InvoiceService
- .uow
- shared/dto.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- invitations/controller.py
- clients/controller.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- install
- goals/controller.py
- verify
- image
- clean_code.py
- _onboard_owner
- confirm
- Avant: repositório e plano do MVP
- reports/service.py
- invoices/controller.py
- Actor
- session-start.sh
- avant-api
- security.py
- BaseModel
- .save_rule
- CommissionService
- test_company_image.py
- documents/controller.py
- test_networks.py
- checklists/controller.py
- security.py
- uuid
- networks/service.py
- SiteChecklistService
- download
- Services
- commissions/dto.py
- get
- edit
- currencies/controller.py
- members/controller.py
- contracts/controller.py
- clients
- OwnerInvitationOut
- _onboard_owner
- account/controller.py
- networks/controller.py
- .approve
- commissions/controller.py
- main.py
- limits.py
- Actor
- ItemsOut
- export.py
- limits.py
- .of
- GoalService
- events.py
- avant-api
- NetworkDetailOut
- CompanyService
- BaseModel
- profile/controller.py
- image
- download
- people/controller.py
- test_events.py
- uuid
- InvoiceService
- avant_core_access_models
- _marketing_client
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- Counter
- SiteListOut
- test_api_keys.py
- google/controller.py
- invoices/service.py
- _csrf
- SiteOut
- AdUnitOut
- tasks/controller.py
- connect
- updates
- TaskDetailOut
- TooManyAttempts
- image
- image_response
- edit_image
- ClientService
- UserOut
- users
- mine
- tasks/dto.py
- person
- Arquitetura do MVP do Avant
- test_mfa.py
- AuditOut
- templates
- alerts/dependencies.py
- new_owner
- SiteService
- reports/controller.py
- clients
- test_staff_manage_templates_and_clients_see_them_by_role
- audit/controller.py
- capped
- company/controller.py
- edit_client
- mcm/service.py
- .change_password
- .build
- .available_months
- _member_client
- SiteDetailOut
- create
- Actor
- EventService
- _month
- TaskPatchIn
- .uow
- main.py
- TaskQueue
- ReportService
- .payee_details

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 164 edges
2. `_csrf()` - 147 edges
3. `_onboard_owner()` - 147 edges
4. `PageOut` - 145 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 118 edges
8. `ReportService` - 79 edges
9. `_staff()` - 65 edges
10. `page_out()` - 59 edges

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

## Communities (200 total, 92 thin omitted)

### Community 0 - "conftest.py"
Cohesion: 0.08
Nodes (8): engine(), refresh_levels(), test_deployed_cookies_use_the_host_prefix(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 1 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.08
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "UnitOfWorkFactory"
Cohesion: 0.05
Nodes (9): UnitOfWorkFactory, invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, mfa_service() (+1 more)

### Community 6 - "test_account.py"
Cohesion: 0.05
Nodes (13): CompanyChanged, CsrfFailed, GoogleFailed, NoActiveCompany, QueryTooHeavy, challenge(), _claims(), GoogleAuth (+5 more)

### Community 7 - "GamToolService"
Cohesion: 0.05
Nodes (19): ads_txt(), install(), network(), networks(), run(), runs(), start(), gam_tool_service() (+11 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (22): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+14 more)

### Community 11 - "test_gam_tools.py"
Cohesion: 0.21
Nodes (6): _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _agent(), test_staff_opens_assigns_and_comments_on_tasks()

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "shared/dto.py"
Cohesion: 0.08
Nodes (11): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService (+3 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.11
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "invitations/controller.py"
Cohesion: 0.09
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "clients/controller.py"
Cohesion: 0.17
Nodes (11): client_service(), ClientDetailOut, ClientIn, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+3 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (11): check(), create(), delete(), index(), update(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn (+3 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "install"
Cohesion: 0.25
Nodes (7): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.15
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "_onboard_owner"
Cohesion: 0.09
Nodes (21): CapturingMailer, client(), mailer(), _checkouts(), test_report_requests_use_few_connections(), query(), test_busy_export_answers_503_with_retry_after(), _day() (+13 more)

### Community 28 - "confirm"
Cohesion: 0.17
Nodes (7): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "reports/service.py"
Cohesion: 0.05
Nodes (16): CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn, PreviewPointOut (+8 more)

### Community 31 - "invoices/controller.py"
Cohesion: 0.12
Nodes (13): add_item(), create(), delete(), delete_service(), issue(), pay(), pdf(), remove_item() (+5 more)

### Community 32 - "Actor"
Cohesion: 0.13
Nodes (8): cancel_owner(), change_status(), client(), client_image(), client_options(), edit_client_image(), manager_change(), remove_client_image()

### Community 36 - "security.py"
Cohesion: 0.08
Nodes (16): api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor(), get_auth(), get_session_actor(), get_session_auth() (+8 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - ".save_rule"
Cohesion: 0.12
Nodes (7): adjust(), create_rule(), delete_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 39 - "CommissionService"
Cohesion: 0.16
Nodes (4): set_settings(), settings(), CommissionSettingsOut, CommissionService

### Community 41 - "test_company_image.py"
Cohesion: 0.10
Nodes (13): _check_jpeg_size(), PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image() (+5 more)

### Community 42 - "documents/controller.py"
Cohesion: 0.12
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "test_networks.py"
Cohesion: 0.26
Nodes (8): Sent, _owner_invite(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 44 - "checklists/controller.py"
Cohesion: 0.17
Nodes (10): site_checklist_service(), ChecklistDetailOut, ChecklistMarkIn, ChecklistMonthOut, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut (+2 more)

### Community 45 - "security.py"
Cohesion: 0.06
Nodes (11): Services, NoEvents, Bucket, get_services(), custom_metric_service(), event_service(), client_document_service(), goal_service() (+3 more)

### Community 46 - "uuid"
Cohesion: 0.23
Nodes (16): to_csv(), test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused() (+8 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 49 - "download"
Cohesion: 0.17
Nodes (4): documents(), download(), upload(), document_response()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "commissions/dto.py"
Cohesion: 0.24
Nodes (3): CommissionMonthOut, CommissionSettingsIn, dollars()

### Community 52 - "get"
Cohesion: 0.14
Nodes (5): metrics(), get(), mine(), team(), InvoiceSummaryOut

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "OwnerInvitationOut"
Cohesion: 0.17
Nodes (5): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 59 - "_onboard_owner"
Cohesion: 0.15
Nodes (25): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited(), _onboard_owner() (+17 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "networks/controller.py"
Cohesion: 0.17
Nodes (6): sync_runs(), network_service(), NetworkIn, ServiceAccountOut, SyncRunOut, NetworkService

### Community 63 - "commissions/controller.py"
Cohesion: 0.19
Nodes (3): commission_service(), AdjustmentIn, MonthIn

### Community 64 - "main.py"
Cohesion: 0.15
Nodes (4): health(), ready(), health_service(), HealthService

### Community 65 - "limits.py"
Cohesion: 0.07
Nodes (11): BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket() (+3 more)

### Community 66 - "Actor"
Cohesion: 0.11
Nodes (8): add_note(), check(), checklist(), checklists(), delete_note(), edit_note(), months(), summary()

### Community 67 - "ItemsOut"
Cohesion: 0.19
Nodes (6): site_service(), AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 68 - "export.py"
Cohesion: 0.07
Nodes (11): JsonFormatter, dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_xlsx(), _xlsx_cell() (+3 more)

### Community 69 - "limits.py"
Cohesion: 0.14
Nodes (7): Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "GoalService"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+10 more)

### Community 72 - "events.py"
Cohesion: 0.13
Nodes (4): ExportsBusy, channel(), _parse(), sse()

### Community 74 - "NetworkDetailOut"
Cohesion: 0.14
Nodes (3): index(), options(), NetworkDetailOut

### Community 76 - "CompanyService"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 78 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "download"
Cohesion: 0.15
Nodes (7): approve(), documents(), download(), reject(), ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 81 - "people/controller.py"
Cohesion: 0.09
Nodes (10): require_staff(), dependency(), disable(), enable(), reset_mfa(), users(), people_service(), PersonOut (+2 more)

### Community 82 - "test_events.py"
Cohesion: 0.28
Nodes (10): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports(), test_redis_source_delivers_published_messages() (+2 more)

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - "InvoiceService"
Cohesion: 0.16
Nodes (6): create_service(), services(), invoice_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 85 - "avant_core_access_models"
Cohesion: 0.05
Nodes (10): results(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut (+2 more)

### Community 86 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.04
Nodes (21): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), get_invitation(), login(), me() (+13 more)

### Community 91 - "SiteListOut"
Cohesion: 0.18
Nodes (3): index(), site_options(), SiteListOut

### Community 92 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 94 - "google/controller.py"
Cohesion: 0.06
Nodes (11): GoogleUnavailable, new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), google_redirects(), google_service() (+3 more)

### Community 95 - "invoices/service.py"
Cohesion: 0.12
Nodes (7): service_options(), InvoiceItemOut, InvoiceServiceOptionOut, PayeeDetailsOut, ReturnedOut, ServiceItemIn, FiscalDataOut

### Community 96 - "_csrf"
Cohesion: 0.06
Nodes (42): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+34 more)

### Community 97 - "SiteOut"
Cohesion: 0.13
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 98 - "AdUnitOut"
Cohesion: 0.21
Nodes (3): ad_units(), link(), AdUnitOut

### Community 102 - "tasks/controller.py"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 123 - "connect"
Cohesion: 0.21
Nodes (5): connect(), disconnect(), service_account(), show(), sync()

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "TaskDetailOut"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 129 - "TooManyAttempts"
Cohesion: 0.27
Nodes (3): TooManyAttempts, StreamLimiter, test_stream_limiter_caps_each_person_and_the_process()

### Community 133 - "ClientService"
Cohesion: 0.24
Nodes (4): client_teams(), ClientMemberOut, ClientService, CompanyRefOut

### Community 134 - "UserOut"
Cohesion: 0.14
Nodes (3): edit_image(), remove_image(), UserOut

### Community 135 - "users"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 138 - "tasks/dto.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.38
Nodes (11): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+3 more)

### Community 149 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 150 - "reports/controller.py"
Cohesion: 0.07
Nodes (13): catalog(), create_from_template(), delete(), export(), export_saved(), index(), pin(), query() (+5 more)

### Community 153 - "test_staff_manage_templates_and_clients_see_them_by_role"
Cohesion: 0.38
Nodes (3): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company()

### Community 155 - "audit/controller.py"
Cohesion: 0.13
Nodes (3): index(), audit_service(), AuditService

### Community 160 - "company/controller.py"
Cohesion: 0.16
Nodes (5): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 163 - "mcm/service.py"
Cohesion: 0.11
Nodes (6): assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 175 - "_member_client"
Cohesion: 0.11
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 180 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), classify(), classify_many(), delete(), show(), unlinked()

### Community 184 - "EventService"
Cohesion: 0.16
Nodes (3): EventSource, events(), EventService

### Community 185 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 189 - "main.py"
Cohesion: 0.04
Nodes (16): engine_options(), _google(), _mailer(), configure_logging(), observe(), _route_template(), Settings, CeleryQueue (+8 more)

### Community 191 - "TaskQueue"
Cohesion: 0.09
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskQueue, enqueue_sync()

### Community 195 - "ReportService"
Cohesion: 0.05
Nodes (9): RateLimited, create(), duplicate(), pinned(), update(), SavedReportIn, SavedReportOut, export_slot() (+1 more)

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1836 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **92 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `TaskDetailOut`, `roles/controller.py`, `DashboardService`, `Actor`, `ClientService`, `test_account.py`, `GamToolService`, `_month`, `tasks/dto.py`, `InvoiceService`, `.uow`, `shared/dto.py`, `api_keys/controller.py`, `invitations/controller.py`, `clients/controller.py`, `custom_metrics/controller.py`, `SiteService`, `goals/controller.py`, `audit/controller.py`, `reports/service.py`, `company/controller.py`, `.__init__`, `mcm/service.py`, `CommissionService`, `.__init__`, `documents/controller.py`, `checklists/controller.py`, `.__init__`, `networks/service.py`, `SiteChecklistService`, `Services`, `.__init__`, `.__init__`, `currencies/controller.py`, `contracts/controller.py`, `clients`, `members/controller.py`, `account/controller.py`, `.uow`, `networks/controller.py`, `TaskQueue`, `commissions/controller.py`, `.__init__`, `ReportService`, `ItemsOut`, `.__init__`, `GoalService`, `.__init__`, `CompanyService`, `profile/controller.py`, `image`, `download`, `people/controller.py`, `InvoiceService`, `avant_core_access_models`, `auth/controller.py`, `google/controller.py`, `invoices/service.py`?**
  _High betweenness centrality (0.165) - this node is a cross-community bridge._
- **Are the 123 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 123 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `conftest.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07550860719874804 - nodes in this community are weakly interconnected._
- **Why does `get()` connect `get` to `image`, `DashboardService`, `Actor`, `edit_image`, `ClientService`, `GamToolService`, `mine`, `UnitOfWorkFactory`, `roles/controller.py`, `person`, `InvoiceService`, `.uow`, `shared/dto.py`, `_month`, `api_keys/controller.py`, `AuditOut`, `invitations/controller.py`, `custom_metrics/controller.py`, `templates`, `SiteService`, `reports/controller.py`, `goals/controller.py`, `clients`, `image`, `audit/controller.py`, `invoices/controller.py`, `Actor`, `mcm/service.py`, `.save_rule`, `CommissionService`, `.available_months`, `networks/service.py`, `download`, `Services`, `Actor`, `currencies/controller.py`, `members/controller.py`, `EventService`, `clients`, `OwnerInvitationOut`, `_month`, `account/controller.py`, `contracts/controller.py`, `networks/controller.py`, `main.py`, `Actor`, `ReportService`, `.payee_details`, `GoalService`, `NetworkDetailOut`, `CompanyService`, `image`, `download`, `people/controller.py`, `InvoiceService`, `avant_core_access_models`, `auth/controller.py`, `SiteListOut`, `google/controller.py`, `invoices/service.py`, `SiteOut`, `AdUnitOut`, `tasks/controller.py`, `connect`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07441016333938294 - nodes in this community are weakly interconnected._