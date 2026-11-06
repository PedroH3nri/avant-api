# Graph Report - avant-api  (2026-11-06)

## Corpus Check
- 303 files · ~93,461 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4109 nodes · 11270 edges · 183 communities (102 shown, 81 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1874 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `413480b9`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- datetime
- avant_core_access_models
- roles/controller.py
- DashboardService
- AlertService
- require_staff
- .save_rule
- GoalService
- steps
- schedules/controller.py
- Avant: models do MVP
- test_api.py
- .trusted_uow
- GroupService
- inventory/controller.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- InvitationOut
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- company/controller.py
- dashboard_templates/controller.py
- invoice_pdf.py
- test_report_export.py
- clean_code.py
- GoalTemplateIn
- mfa/controller.py
- Avant: repositório e plano do MVP
- reports/service.py
- events.py
- test_sites.py
- session-start.sh
- avant-api
- require
- BaseModel
- export.py
- ItemsOut
- CompanyService
- .of
- errors.py
- SiteChecklistService
- security.py
- AuthService
- views/controller.py
- test_mfa.py
- router.py
- client_notes/controller.py
- mine
- profile/controller.py
- edit
- currencies/controller.py
- members/controller.py
- typing
- ItemsOut
- errors.py
- conftest.py
- AccountService
- ClientDocumentService
- health/controller.py
- commissions/controller.py
- mcm/service.py
- invoices/controller.py
- sites/controller.py
- documents/controller.py
- Limiter
- ReportService
- google.py
- avant-api
- networks/controller.py
- uuid
- CommissionService
- Avant: conexão com o GAM
- costs/controller.py
- client_documents/controller.py
- goals/service.py
- commissions/controller.py
- test_dashboards.py
- InvoiceService
- test_events.py
- ContractService
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- checklists/dto.py
- Actor
- team
- GoogleService
- Actor
- .of
- goals/controller.py
- shared/__init__.py
- .of
- http.py
- auth/controller.py
- TaskQueue
- ChecklistDetailOut
- Counter
- ClientService
- AuditOut
- FakeGoogle
- reports/service.py
- TaskDetailOut
- Services
- TaskQueue
- _staff
- shared/dto.py
- test_goals.py
- _csrf
- UnitOfWorkFactory
- SiteService
- AuditService
- SiteService
- test_company_image.py
- Suporte
- RedisCounter
- do_reset_password
- .__init__
- DashboardTemplateOut
- _member_client
- .__init__
- ProfileService
- checklists
- .create
- events
- .first_day

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

## Communities (183 total, 81 thin omitted)

### Community 0 - "datetime"
Cohesion: 0.08
Nodes (13): refresh_levels(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone() (+5 more)

### Community 1 - "avant_core_access_models"
Cohesion: 0.09
Nodes (8): require_staff(), dependency(), invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (26): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+18 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 6 - ".save_rule"
Cohesion: 0.05
Nodes (19): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+11 more)

### Community 7 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.05
Nodes (35): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+27 more)

