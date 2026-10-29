# Graph Report - avant-api  (2026-10-29)

## Corpus Check
- 201 files · ~60,025 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2503 nodes · 6454 edges · 145 communities (76 shown, 69 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1049 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `79e91441`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_internal.py
- contracts/controller.py
- roles/controller.py
- sites/controller.py
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
- avant_core_access_models
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- goals/controller.py
- clients/controller.py
- Avant: conexão com o GAM
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- test_goals.py
- health/controller.py
- BaseModel
- session-start.sh
- avant-api
- NetworkDetailOut
- conftest.py
- Services
- to_csv
- test_account.py
- update
- test_costs_results.py
- install
- SavedReportOut
- invitations/controller.py
- CapturingMailer
- limits.py
- google/controller.py
- .of
- export.py
- .uow
- CompanyService
- edit
- currencies/controller.py
- account/controller.py
- conftest.py
- index
- index
- networks/service.py
- test_sites.py
- .catalog
- reports/dependencies.py
- PeopleService
- mcm/controller.py
- _onboard_owner
- .of
- reports/controller.py
- Limiter
- .uow
- PageOut
- SessionCookies
- avant-api
- TaskQueue
- uuid
- PageOut
- .list_all
- middleware.py
- ClientService
- UnitOfWorkFactory
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- edit_fiscal
- image
- templates
- auth/controller.py
- image_response
- profile/controller.py
- shared/dto.py
- do_reset_password
- edit
- edit_image
- MemoryCounter
- .page_saved
- _csv_cell
- .trusted_uow
- image
- image_url
- reports/service.py
- fiscal
- source_files

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 97 edges
2. `_onboard_owner()` - 89 edges
3. `Services` - 87 edges
4. `UnitOfWorkFactory` - 82 edges
5. `_csrf()` - 78 edges
6. `PageOut` - 66 edges
7. `ClientService` - 51 edges
8. `ReportService` - 51 edges
9. `ItemsOut` - 37 edges
10. `SiteService` - 36 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/modules/company/controller.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (145 total, 69 thin omitted)

### Community 0 - "test_internal.py"
Cohesion: 0.13
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _staff(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_internal_clients() (+6 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "sites/controller.py"
Cohesion: 0.05
Nodes (26): Atribuição de sites, GAM, Networks, Sites e ad units, ad_units(), assign_sites(), create(), delete() (+18 more)

### Community 4 - "Actor"
Cohesion: 0.08
Nodes (12): cancel_owner(), client(), client_image(), client_options(), clients(), edit_client(), invite_owner(), new_owner() (+4 more)

### Community 5 - "security.py"
Cohesion: 0.08
Nodes (14): CsrfFailed, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor(), get_session_auth() (+6 more)

### Community 6 - "test_events.py"
Cohesion: 0.07
Nodes (17): channel(), EventSource, _parse(), RedisEvents, sse(), events(), EventService, _collect() (+9 more)

### Community 7 - "pydantic"
Cohesion: 0.11
Nodes (3): google_status(), google_unlink(), GoogleStatusOut

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "UserOut"
Cohesion: 0.16
Nodes (3): PersonOut, person_out(), UserOut

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.17
Nodes (17): _csrf(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission(), _png() (+9 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "MemberOut"
Cohesion: 0.11
Nodes (6): invite(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.16
Nodes (6): create(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "avant_core_access_models"
Cohesion: 0.07
Nodes (8): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, default_period(), ResultService

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.25
Nodes (6): custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn, CustomMetricOut, CustomMetricService

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
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), templates() (+10 more)

### Community 24 - "clients/controller.py"
Cohesion: 0.15
Nodes (13): change_status(), edit_client_image(), client_service(), ClientDetailOut, ClientIn, ClientOptionOut, ClientOut, ClientPatchIn (+5 more)

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.14
Nodes (11): Modelo de dados, Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "test_reports.py"
Cohesion: 0.23
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.07
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "test_goals.py"
Cohesion: 0.43
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 31 - "health/controller.py"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 32 - "BaseModel"
Cohesion: 0.14
Nodes (6): FilterIn, OrderIn, PeriodIn, ReportRangeOut, ReportRowOut, SavedQueryOut

### Community 36 - "NetworkDetailOut"
Cohesion: 0.19
Nodes (3): connect(), NetworkDetailOut, NetworkService

### Community 37 - "conftest.py"
Cohesion: 0.11
Nodes (6): client(), engine(), mailer(), Sent, _membership_ids(), test_groups_lifecycle()

### Community 38 - "Services"
Cohesion: 0.05
Nodes (11): _mailer(), Services, NoEvents, PillowImageProcessor, get_services(), Settings, CeleryQueue, RecordingQueue (+3 more)

### Community 39 - "to_csv"
Cohesion: 0.20
Nodes (6): dimension_text(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx()

### Community 40 - "test_account.py"
Cohesion: 0.22
Nodes (7): FakeGoogle, _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 41 - "update"
Cohesion: 0.14
Nodes (5): check(), create(), delete(), index(), update()

### Community 42 - "test_costs_results.py"
Cohesion: 0.18
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 45 - "invitations/controller.py"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 46 - "CapturingMailer"
Cohesion: 0.31
Nodes (8): CapturingMailer, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_role_options_are_light(), test_team_lists_come_in_pages()

### Community 47 - "limits.py"
Cohesion: 0.08
Nodes (8): BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 48 - "google/controller.py"
Cohesion: 0.04
Nodes (18): _google(), GoogleFailed, GoogleUnavailable, NoActiveCompany, challenge(), _claims(), GoogleAuth, GoogleOAuth (+10 more)

### Community 49 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 50 - "export.py"
Cohesion: 0.12
Nodes (4): _xlsx_cell(), _result(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 51 - ".uow"
Cohesion: 0.09
Nodes (5): Bucket, query(), ReportQueryIn, ReportResultOut, ReportService

### Community 52 - "CompanyService"
Cohesion: 0.24
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 53 - "edit"
Cohesion: 0.15
Nodes (12): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+4 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "account/controller.py"
Cohesion: 0.10
Nodes (11): delete_session(), do_change_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn (+3 more)

### Community 57 - "conftest.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 58 - "index"
Cohesion: 0.14
Nodes (3): index(), leave(), options()

### Community 60 - "networks/service.py"
Cohesion: 0.24
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 61 - "test_sites.py"
Cohesion: 0.29
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 62 - ".catalog"
Cohesion: 0.13
Nodes (5): catalog(), DimensionOut, LabelOut, MetricCatalogOut, MetricOut

### Community 64 - "PeopleService"
Cohesion: 0.15
Nodes (5): disable(), enable(), reset_mfa(), people_service(), PeopleService

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "_onboard_owner"
Cohesion: 0.32
Nodes (8): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format()

### Community 68 - "reports/controller.py"
Cohesion: 0.13
Nodes (10): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), run(), show() (+2 more)

### Community 69 - "Limiter"
Cohesion: 0.12
Nodes (7): TooManyAttempts, Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - ".uow"
Cohesion: 0.11
Nodes (11): edit(), remove(), set_permissions(), show(), member_service(), DirectPermissionIn, DirectPermissionOut, MemberDetailOut (+3 more)

### Community 71 - "PageOut"
Cohesion: 0.18
Nodes (7): disconnect(), index(), options(), service_account(), show(), sync(), sync_runs()

### Community 74 - "TaskQueue"
Cohesion: 0.11
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskQueue, enqueue_sync()

### Community 75 - "uuid"
Cohesion: 0.25
Nodes (14): test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+6 more)

### Community 76 - "PageOut"
Cohesion: 0.08
Nodes (8): require(), index(), audit_service(), AuditService, audit(), AuditOut, page_out(), PageOut

### Community 79 - "middleware.py"
Cohesion: 0.14
Nodes (4): configure_logging(), JsonFormatter, observe(), _route_template()

### Community 80 - "ClientService"
Cohesion: 0.43
Nodes (4): client_teams(), ClientMemberOut, ClientService, CompanyRefOut

### Community 82 - "test_company_image.py"
Cohesion: 0.31
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.07
Nodes (15): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), AcceptInvitationIn (+7 more)

### Community 89 - "image_response"
Cohesion: 0.18
Nodes (3): company_service(), image_response(), image_upload()

### Community 91 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 94 - "do_reset_password"
Cohesion: 0.17
Nodes (3): do_reset_password(), forgot_password(), client_info()

### Community 95 - "edit"
Cohesion: 0.33
Nodes (3): Imagem da Empresa, edit(), CompanyPatchIn

### Community 136 - "reports/service.py"
Cohesion: 0.09
Nodes (5): QueryTooHeavy, RateLimited, CustomCatalogMetricOut, ReportCountsOut, _statement_timeout()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1169 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **69 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `.__init__`, `sites/controller.py`, `.trusted_uow`, `roles/controller.py`, `.__init__`, `reports/service.py`, `.__init__`, `company/service.py`, `.uow`, `MemberOut`, `api_keys/controller.py`, `.__init__`, `.__init__`, `custom_metrics/controller.py`, `.__init__`, `avant_core_access_models`, `costs/controller.py`, `goals/controller.py`, `clients/controller.py`, `mfa/controller.py`, `NetworkDetailOut`, `invitations/controller.py`, `google/controller.py`, `.uow`, `CompanyService`, `currencies/controller.py`, `account/controller.py`, `networks/service.py`, `PeopleService`, `mcm/controller.py`, `.uow`, `TaskQueue`, `PageOut`, `ports.py`, `ClientService`, `auth/controller.py`, `profile/controller.py`, `.__init__`?**
  _High betweenness centrality (0.149) - this node is a cross-community bridge._
- **Are the 72 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 72 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_internal.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13446969696969696 - nodes in this community are weakly interconnected._
- **Why does `Services` connect `Services` to `contracts/controller.py`, `roles/controller.py`, `sites/controller.py`, `security.py`, `test_events.py`, `.uow`, `MemberOut`, `api_keys/controller.py`, `avant_core_access_models`, `custom_metrics/controller.py`, `costs/controller.py`, `goals/controller.py`, `clients/controller.py`, `mfa/controller.py`, `health/controller.py`, `conftest.py`, `invitations/controller.py`, `limits.py`, `google/controller.py`, `.uow`, `currencies/controller.py`, `account/controller.py`, `reports/dependencies.py`, `PeopleService`, `mcm/controller.py`, `Limiter`, `.uow`, `SessionCookies`, `TaskQueue`, `PageOut`, `image_response`, `profile/controller.py`, `MemoryCounter`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Services` (e.g. with `Estrutura` and `EventSource`) actually correct?**
  _`Services` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0676056338028169 - nodes in this community are weakly interconnected._