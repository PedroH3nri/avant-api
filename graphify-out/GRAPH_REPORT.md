# Graph Report - avant-api  (2026-11-06)

## Corpus Check
- 303 files · ~94,087 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4125 nodes · 11274 edges · 206 communities (106 shown, 100 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1860 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `628e3fe6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_costs_results.py
- MemberOut
- roles/controller.py
- .uow
- AlertService
- _report
- GamToolService
- GoalTemplateOut
- steps
- schedules/controller.py
- Avant: conexão com o GAM
- .of
- .trusted_uow
- GroupService
- inventory/dto.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- PageOut
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- Settings
- dashboard_templates/controller.py
- invoice_pdf.py
- http.py
- clean_code.py
- delete_template
- mfa/controller.py
- Avant: repositório e plano do MVP
- reports/service.py
- .square_webp
- test_report_export.py
- session-start.sh
- avant-api
- require_staff
- BaseModel
- enqueue_sync
- test_key_values.py
- ClientService
- test_api.py
- documents/controller.py
- CapturingMailer
- SiteChecklistService
- security.py
- test_reports.py
- views/controller.py
- checklists/controller.py
- download
- client_notes/controller.py
- mine
- image
- edit
- currencies/controller.py
- avant_core_access_models
- MemoryCounter
- ItemsOut
- test_account.py
- test_api_keys.py
- account/controller.py
- ChecklistMonthOut
- .save_rule
- .classify
- install
- InvoiceService
- Actor
- export.py
- Limiter
- ReportService
- .of_detail
- avant-api
- NetworkService
- mcm/service.py
- clients
- networks/controller.py
- costs/controller.py
- client_documents/controller.py
- test_events.py
- uuid
- MemoryKeyValueBuffer
- results/dto.py
- sites/controller.py
- Avant: grupos na Empresa e imagem da Empresa
- key_values/service.py
- typing
- index
- GoalService
- errors.py
- RecordingQueue
- dollars
- goals/controller.py
- edit_image
- updates
- auth/controller.py
- test_goal_progress_routes
- RateLimited
- limits.py
- contracts/controller.py
- PageOut
- AdUnitOut
- invoices/service.py
- Arquitetura do MVP do Avant
- test_mfa.py
- get
- _csrf
- UnitOfWorkFactory
- SiteService
- .uow
- tasks/controller.py
- main.py
- company/controller.py
- .of
- _month
- mcm/controller.py
- RedisEvents
- TaskDetailOut
- people/service.py
- document_response
- commissions/controller.py
- test_account.py
- _member_client
- profile/controller.py
- tasks/dto.py
- ResultsOut
- .assign
- internal/results/controller.py
- mine
- CommissionService
- internal/results/service.py
- Actor
- CommissionRuleOut
- DashboardTemplateOut
- person
- fiscal
- test_checklists_need_permission
- image
- SiteListOut
- TaskPatchIn
- mcm/dto.py
- source_files

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 168 edges
2. `_csrf()` - 150 edges
3. `_onboard_owner()` - 150 edges
4. `PageOut` - 143 edges
5. `UnitOfWorkFactory` - 125 edges
6. `get()` - 125 edges
7. `Services` - 123 edges
8. `ReportService` - 79 edges
9. `_staff()` - 67 edges
10. `page_out()` - 59 edges

## Surprising Connections (you probably didn't know these)
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/modules/internal/people/controller.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Estrutura` --references--> `TaskQueue`  [INFERRED]
  README.md → src/avant_api/app/tasks.py
- `Estrutura` --references--> `Services`  [INFERRED]
  README.md → src/avant_api/app/container.py

## Import Cycles
- None detected.

## Communities (206 total, 100 thin omitted)

### Community 0 - "test_costs_results.py"
Cohesion: 0.11
Nodes (9): refresh_levels(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone() (+1 more)

### Community 1 - "MemberOut"
Cohesion: 0.11
Nodes (8): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut, RoleRefOut

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.05
Nodes (24): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+16 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "_report"
Cohesion: 0.13
Nodes (19): test_busy_export_answers_503_with_retry_after(), test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused() (+11 more)

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (20): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+12 more)

### Community 7 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 8 - "steps"
Cohesion: 0.05
Nodes (34): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+26 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: conexão com o GAM"
Cohesion: 0.09
Nodes (21): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+13 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.08
Nodes (8): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "Settings"
Cohesion: 0.04
Nodes (14): engine_options(), _google(), _mailer(), SessionCookies, NoEvents, get_cookies(), Settings, CeleryQueue (+6 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.18
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "reports/service.py"
Cohesion: 0.05
Nodes (18): QueryTooHeavy, catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn (+10 more)

### Community 31 - ".square_webp"
Cohesion: 0.17
Nodes (4): _check_jpeg_size(), _sharpness(), _striped_logo(), test_wide_and_palette_logos_stay_sharp()

### Community 32 - "test_report_export.py"
Cohesion: 0.28
Nodes (3): _result(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 36 - "require_staff"
Cohesion: 0.06
Nodes (22): CompanyChanged, ExportsBusy, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor() (+14 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 39 - "test_key_values.py"
Cohesion: 0.12
Nodes (6): RedisKeyValueBuffer, _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 40 - "ClientService"
Cohesion: 0.05
Nodes (32): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), edit_client() (+24 more)

### Community 41 - "test_api.py"
Cohesion: 0.07
Nodes (14): client(), engine(), mailer(), _error_code(), test_deployed_cookies_use_the_host_prefix(), test_every_write_route_refuses_another_site(), _jpeg(), _png() (+6 more)

### Community 42 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "CapturingMailer"
Cohesion: 0.11
Nodes (29): CapturingMailer, Sent, test_change_password_attempts_are_limited(), _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login() (+21 more)

### Community 44 - "SiteChecklistService"
Cohesion: 0.12
Nodes (4): checklist(), ChecklistDetailOut, ChecklistOut, SiteChecklistService

### Community 45 - "security.py"
Cohesion: 0.06
Nodes (13): Services, PillowImageProcessor, RedisBucket, get_services(), known_companies(), audit_service(), dashboard_service(), checklist_item_service() (+5 more)

### Community 46 - "test_reports.py"
Cohesion: 0.14
Nodes (17): _checkouts(), test_report_requests_use_few_connections(), query(), _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait() (+9 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "checklists/controller.py"
Cohesion: 0.10
Nodes (11): add_note(), check(), checklists(), delete_note(), edit_note(), mark(), months(), summary() (+3 more)

### Community 49 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.15
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "avant_core_access_models"
Cohesion: 0.07
Nodes (13): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+5 more)

### Community 57 - "ItemsOut"
Cohesion: 0.13
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 58 - "test_account.py"
Cohesion: 0.10
Nodes (7): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 59 - "test_api_keys.py"
Cohesion: 0.50
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 60 - "account/controller.py"
Cohesion: 0.08
Nodes (14): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+6 more)

### Community 63 - ".save_rule"
Cohesion: 0.14
Nodes (6): adjust(), create_rule(), delete_rule(), settings(), update_rule(), CommissionRuleIn

### Community 65 - "install"
Cohesion: 0.25
Nodes (7): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 66 - "InvoiceService"
Cohesion: 0.16
Nodes (8): create_service(), save_payment_details(), services(), update_item(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 67 - "Actor"
Cohesion: 0.14
Nodes (7): ad_units(), delete(), link(), show(), site_options(), sites_of_member(), unlinked()

### Community 68 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "Limiter"
Cohesion: 0.11
Nodes (8): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter()

### Community 70 - "ReportService"
Cohesion: 0.08
Nodes (15): create(), create_from_template(), delete(), export(), export_saved(), index(), pin(), query() (+7 more)

### Community 72 - ".of_detail"
Cohesion: 0.11
Nodes (4): ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "NetworkService"
Cohesion: 0.14
Nodes (3): options(), NetworkDetailOut, NetworkService

### Community 75 - "mcm/service.py"
Cohesion: 0.13
Nodes (4): NetworkIn, ServiceAccountOut, SyncRunOut, enqueue_sync()

### Community 78 - "networks/controller.py"
Cohesion: 0.13
Nodes (8): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs(), capped()

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "client_documents/controller.py"
Cohesion: 0.14
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 82 - "test_events.py"
Cohesion: 0.09
Nodes (15): channel(), _parse(), sse(), events(), _collect(), _event(), ListEvents, test_events_route() (+7 more)

### Community 83 - "uuid"
Cohesion: 0.13
Nodes (14): test_change_password_and_sessions(), _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), _kpi() (+6 more)

### Community 85 - "results/dto.py"
Cohesion: 0.15
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 86 - "sites/controller.py"
Cohesion: 0.25
Nodes (7): AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "key_values/service.py"
Cohesion: 0.09
Nodes (14): Network, Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação (+6 more)

### Community 89 - "typing"
Cohesion: 0.09
Nodes (5): RedisCounter, test_redis_limiter(), test_docs_are_closed_in_production(), test_every_response_has_the_security_headers(), test_redis_down_is_a_503_not_a_500()

### Community 92 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 94 - "errors.py"
Cohesion: 0.03
Nodes (19): GoogleUnavailable, EventSource, StreamLimiter, GoogleAuth, new_verifier(), event_service(), EventService, google_callback() (+11 more)

### Community 96 - "RecordingQueue"
Cohesion: 0.23
Nodes (9): RecordingQueue, _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites() (+1 more)

### Community 98 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "auth/controller.py"
Cohesion: 0.06
Nodes (16): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+8 more)

### Community 129 - "test_goal_progress_routes"
Cohesion: 0.53
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 131 - "limits.py"
Cohesion: 0.13
Nodes (7): Bucket, BucketResult, BucketRule, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 132 - "contracts/controller.py"
Cohesion: 0.06
Nodes (25): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+17 more)

