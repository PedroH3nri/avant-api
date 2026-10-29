# Graph Report - avant-api  (2026-10-29)

## Corpus Check
- 194 files · ~56,568 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2345 nodes · 5943 edges · 137 communities (73 shown, 64 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 946 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6e86840d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- sites/controller.py
- Actor
- Services
- events/controller.py
- google/controller.py
- steps
- NetworkService
- Avant: models do MVP
- _member_client
- CompanyService
- .uow
- audit/controller.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- avant_core_access_models
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- results
- UnitOfWorkFactory
- Avant: conexão com o GAM
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- google/controller.py
- ready
- main.py
- session-start.sh
- avant-api
- clients/controller.py
- modules/results/dependencies.py
- UserOut
- CapturingMailer
- test_account.py
- MemberOut
- test_costs_results.py
- install
- internal/results/dependencies.py
- InvitationOut
- account/controller.py
- limits.py
- conftest.py
- MemberService
- export.py
- .uow
- ItemsOut
- edit
- currencies/controller.py
- auth/controller.py
- .build
- test_api_keys.py
- ReportQueryIn
- enqueue_sync
- test_sites.py
- reports/service.py
- .of
- people/controller.py
- mcm/controller.py
- container.py
- RedisCounter
- reports/controller.py
- Limiter
- BaseModel
- connect
- avant-api
- company/controller.py
- uuid
- image
- MemoryBucket
- ItemsOut
- main.py
- networks/service.py
- Counter
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- ClientOut
- .show
- RedisBucket
- MemoryCounter
- index
- image_response
- edit_image
- profile/controller.py
- edit_fiscal
- google_callback
- networks/dependencies.py
- is_exempt
- SavedReportOut
- ReportService
- ClientService
- image

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 87 edges
2. `Services` - 85 edges
3. `UnitOfWorkFactory` - 79 edges
4. `_onboard_owner()` - 79 edges
5. `_csrf()` - 72 edges
6. `ItemsOut` - 53 edges
7. `ReportService` - 49 edges
8. `ClientService` - 48 edges
9. `_member_client()` - 36 edges
10. `get_services()` - 31 edges

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

## Communities (137 total, 64 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.17
Nodes (15): _csrf(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _staff(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client() (+7 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (11): create(), edit(), index(), permissions(), remove(), role_service(), PermissionOut, RoleIn (+3 more)

### Community 3 - "sites/controller.py"
Cohesion: 0.06
Nodes (23): Atribuição de sites, GAM, Networks, Sites e ad units, ad_units(), assign_sites(), create(), delete() (+15 more)

### Community 4 - "Actor"
Cohesion: 0.15
Nodes (6): cancel_owner(), change_status(), client_image(), edit_client(), edit_client_image(), remove_client_image()

### Community 5 - "Services"
Cohesion: 0.05
Nodes (18): Services, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_services(), get_session_actor() (+10 more)

### Community 6 - "events/controller.py"
Cohesion: 0.11
Nodes (6): channel(), EventSource, _parse(), sse(), events(), EventService

### Community 7 - "google/controller.py"
Cohesion: 0.07
Nodes (8): _google(), GoogleFailed, challenge(), _claims(), GoogleAuth, GoogleOAuth, identity_from_id_token(), FakeGoogle

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.19
Nodes (10): _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _member_client(), test_audit_log(), test_company_and_members(), test_leave_company(), test_requires_session() (+2 more)

### Community 12 - "CompanyService"
Cohesion: 0.21
Nodes (3): show(), CompanyDetailOut, CompanyService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), remove(), remove_member(), show(), group_service() (+6 more)

### Community 14 - "audit/controller.py"
Cohesion: 0.17
Nodes (3): require(), index(), AuditService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "avant_core_access_models"
Cohesion: 0.15
Nodes (5): CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut, default_period()

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

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

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.22
Nodes (10): _day(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission(), test_query_refuses_bad_definitions_and_internal_metrics() (+2 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "google/controller.py"
Cohesion: 0.10
Nodes (6): Settings, google_redirects(), google_service(), GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 31 - "ready"
Cohesion: 0.18
Nodes (3): health(), metrics(), ready()

### Community 32 - "main.py"
Cohesion: 0.10
Nodes (5): configure_logging(), JsonFormatter, observe(), _route_template(), create_app()

### Community 36 - "clients/controller.py"
Cohesion: 0.14
Nodes (11): invite_owner(), new_owner(), register_client(), resend_owner(), ClientIn, ClientPatchIn, ClientProfileIn, ClientProfileOut (+3 more)

### Community 37 - "modules/results/dependencies.py"
Cohesion: 0.13
Nodes (3): show(), result_service(), ResultService

### Community 38 - "UserOut"
Cohesion: 0.17
Nodes (3): PersonOut, person_out(), UserOut

### Community 39 - "CapturingMailer"
Cohesion: 0.47
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 40 - "test_account.py"
Cohesion: 0.33
Nodes (7): _google_round(), _jwt(), _login(), test_forgot_and_reset_password(), test_google_link_and_login(), test_id_token_claims(), test_login_attempts_are_limited()

### Community 41 - "MemberOut"
Cohesion: 0.15
Nodes (6): invite(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 42 - "test_costs_results.py"
Cohesion: 0.11
Nodes (14): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format(), _marketing_client() (+6 more)

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 45 - "InvitationOut"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 46 - "account/controller.py"
Cohesion: 0.08
Nodes (14): SessionCookies, get_cookies(), delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others() (+6 more)

### Community 47 - "limits.py"
Cohesion: 0.18
Nodes (3): TooManyAttempts, BucketResult, BucketRule

### Community 48 - "conftest.py"
Cohesion: 0.12
Nodes (9): client(), engine(), mailer(), _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit() (+1 more)

### Community 49 - "MemberService"
Cohesion: 0.10
Nodes (11): edit(), leave(), remove(), set_permissions(), show(), member_service(), DirectPermissionIn, MemberDetailOut (+3 more)

### Community 50 - "export.py"
Cohesion: 0.09
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 52 - "ItemsOut"
Cohesion: 0.23
Nodes (6): client_teams(), client_service(), ClientMemberOut, ClientService, CompanyRefOut, ItemsOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "auth/controller.py"
Cohesion: 0.06
Nodes (17): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+9 more)

### Community 56 - ".build"
Cohesion: 0.16
Nodes (5): _mailer(), NoEvents, RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 57 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 58 - "ReportQueryIn"
Cohesion: 0.18
Nodes (4): query(), ReportQueryIn, ReportResultOut, ReportRowOut

### Community 61 - "test_sites.py"
Cohesion: 0.29
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 62 - "reports/service.py"
Cohesion: 0.09
Nodes (4): CustomCatalogMetricOut, DimensionOut, LabelOut, MetricOut

### Community 64 - "people/controller.py"
Cohesion: 0.12
Nodes (7): Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PeopleService

### Community 65 - "mcm/controller.py"
Cohesion: 0.09
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "container.py"
Cohesion: 0.07
Nodes (9): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, PillowImageProcessor, CeleryQueue, RecordingQueue (+1 more)

### Community 68 - "reports/controller.py"
Cohesion: 0.11
Nodes (10): catalog(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), run() (+2 more)

### Community 69 - "Limiter"
Cohesion: 0.19
Nodes (4): Limiter, Rule, _limiter_round(), test_memory_limiter()

### Community 70 - "BaseModel"
Cohesion: 0.15
Nodes (5): FilterIn, OrderIn, PeriodIn, ReportRangeOut, SavedQueryOut

### Community 71 - "connect"
Cohesion: 0.18
Nodes (7): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs()

### Community 74 - "company/controller.py"
Cohesion: 0.20
Nodes (5): company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, FiscalDataOut

### Community 75 - "uuid"
Cohesion: 0.18
Nodes (18): CapturingMailer, Sent, test_change_password_and_sessions(), _owner_invite(), _metrics(), _ana_id(), _report(), test_chart_options_keep_metric_styles() (+10 more)

### Community 77 - "MemoryBucket"
Cohesion: 0.28
Nodes (4): MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 79 - "main.py"
Cohesion: 0.07
Nodes (7): CsrfFailed, GoogleUnavailable, NoActiveCompany, QueryTooHeavy, RateLimited, GoogleStatusOut, client_info()

### Community 80 - "networks/service.py"
Cohesion: 0.18
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 82 - "test_company_image.py"
Cohesion: 0.36
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 85 - ".show"
Cohesion: 0.29
Nodes (3): client(), owner_invitations(), ClientDetailOut

### Community 91 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 92 - "edit_fiscal"
Cohesion: 0.25
Nodes (3): edit_fiscal(), edit_image(), remove_image()

### Community 96 - "google_callback"
Cohesion: 0.07
Nodes (6): new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), GoogleService

### Community 130 - "SavedReportOut"
Cohesion: 0.15
Nodes (4): create(), update(), SavedReportIn, SavedReportOut

### Community 131 - "ReportService"
Cohesion: 0.16
Nodes (5): Bucket, templates(), report_service(), ReportTemplateOut, ReportService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1096 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **64 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `.__init__`, `contracts/controller.py`, `.__init__`, `ReportService`, `ClientService`, `.__init__`, `roles/controller.py`, `google/controller.py`, `sites/controller.py`, `NetworkService`, `CompanyService`, `.uow`, `audit/controller.py`, `api_keys/controller.py`, `avant_core_access_models`, `custom_metrics/controller.py`, `costs/controller.py`, `mfa/controller.py`, `modules/results/dependencies.py`, `UserOut`, `MemberOut`, `internal/results/dependencies.py`, `InvitationOut`, `account/controller.py`, `MemberService`, `.uow`, `ItemsOut`, `currencies/controller.py`, `auth/controller.py`, `reports/service.py`, `people/controller.py`, `mcm/controller.py`, `company/controller.py`, `main.py`, `networks/service.py`, `profile/controller.py`, `.__init__`, `google_callback`?**
  _High betweenness centrality (0.138) - this node is a cross-community bridge._
- **Are the 64 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 64 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06680080482897384 - nodes in this community are weakly interconnected._
- **Why does `Services` connect `Services` to `contracts/controller.py`, `roles/controller.py`, `ReportService`, `sites/controller.py`, `events/controller.py`, `google/controller.py`, `.uow`, `api_keys/controller.py`, `custom_metrics/controller.py`, `costs/controller.py`, `mfa/controller.py`, `google/controller.py`, `main.py`, `modules/results/dependencies.py`, `MemberOut`, `internal/results/dependencies.py`, `InvitationOut`, `account/controller.py`, `conftest.py`, `MemberService`, `ItemsOut`, `currencies/controller.py`, `auth/controller.py`, `.build`, `people/controller.py`, `mcm/controller.py`, `container.py`, `RedisCounter`, `Limiter`, `company/controller.py`, `MemoryBucket`, `main.py`, `RedisBucket`, `MemoryCounter`, `profile/controller.py`, `networks/dependencies.py`?**
  _High betweenness centrality (0.061) - this node is a cross-community bridge._
- **Are the 52 inferred relationships involving `Services` (e.g. with `Estrutura` and `EventSource`) actually correct?**
  _`Services` has 52 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07744107744107744 - nodes in this community are weakly interconnected._