# Graph Report - avant-api  (2026-11-02)

## Corpus Check
- 214 files · ~68,357 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 2833 nodes · 7612 edges · 156 communities (85 shown, 71 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1267 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6aa2d3d7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- sites/controller.py
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
- GoalService
- invoice_pdf.py
- NetworkDetailOut
- clean_code.py
- CapturingMailer
- mfa/controller.py
- Avant: repositório e plano do MVP
- get
- ReportService
- ._run
- session-start.sh
- avant-api
- ClientService
- test_api_keys.py
- invoices/controller.py
- export.py
- test_account.py
- CompanyService
- results/dto.py
- errors.py
- limits.py
- InvoiceService
- _onboard_owner
- networks/service.py
- AuthService
- modules/results/controller.py
- Services
- .export_saved
- UnitOfWorkFactory
- edit
- currencies/controller.py
- members/controller.py
- health/controller.py
- mine
- company/controller.py
- account/controller.py
- Actor
- verify
- UUID
- Actor
- mcm/controller.py
- test_networks.py
- datetime
- reports/controller.py
- Limiter
- auth/controller.py
- sqlalchemy
- google/controller.py
- avant-api
- TaskQueue
- uuid
- people/controller.py
- .catalog
- commissions/dto.py
- .assign
- FiscalDataOut
- GoogleService
- commissions/controller.py
- add_item
- events.py
- edit_image
- Avant: grupos na Empresa e imagem da Empresa
- modules/results/service.py
- main.py
- UserOut
- CeleryQueue
- ClientOut
- .page_saved
- source_files
- PayeeDetailsOut
- delete_rule
- SiteService
- results
- PersonOut
- MemoryCounter
- Actor
- image
- Actor
- Avant: conexão com o GAM
- reports/service.py
- images.py
- CommissionService
- PageOut
- person
- create
- ItemsOut
- image_response

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 110 edges
2. `PageOut` - 105 edges
3. `_onboard_owner()` - 98 edges
4. `_csrf()` - 97 edges
5. `Services` - 92 edges
6. `get()` - 91 edges
7. `UnitOfWorkFactory` - 88 edges
8. `ReportService` - 62 edges
9. `InvoiceService` - 58 edges
10. `ClientService` - 54 edges

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

## Communities (156 total, 71 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.13
Nodes (24): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+16 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (24): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+16 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "sites/controller.py"
Cohesion: 0.28
Nodes (7): AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut

### Community 4 - "clients/controller.py"
Cohesion: 0.12
Nodes (8): client_options(), new_owner(), client_service(), ClientOptionOut, ClientProfileIn, ClientProfileOut, ClientStatusIn, OwnerChangeIn

### Community 5 - "security.py"
Cohesion: 0.10
Nodes (17): CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor() (+9 more)

### Community 6 - ".save_rule"
Cohesion: 0.20
Nodes (4): adjust(), create_rule(), update_rule(), CommissionRuleIn

### Community 7 - "conftest.py"
Cohesion: 0.10
Nodes (7): client(), engine(), mailer(), Sent, test_events_route(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.10
Nodes (16): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person() (+8 more)

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
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "pydantic"
Cohesion: 0.06
Nodes (14): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, cancel(), create_invitation() (+6 more)

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

### Community 22 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 23 - "GoalService"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+10 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.18
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "CapturingMailer"
Cohesion: 0.30
Nodes (11): CapturingMailer, _day(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "get"
Cohesion: 0.11
Nodes (10): available_months(), delete(), delete_service(), get(), mine(), payment_details(), pdf(), remove_item() (+2 more)

### Community 31 - "ReportService"
Cohesion: 0.11
Nodes (6): create(), duplicate(), update(), SavedReportIn, SavedReportOut, ReportService

### Community 32 - "._run"
Cohesion: 0.14
Nodes (3): QueryTooHeavy, RateLimited, _statement_timeout()

### Community 36 - "ClientService"
Cohesion: 0.16
Nodes (7): client_teams(), manager_change(), ClientMemberOut, ManagerChangeOut, ClientService, AuditOut, CompanyRefOut

### Community 37 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 38 - "invoices/controller.py"
Cohesion: 0.17
Nodes (11): create_service(), services(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceServiceOut, InvoiceSummaryOut (+3 more)

### Community 39 - "export.py"
Cohesion: 0.08
Nodes (11): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+3 more)

### Community 40 - "test_account.py"
Cohesion: 0.35
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 41 - "CompanyService"
Cohesion: 0.18
Nodes (4): show(), CompanyDetailOut, CompanyService, image_url()

### Community 42 - "results/dto.py"
Cohesion: 0.15
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 43 - "errors.py"
Cohesion: 0.12
Nodes (7): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), event_service()

### Community 44 - "limits.py"
Cohesion: 0.08
Nodes (8): BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 45 - "InvoiceService"
Cohesion: 0.14
Nodes (4): service_options(), update_service(), invoice_service(), InvoiceService

### Community 46 - "_onboard_owner"
Cohesion: 0.21
Nodes (16): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format(), test_costs_and_reports_come_in_pages() (+8 more)

### Community 47 - "networks/service.py"
Cohesion: 0.13
Nodes (4): NetworkIn, ServiceAccountOut, SyncRunOut, enqueue_sync()

### Community 49 - "modules/results/controller.py"
Cohesion: 0.13
Nodes (4): show(), result_service(), ResultsOut, ResultService

### Community 50 - "Services"
Cohesion: 0.05
Nodes (11): Services, get_services(), RecordingQueue, api_key_service(), auth_service(), company_service(), contract_service(), goal_service() (+3 more)

### Community 51 - ".export_saved"
Cohesion: 0.10
Nodes (3): query(), ReportQueryIn, ReportResultOut

### Community 52 - "UnitOfWorkFactory"
Cohesion: 0.07
Nodes (3): UnitOfWorkFactory, ClientResultService, page_out()

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 57 - "health/controller.py"
Cohesion: 0.14
Nodes (4): health(), ready(), health_service(), HealthService

### Community 59 - "company/controller.py"
Cohesion: 0.20
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (14): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+6 more)

### Community 61 - "Actor"
Cohesion: 0.23
Nodes (3): set_settings(), settings(), CommissionSettingsOut

### Community 63 - "UUID"
Cohesion: 0.18
Nodes (5): audit(), cancel_owner(), change_status(), edit_client_image(), remove_client_image()

### Community 64 - "Actor"
Cohesion: 0.14
Nodes (7): assign_sites(), delete(), index(), link(), show(), sites_of_member(), unlinked()

### Community 65 - "mcm/controller.py"
Cohesion: 0.11
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "test_networks.py"
Cohesion: 0.47
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 67 - "datetime"
Cohesion: 0.11
Nodes (11): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), test_invoice_lifecycle(), test_who_sees_and_changes_invoices(), _validated_month(), _enable(), _now_code() (+3 more)

