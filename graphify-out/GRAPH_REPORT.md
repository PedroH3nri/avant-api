# Graph Report - avant-api  (2026-10-29)

## Corpus Check
- 201 files · ~60,432 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2510 nodes · 6514 edges · 139 communities (80 shown, 59 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1063 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `c576c237`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _enable
- contracts/controller.py
- roles/controller.py
- .uow
- Actor
- security.py
- events.py
- conftest.py
- steps
- shared/dto.py
- Avant: models do MVP
- _member_client
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
- clients/dto.py
- networks/controller.py
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- container.py
- fastapi
- ReportService
- session-start.sh
- avant-api
- NetworkService
- test_api_keys.py
- events/controller.py
- export.py
- test_account.py
- company/controller.py
- test_costs_results.py
- install
- _staff
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
- RedisCounter
- ItemsOut
- networks/service.py
- GoalTemplateOut
- .change_password
- test_sites.py
- mine
- goals/service.py
- PeopleService
- mcm/controller.py
- _onboard_owner
- tasks.py
- reports/controller.py
- Limiter
- .uow
- ReportResultOut
- SessionCookies
- avant-api
- TaskQueue
- uuid
- AuditService
- team
- AdUnitOut
- SiteService
- pytest
- GoogleService
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- edit_fiscal
- middleware.py
- templates
- auth/controller.py
- http.py
- profile/controller.py
- PageOut
- do_reset_password
- RateLimited
- source_files
- UnitOfWorkFactory
- .page_saved
- delete_session
- RoleGoalOut
- .trusted_uow
- image
- GoalService
- reports/service.py
- GoogleFailed
- CompanyService

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 99 edges
2. `PageOut` - 96 edges
3. `_onboard_owner()` - 91 edges
4. `Services` - 87 edges
5. `UnitOfWorkFactory` - 82 edges
6. `_csrf()` - 79 edges
7. `ClientService` - 51 edges
8. `ReportService` - 51 edges
9. `page_out()` - 41 edges
10. `_member_client()` - 38 edges

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

## Communities (139 total, 59 thin omitted)

### Community 0 - "_enable"
Cohesion: 0.22
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 1 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.11
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 4 - "Actor"
Cohesion: 0.08
Nodes (18): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), clients() (+10 more)

### Community 5 - "security.py"
Cohesion: 0.06
Nodes (19): Services, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_services() (+11 more)

