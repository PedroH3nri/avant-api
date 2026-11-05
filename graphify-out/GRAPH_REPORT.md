# Graph Report - avant-api  (2026-11-05)

## Corpus Check
- 295 files · ~91,356 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4000 nodes · 11012 edges · 200 communities (105 shown, 95 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1840 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `25d670c3`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- conftest.py
- typing
- roles/controller.py
- DashboardService
- Actor
- UserOut
- google.py
- GamToolService
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
- fastapi
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- install
- goals/controller.py
- verify
- image
- clean_code.py
- _onboard_owner
- mfa/controller.py
- Avant: repositório e plano do MVP
- ReportService
- ClientService
- session-start.sh
- avant-api
- security.py
- BaseModel
- .save_rule
- CommissionService
- client_image
- documents/controller.py
- CapturingMailer
- months
- Services
- reports/service.py
- networks/service.py
- uuid
- Services
- commissions/dto.py
- get
- edit
- currencies/controller.py
- members/controller.py
- contracts/controller.py
- clients
- GoogleService
- _onboard_owner
- account/controller.py
- pydantic
- commissions/controller.py
- main.py
- MemoryBucket
- Actor
- ItemsOut
- export.py
- limits.py
- page_out
- main.py
- google.py
- avant-api
- networks/controller.py
- TaskQueue
- networks/service.py
- download
- image
- download
- people/controller.py
- test_company_image.py
- uuid
- to_csv
- avant_core_access_models
- RedisCounter
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- SiteListOut
- errors.py
- google/dependencies.py
- middleware.py
- _csrf
- SiteOut
- GoalService
- tasks/controller.py
- google_status
- do_reset_password
- TaskDetailOut
- .of_view
- .assign
- capped
- .of
- users
- mine
- .page_saved
- tasks/dto.py
- person
- delete_session
- Arquitetura do MVP do Avant
- test_mfa.py
- .page_saved
- image_url
- test_groups_lifecycle
- UUID
- SiteService
- SavedReportOut
- InvoiceService
- _csv_cell
- UnitOfWorkFactory
- company/controller.py
- edit_client
- mcm/service.py
- .change_password
- .build
- download
- create
- _member_client
- show
- delete_template
- Actor
- edit_image
- test_events.py
- _month
- TaskPatchIn
- .uow
- test_database.py
- .to_data
- TaskQueue
- Actor
- .trusted_uow
- SessionCookies
- GoogleAuth

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 162 edges
2. `PageOut` - 145 edges
3. `_onboard_owner()` - 145 edges
4. `_csrf()` - 144 edges
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

## Communities (200 total, 95 thin omitted)

### Community 0 - "conftest.py"
Cohesion: 0.06
Nodes (18): client(), engine(), mailer(), refresh_levels(), _jwt(), test_id_token_claims(), test_deployed_cookies_use_the_host_prefix(), _scaling_client() (+10 more)

### Community 1 - "typing"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.07
Nodes (26): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+18 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "UserOut"
Cohesion: 0.11
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 6 - "google.py"
Cohesion: 0.12
Nodes (6): GoogleFailed, challenge(), _claims(), identity_from_id_token(), new_verifier(), google_start()

### Community 7 - "GamToolService"
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
Nodes (22): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+14 more)

