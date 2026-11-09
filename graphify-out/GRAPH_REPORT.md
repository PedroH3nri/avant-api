# Graph Report - avant-api  (2026-11-09)

## Corpus Check
- 317 files · ~98,876 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4388 nodes · 12004 edges · 212 communities (111 shown, 101 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1949 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2f5baf15`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _marketing_client
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
- DashboardTemplateOut
- .trusted_uow
- GroupService
- inventory/dto.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- PageOut
- clients/dto.py
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
- ReportService
- ExportsBusy
- RewardService
- session-start.sh
- avant-api
- require_staff
- tasks/controller.py
- TaskQueue
- test_key_values.py
- clients/controller.py
- test_api.py
- documents/controller.py
- CapturingMailer
- security.py
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
- CapturingMailer
- ItemsOut
- test_account.py
- ClientRewardService
- account/controller.py
- ClientDocumentsOut
- SiteChecklistService
- commissions/controller.py
- SessionCookies
- install
- InvoiceService
- auth/controller.py
- export.py
- Limiter
- ReportService
- main.py
- .of_detail
- avant-api
- NetworkService
- networks/service.py
- Actor
- test_company_image.py
- networks/controller.py
- costs/controller.py
- client_documents/controller.py
- events.py
- test_dashboards.py
- test_alerts.py
- sites/controller.py
- Avant: grupos na Empresa e imagem da Empresa
- limits.py
- test_events.py
- SiteListOut
- GoalService
- google/controller.py
- RecordingQueue
- ClientService
- goals/controller.py
- GoogleService
- updates
- auth/controller.py
- google_status
- AdUnitOut
- RedisCounter
- contracts/controller.py
- RewardCache
- PageOut
- SiteOut
- invoices/service.py
- OwnerInvitationOut
- Arquitetura do MVP do Avant
- test_mfa.py
- .of
- get
- _csrf
- UnitOfWorkFactory
- SiteService
- .uow
- rewards/http.py
- RedisRewardCache
- health/controller.py
- test_rewards_panel
- company/controller.py
- clients
- Actor
- mcm/controller.py
- RedisEvents
- options
- people/service.py
- Actor
- document_response
- .of
- .of
- _member_client
- http.py
- PayeeDetailsOut
- UserOut
- results/dto.py
- SiteService
- service_options
- FakeGoogle
- networks/dependencies.py
- source_files
- metrics

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 173 edges
2. `PageOut` - 155 edges
3. `_csrf()` - 155 edges
4. `_onboard_owner()` - 154 edges
5. `get()` - 137 edges
6. `UnitOfWorkFactory` - 129 edges
7. `Services` - 112 edges
8. `ReportService` - 79 edges
9. `_staff()` - 70 edges
10. `page_out()` - 65 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/modules/company/controller.py
- `Imagem da Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/08-grupos-e-imagem-da-empresa.md → src/avant_api/modules/company/controller.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Estrutura` --references--> `Services`  [INFERRED]
  README.md → src/avant_api/app/container.py

## Import Cycles
- None detected.

## Communities (212 total, 101 thin omitted)

### Community 0 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 1 - "MemberOut"
Cohesion: 0.13
Nodes (7): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.06
Nodes (24): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+16 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "_report"
Cohesion: 0.11
Nodes (21): Sent, _owner_invite(), test_busy_export_answers_503_with_retry_after(), _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast(), _ana_id() (+13 more)

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (20): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+12 more)

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
Cohesion: 0.08
Nodes (25): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+17 more)

### Community 11 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.08
Nodes (8): networks(), sites(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, image_url()

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.11
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "clients/dto.py"
Cohesion: 0.09
Nodes (9): edit_client(), register_client(), ClientIn, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+1 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "Settings"
Cohesion: 0.04
Nodes (15): engine_options(), _google(), _mailer(), NoEvents, MemoryCounter, MemoryRewardCache, Settings, CeleryQueue (+7 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.13
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "http.py"
Cohesion: 0.17
Nodes (3): client_image(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "ReportService"
Cohesion: 0.04
Nodes (20): QueryTooHeavy, catalog(), index(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut (+12 more)

### Community 31 - "ExportsBusy"
Cohesion: 0.40
Nodes (3): ExportsBusy, test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 32 - "RewardService"
Cohesion: 0.09
Nodes (6): forget_pages(), create(), update(), RewardIn, RewardOut, RewardService

### Community 36 - "require_staff"
Cohesion: 0.06
Nodes (24): CompanyChanged, CsrfFailed, NoActiveCompany, RateLimited, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site() (+16 more)

### Community 37 - "tasks/controller.py"
Cohesion: 0.05
Nodes (17): change(), comment(), create(), task(), tasks(), TaskClientOut, TaskCommentIn, TaskDataIn (+9 more)

### Community 39 - "test_key_values.py"
Cohesion: 0.09
Nodes (7): MemoryKeyValueBuffer, RedisKeyValueBuffer, _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 40 - "clients/controller.py"
Cohesion: 0.13
Nodes (11): audit(), cancel_owner(), change_status(), client_options(), edit_client_image(), invite_owner(), new_owner(), remove_client_image() (+3 more)

### Community 41 - "test_api.py"
Cohesion: 0.08
Nodes (6): refresh_levels(), _error_code(), test_every_write_route_refuses_another_site(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 42 - "documents/controller.py"
Cohesion: 0.16
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 43 - "CapturingMailer"
Cohesion: 0.13
Nodes (22): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited(), _bearer() (+14 more)

### Community 45 - "security.py"
Cohesion: 0.04
Nodes (14): Services, get_services(), audit_service(), dashboard_service(), checklist_item_service(), site_checklist_service(), commission_service(), contract_service() (+6 more)

### Community 46 - "test_reports.py"
Cohesion: 0.12
Nodes (17): _checkouts(), test_report_requests_use_few_connections(), query(), _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait() (+9 more)

### Community 47 - "SavedViewService"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "checklists/controller.py"
Cohesion: 0.15
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistDetailOut, ChecklistMarkIn (+2 more)

### Community 49 - "download"
Cohesion: 0.09
Nodes (5): documents(), download(), upload(), document_service(), DocumentService

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (10): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+2 more)

### Community 51 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 52 - "modules/rewards/controller.py"
Cohesion: 0.09
Nodes (14): metrics(), RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut (+6 more)

### Community 53 - "edit"
Cohesion: 0.10
Nodes (17): API first e chaves de API, Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa (+9 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "avant_core_access_models"
Cohesion: 0.10
Nodes (11): edit(), leave(), options(), remove(), set_permissions(), show(), member_service(), MemberDetailOut (+3 more)

### Community 56 - "CapturingMailer"
Cohesion: 0.14
Nodes (18): CapturingMailer, _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission() (+10 more)

### Community 57 - "ItemsOut"
Cohesion: 0.13
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 58 - "test_account.py"
Cohesion: 0.11
Nodes (8): GoogleFailed, _parse(), challenge(), _claims(), GoogleOAuth, identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 59 - "ClientRewardService"
Cohesion: 0.11
Nodes (13): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+5 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 62 - "SiteChecklistService"
Cohesion: 0.15
Nodes (5): checklists(), months(), summary(), ChecklistMonthOut, SiteChecklistService

### Community 63 - "commissions/controller.py"
Cohesion: 0.05
Nodes (22): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+14 more)

### Community 65 - "install"
Cohesion: 0.19
Nodes (7): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 66 - "InvoiceService"
Cohesion: 0.15
Nodes (6): create_service(), update_service(), invoice_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 67 - "auth/controller.py"
Cohesion: 0.13
Nodes (11): get_cookies(), get_invitation(), auth_service(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn (+3 more)

### Community 68 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "Limiter"
Cohesion: 0.10
Nodes (7): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter()

### Community 70 - "ReportService"
Cohesion: 0.07
Nodes (14): create_from_template(), delete(), export(), export_saved(), pin(), pinned(), query(), query_batch() (+6 more)

### Community 71 - "main.py"
Cohesion: 0.10
Nodes (5): configure_logging(), JsonFormatter, observe(), _route_template(), create_app()

### Community 72 - ".of_detail"
Cohesion: 0.14
Nodes (3): ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 74 - "NetworkService"
Cohesion: 0.19
Nodes (3): options(), NetworkDetailOut, NetworkService

### Community 75 - "networks/service.py"
Cohesion: 0.24
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 76 - "Actor"
Cohesion: 0.11
Nodes (9): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), set_active(), set_icon() (+1 more)

### Community 77 - "test_company_image.py"
Cohesion: 0.10
Nodes (13): _check_jpeg_size(), PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image() (+5 more)

### Community 78 - "networks/controller.py"
Cohesion: 0.18
Nodes (7): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs()

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "client_documents/controller.py"
Cohesion: 0.13
Nodes (7): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentService

### Community 82 - "events.py"
Cohesion: 0.08
Nodes (9): TooManyAttempts, channel(), EventSource, sse(), StreamLimiter, events(), event_service(), EventService (+1 more)

### Community 83 - "test_dashboards.py"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - "test_alerts.py"
Cohesion: 0.11
Nodes (11): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company() (+3 more)

### Community 86 - "sites/controller.py"
Cohesion: 0.17
Nodes (7): classify(), classify_many(), AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.20
Nodes (9): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Imagem da Empresa, Issues, Modelo de dados, Regras, Resumo (+1 more)

### Community 88 - "limits.py"
Cohesion: 0.06
Nodes (17): Network, Segurança e limites, KeyValueBuffer, Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket (+9 more)

### Community 89 - "test_events.py"
Cohesion: 0.18
Nodes (13): client(), engine(), mailer(), _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot() (+5 more)

### Community 91 - "SiteListOut"
Cohesion: 0.13
Nodes (4): create(), index(), site_options(), SiteListOut

### Community 92 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 94 - "google/controller.py"
Cohesion: 0.12
Nodes (6): new_verifier(), google_callback(), google_start(), google_redirects(), google_service(), GoogleRedirects

### Community 96 - "RecordingQueue"
Cohesion: 0.11
Nodes (15): RecordingQueue, _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites() (+7 more)

### Community 97 - "ClientService"
Cohesion: 0.15
Nodes (8): client_teams(), manager_change(), client_service(), ClientMemberOut, ManagerChangeOut, ClientService, CompanyRefOut, RevenueStatusOut

### Community 98 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 123 - "GoogleService"
Cohesion: 0.12
Nodes (3): GoogleUnavailable, GoogleAuth, GoogleService

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "auth/controller.py"
Cohesion: 0.10
Nodes (6): accept(), company_image(), do_logout(), login(), me(), set_active_company()

### Community 129 - "google_status"
Cohesion: 0.12
Nodes (3): google_status(), google_unlink(), GoogleStatusOut

### Community 130 - "AdUnitOut"
Cohesion: 0.14
Nodes (4): ad_units(), link(), unlinked(), AdUnitOut

### Community 131 - "RedisCounter"
Cohesion: 0.13
Nodes (5): RedisCounter, test_redis_limiter(), test_docs_are_closed_in_production(), test_every_response_has_the_security_headers(), test_redis_down_is_a_503_not_a_500()

### Community 132 - "contracts/controller.py"
Cohesion: 0.06
Nodes (22): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, contract(), contract_networks() (+14 more)

### Community 138 - "invoices/service.py"
Cohesion: 0.10
Nodes (7): dollars(), AvailableMonthOut, InvoiceItemOut, InvoiceSummaryOut, ReturnedOut, ReturnIn, ServiceItemIn

### Community 142 - "OwnerInvitationOut"
Cohesion: 0.23
Nodes (3): owner_invitations(), OwnerInvitationOut, owner_invitation_out()

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.38
Nodes (11): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+3 more)

### Community 146 - "get"
Cohesion: 0.10
Nodes (15): add_item(), available_months(), delete(), delete_service(), get(), issue(), mine(), pay() (+7 more)

### Community 147 - "_csrf"
Cohesion: 0.07
Nodes (38): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+30 more)

### Community 148 - "UnitOfWorkFactory"
Cohesion: 0.07
Nodes (3): UnitOfWorkFactory, reward_cache_key(), page_out()

### Community 149 - "SiteService"
Cohesion: 0.22
Nodes (3): delete(), members(), SiteMemberOut

### Community 150 - ".uow"
Cohesion: 0.05
Nodes (6): create(), duplicate(), update(), SavedReportIn, SavedReportOut, ReportService

### Community 152 - "rewards/http.py"
Cohesion: 0.18
Nodes (3): csv_response(), lead_filter(), period()

### Community 155 - "health/controller.py"
Cohesion: 0.14
Nodes (4): health(), ready(), health_service(), HealthService

### Community 158 - "test_rewards_panel"
Cohesion: 0.29
Nodes (5): _body(), _cache(), _site(), test_rewards_internal(), test_rewards_panel()

### Community 160 - "company/controller.py"
Cohesion: 0.06
Nodes (13): edit(), edit_fiscal(), edit_image(), fiscal(), image(), remove_image(), show(), company_service() (+5 more)

### Community 163 - "mcm/controller.py"
Cohesion: 0.08
Nodes (8): confirm_network(), register_network(), reject_network(), unassigned_networks(), ClientNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 167 - "people/service.py"
Cohesion: 0.07
Nodes (17): Modelo de dados, Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação (+9 more)

### Community 175 - "_member_client"
Cohesion: 0.10
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 177 - "PayeeDetailsOut"
Cohesion: 0.19
Nodes (3): save_payment_details(), PayeeDetailsOut, FiscalDataOut

### Community 178 - "UserOut"
Cohesion: 0.08
Nodes (9): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService (+1 more)

### Community 180 - "results/dto.py"
Cohesion: 0.05
Nodes (12): results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut (+4 more)

### Community 182 - "SiteService"
Cohesion: 0.19
Nodes (4): show(), site_service(), SiteDetailOut, SiteService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2004 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **101 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `MemberOut`, `roles/controller.py`, `.uow`, `AlertService`, `contracts/controller.py`, `PageOut`, `GamToolService`, `RewardCache`, `schedules/controller.py`, `invoices/service.py`, `.trusted_uow`, `GroupService`, `inventory/dto.py`, `api_keys/controller.py`, `PageOut`, `custom_metrics/controller.py`, `.uow`, `dashboard_templates/controller.py`, `mfa/controller.py`, `ReportService`, `company/controller.py`, `mcm/controller.py`, `tasks/controller.py`, `TaskQueue`, `people/service.py`, `documents/controller.py`, `SavedViewService`, `download`, `client_notes/controller.py`, `UserOut`, `results/dto.py`, `currencies/controller.py`, `avant_core_access_models`, `SiteService`, `.__init__`, `ItemsOut`, `account/controller.py`, `.__init__`, `SiteChecklistService`, `commissions/controller.py`, `InvoiceService`, `auth/controller.py`, `Limiter`, `.__init__`, `.__init__`, `.__init__`, `networks/service.py`, `.__init__`, `NetworkService`, `costs/controller.py`, `client_documents/controller.py`, `goals/service.py`, `sites/controller.py`, `GoalService`, `.__init__`, `ClientService`, `GoogleService`?**
  _High betweenness centrality (0.116) - this node is a cross-community bridge._
- **Are the 116 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 116 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `MemberOut` be split into smaller, more focused modules?**
  _Cohesion score 0.12698412698412698 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `client_notes/controller.py` to `MemberOut`, `roles/controller.py`, `.uow`, `AlertService`, `contracts/controller.py`, `PageOut`, `GamToolService`, `GoalTemplateOut`, `schedules/controller.py`, `invoices/service.py`, `AdUnitOut`, `.trusted_uow`, `GroupService`, `OwnerInvitationOut`, `inventory/dto.py`, `api_keys/controller.py`, `PageOut`, `get`, `.of`, `UnitOfWorkFactory`, `ReportService`, `RewardService`, `clients`, `mcm/controller.py`, `require_staff`, `tasks/controller.py`, `people/service.py`, `clients/controller.py`, `checklists/controller.py`, `results/dto.py`, `modules/rewards/controller.py`, `SiteService`, `avant_core_access_models`, `ClientRewardService`, `SiteChecklistService`, `InvoiceService`, `NetworkService`, `networks/service.py`, `Actor`, `networks/controller.py`, `costs/controller.py`, `goals/service.py`, `Actor`, `sites/controller.py`, `SiteListOut`, `GoalService`, `ClientService`, `goals/controller.py`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07581453634085213 - nodes in this community are weakly interconnected._