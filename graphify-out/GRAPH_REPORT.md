# Graph Report - avant-api  (2026-11-03)

## Corpus Check
- 290 files · ~87,085 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3859 nodes · 10541 edges · 188 communities (95 shown, 93 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1764 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `328f41f5`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
- roles/controller.py
- .uow
- Actor
- .show
- CommissionService
- test_events.py
- steps
- _month
- Avant: models do MVP
- _member_client
- CapturingMailer
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
- verify
- export.py
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- limits.py
- company/controller.py
- .uow
- session-start.sh
- avant-api
- tasks/controller.py
- get
- to_xlsx
- test_account.py
- company/controller.py
- ReportResultOut
- install
- MemoryBucket
- networks/service.py
- _onboard_owner
- networks/service.py
- google.py
- PageOut
- Services
- ._out
- profile/controller.py
- edit
- currencies/controller.py
- members/controller.py
- results
- clients
- mine
- checklists/controller.py
- account/controller.py
- Actor
- mine
- goals/service.py
- .build
- NetworkOut
- test_networks.py
- ItemsOut
- reports/controller.py
- Limiter
- AuthService
- GoalTemplateOut
- google/controller.py
- avant-api
- networks/controller.py
- uuid
- UserOut
- team
- image
- commissions/controller.py
- disable
- uuid
- main.py
- .trusted_uow
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- Settings
- add_note
- .preview_invitation
- .page_saved
- source_files
- Actor
- .of
- logs.py
- middleware.py
- delete_template
- CeleryQueue
- test_api_keys.py
- ReportService
- GoalService
- Actor
- mine
- security.py
- UnitOfWorkFactory
- person
- image
- test_api.py
- _xlsx_cell
- NetworkDetailOut
- GoalService
- Actor
- .__init__
- .of
- MemoryCounter
- client_image
- events
- edit_image
- images.py
- avant-api
- new_owner
- edit_image
- dollars
- document_response
- Settings
- events.py
- ClientService

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 146 edges
2. `PageOut` - 145 edges
3. `_csrf()` - 130 edges
4. `_onboard_owner()` - 130 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 118 edges
8. `ReportService` - 75 edges
9. `_staff()` - 64 edges
10. `page_out()` - 59 edges

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

## Communities (188 total, 93 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.07
Nodes (34): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+26 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - ".uow"
Cohesion: 0.05
Nodes (22): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+14 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - ".show"
Cohesion: 0.09
Nodes (4): show(), CostLineOut, MonthResultOut, ResultTotalsOut

### Community 6 - "CommissionService"
Cohesion: 0.07
Nodes (15): adjust(), create_rule(), delete_rule(), person(), rules(), set_settings(), settings(), update_rule() (+7 more)

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
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "_member_client"
Cohesion: 0.08
Nodes (20): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person() (+12 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "networks/controller.py"
Cohesion: 0.12
Nodes (9): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService (+1 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.08
Nodes (9): require_session(), create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut (+1 more)

### Community 17 - "InvitationOut"
Cohesion: 0.11
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

### Community 22 - "costs/controller.py"
Cohesion: 0.18
Nodes (3): client_info(), image_response(), image_upload()

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "export.py"
Cohesion: 0.15
Nodes (5): to_csv(), _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.23
Nodes (12): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas(), test_groone_reports_sum_every_client(), test_page_views_query_by_hour() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.07
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 31 - "company/controller.py"
Cohesion: 0.14
Nodes (6): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 32 - ".uow"
Cohesion: 0.21
Nodes (10): CapturingMailer, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_option_lists_keep_the_permissions() (+2 more)

### Community 36 - "tasks/controller.py"
Cohesion: 0.07
Nodes (18): change(), comment(), create(), task(), tasks(), support_task_service(), TaskClientOut, TaskCommentIn (+10 more)

### Community 38 - "get"
Cohesion: 0.10
Nodes (19): available_months(), create_service(), get(), mine(), payment_details(), service_options(), services(), invoice_service() (+11 more)

### Community 39 - "to_xlsx"
Cohesion: 0.20
Nodes (5): dimension_text(), _header(), _metric_label(), _rows(), to_xlsx()

### Community 40 - "test_account.py"
Cohesion: 0.11
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 41 - "company/controller.py"
Cohesion: 0.18
Nodes (3): show(), CompanyDetailOut, image_url()

### Community 42 - "ReportResultOut"
Cohesion: 0.11
Nodes (3): query(), run(), ReportResultOut

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "MemoryBucket"
Cohesion: 0.14
Nodes (7): BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 45 - "networks/service.py"
Cohesion: 0.13
Nodes (4): NetworkIn, ServiceAccountOut, SyncRunOut, enqueue_sync()

### Community 46 - "_onboard_owner"
Cohesion: 0.27
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "google.py"
Cohesion: 0.18
Nodes (8): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), test_client_can_disable(), test_login_with_mfa(), test_staff_must_set_up_mfa_first()

### Community 49 - "PageOut"
Cohesion: 0.04
Nodes (13): index(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, results(), client_result_service() (+5 more)

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 52 - "profile/controller.py"
Cohesion: 0.20
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): API first e chaves de API, Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.07
Nodes (15): api_key_actor(), bearer_token(), get_actor(), get_auth(), get_session_actor(), get_session_auth(), optional_auth(), require_report() (+7 more)

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+7 more)

### Community 56 - "results"
Cohesion: 0.18
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 57 - "clients"
Cohesion: 0.12
Nodes (7): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut

### Community 58 - "mine"
Cohesion: 0.05
Nodes (14): CsrfFailed, GoogleUnavailable, NoActiveCompany, QueryTooHeavy, GoogleAuth, new_verifier(), check_csrf(), google_callback() (+6 more)

### Community 59 - "checklists/controller.py"
Cohesion: 0.19
Nodes (6): checklist(), mark(), site_checklist_service(), ChecklistDetailOut, ChecklistOut, SiteChecklistService

### Community 60 - "account/controller.py"
Cohesion: 0.08
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "Actor"
Cohesion: 0.10
Nodes (12): add_item(), delete(), delete_service(), issue(), pay(), pdf(), remove_item(), return_to_draft() (+4 more)

### Community 62 - "mine"
Cohesion: 0.12
Nodes (5): health(), metrics(), ready(), health_service(), HealthService

### Community 63 - "goals/service.py"
Cohesion: 0.22
Nodes (8): ClientIn, ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn, ManagerChangeOut, OwnerChangeIn

### Community 64 - ".build"
Cohesion: 0.14
Nodes (6): _google(), _mailer(), NoEvents, RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 66 - "test_networks.py"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 67 - "ItemsOut"
Cohesion: 0.05
Nodes (26): ad_units(), assign_sites(), classify(), classify_many(), create(), delete(), index(), link() (+18 more)

### Community 68 - "reports/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 69 - "Limiter"
Cohesion: 0.06
Nodes (8): TooManyAttempts, Counter, Limiter, RedisCounter, Rule, _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 72 - "google/controller.py"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 74 - "networks/controller.py"
Cohesion: 0.15
Nodes (9): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs(), network_service() (+1 more)

### Community 75 - "uuid"
Cohesion: 0.20
Nodes (18): _onboard_owner(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+10 more)

### Community 76 - "UserOut"
Cohesion: 0.18
Nodes (7): Modelo de dados, Resumo, users(), PersonOut, PeopleService, person_out(), UserOut

### Community 77 - "team"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "commissions/controller.py"
Cohesion: 0.08
Nodes (8): mine(), _month(), team(), CommissionMonthOut, MonthIn, MyCommissionsOut, PersonMonthOut, create()

### Community 81 - "disable"
Cohesion: 0.20
Nodes (3): disable(), enable(), reset_mfa()

### Community 83 - "uuid"
Cohesion: 0.14
Nodes (12): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), _kpi(), _run() (+4 more)