### Community 11 - "test_gam_tools.py"
Cohesion: 0.13
Nodes (11): RecordingQueue, _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list() (+3 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "shared/dto.py"
Cohesion: 0.14
Nodes (6): networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "invitations/controller.py"
Cohesion: 0.10
Nodes (9): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut (+1 more)

### Community 18 - "fastapi"
Cohesion: 0.18
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

### Community 22 - "install"
Cohesion: 0.25
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
Cohesion: 0.17
Nodes (16): test_busy_export_answers_503_with_retry_after(), test_export_slots_refuse_a_third_export_while_two_run(), _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics() (+8 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.05
Nodes (13): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+5 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "ReportService"
Cohesion: 0.06
Nodes (19): Bucket, create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned() (+11 more)

### Community 32 - "ClientService"
Cohesion: 0.06
Nodes (27): audit(), cancel_owner(), change_status(), client(), client_options(), client_teams(), edit_client(), edit_client_image() (+19 more)

### Community 36 - "security.py"
Cohesion: 0.09
Nodes (17): CsrfFailed, api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor(), get_auth(), get_session_actor() (+9 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - ".save_rule"
Cohesion: 0.12
Nodes (7): adjust(), create_rule(), delete_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 39 - "CommissionService"
Cohesion: 0.16
Nodes (4): set_settings(), settings(), CommissionSettingsOut, CommissionService

### Community 42 - "documents/controller.py"
Cohesion: 0.11
Nodes (7): documents(), upload(), document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "CapturingMailer"
Cohesion: 0.13
Nodes (15): CapturingMailer, Sent, _owner_invite(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_groone_routes_need_the_session_with_2fa(), test_internal_clients() (+7 more)

### Community 44 - "months"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 45 - "Services"
Cohesion: 0.04
Nodes (16): _google(), _mailer(), Services, NoEvents, GoogleOAuth, configure_logging(), get_services(), Settings (+8 more)

### Community 46 - "reports/service.py"
Cohesion: 0.05
Nodes (17): catalog(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn (+9 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "uuid"
Cohesion: 0.28
Nodes (14): _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency(), test_pinned_reports_and_preview_refresh() (+6 more)

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "commissions/dto.py"
Cohesion: 0.24
Nodes (3): CommissionMonthOut, CommissionSettingsIn, dollars()

### Community 52 - "get"
Cohesion: 0.15
Nodes (8): available_months(), get(), mine(), payment_details(), pdf(), service_options(), services(), team()

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (19): ClientMemberOut, edit(), index(), leave(), options(), remove(), set_permissions(), show() (+11 more)

### Community 56 - "contracts/controller.py"
Cohesion: 0.06
Nodes (25): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+17 more)

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 59 - "_onboard_owner"
Cohesion: 0.13
Nodes (27): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited(), _onboard_owner() (+19 more)

### Community 60 - "account/controller.py"
Cohesion: 0.08
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "pydantic"
Cohesion: 0.22
Nodes (5): client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 63 - "commissions/controller.py"
Cohesion: 0.19
Nodes (3): commission_service(), AdjustmentIn, MonthIn

### Community 64 - "main.py"
Cohesion: 0.15
Nodes (4): health(), ready(), health_service(), HealthService

### Community 65 - "MemoryBucket"
Cohesion: 0.11
Nodes (7): BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 66 - "Actor"
Cohesion: 0.10
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), site_checklist_service(), ChecklistDetailOut (+2 more)

### Community 67 - "ItemsOut"
Cohesion: 0.19
Nodes (6): site_service(), AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 68 - "export.py"
Cohesion: 0.08
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 69 - "limits.py"
Cohesion: 0.09
Nodes (9): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+1 more)

### Community 70 - "page_out"
Cohesion: 0.10
Nodes (3): clients(), AuditOut, page_out()

### Community 71 - "main.py"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 74 - "networks/controller.py"
Cohesion: 0.13
Nodes (11): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+3 more)

### Community 76 - "TaskQueue"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 77 - "networks/service.py"
Cohesion: 0.18
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 78 - "download"
Cohesion: 0.09
Nodes (9): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService (+1 more)

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "download"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 81 - "people/controller.py"
Cohesion: 0.12
Nodes (9): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PersonOut (+1 more)

### Community 82 - "test_company_image.py"
Cohesion: 0.10
Nodes (13): _check_jpeg_size(), PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image() (+5 more)

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - "to_csv"
Cohesion: 0.25
Nodes (5): _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search(), test_site_category_and_responsible(), test_sites_and_assignment()

### Community 85 - "avant_core_access_models"
Cohesion: 0.05
Nodes (11): results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut (+3 more)

### Community 86 - "RedisCounter"
Cohesion: 0.14
Nodes (4): RedisCounter, test_docs_are_closed_in_production(), test_every_response_has_the_security_headers(), test_redis_down_is_a_503_not_a_500()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.07
Nodes (15): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), AcceptInvitationIn (+7 more)

### Community 91 - "SiteListOut"
Cohesion: 0.18
Nodes (3): index(), site_options(), SiteListOut

### Community 92 - "errors.py"
Cohesion: 0.15
Nodes (5): CompanyChanged, ExportsBusy, GoogleUnavailable, NoActiveCompany, QueryTooHeavy

### Community 94 - "google/dependencies.py"
Cohesion: 0.13
Nodes (3): google_redirects(), google_service(), GoogleRedirects

### Community 95 - "middleware.py"
Cohesion: 0.16
Nodes (12): create_service(), update_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceServiceOut, InvoiceSummaryOut (+4 more)

### Community 96 - "_csrf"
Cohesion: 0.07
Nodes (32): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+24 more)