### Community 134 - "PageOut"
Cohesion: 0.08
Nodes (5): index(), AuditService, AuditOut, page_out(), PageOut

### Community 138 - "invoices/service.py"
Cohesion: 0.16
Nodes (10): service_options(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut (+2 more)

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.17
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+6 more)

### Community 146 - "get"
Cohesion: 0.09
Nodes (14): add_item(), available_months(), create(), delete(), delete_service(), get(), issue(), mine() (+6 more)

### Community 147 - "_csrf"
Cohesion: 0.07
Nodes (35): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+27 more)

### Community 149 - "SiteService"
Cohesion: 0.22
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 150 - ".uow"
Cohesion: 0.07
Nodes (5): duplicate(), pinned(), SavedReportOut, export_slot(), ReportService

### Community 153 - "tasks/controller.py"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 155 - "main.py"
Cohesion: 0.08
Nodes (8): CsrfFailed, configure_logging(), JsonFormatter, observe(), _route_template(), check_fetch_site(), create_app(), health()

### Community 160 - "company/controller.py"
Cohesion: 0.16
Nodes (8): edit_fiscal(), edit_image(), company_service(), CompanyDetailOut, CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 162 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 163 - "mcm/controller.py"
Cohesion: 0.13
Nodes (6): confirm_network(), register_network(), reject_network(), unassigned_networks(), McmService, NetworkOut

