# Graph Report - avant-api  (2026-10-29)

## Corpus Check
- 200 files · ~58,218 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2446 nodes · 6207 edges · 133 communities (73 shown, 60 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 994 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `cd21dbc2`
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
- _staff
- ready
- main.py
- session-start.sh
- avant-api
- shared/dto.py
- _onboard_owner
- UserOut
- CapturingMailer
- test_account.py
- _marketing_client
- conftest.py
- errors.py
- users
- InvitationOut
- account/controller.py
- limits.py
- test_events.py
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
- CompanyFiscalOut
- .update_fiscal
- test_sites.py
- reports/service.py
- list_currencies
- people/controller.py
- mcm/controller.py
- TaskQueue
- reports/controller.py
- Limiter
- BaseModel
- connect
- SessionCookies
- avant-api
- company/controller.py
- uuid
- image
- FakeGoogle
- test_groups_lifecycle
- ._run
- networks/service.py
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- clients
- reports/dependencies.py
- image_response
- profile/controller.py
- edit_fiscal
- google/controller.py
- networks/dependencies.py
- is_exempt
- templates
- ClientService
- image

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 89 edges
2. `Services` - 87 edges
3. `UnitOfWorkFactory` - 82 edges
4. `_onboard_owner()` - 81 edges
5. `_csrf()` - 75 edges
6. `ItemsOut` - 56 edges
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

## Communities (133 total, 60 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.22
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

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
Nodes (10): cancel_owner(), change_status(), client(), edit_client(), edit_client_image(), invite_owner(), new_owner(), register_client() (+2 more)

### Community 5 - "Services"
Cohesion: 0.06
Nodes (19): Services, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth() (+11 more)

### Community 6 - "events/controller.py"
Cohesion: 0.09
Nodes (7): channel(), EventSource, _parse(), sse(), events(), event_service(), EventService

### Community 7 - "GoogleService"
Cohesion: 0.08
Nodes (4): GoogleUnavailable, GoogleAuth, google_service(), GoogleService

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.22
Nodes (9): CapturingMailer, Sent, _member_client(), test_audit_log(), test_company_and_members(), test_leave_company(), test_requires_session(), test_resend_and_cancel_invitation() (+1 more)

### Community 12 - "CompanyService"
Cohesion: 0.21
Nodes (3): show(), CompanyDetailOut, CompanyService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), remove(), remove_member(), show(), group_service() (+6 more)

### Community 14 - "ItemsOut"
Cohesion: 0.11
Nodes (6): index(), audit_service(), AuditService, audit(), AuditOut, ItemsOut

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "avant_core_access_models"
Cohesion: 0.06
Nodes (10): results(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut (+2 more)

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

### Community 23 - "goals/controller.py"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), templates() (+10 more)

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.20
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "_staff"
Cohesion: 0.26
Nodes (9): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal(), _staff(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_internal_clients() (+1 more)

### Community 31 - "ready"
Cohesion: 0.13
Nodes (4): health(), metrics(), ready(), HealthService

### Community 32 - "main.py"
Cohesion: 0.12
Nodes (4): configure_logging(), observe(), _route_template(), create_app()

### Community 36 - "shared/dto.py"
Cohesion: 0.14
Nodes (11): ClientDetailOut, ClientIn, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn, OwnerChangeIn (+3 more)

### Community 37 - "_onboard_owner"
Cohesion: 0.23
Nodes (10): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format(), _png() (+2 more)

### Community 38 - "UserOut"
Cohesion: 0.17
Nodes (3): edit_image(), remove_image(), UserOut

### Community 39 - "CapturingMailer"
Cohesion: 0.47
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 40 - "test_account.py"
Cohesion: 0.32
Nodes (8): _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_id_token_claims(), test_login_attempts_are_limited()

### Community 41 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 42 - "conftest.py"
Cohesion: 0.13
Nodes (3): client(), engine(), mailer()

### Community 43 - "errors.py"
Cohesion: 0.12
Nodes (7): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), PillowImageProcessor

### Community 44 - "users"
Cohesion: 0.22
Nodes (4): Resumo, users(), PersonOut, person_out()

### Community 45 - "InvitationOut"
Cohesion: 0.06
Nodes (13): invite(), staff(), staff_service(), StaffInviteIn, StaffService, cancel(), create_invitation(), list_invitations() (+5 more)

### Community 46 - "account/controller.py"
Cohesion: 0.08
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 47 - "limits.py"
Cohesion: 0.08
Nodes (8): BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 48 - "test_events.py"
Cohesion: 0.28
Nodes (6): _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 49 - "MemberService"
Cohesion: 0.07
Nodes (14): edit(), index(), leave(), remove(), set_permissions(), show(), member_service(), DirectPermissionIn (+6 more)

### Community 50 - "export.py"
Cohesion: 0.07
Nodes (12): JsonFormatter, dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx() (+4 more)

### Community 51 - ".uow"
Cohesion: 0.13
Nodes (3): SavedReportIn, SavedReportOut, ReportService

### Community 52 - "ItemsOut"
Cohesion: 0.20
Nodes (6): client_teams(), client_service(), ClientMemberOut, ClientService, CompanyRefOut, RoleRefOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.18
Nodes (4): currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "auth/controller.py"
Cohesion: 0.06
Nodes (16): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+8 more)

