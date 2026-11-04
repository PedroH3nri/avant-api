# Graph Report - avant-api  (2026-11-04)

## Corpus Check
- 290 files · ~89,158 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3919 nodes · 10778 edges · 203 communities (111 shown, 92 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1811 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `51bbe855`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- clients/controller.py
- roles/controller.py
- .uow
- Actor
- Actor
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
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- image_response
- goals/controller.py
- verify
- http.py
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- limits.py
- _onboard_owner
- session-start.sh
- avant-api
- tasks.py
- BaseModel
- invoices/controller.py
- .save_rule
- test_account.py
- company/controller.py
- documents/controller.py
- install
- MemoryBucket
- security.py
- _month
- networks/service.py
- SupportTaskService
- PageOut
- Services
- Actor
- UserOut
- edit
- currencies/controller.py
- members/controller.py
- tasks/controller.py
- clients
- GoogleService
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
- contracts/controller.py
- GoalTemplateOut
- google/controller.py
- avant-api
- NetworkService
- uuid
- .of
- team
- mine
- image
- client_documents/controller.py
- disable
- commissions/controller.py
- uuid
- image_url
- goals/controller.py
- DashboardTemplateOut
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- checklists/dto.py
- Actor
- add_note
- UnitOfWorkFactory
- GoalService
- test_gam_tools.py
- tasks
- networks/service.py
- .run_guarded
- mine
- test_api_keys.py
- SiteOut
- SiteListOut
- ClientService
- test_company_image.py
- test_account.py
- ReportService
- clients
- person
- AdUnitOut
- .show
- TaskQueue
- test_mfa.py
- InvoiceServiceOut
- test_costs_results.py
- export.py
- events
- CompanyService
- test_groone_alerts_preview_every_client
- ReportService
- .fiscal
- .update_fiscal
- _onboard_owner
- MemoryCounter
- Actor
- conftest.py
- document_response
- RedisEvents
- Counter
- dollars
- AuditOut
- .of
- client_image
- SiteDetailOut
- images.py
- ClientDocumentsOut
- delete_template
- events/controller.py
- Suporte
- TaskPatchIn
- manager_change
- networks/dependencies.py
- enqueue_sync
- shared/dto.py
- create

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 156 edges
2. `PageOut` - 145 edges
3. `_onboard_owner()` - 140 edges
4. `_csrf()` - 138 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 118 edges
8. `ReportService` - 79 edges
9. `_staff()` - 64 edges
10. `page_out()` - 59 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/modules/internal/people/controller.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (203 total, 92 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.09
Nodes (31): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+23 more)

### Community 1 - "clients/controller.py"
Cohesion: 0.17
Nodes (12): register_client(), ClientDetailOut, ClientIn, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+4 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.05
Nodes (25): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+17 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "Actor"
Cohesion: 0.12
Nodes (4): owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 6 - "CommissionService"
Cohesion: 0.21
Nodes (4): set_settings(), settings(), CommissionSettingsOut, CommissionService

### Community 7 - "test_events.py"
Cohesion: 0.05
Nodes (19): ads_txt(), install(), network(), networks(), run(), runs(), start(), gam_tool_service() (+11 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.08
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (21): Acesso, AdUnit, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, GAM, Identidade (+13 more)

### Community 11 - "_member_client"
Cohesion: 0.07
Nodes (18): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture() (+10 more)

### Community 12 - ".trusted_uow"
Cohesion: 0.11
Nodes (4): issue(), update_item(), InvoiceOut, InvoiceService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "networks/controller.py"
Cohesion: 0.20
Nodes (5): sites(), client_inventory_service(), ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.09
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

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
Cohesion: 0.11
Nodes (6): get_cookies(), mfa_service(), profile_service(), client_info(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.15
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.23
Nodes (14): _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas() (+6 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (8): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut, MfaService

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "limits.py"
Cohesion: 0.07
Nodes (4): pinned(), update(), SavedReportIn, SavedReportOut

### Community 32 - "_onboard_owner"
Cohesion: 0.21
Nodes (10): CapturingMailer, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_option_lists_keep_the_permissions() (+2 more)

### Community 36 - "tasks.py"
Cohesion: 0.06
Nodes (6): _google(), _mailer(), NoEvents, RedisCounter, CeleryQueue, RecordingQueue

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - "invoices/controller.py"
Cohesion: 0.11
Nodes (12): FiscalDataIn, save_payment_details(), invoice_service(), InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut (+4 more)

### Community 39 - ".save_rule"
Cohesion: 0.14
Nodes (6): adjust(), create_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 40 - "test_account.py"
Cohesion: 0.10
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 41 - "company/controller.py"
Cohesion: 0.19
Nodes (4): show(), CompanyDetailOut, CompanyPatchIn, CompanyService

### Community 42 - "documents/controller.py"
Cohesion: 0.16
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "MemoryBucket"
Cohesion: 0.10
Nodes (7): BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 45 - "security.py"
Cohesion: 0.04
Nodes (27): Services, api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor(), get_auth(), get_services() (+19 more)

### Community 46 - "_month"
Cohesion: 0.18
Nodes (4): team(), CommissionMonthOut, CommissionSettingsIn, PersonMonthOut

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "SupportTaskService"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 49 - "PageOut"
Cohesion: 0.07
Nodes (7): results(), ClientResultService, show(), result_service(), ResultsOut, default_period(), ResultService

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 52 - "UserOut"
Cohesion: 0.08
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService, UserOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.15
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (16): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+8 more)

### Community 56 - "tasks/controller.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 57 - "clients"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "GoogleService"
Cohesion: 0.07
Nodes (7): GoogleUnavailable, GoogleAuth, google_callback(), google_status(), google_unlink(), google_service(), GoogleService

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "get"
Cohesion: 0.09
Nodes (14): add_item(), create(), delete(), delete_service(), get(), mine(), pay(), payment_details() (+6 more)

### Community 62 - "networks/controller.py"
Cohesion: 0.20
Nodes (6): connect(), disconnect(), service_account(), show(), sync(), sync_runs()

### Community 63 - "Actor"
Cohesion: 0.11
Nodes (9): audit(), cancel_owner(), change_status(), client_options(), edit_client(), edit_client_image(), invite_owner(), new_owner() (+1 more)

### Community 64 - "main.py"
Cohesion: 0.06
Nodes (9): configure_logging(), JsonFormatter, observe(), _route_template(), create_app(), health(), ready(), health_service() (+1 more)

### Community 65 - "NetworkOut"
Cohesion: 0.11
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 67 - "ItemsOut"
Cohesion: 0.19
Nodes (6): site_service(), AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 68 - "documents/controller.py"
Cohesion: 0.09
Nodes (5): documents(), download(), upload(), document_service(), DocumentService

### Community 69 - "limits.py"
Cohesion: 0.13
Nodes (8): TooManyAttempts, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "contracts/controller.py"
Cohesion: 0.06
Nodes (25): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+17 more)

### Community 71 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 72 - "google/controller.py"
Cohesion: 0.04
Nodes (15): CompanyChanged, CsrfFailed, GoogleFailed, NoActiveCompany, QueryTooHeavy, challenge(), _claims(), GoogleOAuth (+7 more)

### Community 74 - "NetworkService"
Cohesion: 0.15
Nodes (4): index(), options(), NetworkDetailOut, NetworkService

### Community 75 - "uuid"
Cohesion: 0.26
Nodes (15): test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+7 more)

### Community 76 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 77 - "team"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 78 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "client_documents/controller.py"
Cohesion: 0.13
Nodes (7): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentService

### Community 81 - "disable"
Cohesion: 0.11
Nodes (8): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out()

### Community 82 - "commissions/controller.py"
Cohesion: 0.18
Nodes (3): commission_service(), AdjustmentIn, MonthIn

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 85 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 86 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.05
Nodes (18): SessionCookies, accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company() (+10 more)

### Community 89 - "checklists/dto.py"
Cohesion: 0.09
Nodes (5): ChecklistMarkIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 91 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), classify(), classify_many(), delete(), show(), unlinked()

