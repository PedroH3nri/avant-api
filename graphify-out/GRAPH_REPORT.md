# Graph Report - avant-api  (2026-10-29)

## Corpus Check
- 201 files · ~59,494 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2488 nodes · 6389 edges · 140 communities (75 shown, 65 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1037 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `369d7fa4`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_internal.py
- contracts/controller.py
- roles/controller.py
- sites/controller.py
- Actor
- security.py
- events.py
- GoogleService
- steps
- UserOut
- Avant: models do MVP
- _member_client
- company/controller.py
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
- fastapi
- BaseModel
- session-start.sh
- avant-api
- pytest
- _onboard_owner
- main.py
- google_callback
- test_account.py
- SessionCookies
- test_costs_results.py
- install
- ReportService
- invitations/controller.py
- CapturingMailer
- limits.py
- google.py
- google_status
- export.py
- .uow
- CompanyService
- edit
- currencies/controller.py
- AccountService
- Services
- conftest.py
- avant_core_access_models
- .of
- test_events.py
- shared/dto.py
- reports/service.py
- middleware.py
- PeopleService
- mcm/controller.py
- .of
- .of
- reports/controller.py
- Limiter
- .uow
- networks/controller.py
- auth/controller.py
- avant-api
- uuid
- audit/controller.py
- logs.py
- UnitOfWorkFactory
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- image
- NoEvents
- .authenticate
- image_response
- profile/controller.py
- test_sites.py
- edit_fiscal
- RedisEvents
- client_image
- MemoryCounter
- events
- ClientService
- avant_core_shared_clock
- .trusted_uow
- image
- edit_image
- RateLimited
- source_files

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 95 edges
2. `Services` - 87 edges
3. `_onboard_owner()` - 87 edges
4. `UnitOfWorkFactory` - 82 edges
5. `_csrf()` - 75 edges
6. `ReportService` - 49 edges
7. `ClientService` - 48 edges
8. `PageOut` - 48 edges
9. `ItemsOut` - 46 edges
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

## Communities (140 total, 65 thin omitted)

### Community 0 - "test_internal.py"
Cohesion: 0.15
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _staff(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_internal_clients() (+6 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (25): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem, health(), metrics(), contract() (+17 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "sites/controller.py"
Cohesion: 0.05
Nodes (25): Atribuição de sites, GAM, Networks, Sites e ad units, ad_units(), assign_sites(), create(), delete() (+17 more)

### Community 4 - "Actor"
Cohesion: 0.13
Nodes (9): cancel_owner(), change_status(), client(), edit_client_image(), invite_owner(), new_owner(), register_client(), remove_client_image() (+1 more)

### Community 5 - "security.py"
Cohesion: 0.09
Nodes (14): NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor(), get_session_auth() (+6 more)

### Community 6 - "events.py"
Cohesion: 0.23
Nodes (3): channel(), _parse(), sse()

### Community 7 - "GoogleService"
Cohesion: 0.12
Nodes (3): GoogleUnavailable, GoogleAuth, GoogleService

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "UserOut"
Cohesion: 0.17
Nodes (4): PersonOut, person_out(), CompanyRefOut, UserOut

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.17
Nodes (10): test_events_route(), _membership_ids(), test_groups_lifecycle(), _member_client(), test_audit_log(), test_company_and_members(), test_leave_company(), test_requires_session() (+2 more)

### Community 12 - "company/controller.py"
Cohesion: 0.30
Nodes (4): CompanyDetailOut, CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "MemberOut"
Cohesion: 0.15
Nodes (6): invite(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

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
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), templates() (+10 more)

### Community 24 - "clients/controller.py"
Cohesion: 0.20
Nodes (10): client_service(), ClientDetailOut, ClientIn, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn (+2 more)

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "test_reports.py"
Cohesion: 0.23
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (7): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "test_goals.py"
Cohesion: 0.43
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 31 - "fastapi"
Cohesion: 0.07
Nodes (6): google_redirects(), google_service(), ready(), health_service(), HealthService, people_service()

### Community 32 - "BaseModel"
Cohesion: 0.09
Nodes (8): templates(), FilterIn, OrderIn, PeriodIn, ReportRangeOut, ReportRowOut, ReportTemplateOut, SavedQueryOut

### Community 36 - "pytest"
Cohesion: 0.28
Nodes (4): client(), engine(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 37 - "_onboard_owner"
Cohesion: 0.21
Nodes (13): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format() (+5 more)

### Community 38 - "main.py"
Cohesion: 0.12
Nodes (5): _google(), _mailer(), configure_logging(), Settings, create_app()

### Community 39 - "google_callback"
Cohesion: 0.14
Nodes (4): new_verifier(), google_callback(), google_start(), GoogleRedirects

### Community 40 - "test_account.py"
Cohesion: 0.35
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 41 - "SessionCookies"
Cohesion: 0.12
Nodes (3): SessionCookies, do_logout(), verify()

### Community 42 - "test_costs_results.py"
Cohesion: 0.16
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 43 - "install"
Cohesion: 0.20
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 45 - "invitations/controller.py"
Cohesion: 0.10
Nodes (9): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut (+1 more)

### Community 46 - "CapturingMailer"
Cohesion: 0.27
Nodes (7): CapturingMailer, _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 47 - "limits.py"
Cohesion: 0.07
Nodes (9): Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket() (+1 more)

### Community 48 - "google.py"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 49 - "google_status"
Cohesion: 0.13
Nodes (3): google_status(), google_unlink(), GoogleStatusOut

### Community 50 - "export.py"
Cohesion: 0.08
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 51 - ".uow"
Cohesion: 0.11
Nodes (5): query(), ReportQueryIn, ReportResultOut, ReportService, _statement_timeout()

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "AccountService"
Cohesion: 0.08
Nodes (12): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn (+4 more)

### Community 56 - "Services"
Cohesion: 0.06
Nodes (11): Estrutura, Services, get_services(), CeleryQueue, RecordingQueue, TaskQueue, account_service(), auth_service() (+3 more)

### Community 57 - "conftest.py"
Cohesion: 0.15
Nodes (7): mailer(), Sent, _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 58 - "avant_core_access_models"
Cohesion: 0.23
Nodes (3): EventSource, event_service(), EventService

### Community 59 - ".of"
Cohesion: 0.14
Nodes (3): index(), options(), RoleRefOut

### Community 60 - "test_events.py"
Cohesion: 0.38
Nodes (5): _collect(), _event(), ListEvents, test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 62 - "reports/service.py"
Cohesion: 0.08
Nodes (6): catalog(), CustomCatalogMetricOut, DimensionOut, LabelOut, MetricCatalogOut, MetricOut

### Community 64 - "PeopleService"
Cohesion: 0.13
Nodes (7): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), PeopleService

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (6): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService

### Community 68 - "reports/controller.py"
Cohesion: 0.11
Nodes (10): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), run() (+2 more)

### Community 69 - "Limiter"
Cohesion: 0.10
Nodes (7): TooManyAttempts, Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - ".uow"
Cohesion: 0.10
Nodes (12): edit(), leave(), remove(), set_permissions(), show(), member_service(), DirectPermissionIn, DirectPermissionOut (+4 more)

### Community 71 - "networks/controller.py"
Cohesion: 0.05
Nodes (16): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+8 more)

### Community 72 - "auth/controller.py"
Cohesion: 0.10
Nodes (15): accept(), company_image(), get_invitation(), login(), me(), set_active_company(), AcceptInvitationIn, ActiveCompanyIn (+7 more)

### Community 75 - "uuid"
Cohesion: 0.31
Nodes (14): _csrf(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+6 more)

### Community 76 - "audit/controller.py"
Cohesion: 0.13
Nodes (3): index(), audit_service(), AuditService

### Community 82 - "test_company_image.py"
Cohesion: 0.16
Nodes (7): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 91 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 92 - "test_sites.py"
Cohesion: 0.39
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 94 - "edit_fiscal"
Cohesion: 0.16
Nodes (5): edit_fiscal(), edit_image(), fiscal(), remove_image(), show()

### Community 95 - "RedisEvents"
Cohesion: 0.47
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 128 - "ClientService"
Cohesion: 0.16
Nodes (8): audit(), client_teams(), clients(), owner_invitations(), ClientMemberOut, ClientService, AuditOut, ItemsOut

### Community 129 - "avant_core_shared_clock"
Cohesion: 0.11
Nodes (4): PillowImageProcessor, get_cookies(), mfa_service(), MfaService

### Community 136 - "RateLimited"
Cohesion: 0.29
Nodes (3): CsrfFailed, QueryTooHeavy, RateLimited

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1162 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **65 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `ClientService`, `contracts/controller.py`, `.__init__`, `avant_core_shared_clock`, `.trusted_uow`, `.__init__`, `roles/controller.py`, `GoogleService`, `sites/controller.py`, `UserOut`, `.__init__`, `company/controller.py`, `.uow`, `MemberOut`, `api_keys/controller.py`, `avant_core_access_models`, `custom_metrics/controller.py`, `costs/controller.py`, `goals/controller.py`, `clients/controller.py`, `ReportService`, `invitations/controller.py`, `limits.py`, `.uow`, `CompanyService`, `currencies/controller.py`, `AccountService`, `reports/service.py`, `PeopleService`, `mcm/controller.py`, `Limiter`, `.uow`, `networks/controller.py`, `auth/controller.py`, `audit/controller.py`, `ports.py`, `.authenticate`, `profile/controller.py`, `.__init__`?**
  _High betweenness centrality (0.151) - this node is a cross-community bridge._
- **Are the 70 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 70 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_internal.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14838709677419354 - nodes in this community are weakly interconnected._
- **Why does `Services` connect `Services` to `avant_core_shared_clock`, `contracts/controller.py`, `roles/controller.py`, `sites/controller.py`, `security.py`, `GoogleService`, `.uow`, `MemberOut`, `api_keys/controller.py`, `avant_core_access_models`, `custom_metrics/controller.py`, `goals/controller.py`, `clients/controller.py`, `fastapi`, `pytest`, `main.py`, `invitations/controller.py`, `limits.py`, `currencies/controller.py`, `avant_core_access_models`, `mcm/controller.py`, `Limiter`, `.uow`, `networks/controller.py`, `audit/controller.py`, `NoEvents`, `profile/controller.py`, `RedisEvents`, `MemoryCounter`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Services` (e.g. with `Estrutura` and `EventSource`) actually correct?**
  _`Services` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05506329113924051 - nodes in this community are weakly interconnected._