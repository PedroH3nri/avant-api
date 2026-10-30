# Graph Report - avant-api  (2026-10-30)

## Corpus Check
- 207 files · ~63,555 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2654 nodes · 6952 edges · 154 communities (88 shown, 66 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1142 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6324662f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- .uow
- Actor
- security.py
- commissions/controller.py
- test_events.py
- steps
- _month
- Avant: models do MVP
- _member_client
- clients/controller.py
- .uow
- networks/controller.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- InvitationOut
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- goals/controller.py
- google_callback
- NetworkService
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- limits.py
- health/controller.py
- .uow
- session-start.sh
- avant-api
- PageOut
- test_api_keys.py
- events/controller.py
- export.py
- test_account.py
- company/controller.py
- ContractClientRefOut
- errors.py
- conftest.py
- PageOut
- CapturingMailer
- networks/service.py
- google.py
- datetime
- Services
- ReportQueryIn
- shared/dto.py
- edit
- currencies/controller.py
- members/controller.py
- results
- http.py
- .catalog
- GoalTemplateOut
- AccountService
- CommissionService
- mine
- goals/service.py
- ResultService
- mcm/controller.py
- _onboard_owner
- company_image
- reports/controller.py
- Limiter
- AuthService
- _marketing_client
- SessionCookies
- avant-api
- tasks.py
- uuid
- people/controller.py
- team
- commissions/dto.py
- TaskQueue
- commissions/controller.py
- GoogleService
- test_company_image.py
- images.py
- .change_password
- main.py
- test_manual_site
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- Settings
- profile/controller.py
- do_reset_password
- Counter
- reports/service.py
- source_files
- UnitOfWorkFactory
- Actor
- MemoryCounter
- pytest
- test_contract_crud
- RoleGoalOut
- image
- Avant: conexão com o GAM
- reports/service.py
- GoalService
- ClientService
- test_groups_lifecycle
- audit/service.py
- person
- NoEvents
- .build

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 104 edges
2. `PageOut` - 96 edges
3. `_onboard_owner()` - 94 edges
4. `_csrf()` - 90 edges
5. `Services` - 89 edges
6. `UnitOfWorkFactory` - 85 edges
7. `ClientService` - 54 edges
8. `ReportService` - 51 edges
9. `page_out()` - 41 edges
10. `CommissionService` - 38 edges

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

## Communities (154 total, 66 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.14
Nodes (22): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+14 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (24): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, contract(), contract_networks() (+16 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.05
Nodes (26): Atribuição de sites, GAM, Networks, Sites e ad units, ad_units(), assign_sites(), create(), delete() (+18 more)

### Community 4 - "Actor"
Cohesion: 0.08
Nodes (14): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), clients(), edit_client_image() (+6 more)

### Community 5 - "security.py"
Cohesion: 0.09
Nodes (13): api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor(), get_session_auth(), optional_auth() (+5 more)

### Community 6 - "commissions/controller.py"
Cohesion: 0.17
Nodes (4): rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 7 - "test_events.py"
Cohesion: 0.14
Nodes (9): channel(), _parse(), sse(), _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit() (+1 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.21
Nodes (10): _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _member_client(), test_audit_log(), test_company_and_members(), test_leave_company(), test_requires_session() (+2 more)

### Community 12 - "clients/controller.py"
Cohesion: 0.20
Nodes (11): edit_client(), ClientDetailOut, ClientIn, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+3 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "networks/controller.py"
Cohesion: 0.20
Nodes (6): disconnect(), options(), service_account(), show(), sync(), sync_runs()

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.08
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (11): check(), create(), delete(), index(), update(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn (+3 more)

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

### Community 24 - "google_callback"
Cohesion: 0.13
Nodes (3): google_callback(), verify(), client_info()

### Community 25 - "NetworkService"
Cohesion: 0.17
Nodes (4): connect(), index(), NetworkDetailOut, NetworkService

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "test_reports.py"
Cohesion: 0.19
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (10): auth_service(), confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "limits.py"
Cohesion: 0.09
Nodes (9): Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket() (+1 more)

### Community 31 - "health/controller.py"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 32 - ".uow"
Cohesion: 0.11
Nodes (4): create(), SavedReportIn, SavedReportOut, ReportService

### Community 36 - "PageOut"
Cohesion: 0.11
Nodes (5): owner_invitations(), OwnerInvitationOut, owner_invitation_out(), page_out(), PageOut

### Community 37 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 38 - "events/controller.py"
Cohesion: 0.13
Nodes (4): EventSource, events(), event_service(), EventService

### Community 39 - "export.py"
Cohesion: 0.09
Nodes (11): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+3 more)

### Community 40 - "test_account.py"
Cohesion: 0.40
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 41 - "company/controller.py"
Cohesion: 0.11
Nodes (10): edit_fiscal(), edit_image(), fiscal(), company_service(), CompanyDetailOut, CompanyFiscalOut, CompanyPatchIn, FiscalDataIn (+2 more)

### Community 42 - "ContractClientRefOut"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 43 - "errors.py"
Cohesion: 0.12
Nodes (10): CsrfFailed, error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), NoActiveCompany (+2 more)

### Community 44 - "conftest.py"
Cohesion: 0.13
Nodes (5): _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 45 - "PageOut"
Cohesion: 0.11
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 46 - "CapturingMailer"
Cohesion: 0.16
Nodes (14): CapturingMailer, client(), engine(), mailer(), Sent, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages() (+6 more)

### Community 47 - "networks/service.py"
Cohesion: 0.18
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 48 - "google.py"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 50 - "Services"
Cohesion: 0.06
Nodes (7): Services, get_services(), account_service(), custom_metric_service(), google_redirects(), network_service(), profile_service()

### Community 51 - "ReportQueryIn"
Cohesion: 0.12
Nodes (3): query(), ReportQueryIn, ReportResultOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (4): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (16): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+8 more)