### Community 92 - "add_note"
Cohesion: 0.11
Nodes (13): add_note(), check(), checklist(), checklists(), delete_note(), edit_note(), mark(), months() (+5 more)

### Community 94 - "UnitOfWorkFactory"
Cohesion: 0.07
Nodes (3): UnitOfWorkFactory, ClientNetworkOut, page_out()

### Community 95 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 96 - "test_gam_tools.py"
Cohesion: 0.13
Nodes (10): _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list(), test_staff_marks_checks_and_writes_notes() (+2 more)

### Community 97 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 98 - "networks/service.py"
Cohesion: 0.24
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 128 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), MyCommissionsOut

### Community 129 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 131 - "SiteOut"
Cohesion: 0.13
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 132 - "SiteListOut"
Cohesion: 0.18
Nodes (3): index(), site_options(), SiteListOut

### Community 133 - "ClientService"
Cohesion: 0.17
Nodes (5): client_teams(), client_service(), ClientMemberOut, ClientService, CompanyRefOut

### Community 134 - "test_company_image.py"
Cohesion: 0.31
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 135 - "test_account.py"
Cohesion: 0.19
Nodes (8): FakeGoogle, _google_round(), _jwt(), _login(), test_forgot_and_reset_password(), test_google_link_and_login(), test_id_token_claims(), test_login_attempts_are_limited()

