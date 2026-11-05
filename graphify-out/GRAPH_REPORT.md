# Graph Report - avant-api  (2026-11-05)

## Corpus Check
- 303 files · ~93,372 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4108 nodes · 11264 edges · 210 communities (105 shown, 105 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1873 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0dacf0f7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- datetime
- test_alerts.py
- roles/controller.py
- DashboardService
- Actor
- PageOut
- GamToolService
- test_account.py
- steps
- _month
- Avant: models do MVP
- test_gam_tools.py
- InvoiceService
- .uow
- router.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- invitations/controller.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- Settings
- goals/controller.py
- verify
- image_response
- clean_code.py
- _onboard_owner
- mfa/controller.py
- Avant: repositório e plano do MVP
- reports/service.py
- router.py
- CapturingMailer
- session-start.sh
- avant-api
- require_staff
- tasks/controller.py
- networks/controller.py
- networks/service.py
- clients/controller.py
- test_company_image.py
- documents/controller.py
- _onboard_owner
- checklists
- security.py
- uuid
- networks/service.py
- ChecklistDetailOut
- download
- Services
- _month
- .of
- edit
- currencies/controller.py
- members/controller.py
- test_key_values.py
- clients
- key_values/service.py
- conftest.py
- account/controller.py
- client_documents/controller.py
- Actor
- commissions/controller.py
- AuthService
- install
- invoices/controller.py
- ItemsOut
- export.py
- limits.py
- export_saved
- UnitOfWorkFactory
- avant-api
- NetworkService
- create_app
- Actor
- .of
- image
- CommissionService
- test_events.py
- uuid
- ClientService
- avant_core_access_models
- AdUnitOut
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- limits.py
- SiteListOut
- get
- google/controller.py
- capped
- _csrf
- UserOut
- GoalService
- internal/results/controller.py
- updates
- accept
- TaskQueue
- ProfileService
- ports.py
- users
- enqueue_sync
- checklists/controller.py
- typing
- health/controller.py
- contracts/controller.py
- Arquitetura do MVP do Avant
- test_mfa.py
- shared/dto.py
- InvoiceService
- time
- InvoiceServiceOut
- SiteService
- .uow
- clients
- .save_payee_details
- image
- company/controller.py
- ClientOut
- ExportsBusy
- mcm/service.py
- .change_password
- team
- UserOut
- verify
- document_response
- person
- _member_client
- SiteDetailOut
- .of
- edit_image
- Actor
- .assign
- page_out
- TooManyAttempts
- .preview_invitation
- Settings
- manager_change
- .build
- is_exempt
- edit_image
- commissions/dto.py

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 168 edges
2. `_csrf()` - 150 edges
3. `_onboard_owner()` - 150 edges
4. `PageOut` - 145 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 123 edges
8. `ReportService` - 79 edges
9. `_staff()` - 67 edges
10. `page_out()` - 59 edges

## Surprising Connections (you probably didn't know these)
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py
- `Pipeline` --references--> `main()`  [INFERRED]
  docs/decisoes/07-repositorios-e-plano.md → scripts/clean_code.py
- `Primeira semana (23/10 a 02/11)` --references--> `main()`  [INFERRED]
  docs/decisoes/07-repositorios-e-plano.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (210 total, 105 thin omitted)

### Community 0 - "datetime"
Cohesion: 0.08
Nodes (13): refresh_levels(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone() (+5 more)

### Community 1 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (26): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+18 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "PageOut"
Cohesion: 0.12
Nodes (5): index(), audit_service(), AuditService, AuditOut, PageOut

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (20): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+12 more)

### Community 7 - "test_account.py"
Cohesion: 0.18
Nodes (9): FakeGoogle, _google_round(), _jwt(), _login(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_id_token_claims() (+1 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (32): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+24 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (21): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+13 more)

### Community 11 - "test_gam_tools.py"
Cohesion: 0.27
Nodes (8): _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads()

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "router.py"
Cohesion: 0.13
Nodes (7): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "invitations/controller.py"
Cohesion: 0.11
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService, InvitationOut

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
Cohesion: 0.13
Nodes (6): engine_options(), _mailer(), Settings, _settings(), test_every_connection_has_a_statement_and_idle_timeout(), test_pool_is_bounded_and_waits_little()

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "image_response"
Cohesion: 0.17
Nodes (3): image(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 27 - "_onboard_owner"
Cohesion: 0.13
Nodes (16): _checkouts(), test_report_requests_use_few_connections(), _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics() (+8 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (11): get_cookies(), auth_service(), confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn (+3 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "reports/service.py"
Cohesion: 0.05
Nodes (32): catalog(), delete(), index(), pin(), query(), query_batch(), show(), templates() (+24 more)

### Community 31 - "router.py"
Cohesion: 0.13
Nodes (7): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 32 - "CapturingMailer"
Cohesion: 0.21
Nodes (10): CapturingMailer, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_option_lists_keep_the_permissions() (+2 more)

### Community 36 - "require_staff"
Cohesion: 0.08
Nodes (16): api_key_actor(), bearer_token(), check_tab_company(), get_actor(), get_session_actor(), get_session_auth(), known_companies(), optional_auth() (+8 more)

### Community 37 - "tasks/controller.py"
Cohesion: 0.05
Nodes (18): change(), comment(), create(), task(), tasks(), support_task_service(), TaskClientOut, TaskCommentIn (+10 more)

### Community 38 - "networks/controller.py"
Cohesion: 0.21
Nodes (5): disconnect(), service_account(), show(), sync(), sync_runs()

### Community 39 - "networks/service.py"
Cohesion: 0.20
Nodes (4): network_service(), NetworkIn, ServiceAccountOut, SyncRunOut

### Community 40 - "clients/controller.py"
Cohesion: 0.14
Nodes (13): client_teams(), new_owner(), ClientIn, ClientMemberOut, ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+5 more)

### Community 41 - "test_company_image.py"
Cohesion: 0.09
Nodes (12): _check_jpeg_size(), _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client() (+4 more)

### Community 42 - "documents/controller.py"
Cohesion: 0.16
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "_onboard_owner"
Cohesion: 0.16
Nodes (20): _error_code(), _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_deployed_cookies_use_the_host_prefix(), test_every_write_route_refuses_another_site(), test_health_and_metrics(), test_owner_onboarding_and_login() (+12 more)

### Community 44 - "checklists"
Cohesion: 0.14
Nodes (3): checklists(), months(), summary()

### Community 45 - "security.py"
Cohesion: 0.04
Nodes (20): Services, CsrfFailed, EventSource, PillowImageProcessor, check_csrf(), check_fetch_site(), get_auth(), get_services() (+12 more)

### Community 46 - "uuid"
Cohesion: 0.11
Nodes (22): test_change_password_and_sessions(), test_busy_export_answers_503_with_retry_after(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run(), _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast() (+14 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "ChecklistDetailOut"
Cohesion: 0.10
Nodes (8): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistDetailOut, SiteChecklistService

### Community 49 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "_month"
Cohesion: 0.18
Nodes (3): mine(), _month(), MyCommissionsOut

### Community 52 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.15
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (13): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+5 more)

### Community 56 - "test_key_values.py"
Cohesion: 0.10
Nodes (7): MemoryKeyValueBuffer, RedisKeyValueBuffer, _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 57 - "clients"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "key_values/service.py"
Cohesion: 0.11
Nodes (7): Network, Segurança e limites, KeyValueBuffer, receive(), KeyValueIn, network_code(), receive_key_values()

### Community 59 - "conftest.py"
Cohesion: 0.12
Nodes (10): client(), engine(), mailer(), Sent, _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys() (+2 more)

### Community 60 - "account/controller.py"
Cohesion: 0.08
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "client_documents/controller.py"
Cohesion: 0.15
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 63 - "commissions/controller.py"
Cohesion: 0.12
Nodes (8): adjust(), create_rule(), delete_rule(), rules(), set_settings(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 65 - "install"
Cohesion: 0.25
Nodes (7): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 66 - "invoices/controller.py"
Cohesion: 0.20
Nodes (11): update_item(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut (+3 more)

### Community 67 - "ItemsOut"
Cohesion: 0.16
Nodes (7): classify(), classify_many(), MemberSitesIn, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "limits.py"
Cohesion: 0.10
Nodes (8): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 74 - "NetworkService"
Cohesion: 0.17
Nodes (4): connect(), index(), NetworkDetailOut, NetworkService

### Community 75 - "create_app"
Cohesion: 0.11
Nodes (6): RedisCounter, create_app(), health(), test_docs_are_closed_in_production(), test_every_response_has_the_security_headers(), test_redis_down_is_a_503_not_a_500()

### Community 77 - "Actor"
Cohesion: 0.12
Nodes (7): audit(), cancel_owner(), change_status(), client_image(), client_options(), edit_client_image(), remove_client_image()

### Community 79 - "image"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 81 - "CommissionService"
Cohesion: 0.15
Nodes (4): settings(), commission_service(), CommissionSettingsOut, CommissionService

### Community 82 - "test_events.py"
Cohesion: 0.12
Nodes (13): channel(), _parse(), sse(), _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot() (+5 more)

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - "ClientService"
Cohesion: 0.18
Nodes (6): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, ClientService, owner_invitation_out()

### Community 85 - "avant_core_access_models"
Cohesion: 0.14
Nodes (4): show(), result_service(), ResultsOut, ResultService

### Community 86 - "AdUnitOut"
Cohesion: 0.18
Nodes (4): ad_units(), link(), AdUnitOut, AdUnitPatchIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.26
Nodes (7): AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut, MeOut

### Community 89 - "limits.py"
Cohesion: 0.12
Nodes (8): Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 92 - "get"
Cohesion: 0.09
Nodes (14): add_item(), available_months(), create_service(), delete(), delete_service(), get(), issue(), pay() (+6 more)

### Community 94 - "google/controller.py"
Cohesion: 0.03
Nodes (23): _google(), CompanyChanged, GoogleFailed, GoogleUnavailable, NoActiveCompany, QueryTooHeavy, RateLimited, challenge() (+15 more)

### Community 96 - "_csrf"
Cohesion: 0.06
Nodes (38): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+30 more)

### Community 97 - "UserOut"
Cohesion: 0.17
Nodes (3): PersonOut, person_out(), UserOut

### Community 98 - "GoalService"
Cohesion: 0.05
Nodes (19): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+11 more)

### Community 102 - "internal/results/controller.py"
Cohesion: 0.14
Nodes (3): results(), client_result_service(), ClientResultService

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "accept"
Cohesion: 0.21
Nodes (5): accept(), company_image(), do_logout(), login(), set_active_company()

### Community 130 - "ProfileService"
Cohesion: 0.24
Nodes (4): edit_appearance(), AppearanceIn, AppearanceOut, ProfileService

### Community 135 - "users"
Cohesion: 0.25
Nodes (7): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação

### Community 137 - "checklists/controller.py"
Cohesion: 0.17
Nodes (9): site_checklist_service(), ChecklistMarkIn, ChecklistMonthOut, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut (+1 more)

### Community 139 - "health/controller.py"
Cohesion: 0.17
Nodes (3): ready(), health_service(), HealthService

### Community 142 - "contracts/controller.py"
Cohesion: 0.06
Nodes (25): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+17 more)

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.14
Nodes (16): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+8 more)

### Community 146 - "InvoiceService"
Cohesion: 0.20
Nodes (4): mine(), service_options(), invoice_service(), InvoiceService

### Community 149 - "SiteService"
Cohesion: 0.16
Nodes (3): members(), SiteMemberOut, SiteService

### Community 150 - ".uow"
Cohesion: 0.05
Nodes (7): create(), create_from_template(), duplicate(), pinned(), run(), SavedReportOut, ReportService

### Community 160 - "company/controller.py"
Cohesion: 0.20
Nodes (8): edit_fiscal(), show(), company_service(), CompanyDetailOut, CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 161 - "ClientOut"
Cohesion: 0.11
Nodes (4): clients(), edit_client(), register_client(), ClientOut

### Community 163 - "mcm/service.py"
Cohesion: 0.14
Nodes (6): assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 167 - "UserOut"
Cohesion: 0.12
Nodes (7): Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PeopleService

### Community 175 - "_member_client"
Cohesion: 0.09
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 180 - "Actor"
Cohesion: 0.16
Nodes (6): delete(), index(), show(), site_options(), sites_of_member(), unlinked()

### Community 182 - ".assign"
Cohesion: 0.25
Nodes (5): Atribuição de sites, GAM, Networks, Sites e ad units, assign_sites()

### Community 184 - "TooManyAttempts"
Cohesion: 0.14
Nodes (4): TooManyAttempts, StreamLimiter, events(), test_stream_limiter_caps_each_person_and_the_process()

### Community 192 - ".build"
Cohesion: 0.06
Nodes (6): NoEvents, MemoryCounter, CeleryQueue, RecordingQueue, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 203 - "edit_image"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 216 - "commissions/dto.py"
Cohesion: 0.17
Nodes (5): AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, dollars(), MonthIn

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1868 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **105 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `TaskQueue`, `ProfileService`, `DashboardService`, `ports.py`, `Actor`, `PageOut`, `.__init__`, `GamToolService`, `checklists/controller.py`, `.__init__`, `roles/controller.py`, `InvoiceService`, `.uow`, `contracts/controller.py`, `router.py`, `api_keys/controller.py`, `invitations/controller.py`, `InvoiceService`, `custom_metrics/controller.py`, `SiteService`, `.uow`, `goals/controller.py`, `mfa/controller.py`, `reports/service.py`, `router.py`, `company/controller.py`, `mcm/service.py`, `tasks/controller.py`, `UserOut`, `clients/controller.py`, `networks/service.py`, `documents/controller.py`, `_month`, `networks/service.py`, `ChecklistDetailOut`, `Services`, `currencies/controller.py`, `members/controller.py`, `.__init__`, `clients`, `account/controller.py`, `client_documents/controller.py`, `.__init__`, `AuthService`, `invoices/controller.py`, `ItemsOut`, `.__init__`, `NetworkService`, `.__init__`, `image`, `CommissionService`, `ClientService`, `avant_core_access_models`, `auth/controller.py`, `google/controller.py`, `UserOut`, `GoalService`, `internal/results/controller.py`?**
  _High betweenness centrality (0.164) - this node is a cross-community bridge._
- **Are the 127 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 127 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `datetime` be split into smaller, more focused modules?**
  _Cohesion score 0.08246225319396051 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `roles/controller.py`, `DashboardService`, `Actor`, `ports.py`, `GamToolService`, `checklists/controller.py`, `_month`, `InvoiceService`, `.uow`, `contracts/controller.py`, `router.py`, `api_keys/controller.py`, `invitations/controller.py`, `InvoiceService`, `shared/dto.py`, `InvoiceServiceOut`, `SiteService`, `reports/service.py`, `router.py`, `ClientOut`, `mcm/service.py`, `tasks/controller.py`, `networks/controller.py`, `UserOut`, `clients/controller.py`, `networks/service.py`, `checklists`, `ChecklistDetailOut`, `Services`, `Actor`, `members/controller.py`, `page_out`, `Actor`, `invoices/controller.py`, `ItemsOut`, `NetworkService`, `Actor`, `image`, `ClientService`, `get`, `UserOut`, `GoalService`, `internal/results/controller.py`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07792207792207792 - nodes in this community are weakly interconnected._