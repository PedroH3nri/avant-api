# Graph Report - avant-api  (2026-11-04)

## Corpus Check
- 290 files · ~86,576 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3850 nodes · 10515 edges · 197 communities (102 shown, 95 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1762 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `fd7e275b`
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
- ReportResultOut
- company/controller.py
- .page_saved
- session-start.sh
- avant-api
- networks/service.py
- tasks/controller.py
- invoices/controller.py
- export.py
- ItemsOut
- CompanyService
- auth/controller.py
- install
- MemoryBucket
- _onboard_owner
- views/controller.py
- Settings
- avant_core_access_models
- client_notes/controller.py
- UserOut
- profile/controller.py
- edit
- currencies/controller.py
- members/controller.py
- conftest.py
- ItemsOut
- GoogleService
- checklists/controller.py
- AccountService
- UUID
- health/controller.py
- ClientService
- Actor
- mcm/controller.py
- checklists
- sites/controller.py
- documents/controller.py
- Limiter
- account/controller.py
- google.py
- avant-api
- networks/controller.py
- uuid
- people/controller.py
- Avant: conexão com o GAM
- test_company_image.py
- costs/controller.py
- _month
- CommissionService
- ClientDocumentService
- test_dashboards.py
- InvoiceServiceOut
- test_events.py
- download
- Avant: grupos na Empresa e imagem da Empresa
- AuthService
- checklists/dto.py
- get
- commissions/dto.py
- ClientOut
- GoalService
- update_item
- .page
- .assign
- client_documents/controller.py
- test_alerts.py
- do_reset_password
- mine
- AdUnitOut
- SiteListOut
- reports/service.py
- .classify
- person
- image
- Services
- UnitOfWorkFactory
- _staff
- templates
- test_account.py
- Counter
- .run_guarded
- delete_session
- Actor
- image
- commissions/controller.py
- SiteService
- edit_image
- test_staff_manage_templates_and_clients_see_them_by_role
- GAM
- download
- tasks.py
- index
- edit_image
- test_goal_progress_routes
- commissions/dependencies.py
- document_response
- create_app
- .build
- events.py
- images.py
- ResultService

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
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py
- `Pipeline` --references--> `main()`  [INFERRED]
  docs/decisoes/07-repositorios-e-plano.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (197 total, 95 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.10
Nodes (22): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+14 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (23): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem, metrics(), contract(), contract_networks() (+15 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.06
Nodes (23): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+15 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "require_staff"
Cohesion: 0.09
Nodes (15): api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor(), get_session_auth(), optional_auth() (+7 more)

### Community 7 - "GamToolService"
Cohesion: 0.06
Nodes (17): ads_txt(), install(), network(), networks(), run(), runs(), start(), gam_tool_service() (+9 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.10
Nodes (20): Acesso, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade (+12 more)

### Community 11 - "test_company_image.py"
Cohesion: 0.11
Nodes (16): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_site_category_and_responsible() (+8 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/controller.py"
Cohesion: 0.07
Nodes (11): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, page_out() (+3 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "pydantic"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

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
Cohesion: 0.16
Nodes (3): client_info(), image_response(), image_upload()

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "audit/controller.py"
Cohesion: 0.14
Nodes (3): index(), audit_service(), AuditService

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "CapturingMailer"
Cohesion: 0.22
Nodes (12): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "ReportResultOut"
Cohesion: 0.11
Nodes (4): query(), ReportQueryIn, ReportResultOut, ReportRowOut

### Community 31 - "company/controller.py"
Cohesion: 0.17
Nodes (5): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 36 - "networks/service.py"
Cohesion: 0.13
Nodes (4): NetworkIn, ServiceAccountOut, SyncRunOut, enqueue_sync()

### Community 37 - "tasks/controller.py"
Cohesion: 0.05
Nodes (18): change(), comment(), create(), task(), tasks(), support_task_service(), TaskClientOut, TaskCommentIn (+10 more)

### Community 38 - "invoices/controller.py"
Cohesion: 0.18
Nodes (10): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn (+2 more)

### Community 39 - "export.py"
Cohesion: 0.07
Nodes (11): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+3 more)

### Community 40 - "ItemsOut"
Cohesion: 0.12
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 41 - "CompanyService"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 42 - "auth/controller.py"
Cohesion: 0.10
Nodes (15): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), login(), me(), set_active_company() (+7 more)

### Community 43 - "install"
Cohesion: 0.08
Nodes (12): CsrfFailed, error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), NoActiveCompany (+4 more)

### Community 44 - "MemoryBucket"
Cohesion: 0.08
Nodes (9): Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket() (+1 more)

### Community 46 - "_onboard_owner"
Cohesion: 0.17
Nodes (9): CapturingMailer, Sent, _owner_invite(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company() (+1 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "Settings"
Cohesion: 0.11
Nodes (6): Settings, google_redirects(), google_service(), GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 49 - "avant_core_access_models"
Cohesion: 0.09
Nodes (8): results(), client_result_service(), ClientResultService, CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut, default_period()

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "UserOut"
Cohesion: 0.15
Nodes (3): PersonOut, person_out(), UserOut

### Community 52 - "profile/controller.py"
Cohesion: 0.20
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "conftest.py"
Cohesion: 0.07
Nodes (17): client(), engine(), mailer(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow() (+9 more)

### Community 57 - "ItemsOut"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "GoogleService"
Cohesion: 0.06
Nodes (9): GoogleUnavailable, GoogleAuth, new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), GoogleStatusOut (+1 more)

### Community 59 - "checklists/controller.py"
Cohesion: 0.14
Nodes (6): add_note(), check(), delete_note(), edit_note(), mark(), site_checklist_service()

### Community 60 - "AccountService"
Cohesion: 0.16
Nodes (5): do_change_password(), get_sessions(), revoke_others(), account_service(), AccountService

### Community 61 - "UUID"
Cohesion: 0.13
Nodes (8): add_item(), create(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft()

### Community 62 - "health/controller.py"
Cohesion: 0.17
Nodes (3): ready(), health_service(), HealthService

### Community 63 - "ClientService"
Cohesion: 0.05
Nodes (33): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), edit_client() (+25 more)

### Community 64 - "Actor"
Cohesion: 0.14
Nodes (7): ad_units(), delete(), link(), show(), site_options(), sites_of_member(), unlinked()

### Community 65 - "mcm/controller.py"
Cohesion: 0.12
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "checklists"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 67 - "sites/controller.py"
Cohesion: 0.25
Nodes (7): AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "documents/controller.py"
Cohesion: 0.15
Nodes (4): document_service(), DocumentService, document_upload(), DocumentsOut

### Community 69 - "Limiter"
Cohesion: 0.23
Nodes (5): Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "account/controller.py"
Cohesion: 0.32
Nodes (5): ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut, SessionOut

### Community 72 - "google.py"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 74 - "networks/controller.py"
Cohesion: 0.13
Nodes (11): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+3 more)

### Community 75 - "uuid"
Cohesion: 0.18
Nodes (25): _onboard_owner(), test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_option_lists_keep_the_permissions() (+17 more)

### Community 76 - "people/controller.py"
Cohesion: 0.17
Nodes (5): disable(), enable(), reset_mfa(), people_service(), PeopleService

### Community 77 - "Avant: conexão com o GAM"
Cohesion: 0.17
Nodes (10): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+2 more)

### Community 78 - "test_company_image.py"
Cohesion: 0.31
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 81 - "CommissionService"
Cohesion: 0.22
Nodes (5): set_settings(), settings(), update_rule(), CommissionSettingsOut, CommissionService

### Community 83 - "test_dashboards.py"
Cohesion: 0.28
Nodes (7): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit()

### Community 84 - "InvoiceServiceOut"
Cohesion: 0.24
Nodes (5): create_service(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 85 - "test_events.py"
Cohesion: 0.15
Nodes (12): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit(), _collect(), _event(), ListEvents (+4 more)

### Community 86 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "AuthService"
Cohesion: 0.09
Nodes (3): get_invitation(), auth_service(), AuthService

### Community 89 - "checklists/dto.py"
Cohesion: 0.09
Nodes (7): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 91 - "get"
Cohesion: 0.11
Nodes (8): available_months(), get(), mine(), payment_details(), pdf(), service_options(), services(), team()

### Community 92 - "commissions/dto.py"
Cohesion: 0.15
Nodes (4): CommissionMonthOut, CommissionRuleIn, CommissionSettingsIn, dollars()

### Community 94 - "ClientOut"
Cohesion: 0.07
Nodes (3): clients(), ClientRefOut, image_url()

### Community 95 - "GoalService"
Cohesion: 0.05
Nodes (19): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+11 more)

### Community 98 - ".page"
Cohesion: 0.17
Nodes (3): checklist(), ChecklistDetailOut, SiteChecklistService

### Community 127 - ".assign"
Cohesion: 0.25
Nodes (5): Atribuição de sites, GAM, Networks, Sites e ad units, assign_sites()

### Community 128 - "client_documents/controller.py"
Cohesion: 0.22
Nodes (5): client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, DocumentOut

### Community 131 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 136 - "reports/service.py"
Cohesion: 0.06
Nodes (14): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+6 more)

### Community 142 - "Services"
Cohesion: 0.07
Nodes (10): Estrutura, Services, get_services(), TaskQueue, cost_service(), contract_service(), saved_view_service(), report_service() (+2 more)

### Community 144 - "_staff"
Cohesion: 0.07
Nodes (27): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _network(), test_gam_tools_need_permission() (+19 more)

### Community 146 - "test_account.py"
Cohesion: 0.40
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 152 - "Actor"
Cohesion: 0.06
Nodes (15): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned() (+7 more)

### Community 158 - "commissions/controller.py"
Cohesion: 0.16
Nodes (6): adjust(), create_rule(), delete_rule(), rules(), AdjustmentIn, MonthIn

### Community 160 - "SiteService"
Cohesion: 0.22
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 162 - "test_staff_manage_templates_and_clients_see_them_by_role"
Cohesion: 0.38
Nodes (3): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company()

### Community 163 - "GAM"
Cohesion: 0.33
Nodes (6): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment

### Community 164 - "download"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 172 - "test_goal_progress_routes"
Cohesion: 0.53
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 180 - "create_app"
Cohesion: 0.10
Nodes (6): configure_logging(), JsonFormatter, observe(), _route_template(), create_app(), health()

### Community 182 - ".build"
Cohesion: 0.09
Nodes (6): _google(), _mailer(), NoEvents, RedisEvents, MemoryCounter, run()

### Community 184 - "events.py"
Cohesion: 0.11
Nodes (6): channel(), EventSource, _parse(), sse(), events(), EventService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1762 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **95 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `client_documents/controller.py`, `.__init__`, `contracts/controller.py`, `DashboardService`, `AlertService`, `roles/controller.py`, `GamToolService`, `reports/service.py`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `inventory/controller.py`, `api_keys/controller.py`, `pydantic`, `custom_metrics/controller.py`, `dashboard_templates/controller.py`, `Actor`, `audit/controller.py`, `mfa/controller.py`, `company/controller.py`, `SiteService`, `networks/service.py`, `.__init__`, `invoices/controller.py`, `tasks/controller.py`, `.__init__`, `CompanyService`, `auth/controller.py`, `ItemsOut`, `MemoryBucket`, `views/controller.py`, `avant_core_access_models`, `client_notes/controller.py`, `UserOut`, `profile/controller.py`, `currencies/controller.py`, `members/controller.py`, `ItemsOut`, `GoogleService`, `.__init__`, `AccountService`, `.__init__`, `ClientService`, `mcm/controller.py`, `.__init__`, `sites/controller.py`, `documents/controller.py`, `ResultService`, `account/controller.py`, `networks/controller.py`, `people/controller.py`, `costs/controller.py`, `CommissionService`, `ClientDocumentService`, `InvoiceServiceOut`, `AuthService`, `checklists/dto.py`, `commissions/dto.py`, `GoalService`, `.page`?**
  _High betweenness centrality (0.121) - this node is a cross-community bridge._
- **Are the 107 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 107 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.09795918367346938 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `inventory/controller.py` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `AdUnitOut`, `GamToolService`, `reports/service.py`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `api_keys/controller.py`, `pydantic`, `audit/controller.py`, `.page_saved`, `SiteService`, `networks/service.py`, `tasks/controller.py`, `invoices/controller.py`, `index`, `ItemsOut`, `avant_core_access_models`, `client_notes/controller.py`, `UserOut`, `members/controller.py`, `checklists/controller.py`, `ClientService`, `Actor`, `mcm/controller.py`, `checklists`, `sites/controller.py`, `networks/controller.py`, `people/controller.py`, `Avant: conexão com o GAM`, `costs/controller.py`, `InvoiceServiceOut`, `checklists/dto.py`, `get`, `ClientOut`, `GoalService`, `.show`, `.page`?**
  _High betweenness centrality (0.078) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06202435312024353 - nodes in this community are weakly interconnected._