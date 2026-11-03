# Graph Report - avant-api  (2026-11-03)

## Corpus Check
- 250 files · ~77,980 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3351 nodes · 9137 edges · 164 communities (98 shown, 66 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1543 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `08932779`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- DashboardService
- AlertService
- security.py
- commissions/controller.py
- test_api_keys.py
- steps
- schedules/controller.py
- Avant: models do MVP
- test_company_image.py
- .trusted_uow
- GroupService
- PageOut
- Groone Avant: contexto do projeto
- api_keys/controller.py
- pydantic
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- Settings
- dashboard_templates/controller.py
- invoice_pdf.py
- audit/controller.py
- clean_code.py
- CapturingMailer
- mfa/controller.py
- Avant: repositório e plano do MVP
- get
- clients/controller.py
- Actor
- session-start.sh
- avant-api
- ClientService
- _member_client
- invoices/controller.py
- export.py
- staff/controller.py
- CompanyService
- errors.py
- limits.py
- commissions/dto.py
- io
- views/controller.py
- auth/controller.py
- datetime
- alerts/dependencies.py
- ReportResultOut
- UserOut
- edit
- currencies/controller.py
- members/controller.py
- conftest.py
- goals/controller.py
- google/controller.py
- company/controller.py
- account/controller.py
- main.py
- Actor
- Actor
- mcm/controller.py
- CapturingMailer
- sites/controller.py
- reports/controller.py
- Limiter
- auth/service.py
- sqlalchemy
- google.py
- avant-api
- networks/controller.py
- uuid
- people/controller.py
- Avant: conexão com o GAM
- GoalService
- costs/controller.py
- _month
- CommissionService
- to_xlsx
- test_dashboards.py
- InvoiceService
- events.py
- test_networks.py
- Avant: grupos na Empresa e imagem da Empresa
- SiteService
- test_members_without_schedules_manage_only_see_what_they_receive
- profile/controller.py
- Actor
- ClientOut
- GoalTemplateOut
- .of
- update_item
- .assign
- Actor
- test_alerts.py
- Actor
- mine
- OwnerInvitationOut
- .fiscal
- reports/service.py
- SiteListOut
- person
- .build
- UnitOfWorkFactory
- test_contract_crud
- CommissionRuleOut
- test_account.py
- AdUnitOut
- delete_template
- Suporte
- google/controller.py
- members
- clients

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 132 edges
2. `PageOut` - 123 edges
3. `_onboard_owner()` - 118 edges
4. `_csrf()` - 116 edges
5. `get()` - 107 edges
6. `UnitOfWorkFactory` - 106 edges
7. `Services` - 104 edges
8. `ReportService` - 75 edges
9. `InvoiceService` - 58 edges
10. `ClientService` - 55 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/modules/internal/people/controller.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (164 total, 66 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.09
Nodes (35): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+27 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (25): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+17 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.06
Nodes (22): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+14 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "security.py"
Cohesion: 0.04
Nodes (23): Services, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_cookies(), get_services() (+15 more)

### Community 6 - "commissions/controller.py"
Cohesion: 0.16
Nodes (6): adjust(), create_rule(), delete_rule(), rules(), update_rule(), CommissionRuleIn

### Community 7 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (21): Acesso, AdUnit, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, GAM, Identidade (+13 more)

### Community 11 - "test_company_image.py"
Cohesion: 0.16
Nodes (7): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture()

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "PageOut"
Cohesion: 0.09
Nodes (8): networks(), sites(), ClientNetworkOut, ClientRefOut, ClientSiteOut, ClientInventoryService, page_out(), PageOut

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "pydantic"
Cohesion: 0.09
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "Settings"
Cohesion: 0.09
Nodes (5): Settings, google_redirects(), GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.13
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "audit/controller.py"
Cohesion: 0.15
Nodes (3): index(), audit_service(), AuditService

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "CapturingMailer"
Cohesion: 0.22
Nodes (12): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "get"
Cohesion: 0.09
Nodes (14): add_item(), create(), delete(), delete_service(), get(), mine(), pay(), payment_details() (+6 more)

### Community 31 - "clients/controller.py"
Cohesion: 0.13
Nodes (8): manager_change(), new_owner(), ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientStatusIn, ManagerChangeOut, OwnerChangeIn

### Community 32 - "Actor"
Cohesion: 0.07
Nodes (5): duplicate(), pinned(), show(), SavedReportOut, ReportService

### Community 36 - "ClientService"
Cohesion: 0.17
Nodes (5): client_teams(), client_service(), ClientMemberOut, ClientService, CompanyRefOut

### Community 37 - "_member_client"
Cohesion: 0.14
Nodes (13): _membership_ids(), test_groups_lifecycle(), _inventory(), test_manual_site(), test_site_category_and_responsible(), test_sites_and_assignment(), _member_client(), test_audit_log() (+5 more)

### Community 38 - "invoices/controller.py"
Cohesion: 0.09
Nodes (10): FiscalDataIn, dollars(), available_months(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceSummaryOut, ReturnedOut (+2 more)

### Community 39 - "export.py"
Cohesion: 0.13
Nodes (3): dimension_text(), _csv_cell(), _xlsx_cell()

### Community 40 - "staff/controller.py"
Cohesion: 0.11
Nodes (7): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 41 - "CompanyService"
Cohesion: 0.16
Nodes (4): show(), CompanyDetailOut, CompanyPatchIn, CompanyService

### Community 43 - "errors.py"
Cohesion: 0.08
Nodes (12): CsrfFailed, error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), NoActiveCompany (+4 more)

### Community 44 - "limits.py"
Cohesion: 0.08
Nodes (9): Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket() (+1 more)

### Community 45 - "commissions/dto.py"
Cohesion: 0.17
Nodes (5): AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn

### Community 46 - "io"
Cohesion: 0.21
Nodes (5): to_csv(), _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "auth/controller.py"
Cohesion: 0.09
Nodes (10): SessionCookies, accept(), company_image(), do_logout(), login(), me(), set_active_company(), MeOut (+2 more)

### Community 49 - "datetime"
Cohesion: 0.06
Nodes (8): results(), client_result_service(), ClientResultService, show(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut

### Community 51 - "ReportResultOut"
Cohesion: 0.14
Nodes (3): query(), ReportQueryIn, ReportResultOut

### Community 52 - "UserOut"
Cohesion: 0.12
Nodes (5): person_out(), edit_image(), remove_image(), ProfileService, UserOut

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+6 more)

### Community 56 - "conftest.py"
Cohesion: 0.11
Nodes (3): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 57 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 58 - "google/controller.py"
Cohesion: 0.06
Nodes (10): GoogleUnavailable, GoogleAuth, new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), google_service() (+2 more)

### Community 59 - "company/controller.py"
Cohesion: 0.13
Nodes (6): edit_fiscal(), edit_image(), fiscal(), image(), remove_image(), company_service()

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 62 - "main.py"
Cohesion: 0.06
Nodes (9): configure_logging(), JsonFormatter, observe(), _route_template(), create_app(), health(), ready(), health_service() (+1 more)

### Community 63 - "Actor"
Cohesion: 0.14
Nodes (7): audit(), cancel_owner(), change_status(), client_image(), client_options(), edit_client_image(), remove_client_image()

### Community 64 - "Actor"
Cohesion: 0.14
Nodes (7): classify(), classify_many(), delete(), index(), show(), sites_of_member(), unlinked()

### Community 65 - "mcm/controller.py"
Cohesion: 0.07
Nodes (9): TaskQueue, assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut (+1 more)

### Community 66 - "CapturingMailer"
Cohesion: 0.11
Nodes (11): CapturingMailer, client(), engine(), mailer(), Sent, test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login() (+3 more)

### Community 67 - "sites/controller.py"
Cohesion: 0.19
Nodes (8): site_service(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "reports/controller.py"
Cohesion: 0.08
Nodes (12): create(), create_from_template(), delete(), export(), export_saved(), index(), pin(), run() (+4 more)

### Community 69 - "Limiter"
Cohesion: 0.11
Nodes (6): Counter, Limiter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "auth/service.py"
Cohesion: 0.13
Nodes (10): get_invitation(), auth_service(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut (+2 more)

### Community 71 - "sqlalchemy"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 72 - "google.py"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 74 - "networks/controller.py"
Cohesion: 0.08
Nodes (14): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+6 more)

### Community 75 - "uuid"
Cohesion: 0.18
Nodes (25): _onboard_owner(), _owner_invite(), test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten() (+17 more)

### Community 76 - "people/controller.py"
Cohesion: 0.13
Nodes (7): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService

### Community 77 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 78 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 81 - "CommissionService"
Cohesion: 0.18
Nodes (3): set_settings(), commission_service(), CommissionService

### Community 82 - "to_xlsx"
Cohesion: 0.27
Nodes (4): _header(), _metric_label(), _rows(), to_xlsx()

### Community 83 - "test_dashboards.py"
Cohesion: 0.28
Nodes (7): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit()

### Community 84 - "InvoiceService"
Cohesion: 0.14
Nodes (7): create_service(), service_options(), update_service(), InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceServiceOut, InvoiceService

### Community 85 - "events.py"
Cohesion: 0.08
Nodes (15): channel(), EventSource, _parse(), RedisEvents, sse(), events(), EventService, _collect() (+7 more)

### Community 86 - "test_networks.py"
Cohesion: 0.47
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 89 - "test_members_without_schedules_manage_only_see_what_they_receive"
Cohesion: 0.15
Nodes (6): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 91 - "profile/controller.py"
Cohesion: 0.24
Nodes (3): edit_appearance(), AppearanceIn, AppearanceOut

### Community 94 - "ClientOut"
Cohesion: 0.14
Nodes (5): edit_client(), register_client(), ClientIn, ClientOut, ClientProfileOut

### Community 95 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 96 - ".of"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 97 - "update_item"
Cohesion: 0.15
Nodes (3): save_payment_details(), PayeeDetailsOut, FiscalDataOut

### Community 98 - ".assign"
Cohesion: 0.25
Nodes (5): Atribuição de sites, GAM, Networks, Sites e ad units, assign_sites()

### Community 131 - "test_alerts.py"
Cohesion: 0.35
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 134 - "OwnerInvitationOut"
Cohesion: 0.17
Nodes (5): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 136 - "reports/service.py"
Cohesion: 0.05
Nodes (19): catalog(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut (+11 more)

### Community 137 - "SiteListOut"
Cohesion: 0.20
Nodes (4): create(), site_options(), SiteListOut, ItemsOut

### Community 142 - ".build"
Cohesion: 0.06
Nodes (6): _google(), _mailer(), NoEvents, MemoryCounter, CeleryQueue, RecordingQueue

### Community 144 - "test_contract_crud"
Cohesion: 0.38
Nodes (3): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission()

### Community 146 - "test_account.py"
Cohesion: 0.40
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 147 - "AdUnitOut"
Cohesion: 0.16
Nodes (3): ad_units(), link(), AdUnitOut

### Community 152 - "Suporte"
Cohesion: 0.40
Nodes (5): ApiKey, AuditLog, PasswordReset, Session, Suporte

### Community 155 - "google/controller.py"
Cohesion: 0.11
Nodes (4): image(), profile_service(), image_response(), image_upload()

### Community 167 - "clients"
Cohesion: 0.12
Nodes (3): clients(), AuditOut, RevenueStatusOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1541 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **66 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `.__init__`, `contracts/controller.py`, `DashboardService`, `AlertService`, `security.py`, `roles/controller.py`, `reports/service.py`, `schedules/controller.py`, `goals/service.py`, `.trusted_uow`, `GroupService`, `PageOut`, `api_keys/controller.py`, `pydantic`, `custom_metrics/controller.py`, `.__init__`, `.__init__`, `dashboard_templates/controller.py`, `.__init__`, `audit/controller.py`, `mfa/controller.py`, `clients/controller.py`, `Actor`, `ClientService`, `invoices/controller.py`, `staff/controller.py`, `CompanyService`, `commissions/dto.py`, `views/controller.py`, `datetime`, `UserOut`, `currencies/controller.py`, `members/controller.py`, `google/controller.py`, `account/controller.py`, `mcm/controller.py`, `sites/controller.py`, `Limiter`, `auth/service.py`, `networks/controller.py`, `people/controller.py`, `GoalService`, `costs/controller.py`, `CommissionService`, `InvoiceService`, `SiteService`, `profile/controller.py`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._
- **Are the 97 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 97 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.08587570621468926 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `Actor`, `OwnerInvitationOut`, `reports/service.py`, `schedules/controller.py`, `goals/service.py`, `.trusted_uow`, `GroupService`, `UnitOfWorkFactory`, `api_keys/controller.py`, `pydantic`, `audit/controller.py`, `get`, `clients/controller.py`, `ClientService`, `invoices/controller.py`, `clients`, `staff/controller.py`, `datetime`, `members/controller.py`, `goals/controller.py`, `Actor`, `Actor`, `mcm/controller.py`, `sites/controller.py`, `reports/controller.py`, `networks/controller.py`, `people/controller.py`, `GoalService`, `costs/controller.py`, `InvoiceService`, `SiteService`, `GoalTemplateOut`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 50 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 50 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05506329113924051 - nodes in this community are weakly interconnected._