# Graph Report - avant-api  (2026-11-04)

## Corpus Check
- 290 files · ~89,421 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3923 nodes · 10792 edges · 200 communities (110 shown, 90 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1811 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f46ab456`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- clients/service.py
- roles/controller.py
- .uow
- Actor
- ClientService
- CommissionService
- test_events.py
- steps
- _month
- Avant: models do MVP
- conftest.py
- .trusted_uow
- .uow
- networks/controller.py
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
- uuid
- account/controller.py
- get
- networks/controller.py
- Actor
- health/controller.py
- NetworkOut
- checklists/controller.py
- ItemsOut
- io
- limits.py
- contracts/controller.py
- GoalTemplateOut
- google/controller.py
- avant-api
- NetworkService
- mine
- goals/controller.py
- GoalService
- Arquitetura do MVP do Avant
- image
- client_documents/controller.py
- people/controller.py
- commissions/dto.py
- uuid
- image_url
- require
- images.py
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- .of
- Actor
- checklists
- UnitOfWorkFactory
- update_item
- test_gam_tools.py
- tasks
- networks/service.py
- .run_guarded
- mine
- Avant: conexão com o GAM
- SiteOut
- SiteListOut
- ClientService
- test_company_image.py
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
- export.py
- _xlsx_cell
- CompanyService
- test_alerts.py
- ReportService
- company/controller.py
- FiscalDataIn
- _onboard_owner
- image
- .page_saved
- _staff
- main.py
- clients/controller.py
- client_image
- edit_image
- dollars
- CommissionRuleOut
- test_sites.py
- edit_client
- test_staff_manage_templates_and_clients_see_them_by_role
- delete_template
- SiteDetailOut
- Suporte
- dimension_text
- events/controller.py
- TaskPatchIn
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

## Communities (200 total, 90 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.13
Nodes (19): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+11 more)

### Community 1 - "clients/service.py"
Cohesion: 0.17
Nodes (6): ClientDetailOut, ClientMemberOut, ClientOut, AuditOut, CompanyRefOut, RevenueStatusOut

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.05
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "ClientService"
Cohesion: 0.10
Nodes (4): invite_owner(), owner_invitations(), OwnerInvitationOut, owner_invitation_out()

### Community 6 - "CommissionService"
Cohesion: 0.18
Nodes (3): set_settings(), commission_service(), CommissionService

### Community 7 - "test_events.py"
Cohesion: 0.06
Nodes (18): ads_txt(), install(), network(), networks(), run(), runs(), start(), AdsTxtOut (+10 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (21): Acesso, AdUnit, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, GAM, Identidade (+13 more)

### Community 11 - "conftest.py"
Cohesion: 0.08
Nodes (20): client(), engine(), mailer(), _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit() (+12 more)

### Community 12 - ".trusted_uow"
Cohesion: 0.11
Nodes (3): remove_item(), InvoiceOut, InvoiceService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "networks/controller.py"
Cohesion: 0.13
Nodes (6): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteOut, ClientInventoryService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.10
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService

### Community 18 - "PageOut"
Cohesion: 0.14
Nodes (4): index(), audit_service(), AuditService, PageOut

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
Cohesion: 0.18
Nodes (3): client_info(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.23
Nodes (14): _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas() (+6 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.07
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 32 - "_onboard_owner"
Cohesion: 0.13
Nodes (18): CapturingMailer, Sent, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login() (+10 more)

### Community 36 - "Services"
Cohesion: 0.05
Nodes (14): _google(), _mailer(), NoEvents, Bucket, BucketResult, BucketRule, MemoryBucket, MemoryCounter (+6 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - "invoices/controller.py"
Cohesion: 0.18
Nodes (11): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut (+3 more)

### Community 39 - ".save_rule"
Cohesion: 0.16
Nodes (6): adjust(), create_rule(), delete_rule(), rules(), update_rule(), CommissionRuleIn

### Community 40 - "test_account.py"
Cohesion: 0.10
Nodes (6): invite(), options(), staff(), StaffInviteIn, StaffService, InvitationOut

### Community 41 - "company/controller.py"
Cohesion: 0.20
Nodes (4): show(), CompanyDetailOut, CompanyPatchIn, CompanyService

### Community 42 - "documents/controller.py"
Cohesion: 0.07
Nodes (9): documents(), download(), upload(), document_service(), DocumentService, document_response(), document_upload(), DocumentOut (+1 more)

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "checklists/dto.py"
Cohesion: 0.14
Nodes (4): ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 45 - "security.py"
Cohesion: 0.06
Nodes (19): Services, api_key_actor(), bearer_token(), check_tab_company(), get_actor(), get_auth(), get_services(), get_session_actor() (+11 more)

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
Cohesion: 0.05
Nodes (10): results(), client_result_service(), ClientResultService, show(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut (+2 more)

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "profile/controller.py"
Cohesion: 0.20
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 52 - "UserOut"
Cohesion: 0.17
Nodes (3): PersonOut, person_out(), UserOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

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
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "GoogleService"
Cohesion: 0.05
Nodes (13): CompanyChanged, CsrfFailed, GoogleUnavailable, NoActiveCompany, QueryTooHeavy, GoogleAuth, new_verifier(), check_csrf() (+5 more)

### Community 59 - "uuid"
Cohesion: 0.30
Nodes (14): _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency(), test_pinned_reports_and_preview_refresh() (+6 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "get"
Cohesion: 0.08
Nodes (15): health(), add_item(), create(), delete(), delete_service(), get(), issue(), mine() (+7 more)

### Community 62 - "networks/controller.py"
Cohesion: 0.15
Nodes (8): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs(), network_service()

### Community 63 - "Actor"
Cohesion: 0.13
Nodes (9): audit(), cancel_owner(), change_status(), client(), client_teams(), edit_client_image(), new_owner(), remove_client_image() (+1 more)

### Community 64 - "health/controller.py"
Cohesion: 0.17
Nodes (3): ready(), health_service(), HealthService

### Community 65 - "NetworkOut"
Cohesion: 0.11
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "checklists/controller.py"
Cohesion: 0.10
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistDetailOut, ChecklistMarkIn (+2 more)

### Community 67 - "ItemsOut"
Cohesion: 0.19
Nodes (6): site_service(), AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 68 - "io"
Cohesion: 0.21
Nodes (7): _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters()

### Community 69 - "limits.py"
Cohesion: 0.06
Nodes (10): TooManyAttempts, Counter, Limiter, RedisCounter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round() (+2 more)

### Community 70 - "contracts/controller.py"
Cohesion: 0.06
Nodes (25): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+17 more)

### Community 71 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 72 - "google/controller.py"
Cohesion: 0.09
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 74 - "NetworkService"
Cohesion: 0.19
Nodes (3): options(), NetworkDetailOut, NetworkService

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
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "client_documents/controller.py"
Cohesion: 0.08
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 81 - "people/controller.py"
Cohesion: 0.13
Nodes (7): Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PeopleService

### Community 82 - "commissions/dto.py"
Cohesion: 0.17
Nodes (5): AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 85 - "require"
Cohesion: 0.18
Nodes (4): require(), dependency(), require_report(), require_session()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.05
Nodes (19): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), get_invitation(), login(), me() (+11 more)

### Community 91 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), classify(), classify_many(), delete(), show(), unlinked()

### Community 92 - "checklists"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 94 - "UnitOfWorkFactory"
Cohesion: 0.07
Nodes (4): UnitOfWorkFactory, ClientSiteChecklistOut, image_url(), page_out()

### Community 96 - "test_gam_tools.py"
Cohesion: 0.13
Nodes (10): _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list(), test_staff_marks_checks_and_writes_notes() (+2 more)

### Community 97 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 98 - "networks/service.py"
Cohesion: 0.24
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 127 - ".run_guarded"
Cohesion: 0.12
Nodes (3): ReportRangeOut, ReportRowOut, _statement_timeout()

### Community 129 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 131 - "SiteOut"
Cohesion: 0.13
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 132 - "SiteListOut"
Cohesion: 0.18
Nodes (3): index(), site_options(), SiteListOut

### Community 133 - "ClientService"
Cohesion: 0.17
Nodes (4): manager_change(), client_service(), ManagerChangeOut, ClientService

### Community 134 - "test_company_image.py"
Cohesion: 0.29
Nodes (5): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), test_upload_without_session_is_refused_before_reading_the_body()

### Community 136 - "ReportService"
Cohesion: 0.05
Nodes (18): catalog(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut (+10 more)

### Community 139 - "AdUnitOut"
Cohesion: 0.21
Nodes (3): ad_units(), link(), AdUnitOut

### Community 142 - ".show"
Cohesion: 0.18
Nodes (3): register_client(), ClientIn, ClientProfileOut

### Community 144 - "test_mfa.py"
Cohesion: 0.20
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+6 more)

### Community 145 - "InvoiceServiceOut"
Cohesion: 0.25
Nodes (3): create_service(), update_service(), InvoiceServiceOut

### Community 146 - "_marketing_client"
Cohesion: 0.26
Nodes (4): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone()

### Community 149 - "CompanyService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 150 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 152 - "ReportService"
Cohesion: 0.06
Nodes (18): RateLimited, create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin() (+10 more)

### Community 153 - "company/controller.py"
Cohesion: 0.17
Nodes (5): edit_fiscal(), edit_image(), fiscal(), remove_image(), company_service()

### Community 158 - "_onboard_owner"
Cohesion: 0.14
Nodes (17): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session(), test_team_invitation_flow() (+9 more)

### Community 163 - "_staff"
Cohesion: 0.11
Nodes (16): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal(), _staff(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_groone_routes_need_the_session_with_2fa() (+8 more)

### Community 166 - "main.py"
Cohesion: 0.05
Nodes (10): configure_logging(), JsonFormatter, observe(), _route_template(), Settings, create_app(), google_redirects(), GoogleRedirects (+2 more)

### Community 167 - "clients/controller.py"
Cohesion: 0.17
Nodes (5): client_options(), ClientOptionOut, ClientProfileIn, ClientStatusIn, OwnerChangeIn

### Community 175 - "test_sites.py"
Cohesion: 0.16
Nodes (7): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _inventory(), test_manual_site(), test_site_category_and_responsible(), test_sites_and_assignment()

### Community 177 - "test_staff_manage_templates_and_clients_see_them_by_role"
Cohesion: 0.38
Nodes (3): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company()

### Community 180 - "Suporte"
Cohesion: 0.40
Nodes (5): ApiKey, AuditLog, PasswordReset, Session, Suporte

### Community 184 - "events/controller.py"
Cohesion: 0.07
Nodes (15): channel(), EventSource, _parse(), RedisEvents, sse(), events(), event_service(), EventService (+7 more)

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1789 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **90 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `clients/service.py`, `roles/controller.py`, `.uow`, `Actor`, `ClientService`, `CommissionService`, `test_events.py`, `ReportService`, `_month`, `.trusted_uow`, `.uow`, `networks/controller.py`, `TaskQueue`, `api_keys/controller.py`, `InvitationOut`, `PageOut`, `custom_metrics/controller.py`, `CompanyService`, `goals/controller.py`, `ReportService`, `mfa/controller.py`, `company/controller.py`, `.__init__`, `goals/service.py`, `invoices/controller.py`, `test_account.py`, `company/controller.py`, `documents/controller.py`, `networks/service.py`, `SupportTaskService`, `PageOut`, `Services`, `profile/controller.py`, `UserOut`, `currencies/controller.py`, `members/controller.py`, `tasks/controller.py`, `clients`, `GoogleService`, `account/controller.py`, `.__init__`, `.__init__`, `.__init__`, `NetworkOut`, `.__init__`, `checklists/controller.py`, `.__init__`, `.__init__`, `contracts/controller.py`, `ItemsOut`, `NetworkService`, `GoalService`, `image`, `client_documents/controller.py`, `people/controller.py`, `commissions/dto.py`, `auth/controller.py`, `networks/service.py`?**
  _High betweenness centrality (0.157) - this node is a cross-community bridge._
- **Are the 118 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 118 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.13086770981507823 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `clients/service.py`, `roles/controller.py`, `.uow`, `Actor`, `ClientService`, `ClientService`, `test_events.py`, `ReportService`, `_month`, `SiteListOut`, `SiteOut`, `.trusted_uow`, `.uow`, `networks/controller.py`, `api_keys/controller.py`, `InvitationOut`, `CompanyService`, `.page_saved`, `goals/service.py`, `invoices/controller.py`, `clients/controller.py`, `test_account.py`, `SupportTaskService`, `PageOut`, `Services`, `UserOut`, `members/controller.py`, `tasks/controller.py`, `get`, `networks/controller.py`, `Actor`, `NetworkOut`, `checklists/controller.py`, `ItemsOut`, `contracts/controller.py`, `GoalTemplateOut`, `NetworkService`, `goals/controller.py`, `GoalService`, `image`, `people/controller.py`, `image_url`, `Actor`, `checklists`, `UnitOfWorkFactory`, `tasks`, `networks/service.py`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07581453634085213 - nodes in this community are weakly interconnected._