### Community 56 - ".build"
Cohesion: 0.06
Nodes (11): _google(), _mailer(), NoEvents, RedisEvents, MemoryCounter, CeleryQueue, RecordingQueue, test_redis_source_delivers_published_messages() (+3 more)

### Community 57 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 58 - "ReportQueryIn"
Cohesion: 0.14
Nodes (4): query(), ReportQueryIn, ReportResultOut, ReportRowOut

### Community 61 - "test_sites.py"
Cohesion: 0.29
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 62 - "reports/service.py"
Cohesion: 0.07
Nodes (7): Bucket, catalog(), CustomCatalogMetricOut, DimensionOut, LabelOut, MetricCatalogOut, MetricOut

### Community 64 - "people/controller.py"
Cohesion: 0.14
Nodes (5): disable(), enable(), reset_mfa(), people_service(), PeopleService

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 68 - "reports/controller.py"
Cohesion: 0.11
Nodes (10): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), run() (+2 more)

### Community 69 - "Limiter"
Cohesion: 0.10
Nodes (7): TooManyAttempts, Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "BaseModel"
Cohesion: 0.15
Nodes (5): FilterIn, OrderIn, PeriodIn, ReportRangeOut, SavedQueryOut

### Community 71 - "connect"
Cohesion: 0.18
Nodes (7): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs()

### Community 72 - "SessionCookies"
Cohesion: 0.11
Nodes (3): SessionCookies, get_cookies(), verify()

### Community 75 - "uuid"
Cohesion: 0.26
Nodes (16): _csrf(), _owner_invite(), test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx() (+8 more)

### Community 79 - "._run"
Cohesion: 0.17
Nodes (3): QueryTooHeavy, RateLimited, _statement_timeout()

### Community 80 - "networks/service.py"
Cohesion: 0.24
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 82 - "test_company_image.py"
Cohesion: 0.31
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 84 - "clients"
Cohesion: 0.20
Nodes (3): client_image(), clients(), owner_invitations()

### Community 89 - "image_response"
Cohesion: 0.16
Nodes (3): client_info(), image_response(), image_upload()

### Community 91 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 92 - "edit_fiscal"
Cohesion: 0.25
Nodes (3): edit_fiscal(), edit_image(), remove_image()

### Community 96 - "google/controller.py"
Cohesion: 0.05
Nodes (14): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), Settings, google_callback() (+6 more)

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1143 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **60 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `.__init__`, `contracts/controller.py`, `.__init__`, `roles/controller.py`, `ClientService`, `.__init__`, `sites/controller.py`, `GoogleService`, `NetworkService`, `CompanyService`, `.uow`, `ItemsOut`, `api_keys/controller.py`, `avant_core_access_models`, `custom_metrics/controller.py`, `costs/controller.py`, `goals/controller.py`, `mfa/controller.py`, `shared/dto.py`, `InvitationOut`, `account/controller.py`, `MemberService`, `.uow`, `ItemsOut`, `currencies/controller.py`, `auth/controller.py`, `reports/service.py`, `people/controller.py`, `mcm/controller.py`, `TaskQueue`, `Limiter`, `company/controller.py`, `networks/service.py`, `.__init__`, `.__init__`, `.__init__`, `profile/controller.py`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **Are the 65 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 65 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05744888023369036 - nodes in this community are weakly interconnected._
- **Why does `ItemsOut` connect `ItemsOut` to `contracts/controller.py`, `roles/controller.py`, `templates`, `sites/controller.py`, `.uow`, `api_keys/controller.py`, `avant_core_access_models`, `custom_metrics/controller.py`, `costs/controller.py`, `goals/controller.py`, `shared/dto.py`, `users`, `InvitationOut`, `MemberService`, `ItemsOut`, `people/controller.py`, `mcm/controller.py`, `reports/controller.py`, `connect`, `clients`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Services` (e.g. with `Estrutura` and `EventSource`) actually correct?**
  _`Services` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07744107744107744 - nodes in this community are weakly interconnected._