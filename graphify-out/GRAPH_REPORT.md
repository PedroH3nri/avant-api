# Graph Report - avant-api  (2026-10-29)

## Corpus Check
- 207 files · ~62,591 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2630 nodes · 6858 edges · 154 communities (82 shown, 72 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1129 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7ea2338d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _staff
- contracts/controller.py
- roles/controller.py
- SiteService
- Actor
- security.py
- commissions/controller.py
- test_events.py
- steps
- _month
- Avant: models do MVP
- _member_client
- FiscalDataOut
- .uow
- mcm/controller.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- internal/results/controller.py
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- goals/controller.py
- shared/dto.py
- networks/controller.py
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- .build
- health/controller.py
- .uow
- session-start.sh
- avant-api
- NetworkService
- test_api_keys.py
- events/controller.py
- export.py
- test_account.py
- company/controller.py
- _marketing_client
- errors.py
- invitations/controller.py
- CapturingMailer
- limits.py
- google.py
- datetime
- Services
- ReportQueryIn
- CompanyService
- edit
- currencies/controller.py
- MemberService
- google_status
- OwnerInvitationOut
- networks/service.py
- GoalTemplateOut
- AccountService
- CommissionService
- mine
- goals/service.py
- PeopleService
- mcm/controller.py
- _onboard_owner
- google_start
- reports/controller.py
- Limiter
- index
- auth/dto.py
- SessionCookies
- avant-api
- uuid
- PageOut
- team
- commissions/dto.py
- test_report_export.py
- issue
- GoogleService
- test_company_image.py
- Avant: grupos na Empresa e imagem da Empresa
- edit_fiscal
- main.py
- Actor
- auth/controller.py
- google/controller.py
- profile/controller.py
- _enable
- pydantic
- QueryTooHeavy
- source_files
- UnitOfWorkFactory
- Actor
- .page_saved
- pytest
- .of
- RoleGoalOut
- MemoryCounter
- image
- GoalService
- Avant: conexão com o GAM
- reports/service.py
- Actor
- .of
- FakeGoogle
- audit/service.py
- person
- fiscal
- test_groups_lifecycle
- GoogleOAuth
- set_permissions
- company_service

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 101 edges
2. `PageOut` - 96 edges
3. `_onboard_owner()` - 93 edges
4. `Services` - 89 edges
5. `UnitOfWorkFactory` - 85 edges
6. `_csrf()` - 83 edges
7. `ClientService` - 51 edges
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

## Communities (154 total, 72 thin omitted)

### Community 0 - "_staff"
Cohesion: 0.19
Nodes (13): _admin_role(), test_groone_role_with_internal_permissions(), test_rules_on_the_role(), test_start_my_commission_team_discount_and_issue(), _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal(), _staff() (+5 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (23): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, contract(), contract_networks() (+15 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "SiteService"
Cohesion: 0.05
Nodes (26): Atribuição de sites, GAM, Networks, Sites e ad units, ad_units(), assign_sites(), create(), delete() (+18 more)

### Community 4 - "Actor"
Cohesion: 0.09
Nodes (18): audit(), cancel_owner(), change_status(), client(), edit_client(), edit_client_image(), register_client(), remove_client_image() (+10 more)

### Community 5 - "security.py"
Cohesion: 0.08
Nodes (12): api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor(), optional_auth(), require() (+4 more)

### Community 6 - "commissions/controller.py"
Cohesion: 0.16
Nodes (5): create_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 7 - "test_events.py"
Cohesion: 0.23
Nodes (6): _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

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
Cohesion: 0.16
Nodes (13): _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_sites_and_assignment(), _member_client(), test_audit_log() (+5 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "mcm/controller.py"
Cohesion: 0.12
Nodes (5): mcm_service(), people_service(), staff(), staff_service(), StaffService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "internal/results/controller.py"
Cohesion: 0.13
Nodes (5): results(), client_result_service(), ClientResultService, result_service(), ResultService

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

### Community 24 - "shared/dto.py"
Cohesion: 0.21
Nodes (5): DirectPermissionIn, MemberDetailOut, MemberPatchIn, MemberPermissionsIn, MemberOut

### Community 25 - "networks/controller.py"
Cohesion: 0.14
Nodes (11): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "test_reports.py"
Cohesion: 0.20
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (8): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut, MfaService

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - ".build"
Cohesion: 0.06
Nodes (10): _google(), _mailer(), NoEvents, RedisEvents, RedisCounter, Settings, CeleryQueue, RecordingQueue (+2 more)

### Community 31 - "health/controller.py"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 32 - ".uow"
Cohesion: 0.10
Nodes (7): Bucket, create(), show(), update(), SavedReportIn, SavedReportOut, ReportService

### Community 37 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 38 - "events/controller.py"
Cohesion: 0.09
Nodes (7): channel(), EventSource, _parse(), sse(), events(), event_service(), EventService

### Community 39 - "export.py"
Cohesion: 0.08
Nodes (9): JsonFormatter, dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx() (+1 more)

### Community 40 - "test_account.py"
Cohesion: 0.31
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 41 - "company/controller.py"
Cohesion: 0.17
Nodes (5): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, image_url()

### Community 42 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 43 - "errors.py"
Cohesion: 0.14
Nodes (9): CsrfFailed, error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), NoActiveCompany (+1 more)

### Community 45 - "invitations/controller.py"
Cohesion: 0.07
Nodes (9): invite(), cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService (+1 more)

### Community 46 - "CapturingMailer"
Cohesion: 0.21
Nodes (11): CapturingMailer, Sent, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten() (+3 more)

### Community 47 - "limits.py"
Cohesion: 0.08
Nodes (7): BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 48 - "google.py"
Cohesion: 0.19
Nodes (6): GoogleFailed, challenge(), _claims(), identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 49 - "datetime"
Cohesion: 0.07
Nodes (6): show(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut, default_period()

### Community 50 - "Services"
Cohesion: 0.05
Nodes (14): Services, get_cookies(), get_services(), get_session_auth(), account_service(), api_key_service(), auth_service(), currency_service() (+6 more)

### Community 51 - "ReportQueryIn"
Cohesion: 0.10
Nodes (5): query(), ReportQueryIn, ReportRangeOut, ReportResultOut, ReportRowOut

### Community 52 - "CompanyService"
Cohesion: 0.21
Nodes (3): show(), CompanyDetailOut, CompanyService

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 57 - "OwnerInvitationOut"
Cohesion: 0.16
Nodes (5): invite_owner(), new_owner(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 58 - "networks/service.py"
Cohesion: 0.16
Nodes (4): NetworkIn, NetworkOut, ServiceAccountOut, SyncRunOut

### Community 59 - "GoalTemplateOut"
Cohesion: 0.16
Nodes (3): create_template(), GoalTemplateIn, GoalTemplateOut

### Community 60 - "AccountService"
Cohesion: 0.10
Nodes (12): do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn (+4 more)

### Community 61 - "CommissionService"
Cohesion: 0.20
Nodes (4): adjust(), delete_rule(), AdjustmentIn, CommissionService

### Community 62 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 64 - "PeopleService"
Cohesion: 0.20
Nodes (3): disable(), enable(), reset_mfa()

### Community 65 - "mcm/controller.py"
Cohesion: 0.11
Nodes (5): assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService

### Community 66 - "_onboard_owner"
Cohesion: 0.22
Nodes (14): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format() (+6 more)

### Community 67 - "google_start"
Cohesion: 0.15
Nodes (3): new_verifier(), google_callback(), google_start()

### Community 68 - "reports/controller.py"
Cohesion: 0.11
Nodes (9): catalog(), create_from_template(), delete(), duplicate(), export(), export_saved(), run(), templates() (+1 more)

### Community 69 - "Limiter"
Cohesion: 0.09
Nodes (7): TooManyAttempts, Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "index"
Cohesion: 0.13
Nodes (6): edit(), index(), leave(), options(), remove(), show()

### Community 71 - "auth/dto.py"
Cohesion: 0.17
Nodes (7): get_invitation(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut

### Community 75 - "uuid"
Cohesion: 0.29
Nodes (15): _csrf(), test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused() (+7 more)

### Community 76 - "PageOut"
Cohesion: 0.08
Nodes (10): Resumo, client_teams(), ClientMemberOut, users(), PersonOut, PeopleService, person_out(), CompanyRefOut (+2 more)

### Community 77 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 79 - "test_report_export.py"
Cohesion: 0.22
Nodes (3): _result(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 80 - "issue"
Cohesion: 0.24
Nodes (4): issue(), CommissionSettingsIn, IssuedOut, MonthIn

### Community 81 - "GoogleService"
Cohesion: 0.12
Nodes (3): GoogleUnavailable, GoogleAuth, GoogleService

### Community 82 - "test_company_image.py"
Cohesion: 0.39
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 83 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 85 - "main.py"
Cohesion: 0.10
Nodes (5): configure_logging(), observe(), _route_template(), create_app(), audit_service()

### Community 87 - "Actor"
Cohesion: 0.18
Nodes (5): Modelo de dados, client_image(), client_options(), clients(), owner_invitations()

### Community 88 - "auth/controller.py"
Cohesion: 0.10
Nodes (9): accept(), company_image(), do_logout(), login(), me(), set_active_company(), MeOut, AuthService (+1 more)

### Community 89 - "google/controller.py"
Cohesion: 0.10
Nodes (4): PillowImageProcessor, google_redirects(), google_service(), GoogleRedirects

### Community 91 - "profile/controller.py"
Cohesion: 0.06
Nodes (10): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService, UserOut (+2 more)

### Community 92 - "_enable"
Cohesion: 0.22
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 98 - "Actor"
Cohesion: 0.23
Nodes (3): set_settings(), settings(), CommissionSettingsOut

### Community 128 - "pytest"
Cohesion: 0.24
Nodes (5): client(), engine(), mailer(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 135 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 136 - "reports/service.py"
Cohesion: 0.06
Nodes (11): CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+3 more)

### Community 143 - "audit/service.py"
Cohesion: 0.12
Nodes (3): index(), AuditService, AuditOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1224 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **72 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `roles/controller.py`, `SiteService`, `.trusted_uow`, `Actor`, `GoalService`, `reports/service.py`, `.uow`, `mcm/controller.py`, `audit/service.py`, `api_keys/controller.py`, `internal/results/controller.py`, `.__init__`, `custom_metrics/controller.py`, `.__init__`, `costs/controller.py`, `shared/dto.py`, `networks/controller.py`, `mfa/controller.py`, `.uow`, `company/controller.py`, `invitations/controller.py`, `limits.py`, `datetime`, `Services`, `CompanyService`, `currencies/controller.py`, `MemberService`, `networks/service.py`, `AccountService`, `CommissionService`, `goals/service.py`, `mcm/controller.py`, `Limiter`, `PageOut`, `commissions/dto.py`, `GoogleService`, `auth/controller.py`, `profile/controller.py`, `pydantic`?**
  _High betweenness centrality (0.134) - this node is a cross-community bridge._
- **Are the 75 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 75 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06018018018018018 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `contracts/controller.py`, `roles/controller.py`, `SiteService`, `Actor`, `.trusted_uow`, `GoalService`, `reports/service.py`, `.uow`, `mcm/controller.py`, `audit/service.py`, `api_keys/controller.py`, `internal/results/controller.py`, `costs/controller.py`, `goals/controller.py`, `shared/dto.py`, `networks/controller.py`, `NetworkService`, `invitations/controller.py`, `datetime`, `MemberService`, `OwnerInvitationOut`, `networks/service.py`, `GoalTemplateOut`, `goals/service.py`, `mcm/controller.py`, `index`, `main.py`, `Actor`, `pydantic`, `.page_saved`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Are the 38 inferred relationships involving `PageOut` (e.g. with `index()` and `ApiKeyService`) actually correct?**
  _`PageOut` has 38 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07922077922077922 - nodes in this community are weakly interconnected._