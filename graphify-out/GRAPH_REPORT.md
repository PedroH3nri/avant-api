# Graph Report - avant-api  (2026-11-04)

## Corpus Check
- 290 files · ~88,704 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3909 nodes · 10721 edges · 203 communities (109 shown, 94 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1802 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `aee3475d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- contracts/controller.py
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
- test_alerts.py
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- limits.py
- _onboard_owner
- session-start.sh
- avant-api
- Settings
- tasks/controller.py
- invoices/controller.py
- networks/controller.py
- test_account.py
- company/controller.py
- company/controller.py
- install
- MemoryBucket
- networks/service.py
- mine
- networks/service.py
- test_mfa.py
- PageOut
- Services
- test_staff_manage_templates_and_clients_see_them_by_role
- profile/controller.py
- edit
- currencies/controller.py
- members/controller.py
- results
- clients
- mine
- UnitOfWorkFactory
- account/controller.py
- get
- Services
- ClientService
- main.py
- NetworkOut
- test_networks.py
- ItemsOut
- reports/controller.py
- limits.py
- .trusted_uow
- GoalTemplateOut
- google/controller.py
- avant-api
- NetworkService
- uuid
- CommissionService
- team
- document_response
- image
- mine
- disable
- commissions/dto.py
- uuid
- .__init__
- test_events.py
- goals/controller.py
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- Settings
- .of_view
- add_note
- .preview_invitation
- source_files
- .save_payee_details
- networks/service.py
- ReportQueryIn
- .of
- members/service.py
- .save_rule
- AdUnitOut
- delete_template
- .of
- container.py
- CapturingMailer
- ReportService
- shared/dto.py
- index
- GoalService
- dashboards/dependencies.py
- UnitOfWorkFactory
- person
- UUID
- _marketing_client
- export.py
- Actor
- CompanyService
- GoalService
- Actor
- image
- test_networks.py
- MemoryCounter
- client_image
- delete
- edit_image
- image
- person
- .show
- test_checklists_need_permission
- .classify
- index
- .assign
- delete_template
- team
- .build
- events/controller.py
- commissions/dependencies.py
- members/dependencies.py
- _month
- page_out

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 152 edges
2. `PageOut` - 145 edges
3. `_onboard_owner()` - 136 edges
4. `_csrf()` - 135 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 118 edges
8. `ReportService` - 79 edges
9. `_staff()` - 64 edges
10. `page_out()` - 59 edges

## Surprising Connections (you probably didn't know these)
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/modules/internal/people/controller.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py
- `Pipeline` --references--> `main()`  [INFERRED]
  docs/decisoes/07-repositorios-e-plano.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (203 total, 94 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.07
Nodes (37): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+29 more)

### Community 1 - "contracts/controller.py"
Cohesion: 0.06
Nodes (25): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+17 more)

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
Cohesion: 0.11
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 6 - "commissions/controller.py"
Cohesion: 0.16
Nodes (6): adjust(), create_rule(), delete_rule(), rules(), AdjustmentIn, MonthIn

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
Cohesion: 0.09
Nodes (22): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+14 more)

### Community 11 - "_member_client"
Cohesion: 0.11
Nodes (16): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_site_category_and_responsible() (+8 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+6 more)

### Community 14 - "networks/controller.py"
Cohesion: 0.15
Nodes (8): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, PageOut

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.14
Nodes (6): create(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.10
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

### Community 22 - "costs/controller.py"
Cohesion: 0.18
Nodes (3): client_info(), image_response(), image_upload()

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.21
Nodes (14): _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas() (+6 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.07
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "limits.py"
Cohesion: 0.06
Nodes (8): create(), create_from_template(), duplicate(), pinned(), update(), SavedReportIn, SavedReportOut, ReportService

### Community 32 - "_onboard_owner"
Cohesion: 0.23
Nodes (16): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format(), test_costs_and_reports_come_in_pages() (+8 more)

### Community 36 - "Settings"
Cohesion: 0.12
Nodes (5): Settings, client(), engine(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 37 - "tasks/controller.py"
Cohesion: 0.05
Nodes (18): change(), comment(), create(), task(), tasks(), support_task_service(), TaskClientOut, TaskCommentIn (+10 more)

### Community 38 - "invoices/controller.py"
Cohesion: 0.20
Nodes (10): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut (+2 more)

### Community 39 - "networks/controller.py"
Cohesion: 0.16
Nodes (7): disconnect(), options(), service_account(), show(), sync(), sync_runs(), network_service()

### Community 40 - "test_account.py"
Cohesion: 0.11
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 42 - "company/controller.py"
Cohesion: 0.23
Nodes (5): company_service(), CompanyDetailOut, CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 43 - "install"
Cohesion: 0.27
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 44 - "MemoryBucket"
Cohesion: 0.13
Nodes (8): Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 45 - "networks/service.py"
Cohesion: 0.08
Nodes (18): CsrfFailed, NoActiveCompany, QueryTooHeavy, RateLimited, api_key_actor(), bearer_token(), check_csrf(), get_actor() (+10 more)

### Community 46 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "test_mfa.py"
Cohesion: 0.40
Nodes (8): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_staff_must_set_up_mfa_first(), test_verify_is_limited_by_ip()

### Community 49 - "PageOut"
Cohesion: 0.10
Nodes (6): require_staff(), results(), client_result_service(), ClientResultService, ResultsOut, default_period()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "test_staff_manage_templates_and_clients_see_them_by_role"
Cohesion: 0.38
Nodes (3): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company()

### Community 52 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.08
Nodes (10): edit(), index(), leave(), options(), remove(), set_permissions(), show(), MemberDetailOut (+2 more)

### Community 56 - "results"
Cohesion: 0.10
Nodes (3): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "mine"
Cohesion: 0.05
Nodes (11): GoogleUnavailable, GoogleAuth, google_callback(), google_start(), google_status(), google_unlink(), google_redirects(), google_service() (+3 more)

### Community 60 - "account/controller.py"
Cohesion: 0.08
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "get"
Cohesion: 0.17
Nodes (6): available_months(), get(), mine(), payment_details(), pdf(), services()

### Community 62 - "Services"
Cohesion: 0.08
Nodes (9): Services, get_services(), audit_service(), group_service(), ready(), health_service(), HealthService, result_service() (+1 more)

### Community 63 - "ClientService"
Cohesion: 0.10
Nodes (17): edit_client(), edit_client_image(), register_client(), client_service(), ClientDetailOut, ClientIn, ClientMemberOut, ClientOptionOut (+9 more)

### Community 64 - "main.py"
Cohesion: 0.09
Nodes (6): configure_logging(), JsonFormatter, observe(), _route_template(), create_app(), health()

### Community 65 - "NetworkOut"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "test_networks.py"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 67 - "ItemsOut"
Cohesion: 0.25
Nodes (7): AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "reports/controller.py"
Cohesion: 0.09
Nodes (8): documents(), download(), upload(), document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 69 - "limits.py"
Cohesion: 0.06
Nodes (8): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - ".trusted_uow"
Cohesion: 0.08
Nodes (4): client_teams(), manager_change(), owner_invitations(), owner_invitation_out()

### Community 71 - "GoalTemplateOut"
Cohesion: 0.14
Nodes (4): create_template(), template_options(), GoalTemplateIn, GoalTemplateOut

### Community 72 - "google/controller.py"
Cohesion: 0.09
Nodes (9): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), FakeGoogle, _jwt() (+1 more)

### Community 74 - "NetworkService"
Cohesion: 0.15
Nodes (5): connect(), index(), NetworkDetailOut, NetworkIn, NetworkService

### Community 75 - "uuid"
Cohesion: 0.15
Nodes (19): _owner_invite(), _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast(), _ana_id(), _report(), test_chart_options_keep_metric_styles() (+11 more)

### Community 76 - "CommissionService"
Cohesion: 0.22
Nodes (5): set_settings(), settings(), update_rule(), CommissionSettingsOut, CommissionService

### Community 77 - "team"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 81 - "disable"
Cohesion: 0.11
Nodes (9): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+1 more)

### Community 82 - "commissions/dto.py"
Cohesion: 0.15
Nodes (4): CommissionMonthOut, CommissionRuleIn, CommissionSettingsIn, dollars()

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - ".__init__"
Cohesion: 0.17
Nodes (5): create_service(), service_options(), update_service(), InvoiceServiceOut, InvoiceService

### Community 85 - "test_events.py"
Cohesion: 0.16
Nodes (9): channel(), _parse(), sse(), _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit() (+1 more)

### Community 86 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.06
Nodes (18): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), get_invitation(), login(), me() (+10 more)

### Community 89 - "Settings"
Cohesion: 0.09
Nodes (6): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 91 - ".of_view"
Cohesion: 0.14
Nodes (7): ad_units(), delete(), link(), show(), site_options(), sites_of_member(), unlinked()

### Community 92 - "add_note"
Cohesion: 0.10
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), site_checklist_service(), ChecklistDetailOut (+2 more)

### Community 94 - ".preview_invitation"
Cohesion: 0.10
Nodes (3): clients(), ClientRefOut, image_url()

### Community 96 - "source_files"
Cohesion: 0.11
Nodes (9): cancel_owner(), change_status(), client(), client_image(), client_options(), invite_owner(), new_owner(), remove_client_image() (+1 more)

### Community 128 - ".of"
Cohesion: 0.11
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 129 - "members/service.py"
Cohesion: 0.23
Nodes (4): DirectPermissionIn, DirectPermissionOut, MemberPatchIn, MemberPermissionsIn

### Community 133 - ".of"
Cohesion: 0.14
Nodes (3): edit_image(), remove_image(), UserOut

### Community 134 - "container.py"
Cohesion: 0.08
Nodes (3): PillowImageProcessor, CeleryQueue, RecordingQueue

### Community 135 - "CapturingMailer"
Cohesion: 0.11
Nodes (15): CapturingMailer, mailer(), Sent, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password() (+7 more)

### Community 136 - "ReportService"
Cohesion: 0.05
Nodes (18): CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+10 more)

### Community 137 - "shared/dto.py"
Cohesion: 0.12
Nodes (3): ClientProfileOut, FiscalDataOut, RoleRefOut

### Community 139 - "GoalService"
Cohesion: 0.23
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 144 - "person"
Cohesion: 0.23
Nodes (6): _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _agent(), test_staff_opens_assigns_and_comments_on_tasks()

### Community 145 - "UUID"
Cohesion: 0.21
Nodes (5): add_item(), create(), issue(), pay(), return_to_draft()

### Community 146 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 147 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 148 - "Actor"
Cohesion: 0.22
Nodes (3): role_goals(), templates(), RoleGoalOut

### Community 149 - "CompanyService"
Cohesion: 0.22
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 152 - "Actor"
Cohesion: 0.08
Nodes (13): catalog(), delete(), export(), export_saved(), index(), pin(), query_batch(), run() (+5 more)

### Community 155 - "image"
Cohesion: 0.14
Nodes (5): edit_fiscal(), edit_image(), fiscal(), image(), remove_image()

### Community 158 - "test_networks.py"
Cohesion: 0.47
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 161 - "client_image"
Cohesion: 0.31
Nodes (4): _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client()

### Community 162 - "delete"
Cohesion: 0.22
Nodes (3): delete(), delete_service(), remove_item()

### Community 171 - "test_checklists_need_permission"
Cohesion: 0.39
Nodes (4): _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list(), test_staff_marks_checks_and_writes_notes()

### Community 178 - ".assign"
Cohesion: 0.25
Nodes (5): Atribuição de sites, GAM, Networks, Sites e ad units, assign_sites()

### Community 183 - ".build"
Cohesion: 0.14
Nodes (6): _google(), _mailer(), NoEvents, RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 184 - "events/controller.py"
Cohesion: 0.13
Nodes (4): EventSource, events(), event_service(), EventService

### Community 190 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 194 - "page_out"
Cohesion: 0.13
Nodes (3): audit(), AuditOut, page_out()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1788 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **94 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `.of`, `contracts/controller.py`, `members/service.py`, `.uow`, `Actor`, `roles/controller.py`, `test_events.py`, `ReportService`, `_month`, `GoalService`, `.uow`, `networks/controller.py`, `UnitOfWorkFactory`, `api_keys/controller.py`, `InvitationOut`, `custom_metrics/controller.py`, `CompanyService`, `GoalService`, `goals/controller.py`, `mfa/controller.py`, `limits.py`, `company/controller.py`, `tasks/controller.py`, `invoices/controller.py`, `.__init__`, `company/controller.py`, `company/controller.py`, `test_account.py`, `goals/service.py`, `networks/service.py`, `.__init__`, `PageOut`, `Services`, `profile/controller.py`, `currencies/controller.py`, `members/controller.py`, `clients`, `mine`, `.__init__`, `account/controller.py`, `Services`, `ClientService`, `.__init__`, `NetworkOut`, `.__init__`, `.__init__`, `reports/controller.py`, `limits.py`, `.trusted_uow`, `.__init__`, `ItemsOut`, `.__init__`, `NetworkService`, `CommissionService`, `image`, `disable`, `commissions/dto.py`, `.__init__`, `auth/controller.py`, `add_note`, `.__init__`, `networks/service.py`?**
  _High betweenness centrality (0.173) - this node is a cross-community bridge._
- **Are the 113 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 113 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.06947996589940324 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `networks/controller.py` to `contracts/controller.py`, `members/service.py`, `.uow`, `Actor`, `roles/controller.py`, `AdUnitOut`, `test_events.py`, `ReportService`, `_month`, `index`, `GoalService`, `shared/dto.py`, `.uow`, `api_keys/controller.py`, `InvitationOut`, `Actor`, `CompanyService`, `GoalService`, `Actor`, `tasks/controller.py`, `invoices/controller.py`, `networks/controller.py`, `test_account.py`, `goals/service.py`, `PageOut`, `Services`, `index`, `team`, `members/controller.py`, `get`, `ClientService`, `NetworkOut`, `page_out`, `test_networks.py`, `ItemsOut`, `.trusted_uow`, `GoalTemplateOut`, `NetworkService`, `image`, `disable`, `.__init__`, `goals/controller.py`, `.of_view`, `add_note`, `.preview_invitation`, `networks/service.py`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `contracts/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05727605727605728 - nodes in this community are weakly interconnected._