# Graph Report - avant-api  (2026-11-05)

## Corpus Check
- 296 files · ~91,621 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4018 nodes · 11064 edges · 204 communities (105 shown, 99 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1845 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `dc7d7e68`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- conftest.py
- test_members_without_schedules_manage_only_see_what_they_receive
- roles/controller.py
- DashboardService
- Actor
- UserOut
- google.py
- gam_tools/dto.py
- steps
- _month
- Avant: models do MVP
- test_gam_tools.py
- InvoiceService
- .uow
- shared/dto.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- invitations/controller.py
- clients/controller.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- install
- goals/controller.py
- verify
- image
- clean_code.py
- _onboard_owner
- mfa/controller.py
- Avant: repositório e plano do MVP
- ReportService
- GamToolService
- Actor
- session-start.sh
- avant-api
- security.py
- .save_rule
- CommissionSettingsOut
- gam_tools/controller.py
- documents/controller.py
- test_networks.py
- months
- Services
- networks/service.py
- download
- Services
- commissions/dto.py
- get
- edit
- currencies/controller.py
- members/controller.py
- contracts/controller.py
- clients
- OwnerInvitationOut
- _onboard_owner
- account/controller.py
- GamToolNetworkOut
- .approve
- commissions/controller.py
- main.py
- limits.py
- Actor
- ItemsOut
- export.py
- limits.py
- main.py
- google.py
- avant-api
- networks/controller.py
- TaskQueue
- test_account.py
- profile/controller.py
- image
- download
- people/controller.py
- test_events.py
- uuid
- InvoiceServiceOut
- avant_core_access_models
- _marketing_client
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- Counter
- SiteListOut
- test_api_keys.py
- google/controller.py
- middleware.py
- _csrf
- SiteService
- GoalService
- tasks/controller.py
- .change_password
- do_reset_password
- TaskDetailOut
- do_reset_password
- image
- image_response
- FiscalDataOut
- ClientService
- UserOut
- users
- mine
- .page_saved
- tasks/dto.py
- person
- gam_tools/service.py
- Arquitetura do MVP do Avant
- test_mfa.py
- .of
- delete_session
- dashboards/dependencies.py
- new_owner
- UUID
- ._out
- edit_image
- _csv_cell
- UnitOfWorkFactory
- company/controller.py
- edit_client
- mcm/service.py
- .change_password
- test_contract_crud
- .build
- tasks/dependencies.py
- document_response
- _member_client
- source_files
- delete_template
- classify
- test_events.py
- _month
- dashboards/dto.py
- test_database.py
- TaskQueue
- Actor

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 164 edges
2. `_csrf()` - 147 edges
3. `_onboard_owner()` - 147 edges
4. `PageOut` - 145 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 118 edges
8. `ReportService` - 79 edges
9. `_staff()` - 65 edges
10. `page_out()` - 59 edges

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

## Communities (204 total, 99 thin omitted)

### Community 0 - "conftest.py"
Cohesion: 0.08
Nodes (5): refresh_levels(), test_deployed_cookies_use_the_host_prefix(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 1 - "test_members_without_schedules_manage_only_see_what_they_receive"
Cohesion: 0.38
Nodes (3): _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.06
Nodes (19): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+11 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "UserOut"
Cohesion: 0.11
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 6 - "google.py"
Cohesion: 0.07
Nodes (11): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), configure_logging(), JsonFormatter, observe() (+3 more)

### Community 7 - "gam_tools/dto.py"
Cohesion: 0.13
Nodes (5): GamStepOut, GamToolClientOut, GamToolPersonOut, GamToolRunNetworkOut, GamToolSiteOut

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "test_gam_tools.py"
Cohesion: 0.13
Nodes (10): _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list(), test_staff_marks_checks_and_writes_notes() (+2 more)

### Community 12 - "InvoiceService"
Cohesion: 0.10
Nodes (10): add_item(), create(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft() (+2 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "shared/dto.py"
Cohesion: 0.08
Nodes (9): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService (+1 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "invitations/controller.py"
Cohesion: 0.09
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "clients/controller.py"
Cohesion: 0.17
Nodes (11): client_service(), ClientDetailOut, ClientIn, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+3 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "install"
Cohesion: 0.25
Nodes (7): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "_onboard_owner"
Cohesion: 0.09
Nodes (33): _onboard_owner(), _checkouts(), test_report_requests_use_few_connections(), test_busy_export_answers_503_with_retry_after(), test_export_slots_refuse_a_third_export_while_two_run(), _day(), _metrics(), _row() (+25 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "ReportService"
Cohesion: 0.05
Nodes (38): catalog(), create(), create_from_template(), delete(), duplicate(), export(), pin(), pinned() (+30 more)

### Community 31 - "GamToolService"
Cohesion: 0.18
Nodes (4): start(), GamToolRunIn, GamToolRunOut, GamToolService

### Community 32 - "Actor"
Cohesion: 0.10
Nodes (10): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), clients(), edit_client_image() (+2 more)

### Community 36 - "security.py"
Cohesion: 0.06
Nodes (24): CompanyChanged, CsrfFailed, ExportsBusy, NoActiveCompany, QueryTooHeavy, RateLimited, api_key_actor(), bearer_token() (+16 more)

### Community 38 - ".save_rule"
Cohesion: 0.15
Nodes (3): update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 41 - "gam_tools/controller.py"
Cohesion: 0.16
Nodes (6): ads_txt(), install(), network(), run(), runs(), gam_tool_service()

### Community 42 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "test_networks.py"
Cohesion: 0.23
Nodes (8): Sent, _owner_invite(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 44 - "months"
Cohesion: 0.15
Nodes (5): checklists(), months(), summary(), ChecklistMonthOut, SiteChecklistService

### Community 45 - "Services"
Cohesion: 0.04
Nodes (22): _google(), _mailer(), Services, NoEvents, PillowImageProcessor, MemoryBucket, get_services(), Settings (+14 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 49 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "Services"
Cohesion: 0.09
Nodes (8): add(), delete(), edit(), notes(), ClientNoteIn, ClientNoteOut, NotePersonOut, ClientNoteService

### Community 51 - "commissions/dto.py"
Cohesion: 0.17
Nodes (4): CommissionMonthOut, CommissionSettingsIn, dollars(), MonthIn

### Community 52 - "get"
Cohesion: 0.11
Nodes (9): metrics(), available_months(), get(), mine(), payment_details(), pdf(), service_options(), services() (+1 more)

### Community 53 - "edit"
Cohesion: 0.10
Nodes (17): API first e chaves de API, Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa (+9 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 57 - "clients"
Cohesion: 0.13
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 58 - "OwnerInvitationOut"
Cohesion: 0.17
Nodes (5): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 59 - "_onboard_owner"
Cohesion: 0.14
Nodes (18): CapturingMailer, test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session(), test_team_invitation_flow(), test_validation_error_format() (+10 more)

### Community 60 - "account/controller.py"
Cohesion: 0.20
Nodes (8): get_sessions(), account_service(), ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut, SessionOut, AccountService

### Community 61 - "GamToolNetworkOut"
Cohesion: 0.19
Nodes (3): networks(), GamToolNetworkDetailOut, GamToolNetworkOut

### Community 63 - "commissions/controller.py"
Cohesion: 0.13
Nodes (8): adjust(), create_rule(), delete_rule(), rules(), settings(), commission_service(), AdjustmentIn, CommissionService

### Community 64 - "main.py"
Cohesion: 0.14
Nodes (4): health(), ready(), health_service(), HealthService

### Community 65 - "limits.py"
Cohesion: 0.05
Nodes (12): _check_jpeg_size(), Bucket, BucketResult, BucketRule, RedisBucket, RedisCounter, _exercise(), test_memory_bucket() (+4 more)

### Community 66 - "Actor"
Cohesion: 0.15
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistDetailOut, ChecklistMarkIn (+2 more)

### Community 67 - "ItemsOut"
Cohesion: 0.19
Nodes (8): site_service(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "export.py"
Cohesion: 0.08
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 69 - "limits.py"
Cohesion: 0.15
Nodes (8): TooManyAttempts, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "main.py"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 74 - "networks/controller.py"
Cohesion: 0.06
Nodes (16): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+8 more)

### Community 76 - "TaskQueue"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 77 - "test_account.py"
Cohesion: 0.33
Nodes (7): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 78 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "download"
Cohesion: 0.18
Nodes (6): approve(), documents(), download(), reject(), ClientDocumentsOut, RejectDocumentIn

### Community 81 - "people/controller.py"
Cohesion: 0.16
Nodes (5): disable(), enable(), reset_mfa(), people_service(), PeopleService

### Community 82 - "test_events.py"
Cohesion: 0.10
Nodes (21): client(), engine(), mailer(), _jpeg(), _sharpness(), _striped_logo(), test_phone_photos_pass_and_huge_pngs_are_refused(), test_phone_rotation_from_exif_is_kept() (+13 more)

### Community 83 - "uuid"
Cohesion: 0.14
Nodes (13): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), _kpi(), _run() (+5 more)

### Community 84 - "InvoiceServiceOut"
Cohesion: 0.27
Nodes (4): create_service(), update_service(), InvoiceServiceIn, InvoiceServiceOut

### Community 85 - "avant_core_access_models"
Cohesion: 0.06
Nodes (8): results(), ClientResultService, show(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut, default_period()

### Community 86 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.20
Nodes (9): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Imagem da Empresa, Issues, Modelo de dados, Regras, Resumo (+1 more)

### Community 88 - "auth/controller.py"
Cohesion: 0.04
Nodes (20): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), get_invitation(), login(), me() (+12 more)

### Community 91 - "SiteListOut"
Cohesion: 0.11
Nodes (5): create(), delete(), index(), site_options(), SiteListOut

### Community 92 - "test_api_keys.py"
Cohesion: 0.33
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 94 - "google/controller.py"
Cohesion: 0.04
Nodes (13): GoogleUnavailable, GoogleAuth, new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), google_redirects() (+5 more)

### Community 95 - "middleware.py"
Cohesion: 0.16
Nodes (11): save_payment_details(), update_item(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut (+3 more)

### Community 96 - "_csrf"
Cohesion: 0.06
Nodes (42): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+34 more)

### Community 97 - "SiteService"
Cohesion: 0.14
Nodes (3): unlinked(), AdUnitOut, SiteService

### Community 98 - "GoalService"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 102 - "tasks/controller.py"
Cohesion: 0.18
Nodes (3): change(), task(), tasks()

### Community 127 - "do_reset_password"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 128 - "TaskDetailOut"
Cohesion: 0.19
Nodes (4): comment(), create(), TaskDetailOut, SupportTaskService

### Community 133 - "ClientService"
Cohesion: 0.24
Nodes (4): client_teams(), ClientMemberOut, ClientService, CompanyRefOut

### Community 134 - "UserOut"
Cohesion: 0.14
Nodes (3): PersonOut, person_out(), UserOut

### Community 135 - "users"
Cohesion: 0.15
Nodes (11): Modelo de dados, Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação (+3 more)

### Community 136 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), MyCommissionsOut

### Community 137 - ".page_saved"
Cohesion: 0.14
Nodes (3): ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 138 - "tasks/dto.py"
Cohesion: 0.20
Nodes (10): TaskClientOut, TaskCommentIn, TaskDataIn, TaskEventOut, TaskIn, TaskNetworkOut, TaskOut, TaskPatchIn (+2 more)

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.38
Nodes (11): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+3 more)

### Community 149 - "UUID"
Cohesion: 0.15
Nodes (5): ad_units(), members(), show(), sites_of_member(), SiteMemberOut

### Community 155 - "UnitOfWorkFactory"
Cohesion: 0.04
Nodes (5): UnitOfWorkFactory, index(), AuditService, AuditOut, RoleRefOut

### Community 160 - "company/controller.py"
Cohesion: 0.07
Nodes (12): edit(), edit_fiscal(), edit_image(), fiscal(), remove_image(), show(), company_service(), CompanyDetailOut (+4 more)

### Community 163 - "mcm/service.py"
Cohesion: 0.06
Nodes (8): assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut, page_out(), PageOut

### Community 165 - "test_contract_crud"
Cohesion: 0.38
Nodes (3): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission()

### Community 175 - "_member_client"
Cohesion: 0.10
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 180 - "classify"
Cohesion: 0.29
Nodes (3): classify(), classify_many(), link()

### Community 184 - "test_events.py"
Cohesion: 0.08
Nodes (9): channel(), EventSource, _parse(), sse(), StreamLimiter, events(), event_service(), EventService (+1 more)

### Community 188 - "dashboards/dto.py"
Cohesion: 0.12
Nodes (7): templates(), DashboardChoiceIn, DashboardRunOut, DashboardTemplateOut, HomeDashboardOut, WidgetErrorOut, LabelOut

### Community 189 - "test_database.py"
Cohesion: 0.14
Nodes (6): engine_options(), _settings(), test_every_connection_has_a_statement_and_idle_timeout(), test_pool_is_bounded_and_waits_little(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 191 - "TaskQueue"
Cohesion: 0.11
Nodes (6): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskQueue

### Community 195 - "Actor"
Cohesion: 0.06
Nodes (3): export_saved(), export_slot(), _statement_timeout()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1829 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **99 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `TaskDetailOut`, `roles/controller.py`, `DashboardService`, `Actor`, `ClientService`, `UserOut`, `_month`, `tasks/dto.py`, `InvoiceService`, `.uow`, `gam_tools/service.py`, `shared/dto.py`, `api_keys/controller.py`, `invitations/controller.py`, `clients/controller.py`, `custom_metrics/controller.py`, `goals/controller.py`, `mfa/controller.py`, `ReportService`, `GamToolService`, `company/controller.py`, `.__init__`, `mcm/service.py`, `.save_rule`, `documents/controller.py`, `months`, `Services`, `networks/service.py`, `.__init__`, `Services`, `.__init__`, `currencies/controller.py`, `contracts/controller.py`, `clients`, `goals/service.py`, `members/controller.py`, `dashboards/dto.py`, `account/controller.py`, `.approve`, `TaskQueue`, `commissions/controller.py`, `.__init__`, `.__init__`, `.__init__`, `Actor`, `.__init__`, `.__init__`, `ItemsOut`, `networks/controller.py`, `.__init__`, `profile/controller.py`, `image`, `people/controller.py`, `avant_core_access_models`, `auth/controller.py`, `google/controller.py`, `middleware.py`, `SiteService`, `do_reset_password`?**
  _High betweenness centrality (0.137) - this node is a cross-community bridge._
- **Are the 123 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 123 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `conftest.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08221153846153846 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `mcm/service.py` to `TaskDetailOut`, `roles/controller.py`, `DashboardService`, `Actor`, `ClientService`, `UserOut`, `users`, `_month`, `tasks/dto.py`, `InvoiceService`, `.uow`, `gam_tools/service.py`, `shared/dto.py`, `api_keys/controller.py`, `invitations/controller.py`, `clients/controller.py`, `UnitOfWorkFactory`, `ReportService`, `GamToolService`, `Actor`, `gam_tools/controller.py`, `months`, `Services`, `get`, `goals/service.py`, `contracts/controller.py`, `members/controller.py`, `OwnerInvitationOut`, `dashboards/dto.py`, `GamToolNetworkOut`, `Actor`, `ItemsOut`, `main.py`, `networks/controller.py`, `image`, `people/controller.py`, `avant_core_access_models`, `SiteListOut`, `middleware.py`, `SiteService`, `GoalService`, `tasks/controller.py`, `do_reset_password`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07231638418079096 - nodes in this community are weakly interconnected._