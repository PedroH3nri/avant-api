# Graph Report - avant-api  (2026-10-29)

## Corpus Check
- 201 files · ~59,771 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2496 nodes · 6420 edges · 155 communities (74 shown, 81 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1041 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `65ab8353`
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
- shared/dto.py
- Avant: conexão com o GAM
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- test_goals.py
- health/controller.py
- .of
- session-start.sh
- avant-api
- NetworkDetailOut
- conftest.py
- Services
- test_account.py
- verify
- test_costs_results.py
- install
- SavedReportOut
- invitations/controller.py
- CapturingMailer
- limits.py
- google.py
- .of
- export.py
- CompanyService
- edit
- currencies/controller.py
- AccountService
- auth/controller.py
- conftest.py
- avant_core_access_models
- account/controller.py
- networks/service.py
- page_out
- BaseModel
- ReportService
- PeopleService
- mcm/controller.py
- _onboard_owner
- reports/controller.py
- Limiter
- .uow
- PageOut
- SessionCookies
- avant-api
- TaskQueue
- uuid
- audit/controller.py
- google_callback
- tasks.py
- .show
- UnitOfWorkFactory
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- .update_fiscal
- image
- templates
- .authenticate
- image_response
- profile/controller.py
- Counter
- do_reset_password
- RedisEvents
- OwnerInvitationOut
- MemoryCounter
- .page_saved
- google/controller.py
- .trusted_uow
- image
- delete_session
- reports/service.py
- source_files
- test_groups_lifecycle
- AuditService

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 96 edges
2. `_onboard_owner()` - 88 edges
3. `Services` - 87 edges
4. `UnitOfWorkFactory` - 82 edges
5. `_csrf()` - 77 edges
6. `PageOut` - 55 edges
7. `ReportService` - 51 edges
8. `ClientService` - 48 edges
9. `ItemsOut` - 43 edges
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

## Communities (155 total, 81 thin omitted)

### Community 0 - "test_internal.py"
Cohesion: 0.14
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _staff(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_internal_clients() (+6 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (24): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, contract(), contract_networks() (+16 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "sites/controller.py"
Cohesion: 0.05
Nodes (25): Atribuição de sites, GAM, Networks, Sites e ad units, ad_units(), assign_sites(), create(), delete() (+17 more)

### Community 4 - "Actor"
Cohesion: 0.10
Nodes (10): cancel_owner(), change_status(), client(), client_image(), clients(), edit_client_image(), invite_owner(), new_owner() (+2 more)

### Community 5 - "security.py"
Cohesion: 0.09
Nodes (15): CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor() (+7 more)

### Community 6 - "test_events.py"
Cohesion: 0.13
Nodes (10): channel(), EventSource, _parse(), sse(), _collect(), _event(), ListEvents, test_events_route() (+2 more)

### Community 7 - "GoogleService"
Cohesion: 0.08
Nodes (6): GoogleUnavailable, GoogleAuth, google_start(), google_status(), google_unlink(), GoogleService

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "UserOut"
Cohesion: 0.15
Nodes (4): person_out(), edit_image(), remove_image(), UserOut

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.22
Nodes (10): _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _member_client(), test_audit_log(), test_company_and_members(), test_leave_company(), test_requires_session() (+2 more)

### Community 12 - "company/controller.py"
Cohesion: 0.23
Nodes (4): company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

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
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "avant_core_access_models"
Cohesion: 0.09
Nodes (7): results(), client_result_service(), ClientResultService, result_service(), ResultsOut, default_period(), ResultService

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

### Community 23 - "goals/controller.py"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), templates() (+10 more)

### Community 24 - "shared/dto.py"
Cohesion: 0.10
Nodes (17): audit(), client_teams(), client_service(), ClientDetailOut, ClientIn, ClientMemberOut, ClientPatchIn, ClientProfileIn (+9 more)

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
Cohesion: 0.10
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "test_goals.py"
Cohesion: 0.53
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 31 - "health/controller.py"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 37 - "conftest.py"
Cohesion: 0.12
Nodes (9): client(), engine(), mailer(), test_costs_and_reports_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_role_options_are_light() (+1 more)

### Community 38 - "Services"
Cohesion: 0.06
Nodes (11): _google(), _mailer(), Services, NoEvents, GoogleOAuth, PillowImageProcessor, Bucket, Settings (+3 more)

### Community 40 - "test_account.py"
Cohesion: 0.35
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 42 - "test_costs_results.py"
Cohesion: 0.11
Nodes (8): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query(), _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 43 - "install"
Cohesion: 0.15
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "SavedReportOut"
Cohesion: 0.18
Nodes (3): create(), SavedReportIn, SavedReportOut

### Community 45 - "invitations/controller.py"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 46 - "CapturingMailer"
Cohesion: 0.33
Nodes (7): CapturingMailer, _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 47 - "limits.py"
Cohesion: 0.08
Nodes (8): BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 48 - "google.py"
Cohesion: 0.10
Nodes (7): GoogleFailed, challenge(), _claims(), identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 49 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 50 - "export.py"
Cohesion: 0.06
Nodes (14): observe(), _route_template(), dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv() (+6 more)

### Community 52 - "CompanyService"
Cohesion: 0.20
Nodes (3): remove_image(), CompanyDetailOut, CompanyService

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "AccountService"
Cohesion: 0.16
Nodes (4): do_change_password(), get_sessions(), revoke_others(), AccountService

### Community 56 - "auth/controller.py"
Cohesion: 0.17
Nodes (7): auth_service(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut

### Community 57 - "conftest.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 58 - "avant_core_access_models"
Cohesion: 0.16
Nodes (3): events(), event_service(), EventService

### Community 59 - "account/controller.py"
Cohesion: 0.25
Nodes (6): account_service(), ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut, SessionOut

### Community 60 - "networks/service.py"
Cohesion: 0.18
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 62 - "BaseModel"
Cohesion: 0.09
Nodes (9): CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+1 more)

### Community 63 - "ReportService"
Cohesion: 0.20
Nodes (5): query(), report_service(), ReportQueryIn, ReportResultOut, ReportService

### Community 64 - "PeopleService"
Cohesion: 0.12
Nodes (6): disable(), enable(), reset_mfa(), people_service(), PersonOut, PeopleService

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "_onboard_owner"
Cohesion: 0.24
Nodes (9): Sent, _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow() (+1 more)

### Community 68 - "reports/controller.py"
Cohesion: 0.12
Nodes (9): catalog(), create_from_template(), delete(), duplicate(), export(), export_saved(), run(), show() (+1 more)

### Community 69 - "Limiter"
Cohesion: 0.17
Nodes (6): TooManyAttempts, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - ".uow"
Cohesion: 0.07
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+6 more)

### Community 71 - "PageOut"
Cohesion: 0.14
Nodes (11): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+3 more)

### Community 72 - "SessionCookies"
Cohesion: 0.10
Nodes (8): SessionCookies, accept(), company_image(), do_logout(), login(), me(), set_active_company(), MeOut

### Community 75 - "uuid"
Cohesion: 0.31
Nodes (14): _csrf(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+6 more)

### Community 76 - "audit/controller.py"
Cohesion: 0.13
Nodes (3): get_services(), index(), audit_service()

### Community 82 - "test_company_image.py"
Cohesion: 0.31
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 91 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 95 - "RedisEvents"
Cohesion: 0.24
Nodes (5): RedisEvents, test_redis_source_delivers_published_messages(), run(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 96 - "OwnerInvitationOut"
Cohesion: 0.32
Nodes (3): owner_invitations(), OwnerInvitationOut, owner_invitation_out()

### Community 129 - "google/controller.py"
Cohesion: 0.10
Nodes (6): new_verifier(), get_cookies(), google_redirects(), google_service(), GoogleStatusOut, GoogleRedirects

### Community 132 - ".trusted_uow"
Cohesion: 0.10
Nodes (4): edit_client(), register_client(), ClientOut, ClientService

### Community 133 - "image"
Cohesion: 0.18
Nodes (3): fiscal(), image(), show()

### Community 136 - "reports/service.py"
Cohesion: 0.11
Nodes (4): QueryTooHeavy, RateLimited, ReportCountsOut, _statement_timeout()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1166 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **81 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `.__init__`, `.__init__`, `.trusted_uow`, `roles/controller.py`, `sites/controller.py`, `.__init__`, `GoogleService`, `reports/service.py`, `.__init__`, `company/controller.py`, `.uow`, `MemberOut`, `AuditService`, `api_keys/controller.py`, `.__init__`, `.__init__`, `custom_metrics/controller.py`, `.__init__`, `.__init__`, `costs/controller.py`, `goals/controller.py`, `shared/dto.py`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `mfa/controller.py`, `.__init__`, `.__init__`, `invitations/controller.py`, `.uow`, `CompanyService`, `currencies/controller.py`, `AccountService`, `auth/controller.py`, `account/controller.py`, `networks/service.py`, `ReportService`, `PeopleService`, `mcm/controller.py`, `.uow`, `PageOut`, `TaskQueue`, `audit/controller.py`, `ports.py`, `avant_core_access_models`, `.authenticate`, `profile/controller.py`, `.__init__`?**
  _High betweenness centrality (0.157) - this node is a cross-community bridge._
- **Are the 71 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 71 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_internal.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14408602150537633 - nodes in this community are weakly interconnected._
- **Why does `Services` connect `Services` to `contracts/controller.py`, `google/controller.py`, `roles/controller.py`, `sites/controller.py`, `security.py`, `test_events.py`, `GoogleService`, `company/controller.py`, `.uow`, `MemberOut`, `api_keys/controller.py`, `avant_core_access_models`, `custom_metrics/controller.py`, `costs/controller.py`, `goals/controller.py`, `shared/dto.py`, `mfa/controller.py`, `health/controller.py`, `conftest.py`, `invitations/controller.py`, `limits.py`, `currencies/controller.py`, `auth/controller.py`, `avant_core_access_models`, `account/controller.py`, `ReportService`, `PeopleService`, `mcm/controller.py`, `Limiter`, `.uow`, `PageOut`, `TaskQueue`, `audit/controller.py`, `profile/controller.py`, `RedisEvents`, `MemoryCounter`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Services` (e.g. with `Estrutura` and `EventSource`) actually correct?**
  _`Services` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.060350877192982454 - nodes in this community are weakly interconnected._