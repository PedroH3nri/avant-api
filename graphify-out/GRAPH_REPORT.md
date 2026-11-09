# Graph Report - avant-api  (2026-11-09)

## Corpus Check
- 317 files · ~98,956 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4396 nodes · 12002 edges · 251 communities (119 shown, 132 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1946 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9cefc433`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- reward_public/service.py
- MemberOut
- roles/controller.py
- .uow
- AlertService
- _report
- gam_tools/dto.py
- GoalTemplateOut
- steps
- schedules/controller.py
- Avant: conexão com o GAM
- SavedReportOut
- .trusted_uow
- GroupService
- inventory/dto.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- PageOut
- ClientOut
- CustomMetricService
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- Settings
- dashboard_templates/controller.py
- invoice_pdf.py
- shared/http.py
- clean_code.py
- delete_template
- mfa/controller.py
- Avant: repositório e plano do MVP
- ReportService
- company/controller.py
- forget_pages
- session-start.sh
- avant-api
- require_staff
- BaseModel
- .start
- skipif
- Actor
- datetime
- documents/controller.py
- test_account.py
- Services
- test_reports.py
- SavedViewService
- checklists/controller.py
- download
- client_notes/controller.py
- mine
- modules/rewards/controller.py
- edit
- currencies/controller.py
- avant_core_access_models
- test_rewards.py
- ItemsOut
- SupportTaskService
- internal/rewards/controller.py
- account/controller.py
- client_documents/controller.py
- checklists
- commissions/controller.py
- SessionCookies
- install
- company/controller.py
- tasks/controller.py
- export.py
- Limiter
- .export
- logs.py
- .of_detail
- avant-api
- MemoryBucket
- modules/rewards/controller.py
- test_company_image.py
- networks/controller.py
- costs/controller.py
- ClientDocumentService
- events.py
- test_dashboards.py
- test_alerts.py
- ClientRewardService
- sites/controller.py
- Avant: grupos na Empresa e imagem da Empresa
- key_values/controller.py
- tasks/controller.py
- SiteListOut
- GoalService
- google/controller.py
- RecordingQueue
- clients/controller.py
- goals/controller.py
- Avant: conexão com o GAM
- updates
- auth/controller.py
- contracts/dto.py
- GamToolService
- ContractOut
- ReportService
- shared/dto.py
- Actor
- dollars
- .of
- Arquitetura do MVP do Avant
- test_mfa.py
- .of
- get
- _csrf
- PageOut
- SiteService
- commissions/dto.py
- RedisCounter
- tasks
- CompanyService
- clients
- Actor
- mcm/controller.py
- AuthService
- download
- .of_view
- people/service.py
- ClientService
- document_response
- .of
- GamToolNetworkOut
- conftest.py
- .of
- UUID
- UserOut
- modules/results/controller.py
- ad_units
- .of
- get
- available_months
- RevenueStatusOut
- UserOut
- _month
- tasks
- NetworkOut
- TaskPatchIn
- test_key_values.py
- gam_tools/controller.py
- download
- gam_tools/service.py
- ReportQueryIn
- .export_saved
- Avant: conexão com o GAM
- MemoryCounter
- Actor
- image
- mine
- person
- CommissionService
- .page_saved
- .query_batch
- image
- test_members_without_schedules_manage_only_see_what_they_receive
- CommissionRuleOut
- .assign
- edit_image
- profile/controller.py
- set_settings
- TaskPatchIn
- test_groups_lifecycle
- is_exempt

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 173 edges
2. `PageOut` - 155 edges
3. `_csrf()` - 155 edges
4. `_onboard_owner()` - 154 edges
5. `get()` - 137 edges
6. `UnitOfWorkFactory` - 129 edges
7. `Services` - 115 edges
8. `ReportService` - 79 edges
9. `_staff()` - 70 edges
10. `page_out()` - 65 edges

## Surprising Connections (you probably didn't know these)
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/modules/internal/people/controller.py
- `Estrutura` --references--> `Services`  [INFERRED]
  README.md → src/avant_api/app/container.py
- `O que já tem` --references--> `edit()`  [INFERRED]
  README.md → src/avant_api/modules/company/controller.py
- `O que já tem` --references--> `items()`  [INFERRED]
  README.md → src/avant_api/modules/internal/checklist_items/controller.py

## Import Cycles
- None detected.

## Communities (251 total, 132 thin omitted)

### Community 0 - "reward_public/service.py"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 1 - "MemberOut"
Cohesion: 0.09
Nodes (5): invite(), options(), staff(), StaffInviteIn, StaffService

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.05
Nodes (28): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+20 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "_report"
Cohesion: 0.14
Nodes (19): Sent, _owner_invite(), test_busy_export_answers_503_with_retry_after(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run(), _ana_id(), _report(), test_chart_options_keep_metric_styles() (+11 more)

### Community 6 - "gam_tools/dto.py"
Cohesion: 0.13
Nodes (4): GamStepOut, GamToolPersonOut, GamToolRunNetworkOut, GamToolSiteOut

### Community 7 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: conexão com o GAM"
Cohesion: 0.09
Nodes (21): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+13 more)

### Community 11 - "SavedReportOut"
Cohesion: 0.10
Nodes (4): create(), update(), SavedReportIn, SavedReportOut

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.13
Nodes (6): networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.12
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "ClientOut"
Cohesion: 0.12
Nodes (5): client(), register_client(), remove_client_image(), ClientDetailOut, ClientOut

### Community 19 - "CustomMetricService"
Cohesion: 0.08
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "Settings"
Cohesion: 0.05
Nodes (16): engine_options(), _google(), _mailer(), NoEvents, GoogleOAuth, configure_logging(), MemoryRewardCache, Settings (+8 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.13
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (11): get_cookies(), auth_service(), confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn (+3 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "ReportService"
Cohesion: 0.06
Nodes (17): QueryTooHeavy, Bucket, CustomCatalogMetricOut, DimensionOut, FilterIn, MetricOut, OrderIn, PeriodIn (+9 more)

### Community 31 - "company/controller.py"
Cohesion: 0.16
Nodes (5): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 36 - "require_staff"
Cohesion: 0.06
Nodes (23): CompanyChanged, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company() (+15 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 40 - "Actor"
Cohesion: 0.12
Nodes (7): audit(), cancel_owner(), change_status(), client_image(), client_options(), edit_client(), edit_client_image()

### Community 41 - "datetime"
Cohesion: 0.07
Nodes (8): refresh_levels(), _error_code(), test_closing_deployed_cookies_keeps_them_secure(), test_deployed_cookies_use_the_host_prefix(), test_every_write_route_refuses_another_site(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 42 - "documents/controller.py"
Cohesion: 0.15
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "test_account.py"
Cohesion: 0.12
Nodes (27): CapturingMailer, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited() (+19 more)

### Community 45 - "Services"
Cohesion: 0.05
Nodes (12): Services, get_services(), account_service(), api_key_service(), checklist_item_service(), site_checklist_service(), client_inventory_service(), client_result_service() (+4 more)

### Community 46 - "test_reports.py"
Cohesion: 0.11
Nodes (20): client(), engine(), mailer(), _checkouts(), test_report_requests_use_few_connections(), query(), _day(), _metrics() (+12 more)

### Community 47 - "SavedViewService"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "checklists/controller.py"
Cohesion: 0.15
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistDetailOut, ChecklistMarkIn (+2 more)

### Community 49 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 52 - "modules/rewards/controller.py"
Cohesion: 0.09
Nodes (11): RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO (+3 more)

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "avant_core_access_models"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "test_rewards.py"
Cohesion: 0.15
Nodes (13): _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission(), test_staff_without_permission_and_other_clients() (+5 more)

### Community 57 - "ItemsOut"
Cohesion: 0.13
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 58 - "SupportTaskService"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 59 - "internal/rewards/controller.py"
Cohesion: 0.08
Nodes (13): ad_units(), create(), delete(), delete_lead(), export_leads(), leads(), set_active(), set_icon() (+5 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn (+5 more)

### Community 61 - "client_documents/controller.py"
Cohesion: 0.23
Nodes (3): client_document_service(), ClientDocumentsOut, RejectDocumentIn

### Community 62 - "checklists"
Cohesion: 0.15
Nodes (5): checklists(), months(), summary(), ChecklistMonthOut, SiteChecklistService

### Community 63 - "commissions/controller.py"
Cohesion: 0.16
Nodes (6): adjust(), create_rule(), delete_rule(), rules(), update_rule(), CommissionRuleIn

### Community 65 - "install"
Cohesion: 0.12
Nodes (8): error_body(), ExportsBusy, install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 66 - "company/controller.py"
Cohesion: 0.15
Nodes (6): create_service(), update_service(), invoice_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 67 - "tasks/controller.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 68 - "export.py"
Cohesion: 0.08
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 69 - "Limiter"
Cohesion: 0.10
Nodes (10): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter() (+2 more)

### Community 70 - ".export"
Cohesion: 0.10
Nodes (11): create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned(), run() (+3 more)

### Community 72 - ".of_detail"
Cohesion: 0.14
Nodes (3): ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 75 - "MemoryBucket"
Cohesion: 0.14
Nodes (7): BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 76 - "modules/rewards/controller.py"
Cohesion: 0.09
Nodes (14): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+6 more)

### Community 77 - "test_company_image.py"
Cohesion: 0.10
Nodes (13): _check_jpeg_size(), PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image() (+5 more)

### Community 78 - "networks/controller.py"
Cohesion: 0.12
Nodes (13): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+5 more)

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 82 - "events.py"
Cohesion: 0.09
Nodes (9): TooManyAttempts, channel(), EventSource, _parse(), sse(), StreamLimiter, events(), EventService (+1 more)

### Community 83 - "test_dashboards.py"
Cohesion: 0.18
Nodes (9): _form(), _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit() (+1 more)

### Community 84 - "test_alerts.py"
Cohesion: 0.35
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 85 - "ClientRewardService"
Cohesion: 0.12
Nodes (5): index(), metrics(), ClientRewardService, RewardMetricsOut, RewardOut

### Community 86 - "sites/controller.py"
Cohesion: 0.18
Nodes (11): classify(), classify_many(), link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn (+3 more)

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "key_values/controller.py"
Cohesion: 0.09
Nodes (10): Network, Segurança e limites, RateLimited, KeyValueBuffer, cors(), preflight(), receive(), KeyValueIn (+2 more)

### Community 89 - "tasks/controller.py"
Cohesion: 0.28
Nodes (10): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports(), test_redis_source_delivers_published_messages() (+2 more)

### Community 91 - "SiteListOut"
Cohesion: 0.17
Nodes (3): create(), site_options(), SiteListOut

### Community 92 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 94 - "google/controller.py"
Cohesion: 0.07
Nodes (11): GoogleFailed, challenge(), _claims(), identity_from_id_token(), new_verifier(), google_start(), google_redirects(), google_service() (+3 more)

### Community 96 - "RecordingQueue"
Cohesion: 0.12
Nodes (15): RecordingQueue, _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites() (+7 more)

### Community 97 - "clients/controller.py"
Cohesion: 0.16
Nodes (10): new_owner(), client_service(), ClientIn, ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn (+2 more)

### Community 98 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 123 - "Avant: conexão com o GAM"
Cohesion: 0.10
Nodes (4): GoogleUnavailable, GoogleAuth, google_callback(), GoogleService

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "auth/controller.py"
Cohesion: 0.12
Nodes (13): accept(), company_image(), do_logout(), login(), me(), set_active_company(), AcceptInvitationIn, ActiveCompanyIn (+5 more)

### Community 129 - "contracts/dto.py"
Cohesion: 0.12
Nodes (3): google_status(), google_unlink(), GoogleStatusOut

### Community 131 - "GamToolService"
Cohesion: 0.19
Nodes (3): run(), GamToolRunOut, GamToolService

### Community 132 - "ContractOut"
Cohesion: 0.06
Nodes (24): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, contract(), contract_networks() (+16 more)

### Community 133 - "ReportService"
Cohesion: 0.15
Nodes (3): catalog(), MetricCatalogOut, ReportService

### Community 134 - "shared/dto.py"
Cohesion: 0.13
Nodes (4): index(), audit_service(), AuditService, AuditOut

### Community 136 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), delete(), index(), show(), sites_of_member(), unlinked()

### Community 138 - "dollars"
Cohesion: 0.10
Nodes (7): dollars(), AvailableMonthOut, InvoiceItemOut, InvoiceSummaryOut, ReturnedOut, ReturnIn, ServiceItemIn

### Community 142 - ".of"
Cohesion: 0.18
Nodes (6): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, ClientService, owner_invitation_out()

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.21
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+6 more)

### Community 145 - ".of"
Cohesion: 0.24
Nodes (4): client_teams(), ClientMemberOut, CompanyRefOut, RoleRefOut

### Community 146 - "get"
Cohesion: 0.10
Nodes (15): add_item(), available_months(), delete(), delete_service(), get(), issue(), mine(), pay() (+7 more)

### Community 147 - "_csrf"
Cohesion: 0.07
Nodes (37): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+29 more)

### Community 148 - "PageOut"
Cohesion: 0.04
Nodes (10): UnitOfWorkFactory, reward_cache_key(), RewardCache, TaskQueue, results(), ClientResultService, ResultsOut, default_period() (+2 more)

### Community 149 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 152 - "commissions/dto.py"
Cohesion: 0.17
Nodes (5): AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn

### Community 155 - "tasks"
Cohesion: 0.09
Nodes (6): observe(), _route_template(), health(), ready(), health_service(), HealthService

### Community 160 - "CompanyService"
Cohesion: 0.16
Nodes (5): remove_image(), show(), CompanyDetailOut, CompanyService, image_url()

### Community 163 - "mcm/controller.py"
Cohesion: 0.14
Nodes (8): confirm_network(), register_network(), reject_network(), unassigned_networks(), mcm_service(), ClientNetworkIn, McmCandidateOut, McmService

### Community 167 - "people/service.py"
Cohesion: 0.15
Nodes (6): disable(), enable(), reset_mfa(), users(), people_service(), PeopleService

### Community 174 - "GamToolNetworkOut"
Cohesion: 0.15
Nodes (5): network(), networks(), GamToolClientOut, GamToolNetworkDetailOut, GamToolNetworkOut

### Community 175 - "conftest.py"
Cohesion: 0.10
Nodes (20): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture() (+12 more)

### Community 176 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 177 - "UUID"
Cohesion: 0.19
Nodes (3): save_payment_details(), PayeeDetailsOut, FiscalDataOut

### Community 178 - "UserOut"
Cohesion: 0.12
Nodes (6): edit_appearance(), edit_image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService

### Community 180 - "modules/results/controller.py"
Cohesion: 0.14
Nodes (3): show(), result_service(), ResultService

### Community 190 - "UserOut"
Cohesion: 0.18
Nodes (3): PersonOut, person_out(), UserOut

### Community 191 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 192 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 198 - "test_key_values.py"
Cohesion: 0.22
Nodes (5): _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 201 - "gam_tools/controller.py"
Cohesion: 0.23
Nodes (4): ads_txt(), install(), runs(), AdsTxtOut

### Community 204 - "download"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 214 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo

### Community 224 - ".query_batch"
Cohesion: 0.32
Nodes (3): query_batch(), ReportBatchIn, ReportBatchOut

### Community 226 - "test_members_without_schedules_manage_only_see_what_they_receive"
Cohesion: 0.38
Nodes (3): _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 228 - ".assign"
Cohesion: 0.40
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2015 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **132 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `PageOut` to `auth/controller.py`, `MemberOut`, `roles/controller.py`, `.uow`, `AlertService`, `ContractOut`, `shared/dto.py`, `GamToolService`, `ReportService`, `schedules/controller.py`, `dollars`, `.trusted_uow`, `GroupService`, `.of`, `inventory/dto.py`, `api_keys/controller.py`, `PageOut`, `CustomMetricService`, `SiteService`, `.uow`, `dashboard_templates/controller.py`, `commissions/dto.py`, `mfa/controller.py`, `ReportService`, `company/controller.py`, `CompanyService`, `AuthService`, `people/service.py`, `documents/controller.py`, `SavedViewService`, `client_notes/controller.py`, `UserOut`, `modules/results/controller.py`, `currencies/controller.py`, `avant_core_access_models`, `.__init__`, `ItemsOut`, `SupportTaskService`, `account/controller.py`, `client_documents/controller.py`, `checklists`, `UnitOfWorkFactory`, `company/controller.py`, `tasks/controller.py`, `.of`, `networks/controller.py`, `costs/controller.py`, `ClientDocumentService`, `goals/service.py`, `gam_tools/service.py`, `sites/controller.py`, `GoalService`, `CompanyImage`, `google/controller.py`, `CommissionService`, `clients/controller.py`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `Avant: conexão com o GAM`?**
  _High betweenness centrality (0.118) - this node is a cross-community bridge._
- **Are the 116 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 116 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `MemberOut` be split into smaller, more focused modules?**
  _Cohesion score 0.0946969696969697 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `MemberOut`, `roles/controller.py`, `.uow`, `AlertService`, `ContractOut`, `shared/dto.py`, `GamToolService`, `GoalTemplateOut`, `schedules/controller.py`, `dollars`, `Actor`, `.trusted_uow`, `GroupService`, `.of`, `inventory/dto.py`, `api_keys/controller.py`, `.of`, `get`, `PageOut`, `Actor`, `SiteService`, `ReportService`, `forget_pages`, `clients`, `mcm/controller.py`, `people/service.py`, `Actor`, `ClientService`, `GamToolNetworkOut`, `checklists/controller.py`, `client_notes/controller.py`, `avant_core_access_models`, `SupportTaskService`, `internal/rewards/controller.py`, `checklists`, `tasks`, `company/controller.py`, `tasks/controller.py`, `gam_tools/controller.py`, `NetworkService`, `modules/rewards/controller.py`, `networks/controller.py`, `costs/controller.py`, `goals/service.py`, `gam_tools/service.py`, `ClientRewardService`, `sites/controller.py`, `GoalService`, `.page_saved`, `clients/controller.py`, `goals/controller.py`?**
  _High betweenness centrality (0.090) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07441016333938294 - nodes in this community are weakly interconnected._