# Graph Report - avant-api  (2026-10-30)

## Corpus Check
- 207 files · ~63,749 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2655 nodes · 6959 edges · 151 communities (82 shown, 69 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1143 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1a40dac6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- .uow
- Actor
- security.py
- commissions/controller.py
- test_events.py
- steps
- _month
- Avant: models do MVP
- _member_client
- CapturingMailer
- .uow
- networks/controller.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- InvitationOut
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- goals/controller.py
- verify
- NetworkService
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- limits.py
- health/controller.py
- .uow
- session-start.sh
- avant-api
- PageOut
- test_api_keys.py
- events/controller.py
- export.py
- test_account.py
- company/controller.py
- ContractClientRefOut
- errors.py
- conftest.py
- edit_fiscal
- _onboard_owner
- networks/service.py
- google.py
- datetime
- Services
- ReportQueryIn
- shared/dto.py
- edit
- currencies/controller.py
- members/controller.py
- results
- clients
- mine
- GoalTemplateOut
- account/controller.py
- CommissionService
- mine
- goals/service.py
- ResultService
- mcm/controller.py
- test_networks.py
- set_active_company
- reports/controller.py
- Limiter
- AuthService
- _marketing_client
- google/controller.py
- avant-api
- uuid
- people/controller.py
- team
- commissions/dto.py
- image
- commissions/controller.py
- GoogleService
- test_company_image.py
- images.py
- http.py
- main.py
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- Settings
- profile/controller.py
- test_goal_progress_routes
- .preview_invitation
- .page_saved
- source_files
- Actor
- MemoryCounter
- RoleGoalOut
- .trusted_uow
- CompanyDetailOut
- fiscal
- Avant: conexão com o GAM
- reports/service.py
- GoalService
- test_groups_lifecycle
- audit/service.py
- person
- NoEvents
- .to_data
- CompanyService
- .build

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 105 edges
2. `PageOut` - 96 edges
3. `_onboard_owner()` - 94 edges
4. `_csrf()` - 91 edges
5. `Services` - 89 edges
6. `UnitOfWorkFactory` - 85 edges
7. `ClientService` - 54 edges
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

## Communities (151 total, 69 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.12
Nodes (23): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+15 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (23): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem, contract(), contract_networks(), contracts() (+15 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.05
Nodes (26): Atribuição de sites, GAM, Networks, Sites e ad units, ad_units(), assign_sites(), create(), delete() (+18 more)

### Community 4 - "Actor"
Cohesion: 0.09
Nodes (17): audit(), cancel_owner(), change_status(), client_image(), client_options(), edit_client_image(), invite_owner(), manager_change() (+9 more)

### Community 5 - "security.py"
Cohesion: 0.11
Nodes (13): api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor(), get_session_auth(), optional_auth() (+5 more)

### Community 6 - "commissions/controller.py"
Cohesion: 0.16
Nodes (5): create_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 7 - "test_events.py"
Cohesion: 0.09
Nodes (14): channel(), _parse(), RedisEvents, sse(), _collect(), _event(), ListEvents, test_events_route() (+6 more)

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
Cohesion: 0.15
Nodes (13): _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_sites_and_assignment(), _member_client(), test_audit_log() (+5 more)

### Community 12 - "CapturingMailer"
Cohesion: 0.23
Nodes (7): CapturingMailer, Sent, test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_internal_clients(), test_internal_people_and_staff()

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "networks/controller.py"
Cohesion: 0.16
Nodes (8): disconnect(), index(), options(), service_account(), show(), sync(), sync_runs(), network_service()

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.05
Nodes (14): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, cancel(), create_invitation() (+6 more)

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

### Community 25 - "NetworkService"
Cohesion: 0.17
Nodes (3): connect(), NetworkDetailOut, NetworkService

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "test_reports.py"
Cohesion: 0.23
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "limits.py"
Cohesion: 0.09
Nodes (8): BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 31 - "health/controller.py"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 32 - ".uow"
Cohesion: 0.08
Nodes (5): RateLimited, Bucket, SavedReportOut, ReportService, _statement_timeout()

### Community 36 - "PageOut"
Cohesion: 0.09
Nodes (7): client_teams(), owner_invitations(), ClientMemberOut, OwnerInvitationOut, owner_invitation_out(), page_out(), PageOut

### Community 37 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 38 - "events/controller.py"
Cohesion: 0.14
Nodes (4): EventSource, events(), event_service(), EventService

### Community 39 - "export.py"
Cohesion: 0.08
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 40 - "test_account.py"
Cohesion: 0.35
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 41 - "company/controller.py"
Cohesion: 0.22
Nodes (3): CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 42 - "ContractClientRefOut"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 43 - "errors.py"
Cohesion: 0.09
Nodes (13): CsrfFailed, error_body(), GoogleFailed, GoogleUnavailable, install(), domain_error(), http_error(), unexpected() (+5 more)

### Community 44 - "conftest.py"
Cohesion: 0.13
Nodes (3): client(), engine(), mailer()

### Community 45 - "edit_fiscal"
Cohesion: 0.25
Nodes (3): edit_fiscal(), edit_image(), remove_image()

### Community 46 - "_onboard_owner"
Cohesion: 0.23
Nodes (16): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format(), test_costs_and_reports_come_in_pages() (+8 more)

### Community 47 - "networks/service.py"
Cohesion: 0.14
Nodes (4): NetworkIn, ServiceAccountOut, SyncRunOut, enqueue_sync()

### Community 48 - "google.py"
Cohesion: 0.10
Nodes (7): _google(), challenge(), _claims(), GoogleOAuth, identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 49 - "datetime"
Cohesion: 0.16
Nodes (3): result_service(), ResultsOut, ResultService

### Community 50 - "Services"
Cohesion: 0.07
Nodes (9): Estrutura, Services, get_services(), CeleryQueue, RecordingQueue, TaskQueue, account_service(), audit_service() (+1 more)

### Community 51 - "ReportQueryIn"
Cohesion: 0.17
Nodes (4): query(), ReportQueryIn, ReportRangeOut, ReportResultOut

### Community 52 - "shared/dto.py"
Cohesion: 0.10
Nodes (8): ClientProfileOut, PersonOut, person_out(), CompanyRefOut, FiscalDataOut, image_url(), RoleRefOut, UserOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.10
Nodes (7): UnitOfWorkFactory, list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "results"
Cohesion: 0.12
Nodes (4): results(), client_result_service(), ClientResultService, default_period()

### Community 57 - "clients"
Cohesion: 0.25
Nodes (4): Modelo de dados, Resumo, clients(), users()

### Community 59 - "GoalTemplateOut"
Cohesion: 0.16
Nodes (3): create_template(), GoalTemplateIn, GoalTemplateOut

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (12): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn (+4 more)

### Community 61 - "CommissionService"
Cohesion: 0.17
Nodes (3): commission_service(), IssuedOut, CommissionService

### Community 62 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 65 - "mcm/controller.py"
Cohesion: 0.11
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "test_networks.py"
Cohesion: 0.40
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 67 - "set_active_company"
Cohesion: 0.16
Nodes (4): company_image(), do_logout(), me(), set_active_company()

### Community 68 - "reports/controller.py"
Cohesion: 0.08
Nodes (13): catalog(), create(), create_from_template(), delete(), duplicate(), export(), export_saved(), run() (+5 more)

### Community 69 - "Limiter"
Cohesion: 0.09
Nodes (6): Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "_marketing_client"
Cohesion: 0.19
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 72 - "google/controller.py"
Cohesion: 0.08
Nodes (8): SessionCookies, new_verifier(), get_cookies(), google_callback(), google_start(), google_status(), google_unlink(), GoogleStatusOut

### Community 75 - "uuid"
Cohesion: 0.25
Nodes (14): _owner_invite(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+6 more)

### Community 76 - "people/controller.py"
Cohesion: 0.16
Nodes (5): disable(), enable(), reset_mfa(), people_service(), PeopleService

### Community 77 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 78 - "commissions/dto.py"
Cohesion: 0.24
Nodes (3): CommissionMonthOut, CommissionSettingsIn, dollars()

### Community 80 - "commissions/controller.py"
Cohesion: 0.17
Nodes (5): adjust(), delete_rule(), issue(), AdjustmentIn, MonthIn

### Community 82 - "test_company_image.py"
Cohesion: 0.31
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 85 - "main.py"
Cohesion: 0.09
Nodes (5): configure_logging(), JsonFormatter, observe(), _route_template(), create_app()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.18
Nodes (9): login(), auth_service(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut (+1 more)

### Community 89 - "Settings"
Cohesion: 0.09
Nodes (4): Settings, google_redirects(), google_service(), GoogleRedirects

### Community 91 - "profile/controller.py"
Cohesion: 0.07
Nodes (10): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService (+2 more)

### Community 92 - "test_goal_progress_routes"
Cohesion: 0.53
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 98 - "Actor"
Cohesion: 0.21
Nodes (3): set_settings(), settings(), CommissionSettingsOut

### Community 132 - ".trusted_uow"
Cohesion: 0.09
Nodes (7): client(), edit_client(), client_service(), ClientDetailOut, ClientOut, ClientPatchIn, ClientService

### Community 135 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 136 - "reports/service.py"
Cohesion: 0.06
Nodes (12): CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+4 more)

### Community 143 - "audit/service.py"
Cohesion: 0.13
Nodes (3): index(), AuditService, AuditOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1228 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **69 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `currencies/controller.py` to `contracts/controller.py`, `.__init__`, `.uow`, `.trusted_uow`, `.__init__`, `roles/controller.py`, `reports/service.py`, `GoalService`, `.uow`, `audit/service.py`, `api_keys/controller.py`, `InvitationOut`, `custom_metrics/controller.py`, `CompanyService`, `costs/controller.py`, `NetworkService`, `.__init__`, `mfa/controller.py`, `.uow`, `PageOut`, `company/controller.py`, `errors.py`, `networks/service.py`, `datetime`, `shared/dto.py`, `members/controller.py`, `results`, `account/controller.py`, `CommissionService`, `goals/service.py`, `mcm/controller.py`, `Limiter`, `AuthService`, `people/controller.py`, `GoogleService`, `auth/controller.py`, `profile/controller.py`, `.__init__`?**
  _High betweenness centrality (0.129) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 79 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.12311265969802555 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `contracts/controller.py`, `roles/controller.py`, `.uow`, `Actor`, `.trusted_uow`, `reports/service.py`, `GoalService`, `.uow`, `networks/controller.py`, `audit/service.py`, `api_keys/controller.py`, `InvitationOut`, `costs/controller.py`, `goals/controller.py`, `NetworkService`, `networks/service.py`, `datetime`, `shared/dto.py`, `members/controller.py`, `results`, `clients`, `GoalTemplateOut`, `goals/service.py`, `mcm/controller.py`, `people/controller.py`, `.page_saved`?**
  _High betweenness centrality (0.090) - this node is a cross-community bridge._
- **Are the 38 inferred relationships involving `PageOut` (e.g. with `index()` and `ApiKeyService`) actually correct?**
  _`PageOut` has 38 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05679974034404414 - nodes in this community are weakly interconnected._