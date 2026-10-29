# Graph Report - avant-api  (2026-10-29)

## Corpus Check
- 201 files · ~58,557 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2459 nodes · 6254 edges · 145 communities (71 shown, 74 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1003 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0e0de24d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_internal.py
- contracts/controller.py
- roles/controller.py
- sites/controller.py
- Actor
- Services
- events/controller.py
- GoogleService
- steps
- NetworkService
- Avant: models do MVP
- _member_client
- CompanyService
- .uow
- ItemsOut
- Groone Avant: contexto do projeto
- api_keys/controller.py
- avant_core_access_models
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- goals/controller.py
- UnitOfWorkFactory
- Avant: conexão com o GAM
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- test_goal_progress_routes
- ready
- middleware.py
- session-start.sh
- avant-api
- shared/dto.py
- _onboard_owner
- CapturingMailer
- test_account.py
- MemberOut
- conftest.py
- install
- shared/dto.py
- InvitationOut
- account/controller.py
- limits.py
- google.py
- MemberService
- export.py
- .uow
- edit
- currencies/controller.py
- auth/controller.py
- container.py
- test_api_keys.py
- .update_fiscal
- members/controller.py
- reports/service.py
- list_currencies
- people/controller.py
- mcm/controller.py
- enqueue_sync
- reports/controller.py
- Limiter
- index
- connect
- SessionCookies
- avant-api
- company/controller.py
- uuid
- audit/controller.py
- FakeGoogle
- test_groups_lifecycle
- QueryTooHeavy
- networks/service.py
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- errors.py
- google_status
- image_response
- profile/controller.py
- settings.py
- google/controller.py
- GoogleAuth
- networks/dependencies.py
- MemoryCounter
- images.py
- templates
- ClientService
- change_status
- .owner_invitations
- image
- source_files
- RateLimited

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 92 edges
2. `Services` - 87 edges
3. `_onboard_owner()` - 84 edges
4. `UnitOfWorkFactory` - 82 edges
5. `_csrf()` - 75 edges
6. `ItemsOut` - 55 edges
7. `ReportService` - 49 edges
8. `ClientService` - 48 edges
9. `_member_client()` - 36 edges
10. `get_services()` - 32 edges

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

## Communities (145 total, 74 thin omitted)

### Community 0 - "test_internal.py"
Cohesion: 0.14
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _staff(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_internal_clients() (+6 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (23): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem, contract(), contract_networks(), contracts() (+15 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "sites/controller.py"
Cohesion: 0.06
Nodes (23): Atribuição de sites, GAM, Networks, Sites e ad units, ad_units(), assign_sites(), create(), delete() (+15 more)

### Community 4 - "Actor"
Cohesion: 0.09
Nodes (10): cancel_owner(), client(), client_image(), client_teams(), clients(), edit_client(), invite_owner(), owner_invitations() (+2 more)

### Community 5 - "Services"
Cohesion: 0.07
Nodes (16): Services, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_services(), get_session_actor() (+8 more)

### Community 6 - "events/controller.py"
Cohesion: 0.07
Nodes (15): channel(), EventSource, _parse(), RedisEvents, sse(), events(), EventService, _collect() (+7 more)

### Community 7 - "GoogleService"
Cohesion: 0.15
Nodes (3): google_callback(), google_service(), GoogleService

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.19
Nodes (10): _inventory(), test_manual_site(), test_sites_and_assignment(), _member_client(), test_audit_log(), test_company_and_members(), test_leave_company(), test_requires_session() (+2 more)

### Community 12 - "CompanyService"
Cohesion: 0.20
Nodes (3): remove_image(), CompanyDetailOut, CompanyService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), remove(), remove_member(), show(), group_service() (+6 more)

### Community 14 - "ItemsOut"
Cohesion: 0.16
Nodes (4): index(), audit(), AuditOut, ItemsOut

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "avant_core_access_models"
Cohesion: 0.05
Nodes (11): results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut (+3 more)

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
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), templates() (+10 more)

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 26 - "clean_code.py"
Cohesion: 0.18
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "test_reports.py"
Cohesion: 0.22
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (10): get_cookies(), get_session_auth(), confirm(), disable(), new_recovery_codes(), setup(), verify(), MfaCodeIn (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "test_goal_progress_routes"
Cohesion: 0.53
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 31 - "ready"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 36 - "shared/dto.py"
Cohesion: 0.14
Nodes (13): new_owner(), client_service(), ClientDetailOut, ClientIn, ClientMemberOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+5 more)

### Community 37 - "_onboard_owner"
Cohesion: 0.18
Nodes (12): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format(), test_members_come_in_pages_of_ten() (+4 more)

### Community 39 - "CapturingMailer"
Cohesion: 0.17
Nodes (11): CapturingMailer, client(), engine(), mailer(), Sent, _queue(), _second_owner(), test_connect_sync_and_disconnect() (+3 more)

### Community 40 - "test_account.py"
Cohesion: 0.35
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 41 - "MemberOut"
Cohesion: 0.13
Nodes (6): invite(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 42 - "conftest.py"
Cohesion: 0.11
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "shared/dto.py"
Cohesion: 0.16
Nodes (5): PersonOut, person_out(), CompanyRefOut, RoleRefOut, UserOut

### Community 45 - "InvitationOut"
Cohesion: 0.09
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 46 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 47 - "limits.py"
Cohesion: 0.08
Nodes (9): Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket() (+1 more)

### Community 48 - "google.py"
Cohesion: 0.13
Nodes (7): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 49 - "MemberService"
Cohesion: 0.17
Nodes (3): set_permissions(), MemberDetailOut, MemberService

### Community 50 - "export.py"
Cohesion: 0.07
Nodes (13): JsonFormatter, dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx() (+5 more)

### Community 51 - ".uow"
Cohesion: 0.09
Nodes (3): SavedReportIn, SavedReportOut, ReportService

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.19
Nodes (4): currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "auth/controller.py"
Cohesion: 0.15
Nodes (9): get_invitation(), auth_service(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut (+1 more)

### Community 56 - "container.py"
Cohesion: 0.05
Nodes (10): Estrutura, _google(), _mailer(), NoEvents, configure_logging(), Settings, CeleryQueue, RecordingQueue (+2 more)

### Community 57 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 61 - "members/controller.py"
Cohesion: 0.20
Nodes (6): member_service(), DirectPermissionIn, DirectPermissionOut, MemberPatchIn, MemberPermissionsIn, PageOut

### Community 62 - "reports/service.py"
Cohesion: 0.07
Nodes (11): CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+3 more)

### Community 64 - "people/controller.py"
Cohesion: 0.12
Nodes (8): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PeopleService

### Community 65 - "mcm/controller.py"
Cohesion: 0.09
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 68 - "reports/controller.py"
Cohesion: 0.09
Nodes (14): catalog(), create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index() (+6 more)

### Community 69 - "Limiter"
Cohesion: 0.12
Nodes (6): Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "index"
Cohesion: 0.15
Nodes (5): edit(), index(), leave(), remove(), show()

### Community 71 - "connect"
Cohesion: 0.18
Nodes (7): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs()

### Community 72 - "SessionCookies"
Cohesion: 0.09
Nodes (8): SessionCookies, accept(), company_image(), do_logout(), login(), me(), set_active_company(), MeOut

### Community 74 - "company/controller.py"
Cohesion: 0.23
Nodes (4): company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 75 - "uuid"
Cohesion: 0.27
Nodes (15): _csrf(), _owner_invite(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused() (+7 more)

### Community 76 - "audit/controller.py"
Cohesion: 0.15
Nodes (4): require(), dependency(), require_session(), audit_service()

### Community 80 - "networks/service.py"
Cohesion: 0.18
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 82 - "test_company_image.py"
Cohesion: 0.31
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 84 - "errors.py"
Cohesion: 0.20
Nodes (4): CsrfFailed, GoogleUnavailable, NoActiveCompany, TooManyAttempts

### Community 89 - "image_response"
Cohesion: 0.18
Nodes (3): client_info(), image_response(), image_upload()

### Community 91 - "profile/controller.py"
Cohesion: 0.12
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 96 - "google/controller.py"
Cohesion: 0.12
Nodes (4): new_verifier(), google_start(), GoogleStatusOut, GoogleRedirects

### Community 132 - "ClientService"
Cohesion: 0.12
Nodes (3): remove_client_image(), ClientOut, ClientService

### Community 136 - "image"
Cohesion: 0.18
Nodes (3): fiscal(), image(), show()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1147 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **74 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `.__init__`, `roles/controller.py`, `ClientService`, `Services`, `.__init__`, `GoogleService`, `sites/controller.py`, `NetworkService`, `CompanyService`, `.uow`, `.__init__`, `api_keys/controller.py`, `avant_core_access_models`, `.__init__`, `custom_metrics/controller.py`, `costs/controller.py`, `goals/controller.py`, `shared/dto.py`, `MemberOut`, `shared/dto.py`, `InvitationOut`, `account/controller.py`, `MemberService`, `.uow`, `currencies/controller.py`, `auth/controller.py`, `members/controller.py`, `reports/service.py`, `people/controller.py`, `mcm/controller.py`, `company/controller.py`, `audit/controller.py`, `networks/service.py`, `.__init__`, `errors.py`, `.__init__`, `profile/controller.py`, `avant_core_shared_clock`, `GoogleAuth`?**
  _High betweenness centrality (0.128) - this node is a cross-community bridge._
- **Are the 67 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 67 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_internal.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13709677419354838 - nodes in this community are weakly interconnected._
- **Why does `Services` connect `Services` to `MemoryCounter`, `images.py`, `contracts/controller.py`, `roles/controller.py`, `sites/controller.py`, `events/controller.py`, `GoogleService`, `.uow`, `.uow`, `api_keys/controller.py`, `avant_core_access_models`, `custom_metrics/controller.py`, `costs/controller.py`, `goals/controller.py`, `mfa/controller.py`, `ready`, `shared/dto.py`, `CapturingMailer`, `MemberOut`, `InvitationOut`, `account/controller.py`, `limits.py`, `currencies/controller.py`, `auth/controller.py`, `container.py`, `members/controller.py`, `people/controller.py`, `mcm/controller.py`, `Limiter`, `company/controller.py`, `audit/controller.py`, `profile/controller.py`, `GoogleAuth`, `networks/dependencies.py`?**
  _High betweenness centrality (0.057) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Services` (e.g. with `Estrutura` and `EventSource`) actually correct?**
  _`Services` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06070175438596491 - nodes in this community are weakly interconnected._