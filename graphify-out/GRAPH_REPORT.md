# Graph Report - avant-api  (2026-10-29)

## Corpus Check
- 201 files · ~60,344 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2509 nodes · 6507 edges · 149 communities (80 shown, 69 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1062 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `543b1c7b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_internal.py
- contracts/controller.py
- roles/controller.py
- .uow
- Actor
- security.py
- test_events.py
- pydantic
- steps
- UserOut
- Avant: models do MVP
- _member_client
- company/service.py
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
- ClientService
- Avant: conexão com o GAM
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- Settings
- health/controller.py
- .export_saved
- session-start.sh
- avant-api
- networks/controller.py
- conftest.py
- Services
- export.py
- test_account.py
- auth/controller.py
- test_costs_results.py
- install
- main.py
- invitations/controller.py
- CapturingMailer
- limits.py
- google.py
- .of
- sites/controller.py
- ReportService
- CompanyService
- edit
- currencies/controller.py
- account/controller.py
- .build
- ItemsOut
- set_active_company
- GoalTemplateOut
- .change_password
- test_sites.py
- mine
- goals/service.py
- PeopleService
- mcm/controller.py
- _onboard_owner
- reports/controller.py
- Limiter
- .uow
- ReportResultOut
- SessionCookies
- avant-api
- tasks.py
- uuid
- AuditService
- team
- AdUnitOut
- SiteService
- pytest
- GoogleService
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- company/controller.py
- image
- templates
- AuthService
- image_response
- profile/controller.py
- UnitOfWorkFactory
- do_reset_password
- RateLimited
- .of
- MemoryCounter
- .page_saved
- delete_session
- audit/controller.py
- RoleGoalOut
- .trusted_uow
- image
- GoalService
- reports/service.py
- FakeGoogle
- PillowImageProcessor
- is_exempt

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 98 edges
2. `PageOut` - 96 edges
3. `_onboard_owner()` - 90 edges
4. `Services` - 87 edges
5. `UnitOfWorkFactory` - 82 edges
6. `_csrf()` - 79 edges
7. `ClientService` - 51 edges
8. `ReportService` - 51 edges
9. `page_out()` - 41 edges
10. `SiteService` - 36 edges

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

## Communities (149 total, 69 thin omitted)

### Community 0 - "test_internal.py"
Cohesion: 0.11
Nodes (17): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal(), _staff(), test_client_owner_cannot_reach_internal() (+9 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (23): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem, contract(), contract_networks(), contracts() (+15 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - ".uow"
Cohesion: 0.11
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 4 - "Actor"
Cohesion: 0.08
Nodes (13): audit(), cancel_owner(), change_status(), client_image(), client_options(), client_teams(), clients(), edit_client_image() (+5 more)

### Community 5 - "security.py"
Cohesion: 0.10
Nodes (15): CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor() (+7 more)

### Community 6 - "test_events.py"
Cohesion: 0.05
Nodes (19): channel(), EventSource, _parse(), RedisEvents, sse(), configure_logging(), JsonFormatter, observe() (+11 more)

### Community 7 - "pydantic"
Cohesion: 0.13
Nodes (5): new_verifier(), google_start(), google_status(), google_unlink(), GoogleStatusOut

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "UserOut"
Cohesion: 0.19
Nodes (5): Resumo, users(), PersonOut, person_out(), UserOut

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.14
Nodes (12): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _member_client(), test_audit_log(), test_company_and_members() (+4 more)

### Community 12 - "company/service.py"
Cohesion: 0.18
Nodes (3): edit_fiscal(), CompanyFiscalOut, FiscalDataIn

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "MemberOut"
Cohesion: 0.11
Nodes (5): invite(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "modules/results/controller.py"
Cohesion: 0.14
Nodes (4): show(), result_service(), ResultsOut, ResultService

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

### Community 23 - "goals/controller.py"
Cohesion: 0.17
Nodes (6): delete_template(), role_goals(), set_role_goal(), template_options(), templates(), update_template()

### Community 24 - "ClientService"
Cohesion: 0.10
Nodes (20): edit_client(), register_client(), client_service(), ClientDetailOut, ClientIn, ClientMemberOut, ClientOptionOut, ClientOut (+12 more)

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.23
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.12
Nodes (8): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut, MfaService

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "Settings"
Cohesion: 0.09
Nodes (3): _google(), Settings, GoogleRedirects

### Community 31 - "health/controller.py"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 36 - "networks/controller.py"
Cohesion: 0.07
Nodes (14): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+6 more)

### Community 37 - "conftest.py"
Cohesion: 0.16
Nodes (7): mailer(), Sent, _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 38 - "Services"
Cohesion: 0.07
Nodes (11): Estrutura, Services, get_services(), TaskQueue, event_service(), google_redirects(), google_service(), member_service() (+3 more)

### Community 39 - "export.py"
Cohesion: 0.10
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 40 - "test_account.py"
Cohesion: 0.35
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 41 - "auth/controller.py"
Cohesion: 0.16
Nodes (9): login(), auth_service(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut (+1 more)

### Community 42 - "test_costs_results.py"
Cohesion: 0.16
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 43 - "install"
Cohesion: 0.17
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "main.py"
Cohesion: 0.10
Nodes (4): create_app(), results(), client_result_service(), ClientResultService

### Community 45 - "invitations/controller.py"
Cohesion: 0.09
Nodes (9): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut (+1 more)

### Community 46 - "CapturingMailer"
Cohesion: 0.31
Nodes (9): CapturingMailer, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_role_options_are_light() (+1 more)

### Community 47 - "limits.py"
Cohesion: 0.12
Nodes (7): TooManyAttempts, BucketResult, BucketRule, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 48 - "google.py"
Cohesion: 0.13
Nodes (7): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 49 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 50 - "sites/controller.py"
Cohesion: 0.18
Nodes (8): create(), site_service(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut

### Community 51 - "ReportService"
Cohesion: 0.11
Nodes (6): Bucket, create(), show(), SavedReportIn, SavedReportOut, ReportService

### Community 52 - "CompanyService"
Cohesion: 0.21
Nodes (3): CompanyDetailOut, CompanyPatchIn, CompanyService

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "account/controller.py"
Cohesion: 0.23
Nodes (7): account_service(), ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut, SessionOut, AccountService

### Community 56 - ".build"
Cohesion: 0.09
Nodes (4): _mailer(), NoEvents, RedisBucket, RedisCounter

### Community 57 - "ItemsOut"
Cohesion: 0.14
Nodes (9): ad_units(), assign_sites(), delete(), index(), show(), site_options(), sites_of_member(), unlinked() (+1 more)

### Community 58 - "set_active_company"
Cohesion: 0.12
Nodes (5): company_image(), do_logout(), get_invitation(), me(), set_active_company()

### Community 59 - "GoalTemplateOut"
Cohesion: 0.16
Nodes (3): create_template(), GoalTemplateIn, GoalTemplateOut

### Community 60 - ".change_password"
Cohesion: 0.15
Nodes (3): do_change_password(), get_sessions(), revoke_others()

### Community 61 - "test_sites.py"
Cohesion: 0.29
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 62 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 64 - "PeopleService"
Cohesion: 0.17
Nodes (5): disable(), enable(), reset_mfa(), people_service(), PeopleService

### Community 65 - "mcm/controller.py"
Cohesion: 0.09
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "_onboard_owner"
Cohesion: 0.21
Nodes (14): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format() (+6 more)

### Community 68 - "reports/controller.py"
Cohesion: 0.11
Nodes (9): create_from_template(), delete(), duplicate(), export(), export_saved(), query(), run(), update() (+1 more)

### Community 69 - "Limiter"
Cohesion: 0.13
Nodes (6): Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - ".uow"
Cohesion: 0.06
Nodes (13): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+5 more)

### Community 71 - "ReportResultOut"
Cohesion: 0.18
Nodes (3): ReportRangeOut, ReportResultOut, ReportRowOut

### Community 72 - "SessionCookies"
Cohesion: 0.11
Nodes (4): SessionCookies, get_cookies(), google_callback(), verify()

### Community 75 - "uuid"
Cohesion: 0.32
Nodes (14): _csrf(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+6 more)

### Community 77 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 79 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 80 - "pytest"
Cohesion: 0.28
Nodes (4): client(), engine(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 81 - "GoogleService"
Cohesion: 0.09
Nodes (3): GoogleUnavailable, GoogleAuth, GoogleService

### Community 82 - "test_company_image.py"
Cohesion: 0.13
Nodes (8): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 84 - "company/controller.py"
Cohesion: 0.16
Nodes (5): edit_image(), fiscal(), remove_image(), show(), company_service()

### Community 89 - "image_response"
Cohesion: 0.18
Nodes (3): client_info(), image_response(), image_upload()

### Community 91 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 92 - "UnitOfWorkFactory"
Cohesion: 0.07
Nodes (4): UnitOfWorkFactory, default_period(), page_out(), RoleRefOut

### Community 95 - "RateLimited"
Cohesion: 0.25
Nodes (3): QueryTooHeavy, RateLimited, _statement_timeout()

### Community 136 - "reports/service.py"
Cohesion: 0.07
Nodes (11): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn (+3 more)

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1172 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **69 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `roles/controller.py`, `.uow`, `.trusted_uow`, `GoalService`, `.__init__`, `reports/service.py`, `.__init__`, `.uow`, `MemberOut`, `api_keys/controller.py`, `.__init__`, `.__init__`, `custom_metrics/controller.py`, `.__init__`, `.__init__`, `costs/controller.py`, `modules/results/controller.py`, `ClientService`, `mfa/controller.py`, `networks/controller.py`, `auth/controller.py`, `main.py`, `invitations/controller.py`, `sites/controller.py`, `ReportService`, `CompanyService`, `currencies/controller.py`, `account/controller.py`, `goals/service.py`, `PeopleService`, `mcm/controller.py`, `.uow`, `AuditService`, `SiteService`, `GoogleService`, `AuthService`, `profile/controller.py`, `.__init__`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 73 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 73 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_internal.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10975609756097561 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `invitations/controller.py` to `audit/controller.py`, `contracts/controller.py`, `roles/controller.py`, `Actor`, `.trusted_uow`, `GoalService`, `.uow`, `reports/service.py`, `UserOut`, `.uow`, `MemberOut`, `api_keys/controller.py`, `costs/controller.py`, `goals/controller.py`, `ClientService`, `networks/controller.py`, `main.py`, `sites/controller.py`, `ItemsOut`, `GoalTemplateOut`, `goals/service.py`, `PeopleService`, `mcm/controller.py`, `.uow`, `AuditService`, `SiteService`, `UnitOfWorkFactory`, `.page_saved`?**
  _High betweenness centrality (0.101) - this node is a cross-community bridge._
- **Are the 38 inferred relationships involving `PageOut` (e.g. with `index()` and `ApiKeyService`) actually correct?**
  _`PageOut` has 38 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05878332194121668 - nodes in this community are weakly interconnected._