# Graph Report - avant-api  (2026-10-29)

## Corpus Check
- 207 files · ~62,531 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2629 nodes · 6852 edges · 152 communities (79 shown, 73 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1128 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `242d2dbc`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- avant_core_shared_clock
- contracts/controller.py
- roles/controller.py
- SiteService
- Actor
- security.py
- commissions/controller.py
- conftest.py
- steps
- _month
- Avant: models do MVP
- _member_client
- .uow
- MemberOut
- Groone Avant: contexto do projeto
- api_keys/controller.py
- modules/results/controller.py
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- goals/controller.py
- networks/controller.py
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- .build
- health/controller.py
- .uow
- session-start.sh
- avant-api
- NetworkService
- test_api_keys.py
- events/controller.py
- export.py
- test_account.py
- company/controller.py
- test_costs_results.py
- install
- test_goals.py
- invitations/controller.py
- CapturingMailer
- limits.py
- google.py
- ResultsOut
- Services
- CompanyService
- edit
- currencies/controller.py
- ports.py
- google_status
- results/dto.py
- networks/service.py
- GoalTemplateOut
- AccountService
- CommissionService
- mine
- goals/service.py
- PeopleService
- mcm/controller.py
- _onboard_owner
- google_start
- reports/controller.py
- Limiter
- .uow
- SessionCookies
- avant-api
- TaskQueue
- uuid
- PageOut
- team
- commissions/dto.py
- test_report_export.py
- issue
- GoogleService
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- edit_fiscal
- main.py
- templates
- auth/controller.py
- google/controller.py
- profile/controller.py
- datetime
- do_reset_password
- reports/service.py
- source_files
- UnitOfWorkFactory
- Actor
- .page_saved
- image
- avant_core_access_models
- RoleGoalOut
- CommissionRuleOut
- .trusted_uow
- image_response
- GoalService
- Avant: conexão com o GAM
- reports/service.py
- Actor
- results
- FakeGoogle
- audit/controller.py
- person
- fiscal
- google_callback

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 101 edges
2. `PageOut` - 96 edges
3. `_onboard_owner()` - 93 edges
4. `Services` - 89 edges
5. `UnitOfWorkFactory` - 85 edges
6. `_csrf()` - 82 edges
7. `ClientService` - 51 edges
8. `ReportService` - 51 edges
9. `page_out()` - 41 edges
10. `CommissionService` - 38 edges

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

## Communities (152 total, 73 thin omitted)

### Community 0 - "avant_core_shared_clock"
Cohesion: 0.11
Nodes (17): _admin_role(), test_rules_on_the_role(), test_start_my_commission_team_discount_and_issue(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _staff(), test_client_owner_cannot_reach_internal() (+9 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (24): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, contract(), contract_networks() (+16 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "SiteService"
Cohesion: 0.05
Nodes (25): Atribuição de sites, GAM, Networks, Sites e ad units, ad_units(), assign_sites(), create(), delete() (+17 more)

### Community 4 - "Actor"
Cohesion: 0.07
Nodes (26): Modelo de dados, audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), clients() (+18 more)

### Community 5 - "security.py"
Cohesion: 0.07
Nodes (16): CsrfFailed, NoActiveCompany, bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor(), get_session_auth() (+8 more)

### Community 6 - "commissions/controller.py"
Cohesion: 0.18
Nodes (4): create_rule(), delete_rule(), update_rule(), CommissionRuleIn

### Community 7 - "conftest.py"
Cohesion: 0.13
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
Cohesion: 0.14
Nodes (12): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _member_client(), test_audit_log(), test_company_and_members() (+4 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "MemberOut"
Cohesion: 0.14
Nodes (5): invite(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (11): check(), create(), delete(), index(), update(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn (+3 more)

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
Cohesion: 0.17
Nodes (6): delete_template(), role_goals(), set_role_goal(), template_options(), templates(), update_template()

### Community 25 - "networks/controller.py"
Cohesion: 0.16
Nodes (8): disconnect(), index(), options(), service_account(), show(), sync(), sync_runs(), network_service()

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "test_reports.py"
Cohesion: 0.23
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (10): get_cookies(), confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - ".build"
Cohesion: 0.08
Nodes (7): _google(), _mailer(), NoEvents, RedisEvents, MemoryCounter, CeleryQueue, run()

### Community 31 - "health/controller.py"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 32 - ".uow"
Cohesion: 0.09
Nodes (4): create(), SavedReportIn, SavedReportOut, ReportService

### Community 36 - "NetworkService"
Cohesion: 0.19
Nodes (3): connect(), NetworkDetailOut, NetworkService

### Community 37 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 38 - "events/controller.py"
Cohesion: 0.09
Nodes (7): channel(), EventSource, _parse(), sse(), events(), event_service(), EventService

### Community 39 - "export.py"
Cohesion: 0.09
Nodes (9): JsonFormatter, dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx() (+1 more)

### Community 40 - "test_account.py"
Cohesion: 0.35
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 41 - "company/controller.py"
Cohesion: 0.22
Nodes (5): company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, FiscalDataOut

### Community 42 - "test_costs_results.py"
Cohesion: 0.12
Nodes (8): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query(), _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "test_goals.py"
Cohesion: 0.43
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 45 - "invitations/controller.py"
Cohesion: 0.12
Nodes (6): cancel(), create_invitation(), list_invitations(), resend(), InvitationService, InvitationOut

### Community 46 - "CapturingMailer"
Cohesion: 0.21
Nodes (16): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format(), test_costs_and_reports_come_in_pages() (+8 more)

### Community 47 - "limits.py"
Cohesion: 0.08
Nodes (8): BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 48 - "google.py"
Cohesion: 0.12
Nodes (7): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 50 - "Services"
Cohesion: 0.05
Nodes (13): Services, api_key_actor(), get_services(), RecordingQueue, account_service(), auth_service(), custom_metric_service(), commission_service() (+5 more)

### Community 52 - "CompanyService"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 57 - "results/dto.py"
Cohesion: 0.19
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 58 - "networks/service.py"
Cohesion: 0.18
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 59 - "GoalTemplateOut"
Cohesion: 0.16
Nodes (3): create_template(), GoalTemplateIn, GoalTemplateOut

### Community 60 - "AccountService"
Cohesion: 0.11
Nodes (9): do_change_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut, SessionOut (+1 more)

### Community 61 - "CommissionService"
Cohesion: 0.26
Nodes (3): adjust(), AdjustmentIn, CommissionService

### Community 62 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 64 - "PeopleService"
Cohesion: 0.13
Nodes (6): Resumo, disable(), enable(), reset_mfa(), users(), PeopleService

### Community 65 - "mcm/controller.py"
Cohesion: 0.12
Nodes (6): assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "_onboard_owner"
Cohesion: 0.22
Nodes (9): CapturingMailer, Sent, _owner_invite(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company() (+1 more)

### Community 68 - "reports/controller.py"
Cohesion: 0.11
Nodes (12): catalog(), create_from_template(), delete(), duplicate(), export(), export_saved(), query(), run() (+4 more)

### Community 69 - "Limiter"
Cohesion: 0.10
Nodes (7): TooManyAttempts, Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - ".uow"
Cohesion: 0.06
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 72 - "SessionCookies"
Cohesion: 0.09
Nodes (3): SessionCookies, delete_session(), verify()

### Community 75 - "uuid"
Cohesion: 0.29
Nodes (15): _csrf(), test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused() (+7 more)

### Community 76 - "PageOut"
Cohesion: 0.08
Nodes (7): index(), client_teams(), ClientMemberOut, AuditOut, page_out(), PageOut, RoleRefOut

### Community 77 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 79 - "test_report_export.py"
Cohesion: 0.22
Nodes (3): _result(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 80 - "issue"
Cohesion: 0.24
Nodes (4): issue(), CommissionSettingsIn, IssuedOut, MonthIn

### Community 81 - "GoogleService"
Cohesion: 0.14
Nodes (3): GoogleUnavailable, GoogleAuth, GoogleService

### Community 82 - "test_company_image.py"
Cohesion: 0.31
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 85 - "main.py"
Cohesion: 0.12
Nodes (4): configure_logging(), observe(), _route_template(), create_app()

### Community 88 - "auth/controller.py"
Cohesion: 0.11
Nodes (15): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), AcceptInvitationIn (+7 more)

### Community 89 - "google/controller.py"
Cohesion: 0.06
Nodes (8): PillowImageProcessor, Settings, google_redirects(), google_service(), GoogleStatusOut, GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 91 - "profile/controller.py"
Cohesion: 0.07
Nodes (11): PersonOut, person_out(), edit_appearance(), edit_image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService (+3 more)

### Community 94 - "do_reset_password"
Cohesion: 0.24
Nodes (3): do_reset_password(), forgot_password(), client_info()

### Community 95 - "reports/service.py"
Cohesion: 0.13
Nodes (4): QueryTooHeavy, RateLimited, Bucket, _statement_timeout()

### Community 98 - "Actor"
Cohesion: 0.24
Nodes (3): set_settings(), settings(), CommissionSettingsOut

### Community 132 - ".trusted_uow"
Cohesion: 0.10
Nodes (3): client_service(), ClientService, owner_invitation_out()

### Community 133 - "image_response"
Cohesion: 0.13
Nodes (3): image(), image_response(), image_upload()

### Community 135 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 136 - "reports/service.py"
Cohesion: 0.06
Nodes (12): CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+4 more)

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1224 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **73 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `avant_core_access_models`, `roles/controller.py`, `.trusted_uow`, `Actor`, `GoalService`, `SiteService`, `.uow`, `MemberOut`, `audit/controller.py`, `api_keys/controller.py`, `modules/results/controller.py`, `custom_metrics/controller.py`, `.__init__`, `costs/controller.py`, `mfa/controller.py`, `.uow`, `NetworkService`, `company/controller.py`, `invitations/controller.py`, `CompanyService`, `currencies/controller.py`, `ports.py`, `networks/service.py`, `AccountService`, `CommissionService`, `goals/service.py`, `PeopleService`, `mcm/controller.py`, `Limiter`, `.uow`, `TaskQueue`, `PageOut`, `GoogleService`, `auth/controller.py`, `profile/controller.py`, `datetime`, `reports/service.py`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **Are the 75 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 75 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `avant_core_shared_clock` be split into smaller, more focused modules?**
  _Cohesion score 0.1141025641025641 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `contracts/controller.py`, `avant_core_access_models`, `roles/controller.py`, `Actor`, `.trusted_uow`, `GoalService`, `SiteService`, `reports/service.py`, `results`, `.uow`, `MemberOut`, `audit/controller.py`, `api_keys/controller.py`, `costs/controller.py`, `goals/controller.py`, `networks/controller.py`, `NetworkService`, `invitations/controller.py`, `ports.py`, `networks/service.py`, `GoalTemplateOut`, `goals/service.py`, `PeopleService`, `mcm/controller.py`, `.uow`, `profile/controller.py`, `datetime`, `.page_saved`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._
- **Are the 38 inferred relationships involving `PageOut` (e.g. with `index()` and `ApiKeyService`) actually correct?**
  _`PageOut` has 38 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.056150600454397924 - nodes in this community are weakly interconnected._