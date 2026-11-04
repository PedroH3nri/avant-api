# Graph Report - avant-api  (2026-11-04)

## Corpus Check
- 290 files · ~89,698 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3931 nodes · 10808 edges · 205 communities (109 shown, 96 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1814 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4f7c381a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- shared/dto.py
- roles/controller.py
- .uow
- Actor
- ClientService
- CommissionService
- test_events.py
- steps
- _month
- Avant: models do MVP
- datetime
- .trusted_uow
- .uow
- PageOut
- Groone Avant: contexto do projeto
- api_keys/controller.py
- InvitationOut
- PageOut
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
- checklists/dto.py
- security.py
- _month
- networks/service.py
- SupportTaskService
- results/dto.py
- Services
- UserOut
- edit
- currencies/controller.py
- members/controller.py
- tasks/controller.py
- clients
- GoogleService
- uuid
- account/controller.py
- get
- networks/controller.py
- typing
- health/controller.py
- NetworkOut
- checklists/controller.py
- ItemsOut
- export.py
- limits.py
- contracts/dto.py
- GoalTemplateOut
- google/controller.py
- avant-api
- mine
- goals/controller.py
- GoalService
- Arquitetura do MVP do Avant
- image
- client_documents/controller.py
- people/controller.py
- commissions/dto.py
- uuid
- router.py
- modules/results/controller.py
- limits.py
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- SessionCookies
- Actor
- checklists
- .save_payee_details
- test_gam_tools.py
- tasks
- networks/service.py
- events/controller.py
- mine
- .upload
- SiteService
- UnitOfWorkFactory
- PillowImageProcessor
- Actor
- ReportService
- Actor
- person
- AdUnitOut
- .show
- TaskQueue
- test_mfa.py
- InvoiceServiceOut
- _marketing_client
- ContractClientRefOut
- contracts/controller.py
- test_members_without_schedules_manage_only_see_what_they_receive
- ReportService
- edit_image
- company/controller.py
- ContractOut
- ContractService
- .page_saved
- test_api_keys.py
- main.py
- client_image
- .of_view
- dollars
- CommissionRuleOut
- _member_client
- O que já tem
- templates
- delete_template
- results
- create
- events/controller.py
- test_staff_sees_client_networks_sites_and_revenue_status
- TaskPatchIn
- test_contract_crud
- alerts/dependencies.py
- .create
- GAM
- .of
- is_exempt

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

## Communities (205 total, 96 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.07
Nodes (37): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+29 more)

