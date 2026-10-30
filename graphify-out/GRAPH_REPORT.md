# Graph Report - avant-api  (2026-10-30)

## Corpus Check
- 207 files · ~63,296 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 2641 nodes · 6918 edges · 148 communities (81 shown, 67 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 1137 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f2f6ae63`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- ContractService
- roles/controller.py
- Actor
- security.py
- commissions/controller.py
- test_events.py
- steps
- _month
- Avant: models do MVP
- _member_client
- shared/dto.py
- .uow
- ItemsOut
- Groone Avant: contexto do projeto
- api_keys/controller.py
- invitations/controller.py
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- costs/controller.py
- goals/controller.py
- sites/controller.py
- networks/controller.py
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- RedisBucket
- health/controller.py
- .uow
- session-start.sh
- avant-api
- page_out
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
- contracts/controller.py
- google.py
- avant_core_access_models
- Services
- ReportQueryIn
- CompanyService
- edit
- currencies/controller.py
- members/controller.py
- google/controller.py
- http.py
- GoalTemplateOut
- AccountService
- CommissionService
- mine
- goals/service.py
- contracts
- mcm/controller.py
- _onboard_owner
- .assign
- reports/controller.py
- Limiter
- SiteService
- verify
- avant-api
- uuid
- people/controller.py
- team
- commissions/dto.py
- .networks
- commissions/controller.py
- GoogleService
- test_company_image.py
- images.py
- test_goal_progress_routes
- main.py
- test_manual_site
- avant-api
- auth/controller.py
- Settings
- profile/controller.py
- RateLimited
- source_files
- UnitOfWorkFactory
- Actor
- .page_saved
- pytest
- GoalService
- .trusted_uow
- image
- _contract_fields
- Avant: conexão com o GAM
- reports/service.py
- link
- .of
- audit/service.py
- person
- GoogleOAuth

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 104 edges
2. `PageOut` - 96 edges
3. `_onboard_owner()` - 94 edges
4. `Services` - 89 edges
5. `_csrf()` - 89 edges
6. `UnitOfWorkFactory` - 85 edges
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

## Communities (148 total, 67 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.14
Nodes (25): _csrf(), _admin_role(), _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions(), test_rules_on_the_role() (+17 more)

### Community 1 - "ContractService"
Cohesion: 0.15
Nodes (5): O que já tem, finish_contract(), new_contract(), ContractOut, ContractService

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 4 - "Actor"
Cohesion: 0.08
Nodes (23): Modelo de dados, audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams() (+15 more)

### Community 5 - "security.py"
Cohesion: 0.08
Nodes (16): CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor() (+8 more)

### Community 6 - "commissions/controller.py"
Cohesion: 0.17
Nodes (4): rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 7 - "test_events.py"
Cohesion: 0.11
Nodes (12): channel(), _parse(), RedisEvents, sse(), _collect(), _event(), ListEvents, test_events_route() (+4 more)

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
Cohesion: 0.15
Nodes (12): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _member_client(), test_audit_log(), test_company_and_members() (+4 more)

### Community 12 - "shared/dto.py"
Cohesion: 0.08
Nodes (7): ClientOptionOut, ClientProfileIn, ClientProfileOut, ClientStatusIn, OwnerChangeIn, FiscalDataOut, image_url()

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "ItemsOut"
Cohesion: 0.14
Nodes (10): ad_units(), assign_sites(), delete(), index(), members(), show(), site_options(), sites_of_member() (+2 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "invitations/controller.py"
Cohesion: 0.15
Nodes (6): cancel(), create_invitation(), resend(), invitation_service(), InviteIn, InvitationService

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
Cohesion: 0.18
Nodes (5): delete_template(), set_role_goal(), template_options(), templates(), update_template()

### Community 24 - "sites/controller.py"
Cohesion: 0.23
Nodes (8): create(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut

### Community 25 - "networks/controller.py"
Cohesion: 0.06
Nodes (16): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+8 more)

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "test_reports.py"
Cohesion: 0.23
Nodes (11): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_page_views_query_by_hour(), test_query_needs_permission() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (10): SessionCookies, get_cookies(), confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 31 - "health/controller.py"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 32 - ".uow"
Cohesion: 0.10
Nodes (5): Bucket, create(), SavedReportIn, SavedReportOut, ReportService

### Community 37 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 38 - "events/controller.py"
Cohesion: 0.13
Nodes (4): EventSource, events(), event_service(), EventService

### Community 39 - "export.py"
Cohesion: 0.08
Nodes (11): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+3 more)

### Community 40 - "test_account.py"
Cohesion: 0.40
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 41 - "company/controller.py"
Cohesion: 0.14
Nodes (6): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 42 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 43 - "errors.py"
Cohesion: 0.20
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "conftest.py"
Cohesion: 0.10
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 45 - "PageOut"
Cohesion: 0.08
Nodes (9): invite(), options(), staff(), StaffInviteIn, StaffService, list_invitations(), InvitationOut, MemberOut (+1 more)

### Community 46 - "CapturingMailer"
Cohesion: 0.37
Nodes (10): _onboard_owner(), test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_option_lists_keep_the_permissions() (+2 more)

### Community 47 - "contracts/controller.py"
Cohesion: 0.26
Nodes (6): contract_service(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut

### Community 48 - "google.py"
Cohesion: 0.14
Nodes (7): GoogleFailed, challenge(), _claims(), identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 49 - "avant_core_access_models"
Cohesion: 0.07
Nodes (8): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, default_period(), ResultService

### Community 50 - "Services"
Cohesion: 0.05
Nodes (16): Estrutura, _mailer(), Services, NoEvents, get_services(), CeleryQueue, RecordingQueue, TaskQueue (+8 more)

### Community 52 - "CompanyService"
Cohesion: 0.16
Nodes (3): edit_image(), remove_image(), CompanyDetailOut

### Community 53 - "edit"
Cohesion: 0.11
Nodes (15): Convites, Empresa, Empresa e equipe, Membros, Papéis e permissões, Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta (+7 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (13): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+5 more)

### Community 56 - "google/controller.py"
Cohesion: 0.13
Nodes (5): new_verifier(), google_start(), google_status(), google_unlink(), GoogleStatusOut

### Community 57 - "http.py"
Cohesion: 0.16
Nodes (3): client_info(), image_response(), image_upload()

### Community 59 - "GoalTemplateOut"
Cohesion: 0.16
Nodes (3): create_template(), GoalTemplateIn, GoalTemplateOut

### Community 60 - "AccountService"
Cohesion: 0.10
Nodes (12): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn (+4 more)

### Community 61 - "CommissionService"
Cohesion: 0.13
Nodes (4): delete_rule(), commission_service(), IssuedOut, CommissionService

### Community 62 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 64 - "contracts"
Cohesion: 0.18
Nodes (5): contract(), contract_networks(), contracts(), edit_contract(), remove_contract()

### Community 65 - "mcm/controller.py"
Cohesion: 0.11
Nodes (6): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService

### Community 66 - "_onboard_owner"
Cohesion: 0.12
Nodes (18): CapturingMailer, client(), engine(), mailer(), Sent, _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics() (+10 more)

### Community 67 - ".assign"
Cohesion: 0.16
Nodes (11): API first e chaves de API, Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Decisões de Pedro (23/10/2026), GAM, Networks (+3 more)

### Community 68 - "reports/controller.py"
Cohesion: 0.10
Nodes (12): catalog(), create_from_template(), delete(), duplicate(), export(), export_saved(), query(), run() (+4 more)

### Community 69 - "Limiter"
Cohesion: 0.05
Nodes (14): TooManyAttempts, BucketResult, BucketRule, Counter, Limiter, MemoryBucket, MemoryCounter, Rule (+6 more)

### Community 71 - "SiteService"
Cohesion: 0.22
Nodes (3): site_service(), SiteMemberOut, SiteService

### Community 75 - "uuid"
Cohesion: 0.26
Nodes (14): test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+6 more)

### Community 76 - "people/controller.py"
Cohesion: 0.10
Nodes (10): Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService (+2 more)

### Community 78 - "commissions/dto.py"
Cohesion: 0.14
Nodes (4): CommissionMonthOut, CommissionSettingsIn, dollars(), MyCommissionsOut

### Community 80 - "commissions/controller.py"
Cohesion: 0.22
Nodes (5): adjust(), create_rule(), issue(), AdjustmentIn, MonthIn

### Community 81 - "GoogleService"
Cohesion: 0.11
Nodes (4): GoogleUnavailable, GoogleAuth, google_callback(), GoogleService

### Community 82 - "test_company_image.py"
Cohesion: 0.31
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 84 - "test_goal_progress_routes"
Cohesion: 0.53
Nodes (3): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 85 - "main.py"
Cohesion: 0.10
Nodes (5): configure_logging(), JsonFormatter, observe(), _route_template(), create_app()

### Community 86 - "test_manual_site"
Cohesion: 0.53
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 87 - "avant-api"
Cohesion: 0.40
Nodes (4): avant-api, Como funciona, Desenvolvimento, Imagem

### Community 88 - "auth/controller.py"
Cohesion: 0.10
Nodes (16): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+8 more)

### Community 91 - "profile/controller.py"
Cohesion: 0.07
Nodes (9): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService (+1 more)

### Community 95 - "RateLimited"
Cohesion: 0.25
Nodes (3): QueryTooHeavy, RateLimited, _statement_timeout()

### Community 98 - "Actor"
Cohesion: 0.18
Nodes (4): mine(), set_settings(), settings(), CommissionSettingsOut

### Community 130 - "GoalService"
Cohesion: 0.17
Nodes (4): role_goals(), goal_service(), RoleGoalOut, GoalService

### Community 133 - "image"
Cohesion: 0.18
Nodes (3): fiscal(), image(), show()

### Community 135 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 136 - "reports/service.py"
Cohesion: 0.09
Nodes (13): CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+5 more)

### Community 143 - "audit/service.py"
Cohesion: 0.16
Nodes (3): index(), audit_service(), AuditService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1224 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **67 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `ContractService`, `GoalService`, `.uow`, `.trusted_uow`, `Actor`, `.__init__`, `roles/controller.py`, `reports/service.py`, `.__init__`, `shared/dto.py`, `.uow`, `audit/service.py`, `api_keys/controller.py`, `invitations/controller.py`, `.__init__`, `custom_metrics/controller.py`, `costs/controller.py`, `sites/controller.py`, `networks/controller.py`, `mfa/controller.py`, `.uow`, `company/controller.py`, `PageOut`, `contracts/controller.py`, `avant_core_access_models`, `currencies/controller.py`, `members/controller.py`, `AccountService`, `CommissionService`, `goals/service.py`, `mcm/controller.py`, `Limiter`, `SiteService`, `people/controller.py`, `GoogleService`, `auth/controller.py`, `profile/controller.py`?**
  _High betweenness centrality (0.137) - this node is a cross-community bridge._
- **Are the 78 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 78 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.13900134952766532 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `ContractService`, `GoalService`, `roles/controller.py`, `Actor`, `.trusted_uow`, `.uow`, `reports/service.py`, `.of`, `shared/dto.py`, `.uow`, `ItemsOut`, `audit/service.py`, `api_keys/controller.py`, `invitations/controller.py`, `costs/controller.py`, `goals/controller.py`, `sites/controller.py`, `networks/controller.py`, `page_out`, `contracts/controller.py`, `avant_core_access_models`, `Services`, `members/controller.py`, `GoalTemplateOut`, `goals/service.py`, `contracts`, `mcm/controller.py`, `SiteService`, `people/controller.py`, `UnitOfWorkFactory`, `.page_saved`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Are the 38 inferred relationships involving `PageOut` (e.g. with `index()` and `ApiKeyService`) actually correct?**
  _`PageOut` has 38 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08081632653061224 - nodes in this community are weakly interconnected._