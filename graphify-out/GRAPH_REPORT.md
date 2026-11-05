# Graph Report - avant-api  (2026-11-05)

## Corpus Check
- 297 files · ~91,970 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4041 nodes · 11109 edges · 218 communities (119 shown, 99 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1851 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `464ef9f7`
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
- GoogleFailed
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
- clients/dto.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- main.py
- goals/controller.py
- verify
- image_response
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
- person
- Actor
- test_company_image.py
- documents/controller.py
- CapturingMailer
- checklists
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
- members/controller.py
- contracts/dto.py
- clients
- Actor
- test_account.py
- account/controller.py
- mine
- ClientDocumentsOut
- commissions/controller.py
- accept
- limits.py
- Actor
- ItemsOut
- export.py
- limits.py
- ReportService
- GoalService
- ExportsBusy
- avant-api
- networks/controller.py
- SupportTaskService
- CompanyService
- shared/dto.py
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
- GoogleService
- invoices/controller.py
- _csrf
- goals/controller.py
- tasks/controller.py
- team
- updates
- TaskDetailOut
- TaskQueue
- ProfileService
- google_status
- google.py
- users
- _month
- pydantic
- tasks/dto.py
- health/controller.py
- ContractOut
- Arquitetura do MVP do Avant
- test_mfa.py
- .of
- contracts/controller.py
- profile/controller.py
- members
- ReportService
- clients
- page_out
- goals/service.py
- time
- company/controller.py
- edit_client
- mcm/service.py
- .change_password
- google_start
- GoalTemplateIn
- UserOut
- Bucket
- document_response
- _member_client
- ad_units
- test_client_changes_the_company_image
- .of
- Actor
- .assign
- test_database.py
- events.py
- GoogleOAuth
- TaskPatchIn
- Settings
- clients
- O que já tem
- MemoryCounter
- GoogleAuth
- .run_guarded
- .payee_details
- client_image
- test_staff_sees_client_networks_sites_and_revenue_status
- test_contract_crud
- edit_image
- new_owner
- source_files
- NoEvents
- google/dto.py
- company_service

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

## Communities (218 total, 99 thin omitted)

### Community 0 - "conftest.py"
Cohesion: 0.08
Nodes (7): engine(), mailer(), _error_code(), test_every_write_route_refuses_another_site(), _jpeg(), test_phone_photos_pass_and_huge_pngs_are_refused(), test_phone_rotation_from_exif_is_kept()

### Community 1 - "test_alerts.py"
Cohesion: 0.19
Nodes (6): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form()

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "PageOut"
Cohesion: 0.06
Nodes (6): UnitOfWorkFactory, index(), audit_service(), AuditService, AuditOut, PageOut

### Community 6 - "GamToolService"
Cohesion: 0.06
Nodes (18): ads_txt(), install(), network(), networks(), run(), runs(), start(), AdsTxtOut (+10 more)

### Community 7 - "GoogleFailed"
Cohesion: 0.19
Nodes (3): GoogleFailed, identity_from_id_token(), FakeGoogle

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "test_gam_tools.py"
Cohesion: 0.13
Nodes (11): RecordingQueue, _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list() (+3 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "router.py"
Cohesion: 0.15
Nodes (6): sites(), client_inventory_service(), ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, staff()

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "invitations/controller.py"
Cohesion: 0.05
Nodes (11): invite(), options(), StaffInviteIn, StaffService, cancel(), create_invitation(), list_invitations(), resend() (+3 more)

### Community 18 - "clients/dto.py"
Cohesion: 0.16
Nodes (7): ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn, ManagerChangeOut, OwnerChangeIn

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (11): check(), create(), delete(), index(), update(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn (+3 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "main.py"
Cohesion: 0.05
Nodes (15): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), QueryTooHeavy (+7 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "image_response"
Cohesion: 0.13
Nodes (3): image(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "_onboard_owner"
Cohesion: 0.09
Nodes (20): client(), refresh_levels(), _checkouts(), test_report_requests_use_few_connections(), query(), test_busy_export_answers_503_with_retry_after(), _day(), _metrics() (+12 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), verify(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "reports/service.py"
Cohesion: 0.05
Nodes (18): catalog(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut (+10 more)

### Community 31 - "UUID"
Cohesion: 0.13
Nodes (8): add_item(), create(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft()

### Community 32 - "Actor"
Cohesion: 0.16
Nodes (7): audit(), cancel_owner(), change_status(), client_options(), edit_client_image(), manager_change(), remove_client_image()

### Community 36 - "security.py"
Cohesion: 0.06
Nodes (24): CompanyChanged, CsrfFailed, NoActiveCompany, RateLimited, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site() (+16 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 39 - "person"
Cohesion: 0.19
Nodes (5): adjust(), create_rule(), delete_rule(), person(), settings()

### Community 40 - "Actor"
Cohesion: 0.12
Nodes (5): client(), client_teams(), ClientDetailOut, ClientMemberOut, ClientService

### Community 41 - "test_company_image.py"
Cohesion: 0.09
Nodes (6): _check_jpeg_size(), PillowImageProcessor, client_service(), _sharpness(), _striped_logo(), test_wide_and_palette_logos_stay_sharp()

### Community 42 - "documents/controller.py"
Cohesion: 0.16
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 43 - "CapturingMailer"
Cohesion: 0.12
Nodes (28): CapturingMailer, Sent, _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit() (+20 more)

### Community 44 - "checklists"
Cohesion: 0.24
Nodes (3): checklists(), summary(), ChecklistMonthOut

### Community 45 - "Services"
Cohesion: 0.05
Nodes (12): Services, get_services(), cost_service(), checklist_item_service(), client_note_service(), contract_service(), gam_tool_service(), mcm_service() (+4 more)

### Community 46 - "uuid"
Cohesion: 0.18
Nodes (17): _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency(), test_pinned_reports_and_preview_refresh() (+9 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "ChecklistDetailOut"
Cohesion: 0.12
Nodes (3): ChecklistDetailOut, ChecklistOut, SiteChecklistService

### Community 49 - "download"
Cohesion: 0.09
Nodes (5): documents(), download(), upload(), document_service(), DocumentService

### Community 50 - "Services"
Cohesion: 0.08
Nodes (8): add(), delete(), edit(), notes(), ClientNoteIn, ClientNoteOut, NotePersonOut, ClientNoteService

### Community 52 - ".of"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "contracts/dto.py"
Cohesion: 0.18
Nodes (6): ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut, _network_ref()

### Community 57 - "clients"
Cohesion: 0.12
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 58 - "Actor"
Cohesion: 0.17
Nodes (5): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 59 - "test_account.py"
Cohesion: 0.17
Nodes (14): _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_id_token_claims() (+6 more)

### Community 60 - "account/controller.py"
Cohesion: 0.08
Nodes (14): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+6 more)

### Community 61 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 63 - "commissions/controller.py"
Cohesion: 0.16
Nodes (15): rules(), set_settings(), update_rule(), commission_service(), AdjustmentIn, CommissionMonthOut, CommissionRuleIn, CommissionRuleOut (+7 more)

### Community 64 - "accept"
Cohesion: 0.11
Nodes (4): accept(), company_image(), do_logout(), set_active_company()

### Community 65 - "limits.py"
Cohesion: 0.10
Nodes (8): _mailer(), BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 66 - "Actor"
Cohesion: 0.13
Nodes (9): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), months(), site_checklist_service() (+1 more)

### Community 67 - "ItemsOut"
Cohesion: 0.18
Nodes (11): classify(), classify_many(), link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn (+3 more)

### Community 68 - "export.py"
Cohesion: 0.08
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 69 - "limits.py"
Cohesion: 0.16
Nodes (7): Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "ReportService"
Cohesion: 0.07
Nodes (20): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+12 more)

### Community 71 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 72 - "ExportsBusy"
Cohesion: 0.40
Nodes (3): ExportsBusy, test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 74 - "networks/controller.py"
Cohesion: 0.07
Nodes (15): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+7 more)

### Community 75 - "SupportTaskService"
Cohesion: 0.15
Nodes (4): tasks(), support_task_service(), TaskOut, SupportTaskService

### Community 76 - "CompanyService"
Cohesion: 0.21
Nodes (3): show(), CompanyDetailOut, CompanyService

### Community 77 - "shared/dto.py"
Cohesion: 0.09
Nodes (3): custom_metric_service(), people_service(), invitation_service()

### Community 78 - "profile/controller.py"
Cohesion: 0.24
Nodes (3): edit_appearance(), AppearanceIn, AppearanceOut

### Community 79 - "image"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "download"
Cohesion: 0.13
Nodes (7): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentService

### Community 81 - "people/controller.py"
Cohesion: 0.21
Nodes (3): disable(), enable(), reset_mfa()

### Community 82 - "test_events.py"
Cohesion: 0.28
Nodes (10): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports(), test_redis_source_delivers_published_messages() (+2 more)

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
Cohesion: 0.11
Nodes (13): get_invitation(), login(), me(), auth_service(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut (+5 more)

### Community 89 - "create_app"
Cohesion: 0.09
Nodes (4): RedisCounter, test_docs_are_closed_in_production(), test_every_response_has_the_security_headers(), test_redis_down_is_a_503_not_a_500()

### Community 91 - "SiteListOut"
Cohesion: 0.17
Nodes (3): create(), site_options(), SiteListOut

### Community 92 - "get"
Cohesion: 0.11
Nodes (8): available_months(), get(), mine(), payment_details(), pdf(), service_options(), services(), team()

### Community 94 - "GoogleService"
Cohesion: 0.16
Nodes (3): GoogleUnavailable, google_callback(), GoogleService

### Community 95 - "invoices/controller.py"
Cohesion: 0.20
Nodes (9): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn (+1 more)

### Community 96 - "_csrf"
Cohesion: 0.07
Nodes (37): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+29 more)

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
Cohesion: 0.17
Nodes (3): CeleryQueue, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 135 - "users"
Cohesion: 0.15
Nodes (11): Modelo de dados, Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação (+3 more)

### Community 136 - "_month"
Cohesion: 0.12
Nodes (3): mine(), _month(), team()

### Community 137 - "pydantic"
Cohesion: 0.14
Nodes (4): ChecklistMarkIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 139 - "health/controller.py"
Cohesion: 0.15
Nodes (4): health(), ready(), health_service(), HealthService

### Community 142 - "ContractOut"
Cohesion: 0.17
Nodes (4): contract(), edit_contract(), ContractOut, ContractService

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.38
Nodes (11): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+3 more)

### Community 147 - "contracts/controller.py"
Cohesion: 0.20
Nodes (4): contract_networks(), contracts(), finish_contract(), remove_contract()

### Community 148 - "profile/controller.py"
Cohesion: 0.15
Nodes (4): edit_image(), image(), remove_image(), profile_service()

### Community 149 - "members"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 150 - "ReportService"
Cohesion: 0.06
Nodes (4): update(), SavedReportIn, SavedReportOut, export_slot()

### Community 152 - "clients"
Cohesion: 0.11
Nodes (4): ClientNetworkOut, ClientRefOut, NetworkOut, RevenueStatusOut

### Community 160 - "company/controller.py"
Cohesion: 0.19
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 161 - "edit_client"
Cohesion: 0.15
Nodes (4): edit_client(), register_client(), ClientIn, ClientOut

### Community 163 - "mcm/service.py"
Cohesion: 0.06
Nodes (7): TaskQueue, assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService, enqueue_sync()

### Community 167 - "UserOut"
Cohesion: 0.19
Nodes (6): PersonOut, PeopleService, person_out(), CompanyRefOut, RoleRefOut, UserOut

### Community 175 - "_member_client"
Cohesion: 0.10
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 177 - "test_client_changes_the_company_image"
Cohesion: 0.33
Nodes (5): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), test_upload_without_session_is_refused_before_reading_the_body()

### Community 180 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), delete(), index(), show(), sites_of_member(), unlinked()

### Community 182 - ".assign"
Cohesion: 0.40
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 183 - "test_database.py"
Cohesion: 0.31
Nodes (4): engine_options(), _settings(), test_every_connection_has_a_statement_and_idle_timeout(), test_pool_is_bounded_and_waits_little()

### Community 184 - "events.py"
Cohesion: 0.09
Nodes (9): TooManyAttempts, channel(), EventSource, _parse(), sse(), StreamLimiter, events(), EventService (+1 more)

### Community 189 - "Settings"
Cohesion: 0.10
Nodes (4): SessionCookies, Settings, test_closing_deployed_cookies_keeps_them_secure(), test_deployed_cookies_use_the_host_prefix()

### Community 191 - "O que já tem"
Cohesion: 0.20
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics()

### Community 198 - "test_staff_sees_client_networks_sites_and_revenue_status"
Cohesion: 0.38
Nodes (3): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 202 - "test_contract_crud"
Cohesion: 0.38
Nodes (3): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission()

### Community 203 - "edit_image"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1838 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **99 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `PageOut` to `ProfileService`, `DashboardService`, `Actor`, `.__init__`, `GamToolService`, `roles/controller.py`, `_month`, `tasks/dto.py`, `InvoiceService`, `.uow`, `ContractOut`, `router.py`, `api_keys/controller.py`, `invitations/controller.py`, `custom_metrics/controller.py`, `members`, `ReportService`, `goals/controller.py`, `clients`, `goals/service.py`, `mfa/controller.py`, `reports/service.py`, `company/controller.py`, `.__init__`, `mcm/service.py`, `UserOut`, `Actor`, `documents/controller.py`, `.__init__`, `networks/service.py`, `ChecklistDetailOut`, `download`, `Services`, `currencies/controller.py`, `members/controller.py`, `contracts/dto.py`, `clients`, `account/controller.py`, `commissions/controller.py`, `GoogleAuth`, `ItemsOut`, `ReportService`, `GoalService`, `networks/controller.py`, `SupportTaskService`, `CompanyService`, `profile/controller.py`, `image`, `download`, `.__init__`, `.__init__`, `InvoiceService`, `.__init__`, `.__init__`, `auth/controller.py`, `.__init__`, `results/dto.py`, `GoogleService`, `invoices/controller.py`?**
  _High betweenness centrality (0.156) - this node is a cross-community bridge._
- **Are the 124 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 124 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `conftest.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07629107981220658 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `roles/controller.py`, `DashboardService`, `Actor`, `GamToolService`, `users`, `_month`, `tasks/dto.py`, `InvoiceService`, `.uow`, `ContractOut`, `router.py`, `api_keys/controller.py`, `invitations/controller.py`, `contracts/controller.py`, `members`, `clients`, `page_out`, `goals/service.py`, `reports/service.py`, `Actor`, `mcm/service.py`, `security.py`, `UserOut`, `Actor`, `test_company_image.py`, `checklists`, `Services`, `ChecklistDetailOut`, `Services`, `Actor`, `members/controller.py`, `contracts/dto.py`, `Actor`, `clients`, `Actor`, `ItemsOut`, `ReportService`, `GoalService`, `networks/controller.py`, `SupportTaskService`, `shared/dto.py`, `image`, `InvoiceService`, `results/dto.py`, `get`, `invoices/controller.py`, `Actor`, `goals/controller.py`, `tasks/controller.py`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07792207792207792 - nodes in this community are weakly interconnected._