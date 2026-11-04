# Graph Report - avant-api  (2026-11-04)

## Corpus Check
- 290 files · ~88,054 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3889 nodes · 10656 edges · 208 communities (103 shown, 105 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1790 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `275e2333`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- DashboardService
- AlertService
- require_staff
- .save_rule
- GamToolService
- steps
- schedules/controller.py
- Avant: models do MVP
- test_company_image.py
- .trusted_uow
- GroupService
- inventory/controller.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- pydantic
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- company/controller.py
- dashboard_templates/controller.py
- invoice_pdf.py
- test_report_export.py
- clean_code.py
- CapturingMailer
- mfa/controller.py
- Avant: repositório e plano do MVP
- .uow
- CapturingMailer
- session-start.sh
- avant-api
- tasks/controller.py
- BaseModel
- invoices/controller.py
- export.py
- ItemsOut
- CompanyService
- .of
- errors.py
- MemoryBucket
- security.py
- AuthService
- views/controller.py
- test_mfa.py
- router.py
- client_notes/controller.py
- test_client_documents.py
- profile/controller.py
- edit
- currencies/controller.py
- members/controller.py
- datetime
- ItemsOut
- GoogleService
- UnitOfWorkFactory
- AccountService
- UUID
- health/controller.py
- clients/controller.py
- main.py
- mcm/service.py
- checklists
- sites/controller.py
- documents/controller.py
- Limiter
- GoalService
- google.py
- avant-api
- networks/controller.py
- uuid
- CommissionService
- Avant: conexão com o GAM
- costs/controller.py
- dollars
- set_settings
- commissions/controller.py
- test_dashboards.py
- InvoiceService
- test_events.py
- ContractService
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- checklists/dto.py
- Actor
- checklists/controller.py
- clients
- SupportTaskService
- Actor
- FiscalDataOut
- Actor
- http.py
- client_documents/controller.py
- _csv_cell
- SiteListOut
- dollars
- SiteListOut
- reports/service.py
- ClientOut
- account/controller.py
- TaskDetailOut
- Services
- TaskQueue
- _staff
- ad_units
- test_goals.py
- export.py
- ContractNetworkOut
- SiteService
- AuditService
- reports/controller.py
- tasks/dto.py
- CompanyFiscalOut
- Actor
- SiteService
- test_company_image.py
- Suporte
- RedisCounter
- do_reset_password
- O que já tem
- service_options
- .__init__
- DashboardTemplateOut
- delete_session
- .of
- .available_months
- GAM
- .assign
- events/controller.py
- SessionCookies
- .create
- RedisEvents
- events.py
- Bucket
- edit_client
- manager_change
- _month
- TaskPatchIn
- client_options
- ClientService
- is_exempt

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 149 edges
2. `PageOut` - 145 edges
3. `_csrf()` - 133 edges
4. `_onboard_owner()` - 133 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 118 edges
8. `ReportService` - 79 edges
9. `_staff()` - 64 edges
10. `page_out()` - 59 edges

## Surprising Connections (you probably didn't know these)
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/modules/company/controller.py
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

## Communities (208 total, 105 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.12
Nodes (22): _admin_role(), NextMonthClock, test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions(), test_groone_role_with_the_whole_catalog(), test_manager_change_preview() (+14 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.16
Nodes (5): contract_networks(), contracts(), edit_contract(), finish_contract(), remove_contract()

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.06
Nodes (24): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+16 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "require_staff"
Cohesion: 0.11
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 6 - ".save_rule"
Cohesion: 0.12
Nodes (8): adjust(), create_rule(), delete_rule(), person(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 7 - "GamToolService"
Cohesion: 0.06
Nodes (19): ads_txt(), install(), network(), networks(), run(), runs(), start(), gam_tool_service() (+11 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.12
Nodes (16): Acesso, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), Identidade, MemberPermission, PasswordReset (+8 more)

### Community 11 - "test_company_image.py"
Cohesion: 0.11
Nodes (16): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_site_category_and_responsible() (+8 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/controller.py"
Cohesion: 0.13
Nodes (7): networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, PageOut

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "pydantic"
Cohesion: 0.10
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService, InvitationOut

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "company/controller.py"
Cohesion: 0.13
Nodes (3): image(), image_response(), image_upload()

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "test_report_export.py"
Cohesion: 0.28
Nodes (3): _result(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 27 - "CapturingMailer"
Cohesion: 0.23
Nodes (14): _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas() (+6 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.11
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 32 - "CapturingMailer"
Cohesion: 0.09
Nodes (29): CapturingMailer, Sent, _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit() (+21 more)

### Community 36 - "tasks/controller.py"
Cohesion: 0.22
Nodes (4): change(), comment(), create(), task()

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - "invoices/controller.py"
Cohesion: 0.10
Nodes (10): FiscalDataIn, mine(), service_options(), invoice_service(), InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, ReturnedOut (+2 more)

### Community 39 - "export.py"
Cohesion: 0.27
Nodes (5): _header(), _metric_label(), _rows(), to_csv(), to_xlsx()

### Community 40 - "ItemsOut"
Cohesion: 0.13
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 41 - "CompanyService"
Cohesion: 0.16
Nodes (5): remove_image(), show(), CompanyDetailOut, CompanyPatchIn, CompanyService

### Community 43 - "errors.py"
Cohesion: 0.11
Nodes (8): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), QueryTooHeavy, PillowImageProcessor

### Community 44 - "MemoryBucket"
Cohesion: 0.13
Nodes (7): TooManyAttempts, BucketResult, BucketRule, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 45 - "security.py"
Cohesion: 0.07
Nodes (19): CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor() (+11 more)

### Community 46 - "AuthService"
Cohesion: 0.11
Nodes (4): accept(), get_invitation(), InvitationPreviewOut, AuthService

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (10): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+2 more)

### Community 48 - "test_mfa.py"
Cohesion: 0.22
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 49 - "router.py"
Cohesion: 0.07
Nodes (8): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, default_period(), ResultService

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (8): add(), delete(), edit(), notes(), ClientNoteIn, ClientNoteOut, NotePersonOut, ClientNoteService

### Community 51 - "test_client_documents.py"
Cohesion: 0.12
Nodes (11): _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _support(), _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company() (+3 more)

### Community 52 - "profile/controller.py"
Cohesion: 0.10
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 53 - "edit"
Cohesion: 0.15
Nodes (12): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+4 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (16): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+8 more)

### Community 56 - "datetime"
Cohesion: 0.10
Nodes (4): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone()

### Community 57 - "ItemsOut"
Cohesion: 0.13
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 58 - "GoogleService"
Cohesion: 0.07
Nodes (7): GoogleUnavailable, GoogleAuth, google_callback(), google_start(), google_status(), google_unlink(), GoogleService

### Community 60 - "AccountService"
Cohesion: 0.18
Nodes (4): do_change_password(), get_sessions(), revoke_others(), AccountService

### Community 61 - "UUID"
Cohesion: 0.10
Nodes (13): add_item(), create(), delete(), delete_service(), get(), pay(), payment_details(), pdf() (+5 more)

### Community 62 - "health/controller.py"
Cohesion: 0.14
Nodes (4): health(), ready(), health_service(), HealthService

### Community 63 - "clients/controller.py"
Cohesion: 0.18
Nodes (10): invite_owner(), ClientDetailOut, ClientIn, ClientOptionOut, ClientOut, ClientPatchIn, ClientStatusIn, OwnerChangeIn (+2 more)

### Community 64 - "main.py"
Cohesion: 0.05
Nodes (12): _google(), _mailer(), NoEvents, RedisBucket, configure_logging(), observe(), _route_template(), Settings (+4 more)

### Community 65 - "mcm/service.py"
Cohesion: 0.10
Nodes (6): assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "checklists"
Cohesion: 0.15
Nodes (5): checklists(), months(), summary(), ChecklistMonthOut, SiteChecklistService

### Community 67 - "sites/controller.py"
Cohesion: 0.18
Nodes (11): classify(), classify_many(), link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn (+3 more)

### Community 68 - "documents/controller.py"
Cohesion: 0.07
Nodes (9): documents(), download(), upload(), document_service(), DocumentService, document_response(), document_upload(), DocumentOut (+1 more)

### Community 69 - "Limiter"
Cohesion: 0.13
Nodes (6): Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "GoalService"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+10 more)

### Community 72 - "google.py"
Cohesion: 0.05
Nodes (12): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), get_cookies(), google_redirects() (+4 more)

### Community 74 - "networks/controller.py"
Cohesion: 0.08
Nodes (13): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+5 more)