### Community 1 - "shared/dto.py"
Cohesion: 0.11
Nodes (15): client_service(), ClientDetailOut, ClientIn, ClientMemberOut, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn (+7 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.07
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "ClientService"
Cohesion: 0.06
Nodes (17): audit(), cancel_owner(), change_status(), client(), client_options(), client_teams(), edit_client(), edit_client_image() (+9 more)

### Community 6 - "CommissionService"
Cohesion: 0.18
Nodes (3): set_settings(), commission_service(), CommissionService

### Community 7 - "test_events.py"
Cohesion: 0.05
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

### Community 11 - "datetime"
Cohesion: 0.09
Nodes (3): client(), engine(), mailer()

### Community 12 - ".trusted_uow"
Cohesion: 0.12
Nodes (5): add_item(), pay(), update_item(), InvoiceOut, InvoiceService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "PageOut"
Cohesion: 0.08
Nodes (11): index(), networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService (+3 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "PageOut"
Cohesion: 0.17
Nodes (3): index(), audit_service(), AuditService

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
Cohesion: 0.15
Nodes (3): client_info(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.14
Nodes (19): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _day(), _metrics(), _row() (+11 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "ReportQueryIn"
Cohesion: 0.07
Nodes (4): QueryTooHeavy, query(), ReportQueryIn, _statement_timeout()

### Community 32 - "_onboard_owner"
Cohesion: 0.11
Nodes (31): CapturingMailer, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited() (+23 more)

### Community 36 - "Services"
Cohesion: 0.06
Nodes (5): _google(), _mailer(), NoEvents, MemoryCounter, CeleryQueue

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - "invoices/controller.py"
Cohesion: 0.18
Nodes (10): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn (+2 more)

### Community 39 - ".save_rule"
Cohesion: 0.16
Nodes (6): adjust(), create_rule(), delete_rule(), rules(), update_rule(), CommissionRuleIn

### Community 40 - "test_account.py"
Cohesion: 0.14
Nodes (5): invite(), options(), staff_service(), StaffInviteIn, StaffService

### Community 41 - "company/controller.py"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 42 - "documents/controller.py"
Cohesion: 0.11
Nodes (8): documents(), download(), upload(), document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "install"
Cohesion: 0.20
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "checklists/dto.py"
Cohesion: 0.09
Nodes (6): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 45 - "security.py"
Cohesion: 0.08
Nodes (22): Services, CompanyChanged, CsrfFailed, NoActiveCompany, RateLimited, api_key_actor(), bearer_token(), check_csrf() (+14 more)

### Community 46 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "SupportTaskService"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 49 - "results/dto.py"
Cohesion: 0.15
Nodes (4): client_result_service(), ClientResultService, ResultsOut, default_period()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "UserOut"
Cohesion: 0.08
Nodes (9): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService (+1 more)

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "tasks/controller.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "GoogleService"
Cohesion: 0.06
Nodes (10): GoogleUnavailable, GoogleAuth, new_verifier(), google_start(), google_status(), google_unlink(), google_redirects(), google_service() (+2 more)

### Community 59 - "uuid"
Cohesion: 0.14
Nodes (20): Sent, _owner_invite(), _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast(), _ana_id(), _report() (+12 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "get"
Cohesion: 0.10
Nodes (11): available_months(), delete(), delete_service(), get(), mine(), payment_details(), pdf(), remove_item() (+3 more)

### Community 62 - "networks/controller.py"
Cohesion: 0.14
Nodes (11): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+3 more)

### Community 63 - "typing"
Cohesion: 0.09
Nodes (4): Settings, GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 64 - "health/controller.py"
Cohesion: 0.16
Nodes (3): ready(), health_service(), HealthService

### Community 65 - "NetworkOut"
Cohesion: 0.11
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "checklists/controller.py"
Cohesion: 0.10
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), site_checklist_service(), ChecklistDetailOut (+2 more)

### Community 67 - "ItemsOut"
Cohesion: 0.18
Nodes (8): site_service(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteMemberOut, SitePatchIn, SitesPatchIn

### Community 68 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "limits.py"
Cohesion: 0.09
Nodes (9): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+1 more)

### Community 70 - "contracts/dto.py"
Cohesion: 0.15
Nodes (5): _contract_fields(), ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut, _network_ref()

### Community 71 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 72 - "google/controller.py"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 75 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 76 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 77 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 78 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 79 - "image"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), update(), cost_service(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "client_documents/controller.py"
Cohesion: 0.14
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 81 - "people/controller.py"
Cohesion: 0.07
Nodes (17): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+9 more)

### Community 82 - "commissions/dto.py"
Cohesion: 0.17
Nodes (5): AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn

### Community 83 - "uuid"
Cohesion: 0.18
Nodes (9): _form(), _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit() (+1 more)

### Community 85 - "modules/results/controller.py"
Cohesion: 0.15
Nodes (3): show(), result_service(), ResultService

### Community 86 - "limits.py"
Cohesion: 0.08
Nodes (8): BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.07
Nodes (17): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+9 more)

### Community 89 - "SessionCookies"
Cohesion: 0.10
Nodes (4): SessionCookies, get_cookies(), google_callback(), verify()

### Community 91 - "Actor"
Cohesion: 0.12
Nodes (8): assign_sites(), classify(), classify_many(), delete(), index(), members(), show(), unlinked()

### Community 92 - "checklists"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 96 - "test_gam_tools.py"
Cohesion: 0.13
Nodes (11): RecordingQueue, _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list() (+3 more)

### Community 97 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 98 - "networks/service.py"
Cohesion: 0.13
Nodes (4): NetworkIn, ServiceAccountOut, SyncRunOut, enqueue_sync()

### Community 127 - "events/controller.py"
Cohesion: 0.12
Nodes (4): EventSource, events(), event_service(), EventService

### Community 131 - "SiteService"
Cohesion: 0.10
Nodes (6): create(), site_options(), sites_of_member(), SiteListOut, SiteOut, SiteService

### Community 134 - "PillowImageProcessor"
Cohesion: 0.11
Nodes (12): PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client() (+4 more)

### Community 136 - "ReportService"
Cohesion: 0.05
Nodes (18): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn (+10 more)

### Community 139 - "AdUnitOut"
Cohesion: 0.16
Nodes (3): ad_units(), link(), AdUnitOut

### Community 144 - "test_mfa.py"
Cohesion: 0.38
Nodes (11): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+3 more)

