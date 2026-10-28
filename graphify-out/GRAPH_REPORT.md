# Graph Report - avant-api  (2026-10-28)

## Corpus Check
- 192 files · ~53,507 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2222 nodes · 5530 edges · 137 communities (69 shown, 68 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 887 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bd896d1a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- sites/controller.py
- Actor
- Services
- Services
- google/controller.py
- steps
- Avant: models do MVP
- _member_client
- CompanyService
- .uow
- fastapi
- Groone Avant: contexto do projeto
- api_keys/controller.py
- avant_core_access_models
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
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
- _onboard_owner
- UserOut
- CapturingMailer
- conftest.py
- MemberOut
- test_costs_results.py
- install
- InvitationOut
- account/controller.py
- limits.py
- test_events.py
- index
- csv_export.py
- ReportQueryIn
- MemoryBucket
- edit
- currencies/controller.py
- RedisCounter
- .of
- test_api_keys.py
- ReportResultOut
- TaskQueue
- GoogleService
- mfa/controller.py
- reports/dto.py
- images.py
- people/controller.py
- mcm/controller.py
- .build
- auth/controller.py
- ReportService
- Limiter
- MemberService
- networks/controller.py
- avant-api
- company/controller.py
- list_currencies
- CustomCatalogMetricOut
- RateLimited
- ItemsOut
- test_sites.py
- networks/service.py
- Counter
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- fiscal
- TooManyAttempts
- members/controller.py
- image_response
- ProfileService
- edit_fiscal
- image
- ClientService
- source_files

## God Nodes (most connected - your core abstractions)
1. `Services` - 85 edges
2. `UnitOfWorkFactory` - 79 edges
3. `CapturingMailer` - 75 edges
4. `_onboard_owner()` - 67 edges
5. `_csrf()` - 60 edges
6. `ItemsOut` - 50 edges
7. `ClientService` - 48 edges
8. `get_services()` - 31 edges
9. `SiteService` - 31 edges
10. `_member_client()` - 31 edges

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

## Communities (137 total, 68 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.17
Nodes (15): _csrf(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _staff(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client() (+7 more)

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
Cohesion: 0.10
Nodes (11): Modelo de dados, audit(), cancel_owner(), change_status(), client(), client_image(), client_teams(), clients() (+3 more)

### Community 5 - "Services"
Cohesion: 0.09
Nodes (14): CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor() (+6 more)

### Community 6 - "Services"
Cohesion: 0.05
Nodes (12): Services, get_services(), account_service(), company_service(), client_service(), mcm_service(), invitation_service(), member_service() (+4 more)

### Community 7 - "google/controller.py"
Cohesion: 0.07
Nodes (7): GoogleFailed, challenge(), _claims(), identity_from_id_token(), new_verifier(), GoogleStatusOut, FakeGoogle

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.13
Nodes (12): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _member_client(), test_audit_log(), test_company_and_members() (+4 more)

### Community 12 - "CompanyService"
Cohesion: 0.21
Nodes (3): show(), CompanyDetailOut, CompanyService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), remove(), remove_member(), show(), group_service() (+6 more)

### Community 14 - "fastapi"
Cohesion: 0.08
Nodes (6): EventSource, index(), audit_service(), events(), event_service(), EventService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "avant_core_access_models"
Cohesion: 0.05
Nodes (11): results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut (+3 more)

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
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

### Community 23 - "shared/dto.py"
Cohesion: 0.17
Nodes (4): PersonOut, person_out(), CompanyRefOut, RoleRefOut

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
Cohesion: 0.08
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), verify(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "google/controller.py"
Cohesion: 0.11
Nodes (6): Settings, google_redirects(), google_service(), GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 31 - "health/controller.py"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 32 - "main.py"
Cohesion: 0.13
Nodes (4): configure_logging(), observe(), _route_template(), create_app()

### Community 36 - "clients/controller.py"
Cohesion: 0.20
Nodes (11): new_owner(), ClientDetailOut, ClientIn, ClientMemberOut, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+3 more)

### Community 37 - "_onboard_owner"
Cohesion: 0.38
Nodes (7): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format()

### Community 38 - "UserOut"
Cohesion: 0.17
Nodes (3): edit_image(), remove_image(), UserOut

### Community 39 - "CapturingMailer"
Cohesion: 0.22
Nodes (9): CapturingMailer, Sent, _owner_invite(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company() (+1 more)

### Community 40 - "conftest.py"
Cohesion: 0.10
Nodes (14): client(), engine(), mailer(), _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password() (+6 more)

### Community 41 - "MemberOut"
Cohesion: 0.13
Nodes (6): invite(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 42 - "test_costs_results.py"
Cohesion: 0.15
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 45 - "InvitationOut"
Cohesion: 0.11
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService, InvitationOut

### Community 46 - "account/controller.py"
Cohesion: 0.08
Nodes (14): SessionCookies, get_cookies(), delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others() (+6 more)

### Community 47 - "limits.py"
Cohesion: 0.15
Nodes (3): BucketResult, BucketRule, RedisBucket

### Community 48 - "test_events.py"
Cohesion: 0.08
Nodes (11): channel(), _parse(), RedisEvents, sse(), JsonFormatter, _collect(), ListEvents, test_redis_source_delivers_published_messages() (+3 more)

### Community 49 - "index"
Cohesion: 0.15
Nodes (5): edit(), index(), leave(), remove(), show()

### Community 50 - "csv_export.py"
Cohesion: 0.15
Nodes (4): _number(), _safe_cell(), to_csv(), dimension_text()

### Community 52 - "MemoryBucket"
Cohesion: 0.28
Nodes (4): MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.18
Nodes (4): update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 57 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 60 - "GoogleService"
Cohesion: 0.06
Nodes (7): GoogleUnavailable, GoogleAuth, google_callback(), google_start(), google_status(), google_unlink(), GoogleService

### Community 62 - "reports/dto.py"
Cohesion: 0.12
Nodes (7): DimensionOut, FilterIn, LabelOut, MetricOut, OrderIn, PeriodIn, ReportRangeOut

### Community 64 - "people/controller.py"
Cohesion: 0.13
Nodes (7): Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PeopleService

### Community 65 - "mcm/controller.py"
Cohesion: 0.11
Nodes (6): assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - ".build"
Cohesion: 0.08
Nodes (7): _google(), _mailer(), NoEvents, GoogleOAuth, MemoryCounter, CeleryQueue, RecordingQueue

### Community 67 - "auth/controller.py"
Cohesion: 0.07
Nodes (16): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+8 more)

### Community 68 - "ReportService"
Cohesion: 0.14
Nodes (6): Bucket, catalog(), export(), query(), MetricCatalogOut, ReportService

### Community 69 - "Limiter"
Cohesion: 0.23
Nodes (4): Limiter, Rule, _limiter_round(), test_memory_limiter()

### Community 71 - "networks/controller.py"
Cohesion: 0.12
Nodes (10): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs(), network_service() (+2 more)

### Community 74 - "company/controller.py"
Cohesion: 0.25
Nodes (4): CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, image_url()

### Community 77 - "RateLimited"
Cohesion: 0.20
Nodes (3): QueryTooHeavy, RateLimited, _statement_timeout()

### Community 79 - "test_sites.py"
Cohesion: 0.39
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 80 - "networks/service.py"
Cohesion: 0.24
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 82 - "test_company_image.py"
Cohesion: 0.36
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 86 - "members/controller.py"
Cohesion: 0.24
Nodes (6): set_permissions(), DirectPermissionIn, DirectPermissionOut, MemberDetailOut, MemberPatchIn, MemberPermissionsIn

### Community 89 - "image_response"
Cohesion: 0.13
Nodes (3): image(), image_response(), image_upload()

### Community 91 - "ProfileService"
Cohesion: 0.25
Nodes (4): edit_appearance(), AppearanceIn, AppearanceOut, ProfileService

### Community 92 - "edit_fiscal"
Cohesion: 0.25
Nodes (3): edit_fiscal(), edit_image(), remove_image()

### Community 132 - "ClientService"
Cohesion: 0.18
Nodes (6): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, ClientService, owner_invitation_out()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1047 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **68 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `roles/controller.py`, `sites/controller.py`, `ClientService`, `.__init__`, `.__init__`, `CompanyService`, `.uow`, `fastapi`, `api_keys/controller.py`, `avant_core_access_models`, `custom_metrics/controller.py`, `costs/controller.py`, `shared/dto.py`, `mfa/controller.py`, `clients/controller.py`, `MemberOut`, `.trusted_uow`, `InvitationOut`, `account/controller.py`, `currencies/controller.py`, `TaskQueue`, `GoogleService`, `mfa/controller.py`, `people/controller.py`, `mcm/controller.py`, `auth/controller.py`, `ReportService`, `MemberService`, `networks/controller.py`, `company/controller.py`, `RateLimited`, `networks/service.py`, `members/controller.py`, `.__init__`, `.__init__`, `.__init__`, `ProfileService`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `.__init__`?**
  _High betweenness centrality (0.149) - this node is a cross-community bridge._
- **Are the 52 inferred relationships involving `Services` (e.g. with `Estrutura` and `EventSource`) actually correct?**
  _`Services` has 52 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0609009009009009 - nodes in this community are weakly interconnected._
- **Why does `Services` connect `Services` to `contracts/controller.py`, `roles/controller.py`, `Services`, `.uow`, `fastapi`, `api_keys/controller.py`, `avant_core_access_models`, `custom_metrics/controller.py`, `costs/controller.py`, `google/controller.py`, `health/controller.py`, `main.py`, `conftest.py`, `MemberOut`, `account/controller.py`, `limits.py`, `test_events.py`, `MemoryBucket`, `RedisCounter`, `TaskQueue`, `GoogleService`, `images.py`, `people/controller.py`, `.build`, `auth/controller.py`, `ReportService`, `Limiter`, `networks/controller.py`?**
  _High betweenness centrality (0.066) - this node is a cross-community bridge._
- **Are the 25 inferred relationships involving `UnitOfWorkFactory` (e.g. with `AccountService` and `ApiKeyService`) actually correct?**
  _`UnitOfWorkFactory` has 25 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08470588235294117 - nodes in this community are weakly interconnected._