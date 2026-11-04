# Graph Report - avant-api  (2026-11-04)

## Corpus Check
- 292 files · ~90,627 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3969 nodes · 10913 edges · 206 communities (103 shown, 103 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1828 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2d75283b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- datetime
- typing
- roles/controller.py
- .uow
- Actor
- profile/controller.py
- test_events.py
- GamToolService
- steps
- _month
- Avant: models do MVP
- avant_core_shared_clock
- .trusted_uow
- .uow
- PageOut
- Groone Avant: contexto do projeto
- api_keys/controller.py
- InvitationOut
- shared/dto.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- Actor
- goals/controller.py
- verify
- http.py
- clean_code.py
- test_reports.py
- pydantic
- Avant: repositório e plano do MVP
- ReportQueryIn
- CapturingMailer
- session-start.sh
- avant-api
- BaseModel
- invoices/controller.py
- .save_rule
- PageOut
- image
- documents/controller.py
- test_api.py
- months
- security.py
- networks/service.py
- SupportTaskService
- UnitOfWorkFactory
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
- results
- main.py
- NetworkOut
- Actor
- ItemsOut
- export.py
- limits.py
- logs.py
- GoalTemplateOut
- test_account.py
- avant-api
- networks/controller.py
- .assign
- mine
- CommissionService
- image
- client_documents/controller.py
- people/controller.py
- commissions/controller.py
- uuid
- checklists
- shared/dto.py
- limits.py
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- Actor
- RedisCounter
- test_networks.py
- InvoiceServiceOut
- test_gam_tools.py
- tasks
- Actor
- test_sites.py
- team
- _month
- link
- CommissionService
- SiteListOut
- SiteChecklistService
- UnitOfWorkFactory
- DashboardTemplateOut
- test_api_keys.py
- .page_saved
- commissions/dto.py
- ad_units
- GoalService
- image
- test_mfa.py
- goals/service.py
- test_costs_results.py
- client_documents/service.py
- get
- SiteService
- test_saved_views.py
- edit_image
- company/controller.py
- contracts/controller.py
- .update_fiscal
- conftest.py
- .__init__
- edit_image
- middleware.py
- ClientService
- document_response
- RedisEvents
- _member_client
- .classify
- mine
- person
- image_url
- goals/service.py
- fastapi
- pytest
- TaskPatchIn
- .uow
- Settings
- NoEvents
- Actor
- .save_payee_details
- CeleryQueue

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

## Communities (206 total, 103 thin omitted)

### Community 0 - "datetime"
Cohesion: 0.07
Nodes (15): RecordingQueue, _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _network() (+7 more)

### Community 1 - "typing"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - ".uow"
Cohesion: 0.08
Nodes (20): choose(), create_from_template(), delete(), duplicate(), home(), index(), run(), run_all() (+12 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "profile/controller.py"
Cohesion: 0.20
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 6 - "test_events.py"
Cohesion: 0.26
Nodes (10): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports(), test_redis_source_delivers_published_messages() (+2 more)

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

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "PageOut"
Cohesion: 0.07
Nodes (9): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService (+1 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "shared/dto.py"
Cohesion: 0.06
Nodes (8): require(), require_report(), index(), audit_service(), AuditService, result_service(), role_service(), AuditOut

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "Actor"
Cohesion: 0.12
Nodes (11): CompanyChanged, CsrfFailed, error_body(), install(), domain_error(), http_error(), unexpected(), validation_error() (+3 more)

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

### Community 27 - "test_reports.py"
Cohesion: 0.25
Nodes (15): _onboard_owner(), _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency() (+7 more)

### Community 28 - "pydantic"
Cohesion: 0.12
Nodes (8): GoogleStatusOut, confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "ReportQueryIn"
Cohesion: 0.05
Nodes (37): catalog(), create(), create_from_template(), duplicate(), export(), export_saved(), index(), pin() (+29 more)

### Community 32 - "CapturingMailer"
Cohesion: 0.21
Nodes (10): CapturingMailer, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_option_lists_keep_the_permissions() (+2 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - "invoices/controller.py"
Cohesion: 0.23
Nodes (9): AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn, ServiceItemIn (+1 more)

### Community 39 - ".save_rule"
Cohesion: 0.12
Nodes (7): adjust(), create_rule(), delete_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 40 - "PageOut"
Cohesion: 0.08
Nodes (10): templates(), invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut (+2 more)

### Community 41 - "image"
Cohesion: 0.11
Nodes (4): fiscal(), image(), remove_image(), show()

### Community 42 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "test_api.py"
Cohesion: 0.18
Nodes (10): test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session(), test_team_invitation_flow(), test_validation_error_format(), _template() (+2 more)

### Community 44 - "months"
Cohesion: 0.21
Nodes (3): months(), summary(), ChecklistMonthOut

### Community 45 - "security.py"
Cohesion: 0.03
Nodes (31): Services, api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor(), get_auth(), get_services() (+23 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "SupportTaskService"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 49 - "UnitOfWorkFactory"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "UserOut"
Cohesion: 0.14
Nodes (3): PersonOut, person_out(), UserOut

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.15
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+6 more)

### Community 56 - "tasks/controller.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 57 - "clients"
Cohesion: 0.13
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 58 - "GoogleService"
Cohesion: 0.07
Nodes (7): GoogleUnavailable, GoogleAuth, google_callback(), google_status(), google_unlink(), google_service(), GoogleService

### Community 59 - "uuid"
Cohesion: 0.23
Nodes (16): _owner_invite(), test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused() (+8 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (12): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn (+4 more)

### Community 61 - "get"
Cohesion: 0.13
Nodes (8): add_item(), create(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft()

### Community 64 - "main.py"
Cohesion: 0.16
Nodes (3): ready(), health_service(), HealthService

### Community 65 - "NetworkOut"
Cohesion: 0.11
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "Actor"
Cohesion: 0.14
Nodes (9): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), site_checklist_service(), ChecklistMarkIn (+1 more)

### Community 67 - "ItemsOut"
Cohesion: 0.25
Nodes (8): AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "export.py"
Cohesion: 0.08
Nodes (11): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+3 more)

### Community 69 - "limits.py"
Cohesion: 0.11
Nodes (8): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 72 - "test_account.py"
Cohesion: 0.08
Nodes (10): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), google_start(), FakeGoogle (+2 more)

### Community 74 - "networks/controller.py"
Cohesion: 0.06
Nodes (15): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+7 more)

### Community 75 - ".assign"
Cohesion: 0.20
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 76 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 78 - "CommissionService"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 79 - "image"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "client_documents/controller.py"
Cohesion: 0.14
Nodes (6): approve(), documents(), download(), reject(), ClientDocumentOut, ClientDocumentService

### Community 81 - "people/controller.py"
Cohesion: 0.12
Nodes (8): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PeopleService

### Community 82 - "commissions/controller.py"
Cohesion: 0.19
Nodes (3): commission_service(), AdjustmentIn, MonthIn

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 85 - "shared/dto.py"
Cohesion: 0.07
Nodes (7): show(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut, default_period(), ResultService

### Community 86 - "limits.py"
Cohesion: 0.09
Nodes (8): Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.08
Nodes (19): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), get_invitation(), login(), me() (+11 more)

### Community 91 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), delete(), index(), show(), sites_of_member(), unlinked()

### Community 94 - "test_networks.py"
Cohesion: 0.47
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 95 - "InvoiceServiceOut"
Cohesion: 0.22
Nodes (6): create_service(), services(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 96 - "test_gam_tools.py"
Cohesion: 0.07
Nodes (35): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+27 more)

### Community 97 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 98 - "Actor"
Cohesion: 0.21
Nodes (4): delete_template(), role_goals(), set_role_goal(), update_template()

### Community 102 - "test_sites.py"
Cohesion: 0.25
Nodes (5): _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search(), test_site_category_and_responsible(), test_sites_and_assignment()

### Community 128 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 130 - "CommissionService"
Cohesion: 0.16
Nodes (4): set_settings(), settings(), CommissionSettingsOut, CommissionService

### Community 131 - "SiteListOut"
Cohesion: 0.13
Nodes (3): create(), site_options(), SiteListOut

### Community 132 - "SiteChecklistService"
Cohesion: 0.13
Nodes (3): TaskQueue, ChecklistDetailOut, SiteChecklistService

### Community 134 - "DashboardTemplateOut"
Cohesion: 0.31
Nodes (3): templates(), DashboardTemplateOut, LabelOut

### Community 135 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 137 - ".page_saved"
Cohesion: 0.11
Nodes (4): ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 138 - "commissions/dto.py"
Cohesion: 0.24
Nodes (3): CommissionMonthOut, CommissionSettingsIn, dollars()

### Community 142 - "GoalService"
Cohesion: 0.31
Nodes (3): template_options(), GoalTemplateOut, GoalService

### Community 144 - "test_mfa.py"
Cohesion: 0.22
Nodes (13): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+5 more)

### Community 145 - "goals/service.py"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 146 - "test_costs_results.py"
Cohesion: 0.21
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 148 - "get"
Cohesion: 0.12
Nodes (7): available_months(), get(), mine(), payment_details(), pdf(), service_options(), team()

### Community 149 - "SiteService"
Cohesion: 0.25
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 155 - "company/controller.py"
Cohesion: 0.21
Nodes (6): company_service(), CompanyDetailOut, CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 158 - "contracts/controller.py"
Cohesion: 0.06
Nodes (25): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+17 more)

