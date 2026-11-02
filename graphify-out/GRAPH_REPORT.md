# Graph Report - avant-api  (2026-11-02)

## Corpus Check
- 226 files · ~72,887 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3062 nodes · 8331 edges · 174 communities (93 shown, 81 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1408 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `18176c00`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- DashboardService
- AlertService
- security.py
- .save_rule
- conftest.py
- steps
- _month
- Avant: models do MVP
- test_company_image.py
- .trusted_uow
- GroupService
- NetworkService
- Groone Avant: contexto do projeto
- api_keys/controller.py
- pydantic
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- GoalTemplateOut
- invoice_pdf.py
- UnitOfWorkFactory
- clean_code.py
- CapturingMailer
- mfa/controller.py
- Avant: repositório e plano do MVP
- UUID
- clients/controller.py
- .uow
- session-start.sh
- avant-api
- ClientService
- _member_client
- invoices/controller.py
- export.py
- staff/controller.py
- CompanyService
- main.py
- errors.py
- limits.py
- InvoiceService
- CapturingMailer
- ContractClientRefOut
- datetime
- google/dependencies.py
- ReportResultOut
- require
- edit
- currencies/controller.py
- members/controller.py
- test_mfa.py
- health/controller.py
- person
- company/controller.py
- account/controller.py
- CommissionService
- google/controller.py
- clients/controller.py
- ItemsOut
- mcm/controller.py
- CapturingMailer
- sites/controller.py
- reports/controller.py
- Limiter
- auth/controller.py
- sqlalchemy
- google.py
- avant-api
- networks/controller.py
- uuid
- people/controller.py
- Avant: conexão com o GAM
- commissions/dto.py
- SiteOut
- GoogleService
- mine
- test_dashboards.py
- get
- events.py
- .update_fiscal
- Avant: grupos na Empresa e imagem da Empresa
- .assign
- verify
- profile/controller.py
- container.py
- ClientOut
- goals/controller.py
- GoalService
- update_item
- test_permissions_on_keys
- audit/controller.py
- google_status
- SiteService
- MemoryCounter
- test_alerts.py
- image
- Actor
- networks/service.py
- reports/service.py
- SiteListOut
- set_settings
- TaskQueue
- shared/dto.py
- dollars
- DashboardTemplateOut
- test_account.py
- AdUnitOut
- Actor
- clients
- GoogleOAuth
- google/controller.py
- AuditOut
- members
- GoogleAuth
- team
- delete_template
- image_url
- manager_change
- is_exempt

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 120 edges
2. `PageOut` - 114 edges
3. `_csrf()` - 107 edges
4. `_onboard_owner()` - 107 edges
5. `get()` - 98 edges
6. `Services` - 96 edges
7. `UnitOfWorkFactory` - 94 edges
8. `ReportService` - 75 edges
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

## Communities (174 total, 81 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.13
Nodes (24): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+16 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.05
Nodes (25): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+17 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.06
Nodes (18): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), set_default() (+10 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "security.py"
Cohesion: 0.06
Nodes (18): Services, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth() (+10 more)

### Community 6 - ".save_rule"
Cohesion: 0.17
Nodes (5): adjust(), create_rule(), rules(), update_rule(), CommissionRuleOut

### Community 7 - "conftest.py"
Cohesion: 0.13
Nodes (10): client(), engine(), mailer(), _collect(), _event(), ListEvents, test_events_route(), test_redis_source_delivers_published_messages() (+2 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "test_company_image.py"
Cohesion: 0.16
Nodes (7): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture()

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "NetworkService"
Cohesion: 0.17
Nodes (5): connect(), index(), NetworkDetailOut, NetworkIn, NetworkService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.11
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "pydantic"
Cohesion: 0.10
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

### Community 22 - "costs/controller.py"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 23 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 27 - "CapturingMailer"
Cohesion: 0.23
Nodes (12): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "UUID"
Cohesion: 0.13
Nodes (8): add_item(), create(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft()

### Community 31 - "clients/controller.py"
Cohesion: 0.17
Nodes (12): new_owner(), register_client(), ClientDetailOut, ClientIn, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn (+4 more)

### Community 32 - ".uow"
Cohesion: 0.06
Nodes (5): RateLimited, Bucket, pinned(), SavedReportOut, ReportService

### Community 36 - "ClientService"
Cohesion: 0.20
Nodes (5): client_teams(), client_service(), ClientMemberOut, ClientService, CompanyRefOut

### Community 37 - "_member_client"
Cohesion: 0.14
Nodes (13): _membership_ids(), test_groups_lifecycle(), _inventory(), test_manual_site(), test_site_category_and_responsible(), test_sites_and_assignment(), _member_client(), test_audit_log() (+5 more)

### Community 38 - "invoices/controller.py"
Cohesion: 0.18
Nodes (12): create_service(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceServiceOut, InvoiceSummaryOut (+4 more)

### Community 39 - "export.py"
Cohesion: 0.08
Nodes (11): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+3 more)

### Community 40 - "staff/controller.py"
Cohesion: 0.13
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 41 - "CompanyService"
Cohesion: 0.21
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 42 - "main.py"
Cohesion: 0.08
Nodes (6): configure_logging(), JsonFormatter, observe(), _route_template(), Settings, create_app()

### Community 43 - "errors.py"
Cohesion: 0.16
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "limits.py"
Cohesion: 0.08
Nodes (8): BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 46 - "CapturingMailer"
Cohesion: 0.21
Nodes (16): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format(), test_costs_and_reports_come_in_pages() (+8 more)

### Community 47 - "ContractClientRefOut"
Cohesion: 0.09
Nodes (4): show(), CostLineOut, MonthResultOut, ResultTotalsOut

### Community 49 - "datetime"
Cohesion: 0.11
Nodes (5): results(), client_result_service(), ClientResultService, ResultsOut, default_period()

### Community 50 - "google/dependencies.py"
Cohesion: 0.15
Nodes (3): google_redirects(), google_service(), GoogleRedirects

### Community 51 - "ReportResultOut"
Cohesion: 0.12
Nodes (4): run(), query(), ReportQueryIn, ReportResultOut

### Community 52 - "require"
Cohesion: 0.13
Nodes (6): require(), dependency(), require_session(), require_staff(), result_service(), ResultService

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "test_mfa.py"
Cohesion: 0.15
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 57 - "health/controller.py"
Cohesion: 0.15
Nodes (4): health(), ready(), health_service(), HealthService

### Community 58 - "person"
Cohesion: 0.18
Nodes (3): mine(), _month(), person()

### Community 59 - "company/controller.py"
Cohesion: 0.23
Nodes (4): company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 60 - "account/controller.py"
Cohesion: 0.10
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "CommissionService"
Cohesion: 0.16
Nodes (3): delete_rule(), settings(), CommissionService

### Community 62 - "google/controller.py"
Cohesion: 0.16
Nodes (3): new_verifier(), google_start(), GoogleStatusOut

### Community 63 - "clients/controller.py"
Cohesion: 0.13
Nodes (8): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), edit_client_image(), remove_client_image()

### Community 64 - "ItemsOut"
Cohesion: 0.14
Nodes (7): ad_units(), assign_sites(), delete(), index(), site_options(), unlinked(), ItemsOut

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "CapturingMailer"
Cohesion: 0.19
Nodes (9): CapturingMailer, Sent, _owner_invite(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company() (+1 more)

### Community 67 - "sites/controller.py"
Cohesion: 0.19
Nodes (6): site_service(), AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 68 - "reports/controller.py"
Cohesion: 0.07
Nodes (15): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+7 more)

### Community 69 - "Limiter"
Cohesion: 0.09
Nodes (7): TooManyAttempts, Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "auth/controller.py"
Cohesion: 0.09
Nodes (18): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), get_invitation(), login(), me() (+10 more)

### Community 71 - "sqlalchemy"
Cohesion: 0.11
Nodes (8): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query(), test_invoice_lifecycle(), test_who_sees_and_changes_invoices(), _validated_month()

### Community 72 - "google.py"
Cohesion: 0.13
Nodes (6): GoogleFailed, _claims(), identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 74 - "networks/controller.py"
Cohesion: 0.15
Nodes (7): disconnect(), options(), service_account(), show(), sync(), sync_runs(), network_service()

### Community 75 - "uuid"
Cohesion: 0.26
Nodes (15): test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+7 more)