### Community 85 - "main.py"
Cohesion: 0.10
Nodes (15): client(), engine(), mailer(), _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login() (+7 more)

### Community 86 - ".trusted_uow"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.05
Nodes (18): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), get_invitation(), login(), me() (+10 more)

### Community 89 - "Settings"
Cohesion: 0.10
Nodes (5): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 92 - "add_note"
Cohesion: 0.18
Nodes (4): add_note(), check(), delete_note(), edit_note()

### Community 95 - ".page_saved"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 96 - "source_files"
Cohesion: 0.10
Nodes (8): audit(), cancel_owner(), change_status(), client_options(), edit_client_image(), manager_change(), remove_client_image(), AuditOut

### Community 98 - "Actor"
Cohesion: 0.17
Nodes (5): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 128 - ".of"
Cohesion: 0.14
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 135 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 136 - "ReportService"
Cohesion: 0.05
Nodes (28): Bucket, alert_service(), catalog(), create(), templates(), update(), report_service(), CustomCatalogMetricOut (+20 more)

### Community 139 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 142 - "security.py"
Cohesion: 0.05
Nodes (19): Estrutura, Services, get_services(), require(), dependency(), require_staff(), require_staff_member(), TaskQueue (+11 more)

### Community 144 - "person"
Cohesion: 0.08
Nodes (14): RecordingQueue, _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads() (+6 more)