### Community 11 - "test_api.py"
Cohesion: 0.17
Nodes (13): _error_code(), _owner_invite(), test_csrf_is_required_for_writes(), test_deployed_cookies_use_the_host_prefix(), test_every_write_route_refuses_another_site(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit() (+5 more)

### Community 12 - ".trusted_uow"
Cohesion: 0.08
Nodes (11): add_item(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft(), update_item() (+3 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/controller.py"
Cohesion: 0.13
Nodes (9): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, page_out() (+1 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.11
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (11): check(), create(), delete(), index(), update(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn (+3 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "company/controller.py"
Cohesion: 0.04
Nodes (14): engine_options(), _google(), _mailer(), NoEvents, Settings, CeleryQueue, google_redirects(), GoogleRedirects (+6 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (13): create(), delete(), index(), roles(), set_home(), show(), update(), DashboardTemplateIn (+5 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "test_report_export.py"
Cohesion: 0.13
Nodes (3): image(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (8): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut, MfaService

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "reports/service.py"
Cohesion: 0.05
Nodes (17): catalog(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut (+9 more)

### Community 31 - "events.py"
Cohesion: 0.09
Nodes (8): TooManyAttempts, channel(), EventSource, _parse(), sse(), StreamLimiter, EventService, test_stream_limiter_caps_each_person_and_the_process()

### Community 32 - "test_sites.py"
Cohesion: 0.25
Nodes (5): _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search(), test_site_category_and_responsible(), test_sites_and_assignment()

### Community 36 - "require"
Cohesion: 0.09
Nodes (13): api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor(), get_session_actor(), optional_auth(), remember_company() (+5 more)

### Community 37 - "BaseModel"
Cohesion: 0.05
Nodes (17): change(), comment(), create(), task(), tasks(), TaskClientOut, TaskCommentIn, TaskDataIn (+9 more)

### Community 39 - "export.py"
Cohesion: 0.17
Nodes (5): _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 40 - "ItemsOut"
Cohesion: 0.17
Nodes (10): new_owner(), ClientIn, ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn, ManagerChangeOut (+2 more)

### Community 41 - "CompanyService"
Cohesion: 0.10
Nodes (13): _check_jpeg_size(), PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image() (+5 more)

### Community 42 - ".of"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "errors.py"
Cohesion: 0.15
Nodes (17): CapturingMailer, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited() (+9 more)

### Community 44 - "SiteChecklistService"
Cohesion: 0.18
Nodes (5): months(), summary(), site_checklist_service(), ChecklistMonthOut, SiteChecklistService

### Community 45 - "security.py"
Cohesion: 0.04
Nodes (21): Services, get_services(), known_companies(), alert_service(), api_key_service(), audit_service(), currency_service(), custom_metric_service() (+13 more)

### Community 46 - "AuthService"
Cohesion: 0.08
Nodes (36): _onboard_owner(), _checkouts(), test_report_requests_use_few_connections(), test_busy_export_answers_503_with_retry_after(), _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast() (+28 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "test_mfa.py"
Cohesion: 0.19
Nodes (6): add_note(), check(), checklist(), delete_note(), edit_note(), ChecklistNoteIn

### Community 49 - "router.py"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 57 - "ItemsOut"
Cohesion: 0.13
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 58 - "errors.py"
Cohesion: 0.05
Nodes (16): CompanyChanged, CsrfFailed, GoogleFailed, NoActiveCompany, QueryTooHeavy, RateLimited, challenge(), _claims() (+8 more)

### Community 59 - "conftest.py"
Cohesion: 0.12
Nodes (10): client(), engine(), mailer(), Sent, _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys() (+2 more)

### Community 60 - "AccountService"
Cohesion: 0.08
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 63 - "commissions/controller.py"
Cohesion: 0.06
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 65 - "mcm/service.py"
Cohesion: 0.25
Nodes (7): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 66 - "invoices/controller.py"
Cohesion: 0.08
Nodes (15): create_service(), payment_details(), save_payment_details(), services(), update_service(), invoice_service(), InvoiceItemOut, InvoiceServiceIn (+7 more)

### Community 67 - "sites/controller.py"
Cohesion: 0.15
Nodes (8): assign_sites(), classify(), classify_many(), delete(), site_options(), unlinked(), SitePatchIn, SitesPatchIn

### Community 68 - "documents/controller.py"
Cohesion: 0.09
Nodes (9): JsonFormatter, dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx() (+1 more)

### Community 69 - "Limiter"
Cohesion: 0.15
Nodes (7): Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "ReportService"
Cohesion: 0.06
Nodes (21): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+13 more)

### Community 72 - "google.py"
Cohesion: 0.12
Nodes (5): ChecklistMarkIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "networks/controller.py"
Cohesion: 0.06
Nodes (16): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+8 more)

### Community 75 - "uuid"
Cohesion: 0.15
Nodes (4): RedisCounter, test_docs_are_closed_in_production(), test_every_response_has_the_security_headers(), test_redis_down_is_a_503_not_a_500()

### Community 76 - "CommissionService"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 77 - "Avant: conexão com o GAM"
Cohesion: 0.11
Nodes (8): audit(), cancel_owner(), change_status(), client_image(), client_options(), edit_client_image(), manager_change(), remove_client_image()

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "client_documents/controller.py"
Cohesion: 0.18
Nodes (6): approve(), documents(), download(), reject(), ClientDocumentsOut, RejectDocumentIn

### Community 82 - "commissions/controller.py"
Cohesion: 0.28
Nodes (10): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports(), test_redis_source_delivers_published_messages() (+2 more)

### Community 83 - "test_dashboards.py"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - "InvoiceService"
Cohesion: 0.17
Nodes (5): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 85 - "test_events.py"
Cohesion: 0.06
Nodes (9): results(), client_result_service(), ClientResultService, show(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut (+1 more)

### Community 86 - "ContractService"
Cohesion: 0.18
Nodes (5): link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.31
Nodes (3): cors(), preflight(), receive()

### Community 89 - "checklists/dto.py"
Cohesion: 0.12
Nodes (7): BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 91 - "Actor"
Cohesion: 0.14
Nodes (3): create(), index(), SiteListOut

### Community 92 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 94 - "GoogleService"
Cohesion: 0.06
Nodes (9): GoogleUnavailable, GoogleAuth, google_callback(), google_start(), google_status(), google_unlink(), google_service(), GoogleStatusOut (+1 more)

### Community 96 - "Actor"
Cohesion: 0.09
Nodes (24): RecordingQueue, _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites() (+16 more)

### Community 97 - ".of"
Cohesion: 0.07
Nodes (3): dollars(), available_months(), AvailableMonthOut

### Community 98 - "goals/controller.py"
Cohesion: 0.18
Nodes (5): delete_template(), role_goals(), set_role_goal(), update_template(), RoleGoalIn

### Community 102 - "shared/__init__.py"
Cohesion: 0.47
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 123 - ".of"
Cohesion: 0.17
Nodes (3): WidgetErrorOut, ReportRangeOut, ReportRowOut

### Community 127 - "http.py"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "auth/controller.py"
Cohesion: 0.04
Nodes (23): SessionCookies, new_verifier(), get_auth(), get_cookies(), get_session_auth(), accept(), company_image(), do_logout() (+15 more)

### Community 129 - "TaskQueue"
Cohesion: 0.14
Nodes (6): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskQueue

### Community 133 - "ClientService"
Cohesion: 0.20
Nodes (5): client_teams(), client_service(), ClientMemberOut, ClientService, CompanyRefOut

### Community 139 - "TaskDetailOut"
Cohesion: 0.06
Nodes (10): configure_logging(), observe(), _route_template(), check_fetch_site(), create_app(), event_service(), health(), ready() (+2 more)

### Community 142 - "Services"
Cohesion: 0.09
Nodes (13): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+5 more)

### Community 143 - "TaskQueue"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "_staff"
Cohesion: 0.20
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+6 more)

### Community 145 - "shared/dto.py"
Cohesion: 0.09
Nodes (9): _contract_fields(), ContractNetworkOut, ContractNetworkRefOut, ContractSummaryOut, _network_ref(), ClientRefOut, ContractClientRefOut, image_url() (+1 more)

### Community 146 - "test_goals.py"
Cohesion: 0.11
Nodes (7): metrics(), create(), get(), mine(), pdf(), service_options(), team()

### Community 147 - "_csrf"
Cohesion: 0.10
Nodes (22): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+14 more)

### Community 149 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 160 - "SiteService"
Cohesion: 0.17
Nodes (5): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 161 - "test_company_image.py"
Cohesion: 0.10
Nodes (4): clients(), edit_client(), register_client(), ClientOut

### Community 162 - "Suporte"
Cohesion: 0.40
Nodes (3): ExportsBusy, test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 163 - "RedisCounter"
Cohesion: 0.11
Nodes (5): assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService

### Community 167 - ".__init__"
Cohesion: 0.11
Nodes (10): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), PersonOut, PeopleService (+2 more)

### Community 175 - "_member_client"
Cohesion: 0.07
Nodes (23): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company() (+15 more)

### Community 178 - "ProfileService"
Cohesion: 0.09
Nodes (7): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService

### Community 182 - ".create"
Cohesion: 0.15
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1867 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **81 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `auth/controller.py`, `TaskQueue`, `avant_core_access_models`, `DashboardService`, `AlertService`, `require_staff`, `ClientService`, `.save_rule`, `GoalService`, `.__init__`, `roles/controller.py`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `Services`, `inventory/controller.py`, `api_keys/controller.py`, `InvitationOut`, `custom_metrics/controller.py`, `SiteService`, `AuditService`, `dashboard_templates/controller.py`, `mfa/controller.py`, `reports/service.py`, `SiteService`, `RedisCounter`, `BaseModel`, `.__init__`, `ItemsOut`, `.of`, `SiteChecklistService`, `views/controller.py`, `client_notes/controller.py`, `ProfileService`, `currencies/controller.py`, `members/controller.py`, `Bucket`, `ItemsOut`, `AccountService`, `ClientDocumentService`, `commissions/controller.py`, `avant_core_shared_clock`, `invoices/controller.py`, `ReportService`, `GoalService`, `networks/controller.py`, `CommissionService`, `costs/controller.py`, `goals/service.py`, `test_events.py`, `ContractService`, `GoogleService`?**
  _High betweenness centrality (0.162) - this node is a cross-community bridge._
- **Are the 127 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 127 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `datetime` be split into smaller, more focused modules?**
  _Cohesion score 0.08194905869324474 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `inventory/controller.py` to `TaskQueue`, `avant_core_access_models`, `DashboardService`, `AlertService`, `require_staff`, `ClientService`, `AuditOut`, `.save_rule`, `GoalService`, `roles/controller.py`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `Services`, `api_keys/controller.py`, `InvitationOut`, `test_goals.py`, `shared/dto.py`, `SiteService`, `reports/service.py`, `test_company_image.py`, `RedisCounter`, `BaseModel`, `.__init__`, `ItemsOut`, `SiteChecklistService`, `test_mfa.py`, `client_notes/controller.py`, `checklists`, `.create`, `members/controller.py`, `invoices/controller.py`, `sites/controller.py`, `ReportService`, `networks/controller.py`, `Avant: conexão com o GAM`, `costs/controller.py`, `goals/service.py`, `InvoiceService`, `test_events.py`, `ContractService`, `Actor`, `goals/controller.py`?**
  _High betweenness centrality (0.093) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `avant_core_access_models` be split into smaller, more focused modules?**
  _Cohesion score 0.09009009009009009 - nodes in this community are weakly interconnected._