### Community 68 - "reports/controller.py"
Cohesion: 0.10
Nodes (10): create_from_template(), delete(), export(), export_saved(), pin(), pinned(), run(), show() (+2 more)

### Community 69 - "Limiter"
Cohesion: 0.09
Nodes (7): TooManyAttempts, Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "auth/controller.py"
Cohesion: 0.10
Nodes (14): SessionCookies, accept(), company_image(), do_logout(), login(), me(), set_active_company(), AcceptInvitationIn (+6 more)

### Community 71 - "sqlalchemy"
Cohesion: 0.12
Nodes (8): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query(), _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 72 - "google/controller.py"
Cohesion: 0.05
Nodes (16): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), get_cookies(), google_callback() (+8 more)

### Community 75 - "uuid"
Cohesion: 0.17
Nodes (18): _owner_invite(), test_csv_header_escapes_formulas(), _metrics(), _row(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use() (+10 more)

### Community 76 - "people/controller.py"
Cohesion: 0.15
Nodes (6): disable(), enable(), reset_mfa(), users(), people_service(), PeopleService

### Community 77 - ".catalog"
Cohesion: 0.18
Nodes (3): catalog(), CustomCatalogMetricOut, MetricCatalogOut

### Community 79 - ".assign"
Cohesion: 0.20
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 81 - "GoogleService"
Cohesion: 0.08
Nodes (5): GoogleUnavailable, GoogleAuth, google_status(), google_unlink(), GoogleService

### Community 83 - "commissions/controller.py"
Cohesion: 0.22
Nodes (4): commission_service(), AdjustmentIn, CommissionSettingsIn, MonthIn

### Community 84 - "add_item"
Cohesion: 0.18
Nodes (5): add_item(), create(), issue(), pay(), return_to_draft()

### Community 85 - "events.py"
Cohesion: 0.08
Nodes (14): channel(), EventSource, _parse(), RedisEvents, sse(), events(), EventService, _collect() (+6 more)

### Community 86 - "edit_image"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 89 - "main.py"
Cohesion: 0.05
Nodes (9): _google(), _mailer(), NoEvents, configure_logging(), JsonFormatter, observe(), _route_template(), Settings (+1 more)

### Community 91 - "UserOut"
Cohesion: 0.08
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService, UserOut

### Community 94 - "ClientOut"
Cohesion: 0.19
Nodes (5): edit_client(), register_client(), ClientIn, ClientOut, ClientPatchIn

### Community 127 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 134 - "Actor"
Cohesion: 0.14
Nodes (6): clients(), invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 135 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 136 - "reports/service.py"
Cohesion: 0.06
Nodes (14): templates(), DimensionOut, FilterIn, LabelOut, MetricOut, OrderIn, PeriodIn, PreviewPointOut (+6 more)

### Community 139 - "CommissionService"
Cohesion: 0.23
Nodes (3): rules(), CommissionRuleOut, CommissionService

### Community 143 - "PageOut"
Cohesion: 0.11
Nodes (5): index(), audit_service(), AuditService, PageOut, RoleRefOut

### Community 146 - "ItemsOut"
Cohesion: 0.18
Nodes (3): ad_units(), site_options(), ItemsOut

### Community 155 - "image_response"
Cohesion: 0.13
Nodes (3): client_image(), image_response(), image_upload()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1306 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **71 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `roles/controller.py`, `.__init__`, `sites/controller.py`, `reports/service.py`, `.__init__`, `CommissionService`, `.trusted_uow`, `GroupService`, `networks/controller.py`, `PageOut`, `api_keys/controller.py`, `pydantic`, `custom_metrics/controller.py`, `.__init__`, `costs/controller.py`, `GoalService`, `.__init__`, `.__init__`, `mfa/controller.py`, `ReportService`, `ClientService`, `invoices/controller.py`, `CompanyService`, `InvoiceService`, `networks/service.py`, `AuthService`, `modules/results/controller.py`, `currencies/controller.py`, `members/controller.py`, `.__init__`, `company/controller.py`, `account/controller.py`, `mcm/controller.py`, `Limiter`, `TaskQueue`, `people/controller.py`, `commissions/dto.py`, `GoogleService`, `.uow`, `modules/results/service.py`, `UserOut`, `SiteService`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 83 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 83 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.13107822410147993 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `results`, `contracts/controller.py`, `PersonOut`, `roles/controller.py`, `clients/controller.py`, `Actor`, `Actor`, `sites/controller.py`, `reports/service.py`, `.trusted_uow`, `GroupService`, `networks/controller.py`, `api_keys/controller.py`, `pydantic`, `costs/controller.py`, `GoalService`, `NetworkDetailOut`, `get`, `ClientService`, `invoices/controller.py`, `InvoiceService`, `networks/service.py`, `Services`, `UnitOfWorkFactory`, `members/controller.py`, `UUID`, `Actor`, `mcm/controller.py`, `people/controller.py`, `.uow`, `.page_saved`, `SiteService`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 42 inferred relationships involving `PageOut` (e.g. with `index()` and `ApiKeyService`) actually correct?**
  _`PageOut` has 42 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05707450444292549 - nodes in this community are weakly interconnected._