### Community 75 - "uuid"
Cohesion: 0.19
Nodes (19): _csrf(), test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused() (+11 more)

### Community 77 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "dollars"
Cohesion: 0.12
Nodes (3): mine(), dollars(), MyCommissionsOut

### Community 81 - "set_settings"
Cohesion: 0.13
Nodes (6): disable(), enable(), reset_mfa(), users(), people_service(), PeopleService

### Community 82 - "commissions/controller.py"
Cohesion: 0.24
Nodes (8): set_settings(), AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn, PersonMonthOut, WindowMonthOut

### Community 83 - "test_dashboards.py"
Cohesion: 0.14
Nodes (13): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), _kpi(), _run() (+5 more)

### Community 84 - "InvoiceService"
Cohesion: 0.19
Nodes (5): create_service(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 85 - "test_events.py"
Cohesion: 0.10
Nodes (18): client(), engine(), mailer(), _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password() (+10 more)

### Community 86 - "ContractService"
Cohesion: 0.20
Nodes (3): contract(), ContractOut, ContractService

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.12
Nodes (14): Company, Empresa e equipe, Invitation, Membership, Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Imagem da Empresa (+6 more)

### Community 88 - "auth/controller.py"
Cohesion: 0.13
Nodes (11): company_image(), do_logout(), login(), me(), set_active_company(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut (+3 more)

### Community 89 - "checklists/dto.py"
Cohesion: 0.14
Nodes (3): ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 91 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), delete(), index(), show(), sites_of_member(), unlinked()

### Community 92 - "checklists/controller.py"
Cohesion: 0.15
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistDetailOut, ChecklistMarkIn (+2 more)

### Community 95 - "SupportTaskService"
Cohesion: 0.15
Nodes (4): tasks(), support_task_service(), TaskOut, SupportTaskService

### Community 96 - "Actor"
Cohesion: 0.13
Nodes (8): audit(), cancel_owner(), change_status(), client(), client_image(), edit_client_image(), owner_invitations(), remove_client_image()

### Community 97 - "FiscalDataOut"
Cohesion: 0.15
Nodes (3): save_payment_details(), PayeeDetailsOut, FiscalDataOut

### Community 128 - "client_documents/controller.py"
Cohesion: 0.09
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 132 - "SiteListOut"
Cohesion: 0.17
Nodes (3): create(), site_options(), SiteListOut

### Community 133 - "dollars"
Cohesion: 0.13
Nodes (3): PersonOut, person_out(), UserOut

### Community 135 - "SiteListOut"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 136 - "reports/service.py"
Cohesion: 0.05
Nodes (22): templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn (+14 more)

### Community 137 - "ClientOut"
Cohesion: 0.13
Nodes (3): ClientProfileOut, ClientRefOut, image_url()

### Community 138 - "account/controller.py"
Cohesion: 0.30
Nodes (5): ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut, SessionOut

### Community 142 - "Services"
Cohesion: 0.04
Nodes (18): Services, get_services(), account_service(), audit_service(), auth_service(), company_service(), checklist_item_service(), site_checklist_service() (+10 more)

### Community 144 - "_staff"
Cohesion: 0.13
Nodes (11): RecordingQueue, _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list() (+3 more)

### Community 146 - "test_goals.py"
Cohesion: 0.43
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 148 - "ContractNetworkOut"
Cohesion: 0.19
Nodes (5): ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut, _network_ref()

### Community 149 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 152 - "reports/controller.py"
Cohesion: 0.07
Nodes (18): catalog(), create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index() (+10 more)

### Community 155 - "CompanyFiscalOut"
Cohesion: 0.13
Nodes (4): edit_fiscal(), edit_image(), fiscal(), CompanyFiscalOut

### Community 161 - "test_company_image.py"
Cohesion: 0.31
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 165 - "O que já tem"
Cohesion: 0.20
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics()

### Community 177 - "GAM"
Cohesion: 0.33
Nodes (6): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment

### Community 178 - ".assign"
Cohesion: 0.40
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 184 - "events.py"
Cohesion: 0.16
Nodes (5): channel(), EventSource, _parse(), sse(), EventService

### Community 194 - "ClientService"
Cohesion: 0.13
Nodes (6): client_teams(), client_service(), ClientMemberOut, ClientService, AuditOut, CompanyRefOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1781 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **105 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `client_documents/controller.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `GamToolService`, `reports/service.py`, `schedules/controller.py`, `account/controller.py`, `.trusted_uow`, `GroupService`, `inventory/controller.py`, `TaskQueue`, `api_keys/controller.py`, `pydantic`, `custom_metrics/controller.py`, `SiteService`, `AuditService`, `dashboard_templates/controller.py`, `tasks/dto.py`, `mfa/controller.py`, `.uow`, `.__init__`, `invoices/controller.py`, `.__init__`, `CompanyService`, `ItemsOut`, `security.py`, `AuthService`, `views/controller.py`, `.__init__`, `router.py`, `client_notes/controller.py`, `profile/controller.py`, `currencies/controller.py`, `members/controller.py`, `ItemsOut`, `GoogleService`, `.__init__`, `AccountService`, `Bucket`, `clients/controller.py`, `mcm/service.py`, `checklists`, `ClientService`, `documents/controller.py`, `.__init__`, `sites/controller.py`, `GoalService`, `.__init__`, `.__init__`, `.__init__`, `CommissionService`, `networks/controller.py`, `costs/controller.py`, `set_settings`, `commissions/controller.py`, `InvoiceService`, `ContractService`, `SupportTaskService`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Are the 110 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 110 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.11666666666666667 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `inventory/controller.py` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `dollars`, `Actor`, `GamToolService`, `reports/service.py`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `api_keys/controller.py`, `pydantic`, `SiteService`, `AuditService`, `tasks/dto.py`, `tasks/controller.py`, `invoices/controller.py`, `ItemsOut`, `security.py`, `router.py`, `client_notes/controller.py`, `members/controller.py`, `UnitOfWorkFactory`, `UUID`, `clients/controller.py`, `mcm/service.py`, `checklists`, `ClientService`, `sites/controller.py`, `.trusted_uow`, `GoalService`, `networks/controller.py`, `costs/controller.py`, `set_settings`, `InvoiceService`, `ContractService`, `Actor`, `checklists/controller.py`, `clients`, `SupportTaskService`, `Actor`, `Actor`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07792207792207792 - nodes in this community are weakly interconnected._