### Community 136 - "ReportService"
Cohesion: 0.06
Nodes (14): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+6 more)

### Community 139 - "AdUnitOut"
Cohesion: 0.21
Nodes (3): ad_units(), link(), AdUnitOut

### Community 144 - "test_mfa.py"
Cohesion: 0.20
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+6 more)

### Community 145 - "InvoiceServiceOut"
Cohesion: 0.25
Nodes (3): create_service(), update_service(), InvoiceServiceOut

### Community 146 - "test_costs_results.py"
Cohesion: 0.08
Nodes (12): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query() (+4 more)

### Community 147 - "export.py"
Cohesion: 0.08
Nodes (11): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+3 more)

### Community 149 - "CompanyService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 150 - "test_groone_alerts_preview_every_client"
Cohesion: 0.38
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 152 - "ReportService"
Cohesion: 0.06
Nodes (20): alert_service(), create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index() (+12 more)

### Community 155 - ".update_fiscal"
Cohesion: 0.21
Nodes (4): edit_fiscal(), edit_image(), fiscal(), remove_image()

### Community 158 - "_onboard_owner"
Cohesion: 0.18
Nodes (17): test_change_password_and_sessions(), test_change_password_attempts_are_limited(), _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit() (+9 more)

### Community 163 - "conftest.py"
Cohesion: 0.12
Nodes (7): client(), engine(), mailer(), Sent, _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 166 - "RedisEvents"
Cohesion: 0.24
Nodes (5): RedisEvents, test_redis_source_delivers_published_messages(), run(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 172 - "dollars"
Cohesion: 0.12
Nodes (3): dollars(), available_months(), AvailableMonthOut

### Community 184 - "events/controller.py"
Cohesion: 0.12
Nodes (10): channel(), EventSource, _parse(), sse(), _collect(), _event(), ListEvents, test_events_route() (+2 more)

### Community 185 - "Suporte"
Cohesion: 0.40
Nodes (5): ApiKey, AuditLog, PasswordReset, Session, Suporte

### Community 194 - "shared/dto.py"
Cohesion: 0.10
Nodes (5): index(), audit_service(), AuditService, networks(), PageOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1790 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **92 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `clients/controller.py`, `roles/controller.py`, `.uow`, `Actor`, `ClientService`, `CommissionService`, `test_events.py`, `ReportService`, `_month`, `.trusted_uow`, `.uow`, `networks/controller.py`, `TaskQueue`, `api_keys/controller.py`, `InvitationOut`, `custom_metrics/controller.py`, `CompanyService`, `goals/controller.py`, `ReportService`, `mfa/controller.py`, `company/controller.py`, `.__init__`, `invoices/controller.py`, `.__init__`, `company/controller.py`, `documents/controller.py`, `test_account.py`, `goals/service.py`, `SupportTaskService`, `PageOut`, `Services`, `networks/service.py`, `UserOut`, `schedules/dto.py`, `currencies/controller.py`, `members/controller.py`, `tasks/controller.py`, `clients`, `GoogleService`, `.__init__`, `account/controller.py`, `.__init__`, `.__init__`, `NetworkOut`, `shared/dto.py`, `ItemsOut`, `documents/controller.py`, `.__init__`, `contracts/controller.py`, `google/controller.py`, `NetworkService`, `image`, `client_documents/controller.py`, `disable`, `commissions/controller.py`, `auth/controller.py`, `add_note`, `GoalService`, `networks/service.py`?**
  _High betweenness centrality (0.145) - this node is a cross-community bridge._
- **Are the 117 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 117 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.08779761904761904 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `shared/dto.py` to `clients/controller.py`, `roles/controller.py`, `.uow`, `Actor`, `ClientService`, `Actor`, `test_events.py`, `ReportService`, `clients`, `_month`, `SiteListOut`, `.trusted_uow`, `.uow`, `networks/controller.py`, `api_keys/controller.py`, `InvitationOut`, `SiteOut`, `CompanyService`, `ReportService`, `invoices/controller.py`, `test_account.py`, `AuditOut`, `goals/service.py`, `SupportTaskService`, `PageOut`, `Services`, `schedules/dto.py`, `members/controller.py`, `tasks/controller.py`, `get`, `networks/controller.py`, `Actor`, `NetworkOut`, `.page`, `ItemsOut`, `contracts/controller.py`, `GoalTemplateOut`, `NetworkService`, `image`, `disable`, `goals/controller.py`, `Actor`, `add_note`, `UnitOfWorkFactory`, `GoalService`, `tasks`, `networks/service.py`?**
  _High betweenness centrality (0.069) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07364114552893045 - nodes in this community are weakly interconnected._