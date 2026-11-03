# Graph Report - avant-api  (2026-11-03)

## Corpus Check
- 267 files · ~80,492 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3517 nodes · 9562 edges · 208 communities (106 shown, 102 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1599 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `91399a0a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- ContractService
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
- PageOut
- Groone Avant: contexto do projeto
- api_keys/controller.py
- pydantic
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- google/controller.py
- dashboard_templates/controller.py
- invoice_pdf.py
- audit/controller.py
- clean_code.py
- CapturingMailer
- mfa/controller.py
- Avant: repositório e plano do MVP
- get
- clients/controller.py
- Actor
- session-start.sh
- avant-api
- .teams
- test_sites.py
- invoices/controller.py
- export.py
- UnitOfWorkFactory
- CompanyService
- AuthService
- install
- MemoryBucket
- commissions/dto.py
- io
- views/controller.py
- SessionCookies
- avant_core_access_models
- client_notes/controller.py
- ReportResultOut
- ProfileService
- edit
- currencies/controller.py
- members/controller.py
- goals/controller.py
- GoogleService
- edit_image
- account/controller.py
- health/controller.py
- Actor
- Actor
- mcm/controller.py
- CapturingMailer
- sites/service.py
- documents/controller.py
- Limiter
- auth/service.py
- sqlalchemy
- GoogleFailed
- avant-api
- networks/controller.py
- uuid
- people/controller.py
- Avant: conexão com o GAM
- GoalService
- costs/controller.py
- _month
- CommissionService
- ClientDocumentService
- test_dashboards.py
- InvoiceService
- events.py
- download
- Avant: grupos na Empresa e imagem da Empresa
- test_members_without_schedules_manage_only_see_what_they_receive
- UUID
- Actor
- GoalTemplateOut
- .of
- update_item
- .assign
- commissions/service.py
- ContractClientRefOut
- client_documents/controller.py
- test_alerts.py
- ClientService
- mine
- contracts/controller.py
- reports/service.py
- SiteListOut
- person
- security.py
- company/controller.py
- _enable
- networks/service.py
- test_account.py
- show
- delete_template
- google/controller.py
- ItemsOut
- members
- edit_contract
- contracts
- google_status
- download
- google_start
- enqueue_sync
- clients
- test_events_route
- middleware.py
- google.py
- .run_guarded
- .classify
- TaskQueue
- document_response
- AuditOut
- .of
- logs.py
- GoogleAuth
- MemoryCounter
- image
- events
- test_staff_sees_client_networks_sites_and_revenue_status
- index
- RedisEvents
- images.py
- test_goal_progress_routes
- test_who_sees_and_changes_invoices
- FakeGoogle
- _contract_fields

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 135 edges
2. `PageOut` - 128 edges
3. `_onboard_owner()` - 121 edges
4. `_csrf()` - 120 edges
5. `UnitOfWorkFactory` - 115 edges
6. `get()` - 112 edges
7. `Services` - 110 edges
8. `ReportService` - 75 edges
9. `InvoiceService` - 58 edges
10. `ClientService` - 55 edges

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

## Communities (208 total, 102 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.09
Nodes (31): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+23 more)

### Community 1 - "ContractService"
Cohesion: 0.19
Nodes (3): contract(), ContractOut, ContractService

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.09
Nodes (22): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+14 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "require_staff"
Cohesion: 0.08
Nodes (15): api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor(), get_session_auth(), optional_auth() (+7 more)

### Community 6 - ".save_rule"
Cohesion: 0.18
Nodes (4): create_rule(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 7 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "test_company_image.py"
Cohesion: 0.10
Nodes (16): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person() (+8 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "PageOut"
Cohesion: 0.10
Nodes (10): networks(), sites(), ClientNetworkOut, ClientSiteOut, ClientInventoryService, SiteOut, page_out(), PageOut (+2 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.11
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "pydantic"
Cohesion: 0.09
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "google/controller.py"
Cohesion: 0.06
Nodes (13): CsrfFailed, GoogleUnavailable, NoActiveCompany, QueryTooHeavy, RateLimited, get_cookies(), Settings, google_redirects() (+5 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "audit/controller.py"
Cohesion: 0.17
Nodes (3): index(), audit_service(), AuditService

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "CapturingMailer"
Cohesion: 0.22
Nodes (12): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), verify(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "get"
Cohesion: 0.11
Nodes (8): available_months(), get(), mine(), payment_details(), pdf(), service_options(), services(), team()

### Community 31 - "clients/controller.py"
Cohesion: 0.11
Nodes (15): client_options(), new_owner(), register_client(), client_service(), ClientDetailOut, ClientIn, ClientMemberOut, ClientOptionOut (+7 more)

### Community 32 - "Actor"
Cohesion: 0.06
Nodes (15): catalog(), create(), create_from_template(), delete(), duplicate(), index(), pin(), pinned() (+7 more)

### Community 37 - "test_sites.py"
Cohesion: 0.30
Nodes (4): _inventory(), test_manual_site(), test_site_category_and_responsible(), test_sites_and_assignment()

### Community 38 - "invoices/controller.py"
Cohesion: 0.18
Nodes (10): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn (+2 more)

### Community 39 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 41 - "CompanyService"
Cohesion: 0.21
Nodes (3): show(), CompanyDetailOut, CompanyService

### Community 42 - "AuthService"
Cohesion: 0.10
Nodes (3): accept(), AcceptInvitationIn, AuthService

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "MemoryBucket"
Cohesion: 0.17
Nodes (6): BucketResult, BucketRule, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 45 - "commissions/dto.py"
Cohesion: 0.17
Nodes (4): CommissionMonthOut, CommissionSettingsIn, dollars(), MonthIn

### Community 46 - "io"
Cohesion: 0.27
Nodes (3): _result(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "SessionCookies"
Cohesion: 0.14
Nodes (3): SessionCookies, do_logout(), login()

### Community 49 - "avant_core_access_models"
Cohesion: 0.04
Nodes (14): results(), client_result_service(), ClientResultService, invite(), options(), staff(), staff_service(), StaffInviteIn (+6 more)

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "ReportResultOut"
Cohesion: 0.07
Nodes (5): export(), export_saved(), query(), ReportQueryIn, ReportResultOut

### Community 52 - "ProfileService"
Cohesion: 0.06
Nodes (7): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.15
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+6 more)

### Community 57 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 59 - "edit_image"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 60 - "account/controller.py"
Cohesion: 0.10
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 62 - "health/controller.py"
Cohesion: 0.15
Nodes (4): health(), ready(), health_service(), HealthService

### Community 63 - "Actor"
Cohesion: 0.11
Nodes (8): audit(), cancel_owner(), change_status(), client(), client_image(), edit_client(), manager_change(), remove_client_image()

### Community 64 - "Actor"
Cohesion: 0.15
Nodes (6): ad_units(), assign_sites(), delete(), site_options(), sites_of_member(), unlinked()

### Community 65 - "mcm/controller.py"
Cohesion: 0.12
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "CapturingMailer"
Cohesion: 0.12
Nodes (25): CapturingMailer, Sent, _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit() (+17 more)

### Community 67 - "sites/service.py"
Cohesion: 0.18
Nodes (5): link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteIn

### Community 68 - "documents/controller.py"
Cohesion: 0.15
Nodes (4): document_service(), DocumentService, document_upload(), DocumentsOut

### Community 69 - "Limiter"
Cohesion: 0.08
Nodes (7): TooManyAttempts, Bucket, Counter, Limiter, Rule, _limiter_round(), test_memory_limiter()

### Community 70 - "auth/service.py"
Cohesion: 0.11
Nodes (11): company_image(), get_invitation(), me(), set_active_company(), ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn (+3 more)

### Community 71 - "sqlalchemy"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 72 - "GoogleFailed"
Cohesion: 0.21
Nodes (3): GoogleFailed, _claims(), identity_from_id_token()

### Community 74 - "networks/controller.py"
Cohesion: 0.15
Nodes (11): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+3 more)

### Community 75 - "uuid"
Cohesion: 0.24
Nodes (15): test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+7 more)

### Community 76 - "people/controller.py"
Cohesion: 0.11
Nodes (10): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+2 more)

### Community 77 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 78 - "GoalService"
Cohesion: 0.23
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 81 - "CommissionService"
Cohesion: 0.24
Nodes (4): set_settings(), settings(), CommissionSettingsOut, CommissionService

### Community 83 - "test_dashboards.py"
Cohesion: 0.28
Nodes (7): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit()

### Community 84 - "InvoiceService"
Cohesion: 0.24
Nodes (5): create_service(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 85 - "events.py"
Cohesion: 0.21
Nodes (4): channel(), EventSource, _parse(), sse()

### Community 86 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 89 - "test_members_without_schedules_manage_only_see_what_they_receive"
Cohesion: 0.24
Nodes (3): _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 91 - "UUID"
Cohesion: 0.13
Nodes (8): add_item(), create(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft()

### Community 92 - "Actor"
Cohesion: 0.22
Nodes (3): role_goals(), templates(), RoleGoalOut

### Community 95 - "GoalTemplateOut"
Cohesion: 0.14
Nodes (4): create_template(), template_options(), GoalTemplateIn, GoalTemplateOut

### Community 96 - ".of"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 98 - ".assign"
Cohesion: 0.40
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 128 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 130 - "client_documents/controller.py"
Cohesion: 0.22
Nodes (5): client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, DocumentOut

### Community 131 - "test_alerts.py"
Cohesion: 0.35
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 132 - "ClientService"
Cohesion: 0.09
Nodes (7): edit_client_image(), invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, ClientService, owner_invitation_out()

### Community 134 - "contracts/controller.py"
Cohesion: 0.26
Nodes (6): contract_service(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut

### Community 136 - "reports/service.py"
Cohesion: 0.07
Nodes (18): templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn (+10 more)

### Community 142 - "security.py"
Cohesion: 0.03
Nodes (25): _google(), _mailer(), Services, NoEvents, GoogleOAuth, RedisBucket, RedisCounter, configure_logging() (+17 more)

### Community 143 - "company/controller.py"
Cohesion: 0.20
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 144 - "_enable"
Cohesion: 0.22
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 145 - "networks/service.py"
Cohesion: 0.18
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 146 - "test_account.py"
Cohesion: 0.16
Nodes (12): client(), engine(), mailer(), _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password() (+4 more)

### Community 155 - "google/controller.py"
Cohesion: 0.18
Nodes (3): client_info(), image_response(), image_upload()

### Community 158 - "ItemsOut"
Cohesion: 0.19
Nodes (5): delete_rule(), person(), rules(), commission_service(), ItemsOut

### Community 160 - "members"
Cohesion: 0.33
Nodes (3): members(), SiteMemberOut, SiteService

### Community 161 - "edit_contract"
Cohesion: 0.16
Nodes (5): contract_networks(), edit_contract(), finish_contract(), new_contract(), remove_contract()

### Community 162 - "contracts"
Cohesion: 0.15
Nodes (8): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contracts()

### Community 164 - "download"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 168 - "test_events_route"
Cohesion: 0.25
Nodes (6): _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 175 - ".classify"
Cohesion: 0.27
Nodes (4): classify(), classify_many(), SitePatchIn, SitesPatchIn

### Community 185 - "test_staff_sees_client_networks_sites_and_revenue_status"
Cohesion: 0.38
Nodes (3): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 188 - "RedisEvents"
Cohesion: 0.47
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 190 - "test_goal_progress_routes"
Cohesion: 0.53
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 191 - "test_who_sees_and_changes_invoices"
Cohesion: 0.53
Nodes (3): test_invoice_lifecycle(), test_who_sees_and_changes_invoices(), _validated_month()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1617 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **102 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `.__init__`, `client_documents/controller.py`, `DashboardService`, `AlertService`, `ClientService`, `contracts/controller.py`, `ContractService`, `reports/service.py`, `roles/controller.py`, `schedules/controller.py`, `goals/service.py`, `.trusted_uow`, `GroupService`, `PageOut`, `company/controller.py`, `api_keys/controller.py`, `pydantic`, `networks/service.py`, `custom_metrics/controller.py`, `.__init__`, `google/controller.py`, `dashboard_templates/controller.py`, `.__init__`, `audit/controller.py`, `mfa/controller.py`, `clients/controller.py`, `Actor`, `members`, `invoices/controller.py`, `CompanyService`, `AuthService`, `views/controller.py`, `TaskQueue`, `avant_core_access_models`, `client_notes/controller.py`, `ProfileService`, `GoogleAuth`, `currencies/controller.py`, `members/controller.py`, `GoogleService`, `account/controller.py`, `.uow`, `mcm/controller.py`, `.__init__`, `sites/service.py`, `documents/controller.py`, `Limiter`, `auth/service.py`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `people/controller.py`, `.__init__`, `GoalService`, `costs/controller.py`, `.__init__`, `CommissionService`, `ClientDocumentService`, `networks/controller.py`, `InvoiceService`, `commissions/service.py`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Are the 99 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 99 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.08591466978375219 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `ContractService`, `roles/controller.py`, `DashboardService`, `AlertService`, `ClientService`, `contracts/controller.py`, `reports/service.py`, `schedules/controller.py`, `goals/service.py`, `.trusted_uow`, `GroupService`, `security.py`, `api_keys/controller.py`, `pydantic`, `networks/service.py`, `audit/controller.py`, `.show`, `get`, `clients/controller.py`, `members`, `contracts`, `.teams`, `invoices/controller.py`, `clients`, `avant_core_access_models`, `AuditOut`, `client_notes/controller.py`, `members/controller.py`, `goals/controller.py`, `index`, `Actor`, `Actor`, `mcm/controller.py`, `sites/service.py`, `networks/controller.py`, `people/controller.py`, `GoalService`, `costs/controller.py`, `InvoiceService`, `UUID`, `Actor`, `GoalTemplateOut`?**
  _High betweenness centrality (0.091) - this node is a cross-community bridge._
- **Are the 52 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 52 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07441016333938294 - nodes in this community are weakly interconnected._