### Community 56 - "results"
Cohesion: 0.14
Nodes (3): results(), client_result_service(), ClientResultService

### Community 58 - ".catalog"
Cohesion: 0.22
Nodes (3): catalog(), CustomCatalogMetricOut, MetricCatalogOut

### Community 59 - "GoalTemplateOut"
Cohesion: 0.16
Nodes (3): create_template(), GoalTemplateIn, GoalTemplateOut

### Community 60 - "AccountService"
Cohesion: 0.18
Nodes (8): delete_session(), get_sessions(), ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut, SessionOut, AccountService

### Community 61 - "CommissionService"
Cohesion: 0.13
Nodes (4): delete_rule(), commission_service(), IssuedOut, CommissionService

### Community 62 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 64 - "ResultService"
Cohesion: 0.14
Nodes (3): show(), result_service(), ResultService

### Community 65 - "mcm/controller.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "_onboard_owner"
Cohesion: 0.22
Nodes (14): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format() (+6 more)

### Community 67 - "company_image"
Cohesion: 0.18
Nodes (3): company_image(), get_invitation(), me()

### Community 68 - "reports/controller.py"
Cohesion: 0.10
Nodes (11): create_from_template(), delete(), duplicate(), export(), export_saved(), index(), run(), show() (+3 more)

### Community 69 - "Limiter"
Cohesion: 0.17
Nodes (5): Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 72 - "SessionCookies"
Cohesion: 0.17
Nodes (3): SessionCookies, get_cookies(), do_logout()

### Community 75 - "uuid"
Cohesion: 0.26
Nodes (14): test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+6 more)

### Community 76 - "people/controller.py"
Cohesion: 0.10
Nodes (10): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PersonOut (+2 more)

### Community 77 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 78 - "commissions/dto.py"
Cohesion: 0.14
Nodes (4): CommissionMonthOut, CommissionSettingsIn, dollars(), MyCommissionsOut

### Community 80 - "commissions/controller.py"
Cohesion: 0.22
Nodes (5): adjust(), create_rule(), issue(), AdjustmentIn, MonthIn

