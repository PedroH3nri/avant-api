# Graph Report - avant-api  (2026-11-02)

## Corpus Check
- 220 files · ~70,548 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 2946 nodes · 7971 edges · 158 communities (89 shown, 69 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1339 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1ec543b5`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- DashboardService
- clients/controller.py
- security.py
- .save_rule
- conftest.py
- steps
- _month
- Avant: models do MVP
- _member_client
- .trusted_uow
- GroupService
- networks/controller.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- pydantic
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- goals/controller.py
- invoice_pdf.py
- NetworkDetailOut
- clean_code.py
- CapturingMailer
- mfa/controller.py
- Avant: repositório e plano do MVP
- get
- ReportService
- Actor
- session-start.sh
- avant-api
- shared/dto.py
- _member_client
- invoices/controller.py
- export.py
- test_account.py
- CompanyService
- Settings
- errors.py
- limits.py
- InvoiceService
- _onboard_owner
- networks/service.py
- datetime
- Services
- .of
- UnitOfWorkFactory
- edit
- currencies/controller.py
- members/controller.py
- staff/controller.py
- health/controller.py
- mine
- company/controller.py
- account/controller.py
- Actor
- verify
- UUID
- ItemsOut
- mcm/controller.py
- test_networks.py
- datetime
- reports/controller.py
- Limiter
- auth/controller.py
- sqlalchemy
- google.py
- avant-api
- GoalService
- uuid
- people/controller.py
- .catalog
- commissions/dto.py
- GoalTemplateIn
- dollars
- GoogleService
- mine
- test_dashboards.py
- add_item
- events.py
- edit_image
- Avant: grupos na Empresa e imagem da Empresa
- test_events.py
- main.py
- UserOut
- tasks.py
- ClientOut
- .page_saved
- source_files
- PayeeDetailsOut
- delete_rule
- goals/service.py
- team
- test_api.py
- .build
- Actor
- image
- Actor
- events/controller.py
- reports/service.py
- images.py
- CommissionService
- AuditOut
- PageOut
- person
- templates
- events
- RedisEvents
- clients
- FakeGoogle
- ClientProfileIn
- google/controller.py

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 114 edges
2. `PageOut` - 107 edges
3. `_csrf()` - 102 edges
4. `_onboard_owner()` - 102 edges
5. `get()` - 95 edges
6. `Services` - 94 edges
7. `UnitOfWorkFactory` - 91 edges
8. `ReportService` - 68 edges
9. `InvoiceService` - 58 edges
10. `ClientService` - 54 edges

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

## Communities (158 total, 69 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.10
Nodes (27): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+19 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.05
Nodes (24): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem, metrics(), contract(), contract_networks() (+16 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (21): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+13 more)

### Community 4 - "clients/controller.py"
Cohesion: 0.16
Nodes (9): manager_change(), new_owner(), client_service(), ClientIn, ClientOptionOut, ClientPatchIn, ClientStatusIn, ManagerChangeOut (+1 more)

### Community 5 - "security.py"
Cohesion: 0.11
Nodes (13): api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor(), optional_auth(), dependency() (+5 more)

### Community 6 - ".save_rule"
Cohesion: 0.17
Nodes (5): create_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 7 - "conftest.py"
Cohesion: 0.14
Nodes (9): client(), engine(), mailer(), Sent, _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys() (+1 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.16
Nodes (7): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture()

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "networks/controller.py"
Cohesion: 0.15
Nodes (9): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs(), network_service() (+1 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "pydantic"
Cohesion: 0.09
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService, InvitationOut

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "costs/controller.py"
Cohesion: 0.09
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.18
Nodes (5): delete_template(), role_goals(), set_role_goal(), update_template(), RoleGoalIn

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "CapturingMailer"
Cohesion: 0.23
Nodes (12): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (10): get_session_auth(), confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "get"
Cohesion: 0.13
Nodes (8): available_months(), get(), mine(), payment_details(), pdf(), service_options(), services(), team()

### Community 31 - "ReportService"
Cohesion: 0.10
Nodes (5): create(), update(), SavedReportIn, SavedReportOut, ReportService

### Community 36 - "shared/dto.py"
Cohesion: 0.12
Nodes (4): ClientMemberOut, CompanyRefOut, RoleRefOut, UserOut

### Community 37 - "_member_client"
Cohesion: 0.14
Nodes (12): _membership_ids(), test_groups_lifecycle(), _inventory(), test_manual_site(), test_sites_and_assignment(), _member_client(), test_audit_log(), test_company_and_members() (+4 more)

### Community 38 - "invoices/controller.py"
Cohesion: 0.23
Nodes (9): AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn, ServiceItemIn (+1 more)

### Community 39 - "export.py"
Cohesion: 0.08
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 40 - "test_account.py"
Cohesion: 0.40
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 41 - "CompanyService"
Cohesion: 0.18
Nodes (3): show(), CompanyDetailOut, image_url()

### Community 42 - "Settings"
Cohesion: 0.11
Nodes (6): Settings, google_redirects(), google_service(), GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 43 - "errors.py"
Cohesion: 0.13
Nodes (10): CsrfFailed, error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), NoActiveCompany (+2 more)

### Community 44 - "limits.py"
Cohesion: 0.07
Nodes (9): Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket() (+1 more)

### Community 45 - "InvoiceService"
Cohesion: 0.16
Nodes (6): create_service(), update_service(), invoice_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 46 - "_onboard_owner"
Cohesion: 0.30
Nodes (10): CapturingMailer, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_option_lists_keep_the_permissions() (+2 more)

### Community 47 - "networks/service.py"
Cohesion: 0.13
Nodes (4): NetworkIn, ServiceAccountOut, SyncRunOut, enqueue_sync()

### Community 49 - "datetime"
Cohesion: 0.06
Nodes (9): results(), ClientResultService, show(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut, default_period() (+1 more)

### Community 50 - "Services"
Cohesion: 0.06
Nodes (12): Estrutura, Services, get_services(), TaskQueue, account_service(), audit_service(), auth_service(), cost_service() (+4 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "staff/controller.py"
Cohesion: 0.12
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 57 - "health/controller.py"
Cohesion: 0.17
Nodes (3): ready(), health_service(), HealthService

### Community 58 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), MyCommissionsOut

### Community 59 - "company/controller.py"
Cohesion: 0.17
Nodes (6): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 60 - "account/controller.py"
Cohesion: 0.10
Nodes (12): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn (+4 more)

### Community 61 - "Actor"
Cohesion: 0.23
Nodes (3): set_settings(), settings(), CommissionSettingsOut

### Community 62 - "verify"
Cohesion: 0.10
Nodes (3): SessionCookies, get_cookies(), verify()

### Community 63 - "UUID"
Cohesion: 0.14
Nodes (7): cancel_owner(), change_status(), client_image(), client_options(), client_teams(), edit_client_image(), remove_client_image()

### Community 64 - "ItemsOut"
Cohesion: 0.05
Nodes (26): Atribuição de sites, GAM, Networks, Sites e ad units, ad_units(), assign_sites(), create(), delete() (+18 more)

### Community 65 - "mcm/controller.py"
Cohesion: 0.11
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "test_networks.py"
Cohesion: 0.47
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 67 - "datetime"
Cohesion: 0.18
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 68 - "reports/controller.py"
Cohesion: 0.09
Nodes (14): create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned(), query() (+6 more)

### Community 69 - "Limiter"
Cohesion: 0.14
Nodes (6): Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "auth/controller.py"
Cohesion: 0.09
Nodes (15): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), AcceptInvitationIn (+7 more)

### Community 71 - "sqlalchemy"
Cohesion: 0.16
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 72 - "google.py"
Cohesion: 0.11
Nodes (7): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 74 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 75 - "uuid"
Cohesion: 0.28
Nodes (16): _onboard_owner(), _owner_invite(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused() (+8 more)

### Community 76 - "people/controller.py"
Cohesion: 0.07
Nodes (18): Modelo de dados, Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação (+10 more)

### Community 77 - ".catalog"
Cohesion: 0.18
Nodes (3): catalog(), CustomCatalogMetricOut, MetricCatalogOut

### Community 78 - "commissions/dto.py"
Cohesion: 0.18
Nodes (3): CommissionMonthOut, CommissionSettingsIn, MonthIn

### Community 81 - "GoogleService"
Cohesion: 0.07
Nodes (6): GoogleUnavailable, google_callback(), google_start(), google_status(), google_unlink(), GoogleService

### Community 82 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 83 - "test_dashboards.py"
Cohesion: 0.32
Nodes (6): _form(), _kpi(), _run(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit()

### Community 84 - "add_item"
Cohesion: 0.13
Nodes (8): add_item(), create(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft()

### Community 85 - "events.py"
Cohesion: 0.17
Nodes (4): channel(), EventSource, _parse(), sse()

### Community 86 - "edit_image"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "test_events.py"
Cohesion: 0.28
Nodes (6): _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 89 - "main.py"
Cohesion: 0.09
Nodes (6): configure_logging(), JsonFormatter, observe(), _route_template(), create_app(), health()

### Community 91 - "UserOut"
Cohesion: 0.08
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 94 - "ClientOut"
Cohesion: 0.15
Nodes (4): edit_client(), register_client(), ClientOut, ClientProfileOut

### Community 128 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 129 - "test_api.py"
Cohesion: 0.33
Nodes (6): test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format()

### Community 130 - ".build"
Cohesion: 0.10
Nodes (5): _google(), _mailer(), NoEvents, GoogleAuth, MemoryCounter

### Community 132 - "Actor"
Cohesion: 0.15
Nodes (3): client(), ClientDetailOut, ClientService

### Community 134 - "Actor"
Cohesion: 0.17
Nodes (5): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 136 - "reports/service.py"
Cohesion: 0.06
Nodes (10): DimensionOut, FilterIn, LabelOut, MetricOut, OrderIn, PeriodIn, PreviewPointOut, ReportCountsOut (+2 more)

### Community 139 - "CommissionService"
Cohesion: 0.21
Nodes (4): adjust(), commission_service(), AdjustmentIn, CommissionService

### Community 143 - "PageOut"
Cohesion: 0.10
Nodes (5): require(), index(), AuditService, page_out(), PageOut

### Community 147 - "RedisEvents"
Cohesion: 0.47
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 155 - "google/controller.py"
Cohesion: 0.11
Nodes (5): new_verifier(), GoogleStatusOut, client_info(), image_response(), image_upload()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1356 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **69 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `Actor`, `.__init__`, `reports/service.py`, `.__init__`, `CommissionService`, `.trusted_uow`, `GroupService`, `networks/controller.py`, `PageOut`, `api_keys/controller.py`, `pydantic`, `custom_metrics/controller.py`, `.__init__`, `costs/controller.py`, `mfa/controller.py`, `ReportService`, `shared/dto.py`, `invoices/controller.py`, `limits.py`, `InvoiceService`, `networks/service.py`, `datetime`, `currencies/controller.py`, `members/controller.py`, `staff/controller.py`, `company/controller.py`, `account/controller.py`, `ItemsOut`, `mcm/controller.py`, `auth/controller.py`, `GoalService`, `people/controller.py`, `GoogleService`, `UserOut`, `delete_rule`, `goals/service.py`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Are the 86 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 86 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.10235690235690235 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `clients/controller.py`, `Actor`, `Actor`, `reports/service.py`, `.trusted_uow`, `GroupService`, `AuditOut`, `networks/controller.py`, `api_keys/controller.py`, `pydantic`, `costs/controller.py`, `goals/controller.py`, `clients`, `NetworkDetailOut`, `get`, `shared/dto.py`, `invoices/controller.py`, `InvoiceService`, `networks/service.py`, `datetime`, `UnitOfWorkFactory`, `members/controller.py`, `staff/controller.py`, `UUID`, `ItemsOut`, `mcm/controller.py`, `GoalService`, `people/controller.py`, `.page_saved`, `goals/service.py`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Are the 43 inferred relationships involving `PageOut` (e.g. with `index()` and `ApiKeyService`) actually correct?**
  _`PageOut` has 43 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05401234567901234 - nodes in this community are weakly interconnected._