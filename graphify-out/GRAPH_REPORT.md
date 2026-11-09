# Graph Report - avant-api  (2026-11-09)

## Corpus Check
- 324 files · ~101,062 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4484 nodes · 12268 edges · 223 communities (117 shown, 106 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1979 edges (avg confidence: 0.91)
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
- clients/controller.py
- CustomMetricService
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- Settings
- dashboard_templates/controller.py
- invoice_pdf.py
- image_response
- clean_code.py
- delete_template
- mfa/controller.py
- Avant: repositório e plano do MVP
- ReportService
- test_api.py
- modules/rewards/controller.py
- session-start.sh
- avant-api
- require_staff
- BaseModel
- TaskQueue
- clients/controller.py
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
- CapturingMailer
- ItemsOut
- test_account.py
- ClientRewardService
- account/controller.py
- client_documents/controller.py
- checklists
- commissions/controller.py
- SessionCookies
- install
- company/controller.py
- AuthService
- export.py
- Limiter
- .export
- main.py
- .of_detail
- avant-api
- NetworkService
- networks/service.py
- SupportTaskService
- test_company_image.py
- networks/controller.py
- costs/controller.py
- ClientDocumentService
- events.py
- test_dashboards.py
- test_alerts.py
- Actor
- sites/controller.py
- Avant: grupos na Empresa e imagem da Empresa
- key_values/controller.py
- tasks/controller.py
- SiteListOut
- GoalService
- errors.py
- RecordingQueue
- contracts/controller.py
- goals/controller.py
- Avant: conexão com o GAM
- updates
- auth/controller.py
- contracts/dto.py
- AdUnitOut
- limits.py
- ContractOut
- modules/rewards/service.py
- shared/dto.py
- SiteOut
- dollars
- .of
- Arquitetura do MVP do Avant
- test_mfa.py
- custom_metrics/controller.py
- get
- _csrf
- ContractService
- SiteService
- .uow
- test_sites.py
- test_key_values.py
- tasks
- custom_metrics/service.py
- CompanyService
- clients
- Actor
- mcm/controller.py
- image
- download
- people/service.py
- ClientService
- document_response
- .run_guarded
- conftest.py
- decimal
- UUID
- UserOut
- results/dto.py
- SiteService
- .of
- get
- available_months
- UnitOfWorkFactory
- _out
- avant-api
- TaskPatchIn
- classify
- is_exempt

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 175 edges
2. `_csrf()` - 157 edges
3. `_onboard_owner()` - 156 edges
4. `PageOut` - 155 edges
5. `get()` - 139 edges
6. `UnitOfWorkFactory` - 131 edges
7. `Services` - 121 edges
8. `ReportService` - 79 edges
9. `_staff()` - 70 edges
10. `page_out()` - 65 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/modules/internal/people/controller.py
- `Estrutura` --references--> `Services`  [INFERRED]
  README.md → src/avant_api/app/container.py
- `O que já tem` --references--> `edit()`  [INFERRED]
  README.md → src/avant_api/modules/company/controller.py

## Import Cycles
- None detected.

## Communities (223 total, 106 thin omitted)

### Community 0 - "reward_public/service.py"
Cohesion: 0.07
Nodes (15): Bucket, BucketRule, RewardBuffer, client_address(), cors(), events(), icon(), leads() (+7 more)

### Community 1 - "MemberOut"
Cohesion: 0.09
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.05
Nodes (25): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+17 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "_report"
Cohesion: 0.11
Nodes (27): _onboard_owner(), _checkouts(), test_report_requests_use_few_connections(), test_busy_export_answers_503_with_retry_after(), test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages() (+19 more)

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (20): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+12 more)

### Community 7 - "GoalTemplateOut"
Cohesion: 0.14
Nodes (4): create_template(), template_options(), GoalTemplateIn, GoalTemplateOut

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: conexão com o GAM"
Cohesion: 0.10
Nodes (20): Acesso, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade (+12 more)

### Community 11 - "DashboardTemplateOut"
Cohesion: 0.13
Nodes (3): templates(), DashboardTemplateOut, LabelOut