### Community 145 - "InvoiceServiceOut"
Cohesion: 0.22
Nodes (4): create_service(), update_service(), InvoiceServiceIn, InvoiceServiceOut

### Community 146 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 147 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 148 - "contracts/controller.py"
Cohesion: 0.18
Nodes (5): contract(), contracts(), edit_contract(), finish_contract(), remove_contract()

### Community 150 - "test_members_without_schedules_manage_only_see_what_they_receive"
Cohesion: 0.38
Nodes (3): _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 152 - "ReportService"
Cohesion: 0.06
Nodes (16): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned() (+8 more)

### Community 155 - "company/controller.py"
Cohesion: 0.15
Nodes (5): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 160 - "ContractService"
Cohesion: 0.21
Nodes (4): contract_networks(), contract_service(), ContractNetworkOut, ContractService

### Community 163 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 166 - "main.py"
Cohesion: 0.09
Nodes (6): configure_logging(), JsonFormatter, observe(), _route_template(), create_app(), health()

### Community 175 - "_member_client"
Cohesion: 0.11
Nodes (16): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_site_category_and_responsible() (+8 more)

### Community 176 - "O que já tem"
Cohesion: 0.20
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics()

### Community 183 - "create"
Cohesion: 0.29
Nodes (3): create(), issue(), return_to_draft()

### Community 184 - "events/controller.py"
Cohesion: 0.13
Nodes (12): channel(), _parse(), RedisEvents, sse(), _collect(), _event(), ListEvents, test_events_route() (+4 more)

### Community 185 - "test_staff_sees_client_networks_sites_and_revenue_status"
Cohesion: 0.38
Nodes (3): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 188 - "test_contract_crud"
Cohesion: 0.38
Nodes (3): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission()

### Community 193 - "GAM"
Cohesion: 0.50
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1792 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **96 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `shared/dto.py`, `roles/controller.py`, `.uow`, `Actor`, `ClientService`, `CommissionService`, `test_events.py`, `ReportService`, `_month`, `SiteService`, `.trusted_uow`, `.uow`, `PageOut`, `TaskQueue`, `api_keys/controller.py`, `InvitationOut`, `PageOut`, `custom_metrics/controller.py`, `goals/controller.py`, `ReportService`, `company/controller.py`, `mfa/controller.py`, `company/controller.py`, `ContractService`, `.__init__`, `goals/service.py`, `invoices/controller.py`, `test_account.py`, `company/controller.py`, `documents/controller.py`, `networks/service.py`, `SupportTaskService`, `results/dto.py`, `Services`, `UserOut`, `.uow`, `currencies/controller.py`, `members/controller.py`, `tasks/controller.py`, `clients`, `GoogleService`, `account/controller.py`, `networks/controller.py`, `.__init__`, `NetworkOut`, `.__init__`, `checklists/controller.py`, `.__init__`, `limits.py`, `contracts/dto.py`, `ItemsOut`, `.__init__`, `GoalService`, `image`, `client_documents/controller.py`, `people/controller.py`, `commissions/dto.py`, `modules/results/controller.py`, `auth/controller.py`, `ports.py`, `networks/service.py`?**
  _High betweenness centrality (0.155) - this node is a cross-community bridge._
- **Are the 118 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 118 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.0741745816372682 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `shared/dto.py`, `roles/controller.py`, `.uow`, `Actor`, `ClientService`, `SiteService`, `test_events.py`, `ReportService`, `_month`, `.trusted_uow`, `.uow`, `api_keys/controller.py`, `InvoiceServiceOut`, `PageOut`, `InvitationOut`, `contracts/controller.py`, `ContractOut`, `ContractService`, `.page_saved`, `goals/service.py`, `invoices/controller.py`, `test_account.py`, `SupportTaskService`, `results/dto.py`, `Services`, `results`, `members/controller.py`, `tasks/controller.py`, `get`, `networks/controller.py`, `NetworkOut`, `checklists/controller.py`, `ItemsOut`, `contracts/dto.py`, `GoalTemplateOut`, `NetworkService`, `goals/controller.py`, `GoalService`, `image`, `people/controller.py`, `router.py`, `Actor`, `checklists`, `tasks`, `networks/service.py`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `shared/dto.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10931174089068826 - nodes in this community are weakly interconnected._