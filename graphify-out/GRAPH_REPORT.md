# Graph Report - avant-api  (2026-11-05)

## Corpus Check
- 297 files · ~91,931 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4038 nodes · 11104 edges · 218 communities (111 shown, 107 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1851 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4f0ad3d7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- conftest.py
- test_alerts.py
- roles/controller.py
- DashboardService
- Actor
- PageOut
- GamToolService
- google.py
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
- errors.py
- goals/controller.py
- verify
- image
- clean_code.py
- _onboard_owner
- mfa/controller.py
- Avant: repositório e plano do MVP
- reports/service.py
- UUID
- Actor
- session-start.sh
- avant-api
- security.py
- BaseModel
- .save_rule
- CommissionService
- Actor
- test_company_image.py
- documents/controller.py
- CapturingMailer
- SiteChecklistService
- Services
- uuid
- networks/service.py
- ChecklistDetailOut
- download
- Services
- dollars
- .of
- edit
- currencies/controller.py
- MemberService
- contracts/dto.py
- clients
- .owner_invitations
- test_account.py
- account/controller.py
- mine
- commissions/controller.py
- MemberOut
- limits.py
- Actor
- ItemsOut
- export.py
- limits.py
- GoalService
- ExportsBusy
- avant-api
- networks/controller.py
- SupportTaskService
- CompanyService
- .of
- profile/controller.py
- image
- download
- people/controller.py
- test_events.py
- uuid
- InvoiceService
- results/dto.py
- _marketing_client
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- create_app
- SiteListOut
- get
- UnitOfWorkFactory
- invoices/controller.py
- _csrf
- SiteService
- goals/controller.py
- tasks/controller.py
- team
- updates
- TaskDetailOut
- TaskQueue
- networks/service.py
- index
- users
- person
- pydantic
- tasks/dto.py
- health/controller.py
- ContractOut
- Arquitetura do MVP do Avant
- test_mfa.py
- AuditOut
- templates
- contracts/controller.py
- profile/controller.py
- members
- ReportService
- clients
- members/controller.py
- goals/service.py
- test_api_keys.py
- company/controller.py
- edit_client
- mcm/service.py
- .change_password
- logs.py
- GoalTemplateIn
- UserOut
- document_response
- _member_client
- show
- ContractService
- Actor
- .assign
- test_database.py
- events.py
- _month
- TaskPatchIn
- Settings
- O que já tem
- MemoryCounter
- client_documents/service.py
- .run_guarded
- .payee_details
- index
- edit_image
- .page_saved
- capped
- set_settings
- NoEvents
- google/dto.py

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 165 edges
2. `_onboard_owner()` - 148 edges
3. `_csrf()` - 147 edges
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

## Communities (218 total, 107 thin omitted)

### Community 0 - "conftest.py"
Cohesion: 0.09
Nodes (7): refresh_levels(), test_every_write_route_refuses_another_site(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _agent(), test_staff_opens_assigns_and_comments_on_tasks()

### Community 1 - "test_alerts.py"
Cohesion: 0.13
Nodes (9): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), _form(), test_members_without_schedules_manage_only_see_what_they_receive() (+1 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (26): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+18 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "PageOut"
Cohesion: 0.10
Nodes (5): index(), audit_service(), AuditService, page_out(), PageOut

### Community 6 - "GamToolService"
Cohesion: 0.06
Nodes (18): ads_txt(), install(), network(), networks(), run(), runs(), start(), AdsTxtOut (+10 more)

### Community 7 - "google.py"
Cohesion: 0.08
Nodes (10): _google(), GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), FakeGoogle (+2 more)

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
Cohesion: 0.16
Nodes (9): RecordingQueue, _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list() (+1 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "shared/dto.py"
Cohesion: 0.10
Nodes (7): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "invitations/controller.py"
Cohesion: 0.10
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService, InvitationOut

### Community 18 - "clients/controller.py"
Cohesion: 0.14
Nodes (14): client_teams(), client_service(), ClientDetailOut, ClientIn, ClientMemberOut, ClientOptionOut, ClientPatchIn, ClientProfileIn (+6 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (11): check(), create(), delete(), index(), update(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn (+3 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "errors.py"
Cohesion: 0.17
Nodes (7): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "_onboard_owner"
Cohesion: 0.12
Nodes (17): _checkouts(), test_report_requests_use_few_connections(), query(), _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait() (+9 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.05
Nodes (13): get_cookies(), confirm(), disable(), new_recovery_codes(), setup(), verify(), MfaCodeIn, MfaSetupOut (+5 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "reports/service.py"
Cohesion: 0.06
Nodes (20): RateLimited, query_batch(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut (+12 more)

### Community 31 - "UUID"
Cohesion: 0.13
Nodes (8): add_item(), create(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft()

### Community 32 - "Actor"
Cohesion: 0.09
Nodes (13): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), edit_client_image(), invite_owner() (+5 more)

### Community 36 - "security.py"
Cohesion: 0.05
Nodes (24): CompanyChanged, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company() (+16 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - ".save_rule"
Cohesion: 0.17
Nodes (5): adjust(), create_rule(), rules(), update_rule(), CommissionRuleOut

### Community 39 - "CommissionService"
Cohesion: 0.16
Nodes (3): delete_rule(), settings(), CommissionService

### Community 41 - "test_company_image.py"
Cohesion: 0.10
Nodes (11): _check_jpeg_size(), PillowImageProcessor, _jpeg(), _png(), _sharpness(), _striped_logo(), test_client_changes_the_company_image(), test_phone_photos_pass_and_huge_pngs_are_refused() (+3 more)

### Community 42 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "CapturingMailer"
Cohesion: 0.12
Nodes (28): CapturingMailer, Sent, _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit() (+20 more)

### Community 44 - "SiteChecklistService"
Cohesion: 0.11
Nodes (6): checklists(), months(), summary(), ChecklistMonthOut, ChecklistOut, SiteChecklistService

### Community 45 - "Services"
Cohesion: 0.03
Nodes (24): Services, get_services(), alert_service(), cost_service(), currency_service(), custom_metric_service(), dashboard_service(), google_redirects() (+16 more)

### Community 46 - "uuid"
Cohesion: 0.21
Nodes (15): test_busy_export_answers_503_with_retry_after(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+7 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 49 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 52 - ".of"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.15
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "MemberService"
Cohesion: 0.14
Nodes (3): show(), MemberDetailOut, MemberService

### Community 56 - "contracts/dto.py"
Cohesion: 0.13
Nodes (7): contract_networks(), _contract_fields(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractSummaryOut, _network_ref()

### Community 57 - "clients"
Cohesion: 0.13
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 59 - "test_account.py"
Cohesion: 0.33
Nodes (7): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 60 - "account/controller.py"
Cohesion: 0.08
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 63 - "commissions/controller.py"
Cohesion: 0.30
Nodes (8): AdjustmentIn, CommissionMonthOut, CommissionRuleIn, CommissionSettingsIn, CommissionSettingsOut, MonthIn, MyCommissionsOut, WindowMonthOut

### Community 64 - "MemberOut"
Cohesion: 0.12
Nodes (7): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 65 - "limits.py"
Cohesion: 0.13
Nodes (7): BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 66 - "Actor"
Cohesion: 0.15
Nodes (6): add_note(), check(), checklist(), delete_note(), edit_note(), mark()

### Community 67 - "ItemsOut"
Cohesion: 0.18
Nodes (8): classify(), classify_many(), AdUnitPatchIn, MemberSitesIn, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "export.py"
Cohesion: 0.06
Nodes (14): observe(), _route_template(), dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv() (+6 more)

### Community 69 - "limits.py"
Cohesion: 0.12
Nodes (8): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 72 - "ExportsBusy"
Cohesion: 0.22
Nodes (4): ExportsBusy, export_slot(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 74 - "networks/controller.py"
Cohesion: 0.13
Nodes (9): connect(), disconnect(), index(), options(), show(), sync(), sync_runs(), NetworkDetailOut (+1 more)

### Community 75 - "SupportTaskService"
Cohesion: 0.15
Nodes (4): tasks(), support_task_service(), TaskOut, SupportTaskService

### Community 76 - "CompanyService"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 78 - "profile/controller.py"
Cohesion: 0.24
Nodes (4): edit_appearance(), AppearanceIn, AppearanceOut, ProfileService

### Community 79 - "image"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "download"
Cohesion: 0.14
Nodes (6): approve(), documents(), download(), reject(), ClientDocumentOut, ClientDocumentService

### Community 81 - "people/controller.py"
Cohesion: 0.14
Nodes (4): disable(), enable(), reset_mfa(), PeopleService

### Community 82 - "test_events.py"
Cohesion: 0.16
Nodes (14): client(), engine(), mailer(), _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot() (+6 more)

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - "InvoiceService"
Cohesion: 0.19
Nodes (5): create_service(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 85 - "results/dto.py"
Cohesion: 0.07
Nodes (8): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, default_period(), ResultService

### Community 86 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.06
Nodes (16): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+8 more)

### Community 89 - "create_app"
Cohesion: 0.09
Nodes (7): _mailer(), RedisCounter, create_app(), health(), test_docs_are_closed_in_production(), test_every_response_has_the_security_headers(), test_redis_down_is_a_503_not_a_500()

### Community 92 - "get"
Cohesion: 0.11
Nodes (8): available_months(), get(), mine(), payment_details(), pdf(), service_options(), services(), team()

### Community 94 - "UnitOfWorkFactory"
Cohesion: 0.05
Nodes (8): GoogleUnavailable, GoogleAuth, UnitOfWorkFactory, google_callback(), google_start(), google_status(), google_unlink(), GoogleService

### Community 95 - "invoices/controller.py"
Cohesion: 0.20
Nodes (9): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn (+1 more)

### Community 96 - "_csrf"
Cohesion: 0.07
Nodes (39): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+31 more)

### Community 97 - "SiteService"
Cohesion: 0.16
Nodes (3): unlinked(), AdUnitOut, SiteService

### Community 98 - "goals/controller.py"
Cohesion: 0.18
Nodes (5): delete_template(), role_goals(), set_role_goal(), update_template(), RoleGoalIn

### Community 102 - "tasks/controller.py"
Cohesion: 0.22
Nodes (4): change(), comment(), create(), task()

### Community 123 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 129 - "TaskQueue"
Cohesion: 0.09
Nodes (5): CeleryQueue, TaskQueue, enqueue_sync(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 131 - "networks/service.py"
Cohesion: 0.14
Nodes (5): service_account(), NetworkIn, NetworkOut, ServiceAccountOut, SyncRunOut

### Community 132 - "index"
Cohesion: 0.12
Nodes (6): edit(), index(), leave(), options(), remove(), set_permissions()

### Community 135 - "users"
Cohesion: 0.15
Nodes (11): Modelo de dados, Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação (+3 more)

### Community 136 - "person"
Cohesion: 0.18
Nodes (3): mine(), _month(), person()

### Community 137 - "pydantic"
Cohesion: 0.10
Nodes (6): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 139 - "health/controller.py"
Cohesion: 0.17
Nodes (3): ready(), health_service(), HealthService

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.21
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+6 more)

### Community 147 - "contracts/controller.py"
Cohesion: 0.20
Nodes (5): contract(), contracts(), finish_contract(), new_contract(), remove_contract()

### Community 148 - "profile/controller.py"
Cohesion: 0.15
Nodes (4): edit_image(), image(), remove_image(), profile_service()

### Community 150 - "ReportService"
Cohesion: 0.05
Nodes (19): Bucket, catalog(), create(), create_from_template(), delete(), duplicate(), export(), export_saved() (+11 more)

### Community 153 - "members/controller.py"
Cohesion: 0.23
Nodes (4): DirectPermissionIn, DirectPermissionOut, MemberPatchIn, MemberPermissionsIn

### Community 158 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 160 - "company/controller.py"
Cohesion: 0.15
Nodes (6): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, image_url()

### Community 163 - "mcm/service.py"
Cohesion: 0.11
Nodes (5): assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService

### Community 167 - "UserOut"
Cohesion: 0.31
Nodes (3): PersonOut, person_out(), UserOut

### Community 175 - "_member_client"
Cohesion: 0.10
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 177 - "ContractService"
Cohesion: 0.27
Nodes (3): edit_contract(), ContractPatchIn, ContractService

### Community 180 - "Actor"
Cohesion: 0.18
Nodes (5): ad_units(), delete(), link(), site_options(), sites_of_member()

### Community 182 - ".assign"
Cohesion: 0.25
Nodes (5): Atribuição de sites, GAM, Networks, Sites e ad units, assign_sites()

### Community 183 - "test_database.py"
Cohesion: 0.31
Nodes (4): engine_options(), _settings(), test_every_connection_has_a_statement_and_idle_timeout(), test_pool_is_bounded_and_waits_little()

### Community 184 - "events.py"
Cohesion: 0.09
Nodes (8): TooManyAttempts, channel(), EventSource, _parse(), sse(), StreamLimiter, events(), EventService

### Community 189 - "Settings"
Cohesion: 0.09
Nodes (4): SessionCookies, Settings, test_closing_deployed_cookies_keeps_them_secure(), test_deployed_cookies_use_the_host_prefix()

### Community 191 - "O que já tem"
Cohesion: 0.20
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1837 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **107 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `TaskQueue`, `roles/controller.py`, `DashboardService`, `Actor`, `PageOut`, `.__init__`, `GamToolService`, `networks/service.py`, `_month`, `tasks/dto.py`, `InvoiceService`, `.uow`, `shared/dto.py`, `api_keys/controller.py`, `invitations/controller.py`, `clients/controller.py`, `custom_metrics/controller.py`, `ReportService`, `goals/controller.py`, `members/controller.py`, `goals/service.py`, `mfa/controller.py`, `reports/service.py`, `company/controller.py`, `.__init__`, `mcm/service.py`, `CommissionService`, `avant_core_shared_clock`, `Actor`, `documents/controller.py`, `UserOut`, `SiteChecklistService`, `Services`, `.__init__`, `networks/service.py`, `ContractService`, `Services`, `currencies/controller.py`, `MemberService`, `contracts/dto.py`, `clients`, `account/controller.py`, `commissions/controller.py`, `MemberOut`, `client_documents/service.py`, `.__init__`, `ItemsOut`, `.__init__`, `GoalService`, `networks/controller.py`, `SupportTaskService`, `CompanyService`, `profile/controller.py`, `image`, `download`, `people/controller.py`, `InvoiceService`, `results/dto.py`, `.__init__`, `auth/controller.py`, `.__init__`, `invoices/controller.py`, `SiteService`?**
  _High betweenness centrality (0.154) - this node is a cross-community bridge._
- **Are the 124 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 124 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `conftest.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08566895822316235 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `roles/controller.py`, `DashboardService`, `Actor`, `networks/service.py`, `GamToolService`, `users`, `index`, `_month`, `tasks/dto.py`, `InvoiceService`, `.uow`, `ContractOut`, `shared/dto.py`, `api_keys/controller.py`, `invitations/controller.py`, `clients/controller.py`, `contracts/controller.py`, `AuditOut`, `clients`, `members/controller.py`, `goals/service.py`, `reports/service.py`, `Actor`, `mcm/service.py`, `security.py`, `UserOut`, `Actor`, `avant_core_shared_clock`, `SiteChecklistService`, `Services`, `ContractService`, `Services`, `MemberService`, `contracts/dto.py`, `.owner_invitations`, `MemberOut`, `ItemsOut`, `GoalService`, `networks/controller.py`, `SupportTaskService`, `index`, `image`, `people/controller.py`, `InvoiceService`, `results/dto.py`, `get`, `invoices/controller.py`, `SiteService`, `goals/controller.py`, `tasks/controller.py`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_alerts.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12666666666666668 - nodes in this community are weakly interconnected._