### Community 81 - "GoogleService"
Cohesion: 0.07
Nodes (6): GoogleUnavailable, GoogleAuth, google_status(), google_unlink(), google_service(), GoogleService

### Community 82 - "test_company_image.py"
Cohesion: 0.31
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 85 - "main.py"
Cohesion: 0.10
Nodes (5): configure_logging(), JsonFormatter, observe(), _route_template(), create_app()

### Community 86 - "test_manual_site"
Cohesion: 0.53
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.15
Nodes (9): login(), set_active_company(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut (+1 more)

### Community 89 - "Settings"
Cohesion: 0.08
Nodes (5): new_verifier(), Settings, google_start(), GoogleStatusOut, GoogleRedirects

### Community 91 - "profile/controller.py"
Cohesion: 0.09
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService, UserOut

### Community 95 - "reports/service.py"
Cohesion: 0.11
Nodes (4): RateLimited, ReportCountsOut, ReportPageOut, _statement_timeout()

### Community 97 - "UnitOfWorkFactory"
Cohesion: 0.11
Nodes (3): UnitOfWorkFactory, currency_service(), CurrencyService

### Community 98 - "Actor"
Cohesion: 0.18
Nodes (4): mine(), set_settings(), settings(), CommissionSettingsOut

### Community 128 - "pytest"
Cohesion: 0.24
Nodes (5): RedisEvents, test_redis_source_delivers_published_messages(), run(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 129 - "test_contract_crud"
Cohesion: 0.38
Nodes (3): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission()

### Community 133 - "image"
Cohesion: 0.12
Nodes (3): image(), remove_image(), show()

### Community 135 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 136 - "reports/service.py"
Cohesion: 0.07
Nodes (10): DimensionOut, FilterIn, LabelOut, MetricOut, OrderIn, PeriodIn, ReportRangeOut, ReportRowOut (+2 more)

### Community 138 - "ClientService"
Cohesion: 0.31
Nodes (5): client_teams(), client_service(), ClientMemberOut, ClientService, CompanyRefOut

### Community 143 - "audit/service.py"
Cohesion: 0.13
Nodes (4): index(), audit_service(), AuditService, AuditOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1228 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **66 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `roles/controller.py`, `.uow`, `.trusted_uow`, `.__init__`, `GoalService`, `ClientService`, `clients/controller.py`, `.uow`, `audit/service.py`, `api_keys/controller.py`, `InvitationOut`, `.__init__`, `custom_metrics/controller.py`, `.__init__`, `costs/controller.py`, `NetworkService`, `.__init__`, `mfa/controller.py`, `.uow`, `company/controller.py`, `PageOut`, `networks/service.py`, `datetime`, `currencies/controller.py`, `members/controller.py`, `results`, `AccountService`, `CommissionService`, `goals/service.py`, `ResultService`, `mcm/controller.py`, `Limiter`, `AuthService`, `people/controller.py`, `TaskQueue`, `GoogleService`, `auth/controller.py`, `profile/controller.py`, `reports/service.py`?**
  _High betweenness centrality (0.124) - this node is a cross-community bridge._
- **Are the 78 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 78 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.13940256045519203 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `contracts/controller.py`, `roles/controller.py`, `.uow`, `Actor`, `.trusted_uow`, `reports/service.py`, `GoalService`, `ClientService`, `clients/controller.py`, `.uow`, `networks/controller.py`, `audit/service.py`, `api_keys/controller.py`, `InvitationOut`, `costs/controller.py`, `goals/controller.py`, `NetworkService`, `PageOut`, `networks/service.py`, `datetime`, `shared/dto.py`, `members/controller.py`, `results`, `GoalTemplateOut`, `goals/service.py`, `mcm/controller.py`, `people/controller.py`, `reports/service.py`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Are the 38 inferred relationships involving `PageOut` (e.g. with `index()` and `ApiKeyService`) actually correct?**
  _`PageOut` has 38 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05679974034404414 - nodes in this community are weakly interconnected._