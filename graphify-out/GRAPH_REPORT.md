# Graph Report - avant-api  (2026-11-05)

## Corpus Check
- 297 files · ~92,447 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4051 nodes · 11150 edges · 196 communities (94 shown, 102 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1856 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `8bd7a753`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- datetime
- test_alerts.py
- roles/controller.py
- DashboardService
- Actor
- index
- GamToolService
- google.py
- steps
- _month
- Avant: models do MVP
- test_gam_tools.py
- .uow
- PageOut
- Groone Avant: contexto do projeto
- api_keys/controller.py
- invitations/controller.py
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
- router.py
- CapturingMailer
- session-start.sh
- avant-api
- security.py
- tasks/controller.py
- networks/controller.py
- networks/service.py
- ClientService
- test_company_image.py
- documents/controller.py
- _onboard_owner
- checklists
- Services
- uuid
- networks/service.py
- ChecklistDetailOut
- download
- Services
- .of
- edit
- currencies/controller.py
- members/controller.py
- contracts/dto.py
- clients
- events/controller.py
- conftest.py
- account/controller.py
- download
- avant_core_shared_clock
- commissions/controller.py
- AuthService
- install
- documents/controller.py
- ItemsOut
- export.py
- limits.py
- SavedReportOut
- UnitOfWorkFactory
- avant-api
- NetworkService
- .of
- image
- ClientDocumentService
- image
- test_events.py
- uuid
- results/dto.py
- ad_units
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- errors.py
- SiteListOut
- get
- google/controller.py
- capped
- _csrf
- .classify
- GoalService
- networks/dependencies.py
- updates
- TaskQueue
- profile/controller.py
- users
- enqueue_sync
- checklists/controller.py
- health/controller.py
- ContractOut
- Arquitetura do MVP do Avant
- test_mfa.py
- _contract_fields
- contracts/controller.py
- members
- Actor
- clients
- company/controller.py
- mcm/service.py
- .change_password
- UserOut
- document_response
- dollars
- _member_client
- ad_units
- Actor
- .assign
- TooManyAttempts
- O que já tem
- MemoryCounter
- edit_image
- .first_day

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 168 edges
2. `_csrf()` - 150 edges
3. `_onboard_owner()` - 150 edges
4. `PageOut` - 145 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 118 edges
8. `ReportService` - 79 edges
9. `_staff()` - 67 edges
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

## Communities (196 total, 102 thin omitted)

### Community 0 - "datetime"
Cohesion: 0.08
Nodes (13): refresh_levels(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone() (+5 more)

### Community 1 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (19): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+11 more)

### Community 7 - "google.py"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.08
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (22): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+14 more)

### Community 11 - "test_gam_tools.py"
Cohesion: 0.16
Nodes (10): _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads() (+2 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "PageOut"
Cohesion: 0.09
Nodes (9): networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, page_out(), PageOut (+1 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "invitations/controller.py"
Cohesion: 0.11
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.09
Nodes (11): check(), create(), delete(), index(), update(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn (+3 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "main.py"
Cohesion: 0.05
Nodes (16): engine_options(), _google(), _mailer(), configure_logging(), JsonFormatter, observe(), _route_template(), Settings (+8 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.07
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "image_response"
Cohesion: 0.16
Nodes (3): client_info(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.15
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "_onboard_owner"
Cohesion: 0.11
Nodes (17): _checkouts(), test_report_requests_use_few_connections(), test_busy_export_answers_503_with_retry_after(), _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait() (+9 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "reports/service.py"
Cohesion: 0.05
Nodes (27): catalog(), index(), query(), query_batch(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn (+19 more)

### Community 31 - "router.py"
Cohesion: 0.11
Nodes (5): invite(), options(), staff(), StaffInviteIn, StaffService

### Community 32 - "CapturingMailer"
Cohesion: 0.21
Nodes (10): CapturingMailer, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_option_lists_keep_the_permissions() (+2 more)

### Community 36 - "security.py"
Cohesion: 0.06
Nodes (24): CompanyChanged, CsrfFailed, NoActiveCompany, RateLimited, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site() (+16 more)

### Community 37 - "tasks/controller.py"
Cohesion: 0.05
Nodes (18): change(), comment(), create(), task(), tasks(), support_task_service(), TaskClientOut, TaskCommentIn (+10 more)

### Community 38 - "networks/controller.py"
Cohesion: 0.19
Nodes (6): disconnect(), index(), service_account(), show(), sync(), sync_runs()

### Community 40 - "ClientService"
Cohesion: 0.05
Nodes (34): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), edit_client() (+26 more)

### Community 41 - "test_company_image.py"
Cohesion: 0.10
Nodes (13): _check_jpeg_size(), PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image() (+5 more)

### Community 42 - "documents/controller.py"
Cohesion: 0.18
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 43 - "_onboard_owner"
Cohesion: 0.12
Nodes (27): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited(), _error_code() (+19 more)

### Community 44 - "checklists"
Cohesion: 0.13
Nodes (3): checklists(), months(), summary()

### Community 45 - "Services"
Cohesion: 0.04
Nodes (13): Services, get_services(), audit_service(), currency_service(), custom_metric_service(), contract_service(), gam_tool_service(), client_inventory_service() (+5 more)

### Community 46 - "uuid"
Cohesion: 0.16
Nodes (18): _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use() (+10 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "ChecklistDetailOut"
Cohesion: 0.10
Nodes (8): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistDetailOut, SiteChecklistService

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

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+7 more)

### Community 56 - "contracts/dto.py"
Cohesion: 0.32
Nodes (5): ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut

### Community 57 - "clients"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "events/controller.py"
Cohesion: 0.24
Nodes (3): EventSource, event_service(), EventService

### Community 59 - "conftest.py"
Cohesion: 0.12
Nodes (10): client(), engine(), mailer(), Sent, _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys() (+2 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "download"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 62 - "avant_core_shared_clock"
Cohesion: 0.24
Nodes (3): client_document_service(), ClientDocumentsOut, RejectDocumentIn

### Community 63 - "commissions/controller.py"
Cohesion: 0.07
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 64 - "AuthService"
Cohesion: 0.08
Nodes (3): get_invitation(), auth_service(), AuthService

### Community 65 - "install"
Cohesion: 0.25
Nodes (7): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 66 - "documents/controller.py"
Cohesion: 0.29
Nodes (3): documents(), document_service(), DocumentService

### Community 67 - "ItemsOut"
Cohesion: 0.25
Nodes (8): AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "limits.py"
Cohesion: 0.08
Nodes (8): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "SavedReportOut"
Cohesion: 0.05
Nodes (13): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned() (+5 more)

### Community 74 - "NetworkService"
Cohesion: 0.15
Nodes (5): connect(), options(), NetworkDetailOut, NetworkIn, NetworkService

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 82 - "test_events.py"
Cohesion: 0.15
Nodes (13): channel(), _parse(), sse(), _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot() (+5 more)

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 85 - "results/dto.py"
Cohesion: 0.07
Nodes (8): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, default_period(), ResultService

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.09
Nodes (16): SessionCookies, accept(), company_image(), do_logout(), login(), me(), set_active_company(), AcceptInvitationIn (+8 more)

### Community 89 - "errors.py"
Cohesion: 0.04
Nodes (17): ExportsBusy, QueryTooHeavy, NoEvents, Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket (+9 more)

### Community 91 - "SiteListOut"
Cohesion: 0.13
Nodes (3): create(), site_options(), SiteListOut

### Community 92 - "get"
Cohesion: 0.07
Nodes (31): add_item(), available_months(), create_service(), delete(), delete_service(), get(), issue(), mine() (+23 more)

### Community 94 - "google/controller.py"
Cohesion: 0.05
Nodes (13): GoogleUnavailable, GoogleAuth, new_verifier(), get_cookies(), google_callback(), google_start(), google_status(), google_unlink() (+5 more)

### Community 96 - "_csrf"
Cohesion: 0.06
Nodes (38): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+30 more)

### Community 98 - "GoalService"
Cohesion: 0.05
Nodes (19): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+11 more)

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 130 - "profile/controller.py"
Cohesion: 0.09
Nodes (7): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService

### Community 135 - "users"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 137 - "checklists/controller.py"
Cohesion: 0.18
Nodes (9): site_checklist_service(), ChecklistMarkIn, ChecklistMonthOut, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut (+1 more)

### Community 139 - "health/controller.py"
Cohesion: 0.15
Nodes (4): health(), ready(), health_service(), HealthService

### Community 142 - "ContractOut"
Cohesion: 0.19
Nodes (3): contract(), ContractOut, ContractService

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.20
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+6 more)

### Community 147 - "contracts/controller.py"
Cohesion: 0.16
Nodes (5): contract_networks(), edit_contract(), finish_contract(), new_contract(), remove_contract()

### Community 149 - "members"
Cohesion: 0.25
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 160 - "company/controller.py"
Cohesion: 0.20
Nodes (7): show(), company_service(), CompanyDetailOut, CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 163 - "mcm/service.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 167 - "UserOut"
Cohesion: 0.10
Nodes (10): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+2 more)

### Community 175 - "_member_client"
Cohesion: 0.09
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 180 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), delete(), index(), show(), sites_of_member(), unlinked()

### Community 182 - ".assign"
Cohesion: 0.20
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 184 - "TooManyAttempts"
Cohesion: 0.14
Nodes (4): TooManyAttempts, StreamLimiter, events(), test_stream_limiter_caps_each_person_and_the_process()

### Community 191 - "O que já tem"
Cohesion: 0.15
Nodes (8): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contracts()

### Community 203 - "edit_image"
Cohesion: 0.20
Nodes (4): edit_fiscal(), edit_image(), fiscal(), remove_image()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1843 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **102 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `TaskQueue`, `profile/controller.py`, `DashboardService`, `Actor`, `.__init__`, `GamToolService`, `.__init__`, `.__init__`, `checklists/controller.py`, `.__init__`, `roles/controller.py`, `InvoiceService`, `.uow`, `PageOut`, `ContractOut`, `api_keys/controller.py`, `invitations/controller.py`, `.__init__`, `custom_metrics/controller.py`, `.__init__`, `members`, `Actor`, `goals/controller.py`, `.__init__`, `.__init__`, `mfa/controller.py`, `.__init__`, `router.py`, `company/controller.py`, `reports/service.py`, `.__init__`, `mcm/service.py`, `tasks/controller.py`, `.__init__`, `UserOut`, `ClientService`, `networks/service.py`, `documents/controller.py`, `.__init__`, `.__init__`, `networks/service.py`, `ChecklistDetailOut`, `_month`, `Services`, `currencies/controller.py`, `members/controller.py`, `contracts/dto.py`, `clients`, `account/controller.py`, `avant_core_shared_clock`, `commissions/controller.py`, `AuthService`, `documents/controller.py`, `ItemsOut`, `limits.py`, `NetworkService`, `.__init__`, `image`, `ClientDocumentService`, `.__init__`, `.__init__`, `.__init__`, `results/dto.py`, `auth/controller.py`, `.__init__`, `get`, `google/controller.py`, `GoalService`?**
  _High betweenness centrality (0.136) - this node is a cross-community bridge._
- **Are the 127 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 127 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `datetime` be split into smaller, more focused modules?**
  _Cohesion score 0.08084163898117387 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `roles/controller.py`, `DashboardService`, `Actor`, `index`, `GamToolService`, `checklists/controller.py`, `_month`, `InvoiceService`, `.uow`, `ContractOut`, `api_keys/controller.py`, `invitations/controller.py`, `members`, `clients`, `reports/service.py`, `router.py`, `mcm/service.py`, `tasks/controller.py`, `networks/controller.py`, `UserOut`, `ClientService`, `networks/service.py`, `checklists`, `Services`, `ChecklistDetailOut`, `Services`, `Actor`, `.assign`, `members/controller.py`, `contracts/dto.py`, `O que já tem`, `ItemsOut`, `UnitOfWorkFactory`, `NetworkService`, `image`, `results/dto.py`, `SiteListOut`, `get`, `GoalService`?**
  _High betweenness centrality (0.090) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08148148148148149 - nodes in this community are weakly interconnected._