### Community 163 - "conftest.py"
Cohesion: 0.13
Nodes (9): mailer(), Sent, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login() (+1 more)

### Community 168 - "ClientService"
Cohesion: 0.04
Nodes (34): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), clients() (+26 more)

### Community 175 - "_member_client"
Cohesion: 0.06
Nodes (25): _check_jpeg_size(), PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image() (+17 more)

### Community 184 - "fastapi"
Cohesion: 0.09
Nodes (9): TooManyAttempts, channel(), EventSource, _parse(), sse(), StreamLimiter, events(), EventService (+1 more)

### Community 188 - ".uow"
Cohesion: 0.09
Nodes (5): create(), update(), DashboardIn, DashboardOut, DashboardService

### Community 189 - "Settings"
Cohesion: 0.05
Nodes (13): engine_options(), _google(), _mailer(), Settings, create_app(), google_redirects(), GoogleRedirects, health() (+5 more)

### Community 195 - "Actor"
Cohesion: 0.07
Nodes (3): delete(), unpin(), _statement_timeout()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1807 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **103 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `CommissionService`, `.uow`, `Actor`, `SiteChecklistService`, `profile/controller.py`, `GamToolService`, `roles/controller.py`, `_month`, `avant_core_shared_clock`, `.trusted_uow`, `.uow`, `GoalService`, `PageOut`, `api_keys/controller.py`, `InvitationOut`, `shared/dto.py`, `custom_metrics/controller.py`, `client_documents/service.py`, `SiteService`, `goals/controller.py`, `company/controller.py`, `contracts/controller.py`, `company/controller.py`, `ReportQueryIn`, `.__init__`, `invoices/controller.py`, `ClientService`, `PageOut`, `documents/controller.py`, `networks/service.py`, `SupportTaskService`, `.__init__`, `Services`, `UserOut`, `currencies/controller.py`, `goals/service.py`, `tasks/controller.py`, `clients`, `GoogleService`, `members/controller.py`, `account/controller.py`, `.uow`, `results`, `.__init__`, `NetworkOut`, `.__init__`, `ItemsOut`, `.__init__`, `networks/controller.py`, `.__init__`, `image`, `client_documents/controller.py`, `people/controller.py`, `commissions/controller.py`, `shared/dto.py`, `limits.py`, `auth/controller.py`, `InvoiceServiceOut`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **Are the 120 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 120 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `datetime` be split into smaller, more focused modules?**
  _Cohesion score 0.06862745098039216 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `roles/controller.py`, `.uow`, `Actor`, `SiteChecklistService`, `SiteListOut`, `GamToolService`, `_month`, `.trusted_uow`, `.uow`, `GoalService`, `PageOut`, `api_keys/controller.py`, `InvitationOut`, `shared/dto.py`, `get`, `SiteService`, `contracts/controller.py`, `ReportQueryIn`, `invoices/controller.py`, `ClientService`, `SupportTaskService`, `Services`, `UserOut`, `goals/service.py`, `tasks/controller.py`, `members/controller.py`, `results`, `NetworkOut`, `Actor`, `ItemsOut`, `networks/controller.py`, `.assign`, `image`, `people/controller.py`, `checklists`, `shared/dto.py`, `Actor`, `InvoiceServiceOut`, `tasks`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0784313725490196 - nodes in this community are weakly interconnected._