### Community 165 - "TaskDetailOut"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 167 - "people/service.py"
Cohesion: 0.11
Nodes (10): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+2 more)

### Community 172 - "commissions/controller.py"
Cohesion: 0.31
Nodes (5): AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn

### Community 174 - "test_account.py"
Cohesion: 0.27
Nodes (6): FakeGoogle, _google_round(), _login(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 175 - "_member_client"
Cohesion: 0.10
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 178 - "profile/controller.py"
Cohesion: 0.20
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 179 - "tasks/dto.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 180 - "ResultsOut"
Cohesion: 0.13
Nodes (4): show(), result_service(), ResultsOut, ResultService

### Community 182 - ".assign"
Cohesion: 0.25
Nodes (5): Atribuição de sites, GAM, Networks, Sites e ad units, assign_sites()

### Community 183 - "internal/results/controller.py"
Cohesion: 0.14
Nodes (3): results(), client_result_service(), ClientResultService

### Community 189 - "CommissionService"
Cohesion: 0.20
Nodes (3): set_settings(), commission_service(), CommissionService

### Community 195 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 201 - "fiscal"
Cohesion: 0.25
Nodes (3): fiscal(), remove_image(), show()

### Community 203 - "test_checklists_need_permission"
Cohesion: 0.23
Nodes (6): _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list(), test_staff_marks_checks_and_writes_notes(), _agent(), test_staff_opens_assigns_and_comments_on_tasks()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1876 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **100 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `auth/controller.py`, `MemberOut`, `roles/controller.py`, `.uow`, `AlertService`, `contracts/controller.py`, `PageOut`, `GamToolService`, `.__init__`, `schedules/controller.py`, `invoices/service.py`, `.trusted_uow`, `GroupService`, `inventory/dto.py`, `api_keys/controller.py`, `PageOut`, `custom_metrics/controller.py`, `SiteService`, `.uow`, `dashboard_templates/controller.py`, `.__init__`, `mfa/controller.py`, `reports/service.py`, `company/controller.py`, `mcm/controller.py`, `TaskDetailOut`, `people/service.py`, `ClientService`, `documents/controller.py`, `SiteChecklistService`, `commissions/controller.py`, `views/controller.py`, `client_notes/controller.py`, `tasks/dto.py`, `profile/controller.py`, `ResultsOut`, `currencies/controller.py`, `internal/results/controller.py`, `avant_core_access_models`, `ItemsOut`, `.__init__`, `account/controller.py`, `CommissionService`, `internal/results/service.py`, `InvoiceService`, `.__init__`, `NetworkService`, `mcm/service.py`, `costs/controller.py`, `client_documents/controller.py`, `goals/service.py`, `sites/controller.py`, `.__init__`, `GoalService`, `.__init__`, `errors.py`?**
  _High betweenness centrality (0.127) - this node is a cross-community bridge._
- **Are the 122 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 122 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_costs_results.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10574712643678161 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `MemberOut`, `roles/controller.py`, `.uow`, `AlertService`, `contracts/controller.py`, `GamToolService`, `GoalTemplateOut`, `AdUnitOut`, `schedules/controller.py`, `invoices/service.py`, `.trusted_uow`, `GroupService`, `inventory/dto.py`, `api_keys/controller.py`, `PageOut`, `get`, `SiteService`, `tasks/controller.py`, `reports/service.py`, `mcm/controller.py`, `TaskDetailOut`, `people/service.py`, `ClientService`, `SiteChecklistService`, `checklists/controller.py`, `client_notes/controller.py`, `tasks/dto.py`, `internal/results/controller.py`, `avant_core_access_models`, `internal/results/service.py`, `InvoiceService`, `Actor`, `ReportService`, `NetworkService`, `mcm/service.py`, `clients`, `networks/controller.py`, `costs/controller.py`, `goals/service.py`, `sites/controller.py`, `index`, `GoalService`, `goals/controller.py`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Should `MemberOut` be split into smaller, more focused modules?**
  _Cohesion score 0.1051693404634581 - nodes in this community are weakly interconnected._