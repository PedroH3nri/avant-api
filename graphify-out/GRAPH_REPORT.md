# Graph Report - avant-api  (2026-10-28)

## Corpus Check
- 186 files · ~52,214 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2152 nodes · 5338 edges · 142 communities (70 shown, 72 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 851 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `63826eeb`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- sites/controller.py
- Actor
- Services
- fastapi
- google.py
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
- do_reset_password
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- shared/dto.py
- UnitOfWorkFactory
- Avant: conexão com o GAM
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- google/controller.py
- health/controller.py
- main.py
- session-start.sh
- avant-api
- clients/controller.py
- FakeGoogle
- UserOut
- _onboard_owner
- conftest.py
- MemberOut
- test_costs_results.py
- install
- .trusted_uow
- InvitationOut
- AccountService
- limits.py
- test_events.py
- index
- csv_export.py
- ReportQueryIn
- DimensionOut
- edit
- currencies/controller.py
- test_account.py
- clients
- test_api_keys.py
- events/controller.py
- TaskQueue
- GoogleService
- auth/controller.py
- reports/dto.py
- GoogleAuth
- people/controller.py
- mcm/controller.py
- container.py
- login
- ReportService
- Limiter
- MemberService
- networks/controller.py
- SessionCookies
- avant-api
- company/controller.py
- AuthService
- google_start
- RateLimited
- ItemsOut
- test_sites.py
- networks/service.py
- Counter
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- members/controller.py
- image_response
- _staff
- CompanyService
- google_status
- ProfileService
- remove_image
- users
- account/controller.py
- ports.py
- image
- change_status
- export
- .of
- ClientService
- .preview_invitation
- source_files

## God Nodes (most connected - your core abstractions)
1. `Services` - 83 edges
2. `UnitOfWorkFactory` - 76 edges
3. `CapturingMailer` - 73 edges
4. `_onboard_owner()` - 65 edges
5. `_csrf()` - 58 edges
6. `ClientService` - 48 edges
7. `ItemsOut` - 48 edges
8. `SiteService` - 31 edges
9. `_member_client()` - 31 edges
10. `get_services()` - 30 edges

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

## Communities (142 total, 72 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.19
Nodes (9): _csrf(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa() (+1 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (24): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, contract(), contract_networks() (+16 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (11): create(), edit(), index(), permissions(), remove(), role_service(), PermissionOut, RoleIn (+3 more)

### Community 3 - "sites/controller.py"
Cohesion: 0.06
Nodes (23): Atribuição de sites, GAM, Networks, Sites e ad units, ad_units(), assign_sites(), create(), delete() (+15 more)

### Community 4 - "Actor"
Cohesion: 0.12
Nodes (9): cancel_owner(), client(), client_image(), edit_client(), invite_owner(), new_owner(), register_client(), remove_client_image() (+1 more)

### Community 5 - "Services"
Cohesion: 0.07
Nodes (17): Services, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_cookies() (+9 more)

### Community 6 - "fastapi"
Cohesion: 0.06
Nodes (8): get_auth(), get_services(), auth_service(), currency_service(), mfa_service(), MfaService, profile_service(), image_upload()

### Community 7 - "google.py"
Cohesion: 0.12
Nodes (7): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.13
Nodes (12): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _member_client(), test_audit_log(), test_company_and_members() (+4 more)

### Community 13 - ".uow"
Cohesion: 0.08
Nodes (14): add_members(), create(), edit(), index(), remove(), remove_member(), show(), group_service() (+6 more)

### Community 14 - "ItemsOut"
Cohesion: 0.16
Nodes (3): index(), audit_service(), AuditService

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
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 23 - "shared/dto.py"
Cohesion: 0.14
Nodes (4): GoogleStatusOut, CompanyRefOut, FiscalDataOut, RoleRefOut

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
Nodes (7): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "google/controller.py"
Cohesion: 0.11
Nodes (4): Settings, google_redirects(), google_service(), GoogleRedirects

### Community 31 - "health/controller.py"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 32 - "main.py"
Cohesion: 0.10
Nodes (5): configure_logging(), JsonFormatter, observe(), _route_template(), create_app()

### Community 36 - "clients/controller.py"
Cohesion: 0.20
Nodes (10): client_service(), ClientDetailOut, ClientIn, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn (+2 more)

### Community 38 - "UserOut"
Cohesion: 0.17
Nodes (3): edit_image(), remove_image(), UserOut

### Community 39 - "_onboard_owner"
Cohesion: 0.20
Nodes (14): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format() (+6 more)

### Community 40 - "conftest.py"
Cohesion: 0.13
Nodes (5): CapturingMailer, client(), engine(), mailer(), Sent

### Community 41 - "MemberOut"
Cohesion: 0.14
Nodes (6): invite(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 42 - "test_costs_results.py"
Cohesion: 0.26
Nodes (4): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone()

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 45 - "InvitationOut"
Cohesion: 0.09
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 46 - "AccountService"
Cohesion: 0.14
Nodes (5): do_change_password(), forgot_password(), get_sessions(), revoke_others(), AccountService

### Community 47 - "limits.py"
Cohesion: 0.09
Nodes (8): TooManyAttempts, BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 48 - "test_events.py"
Cohesion: 0.07
Nodes (15): channel(), _parse(), RedisEvents, sse(), events(), _collect(), _event(), ListEvents (+7 more)

### Community 49 - "index"
Cohesion: 0.13
Nodes (6): edit(), index(), leave(), remove(), set_permissions(), show()

### Community 50 - "csv_export.py"
Cohesion: 0.12
Nodes (4): _number(), _safe_cell(), to_csv(), dimension_text()

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.16
Nodes (3): list_currencies(), update_preferences(), CurrencyService

### Community 55 - "test_account.py"
Cohesion: 0.35
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 57 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 58 - "events/controller.py"
Cohesion: 0.22
Nodes (3): EventSource, event_service(), EventService

### Community 60 - "GoogleService"
Cohesion: 0.16
Nodes (3): GoogleUnavailable, google_callback(), GoogleService

### Community 61 - "auth/controller.py"
Cohesion: 0.26
Nodes (7): AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut, MeOut

### Community 62 - "reports/dto.py"
Cohesion: 0.12
Nodes (8): FilterIn, LabelOut, MetricOut, OrderIn, PeriodIn, ReportRangeOut, ReportResultOut, ReportRowOut

### Community 64 - "people/controller.py"
Cohesion: 0.16
Nodes (5): disable(), enable(), reset_mfa(), people_service(), PeopleService

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "container.py"
Cohesion: 0.05
Nodes (8): _google(), _mailer(), NoEvents, PillowImageProcessor, MemoryCounter, RedisCounter, CeleryQueue, RecordingQueue

### Community 67 - "login"
Cohesion: 0.21
Nodes (5): accept(), company_image(), do_logout(), login(), set_active_company()

### Community 68 - "ReportService"
Cohesion: 0.20
Nodes (5): Bucket, catalog(), report_service(), MetricCatalogOut, ReportService

### Community 69 - "Limiter"
Cohesion: 0.17
Nodes (5): Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "networks/controller.py"
Cohesion: 0.14
Nodes (10): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs(), network_service() (+2 more)

### Community 74 - "company/controller.py"
Cohesion: 0.32
Nodes (3): CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 77 - "RateLimited"
Cohesion: 0.25
Nodes (3): QueryTooHeavy, RateLimited, _statement_timeout()

### Community 78 - "ItemsOut"
Cohesion: 0.17
Nodes (4): audit(), owner_invitations(), AuditOut, ItemsOut

### Community 79 - "test_sites.py"
Cohesion: 0.29
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 82 - "test_company_image.py"
Cohesion: 0.36
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 86 - "members/controller.py"
Cohesion: 0.25
Nodes (6): member_service(), DirectPermissionIn, DirectPermissionOut, MemberDetailOut, MemberPatchIn, MemberPermissionsIn

### Community 88 - "_staff"
Cohesion: 0.51
Nodes (6): _staff(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_internal_clients(), test_internal_people_and_staff()

### Community 89 - "CompanyService"
Cohesion: 0.14
Nodes (6): edit_fiscal(), edit_image(), fiscal(), image(), show(), CompanyService

### Community 91 - "ProfileService"
Cohesion: 0.25
Nodes (4): edit_appearance(), AppearanceIn, AppearanceOut, ProfileService

### Community 93 - "users"
Cohesion: 0.22
Nodes (4): Resumo, users(), PersonOut, person_out()

### Community 94 - "account/controller.py"
Cohesion: 0.32
Nodes (5): ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut, SessionOut

### Community 132 - "ClientService"
Cohesion: 0.43
Nodes (3): client_teams(), ClientMemberOut, ClientService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1013 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **72 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `roles/controller.py`, `sites/controller.py`, `ClientService`, `fastapi`, `.__init__`, `.__init__`, `.__init__`, `CompanyService`, `.uow`, `ItemsOut`, `api_keys/controller.py`, `avant_core_access_models`, `costs/controller.py`, `shared/dto.py`, `google/controller.py`, `clients/controller.py`, `MemberOut`, `.trusted_uow`, `InvitationOut`, `AccountService`, `csv_export.py`, `currencies/controller.py`, `TaskQueue`, `GoogleService`, `auth/controller.py`, `GoogleAuth`, `people/controller.py`, `mcm/controller.py`, `ReportService`, `MemberService`, `networks/controller.py`, `company/controller.py`, `AuthService`, `networks/service.py`, `members/controller.py`, `CompanyService`, `ProfileService`, `account/controller.py`, `.__init__`, `ports.py`, `.__init__`, `.__init__`?**
  _High betweenness centrality (0.149) - this node is a cross-community bridge._
- **Are the 51 inferred relationships involving `Services` (e.g. with `Estrutura` and `EventSource`) actually correct?**
  _`Services` has 51 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0609009009009009 - nodes in this community are weakly interconnected._
- **Why does `Services` connect `Services` to `contracts/controller.py`, `roles/controller.py`, `sites/controller.py`, `fastapi`, `.uow`, `ItemsOut`, `api_keys/controller.py`, `avant_core_access_models`, `costs/controller.py`, `google/controller.py`, `health/controller.py`, `main.py`, `clients/controller.py`, `conftest.py`, `MemberOut`, `InvitationOut`, `limits.py`, `test_events.py`, `events/controller.py`, `TaskQueue`, `GoogleAuth`, `people/controller.py`, `mcm/controller.py`, `container.py`, `ReportService`, `Limiter`, `networks/controller.py`, `members/controller.py`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **Are the 24 inferred relationships involving `UnitOfWorkFactory` (e.g. with `AccountService` and `ApiKeyService`) actually correct?**
  _`UnitOfWorkFactory` has 24 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.083710407239819 - nodes in this community are weakly interconnected._