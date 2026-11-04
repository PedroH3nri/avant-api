# Graph Report - avant-api  (2026-11-04)

## Corpus Check
- 290 files · ~89,193 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3919 nodes · 10775 edges · 203 communities (104 shown, 99 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1809 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d2b03810`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- clients/controller.py
- roles/controller.py
- .uow
- Actor
- ClientService
- CommissionService
- test_events.py
- steps
- _month
- Avant: models do MVP
- _member_client
- .trusted_uow
- .uow
- networks/controller.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- InvitationOut
- auth/controller.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- image_response
- goals/controller.py
- verify
- http.py
- clean_code.py
- _csrf
- mfa/controller.py
- Avant: repositório e plano do MVP
- ReportQueryIn
- _onboard_owner
- session-start.sh
- avant-api
- Services
- BaseModel
- invoices/controller.py
- .save_rule
- test_account.py
- company/controller.py
- documents/controller.py
- install
- checklists/controller.py
- security.py
- _month
- networks/service.py
- SupportTaskService
- PageOut
- Services
- profile/controller.py
- UserOut
- edit
- currencies/controller.py
- members/controller.py
- tasks/controller.py
- clients
- GoogleService
- UUID
- account/controller.py
- get
- networks/controller.py
- Actor
- main.py
- NetworkOut
- .page
- ItemsOut
- documents/controller.py
- limits.py
- contracts/dto.py
- GoalService
- google/controller.py
- avant-api
- NetworkService
- ContractService
- contracts/controller.py
- image
- client_documents/controller.py
- disable
- commissions/controller.py
- uuid
- image_url
- index
- DashboardTemplateOut
- Avant: grupos na Empresa e imagem da Empresa
- SessionCookies
- Actor
- add_note
- UnitOfWorkFactory
- update_item
- test_gam_tools.py
- tasks
- networks/service.py
- .run_guarded
- mine
- test_api_keys.py
- SiteOut
- SiteListOut
- test_company_image.py
- commissions/dto.py
- ReportService
- O que já tem
- person
- AdUnitOut
- .show
- TaskQueue
- test_mfa.py
- InvoiceServiceOut
- _marketing_client
- export.py
- verify
- CompanyService
- test_alerts.py
- ReportService
- .fiscal
- company/controller.py
- _onboard_owner
- image
- .page_saved
- document_response
- Settings
- .owner_invitations
- AuditOut
- test_staff_sees_client_networks_sites_and_revenue_status
- test_contract_crud
- test_staff_manage_templates_and_clients_see_them_by_role
- .of
- SiteDetailOut
- .create
- test_goal_progress_routes
- events/controller.py
- test_clients_by_manager_and_name
- TaskPatchIn
- dashboards/dependencies.py
- contracts/dependencies.py
- create

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 157 edges
2. `PageOut` - 145 edges
3. `_onboard_owner()` - 140 edges
4. `_csrf()` - 139 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 117 edges
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

## Communities (203 total, 99 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.09
Nodes (28): _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it() (+20 more)

### Community 1 - "clients/controller.py"
Cohesion: 0.14
Nodes (14): client_teams(), client_service(), ClientDetailOut, ClientIn, ClientMemberOut, ClientOptionOut, ClientPatchIn, ClientProfileIn (+6 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.06
Nodes (24): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+16 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 6 - "CommissionService"
Cohesion: 0.16
Nodes (4): set_settings(), settings(), CommissionSettingsOut, CommissionService

### Community 7 - "test_events.py"
Cohesion: 0.06
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

### Community 11 - "_member_client"
Cohesion: 0.10
Nodes (17): test_events_route(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site() (+9 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "networks/controller.py"
Cohesion: 0.12
Nodes (8): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, PageOut

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.16
Nodes (6): create(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.09
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "auth/controller.py"
Cohesion: 0.13
Nodes (9): get_invitation(), auth_service(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut (+1 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "http.py"
Cohesion: 0.16
Nodes (3): client_info(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "_csrf"
Cohesion: 0.14
Nodes (29): _csrf(), _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency() (+21 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (10): get_cookies(), confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 32 - "_onboard_owner"
Cohesion: 0.16
Nodes (13): CapturingMailer, client(), engine(), mailer(), test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages() (+5 more)

### Community 36 - "Services"
Cohesion: 0.03
Nodes (19): _google(), _mailer(), Services, NoEvents, PillowImageProcessor, Bucket, BucketResult, BucketRule (+11 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - "invoices/controller.py"
Cohesion: 0.20
Nodes (9): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn (+1 more)

### Community 39 - ".save_rule"
Cohesion: 0.12
Nodes (7): adjust(), create_rule(), delete_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 40 - "test_account.py"
Cohesion: 0.10
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 41 - "company/controller.py"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 42 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "install"
Cohesion: 0.15
Nodes (7): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), QueryTooHeavy

### Community 44 - "checklists/controller.py"
Cohesion: 0.17
Nodes (10): site_checklist_service(), ChecklistDetailOut, ChecklistMarkIn, ChecklistMonthOut, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut (+2 more)

### Community 45 - "security.py"
Cohesion: 0.08
Nodes (20): CompanyChanged, CsrfFailed, NoActiveCompany, RateLimited, api_key_actor(), bearer_token(), check_csrf(), check_tab_company() (+12 more)

### Community 46 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "SupportTaskService"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 49 - "PageOut"
Cohesion: 0.06
Nodes (12): get_services(), results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut (+4 more)

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "profile/controller.py"
Cohesion: 0.20
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 52 - "UserOut"
Cohesion: 0.14
Nodes (3): edit_image(), remove_image(), UserOut

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (16): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+8 more)

### Community 56 - "tasks/controller.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "GoogleService"
Cohesion: 0.07
Nodes (6): GoogleUnavailable, GoogleAuth, google_status(), google_unlink(), google_service(), GoogleService

### Community 59 - "UUID"
Cohesion: 0.13
Nodes (8): add_item(), create(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft()

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "get"
Cohesion: 0.11
Nodes (8): available_months(), get(), mine(), payment_details(), pdf(), service_options(), services(), team()

### Community 62 - "networks/controller.py"
Cohesion: 0.15
Nodes (7): disconnect(), options(), service_account(), show(), sync(), sync_runs(), network_service()

### Community 63 - "Actor"
Cohesion: 0.09
Nodes (13): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), edit_client_image(), invite_owner() (+5 more)

### Community 64 - "main.py"
Cohesion: 0.07
Nodes (8): configure_logging(), JsonFormatter, observe(), _route_template(), create_app(), health(), ready(), HealthService

### Community 65 - "NetworkOut"
Cohesion: 0.12
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 67 - "ItemsOut"
Cohesion: 0.19
Nodes (6): site_service(), AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 68 - "documents/controller.py"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 69 - "limits.py"
Cohesion: 0.07
Nodes (11): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _jwt(), _limiter_round(), _refused_attempt_round() (+3 more)

### Community 70 - "contracts/dto.py"
Cohesion: 0.18
Nodes (6): ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut, _network_ref(), ContractClientRefOut

### Community 71 - "GoalService"
Cohesion: 0.05
Nodes (19): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+11 more)

### Community 72 - "google/controller.py"
Cohesion: 0.08
Nodes (9): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), google_start(), GoogleStatusOut (+1 more)

### Community 74 - "NetworkService"
Cohesion: 0.17
Nodes (5): connect(), index(), NetworkDetailOut, NetworkIn, NetworkService

### Community 75 - "ContractService"
Cohesion: 0.20
Nodes (3): contract(), ContractOut, ContractService

### Community 78 - "contracts/controller.py"
Cohesion: 0.18
Nodes (5): contract_networks(), contracts(), edit_contract(), finish_contract(), remove_contract()

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "client_documents/controller.py"
Cohesion: 0.14
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 81 - "disable"
Cohesion: 0.05
Nodes (29): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+21 more)

### Community 82 - "commissions/controller.py"
Cohesion: 0.19
Nodes (3): commission_service(), AdjustmentIn, MonthIn

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 86 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "SessionCookies"
Cohesion: 0.09
Nodes (10): SessionCookies, accept(), company_image(), do_logout(), login(), me(), set_active_company(), MeOut (+2 more)

### Community 91 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), classify(), classify_many(), delete(), show(), unlinked()

### Community 92 - "add_note"
Cohesion: 0.11
Nodes (8): add_note(), check(), checklist(), checklists(), delete_note(), edit_note(), months(), summary()

### Community 94 - "UnitOfWorkFactory"
Cohesion: 0.05
Nodes (5): UnitOfWorkFactory, index(), audit_service(), AuditService, page_out()

### Community 96 - "test_gam_tools.py"
Cohesion: 0.13
Nodes (10): _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list(), test_staff_marks_checks_and_writes_notes() (+2 more)

### Community 97 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 129 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 131 - "SiteOut"
Cohesion: 0.13
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 132 - "SiteListOut"
Cohesion: 0.18
Nodes (3): index(), site_options(), SiteListOut

### Community 134 - "test_company_image.py"
Cohesion: 0.39
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 135 - "commissions/dto.py"
Cohesion: 0.24
Nodes (3): CommissionMonthOut, CommissionSettingsIn, dollars()

### Community 136 - "ReportService"
Cohesion: 0.05
Nodes (15): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+7 more)

### Community 137 - "O que já tem"
Cohesion: 0.20
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics()

### Community 139 - "AdUnitOut"
Cohesion: 0.21
Nodes (3): ad_units(), link(), AdUnitOut

### Community 144 - "test_mfa.py"
Cohesion: 0.38
Nodes (11): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+3 more)

### Community 145 - "InvoiceServiceOut"
Cohesion: 0.19
Nodes (5): create_service(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 146 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 147 - "export.py"
Cohesion: 0.07
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 149 - "CompanyService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 150 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 152 - "ReportService"
Cohesion: 0.05
Nodes (19): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned() (+11 more)

### Community 155 - "company/controller.py"
Cohesion: 0.16
Nodes (5): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 158 - "_onboard_owner"
Cohesion: 0.13
Nodes (23): Sent, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited() (+15 more)

### Community 166 - "Settings"
Cohesion: 0.09
Nodes (5): Settings, google_redirects(), GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 175 - "test_staff_sees_client_networks_sites_and_revenue_status"
Cohesion: 0.38
Nodes (3): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 176 - "test_contract_crud"
Cohesion: 0.38
Nodes (3): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission()

### Community 177 - "test_staff_manage_templates_and_clients_see_them_by_role"
Cohesion: 0.38
Nodes (3): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company()

### Community 183 - "test_goal_progress_routes"
Cohesion: 0.53
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 184 - "events/controller.py"
Cohesion: 0.08
Nodes (14): channel(), EventSource, _parse(), RedisEvents, sse(), events(), EventService, _collect() (+6 more)

### Community 185 - "test_clients_by_manager_and_name"
Cohesion: 0.60
Nodes (3): test_clients_by_manager_and_name(), test_saved_views_are_staff_only(), test_saved_views_crud_and_catalog()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1790 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **99 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `clients/controller.py`, `roles/controller.py`, `.uow`, `Actor`, `ClientService`, `.__init__`, `CommissionService`, `test_events.py`, `ReportService`, `_month`, `.trusted_uow`, `.uow`, `networks/controller.py`, `TaskQueue`, `api_keys/controller.py`, `InvoiceServiceOut`, `auth/controller.py`, `custom_metrics/controller.py`, `InvitationOut`, `CompanyService`, `goals/controller.py`, `ReportService`, `company/controller.py`, `mfa/controller.py`, `company/controller.py`, `.__init__`, `Services`, `invoices/controller.py`, `.__init__`, `company/controller.py`, `documents/controller.py`, `test_account.py`, `checklists/controller.py`, `networks/service.py`, `SupportTaskService`, `PageOut`, `Services`, `profile/controller.py`, `currencies/controller.py`, `members/controller.py`, `tasks/controller.py`, `clients`, `GoogleService`, `account/controller.py`, `.__init__`, `NetworkOut`, `.__init__`, `.page`, `.__init__`, `limits.py`, `contracts/dto.py`, `GoalService`, `.__init__`, `ItemsOut`, `NetworkService`, `ContractService`, `image`, `client_documents/controller.py`, `disable`, `commissions/controller.py`, `networks/service.py`?**
  _High betweenness centrality (0.135) - this node is a cross-community bridge._
- **Are the 118 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 118 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.08686868686868687 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `networks/controller.py` to `clients/controller.py`, `roles/controller.py`, `.uow`, `Actor`, `ClientService`, `SiteListOut`, `test_events.py`, `ReportService`, `_month`, `SiteOut`, `.trusted_uow`, `.uow`, `api_keys/controller.py`, `InvoiceServiceOut`, `InvitationOut`, `CompanyService`, `.page_saved`, `invoices/controller.py`, `test_account.py`, `.owner_invitations`, `checklists/controller.py`, `AuditOut`, `SupportTaskService`, `PageOut`, `Services`, `members/controller.py`, `tasks/controller.py`, `get`, `networks/controller.py`, `Actor`, `NetworkOut`, `.page`, `ItemsOut`, `contracts/dto.py`, `GoalService`, `NetworkService`, `ContractService`, `contracts/controller.py`, `image`, `disable`, `image_url`, `index`, `Actor`, `add_note`, `UnitOfWorkFactory`, `tasks`, `networks/service.py`?**
  _High betweenness centrality (0.091) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `clients/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13763440860215054 - nodes in this community are weakly interconnected._