### Community 12 - ".trusted_uow"
Cohesion: 0.08
Nodes (6): create_service(), services(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.11
Nodes (9): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, page_out() (+1 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.11
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.11
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "clients/controller.py"
Cohesion: 0.11
Nodes (16): client_options(), invite_owner(), new_owner(), register_client(), ClientDetailOut, ClientIn, ClientOptionOut, ClientOut (+8 more)

### Community 19 - "CustomMetricService"
Cohesion: 0.16
Nodes (4): create(), CustomMetricIn, CustomMetricOut, CustomMetricService

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "Settings"
Cohesion: 0.05
Nodes (14): engine_options(), _google(), _mailer(), NoEvents, MemoryRewardCache, Settings, CeleryQueue, test_closing_deployed_cookies_keeps_them_secure() (+6 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), verify(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "ReportService"
Cohesion: 0.06
Nodes (27): alert_service(), catalog(), index(), query(), query_batch(), templates(), report_service(), CustomCatalogMetricOut (+19 more)

### Community 31 - "test_api.py"
Cohesion: 0.15
Nodes (13): Sent, _error_code(), _owner_invite(), test_csrf_is_required_for_writes(), test_every_write_route_refuses_another_site(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit() (+5 more)

### Community 32 - "modules/rewards/controller.py"
Cohesion: 0.06
Nodes (16): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+8 more)

### Community 36 - "require_staff"
Cohesion: 0.07
Nodes (24): CompanyChanged, CsrfFailed, NoActiveCompany, RateLimited, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site() (+16 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 40 - "clients/controller.py"
Cohesion: 0.11
Nodes (9): audit(), cancel_owner(), change_status(), client_image(), edit_client(), edit_client_image(), owner_invitations(), remove_client_image() (+1 more)

### Community 41 - "datetime"
Cohesion: 0.08
Nodes (13): refresh_levels(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone() (+5 more)

### Community 42 - "documents/controller.py"
Cohesion: 0.15
Nodes (4): document_service(), DocumentService, document_upload(), DocumentsOut

### Community 43 - "test_account.py"
Cohesion: 0.38
Nodes (7): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 45 - "Services"
Cohesion: 0.03
Nodes (12): Services, KeyValueBuffer, MemoryKeyValueBuffer, RedisKeyValueBuffer, MemoryRewardBuffer, RedisRewardBuffer, get_services(), checklist_item_service() (+4 more)

### Community 46 - "test_reports.py"
Cohesion: 0.23
Nodes (14): _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas() (+6 more)

### Community 47 - "SavedViewService"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "checklists/controller.py"
Cohesion: 0.12
Nodes (15): add_note(), check(), checklist(), edit_note(), mark(), site_checklist_service(), ChecklistDetailOut, ChecklistMarkIn (+7 more)

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
Cohesion: 0.08
Nodes (19): PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicStyleOut, RewardEventIn (+11 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "avant_core_access_models"
Cohesion: 0.06
Nodes (16): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+8 more)

### Community 56 - "CapturingMailer"
Cohesion: 0.14
Nodes (13): CapturingMailer, client(), engine(), mailer(), query(), _clients_viewer(), _queue(), _second_owner() (+5 more)

### Community 57 - "ItemsOut"
Cohesion: 0.12
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 58 - "test_account.py"
Cohesion: 0.09
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 59 - "ClientRewardService"
Cohesion: 0.07
Nodes (14): create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+6 more)

### Community 60 - "account/controller.py"
Cohesion: 0.08
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "client_documents/controller.py"
Cohesion: 0.22
Nodes (5): client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, DocumentOut

### Community 62 - "checklists"
Cohesion: 0.20
Nodes (4): checklists(), delete_note(), months(), summary()

### Community 63 - "commissions/controller.py"
Cohesion: 0.06
Nodes (22): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+14 more)

### Community 65 - "install"
Cohesion: 0.25
Nodes (7): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 66 - "company/controller.py"
Cohesion: 0.17
Nodes (5): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, image_url()

### Community 67 - "AuthService"
Cohesion: 0.08
Nodes (4): get_invitation(), auth_service(), InvitationPreviewOut, AuthService

### Community 68 - "export.py"
Cohesion: 0.10
Nodes (10): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+2 more)

### Community 69 - "Limiter"
Cohesion: 0.11
Nodes (8): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - ".export"
Cohesion: 0.09
Nodes (6): ExportsBusy, export(), export_saved(), export_slot(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 71 - "main.py"
Cohesion: 0.12
Nodes (3): JsonFormatter, observe(), _route_template()

### Community 74 - "NetworkService"
Cohesion: 0.15
Nodes (5): connect(), options(), NetworkDetailOut, NetworkIn, NetworkService

### Community 76 - "SupportTaskService"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 77 - "test_company_image.py"
Cohesion: 0.07
Nodes (22): _check_jpeg_size(), PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image() (+14 more)

### Community 78 - "networks/controller.py"
Cohesion: 0.16
Nodes (7): disconnect(), index(), service_account(), show(), sync(), sync_runs(), network_service()

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 82 - "events.py"
Cohesion: 0.05
Nodes (20): channel(), EventSource, _parse(), RedisEvents, sse(), StreamLimiter, events(), event_service() (+12 more)

### Community 83 - "test_dashboards.py"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 85 - "Actor"
Cohesion: 0.09
Nodes (4): ad_units(), ClientRewardService, RewardAdUnitGroupOut, RewardClientOut

### Community 86 - "sites/controller.py"
Cohesion: 0.19
Nodes (7): site_service(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "key_values/controller.py"
Cohesion: 0.13
Nodes (5): cors(), preflight(), receive(), KeyValueIn, receive_key_values()

### Community 89 - "tasks/controller.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 91 - "SiteListOut"
Cohesion: 0.11
Nodes (5): create(), index(), site_options(), SiteListOut, capped()

### Community 92 - "GoalService"
Cohesion: 0.23
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 94 - "errors.py"
Cohesion: 0.05
Nodes (13): GoogleUnavailable, QueryTooHeavy, GoogleAuth, new_verifier(), get_cookies(), google_start(), google_status(), google_unlink() (+5 more)

### Community 96 - "RecordingQueue"
Cohesion: 0.23
Nodes (9): RecordingQueue, _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites() (+1 more)

### Community 97 - "contracts/controller.py"
Cohesion: 0.17
Nodes (6): contract(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract()

### Community 98 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 123 - "Avant: conexão com o GAM"
Cohesion: 0.11
Nodes (16): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment, Avant: conexão com o GAM, Caminho conta de serviço (+8 more)

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "auth/controller.py"
Cohesion: 0.10
Nodes (13): accept(), company_image(), do_logout(), login(), me(), set_active_company(), AcceptInvitationIn, ActiveCompanyIn (+5 more)

### Community 129 - "contracts/dto.py"
Cohesion: 0.15
Nodes (7): _contract_fields(), ContractIn, ContractNetworkRefOut, ContractSummaryOut, _network_ref(), ClientRefOut, ContractClientRefOut

### Community 131 - "limits.py"
Cohesion: 0.06
Nodes (9): TooManyAttempts, BucketResult, MemoryBucket, MemoryCounter, RedisBucket, RedisCounter, _exercise(), test_memory_bucket() (+1 more)

### Community 132 - "ContractOut"
Cohesion: 0.17
Nodes (3): O que já tem, ContractOut, ContractPatchIn

### Community 133 - "modules/rewards/service.py"
Cohesion: 0.10
Nodes (3): reward_cache_key(), RewardCache, forget_pages()

### Community 134 - "shared/dto.py"
Cohesion: 0.08
Nodes (3): index(), audit_service(), AuditOut

### Community 136 - "SiteOut"
Cohesion: 0.15
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 142 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.21
Nodes (13): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+5 more)

### Community 145 - "custom_metrics/controller.py"
Cohesion: 0.17
Nodes (4): delete(), index(), update(), custom_metric_service()

### Community 146 - "get"
Cohesion: 0.08
Nodes (23): add_item(), create(), delete(), delete_service(), issue(), pay(), payment_details(), pdf() (+15 more)

### Community 147 - "_csrf"
Cohesion: 0.07
Nodes (38): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+30 more)

### Community 148 - "ContractService"
Cohesion: 0.21
Nodes (4): contract_networks(), contract_service(), ContractNetworkOut, ContractService

### Community 149 - "SiteService"
Cohesion: 0.33
Nodes (3): members(), SiteMemberOut, SiteService

### Community 150 - ".uow"
Cohesion: 0.05
Nodes (12): create(), create_from_template(), delete(), duplicate(), pin(), pinned(), run(), show() (+4 more)

### Community 152 - "test_sites.py"
Cohesion: 0.25
Nodes (5): _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search(), test_site_category_and_responsible(), test_sites_and_assignment()

### Community 153 - "test_key_values.py"
Cohesion: 0.11
Nodes (6): RedisRewardCache, _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 155 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 158 - "custom_metrics/service.py"
Cohesion: 0.24
Nodes (3): check(), CustomMetricCheckIn, CustomMetricCheckOut

### Community 160 - "CompanyService"
Cohesion: 0.16
Nodes (5): remove_image(), show(), company_service(), CompanyDetailOut, CompanyService

### Community 162 - "Actor"
Cohesion: 0.22
Nodes (3): role_goals(), templates(), RoleGoalOut

### Community 163 - "mcm/controller.py"
Cohesion: 0.11
Nodes (8): confirm_network(), register_network(), reject_network(), unassigned_networks(), ClientNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 164 - "image"
Cohesion: 0.15
Nodes (3): edit_image(), fiscal(), image()

### Community 165 - "download"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 167 - "people/service.py"
Cohesion: 0.10
Nodes (9): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+1 more)

### Community 168 - "ClientService"
Cohesion: 0.08
Nodes (6): client(), client_teams(), manager_change(), ClientMemberOut, ClientService, owner_invitation_out()

### Community 175 - "conftest.py"
Cohesion: 0.07
Nodes (20): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit(), _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company() (+12 more)

### Community 177 - "UUID"
Cohesion: 0.22
Nodes (3): assign_sites(), delete(), unlinked()

### Community 178 - "UserOut"
Cohesion: 0.07
Nodes (9): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService (+1 more)

### Community 180 - "results/dto.py"
Cohesion: 0.04
Nodes (17): configure_logging(), create_app(), health(), ready(), health_service(), HealthService, results(), client_result_service() (+9 more)

### Community 184 - "get"
Cohesion: 0.15
Nodes (4): metrics(), get(), mine(), service_options()

### Community 191 - "avant-api"
Cohesion: 0.33
Nodes (5): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2049 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **106 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `auth/controller.py`, `MemberOut`, `reward_public/service.py`, `.uow`, `AlertService`, `modules/rewards/service.py`, `shared/dto.py`, `GamToolService`, `roles/controller.py`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `inventory/dto.py`, `api_keys/controller.py`, `PageOut`, `clients/controller.py`, `CustomMetricService`, `ContractService`, `get`, `.uow`, `dashboard_templates/controller.py`, `SiteService`, `mfa/controller.py`, `custom_metrics/service.py`, `ReportService`, `CompanyService`, `TaskQueue`, `people/service.py`, `ClientService`, `documents/controller.py`, `SavedViewService`, `checklists/controller.py`, `client_notes/controller.py`, `UserOut`, `results/dto.py`, `currencies/controller.py`, `avant_core_access_models`, `.__init__`, `ItemsOut`, `account/controller.py`, `client_documents/controller.py`, `commissions/controller.py`, `company/controller.py`, `AuthService`, `.__init__`, `NetworkService`, `networks/service.py`, `SupportTaskService`, `costs/controller.py`, `ClientDocumentService`, `goals/service.py`, `sites/controller.py`, `.__init__`, `tasks/controller.py`, `GoalService`, `errors.py`?**
  _High betweenness centrality (0.128) - this node is a cross-community bridge._
- **Are the 116 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 116 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `reward_public/service.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07474600870827286 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `inventory/dto.py` to `MemberOut`, `roles/controller.py`, `.uow`, `AlertService`, `ContractOut`, `shared/dto.py`, `GamToolService`, `GoalTemplateOut`, `modules/rewards/service.py`, `schedules/controller.py`, `SiteOut`, `.trusted_uow`, `GroupService`, `api_keys/controller.py`, `PageOut`, `clients/controller.py`, `get`, `ContractService`, `SiteService`, `tasks`, `ReportService`, `modules/rewards/controller.py`, `clients`, `Actor`, `mcm/controller.py`, `people/service.py`, `clients/controller.py`, `ClientService`, `Actor`, `checklists/controller.py`, `UUID`, `client_notes/controller.py`, `results/dto.py`, `avant_core_access_models`, `get`, `ClientRewardService`, `UnitOfWorkFactory`, `checklists`, `NetworkService`, `networks/service.py`, `SupportTaskService`, `networks/controller.py`, `costs/controller.py`, `goals/service.py`, `Actor`, `sites/controller.py`, `tasks/controller.py`, `SiteListOut`, `GoalService`, `contracts/controller.py`, `goals/controller.py`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Are the 54 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 54 INFERRED edges - model-reasoned connections that need verification._
- **Should `MemberOut` be split into smaller, more focused modules?**
  _Cohesion score 0.0946969696969697 - nodes in this community are weakly interconnected._