# Graph Report - avant-api  (2026-10-29)

## Corpus Check
- 201 files · ~58,696 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2464 nodes · 6275 edges · 142 communities (78 shown, 64 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1009 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3382e2f8`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_internal.py
- contracts/controller.py
- roles/controller.py
- sites/controller.py
- Actor
- Services
- events.py
- GoogleService
- steps
- NetworkService
- Avant: models do MVP
- _member_client
- company/controller.py
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
- GoalTemplateOut
- UnitOfWorkFactory
- Avant: conexão com o GAM
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- test_internal.py
- ready
- session-start.sh
- avant-api
- clients/controller.py
- _onboard_owner
- main.py
- CapturingMailer
- test_account.py
- SessionCookies
- test_costs_results.py
- errors.py
- ReportService
- InvitationOut
- AccountService
- limits.py
- google.py
- .of
- export.py
- .uow
- mine
- edit
- currencies/controller.py
- account/controller.py
- .build
- conftest.py
- AdUnitOut
- do_reset_password
- test_events.py
- SiteService
- reports/service.py
- Actor
- people/controller.py
- mcm/controller.py
- TaskQueue
- .of
- reports/controller.py
- Limiter
- .uow
- connect
- SessionCookies
- avant-api
- sites/dto.py
- uuid
- audit/controller.py
- FakeGoogle
- SiteOut
- SiteListOut
- networks/service.py
- ClientService
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- goals/controller.py
- team
- .to_data
- .authenticate
- image_response
- profile/controller.py
- test_sites.py
- goals/dto.py
- pytest
- google/controller.py
- sync_runs
- Counter
- events
- clients
- images.py
- templates
- .trusted_uow
- GoalService
- invite_owner
- client_info
- delete_template
- source_files

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 93 edges
2. `Services` - 87 edges
3. `_onboard_owner()` - 85 edges
4. `UnitOfWorkFactory` - 82 edges
5. `_csrf()` - 75 edges
6. `ItemsOut` - 57 edges
7. `ReportService` - 49 edges
8. `ClientService` - 48 edges
9. `_member_client()` - 36 edges
10. `get_services()` - 32 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/modules/company/controller.py
- `Imagem da Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/08-grupos-e-imagem-da-empresa.md → src/avant_api/modules/company/controller.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (142 total, 64 thin omitted)

### Community 0 - "test_internal.py"
Cohesion: 0.20
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 1 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "sites/controller.py"
Cohesion: 0.16
Nodes (7): ad_units(), assign_sites(), delete(), index(), members(), show(), sites_of_member()

### Community 4 - "Actor"
Cohesion: 0.16
Nodes (6): audit(), cancel_owner(), client_image(), client_teams(), owner_invitations(), remove_client_image()

### Community 5 - "Services"
Cohesion: 0.06
Nodes (15): Services, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_services(), get_session_actor() (+7 more)

### Community 6 - "events.py"
Cohesion: 0.16
Nodes (5): channel(), EventSource, _parse(), sse(), EventService

### Community 7 - "GoogleService"
Cohesion: 0.08
Nodes (3): GoogleUnavailable, GoogleAuth, GoogleService

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "NetworkService"
Cohesion: 0.19
Nodes (3): index(), NetworkDetailOut, NetworkService

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.21
Nodes (9): _membership_ids(), test_groups_lifecycle(), _member_client(), test_audit_log(), test_company_and_members(), test_leave_company(), test_requires_session(), test_resend_and_cancel_invitation() (+1 more)

### Community 12 - "company/controller.py"
Cohesion: 0.07
Nodes (13): edit(), edit_fiscal(), edit_image(), fiscal(), image(), remove_image(), show(), company_service() (+5 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), remove(), remove_member(), show(), group_service() (+6 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "avant_core_access_models"
Cohesion: 0.07
Nodes (8): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, default_period(), ResultService

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

### Community 23 - "GoalTemplateOut"
Cohesion: 0.18
Nodes (3): create_template(), GoalTemplateIn, GoalTemplateOut

### Community 24 - "UnitOfWorkFactory"
Cohesion: 0.07
Nodes (8): UnitOfWorkFactory, AuditService, InvitationPreviewOut, ClientMemberOut, AuditOut, image_url(), MemberOut, RoleRefOut

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
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "test_internal.py"
Cohesion: 0.25
Nodes (9): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal(), _staff(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_internal_clients() (+1 more)

### Community 31 - "ready"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 36 - "clients/controller.py"
Cohesion: 0.14
Nodes (8): change_status(), edit_client(), edit_client_image(), ClientIn, ClientOut, ClientPatchIn, ClientStatusIn, OwnerChangeIn

### Community 37 - "_onboard_owner"
Cohesion: 0.20
Nodes (11): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format() (+3 more)

### Community 38 - "main.py"
Cohesion: 0.08
Nodes (6): configure_logging(), JsonFormatter, Settings, create_app(), google_redirects(), GoogleRedirects

### Community 39 - "CapturingMailer"
Cohesion: 0.33
Nodes (7): CapturingMailer, _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 40 - "test_account.py"
Cohesion: 0.36
Nodes (5): _google_round(), _login(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 41 - "SessionCookies"
Cohesion: 0.10
Nodes (4): SessionCookies, get_cookies(), accept(), verify()

### Community 42 - "test_costs_results.py"
Cohesion: 0.15
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 43 - "errors.py"
Cohesion: 0.12
Nodes (10): CsrfFailed, error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), NoActiveCompany (+2 more)

### Community 44 - "ReportService"
Cohesion: 0.16
Nodes (5): create(), update(), SavedReportIn, SavedReportOut, ReportService

### Community 45 - "InvitationOut"
Cohesion: 0.05
Nodes (13): invite(), staff(), staff_service(), StaffInviteIn, StaffService, cancel(), create_invitation(), list_invitations() (+5 more)

### Community 46 - "AccountService"
Cohesion: 0.16
Nodes (4): do_change_password(), get_sessions(), revoke_others(), AccountService

### Community 47 - "limits.py"
Cohesion: 0.08
Nodes (9): Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket() (+1 more)

### Community 48 - "google.py"
Cohesion: 0.12
Nodes (7): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 49 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 50 - "export.py"
Cohesion: 0.08
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 51 - ".uow"
Cohesion: 0.09
Nodes (3): ReportQueryIn, ReportResultOut, _statement_timeout()

### Community 52 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (16): API first e chaves de API, Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa (+8 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.10
Nodes (8): observe(), _route_template(), list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "account/controller.py"
Cohesion: 0.23
Nodes (6): account_service(), ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut, SessionOut

### Community 56 - ".build"
Cohesion: 0.06
Nodes (6): _google(), _mailer(), NoEvents, MemoryCounter, CeleryQueue, RecordingQueue

### Community 57 - "conftest.py"
Cohesion: 0.13
Nodes (9): client(), engine(), mailer(), Sent, _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys() (+1 more)

### Community 60 - "test_events.py"
Cohesion: 0.28
Nodes (6): _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 61 - "SiteService"
Cohesion: 0.19
Nodes (3): site_service(), SiteMemberOut, SiteService

### Community 62 - "reports/service.py"
Cohesion: 0.06
Nodes (13): QueryTooHeavy, catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut (+5 more)

### Community 63 - "Actor"
Cohesion: 0.21
Nodes (3): role_goals(), templates(), RoleGoalOut

### Community 64 - "people/controller.py"
Cohesion: 0.08
Nodes (12): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PersonOut (+4 more)

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "TaskQueue"
Cohesion: 0.12
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskQueue, enqueue_sync()

### Community 68 - "reports/controller.py"
Cohesion: 0.11
Nodes (10): create_from_template(), delete(), duplicate(), export(), export_saved(), index(), query(), run() (+2 more)

### Community 69 - "Limiter"
Cohesion: 0.19
Nodes (5): Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - ".uow"
Cohesion: 0.06
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+6 more)

### Community 71 - "connect"
Cohesion: 0.16
Nodes (6): connect(), disconnect(), service_account(), show(), sync(), network_service()

### Community 72 - "SessionCookies"
Cohesion: 0.12
Nodes (12): company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), AcceptInvitationIn, ActiveCompanyIn (+4 more)

### Community 74 - "sites/dto.py"
Cohesion: 0.27
Nodes (3): AdUnitPatchIn, MemberSitesIn, SiteIn

### Community 75 - "uuid"
Cohesion: 0.29
Nodes (15): test_change_password_and_sessions(), _csrf(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused() (+7 more)

### Community 76 - "audit/controller.py"
Cohesion: 0.12
Nodes (6): require(), dependency(), require_session(), require_staff(), index(), audit_service()

### Community 81 - "ClientService"
Cohesion: 0.17
Nodes (4): client(), client_service(), ClientDetailOut, ClientService

### Community 82 - "test_company_image.py"
Cohesion: 0.16
Nodes (7): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.20
Nodes (9): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Imagem da Empresa, Issues, Modelo de dados, Regras, Resumo (+1 more)

### Community 84 - "goals/controller.py"
Cohesion: 0.27
Nodes (3): set_role_goal(), update_template(), RoleGoalIn

### Community 91 - "profile/controller.py"
Cohesion: 0.08
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 92 - "test_sites.py"
Cohesion: 0.39
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 95 - "pytest"
Cohesion: 0.24
Nodes (5): RedisEvents, test_redis_source_delivers_published_messages(), run(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 96 - "google/controller.py"
Cohesion: 0.10
Nodes (6): new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), GoogleStatusOut

### Community 132 - ".trusted_uow"
Cohesion: 0.12
Nodes (3): resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 134 - "invite_owner"
Cohesion: 0.29
Nodes (3): invite_owner(), new_owner(), register_client()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1149 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **64 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `.__init__`, `roles/controller.py`, `.trusted_uow`, `GoalService`, `GoogleService`, `.__init__`, `NetworkService`, `company/controller.py`, `.uow`, `api_keys/controller.py`, `avant_core_access_models`, `.__init__`, `custom_metrics/controller.py`, `costs/controller.py`, `mfa/controller.py`, `ReportService`, `InvitationOut`, `AccountService`, `currencies/controller.py`, `account/controller.py`, `SiteService`, `reports/service.py`, `people/controller.py`, `mcm/controller.py`, `TaskQueue`, `.uow`, `sites/dto.py`, `networks/service.py`, `ClientService`, `.__init__`, `.authenticate`, `profile/controller.py`, `goals/dto.py`?**
  _High betweenness centrality (0.132) - this node is a cross-community bridge._
- **Are the 68 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 68 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06572769953051644 - nodes in this community are weakly interconnected._
- **Why does `ItemsOut` connect `ItemsOut` to `clients`, `contracts/controller.py`, `roles/controller.py`, `templates`, `Actor`, `.trusted_uow`, `sites/controller.py`, `NetworkService`, `.uow`, `api_keys/controller.py`, `avant_core_access_models`, `custom_metrics/controller.py`, `costs/controller.py`, `UnitOfWorkFactory`, `clients/controller.py`, `InvitationOut`, `Actor`, `people/controller.py`, `mcm/controller.py`, `reports/controller.py`, `.uow`, `connect`, `audit/controller.py`, `ClientService`, `goals/controller.py`, `sync_runs`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Are the 53 inferred relationships involving `Services` (e.g. with `Estrutura` and `EventSource`) actually correct?**
  _`Services` has 53 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07743496672716274 - nodes in this community are weakly interconnected._