### Community 76 - "people/controller.py"
Cohesion: 0.11
Nodes (10): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+2 more)

### Community 77 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 78 - "commissions/dto.py"
Cohesion: 0.30
Nodes (8): AdjustmentIn, CommissionMonthOut, CommissionRuleIn, CommissionSettingsIn, CommissionSettingsOut, MonthIn, MyCommissionsOut, WindowMonthOut

### Community 79 - "SiteOut"
Cohesion: 0.16
Nodes (4): classify(), classify_many(), sites_of_member(), SiteOut

### Community 81 - "GoogleService"
Cohesion: 0.15
Nodes (3): GoogleUnavailable, google_callback(), GoogleService

### Community 82 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 83 - "test_dashboards.py"
Cohesion: 0.32
Nodes (6): _form(), _kpi(), _run(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit()

### Community 84 - "get"
Cohesion: 0.17
Nodes (7): available_months(), get(), mine(), payment_details(), pdf(), service_options(), services()

### Community 85 - "events.py"
Cohesion: 0.10
Nodes (7): channel(), EventSource, _parse(), sse(), events(), event_service(), EventService

### Community 86 - ".update_fiscal"
Cohesion: 0.12
Nodes (3): edit_fiscal(), edit_image(), fiscal()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - ".assign"
Cohesion: 0.17
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 91 - "profile/controller.py"
Cohesion: 0.07
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 92 - "container.py"
Cohesion: 0.05
Nodes (10): _google(), _mailer(), NoEvents, RedisEvents, PillowImageProcessor, CeleryQueue, RecordingQueue, run() (+2 more)

### Community 95 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 96 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 97 - "update_item"
Cohesion: 0.14
Nodes (3): save_payment_details(), update_item(), update_service()

### Community 98 - "test_permissions_on_keys"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 127 - "audit/controller.py"
Cohesion: 0.23
Nodes (3): index(), audit_service(), AuditService

### Community 129 - "SiteService"
Cohesion: 0.23
Nodes (3): show(), SiteDetailOut, SiteService

### Community 131 - "test_alerts.py"
Cohesion: 0.35
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 134 - "Actor"
Cohesion: 0.17
Nodes (5): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 136 - "reports/service.py"
Cohesion: 0.05
Nodes (17): QueryTooHeavy, catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn (+9 more)

### Community 145 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 146 - "test_account.py"
Cohesion: 0.40
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 155 - "google/controller.py"
Cohesion: 0.18
Nodes (3): client_info(), image_response(), image_upload()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1407 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **81 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `SiteService`, `networks/service.py`, `reports/service.py`, `.__init__`, `.trusted_uow`, `GroupService`, `TaskQueue`, `shared/dto.py`, `api_keys/controller.py`, `pydantic`, `NetworkService`, `custom_metrics/controller.py`, `.__init__`, `costs/controller.py`, `mfa/controller.py`, `clients/controller.py`, `.uow`, `GoogleAuth`, `goals/service.py`, `ClientService`, `invoices/controller.py`, `staff/controller.py`, `CompanyService`, `errors.py`, `InvoiceService`, `datetime`, `require`, `currencies/controller.py`, `members/controller.py`, `company/controller.py`, `account/controller.py`, `CommissionService`, `mcm/controller.py`, `sites/controller.py`, `Limiter`, `auth/controller.py`, `people/controller.py`, `commissions/dto.py`, `GoogleService`, `profile/controller.py`, `GoalService`, `audit/controller.py`?**
  _High betweenness centrality (0.122) - this node is a cross-community bridge._
- **Are the 90 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 90 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.13107822410147993 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `people/controller.py` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `Actor`, `Actor`, `networks/service.py`, `reports/service.py`, `SiteService`, `GroupService`, `NetworkService`, `shared/dto.py`, `api_keys/controller.py`, `pydantic`, `costs/controller.py`, `GoalTemplateOut`, `clients`, `AuditOut`, `goals/service.py`, `clients/controller.py`, `team`, `ClientService`, `invoices/controller.py`, `staff/controller.py`, `InvoiceService`, `datetime`, `members/controller.py`, `clients/controller.py`, `ItemsOut`, `mcm/controller.py`, `sites/controller.py`, `reports/controller.py`, `networks/controller.py`, `get`, `.assign`, `goals/controller.py`, `GoalService`, `audit/controller.py`?**
  _High betweenness centrality (0.080) - this node is a cross-community bridge._
- **Are the 46 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 46 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05230678812812224 - nodes in this community are weakly interconnected._