# Graph Report - avant-api  (2026-11-03)

## Corpus Check
- 284 files · ~84,808 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3763 nodes · 10249 edges · 204 communities (99 shown, 105 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1717 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `e1e5b2e6`
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
- test_api_keys.py
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
- clients/controller.py
- ReportResultOut
- session-start.sh
- avant-api
- shared/dto.py
- tasks/controller.py
- invoices/controller.py
- export.py
- ItemsOut
- company/controller.py
- auth/controller.py
- install
- MemoryBucket
- dollars
- _onboard_owner
- views/controller.py
- google/controller.py
- avant_core_access_models
- client_notes/controller.py
- TaskQueue
- ProfileService
- edit
- currencies/controller.py
- members/controller.py
- ItemsOut
- GoogleService
- checklists/controller.py
- account/controller.py
- health/controller.py
- Actor
- Actor
- mcm/controller.py
- CapturingMailer
- sites/controller.py
- documents/controller.py
- Limiter
- page_out
- sqlalchemy
- google.py
- avant-api
- networks/controller.py
- uuid
- people/controller.py
- Avant: conexão com o GAM
- costs/controller.py
- _month
- set_settings
- ClientDocumentService
- test_dashboards.py
- InvoiceServiceOut
- test_events.py
- download
- Avant: grupos na Empresa e imagem da Empresa
- AuthService
- checklists/dto.py
- get
- commissions/controller.py
- ClientOut
- GoalService
- .catalog
- update_item
- client_documents/controller.py
- SessionCookies
- test_alerts.py
- ClientService
- mine
- AdUnitOut
- SiteListOut
- reports/service.py
- SiteOut
- person
- router.py
- Services
- UnitOfWorkFactory
- _enable
- checklists/service.py
- test_account.py
- RedisBucket
- test_site_category_and_responsible
- show
- Actor
- client_image
- AuditOut
- ItemsOut
- SiteService
- RecordingQueue
- NoEvents
- download
- tasks.py
- .owner_invitations
- document_response
- create_app
- .build
- events/controller.py
- test_staff_sees_client_networks_sites_and_revenue_status
- images.py

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 142 edges
2. `PageOut` - 138 edges
3. `_csrf()` - 127 edges
4. `_onboard_owner()` - 126 edges
5. `UnitOfWorkFactory` - 124 edges
6. `get()` - 119 edges
7. `Services` - 116 edges
8. `ReportService` - 75 edges
9. `_staff()` - 60 edges
10. `InvoiceService` - 58 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/modules/company/controller.py
- `Imagem da Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/08-grupos-e-imagem-da-empresa.md → src/avant_api/modules/company/controller.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (204 total, 105 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.07
Nodes (37): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+29 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (24): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+16 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (21): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+13 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "require_staff"
Cohesion: 0.20
Nodes (4): require(), dependency(), require_session(), api_key_service()

### Community 6 - ".save_rule"
Cohesion: 0.16
Nodes (5): create_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 7 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.08
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "test_company_image.py"
Cohesion: 0.10
Nodes (16): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person() (+8 more)

### Community 12 - ".trusted_uow"
Cohesion: 0.09
Nodes (11): add_item(), create(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft() (+3 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/controller.py"
Cohesion: 0.08
Nodes (9): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService (+1 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "pydantic"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

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
Cohesion: 0.18
Nodes (3): index(), audit_service(), AuditService

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "CapturingMailer"
Cohesion: 0.22
Nodes (12): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (10): auth_service(), confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 31 - "clients/controller.py"
Cohesion: 0.16
Nodes (13): client_service(), ClientDetailOut, ClientIn, ClientMemberOut, ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+5 more)

### Community 32 - "ReportResultOut"
Cohesion: 0.09
Nodes (13): create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin(), pinned() (+5 more)

### Community 37 - "tasks/controller.py"
Cohesion: 0.05
Nodes (18): change(), comment(), create(), task(), tasks(), support_task_service(), TaskClientOut, TaskCommentIn (+10 more)

### Community 38 - "invoices/controller.py"
Cohesion: 0.21
Nodes (8): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, ReturnedOut, ReturnIn, ServiceItemIn

### Community 39 - "export.py"
Cohesion: 0.09
Nodes (11): _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell(), _result() (+3 more)

### Community 40 - "ItemsOut"
Cohesion: 0.11
Nodes (4): invite(), options(), StaffInviteIn, StaffService

### Community 41 - "company/controller.py"
Cohesion: 0.08
Nodes (12): edit(), edit_fiscal(), edit_image(), fiscal(), image(), remove_image(), show(), CompanyDetailOut (+4 more)

### Community 42 - "auth/controller.py"
Cohesion: 0.11
Nodes (13): accept(), company_image(), do_logout(), login(), me(), set_active_company(), AcceptInvitationIn, ActiveCompanyIn (+5 more)

### Community 43 - "install"
Cohesion: 0.12
Nodes (10): CsrfFailed, error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), NoActiveCompany (+2 more)

### Community 44 - "MemoryBucket"
Cohesion: 0.14
Nodes (6): BucketResult, BucketRule, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 46 - "_onboard_owner"
Cohesion: 0.22
Nodes (14): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format() (+6 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "google/controller.py"
Cohesion: 0.08
Nodes (6): new_verifier(), Settings, google_start(), google_redirects(), GoogleStatusOut, GoogleRedirects

### Community 49 - "avant_core_access_models"
Cohesion: 0.05
Nodes (11): results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut (+3 more)

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 52 - "ProfileService"
Cohesion: 0.08
Nodes (9): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService (+1 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (16): API first e chaves de API, Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa (+8 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 57 - "ItemsOut"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "GoogleService"
Cohesion: 0.06
Nodes (7): GoogleUnavailable, GoogleAuth, google_callback(), google_status(), google_unlink(), google_service(), GoogleService

### Community 59 - "checklists/controller.py"
Cohesion: 0.11
Nodes (12): add_note(), check(), checklist(), checklists(), delete_note(), edit_note(), mark(), months() (+4 more)

### Community 60 - "account/controller.py"
Cohesion: 0.10
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 62 - "health/controller.py"
Cohesion: 0.10
Nodes (3): ready(), health_service(), HealthService

### Community 63 - "Actor"
Cohesion: 0.10
Nodes (13): audit(), cancel_owner(), change_status(), client(), client_options(), client_teams(), edit_client_image(), invite_owner() (+5 more)

### Community 64 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), classify(), delete(), members(), site_options(), unlinked()

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (8): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut, PageOut

### Community 66 - "CapturingMailer"
Cohesion: 0.16
Nodes (12): CapturingMailer, mailer(), Sent, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team() (+4 more)

### Community 67 - "sites/controller.py"
Cohesion: 0.23
Nodes (5): classify_many(), MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 68 - "documents/controller.py"
Cohesion: 0.15
Nodes (4): document_service(), DocumentService, document_upload(), DocumentsOut

### Community 69 - "Limiter"
Cohesion: 0.11
Nodes (6): Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "sqlalchemy"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 72 - "google.py"
Cohesion: 0.09
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 74 - "networks/controller.py"
Cohesion: 0.07
Nodes (15): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+7 more)

### Community 75 - "uuid"
Cohesion: 0.18
Nodes (17): _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency(), test_pinned_reports_and_preview_refresh() (+9 more)

### Community 76 - "people/controller.py"
Cohesion: 0.10
Nodes (9): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), PersonOut, PeopleService (+1 more)

### Community 77 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "_month"
Cohesion: 0.18
Nodes (4): _month(), team(), PersonMonthOut, CommissionService

### Community 83 - "test_dashboards.py"
Cohesion: 0.28
Nodes (7): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit()

### Community 84 - "InvoiceServiceOut"
Cohesion: 0.19
Nodes (5): create_service(), services(), update_service(), InvoiceServiceIn, InvoiceServiceOut

### Community 85 - "test_events.py"
Cohesion: 0.11
Nodes (12): channel(), _parse(), RedisEvents, sse(), _collect(), _event(), ListEvents, test_events_route() (+4 more)

### Community 86 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.20
Nodes (9): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Imagem da Empresa, Issues, Modelo de dados, Regras, Resumo (+1 more)

### Community 89 - "checklists/dto.py"
Cohesion: 0.11
Nodes (6): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 91 - "get"
Cohesion: 0.14
Nodes (7): available_months(), get(), mine(), payment_details(), pdf(), service_options(), team()

### Community 92 - "commissions/controller.py"
Cohesion: 0.22
Nodes (6): commission_service(), AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn

### Community 94 - "ClientOut"
Cohesion: 0.10
Nodes (4): clients(), edit_client(), ClientOut, image_url()

### Community 95 - "GoalService"
Cohesion: 0.05
Nodes (19): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+11 more)

### Community 128 - "client_documents/controller.py"
Cohesion: 0.22
Nodes (5): client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, DocumentOut

### Community 131 - "test_alerts.py"
Cohesion: 0.25
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 134 - "AdUnitOut"
Cohesion: 0.18
Nodes (4): ad_units(), link(), AdUnitOut, AdUnitPatchIn

### Community 135 - "SiteListOut"
Cohesion: 0.15
Nodes (3): create(), index(), SiteListOut

### Community 136 - "reports/service.py"
Cohesion: 0.05
Nodes (22): Bucket, templates(), CustomCatalogMetricOut, dimension_text(), DimensionOut, FilterIn, LabelOut, MetricCatalogOut (+14 more)

### Community 139 - "router.py"
Cohesion: 0.15
Nodes (4): require_staff(), people_service(), staff(), staff_service()

### Community 142 - "Services"
Cohesion: 0.05
Nodes (21): Services, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_cookies(), get_services() (+13 more)

### Community 144 - "_enable"
Cohesion: 0.22
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 146 - "test_account.py"
Cohesion: 0.40
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 148 - "test_site_category_and_responsible"
Cohesion: 0.36
Nodes (4): _inventory(), test_manual_site(), test_site_category_and_responsible(), test_sites_and_assignment()

### Community 152 - "Actor"
Cohesion: 0.06
Nodes (6): RateLimited, create(), SavedReportIn, SavedReportOut, ReportService, _statement_timeout()

### Community 158 - "ItemsOut"
Cohesion: 0.15
Nodes (3): adjust(), delete_rule(), settings()

### Community 160 - "SiteService"
Cohesion: 0.24
Nodes (3): site_service(), SiteMemberOut, SiteService

### Community 161 - "RecordingQueue"
Cohesion: 0.18
Nodes (7): RecordingQueue, _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list(), test_staff_marks_checks_and_writes_notes(), _agent(), test_staff_opens_assigns_and_comments_on_tasks()

### Community 164 - "download"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 166 - "tasks.py"
Cohesion: 0.14
Nodes (5): CeleryQueue, client(), engine(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 180 - "create_app"
Cohesion: 0.10
Nodes (6): configure_logging(), JsonFormatter, observe(), _route_template(), create_app(), health()

### Community 182 - ".build"
Cohesion: 0.13
Nodes (3): _google(), _mailer(), MemoryCounter

### Community 184 - "events/controller.py"
Cohesion: 0.15
Nodes (4): EventSource, events(), event_service(), EventService

### Community 185 - "test_staff_sees_client_networks_sites_and_revenue_status"
Cohesion: 0.38
Nodes (3): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1724 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **105 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `client_documents/controller.py`, `.__init__`, `contracts/controller.py`, `DashboardService`, `AlertService`, `ClientService`, `ProfileService`, `roles/controller.py`, `reports/service.py`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `inventory/controller.py`, `api_keys/controller.py`, `checklists/service.py`, `pydantic`, `custom_metrics/controller.py`, `.__init__`, `dashboard_templates/controller.py`, `Actor`, `audit/controller.py`, `mfa/controller.py`, `.__init__`, `clients/controller.py`, `SiteService`, `.__init__`, `invoices/controller.py`, `.__init__`, `ItemsOut`, `.__init__`, `auth/controller.py`, `company/controller.py`, `.__init__`, `tasks/controller.py`, `.__init__`, `views/controller.py`, `.__init__`, `avant_core_access_models`, `client_notes/controller.py`, `.__init__`, `TaskQueue`, `.__init__`, `currencies/controller.py`, `.__init__`, `members/controller.py`, `ItemsOut`, `GoogleService`, `.__init__`, `account/controller.py`, `.__init__`, `checklists/controller.py`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `mcm/controller.py`, `documents/controller.py`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `networks/controller.py`, `sites/controller.py`, `people/controller.py`, `.__init__`, `costs/controller.py`, `_month`, `ClientDocumentService`, `AuthService`, `commissions/controller.py`, `GoalService`, `.__init__`?**
  _High betweenness centrality (0.116) - this node is a cross-community bridge._
- **Are the 104 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 104 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.06921529175050302 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `mcm/controller.py` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `require_staff`, `ClientService`, `SiteListOut`, `reports/service.py`, `schedules/controller.py`, `SiteOut`, `router.py`, `.trusted_uow`, `GroupService`, `inventory/controller.py`, `api_keys/controller.py`, `checklists/service.py`, `pydantic`, `audit/controller.py`, `clients/controller.py`, `SiteService`, `shared/dto.py`, `tasks/controller.py`, `invoices/controller.py`, `ItemsOut`, `.owner_invitations`, `avant_core_access_models`, `client_notes/controller.py`, `members/controller.py`, `checklists/controller.py`, `Actor`, `Actor`, `sites/controller.py`, `page_out`, `networks/controller.py`, `people/controller.py`, `costs/controller.py`, `InvoiceServiceOut`, `get`, `ClientOut`, `GoalService`, `.page`?**
  _High betweenness centrality (0.089) - this node is a cross-community bridge._
- **Are the 56 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 56 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.060718252499074414 - nodes in this community are weakly interconnected._