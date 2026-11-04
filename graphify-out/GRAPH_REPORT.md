# Graph Report - avant-api  (2026-11-04)

## Corpus Check
- 293 files · ~90,855 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 3976 nodes · 10932 edges · 190 communities (101 shown, 89 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1830 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `258713ed`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_gam_tools.py
- typing
- roles/controller.py
- DashboardService
- Actor
- UserOut
- test_events.py
- gam_tools/dto.py
- steps
- _month
- Avant: models do MVP
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
- install
- goals/controller.py
- verify
- http.py
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- reports/controller.py
- CapturingMailer
- session-start.sh
- avant-api
- security.py
- tasks/controller.py
- members/controller.py
- commissions/controller.py
- MemberOut
- CompanyService
- documents/controller.py
- _onboard_owner
- months
- Services
- reports/service.py
- networks/service.py
- ContractClientRefOut
- UnitOfWorkFactory
- Services
- StreamLimiter
- .authenticate
- edit
- currencies/controller.py
- MemberService
- ContractOut
- clients
- GoogleService
- uuid
- account/controller.py
- contracts/controller.py
- GamToolService
- main.py
- ContractService
- Actor
- ItemsOut
- export.py
- limits.py
- .of_view
- GoalTemplateOut
- test_account.py
- avant-api
- networks/controller.py
- .assign
- mine
- .square_webp
- .networks
- image
- client_documents/controller.py
- people/controller.py
- test_client_changes_the_company_image
- uuid
- .of
- UnitOfWorkFactory
- limits.py
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- O que já tem
- Actor
- http.py
- .of
- InvoiceService
- test_gam_tools.py
- show
- Actor
- team
- test_checklists_need_permission
- SiteService
- MemberPermissionsIn
- SiteListOut
- image
- test_contract_crud
- test_api_keys.py
- .of
- .page_saved
- GAM
- GoalService
- ads_txt
- test_mfa.py
- .start
- test_costs_results.py
- client_documents/service.py
- get
- SiteMemberOut
- test_goal_progress_routes
- capped
- network
- contracts/dto.py
- company/controller.py
- conftest.py
- ClientService
- document_response
- dollars
- RedisEvents
- _member_client
- goals/service.py
- events.py
- main.py
- .uow
- verify

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 159 edges
2. `PageOut` - 145 edges
3. `_onboard_owner()` - 142 edges
4. `_csrf()` - 141 edges
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

## Communities (190 total, 89 thin omitted)

### Community 0 - "test_gam_tools.py"
Cohesion: 0.23
Nodes (6): _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _agent(), test_staff_opens_assigns_and_comments_on_tasks()

### Community 1 - "typing"
Cohesion: 0.13
Nodes (9): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), _form(), test_members_without_schedules_manage_only_see_what_they_receive() (+1 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "UserOut"
Cohesion: 0.08
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService, UserOut

### Community 6 - "test_events.py"
Cohesion: 0.14
Nodes (19): _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_id_token_claims() (+11 more)

### Community 7 - "gam_tools/dto.py"
Cohesion: 0.16
Nodes (5): GamToolClientOut, GamToolNetworkDetailOut, GamToolNetworkOut, GamToolPersonOut, GamToolSiteOut

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.10
Nodes (20): Acesso, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade (+12 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+6 more)

### Community 14 - "PageOut"
Cohesion: 0.11
Nodes (9): require(), dependency(), require_staff(), networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut (+1 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.10
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService, InvitationOut

### Community 18 - "PageOut"
Cohesion: 0.09
Nodes (7): index(), AuditService, audit(), runs(), AuditOut, page_out(), PageOut

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
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
Cohesion: 0.07
Nodes (13): create(), delete(), index(), roles(), set_home(), show(), update(), DashboardTemplateIn (+5 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.15
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.21
Nodes (14): _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas() (+6 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (11): get_cookies(), auth_service(), confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn (+3 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "reports/controller.py"
Cohesion: 0.08
Nodes (15): create(), create_from_template(), delete(), export(), export_saved(), index(), pin(), query() (+7 more)

### Community 32 - "CapturingMailer"
Cohesion: 0.16
Nodes (13): CapturingMailer, client(), engine(), mailer(), test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages() (+5 more)

### Community 36 - "security.py"
Cohesion: 0.06
Nodes (18): CompanyChanged, CsrfFailed, NoActiveCompany, RateLimited, api_key_actor(), bearer_token(), check_csrf(), check_tab_company() (+10 more)

### Community 37 - "tasks/controller.py"
Cohesion: 0.05
Nodes (17): change(), comment(), create(), task(), tasks(), TaskClientOut, TaskCommentIn, TaskDataIn (+9 more)

### Community 38 - "members/controller.py"
Cohesion: 0.15
Nodes (6): index(), leave(), options(), remove(), set_permissions(), show()

### Community 39 - "commissions/controller.py"
Cohesion: 0.05
Nodes (22): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+14 more)

### Community 40 - "MemberOut"
Cohesion: 0.15
Nodes (7): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 41 - "CompanyService"
Cohesion: 0.17
Nodes (5): remove_image(), show(), CompanyDetailOut, CompanyPatchIn, CompanyService

### Community 42 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "_onboard_owner"
Cohesion: 0.12
Nodes (19): Sent, _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session() (+11 more)

### Community 44 - "months"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 45 - "Services"
Cohesion: 0.03
Nodes (28): Services, get_services(), alert_service(), api_key_service(), audit_service(), company_service(), cost_service(), currency_service() (+20 more)

### Community 46 - "reports/service.py"
Cohesion: 0.05
Nodes (20): catalog(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut (+12 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 49 - "UnitOfWorkFactory"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "Services"
Cohesion: 0.10
Nodes (8): add(), delete(), edit(), notes(), ClientNoteIn, ClientNoteOut, NotePersonOut, ClientNoteService

### Community 51 - "StreamLimiter"
Cohesion: 0.15
Nodes (3): StreamLimiter, events(), test_stream_limiter_caps_each_person_and_the_process()

### Community 52 - ".authenticate"
Cohesion: 0.09
Nodes (3): get_invitation(), InvitationPreviewOut, AuthService

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.15
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "MemberService"
Cohesion: 0.14
Nodes (4): edit(), MemberDetailOut, MemberPatchIn, MemberService

### Community 57 - "clients"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "GoogleService"
Cohesion: 0.05
Nodes (12): GoogleUnavailable, GoogleAuth, new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), google_redirects() (+4 more)

### Community 59 - "uuid"
Cohesion: 0.28
Nodes (14): _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency(), test_pinned_reports_and_preview_refresh() (+6 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "contracts/controller.py"
Cohesion: 0.20
Nodes (5): contract(), contracts(), finish_contract(), new_contract(), remove_contract()

### Community 63 - "GamToolService"
Cohesion: 0.24
Nodes (4): run(), GamToolRunNetworkOut, GamToolRunOut, GamToolService

### Community 64 - "main.py"
Cohesion: 0.15
Nodes (4): health(), ready(), health_service(), HealthService

### Community 65 - "ContractService"
Cohesion: 0.19
Nodes (4): edit_contract(), contract_service(), ContractPatchIn, ContractService

### Community 66 - "Actor"
Cohesion: 0.10
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistDetailOut, ChecklistMarkIn (+2 more)

### Community 67 - "ItemsOut"
Cohesion: 0.18
Nodes (8): classify(), classify_many(), AdUnitPatchIn, MemberSitesIn, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "export.py"
Cohesion: 0.08
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 69 - "limits.py"
Cohesion: 0.10
Nodes (9): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+1 more)

### Community 72 - "test_account.py"
Cohesion: 0.10
Nodes (6): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle

### Community 74 - "networks/controller.py"
Cohesion: 0.04
Nodes (21): TaskQueue, assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService, connect(), disconnect() (+13 more)

### Community 75 - ".assign"
Cohesion: 0.25
Nodes (5): Atribuição de sites, GAM, Networks, Sites e ad units, assign_sites()

### Community 76 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 77 - ".square_webp"
Cohesion: 0.17
Nodes (4): _check_jpeg_size(), _sharpness(), _striped_logo(), test_wide_and_palette_logos_stay_sharp()

### Community 79 - "image"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "client_documents/controller.py"
Cohesion: 0.14
Nodes (6): approve(), documents(), download(), reject(), ClientDocumentOut, ClientDocumentService

### Community 81 - "people/controller.py"
Cohesion: 0.05
Nodes (29): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+21 more)

### Community 82 - "test_client_changes_the_company_image"
Cohesion: 0.23
Nodes (7): _jpeg(), _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), test_phone_photos_pass_and_huge_pngs_are_refused(), test_upload_without_session_is_refused_before_reading_the_body()

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 85 - "UnitOfWorkFactory"
Cohesion: 0.04
Nodes (10): UnitOfWorkFactory, results(), client_result_service(), ClientResultService, show(), ResultsOut, default_period(), ResultService (+2 more)

### Community 86 - "limits.py"
Cohesion: 0.05
Nodes (12): BucketResult, BucketRule, MemoryBucket, MemoryCounter, RedisBucket, RedisCounter, _exercise(), test_memory_bucket() (+4 more)

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.09
Nodes (13): SessionCookies, accept(), company_image(), do_logout(), login(), me(), set_active_company(), AcceptInvitationIn (+5 more)

### Community 89 - "O que já tem"
Cohesion: 0.20
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics()

### Community 91 - "Actor"
Cohesion: 0.15
Nodes (6): ad_units(), delete(), index(), members(), sites_of_member(), unlinked()

### Community 95 - "InvoiceService"
Cohesion: 0.12
Nodes (17): create_service(), save_payment_details(), services(), update_item(), update_service(), invoice_service(), AvailableMonthOut, InvoiceItemOut (+9 more)

### Community 96 - "test_gam_tools.py"
Cohesion: 0.08
Nodes (34): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+26 more)

### Community 98 - "Actor"
Cohesion: 0.18
Nodes (5): delete_template(), role_goals(), set_role_goal(), update_template(), RoleGoalIn

### Community 127 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 128 - "test_checklists_need_permission"
Cohesion: 0.39
Nodes (4): _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list(), test_staff_marks_checks_and_writes_notes()

### Community 129 - "SiteService"
Cohesion: 0.14
Nodes (3): link(), AdUnitOut, SiteService

### Community 130 - "MemberPermissionsIn"
Cohesion: 0.29
Nodes (3): DirectPermissionIn, DirectPermissionOut, MemberPermissionsIn

### Community 131 - "SiteListOut"
Cohesion: 0.17
Nodes (3): create(), site_options(), SiteListOut

### Community 134 - "test_contract_crud"
Cohesion: 0.38
Nodes (3): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission()

### Community 135 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 137 - ".page_saved"
Cohesion: 0.14
Nodes (4): ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 139 - "GAM"
Cohesion: 0.33
Nodes (6): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment

### Community 142 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 144 - "test_mfa.py"
Cohesion: 0.38
Nodes (11): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+3 more)

### Community 146 - "test_costs_results.py"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 148 - "get"
Cohesion: 0.09
Nodes (14): add_item(), available_months(), create(), delete(), delete_service(), get(), mine(), pay() (+6 more)

### Community 150 - "test_goal_progress_routes"
Cohesion: 0.53
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 158 - "contracts/dto.py"
Cohesion: 0.13
Nodes (7): contract_networks(), _contract_fields(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractSummaryOut, _network_ref()

### Community 160 - "company/controller.py"
Cohesion: 0.16
Nodes (5): edit_fiscal(), edit_image(), fiscal(), CompanyFiscalOut, FiscalDataIn

### Community 168 - "ClientService"
Cohesion: 0.04
Nodes (32): cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), clients(), edit_client() (+24 more)

### Community 175 - "_member_client"
Cohesion: 0.10
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 184 - "events.py"
Cohesion: 0.12
Nodes (6): channel(), EventSource, _parse(), sse(), event_service(), EventService

### Community 189 - "main.py"
Cohesion: 0.03
Nodes (18): engine_options(), _google(), _mailer(), QueryTooHeavy, NoEvents, configure_logging(), JsonFormatter, observe() (+10 more)

### Community 195 - ".uow"
Cohesion: 0.06
Nodes (5): Bucket, duplicate(), pinned(), SavedReportOut, ReportService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1807 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **89 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `SiteService`, `roles/controller.py`, `DashboardService`, `Actor`, `.__init__`, `UserOut`, `_month`, `.__init__`, `.trusted_uow`, `.uow`, `GoalService`, `PageOut`, `api_keys/controller.py`, `InvitationOut`, `PageOut`, `custom_metrics/controller.py`, `client_documents/service.py`, `goals/controller.py`, `.__init__`, `mfa/controller.py`, `contracts/dto.py`, `company/controller.py`, `.__init__`, `.__init__`, `.__init__`, `tasks/controller.py`, `commissions/controller.py`, `ClientService`, `CompanyService`, `documents/controller.py`, `MemberOut`, `reports/service.py`, `networks/service.py`, `.__init__`, `Services`, `.authenticate`, `currencies/controller.py`, `goals/service.py`, `MemberService`, `clients`, `GoogleService`, `account/controller.py`, `GamToolService`, `ContractService`, `Actor`, `.uow`, `ItemsOut`, `networks/controller.py`, `image`, `client_documents/controller.py`, `people/controller.py`, `InvoiceService`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._
- **Are the 120 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 120 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `typing` be split into smaller, more focused modules?**
  _Cohesion score 0.12666666666666668 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `SiteService`, `roles/controller.py`, `DashboardService`, `Actor`, `_month`, `.trusted_uow`, `.uow`, `GoalService`, `PageOut`, `api_keys/controller.py`, `InvitationOut`, `get`, `contracts/dto.py`, `reports/controller.py`, `tasks/controller.py`, `members/controller.py`, `ClientService`, `MemberOut`, `months`, `reports/service.py`, `Services`, `goals/service.py`, `ContractOut`, `MemberService`, `contracts/controller.py`, `GamToolService`, `ContractService`, `Actor`, `ItemsOut`, `networks/controller.py`, `.networks`, `image`, `people/controller.py`, `UnitOfWorkFactory`, `Actor`, `InvoiceService`, `Actor`, `.of`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07946127946127945 - nodes in this community are weakly interconnected._