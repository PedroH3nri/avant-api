# Graph Report - avant-api  (2026-11-04)

## Corpus Check
- 290 files · ~88,870 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3913 nodes · 10745 edges · 193 communities (99 shown, 94 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1805 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0091c223`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/dto.py
- roles/controller.py
- .uow
- Actor
- .show
- commissions/controller.py
- test_events.py
- steps
- _month
- Avant: models do MVP
- _member_client
- .trusted_uow
- .uow
- networks/controller.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- InvitationOut
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- image_response
- goals/controller.py
- verify
- test_alerts.py
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- limits.py
- _onboard_owner
- session-start.sh
- avant-api
- pytest
- tasks/controller.py
- invoices/controller.py
- networks/controller.py
- test_account.py
- company/controller.py
- company/controller.py
- install
- MemoryBucket
- security.py
- mine
- networks/service.py
- test_mfa.py
- PageOut
- Services
- AuthService
- profile/controller.py
- edit
- currencies/controller.py
- members/controller.py
- checklists/controller.py
- clients
- mine
- UnitOfWorkFactory
- account/controller.py
- get
- health/controller.py
- ClientService
- main.py
- NetworkOut
- test_networks.py
- ItemsOut
- reports/controller.py
- limits.py
- ContractService
- GoalTemplateOut
- google/controller.py
- avant-api
- NetworkService
- uuid
- download
- team
- document_response
- image
- ClientDocumentOut
- disable
- dollars
- uuid
- contracts/controller.py
- conftest.py
- goals/controller.py
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- .of_detail
- .of_view
- add_note
- .preview_invitation
- O que já tem
- networks/service.py
- ReportResultOut
- client_documents/controller.py
- test_api_keys.py
- client_documents/service.py
- AdUnitOut
- delete_template
- avant_core_shared_errors
- test_account.py
- ReportService
- clients
- templates
- GoalService
- dashboards/dependencies.py
- UnitOfWorkFactory
- fastapi_testclient
- .of
- _marketing_client
- export.py
- Actor
- CompanyService
- GAM
- Actor
- edit_image
- CapturingMailer
- MemoryCounter
- .update
- edit_image
- .classify
- index
- .assign
- delete_template
- verify
- events/controller.py
- shared/dto.py

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 155 edges
2. `PageOut` - 145 edges
3. `_onboard_owner()` - 139 edges
4. `_csrf()` - 137 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 118 edges
8. `ReportService` - 79 edges
9. `_staff()` - 64 edges
10. `page_out()` - 59 edges

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

## Communities (193 total, 94 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.07
Nodes (37): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+29 more)

### Community 1 - "contracts/dto.py"
Cohesion: 0.15
Nodes (7): _contract_fields(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractSummaryOut, _network_ref(), ContractClientRefOut

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.05
Nodes (26): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+18 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - ".show"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 6 - "commissions/controller.py"
Cohesion: 0.06
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 7 - "test_events.py"
Cohesion: 0.06
Nodes (19): ads_txt(), install(), network(), networks(), run(), runs(), start(), gam_tool_service() (+11 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.10
Nodes (20): Acesso, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade (+12 more)

### Community 11 - "_member_client"
Cohesion: 0.07
Nodes (23): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person() (+15 more)

### Community 12 - ".trusted_uow"
Cohesion: 0.08
Nodes (11): add_item(), create(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft() (+3 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+6 more)

### Community 14 - "networks/controller.py"
Cohesion: 0.14
Nodes (7): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

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

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "test_alerts.py"
Cohesion: 0.25
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.23
Nodes (14): _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas() (+6 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "limits.py"
Cohesion: 0.06
Nodes (8): QueryTooHeavy, Bucket, create_from_template(), duplicate(), pinned(), SavedReportOut, ReportService, _statement_timeout()

### Community 32 - "_onboard_owner"
Cohesion: 0.21
Nodes (16): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format(), test_costs_and_reports_come_in_pages() (+8 more)

### Community 37 - "tasks/controller.py"
Cohesion: 0.05
Nodes (18): change(), comment(), create(), task(), tasks(), support_task_service(), TaskClientOut, TaskCommentIn (+10 more)

### Community 38 - "invoices/controller.py"
Cohesion: 0.11
Nodes (15): create_service(), save_payment_details(), update_service(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut (+7 more)

### Community 39 - "networks/controller.py"
Cohesion: 0.15
Nodes (8): connect(), disconnect(), options(), service_account(), show(), sync(), sync_runs(), network_service()

### Community 40 - "test_account.py"
Cohesion: 0.13
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 41 - "company/controller.py"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 42 - "company/controller.py"
Cohesion: 0.19
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "MemoryBucket"
Cohesion: 0.10
Nodes (7): BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 45 - "security.py"
Cohesion: 0.05
Nodes (24): Services, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth() (+16 more)

### Community 46 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "test_mfa.py"
Cohesion: 0.18
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+6 more)

### Community 49 - "PageOut"
Cohesion: 0.07
Nodes (8): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, default_period(), ResultService

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "AuthService"
Cohesion: 0.10
Nodes (3): login(), LoginIn, AuthService

### Community 52 - "profile/controller.py"
Cohesion: 0.09
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (16): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+8 more)

### Community 56 - "checklists/controller.py"
Cohesion: 0.15
Nodes (5): site_checklist_service(), ChecklistMarkIn, ChecklistMonthOut, ChecklistNoteIn, ChecklistOut

### Community 57 - "clients"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "mine"
Cohesion: 0.05
Nodes (13): SessionCookies, GoogleUnavailable, new_verifier(), get_cookies(), google_callback(), google_start(), google_status(), google_unlink() (+5 more)

### Community 60 - "account/controller.py"
Cohesion: 0.07
Nodes (15): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+7 more)

### Community 61 - "get"
Cohesion: 0.13
Nodes (8): available_months(), get(), mine(), payment_details(), pdf(), service_options(), services(), team()

### Community 62 - "health/controller.py"
Cohesion: 0.14
Nodes (4): health(), ready(), health_service(), HealthService

### Community 63 - "ClientService"
Cohesion: 0.05
Nodes (32): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), edit_client() (+24 more)

### Community 64 - "main.py"
Cohesion: 0.05
Nodes (12): _google(), _mailer(), RedisEvents, configure_logging(), observe(), _route_template(), Settings, CeleryQueue (+4 more)

### Community 65 - "NetworkOut"
Cohesion: 0.12
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "test_networks.py"
Cohesion: 0.14
Nodes (3): checklists(), months(), summary()

### Community 67 - "ItemsOut"
Cohesion: 0.25
Nodes (7): AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "reports/controller.py"
Cohesion: 0.15
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 69 - "limits.py"
Cohesion: 0.10
Nodes (8): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "GoalTemplateOut"
Cohesion: 0.14
Nodes (4): create_template(), template_options(), GoalTemplateIn, GoalTemplateOut

### Community 72 - "google/controller.py"
Cohesion: 0.07
Nodes (9): GoogleFailed, RateLimited, challenge(), _claims(), GoogleAuth, GoogleOAuth, identity_from_id_token(), _jwt() (+1 more)

### Community 74 - "NetworkService"
Cohesion: 0.16
Nodes (3): index(), NetworkDetailOut, NetworkService

### Community 75 - "uuid"
Cohesion: 0.15
Nodes (18): _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use() (+10 more)

### Community 76 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 77 - "team"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 81 - "disable"
Cohesion: 0.10
Nodes (11): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+3 more)

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - "contracts/controller.py"
Cohesion: 0.18
Nodes (6): contract(), contract_networks(), contracts(), finish_contract(), new_contract(), remove_contract()

### Community 85 - "conftest.py"
Cohesion: 0.12
Nodes (9): client(), engine(), mailer(), _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit() (+1 more)

### Community 86 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.09
Nodes (14): accept(), company_image(), do_logout(), get_invitation(), me(), set_active_company(), auth_service(), AcceptInvitationIn (+6 more)

### Community 89 - ".of_detail"
Cohesion: 0.14
Nodes (3): ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 91 - ".of_view"
Cohesion: 0.14
Nodes (7): ad_units(), delete(), link(), show(), site_options(), sites_of_member(), unlinked()

### Community 92 - "add_note"
Cohesion: 0.11
Nodes (8): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistDetailOut, SiteChecklistService

### Community 96 - "O que já tem"
Cohesion: 0.20
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics()

### Community 98 - "networks/service.py"
Cohesion: 0.18
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 127 - "ReportResultOut"
Cohesion: 0.12
Nodes (4): query(), run(), ReportQueryIn, ReportResultOut

### Community 128 - "client_documents/controller.py"
Cohesion: 0.19
Nodes (6): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentService

### Community 129 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 135 - "test_account.py"
Cohesion: 0.22
Nodes (8): FakeGoogle, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 136 - "ReportService"
Cohesion: 0.05
Nodes (18): catalog(), query_batch(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn (+10 more)

### Community 139 - "GoalService"
Cohesion: 0.23
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 144 - "fastapi_testclient"
Cohesion: 0.10
Nodes (13): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _checklists() (+5 more)

### Community 146 - "_marketing_client"
Cohesion: 0.18
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 147 - "export.py"
Cohesion: 0.09
Nodes (9): JsonFormatter, dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx() (+1 more)

### Community 148 - "Actor"
Cohesion: 0.22
Nodes (3): role_goals(), templates(), RoleGoalOut

### Community 149 - "CompanyService"
Cohesion: 0.22
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 150 - "GAM"
Cohesion: 0.33
Nodes (6): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment

### Community 152 - "Actor"
Cohesion: 0.08
Nodes (11): create(), delete(), export(), export_saved(), index(), pin(), show(), unpin() (+3 more)

### Community 158 - "CapturingMailer"
Cohesion: 0.17
Nodes (9): CapturingMailer, Sent, _owner_invite(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company() (+1 more)

### Community 178 - ".assign"
Cohesion: 0.25
Nodes (5): Atribuição de sites, GAM, Networks, Sites e ad units, assign_sites()

### Community 184 - "events/controller.py"
Cohesion: 0.08
Nodes (8): channel(), EventSource, NoEvents, _parse(), sse(), events(), event_service(), EventService

### Community 194 - "shared/dto.py"
Cohesion: 0.07
Nodes (4): index(), AuditService, AuditOut, page_out()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1789 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **94 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `client_documents/controller.py`, `contracts/dto.py`, `client_documents/service.py`, `.uow`, `Actor`, `roles/controller.py`, `commissions/controller.py`, `test_events.py`, `ReportService`, `_month`, `GoalService`, `.trusted_uow`, `.uow`, `networks/controller.py`, `UnitOfWorkFactory`, `api_keys/controller.py`, `InvitationOut`, `custom_metrics/controller.py`, `CompanyService`, `goals/controller.py`, `mfa/controller.py`, `limits.py`, `company/controller.py`, `.__init__`, `.__init__`, `tasks/controller.py`, `invoices/controller.py`, `.__init__`, `company/controller.py`, `company/controller.py`, `test_account.py`, `goals/service.py`, `networks/service.py`, `.__init__`, `PageOut`, `Services`, `AuthService`, `profile/controller.py`, `currencies/controller.py`, `members/controller.py`, `checklists/controller.py`, `clients`, `mine`, `.__init__`, `account/controller.py`, `ClientService`, `.__init__`, `NetworkOut`, `shared/dto.py`, `.__init__`, `reports/controller.py`, `ItemsOut`, `ContractService`, `google/controller.py`, `.__init__`, `NetworkService`, `image`, `disable`, `auth/controller.py`, `add_note`, `.__init__`, `networks/service.py`?**
  _High betweenness centrality (0.167) - this node is a cross-community bridge._
- **Are the 116 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 116 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.06684733514001806 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `disable` to `contracts/dto.py`, `roles/controller.py`, `.uow`, `Actor`, `AdUnitOut`, `test_events.py`, `ReportService`, `clients`, `_month`, `GoalService`, `.trusted_uow`, `.uow`, `networks/controller.py`, `api_keys/controller.py`, `InvitationOut`, `Actor`, `CompanyService`, `Actor`, `tasks/controller.py`, `invoices/controller.py`, `networks/controller.py`, `test_account.py`, `goals/service.py`, `security.py`, `PageOut`, `Services`, `index`, `members/controller.py`, `checklists/controller.py`, `get`, `ClientService`, `NetworkOut`, `shared/dto.py`, `test_networks.py`, `ItemsOut`, `ContractService`, `GoalTemplateOut`, `NetworkService`, `image`, `contracts/controller.py`, `goals/controller.py`, `.of_view`, `add_note`, `networks/service.py`?**
  _High betweenness centrality (0.070) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07364114552893045 - nodes in this community are weakly interconnected._