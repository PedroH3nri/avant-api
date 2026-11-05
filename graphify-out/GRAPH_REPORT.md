# Graph Report - avant-api  (2026-11-05)

## Corpus Check
- 295 files · ~91,166 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 3992 nodes · 10989 edges · 208 communities (111 shown, 97 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1833 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `15ba8014`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _staff
- typing
- roles/controller.py
- DashboardService
- Actor
- InvitationOut
- google.py
- GamToolService
- steps
- _month
- Avant: models do MVP
- test_events.py
- .trusted_uow
- .uow
- PageOut
- Groone Avant: contexto do projeto
- api_keys/controller.py
- invitations/controller.py
- PageOut
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- install
- goals/controller.py
- verify
- http.py
- clean_code.py
- _onboard_owner
- mfa/controller.py
- Avant: repositório e plano do MVP
- reports/controller.py
- clients/controller.py
- session-start.sh
- avant-api
- errors.py
- BaseModel
- person
- ClientService
- CompanyService
- documents/controller.py
- test_networks.py
- months
- security.py
- reports/service.py
- networks/service.py
- ContractClientRefOut
- UnitOfWorkFactory
- Services
- dollars
- .authenticate
- edit
- currencies/controller.py
- members/controller.py
- ContractOut
- clients
- GoogleService
- CapturingMailer
- account/controller.py
- edit_contract
- ClientDocumentsOut
- commissions/controller.py
- main.py
- MemoryBucket
- Actor
- ItemsOut
- export.py
- limits.py
- .of_view
- GoalTemplateOut
- FakeGoogle
- avant-api
- networks/controller.py
- mine
- .square_webp
- UserOut
- image
- client_documents/controller.py
- people/controller.py
- conftest.py
- uuid
- test_sites.py
- fastapi
- limits.py
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- contracts
- UUID
- export_slots.py
- google_start
- invoices/controller.py
- _csrf
- Actor
- Actor
- tasks/controller.py
- google_status
- GoalService
- TaskDetailOut
- .assign
- AdUnitOut
- capped
- ClientResultService
- test_api.py
- users
- EventService
- .page_saved
- tasks/dto.py
- logs.py
- middleware.py
- Arquitetura do MVP do Avant
- test_mfa.py
- TooManyAttempts
- refresh_levels
- test_api_keys.py
- get
- SiteService
- .uow
- InvoiceService
- Actor
- UnitOfWorkFactory
- contracts/controller.py
- company/controller.py
- edit_client
- mcm/service.py
- RedisEvents
- .of
- test_goals.py
- MemoryCounter
- clients/service.py
- document_response
- .of
- _member_client
- show
- test_saved_views.py
- delete_template
- .classify
- edit_image
- events.py
- _month
- TaskPatchIn
- Settings
- _contract_fields
- Bucket
- is_exempt
- .of
- update_item
- SessionCookies

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 161 edges
2. `PageOut` - 145 edges
3. `_onboard_owner()` - 144 edges
4. `_csrf()` - 143 edges
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

## Communities (208 total, 97 thin omitted)

### Community 0 - "_staff"
Cohesion: 0.07
Nodes (24): _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _network() (+16 more)

### Community 1 - "typing"
Cohesion: 0.35
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): GoogleStatusOut, create(), edit(), index(), options(), permissions(), remove(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "InvitationOut"
Cohesion: 0.12
Nodes (5): invite(), options(), StaffInviteIn, StaffService, InvitationOut

### Community 6 - "google.py"
Cohesion: 0.13
Nodes (6): GoogleFailed, challenge(), _claims(), identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 7 - "GamToolService"
Cohesion: 0.06
Nodes (19): ads_txt(), install(), network(), networks(), run(), runs(), start(), gam_tool_service() (+11 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (22): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+14 more)

### Community 11 - "test_events.py"
Cohesion: 0.28
Nodes (10): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports(), test_redis_source_delivers_published_messages() (+2 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "PageOut"
Cohesion: 0.09
Nodes (7): networks(), sites(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "invitations/controller.py"
Cohesion: 0.11
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService

### Community 18 - "PageOut"
Cohesion: 0.09
Nodes (3): index(), AuditService, page_out()

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

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

### Community 25 - "http.py"
Cohesion: 0.13
Nodes (3): image(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 27 - "_onboard_owner"
Cohesion: 0.12
Nodes (31): _onboard_owner(), test_busy_export_answers_503_with_retry_after(), test_export_slots_refuse_a_third_export_while_two_run(), _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait() (+23 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (7): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "reports/controller.py"
Cohesion: 0.09
Nodes (15): create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin(), query_batch() (+7 more)

### Community 32 - "clients/controller.py"
Cohesion: 0.08
Nodes (21): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), edit_client(), edit_client_image() (+13 more)

### Community 36 - "errors.py"
Cohesion: 0.06
Nodes (19): CompanyChanged, CsrfFailed, NoActiveCompany, QueryTooHeavy, RateLimited, api_key_actor(), bearer_token(), check_csrf() (+11 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 39 - "person"
Cohesion: 0.19
Nodes (5): adjust(), create_rule(), delete_rule(), person(), settings()

### Community 40 - "ClientService"
Cohesion: 0.08
Nodes (8): manager_change(), owner_invitations(), resend_owner(), client_service(), ManagerChangeOut, OwnerInvitationOut, ClientService, owner_invitation_out()

### Community 42 - "documents/controller.py"
Cohesion: 0.16
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 43 - "test_networks.py"
Cohesion: 0.13
Nodes (9): RecordingQueue, Sent, _owner_invite(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company() (+1 more)

### Community 44 - "months"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 45 - "security.py"
Cohesion: 0.03
Nodes (25): Services, PillowImageProcessor, get_auth(), get_cookies(), get_services(), get_session_auth(), alert_service(), auth_service() (+17 more)

### Community 46 - "reports/service.py"
Cohesion: 0.05
Nodes (19): catalog(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut (+11 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 49 - "UnitOfWorkFactory"
Cohesion: 0.09
Nodes (5): documents(), download(), upload(), document_service(), DocumentService

### Community 50 - "Services"
Cohesion: 0.09
Nodes (8): add(), delete(), edit(), notes(), ClientNoteIn, ClientNoteOut, NotePersonOut, ClientNoteService

### Community 52 - ".authenticate"
Cohesion: 0.09
Nodes (3): get_invitation(), InvitationPreviewOut, AuthService

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.15
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "ContractOut"
Cohesion: 0.17
Nodes (3): contract(), ContractOut, ContractService

### Community 57 - "clients"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "GoogleService"
Cohesion: 0.13
Nodes (3): GoogleUnavailable, GoogleAuth, GoogleService

### Community 59 - "CapturingMailer"
Cohesion: 0.21
Nodes (10): CapturingMailer, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_option_lists_keep_the_permissions() (+2 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "edit_contract"
Cohesion: 0.16
Nodes (5): contract_networks(), edit_contract(), finish_contract(), new_contract(), remove_contract()

### Community 63 - "commissions/controller.py"
Cohesion: 0.16
Nodes (15): rules(), set_settings(), update_rule(), commission_service(), AdjustmentIn, CommissionMonthOut, CommissionRuleIn, CommissionRuleOut (+7 more)

### Community 64 - "main.py"
Cohesion: 0.15
Nodes (4): health(), ready(), health_service(), HealthService

### Community 65 - "MemoryBucket"
Cohesion: 0.17
Nodes (6): BucketResult, BucketRule, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 66 - "Actor"
Cohesion: 0.10
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistDetailOut, ChecklistMarkIn (+2 more)

### Community 67 - "ItemsOut"
Cohesion: 0.25
Nodes (8): AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "export.py"
Cohesion: 0.08
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 69 - "limits.py"
Cohesion: 0.11
Nodes (8): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 74 - "networks/controller.py"
Cohesion: 0.08
Nodes (13): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+5 more)

### Community 76 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 77 - ".square_webp"
Cohesion: 0.17
Nodes (4): _check_jpeg_size(), _sharpness(), _striped_logo(), test_wide_and_palette_logos_stay_sharp()

### Community 78 - "UserOut"
Cohesion: 0.07
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService, UserOut

### Community 79 - "image"
Cohesion: 0.09
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "client_documents/controller.py"
Cohesion: 0.13
Nodes (7): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentService

### Community 81 - "people/controller.py"
Cohesion: 0.11
Nodes (7): disable(), enable(), reset_mfa(), users(), PersonOut, PeopleService, person_out()

### Community 82 - "conftest.py"
Cohesion: 0.09
Nodes (18): client(), engine(), mailer(), _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password() (+10 more)

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - "test_sites.py"
Cohesion: 0.25
Nodes (5): _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search(), test_site_category_and_responsible(), test_sites_and_assignment()

### Community 85 - "fastapi"
Cohesion: 0.07
Nodes (8): results(), client_result_service(), staff(), staff_service(), show(), result_service(), ResultsOut, ResultService

### Community 86 - "limits.py"
Cohesion: 0.07
Nodes (7): RedisBucket, RedisCounter, create_app(), audit_service(), test_docs_are_closed_in_production(), test_every_response_has_the_security_headers(), test_redis_down_is_a_503_not_a_500()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.11
Nodes (14): SessionCookies, accept(), company_image(), do_logout(), login(), me(), set_active_company(), AcceptInvitationIn (+6 more)

### Community 89 - "contracts"
Cohesion: 0.15
Nodes (8): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contracts()

### Community 95 - "invoices/controller.py"
Cohesion: 0.17
Nodes (8): service_options(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, ReturnedOut, ReturnIn, ServiceItemIn

### Community 96 - "_csrf"
Cohesion: 0.14
Nodes (18): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+10 more)

### Community 98 - "Actor"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 102 - "tasks/controller.py"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 127 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 128 - "TaskDetailOut"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 129 - ".assign"
Cohesion: 0.25
Nodes (5): Atribuição de sites, GAM, Networks, Sites e ad units, assign_sites()

### Community 130 - "AdUnitOut"
Cohesion: 0.16
Nodes (4): ad_units(), link(), unlinked(), AdUnitOut

### Community 134 - "test_api.py"
Cohesion: 0.32
Nodes (7): test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session(), test_team_invitation_flow(), test_validation_error_format()

### Community 135 - "users"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 137 - ".page_saved"
Cohesion: 0.14
Nodes (4): ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 138 - "tasks/dto.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.34
Nodes (11): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+3 more)

### Community 145 - "TooManyAttempts"
Cohesion: 0.29
Nodes (3): TooManyAttempts, StreamLimiter, test_stream_limiter_caps_each_person_and_the_process()

### Community 146 - "refresh_levels"
Cohesion: 0.12
Nodes (9): refresh_levels(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone() (+1 more)

### Community 147 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 148 - "get"
Cohesion: 0.08
Nodes (15): add_item(), available_months(), delete(), delete_service(), get(), issue(), mine(), pay() (+7 more)

### Community 149 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 150 - ".uow"
Cohesion: 0.06
Nodes (5): create(), pinned(), SavedReportIn, SavedReportOut, ReportService

### Community 152 - "InvoiceService"
Cohesion: 0.19
Nodes (5): create_service(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 158 - "contracts/controller.py"
Cohesion: 0.26
Nodes (6): contract_service(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut

### Community 160 - "company/controller.py"
Cohesion: 0.14
Nodes (6): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 163 - "mcm/service.py"
Cohesion: 0.07
Nodes (9): TaskQueue, assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut, enqueue_sync() (+1 more)

### Community 166 - "test_goals.py"
Cohesion: 0.43
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 168 - "clients/service.py"
Cohesion: 0.13
Nodes (6): client_teams(), ClientMemberOut, AuditOut, CompanyRefOut, RevenueStatusOut, RoleRefOut

### Community 175 - "_member_client"
Cohesion: 0.07
Nodes (18): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture() (+10 more)

### Community 178 - "test_saved_views.py"
Cohesion: 0.48
Nodes (3): test_clients_by_manager_and_name(), test_saved_views_are_staff_only(), test_saved_views_crud_and_catalog()

### Community 180 - ".classify"
Cohesion: 0.20
Nodes (4): classify(), classify_many(), site_options(), sites_of_member()

### Community 182 - "edit_image"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 184 - "events.py"
Cohesion: 0.18
Nodes (4): channel(), EventSource, _parse(), sse()

### Community 185 - "_month"
Cohesion: 0.12
Nodes (3): mine(), _month(), team()

### Community 189 - "Settings"
Cohesion: 0.06
Nodes (13): engine_options(), _google(), _mailer(), NoEvents, GoogleOAuth, Settings, CeleryQueue, GoogleRedirects (+5 more)

### Community 198 - "SessionCookies"
Cohesion: 0.10
Nodes (3): google_callback(), verify(), client_info()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1815 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **97 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `TaskDetailOut`, `roles/controller.py`, `DashboardService`, `Actor`, `.__init__`, `ClientResultService`, `GamToolService`, `InvitationOut`, `_month`, `tasks/dto.py`, `.trusted_uow`, `.uow`, `PageOut`, `api_keys/controller.py`, `invitations/controller.py`, `PageOut`, `custom_metrics/controller.py`, `SiteService`, `.uow`, `goals/controller.py`, `InvoiceService`, `contracts/controller.py`, `company/controller.py`, `company/controller.py`, `.__init__`, `mcm/service.py`, `clients/service.py`, `ClientService`, `documents/controller.py`, `reports/service.py`, `networks/service.py`, `UnitOfWorkFactory`, `.__init__`, `Services`, `.authenticate`, `currencies/controller.py`, `goals/service.py`, `ContractOut`, `clients`, `GoogleService`, `members/controller.py`, `account/controller.py`, `commissions/controller.py`, `Bucket`, `Actor`, `ItemsOut`, `.__init__`, `networks/controller.py`, `.__init__`, `.__init__`, `.__init__`, `UserOut`, `image`, `client_documents/controller.py`, `people/controller.py`, `fastapi`, `invoices/controller.py`, `GoalService`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Are the 121 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 121 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_staff` be split into smaller, more focused modules?**
  _Cohesion score 0.07115677321156773 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `mcm/service.py` to `TaskDetailOut`, `roles/controller.py`, `DashboardService`, `Actor`, `ClientResultService`, `InvitationOut`, `GamToolService`, `AdUnitOut`, `_month`, `tasks/dto.py`, `.trusted_uow`, `.uow`, `PageOut`, `api_keys/controller.py`, `invitations/controller.py`, `PageOut`, `get`, `SiteService`, `InvoiceService`, `UnitOfWorkFactory`, `contracts/controller.py`, `reports/controller.py`, `clients/controller.py`, `clients/service.py`, `ClientService`, `months`, `reports/service.py`, `Services`, `goals/service.py`, `ContractOut`, `members/controller.py`, `Actor`, `ItemsOut`, `.of_view`, `GoalTemplateOut`, `networks/controller.py`, `image`, `people/controller.py`, `fastapi`, `limits.py`, `contracts`, `UUID`, `invoices/controller.py`, `Actor`, `tasks/controller.py`, `GoalService`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06949152542372881 - nodes in this community are weakly interconnected._