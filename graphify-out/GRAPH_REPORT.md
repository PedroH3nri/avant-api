# Graph Report - avant-api  (2026-11-09)

## Corpus Check
- 324 files · ~101,352 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4498 nodes · 12280 edges · 232 communities (114 shown, 118 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1972 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `49d729d5`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- reward_public/controller.py
- MemberOut
- roles/controller.py
- .uow
- AlertService
- UUID
- gam_tools/dto.py
- GoalService
- test
- schedules/controller.py
- Avant: conexão com o GAM
- DashboardTemplateOut
- .trusted_uow
- GroupService
- inventory/dto.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- PageOut
- .build
- CustomMetricService
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- Settings
- dashboard_templates/controller.py
- invoice_pdf.py
- shared/http.py
- clean_code.py
- errors.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- reports/service.py
- CapturingMailer
- forget_pages
- session-start.sh
- avant-api
- require_staff
- tasks/controller.py
- mcm/service.py
- profile/controller.py
- _marketing_client
- documents/controller.py
- modules/results/controller.py
- router.py
- Services
- test_reports.py
- SavedViewService
- checklists/controller.py
- FastAPI
- client_notes/controller.py
- images.py
- modules/rewards/controller.py
- edit
- currencies/controller.py
- avant_core_access_models
- key_value_buffer.py
- ItemsOut
- SupportTaskService
- modules/rewards/controller.py
- account/controller.py
- client_documents/controller.py
- RedisRewardCache
- commissions/controller.py
- SessionCookies
- install
- company/controller.py
- tasks/controller.py
- export.py
- Limiter
- reports/controller.py
- logs.py
- .of_detail
- avant-api
- NetworkService
- MemoryBucket
- test_events.py
- test_networks.py
- networks/controller.py
- costs/controller.py
- internal/results/controller.py
- events.py
- test_dashboards.py
- test_alerts.py
- ClientRewardService
- sites/controller.py
- Avant: grupos na Empresa e imagem da Empresa
- limits.py
- PublicRewardService
- .assign
- google_start
- GoogleService
- RecordingQueue
- google_status
- InvoiceServiceOut
- test_api_keys.py
- updates
- auth/controller.py
- TooManyAttempts
- alerts/dependencies.py
- RedisCounter
- contracts/controller.py
- ReportService
- audit/controller.py
- SiteService
- dollars
- .of
- Arquitetura do MVP do Avant
- test_mfa.py
- EventService
- get
- _csrf
- internal/results/service.py
- SiteService
- .uow
- datetime
- RedisCounter
- postgres
- steps
- CompanyService
- RedisEvents
- verify
- mcm/controller.py
- AuthService
- download
- .of_view
- people/service.py
- ClientService
- .upload
- edit_image
- image
- _member_client
- RewardAdUnitGroupOut
- Actor
- UserOut
- health/controller.py
- .page_saved
- .of
- metrics
- test_contract_crud
- UnitOfWorkFactory
- test_busy_export_answers_503_with_retry_after
- capped
- .of
- create
- test_key_values.py
- ReportQueryIn
- mcm/dto.py
- site_service

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 175 edges
2. `_csrf()` - 157 edges
3. `_onboard_owner()` - 156 edges
4. `PageOut` - 155 edges
5. `get()` - 139 edges
6. `UnitOfWorkFactory` - 131 edges
7. `Services` - 120 edges
8. `ReportService` - 79 edges
9. `_staff()` - 70 edges
10. `page_out()` - 65 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/modules/internal/people/controller.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Estrutura` --references--> `TaskQueue`  [INFERRED]
  README.md → src/avant_api/app/tasks.py
- `Estrutura` --references--> `Services`  [INFERRED]
  README.md → src/avant_api/app/container.py

## Import Cycles
- None detected.

## Communities (232 total, 118 thin omitted)

### Community 0 - "reward_public/controller.py"
Cohesion: 0.17
Nodes (8): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body()

### Community 1 - "MemberOut"
Cohesion: 0.12
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.06
Nodes (25): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+17 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "UUID"
Cohesion: 0.13
Nodes (21): _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use() (+13 more)

### Community 6 - "gam_tools/dto.py"
Cohesion: 0.05
Nodes (20): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+12 more)

### Community 7 - "GoalService"
Cohesion: 0.05
Nodes (19): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+11 more)

### Community 8 - "test"
Cohesion: 0.15
Nodes (12): AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, jobs, test, name, on, pull_request (+4 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: conexão com o GAM"
Cohesion: 0.05
Nodes (36): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+28 more)

### Community 11 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 12 - ".trusted_uow"
Cohesion: 0.09
Nodes (3): mine(), invoice_service(), InvoiceService

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+6 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.07
Nodes (8): networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, page_out(), PageOut

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.11
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - ".build"
Cohesion: 0.05
Nodes (9): _google(), _mailer(), NoEvents, MemoryCounter, MemoryRewardBuffer, RedisRewardBuffer, RewardBuffer, MemoryRewardCache (+1 more)

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
Cohesion: 0.09
Nodes (9): engine_options(), Settings, test_closing_deployed_cookies_keeps_them_secure(), test_deployed_cookies_use_the_host_prefix(), _settings(), test_every_connection_has_a_statement_and_idle_timeout(), test_pool_is_bounded_and_waits_little(), test_queue_does_not_break_the_request_without_broker() (+1 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 27 - "errors.py"
Cohesion: 0.12
Nodes (6): CompanyChanged, ExportsBusy, GoogleUnavailable, NoActiveCompany, QueryTooHeavy, GoogleStatusOut

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (10): auth_service(), confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "reports/service.py"
Cohesion: 0.05
Nodes (14): CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn, PreviewPointOut (+6 more)

### Community 31 - "CapturingMailer"
Cohesion: 0.09
Nodes (34): CapturingMailer, Sent, _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password() (+26 more)

### Community 32 - "forget_pages"
Cohesion: 0.06
Nodes (14): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+6 more)

### Community 36 - "require_staff"
Cohesion: 0.08
Nodes (20): CsrfFailed, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company(), get_actor(), get_auth() (+12 more)

### Community 37 - "tasks/controller.py"
Cohesion: 0.05
Nodes (17): change(), comment(), create(), task(), tasks(), TaskClientOut, TaskCommentIn, TaskDataIn (+9 more)

### Community 40 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 41 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 42 - "documents/controller.py"
Cohesion: 0.19
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 43 - "modules/results/controller.py"
Cohesion: 0.14
Nodes (4): show(), result_service(), ResultsOut, ResultService

### Community 44 - "router.py"
Cohesion: 0.12
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 45 - "Services"
Cohesion: 0.04
Nodes (15): Services, get_services(), account_service(), currency_service(), google_redirects(), google_service(), group_service(), checklist_item_service() (+7 more)

### Community 46 - "test_reports.py"
Cohesion: 0.10
Nodes (19): client(), refresh_levels(), _checkouts(), test_report_requests_use_few_connections(), query(), _day(), _metrics(), _row() (+11 more)

### Community 47 - "SavedViewService"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "checklists/controller.py"
Cohesion: 0.10
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), site_checklist_service(), ChecklistDetailOut (+2 more)

### Community 49 - "FastAPI"
Cohesion: 0.08
Nodes (9): observe(), _route_template(), create_app(), documents(), download(), upload(), document_service(), DocumentService (+1 more)

### Community 50 - "client_notes/controller.py"
Cohesion: 0.09
Nodes (8): add(), delete(), edit(), notes(), ClientNoteIn, ClientNoteOut, NotePersonOut, ClientNoteService

### Community 51 - "images.py"
Cohesion: 0.13
Nodes (6): _check_jpeg_size(), PillowImageProcessor, _sharpness(), _striped_logo(), test_phone_rotation_from_exif_is_kept(), test_wide_and_palette_logos_stay_sharp()

### Community 52 - "modules/rewards/controller.py"
Cohesion: 0.07
Nodes (21): metrics(), PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicStyleOut (+13 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.15
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "avant_core_access_models"
Cohesion: 0.06
Nodes (16): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+8 more)

### Community 57 - "ItemsOut"
Cohesion: 0.13
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 58 - "SupportTaskService"
Cohesion: 0.10
Nodes (6): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.12
Nodes (6): client_reward_service(), reward_service(), csv_response(), lead_filter(), period(), image_upload()

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn (+5 more)

### Community 61 - "client_documents/controller.py"
Cohesion: 0.26
Nodes (5): client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 62 - "RedisRewardCache"
Cohesion: 0.13
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "commissions/controller.py"
Cohesion: 0.06
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 65 - "install"
Cohesion: 0.25
Nodes (7): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 66 - "company/controller.py"
Cohesion: 0.20
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 67 - "tasks/controller.py"
Cohesion: 0.09
Nodes (6): accept(), company_image(), do_logout(), login(), set_active_company(), AuthService

### Community 68 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "Limiter"
Cohesion: 0.10
Nodes (8): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "reports/controller.py"
Cohesion: 0.08
Nodes (13): catalog(), create_from_template(), delete(), export(), export_saved(), pin(), query(), query_batch() (+5 more)

### Community 72 - ".of_detail"
Cohesion: 0.09
Nodes (6): ChecklistMarkIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "NetworkService"
Cohesion: 0.16
Nodes (3): index(), NetworkDetailOut, NetworkService

### Community 75 - "MemoryBucket"
Cohesion: 0.20
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 76 - "test_events.py"
Cohesion: 0.28
Nodes (10): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports(), test_redis_source_delivers_published_messages() (+2 more)

### Community 77 - "test_networks.py"
Cohesion: 0.08
Nodes (22): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), test_upload_without_session_is_refused_before_reading_the_body(), _clients_viewer(), _queue(), _second_owner() (+14 more)

### Community 78 - "networks/controller.py"
Cohesion: 0.15
Nodes (8): connect(), disconnect(), options(), service_account(), show(), sync(), sync_runs(), network_service()

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 81 - "internal/results/controller.py"
Cohesion: 0.14
Nodes (3): results(), client_result_service(), ClientResultService

### Community 82 - "events.py"
Cohesion: 0.16
Nodes (4): channel(), EventSource, _parse(), sse()

### Community 83 - "test_dashboards.py"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company()

### Community 85 - "ClientRewardService"
Cohesion: 0.07
Nodes (14): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), set_active() (+6 more)

### Community 86 - "sites/controller.py"
Cohesion: 0.25
Nodes (8): AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn, SitesPatchIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "limits.py"
Cohesion: 0.06
Nodes (15): RateLimited, KeyValueBuffer, Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, cors() (+7 more)

### Community 89 - "PublicRewardService"
Cohesion: 0.14
Nodes (3): RewardEventsIn, RewardLeadIn, PublicRewardService

### Community 91 - ".assign"
Cohesion: 0.13
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 92 - "google_start"
Cohesion: 0.21
Nodes (3): new_verifier(), google_start(), GoogleRedirects

### Community 94 - "GoogleService"
Cohesion: 0.12
Nodes (3): GoogleAuth, google_callback(), GoogleService

### Community 96 - "RecordingQueue"
Cohesion: 0.12
Nodes (15): RecordingQueue, _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites() (+7 more)

### Community 98 - "InvoiceServiceOut"
Cohesion: 0.27
Nodes (4): create_service(), update_service(), InvoiceServiceIn, InvoiceServiceOut

### Community 123 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "auth/controller.py"
Cohesion: 0.11
Nodes (10): get_invitation(), me(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut (+2 more)

### Community 129 - "TooManyAttempts"
Cohesion: 0.27
Nodes (3): TooManyAttempts, StreamLimiter, test_stream_limiter_caps_each_person_and_the_process()

### Community 131 - "RedisCounter"
Cohesion: 0.14
Nodes (4): RedisCounter, test_docs_are_closed_in_production(), test_every_response_has_the_security_headers(), test_redis_down_is_a_503_not_a_500()

### Community 132 - "contracts/controller.py"
Cohesion: 0.06
Nodes (23): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, contract(), contract_networks() (+15 more)

### Community 134 - "audit/controller.py"
Cohesion: 0.23
Nodes (3): index(), audit_service(), AuditService

### Community 142 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.38
Nodes (11): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+3 more)

### Community 146 - "get"
Cohesion: 0.08
Nodes (27): add_item(), available_months(), create(), delete(), delete_service(), get(), issue(), pay() (+19 more)

### Community 147 - "_csrf"
Cohesion: 0.08
Nodes (35): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+27 more)

### Community 150 - ".uow"
Cohesion: 0.06
Nodes (8): create(), duplicate(), pinned(), update(), SavedReportIn, SavedReportOut, ReportService, _statement_timeout()

### Community 152 - "datetime"
Cohesion: 0.08
Nodes (6): engine(), mailer(), _error_code(), test_every_write_route_refuses_another_site(), _jpeg(), test_phone_photos_pass_and_huge_pngs_are_refused()

### Community 153 - "RedisCounter"
Cohesion: 0.24
Nodes (5): _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 155 - "postgres"
Cohesion: 0.20
Nodes (10): POSTGRES_PASSWORD, env, image, options, ports, image, ports, postgres (+2 more)

### Community 158 - "steps"
Cohesion: 0.22
Nodes (9): AVANT_CORE_ACCESS, PGPASSWORD, env, name, run, uses, with, steps (+1 more)

### Community 160 - "CompanyService"
Cohesion: 0.18
Nodes (4): show(), company_service(), CompanyDetailOut, CompanyService

### Community 163 - "mcm/controller.py"
Cohesion: 0.13
Nodes (6): confirm_network(), register_network(), reject_network(), unassigned_networks(), McmService, NetworkOut

### Community 165 - "download"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 167 - "people/service.py"
Cohesion: 0.12
Nodes (7): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService

### Community 168 - "ClientService"
Cohesion: 0.04
Nodes (34): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), edit_client() (+26 more)

### Community 172 - "edit_image"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 175 - "_member_client"
Cohesion: 0.10
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 177 - "Actor"
Cohesion: 0.12
Nodes (8): ad_units(), assign_sites(), delete(), index(), show(), site_options(), sites_of_member(), unlinked()

### Community 178 - "UserOut"
Cohesion: 0.12
Nodes (4): person_out(), edit_image(), remove_image(), UserOut

### Community 180 - "health/controller.py"
Cohesion: 0.14
Nodes (4): health(), ready(), health_service(), HealthService

### Community 186 - "test_contract_crud"
Cohesion: 0.38
Nodes (3): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission()

### Community 189 - "test_busy_export_answers_503_with_retry_after"
Cohesion: 0.33
Nodes (3): test_busy_export_answers_503_with_retry_after(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 198 - "test_key_values.py"
Cohesion: 0.25
Nodes (3): classify(), classify_many(), link()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2060 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **118 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `auth/controller.py`, `MemberOut`, `roles/controller.py`, `.uow`, `AlertService`, `contracts/controller.py`, `audit/controller.py`, `gam_tools/dto.py`, `GoalService`, `ReportService`, `schedules/controller.py`, `SiteService`, `.trusted_uow`, `GroupService`, `inventory/dto.py`, `api_keys/controller.py`, `PageOut`, `get`, `CustomMetricService`, `internal/results/service.py`, `.uow`, `dashboard_templates/controller.py`, `errors.py`, `mfa/controller.py`, `reports/service.py`, `CompanyService`, `tasks/controller.py`, `mcm/service.py`, `people/service.py`, `ClientService`, `profile/controller.py`, `documents/controller.py`, `modules/results/controller.py`, `SavedViewService`, `checklists/controller.py`, `FastAPI`, `client_notes/controller.py`, `currencies/controller.py`, `avant_core_access_models`, `.__init__`, `ItemsOut`, `account/controller.py`, `client_documents/controller.py`, `commissions/controller.py`, `company/controller.py`, `tasks/controller.py`, `Limiter`, `gam_tools/controller.py`, `NetworkService`, `costs/controller.py`, `internal/results/controller.py`, `.__init__`, `sites/controller.py`, `MemoryCounter`, `limits.py`, `GoogleService`, `.__init__`, `.__init__`, `.__init__`?**
  _High betweenness centrality (0.114) - this node is a cross-community bridge._
- **Are the 116 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 116 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `MemberOut` be split into smaller, more focused modules?**
  _Cohesion score 0.12307692307692308 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `inventory/dto.py` to `MemberOut`, `roles/controller.py`, `.uow`, `AlertService`, `contracts/controller.py`, `audit/controller.py`, `gam_tools/dto.py`, `GoalService`, `ReportService`, `schedules/controller.py`, `SiteService`, `.trusted_uow`, `GroupService`, `api_keys/controller.py`, `PageOut`, `get`, `internal/results/service.py`, `reports/service.py`, `forget_pages`, `mcm/controller.py`, `tasks/controller.py`, `mcm/service.py`, `.of_view`, `ClientService`, `people/service.py`, `router.py`, `checklists/controller.py`, `Actor`, `client_notes/controller.py`, `.page_saved`, `avant_core_access_models`, `modules/rewards/controller.py`, `NetworkService`, `networks/controller.py`, `costs/controller.py`, `internal/results/controller.py`, `ClientRewardService`, `sites/controller.py`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07562008469449485 - nodes in this community are weakly interconnected._