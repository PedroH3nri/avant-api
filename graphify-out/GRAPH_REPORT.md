# Graph Report - avant-api  (2026-10-30)

## Corpus Check
- 214 files · ~67,431 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 2801 nodes · 7504 edges · 157 communities (82 shown, 75 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1246 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `44d878ce`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/dto.py
- roles/controller.py
- sites/controller.py
- clients/controller.py
- security.py
- commissions/controller.py
- conftest.py
- steps
- _month
- Avant: models do MVP
- _member_client
- .trusted_uow
- GroupService
- networks/controller.py
- Groone Avant: contexto do projeto
- api_keys/service.py
- InvitationOut
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- goals/controller.py
- invoice_pdf.py
- NetworkService
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- get
- metrics
- .uow
- session-start.sh
- avant-api
- clients/service.py
- test_api_keys.py
- invoices/controller.py
- export.py
- test_account.py
- company/controller.py
- ContractClientRefOut
- install
- _onboard_owner
- InvoiceService
- CapturingMailer
- networks/service.py
- google.py
- avant_core_access_models
- Services
- BaseModel
- UnitOfWorkFactory
- .assign
- currencies/controller.py
- members/controller.py
- staff/controller.py
- router.py
- mine
- GoalTemplateIn
- account/controller.py
- CommissionService
- mine
- goals/service.py
- ItemsOut
- mcm/controller.py
- test_networks.py
- test_mfa.py
- ReportService
- limits.py
- auth/controller.py
- test_costs_results.py
- google/controller.py
- avant-api
- TaskQueue
- uuid
- people/controller.py
- team
- commissions/dto.py
- ContractOut
- dollars
- GoogleService
- contracts/controller.py
- api_keys/controller.py
- events.py
- AdUnitOut
- Avant: grupos na Empresa e imagem da Empresa
- google_status
- UserOut
- ContractService
- ClientOut
- .page_saved
- source_files
- update_item
- Actor
- SiteService
- image
- templates
- GoogleFailed
- clients/dependencies.py
- ClientService
- GoogleAuth
- .owner_invitations
- Avant: conexão com o GAM
- reports/service.py
- GoalService
- team
- CommissionRuleOut
- avant-api
- PageOut
- person
- .create
- ProfileService
- google/dto.py
- client_image

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 108 edges
2. `PageOut` - 105 edges
3. `_onboard_owner()` - 96 edges
4. `_csrf()` - 95 edges
5. `Services` - 91 edges
6. `get()` - 90 edges
7. `UnitOfWorkFactory` - 88 edges
8. `InvoiceService` - 58 edges
9. `ClientService` - 54 edges
10. `ReportService` - 51 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/modules/company/controller.py
- `Imagem da Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/08-grupos-e-imagem-da-empresa.md → src/avant_api/modules/company/controller.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/modules/internal/people/controller.py

## Import Cycles
- None detected.

## Communities (157 total, 75 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.12
Nodes (24): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+16 more)

### Community 1 - "contracts/dto.py"
Cohesion: 0.15
Nodes (5): _contract_fields(), ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut, _network_ref()

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "sites/controller.py"
Cohesion: 0.18
Nodes (8): create(), site_service(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut

### Community 4 - "clients/controller.py"
Cohesion: 0.10
Nodes (18): audit(), cancel_owner(), change_status(), client_options(), edit_client_image(), invite_owner(), new_owner(), owner_invitations() (+10 more)

### Community 5 - "security.py"
Cohesion: 0.07
Nodes (15): CsrfFailed, NoActiveCompany, RateLimited, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth() (+7 more)

### Community 6 - "commissions/controller.py"
Cohesion: 0.16
Nodes (6): adjust(), create_rule(), delete_rule(), rules(), update_rule(), CommissionRuleIn

### Community 7 - "conftest.py"
Cohesion: 0.12
Nodes (10): client(), engine(), mailer(), _collect(), _event(), ListEvents, test_events_route(), test_redis_source_delivers_published_messages() (+2 more)

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

### Community 12 - ".trusted_uow"
Cohesion: 0.13
Nodes (4): add_item(), create(), issue(), InvoiceOut

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "networks/controller.py"
Cohesion: 0.16
Nodes (7): disconnect(), options(), service_account(), show(), sync(), sync_runs(), network_service()

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/service.py"
Cohesion: 0.18
Nodes (4): ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.09
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

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
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.18
Nodes (5): delete_template(), role_goals(), set_role_goal(), update_template(), RoleGoalIn

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "NetworkService"
Cohesion: 0.17
Nodes (5): connect(), index(), NetworkDetailOut, NetworkIn, NetworkService

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "test_reports.py"
Cohesion: 0.23
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.05
Nodes (14): auth_service(), confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn (+6 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "get"
Cohesion: 0.10
Nodes (11): available_months(), delete(), delete_service(), get(), mine(), pay(), payment_details(), pdf() (+3 more)

### Community 36 - "clients/service.py"
Cohesion: 0.11
Nodes (8): client_teams(), ClientMemberOut, options(), staff(), AuditOut, CompanyRefOut, MemberOut, RoleRefOut

### Community 37 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 38 - "invoices/controller.py"
Cohesion: 0.18
Nodes (10): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn (+2 more)

### Community 39 - "export.py"
Cohesion: 0.08
Nodes (11): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+3 more)

### Community 40 - "test_account.py"
Cohesion: 0.32
Nodes (8): _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_id_token_claims(), test_login_attempts_are_limited()

### Community 41 - "company/controller.py"
Cohesion: 0.07
Nodes (14): edit(), edit_fiscal(), edit_image(), fiscal(), image(), remove_image(), show(), company_service() (+6 more)

### Community 42 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "_onboard_owner"
Cohesion: 0.20
Nodes (10): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format(), _template() (+2 more)

### Community 45 - "InvoiceService"
Cohesion: 0.17
Nodes (6): create_service(), services(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 46 - "CapturingMailer"
Cohesion: 0.30
Nodes (10): CapturingMailer, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_option_lists_keep_the_permissions() (+2 more)

### Community 48 - "google.py"
Cohesion: 0.17
Nodes (3): challenge(), _claims(), identity_from_id_token()

### Community 49 - "avant_core_access_models"
Cohesion: 0.10
Nodes (5): show(), result_service(), ResultsOut, default_period(), ResultService

### Community 50 - "Services"
Cohesion: 0.04
Nodes (18): _google(), _mailer(), Services, NoEvents, GoogleOAuth, PillowImageProcessor, get_services(), Settings (+10 more)

### Community 51 - "BaseModel"
Cohesion: 0.10
Nodes (9): query(), FilterIn, OrderIn, PeriodIn, ReportQueryIn, ReportRangeOut, ReportResultOut, ReportRowOut (+1 more)

### Community 53 - ".assign"
Cohesion: 0.12
Nodes (16): API first e chaves de API, Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa (+8 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+6 more)

### Community 56 - "staff/controller.py"
Cohesion: 0.15
Nodes (4): invite(), staff_service(), StaffInviteIn, StaffService

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "CommissionService"
Cohesion: 0.18
Nodes (3): set_settings(), commission_service(), CommissionService

### Community 62 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 64 - "ItemsOut"
Cohesion: 0.14
Nodes (8): ad_units(), assign_sites(), delete(), index(), show(), site_options(), sites_of_member(), ItemsOut

### Community 65 - "mcm/controller.py"
Cohesion: 0.11
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "test_networks.py"
Cohesion: 0.26
Nodes (8): Sent, _owner_invite(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 67 - "test_mfa.py"
Cohesion: 0.20
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 68 - "ReportService"
Cohesion: 0.09
Nodes (12): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), run(), show() (+4 more)

### Community 69 - "limits.py"
Cohesion: 0.04
Nodes (16): TooManyAttempts, BucketResult, BucketRule, Counter, Limiter, MemoryBucket, MemoryCounter, RedisBucket (+8 more)

### Community 70 - "auth/controller.py"
Cohesion: 0.05
Nodes (17): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), get_invitation(), login(), me() (+9 more)

### Community 71 - "test_costs_results.py"
Cohesion: 0.11
Nodes (8): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query(), _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 72 - "google/controller.py"
Cohesion: 0.08
Nodes (7): new_verifier(), google_callback(), google_start(), google_redirects(), GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 75 - "uuid"
Cohesion: 0.26
Nodes (14): test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+6 more)

### Community 76 - "people/controller.py"
Cohesion: 0.10
Nodes (9): Modelo de dados, disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService (+1 more)

### Community 77 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 78 - "commissions/dto.py"
Cohesion: 0.17
Nodes (5): AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn

### Community 83 - "contracts/controller.py"
Cohesion: 0.18
Nodes (5): contract(), contracts(), edit_contract(), finish_contract(), remove_contract()

### Community 84 - "api_keys/controller.py"
Cohesion: 0.16
Nodes (4): create(), index(), revoke(), api_key_service()

### Community 85 - "events.py"
Cohesion: 0.05
Nodes (13): channel(), EventSource, _parse(), RedisEvents, sse(), configure_logging(), JsonFormatter, observe() (+5 more)

### Community 86 - "AdUnitOut"
Cohesion: 0.17
Nodes (3): link(), unlinked(), AdUnitOut

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.20
Nodes (9): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Imagem da Empresa, Issues, Modelo de dados, Regras, Resumo (+1 more)

### Community 91 - "UserOut"
Cohesion: 0.17
Nodes (3): edit_image(), remove_image(), UserOut

### Community 92 - "ContractService"
Cohesion: 0.21
Nodes (4): contract_networks(), contract_service(), ContractNetworkOut, ContractService

### Community 94 - "ClientOut"
Cohesion: 0.23
Nodes (3): edit_client(), ClientOut, ClientPatchIn

### Community 127 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 132 - "ClientService"
Cohesion: 0.11
Nodes (5): client(), manager_change(), ClientDetailOut, ManagerChangeOut, ClientService

### Community 135 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 136 - "reports/service.py"
Cohesion: 0.06
Nodes (9): QueryTooHeavy, Bucket, catalog(), CustomCatalogMetricOut, DimensionOut, LabelOut, MetricCatalogOut, MetricOut (+1 more)

### Community 137 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 142 - "avant-api"
Cohesion: 0.33
Nodes (5): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem

### Community 143 - "PageOut"
Cohesion: 0.06
Nodes (9): require(), index(), audit_service(), AuditService, results(), client_result_service(), ClientResultService, page_out() (+1 more)

### Community 153 - "ProfileService"
Cohesion: 0.23
Nodes (4): edit_appearance(), AppearanceIn, AppearanceOut, ProfileService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1293 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **75 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/dto.py`, `roles/controller.py`, `clients/dependencies.py`, `ClientService`, `GoogleAuth`, `sites/controller.py`, `reports/service.py`, `GoalService`, `.trusted_uow`, `GroupService`, `PageOut`, `api_keys/service.py`, `InvitationOut`, `custom_metrics/controller.py`, `.__init__`, `costs/controller.py`, `NetworkService`, `ProfileService`, `mfa/controller.py`, `.uow`, `clients/service.py`, `invoices/controller.py`, `company/controller.py`, `InvoiceService`, `networks/service.py`, `avant_core_access_models`, `currencies/controller.py`, `members/controller.py`, `staff/controller.py`, `account/controller.py`, `CommissionService`, `goals/service.py`, `mcm/controller.py`, `ReportService`, `limits.py`, `auth/controller.py`, `TaskQueue`, `people/controller.py`, `commissions/dto.py`, `GoogleService`, `ContractService`, `SiteService`?**
  _High betweenness centrality (0.122) - this node is a cross-community bridge._
- **Are the 81 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 81 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.12395929694727105 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `contracts/dto.py`, `roles/controller.py`, `sites/controller.py`, `clients/controller.py`, `ClientService`, `.owner_invitations`, `reports/service.py`, `GoalService`, `team`, `GroupService`, `networks/controller.py`, `api_keys/service.py`, `.page`, `InvitationOut`, `costs/controller.py`, `goals/controller.py`, `NetworkService`, `get`, `clients/service.py`, `invoices/controller.py`, `InvoiceService`, `networks/service.py`, `avant_core_access_models`, `UnitOfWorkFactory`, `members/controller.py`, `staff/controller.py`, `router.py`, `goals/service.py`, `ItemsOut`, `mcm/controller.py`, `people/controller.py`, `ContractOut`, `Actor`, `contracts/controller.py`, `api_keys/controller.py`, `AdUnitOut`, `ContractService`, `.page_saved`, `SiteService`?**
  _High betweenness centrality (0.093) - this node is a cross-community bridge._
- **Are the 42 inferred relationships involving `PageOut` (e.g. with `index()` and `ApiKeyService`) actually correct?**
  _`PageOut` has 42 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/dto.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14619883040935672 - nodes in this community are weakly interconnected._