### Community 6 - "events.py"
Cohesion: 0.16
Nodes (7): channel(), _parse(), sse(), _collect(), ListEvents, test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 7 - "conftest.py"
Cohesion: 0.12
Nodes (3): client(), engine(), mailer()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "shared/dto.py"
Cohesion: 0.10
Nodes (6): PersonOut, person_out(), CompanyRefOut, page_out(), RoleRefOut, UserOut

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.11
Nodes (14): _event(), test_events_route(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _member_client() (+6 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "MemberOut"
Cohesion: 0.12
Nodes (6): invite(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

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
Cohesion: 0.17
Nodes (6): delete_template(), role_goals(), set_role_goal(), template_options(), templates(), update_template()

### Community 24 - "clients/dto.py"
Cohesion: 0.11
Nodes (6): ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, FiscalDataOut, image_url()

### Community 25 - "networks/controller.py"
Cohesion: 0.15
Nodes (7): disconnect(), index(), service_account(), show(), sync(), sync_runs(), network_service()

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "test_reports.py"
Cohesion: 0.19
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.07
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "container.py"
Cohesion: 0.07
Nodes (8): _google(), _mailer(), NoEvents, MemoryCounter, Settings, CeleryQueue, RecordingQueue, create_app()

### Community 31 - "fastapi"
Cohesion: 0.06
Nodes (11): get_auth(), currency_service(), google_redirects(), google_service(), GoogleStatusOut, GoogleRedirects, health(), metrics() (+3 more)

### Community 32 - "ReportService"
Cohesion: 0.10
Nodes (6): Bucket, query(), ReportQueryIn, ReportResultOut, ReportService, _statement_timeout()

### Community 36 - "NetworkService"
Cohesion: 0.17
Nodes (4): connect(), options(), NetworkDetailOut, NetworkService

### Community 37 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 38 - "events/controller.py"
Cohesion: 0.14
Nodes (4): EventSource, events(), event_service(), EventService

### Community 39 - "export.py"
Cohesion: 0.07
Nodes (11): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+3 more)

### Community 40 - "test_account.py"
Cohesion: 0.57
Nodes (5): _google_round(), _login(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 41 - "company/controller.py"
Cohesion: 0.21
Nodes (4): company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 42 - "test_costs_results.py"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 43 - "install"
Cohesion: 0.20
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "_staff"
Cohesion: 0.29
Nodes (9): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal(), _staff(), test_client_owner_cannot_reach_internal(), test_client_teams_leave_out_the_groone_team(), test_fiscal_data_only_by_the_client(), test_internal_clients() (+1 more)

### Community 45 - "invitations/controller.py"
Cohesion: 0.11
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService, InvitationOut

### Community 46 - "CapturingMailer"
Cohesion: 0.22
Nodes (12): CapturingMailer, Sent, test_change_password_and_sessions(), test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team() (+4 more)

### Community 47 - "limits.py"
Cohesion: 0.11
Nodes (7): BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 48 - "google.py"
Cohesion: 0.17
Nodes (5): challenge(), _claims(), identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 49 - ".of"
Cohesion: 0.09
Nodes (4): show(), CostLineOut, MonthResultOut, ResultTotalsOut

### Community 50 - "sites/controller.py"
Cohesion: 0.18
Nodes (8): create(), site_service(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut

### Community 51 - "ReportService"
Cohesion: 0.11
Nodes (4): create(), update(), SavedReportIn, SavedReportOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "account/controller.py"
Cohesion: 0.25
Nodes (7): account_service(), ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut, SessionOut, AccountService

### Community 57 - "ItemsOut"
Cohesion: 0.14
Nodes (9): ad_units(), assign_sites(), delete(), index(), show(), site_options(), sites_of_member(), unlinked() (+1 more)

### Community 58 - "networks/service.py"
Cohesion: 0.24
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 59 - "GoalTemplateOut"
Cohesion: 0.16
Nodes (3): create_template(), GoalTemplateIn, GoalTemplateOut

### Community 60 - ".change_password"
Cohesion: 0.15
Nodes (3): do_change_password(), get_sessions(), revoke_others()

### Community 61 - "test_sites.py"
Cohesion: 0.53
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 62 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 64 - "PeopleService"
Cohesion: 0.08
Nodes (16): Modelo de dados, Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação (+8 more)

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "_onboard_owner"
Cohesion: 0.22
Nodes (14): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format() (+6 more)

### Community 68 - "reports/controller.py"
Cohesion: 0.11
Nodes (9): catalog(), create_from_template(), delete(), duplicate(), export(), export_saved(), run(), show() (+1 more)

### Community 69 - "Limiter"
Cohesion: 0.11
Nodes (7): TooManyAttempts, Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - ".uow"
Cohesion: 0.06
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+6 more)

### Community 72 - "SessionCookies"
Cohesion: 0.10
Nodes (3): SessionCookies, get_cookies(), google_callback()

### Community 74 - "TaskQueue"
Cohesion: 0.10
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskQueue, enqueue_sync()

### Community 75 - "uuid"
Cohesion: 0.29
Nodes (15): _csrf(), test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused() (+7 more)

### Community 76 - "AuditService"
Cohesion: 0.13
Nodes (3): index(), AuditService, AuditOut

### Community 77 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 79 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 80 - "pytest"
Cohesion: 0.24
Nodes (5): RedisEvents, test_redis_source_delivers_published_messages(), run(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 81 - "GoogleService"
Cohesion: 0.07
Nodes (7): GoogleUnavailable, GoogleAuth, new_verifier(), google_start(), google_status(), google_unlink(), GoogleService

### Community 82 - "test_company_image.py"
Cohesion: 0.36
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 84 - "edit_fiscal"
Cohesion: 0.25
Nodes (3): edit_fiscal(), edit_image(), remove_image()

### Community 88 - "auth/controller.py"
Cohesion: 0.06
Nodes (16): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+8 more)

### Community 91 - "profile/controller.py"
Cohesion: 0.06
Nodes (10): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService (+2 more)

### Community 92 - "PageOut"
Cohesion: 0.12
Nodes (5): results(), ClientResultService, ResultsOut, default_period(), PageOut

### Community 132 - ".trusted_uow"
Cohesion: 0.08
Nodes (8): owner_invitations(), register_client(), ClientDetailOut, ClientIn, ClientOut, OwnerInvitationOut, ClientService, owner_invitation_out()

### Community 136 - "reports/service.py"
Cohesion: 0.07
Nodes (10): CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+2 more)

### Community 139 - "GoogleFailed"
Cohesion: 0.14
Nodes (3): GoogleFailed, GoogleOAuth, FakeGoogle

### Community 145 - "CompanyService"
Cohesion: 0.20
Nodes (3): fiscal(), show(), CompanyService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1172 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **59 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `roles/controller.py`, `.uow`, `.trusted_uow`, `GoalService`, `.__init__`, `reports/service.py`, `shared/dto.py`, `.uow`, `MemberOut`, `api_keys/controller.py`, `CompanyService`, `modules/results/controller.py`, `custom_metrics/controller.py`, `costs/controller.py`, `mfa/controller.py`, `ReportService`, `NetworkService`, `company/controller.py`, `invitations/controller.py`, `sites/controller.py`, `currencies/controller.py`, `account/controller.py`, `networks/service.py`, `goals/service.py`, `PeopleService`, `mcm/controller.py`, `Limiter`, `.uow`, `TaskQueue`, `AuditService`, `SiteService`, `GoogleService`, `auth/controller.py`, `profile/controller.py`, `PageOut`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **Are the 74 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 74 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06533646322378717 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `contracts/controller.py`, `roles/controller.py`, `.uow`, `Actor`, `.trusted_uow`, `GoalService`, `reports/service.py`, `shared/dto.py`, `.uow`, `MemberOut`, `api_keys/controller.py`, `costs/controller.py`, `goals/controller.py`, `networks/controller.py`, `NetworkService`, `invitations/controller.py`, `sites/controller.py`, `ItemsOut`, `networks/service.py`, `GoalTemplateOut`, `goals/service.py`, `PeopleService`, `mcm/controller.py`, `.uow`, `AuditService`, `SiteService`, `UnitOfWorkFactory`, `.page_saved`?**
  _High betweenness centrality (0.099) - this node is a cross-community bridge._
- **Are the 38 inferred relationships involving `PageOut` (e.g. with `index()` and `ApiKeyService`) actually correct?**
  _`PageOut` has 38 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07683000604960677 - nodes in this community are weakly interconnected._