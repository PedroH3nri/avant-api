# Graph Report - avant-api  (2026-11-04)

## Corpus Check
- 290 files · ~86,670 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3856 nodes · 10531 edges · 188 communities (104 shown, 84 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1763 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `b7461200`
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
- http.py
- dashboard_templates/controller.py
- invoice_pdf.py
- audit/controller.py
- clean_code.py
- CapturingMailer
- mfa/controller.py
- Avant: repositório e plano do MVP
- .run_guarded
- FiscalDataIn
- _onboard_owner
- session-start.sh
- avant-api
- SupportTaskService
- BaseModel
- invoices/controller.py
- export.py
- ItemsOut
- CompanyService
- auth/controller.py
- install
- MemoryBucket
- test_networks.py
- views/controller.py
- test_mfa.py
- avant_core_access_models
- client_notes/controller.py
- tasks/controller.py
- profile/controller.py
- edit
- currencies/controller.py
- members/controller.py
- datetime
- ItemsOut
- GoogleService
- checklists/controller.py
- account/controller.py
- UUID
- health/controller.py
- clients/controller.py
- Actor
- mcm/controller.py
- checklists
- sites/controller.py
- documents/controller.py
- Limiter
- .trusted_uow
- GoalService
- google.py
- avant-api
- networks/controller.py
- uuid
- UserOut
- Avant: conexão com o GAM
- test_company_image.py
- costs/controller.py
- _month
- set_settings
- test_dashboards.py
- InvoiceServiceOut
- test_events.py
- download
- Avant: grupos na Empresa e imagem da Empresa
- AuthService
- checklists/dto.py
- get
- commissions/controller.py
- clients
- goals/controller.py
- Actor
- update_item
- Actor
- .assign
- client_documents/controller.py
- google_callback
- test_alerts.py
- GoalTemplateIn
- dollars
- SiteListOut
- reports/service.py
- ClientOut
- person
- mine
- Services
- UnitOfWorkFactory
- _staff
- templates
- CapturingMailer
- tasks
- ad_units
- goals/service.py
- team
- Actor
- image
- AuditOut
- Actor
- SiteService
- client_image
- Suporte
- .delete_service
- TaskPatchIn
- service_options
- company/controller.py
- document_response
- main.py
- events.py
- ClientService

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 146 edges
2. `PageOut` - 145 edges
3. `_csrf()` - 130 edges
4. `_onboard_owner()` - 130 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 118 edges
8. `ReportService` - 75 edges
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

## Communities (188 total, 84 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.09
Nodes (31): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+23 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.05
Nodes (24): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem, metrics(), contract(), contract_networks() (+16 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.06
Nodes (23): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+15 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "require_staff"
Cohesion: 0.08
Nodes (17): CsrfFailed, NoActiveCompany, RateLimited, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth() (+9 more)

### Community 6 - ".save_rule"
Cohesion: 0.16
Nodes (5): create_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 7 - "GamToolService"
Cohesion: 0.06
Nodes (17): ads_txt(), install(), network(), networks(), run(), runs(), start(), AdsTxtOut (+9 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (21): Acesso, AdUnit, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, GAM, Identidade (+13 more)

### Community 11 - "test_company_image.py"
Cohesion: 0.08
Nodes (19): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture() (+11 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/controller.py"
Cohesion: 0.07
Nodes (11): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService (+3 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "pydantic"
Cohesion: 0.09
Nodes (6): cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService

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

### Community 22 - "http.py"
Cohesion: 0.18
Nodes (3): client_info(), image_response(), image_upload()

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "audit/controller.py"
Cohesion: 0.13
Nodes (3): require(), index(), AuditService

### Community 26 - "clean_code.py"
Cohesion: 0.15
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "CapturingMailer"
Cohesion: 0.23
Nodes (12): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (8): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut, MfaService

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 32 - "_onboard_owner"
Cohesion: 0.21
Nodes (16): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format(), test_costs_and_reports_come_in_pages() (+8 more)

### Community 36 - "SupportTaskService"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - "invoices/controller.py"
Cohesion: 0.27
Nodes (8): AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn, ServiceItemIn

### Community 39 - "export.py"
Cohesion: 0.10
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 40 - "ItemsOut"
Cohesion: 0.11
Nodes (8): invite(), options(), staff(), StaffInviteIn, StaffService, options(), InvitationOut, MemberOut

### Community 41 - "CompanyService"
Cohesion: 0.20
Nodes (4): show(), CompanyDetailOut, CompanyPatchIn, CompanyService

### Community 42 - "auth/controller.py"
Cohesion: 0.11
Nodes (12): SessionCookies, get_cookies(), get_invitation(), login(), auth_service(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut (+4 more)

### Community 43 - "install"
Cohesion: 0.09
Nodes (9): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), QueryTooHeavy, TooManyAttempts (+1 more)

### Community 44 - "MemoryBucket"
Cohesion: 0.06
Nodes (10): Bucket, BucketResult, BucketRule, MemoryBucket, MemoryCounter, RedisBucket, RedisCounter, _exercise() (+2 more)

### Community 46 - "test_networks.py"
Cohesion: 0.47
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "test_mfa.py"
Cohesion: 0.18
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 49 - "avant_core_access_models"
Cohesion: 0.06
Nodes (10): results(), client_result_service(), ClientResultService, show(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut (+2 more)

### Community 50 - "client_notes/controller.py"
Cohesion: 0.09
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "tasks/controller.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 52 - "profile/controller.py"
Cohesion: 0.08
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.15
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (13): edit(), index(), leave(), remove(), set_permissions(), show(), member_service(), DirectPermissionIn (+5 more)

### Community 56 - "datetime"
Cohesion: 0.17
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 57 - "ItemsOut"
Cohesion: 0.12
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 58 - "GoogleService"
Cohesion: 0.05
Nodes (11): GoogleUnavailable, GoogleAuth, new_verifier(), google_start(), google_status(), google_unlink(), google_redirects(), google_service() (+3 more)

### Community 59 - "checklists/controller.py"
Cohesion: 0.09
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), site_checklist_service(), ChecklistDetailOut (+2 more)

### Community 60 - "account/controller.py"
Cohesion: 0.10
Nodes (12): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn (+4 more)

### Community 61 - "UUID"
Cohesion: 0.16
Nodes (7): add_item(), create(), delete(), issue(), pay(), remove_item(), return_to_draft()

### Community 62 - "health/controller.py"
Cohesion: 0.14
Nodes (4): health(), ready(), health_service(), HealthService

### Community 63 - "clients/controller.py"
Cohesion: 0.15
Nodes (9): new_owner(), register_client(), ClientIn, ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn (+1 more)

### Community 64 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), delete(), index(), show(), sites_of_member(), unlinked()

### Community 65 - "mcm/controller.py"
Cohesion: 0.08
Nodes (8): require_staff(), assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "checklists"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 67 - "sites/controller.py"
Cohesion: 0.18
Nodes (11): classify(), classify_many(), link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn (+3 more)

### Community 68 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 69 - "Limiter"
Cohesion: 0.11
Nodes (6): Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 72 - "google.py"
Cohesion: 0.09
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 74 - "networks/controller.py"
Cohesion: 0.07
Nodes (14): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+6 more)

### Community 75 - "uuid"
Cohesion: 0.14
Nodes (19): _owner_invite(), _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast(), _ana_id(), _report(), test_chart_options_keep_metric_styles() (+11 more)

### Community 76 - "UserOut"
Cohesion: 0.10
Nodes (10): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+2 more)

### Community 77 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 78 - "test_company_image.py"
Cohesion: 0.31
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 79 - "costs/controller.py"
Cohesion: 0.09
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "_month"
Cohesion: 0.13
Nodes (5): mine(), _month(), team(), PersonMonthOut, CommissionService

### Community 83 - "test_dashboards.py"
Cohesion: 0.28
Nodes (7): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit()

### Community 84 - "InvoiceServiceOut"
Cohesion: 0.16
Nodes (6): create_service(), update_service(), invoice_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 85 - "test_events.py"
Cohesion: 0.09
Nodes (16): client(), engine(), mailer(), Sent, _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys() (+8 more)

### Community 86 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "AuthService"
Cohesion: 0.08
Nodes (6): accept(), company_image(), do_logout(), me(), set_active_company(), AuthService

### Community 89 - "checklists/dto.py"
Cohesion: 0.09
Nodes (6): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 91 - "get"
Cohesion: 0.14
Nodes (7): available_months(), get(), mine(), payment_details(), pdf(), services(), team()

### Community 92 - "commissions/controller.py"
Cohesion: 0.22
Nodes (7): commission_service(), AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn, MyCommissionsOut

### Community 95 - "goals/controller.py"
Cohesion: 0.18
Nodes (5): delete_template(), role_goals(), set_role_goal(), update_template(), RoleGoalIn

### Community 96 - "Actor"
Cohesion: 0.16
Nodes (7): audit(), cancel_owner(), change_status(), client_options(), edit_client_image(), invite_owner(), remove_client_image()

### Community 98 - "Actor"
Cohesion: 0.17
Nodes (4): owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 127 - ".assign"
Cohesion: 0.40
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 128 - "client_documents/controller.py"
Cohesion: 0.14
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 131 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 135 - "SiteListOut"
Cohesion: 0.17
Nodes (3): create(), site_options(), SiteListOut

### Community 136 - "reports/service.py"
Cohesion: 0.05
Nodes (16): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn (+8 more)

### Community 139 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 142 - "Services"
Cohesion: 0.05
Nodes (15): Estrutura, Services, get_services(), TaskQueue, account_service(), audit_service(), cost_service(), checklist_item_service() (+7 more)

### Community 143 - "UnitOfWorkFactory"
Cohesion: 0.06
Nodes (3): UnitOfWorkFactory, image_url(), RoleRefOut

### Community 144 - "_staff"
Cohesion: 0.09
Nodes (13): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _checklists() (+5 more)

### Community 146 - "CapturingMailer"
Cohesion: 0.14
Nodes (10): CapturingMailer, _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited(), _template() (+2 more)

### Community 147 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 150 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 152 - "Actor"
Cohesion: 0.06
Nodes (18): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+10 more)

### Community 158 - "Actor"
Cohesion: 0.15
Nodes (3): adjust(), delete_rule(), settings()

### Community 160 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 162 - "Suporte"
Cohesion: 0.40
Nodes (5): ApiKey, AuditLog, PasswordReset, Session, Suporte

### Community 171 - "company/controller.py"
Cohesion: 0.17
Nodes (5): edit_fiscal(), edit_image(), fiscal(), remove_image(), company_service()

### Community 180 - "main.py"
Cohesion: 0.04
Nodes (12): _google(), _mailer(), configure_logging(), JsonFormatter, observe(), _route_template(), Settings, CeleryQueue (+4 more)

### Community 184 - "events.py"
Cohesion: 0.08
Nodes (9): channel(), EventSource, NoEvents, _parse(), RedisEvents, sse(), events(), EventService (+1 more)

### Community 194 - "ClientService"
Cohesion: 0.15
Nodes (6): client_teams(), manager_change(), client_service(), ClientMemberOut, ManagerChangeOut, ClientService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1765 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **84 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `client_documents/controller.py`, `.__init__`, `contracts/controller.py`, `DashboardService`, `AlertService`, `roles/controller.py`, `GamToolService`, `reports/service.py`, `schedules/controller.py`, `GroupService`, `inventory/controller.py`, `api_keys/controller.py`, `pydantic`, `custom_metrics/controller.py`, `goals/service.py`, `dashboard_templates/controller.py`, `Actor`, `audit/controller.py`, `mfa/controller.py`, `SiteService`, `SupportTaskService`, `invoices/controller.py`, `.__init__`, `.__init__`, `CompanyService`, `auth/controller.py`, `ItemsOut`, `MemoryBucket`, `.__init__`, `views/controller.py`, `avant_core_access_models`, `client_notes/controller.py`, `tasks/controller.py`, `profile/controller.py`, `currencies/controller.py`, `members/controller.py`, `ItemsOut`, `GoogleService`, `.__init__`, `account/controller.py`, `checklists/controller.py`, `mcm/controller.py`, `ClientService`, `sites/controller.py`, `documents/controller.py`, `Limiter`, `.trusted_uow`, `GoalService`, `networks/controller.py`, `UserOut`, `costs/controller.py`, `_month`, `InvoiceServiceOut`, `AuthService`, `commissions/controller.py`?**
  _High betweenness centrality (0.124) - this node is a cross-community bridge._
- **Are the 107 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 107 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.08701923076923077 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `inventory/controller.py` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `Actor`, `GamToolService`, `reports/service.py`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `UnitOfWorkFactory`, `api_keys/controller.py`, `pydantic`, `tasks`, `goals/service.py`, `Actor`, `audit/controller.py`, `AuditOut`, `SiteService`, `SupportTaskService`, `invoices/controller.py`, `ItemsOut`, `avant_core_access_models`, `client_notes/controller.py`, `tasks/controller.py`, `members/controller.py`, `checklists/controller.py`, `clients/controller.py`, `Actor`, `mcm/controller.py`, `checklists`, `ClientService`, `sites/controller.py`, `GoalService`, `networks/controller.py`, `UserOut`, `costs/controller.py`, `InvoiceServiceOut`, `get`, `clients`, `goals/controller.py`, `Actor`, `Actor`?**
  _High betweenness centrality (0.077) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05432098765432099 - nodes in this community are weakly interconnected._