### Community 146 - "test_api.py"
Cohesion: 0.13
Nodes (11): Sent, _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format() (+3 more)

### Community 150 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 152 - "Actor"
Cohesion: 0.11
Nodes (9): create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned(), show() (+1 more)

### Community 165 - "avant-api"
Cohesion: 0.40
Nodes (4): avant-api, Como funciona, Desenvolvimento, Imagem

### Community 171 - "edit_image"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 180 - "Settings"
Cohesion: 0.08
Nodes (5): Settings, google_redirects(), GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 184 - "events.py"
Cohesion: 0.16
Nodes (5): channel(), EventSource, _parse(), sse(), EventService

### Community 194 - "ClientService"
Cohesion: 0.20
Nodes (5): client_teams(), client_service(), ClientMemberOut, ClientService, CompanyRefOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1766 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **93 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `.of`, `contracts/controller.py`, `roles/controller.py`, `.uow`, `Actor`, `CommissionService`, `test_events.py`, `ReportService`, `_month`, `CapturingMailer`, `.uow`, `security.py`, `networks/controller.py`, `api_keys/controller.py`, `InvitationOut`, `custom_metrics/controller.py`, `CompanyService`, `GoalService`, `goals/controller.py`, `mfa/controller.py`, `company/controller.py`, `tasks/controller.py`, `get`, `.__init__`, `test_account.py`, `networks/service.py`, `.__init__`, `networks/service.py`, `.__init__`, `PageOut`, `Services`, `profile/controller.py`, `currencies/controller.py`, `members/controller.py`, `mine`, `checklists/controller.py`, `account/controller.py`, `goals/service.py`, `ClientService`, `ItemsOut`, `reports/controller.py`, `Limiter`, `networks/controller.py`, `UserOut`, `image`, `.__init__`, `auth/controller.py`?**
  _High betweenness centrality (0.138) - this node is a cross-community bridge._
- **Are the 107 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 107 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.07315315315315316 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `contracts/controller.py`, `roles/controller.py`, `.uow`, `Actor`, `test_events.py`, `ReportService`, `_month`, `CapturingMailer`, `.uow`, `networks/controller.py`, `UnitOfWorkFactory`, `api_keys/controller.py`, `security.py`, `InvitationOut`, `CompanyService`, `GoalService`, `tasks/controller.py`, `get`, `test_account.py`, `networks/service.py`, `Services`, `members/controller.py`, `checklists/controller.py`, `Actor`, `goals/service.py`, `test_networks.py`, `ClientService`, `ItemsOut`, `GoalTemplateOut`, `networks/controller.py`, `UserOut`, `image`, `.preview_invitation`, `.page_saved`, `source_files`, `Actor`, `.show`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07146087743102668 - nodes in this community are weakly interconnected._