### Community 97 - "SiteOut"
Cohesion: 0.13
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 98 - "GoalService"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 102 - "tasks/controller.py"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 123 - "google_status"
Cohesion: 0.12
Nodes (3): google_status(), google_unlink(), GoogleStatusOut

### Community 127 - "do_reset_password"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 128 - "TaskDetailOut"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 130 - ".assign"
Cohesion: 0.21
Nodes (3): ad_units(), link(), AdUnitOut

### Community 135 - "users"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 137 - ".page_saved"
Cohesion: 0.09
Nodes (6): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 138 - "tasks/dto.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 142 - "delete_session"
Cohesion: 0.12
Nodes (3): JsonFormatter, observe(), _route_template()

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.34
Nodes (11): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+3 more)

### Community 148 - "UUID"
Cohesion: 0.13
Nodes (8): add_item(), create(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft()

### Community 149 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 150 - "SavedReportOut"
Cohesion: 0.09
Nodes (4): create(), update(), SavedReportIn, SavedReportOut

### Community 160 - "company/controller.py"
Cohesion: 0.20
Nodes (7): show(), company_service(), CompanyDetailOut, CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 163 - "mcm/service.py"
Cohesion: 0.12
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 175 - "_member_client"
Cohesion: 0.14
Nodes (15): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture() (+7 more)

### Community 180 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), classify(), classify_many(), delete(), show(), unlinked()

### Community 182 - "edit_image"
Cohesion: 0.20
Nodes (4): edit_fiscal(), edit_image(), fiscal(), remove_image()

### Community 184 - "test_events.py"
Cohesion: 0.07
Nodes (17): channel(), EventSource, _parse(), sse(), StreamLimiter, events(), event_service(), EventService (+9 more)

### Community 185 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 189 - "test_database.py"
Cohesion: 0.31
Nodes (4): engine_options(), _settings(), test_every_connection_has_a_statement_and_idle_timeout(), test_pool_is_bounded_and_waits_little()

### Community 195 - "Actor"
Cohesion: 0.08
Nodes (3): RateLimited, export_slot(), _statement_timeout()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1818 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **95 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `TaskDetailOut`, `roles/controller.py`, `DashboardService`, `Actor`, `.__init__`, `UserOut`, `GamToolService`, `_month`, `tasks/dto.py`, `InvoiceService`, `.uow`, `shared/dto.py`, `api_keys/controller.py`, `invitations/controller.py`, `fastapi`, `custom_metrics/controller.py`, `SiteService`, `goals/controller.py`, `InvoiceService`, `mfa/controller.py`, `ReportService`, `company/controller.py`, `company/controller.py`, `ClientService`, `.__init__`, `mcm/service.py`, `CommissionService`, `documents/controller.py`, `reports/service.py`, `networks/service.py`, `.__init__`, `Services`, `currencies/controller.py`, `members/controller.py`, `contracts/controller.py`, `clients`, `GoogleService`, `goals/service.py`, `account/controller.py`, `.uow`, `pydantic`, `TaskQueue`, `commissions/controller.py`, `Actor`, `ItemsOut`, `limits.py`, `GoogleAuth`, `.__init__`, `networks/controller.py`, `networks/service.py`, `download`, `image`, `people/controller.py`, `avant_core_access_models`, `auth/controller.py`, `errors.py`, `middleware.py`, `do_reset_password`?**
  _High betweenness centrality (0.127) - this node is a cross-community bridge._
- **Are the 122 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 122 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `conftest.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05727605727605728 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `invitations/controller.py` to `TaskDetailOut`, `roles/controller.py`, `DashboardService`, `Actor`, `UserOut`, `GamToolService`, `_month`, `tasks/dto.py`, `InvoiceService`, `.uow`, `shared/dto.py`, `api_keys/controller.py`, `.page_saved`, `fastapi`, `SiteService`, `InvoiceService`, `UnitOfWorkFactory`, `ClientService`, `mcm/service.py`, `security.py`, `.of`, `months`, `reports/service.py`, `Services`, `get`, `Actor`, `members/controller.py`, `contracts/controller.py`, `goals/service.py`, `Actor`, `ItemsOut`, `page_out`, `main.py`, `networks/controller.py`, `networks/service.py`, `image`, `people/controller.py`, `avant_core_access_models`, `.show`, `SiteListOut`, `middleware.py`, `SiteOut`, `GoalService`, `tasks/controller.py`, `do_reset_password`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07792207792207792 - nodes in this community are weakly interconnected._