# Graph Report - avant-api  (2026-11-04)

## Corpus Check
- 291 files · ~90,409 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3961 nodes · 10887 edges · 202 communities (106 shown, 96 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1827 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0465ba9d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_gam_tools.py
- typing
- roles/controller.py
- .uow
- Actor
- ClientService
- clients/controller.py
- GamToolService
- steps
- _month
- Avant: models do MVP
- images.py
- .trusted_uow
- .uow
- PageOut
- Groone Avant: contexto do projeto
- api_keys/controller.py
- InvitationOut
- UnitOfWorkFactory
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- Actor
- goals/controller.py
- verify
- http.py
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- ReportQueryIn
- _onboard_owner
- session-start.sh
- avant-api
- UserOut
- BaseModel
- invoices/controller.py
- .save_rule
- test_account.py
- .show
- documents/controller.py
- CapturingMailer
- .of_detail
- security.py
- networks/controller.py
- networks/service.py
- SupportTaskService
- UnitOfWorkFactory
- Services
- profile/controller.py
- edit
- currencies/controller.py
- members/controller.py
- tasks/controller.py
- clients
- GoogleService
- uuid
- account/controller.py
- get
- auth/dto.py
- settings.py
- main.py
- NetworkOut
- Actor
- ItemsOut
- export.py
- limits.py
- networks/service.py
- GoalTemplateOut
- test_account.py
- avant-api
- NetworkService
- Actor
- commissions/controller.py
- mine
- CommissionService
- image
- client_documents/controller.py
- people/controller.py
- commissions/controller.py
- uuid
- router.py
- shared/dto.py
- limits.py
- Avant: grupos na Empresa e imagem da Empresa
- accept
- Actor
- results
- modules/results/controller.py
- InvoiceServiceOut
- test_gam_tools.py
- tasks
- install
- events.py
- _month
- SiteDetailOut
- CommissionService
- SiteListOut
- SiteChecklistService
- CommissionRuleOut
- test_api_keys.py
- ReportService
- commissions/dto.py
- AdUnitOut
- ClientOut
- image
- test_mfa.py
- goals/service.py
- datetime
- service_options
- SiteService
- test_saved_views.py
- ReportService
- image
- company/controller.py
- contracts/controller.py
- manager_change
- .__init__
- middleware.py
- Actor
- .service_options
- .available_months
- RedisEvents
- _member_client
- create
- mine
- .fiscal
- person
- fastapi
- clients
- TaskPatchIn
- Services
- delete_template
- .of
- .save_payee_details
- TaskQueue

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 158 edges
2. `PageOut` - 145 edges
3. `_csrf()` - 141 edges
4. `_onboard_owner()` - 141 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 118 edges
8. `ReportService` - 79 edges
9. `_staff()` - 65 edges
10. `page_out()` - 59 edges

## Surprising Connections (you probably didn't know these)
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py
- `Pipeline` --references--> `main()`  [INFERRED]
  docs/decisoes/07-repositorios-e-plano.md → scripts/clean_code.py
- `Primeira semana (23/10 a 02/11)` --references--> `main()`  [INFERRED]
  docs/decisoes/07-repositorios-e-plano.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (202 total, 96 thin omitted)

### Community 0 - "test_gam_tools.py"
Cohesion: 0.36
Nodes (4): _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads()

### Community 1 - "typing"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company()

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.05
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 6 - "clients/controller.py"
Cohesion: 0.14
Nodes (15): client_service(), ClientDetailOut, ClientIn, ClientMemberOut, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn (+7 more)

### Community 7 - "GamToolService"
Cohesion: 0.06
Nodes (18): ads_txt(), install(), network(), networks(), run(), runs(), start(), AdsTxtOut (+10 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (22): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+14 more)

### Community 11 - "images.py"
Cohesion: 0.14
Nodes (5): _check_jpeg_size(), PillowImageProcessor, _sharpness(), _striped_logo(), test_wide_and_palette_logos_stay_sharp()

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "PageOut"
Cohesion: 0.11
Nodes (8): networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, page_out(), PageOut

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.11
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "UnitOfWorkFactory"
Cohesion: 0.06
Nodes (4): UnitOfWorkFactory, index(), audit_service(), AuditService

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "Actor"
Cohesion: 0.17
Nodes (7): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), QueryTooHeavy

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "http.py"
Cohesion: 0.18
Nodes (3): client_info(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.15
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.23
Nodes (14): _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas() (+6 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "ReportQueryIn"
Cohesion: 0.07
Nodes (17): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+9 more)

### Community 32 - "_onboard_owner"
Cohesion: 0.21
Nodes (17): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session(), test_team_invitation_flow(), test_validation_error_format() (+9 more)

### Community 36 - "UserOut"
Cohesion: 0.14
Nodes (3): edit_image(), remove_image(), UserOut

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - "invoices/controller.py"
Cohesion: 0.20
Nodes (9): mine(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn (+1 more)

### Community 39 - ".save_rule"
Cohesion: 0.12
Nodes (7): adjust(), create_rule(), delete_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 40 - "test_account.py"
Cohesion: 0.10
Nodes (7): require_staff(), dependency(), invite(), options(), staff(), StaffInviteIn, StaffService

### Community 41 - ".show"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 42 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "CapturingMailer"
Cohesion: 0.12
Nodes (16): CapturingMailer, Sent, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login() (+8 more)

### Community 44 - ".of_detail"
Cohesion: 0.17
Nodes (10): site_checklist_service(), ChecklistDetailOut, ChecklistMarkIn, ChecklistMonthOut, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut (+2 more)

### Community 45 - "security.py"
Cohesion: 0.08
Nodes (18): CompanyChanged, CsrfFailed, NoActiveCompany, RateLimited, api_key_actor(), bearer_token(), check_csrf(), check_tab_company() (+10 more)

### Community 46 - "networks/controller.py"
Cohesion: 0.18
Nodes (7): connect(), disconnect(), options(), service_account(), show(), sync(), sync_runs()

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "SupportTaskService"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 49 - "UnitOfWorkFactory"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "profile/controller.py"
Cohesion: 0.20
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.12
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (16): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+8 more)

### Community 56 - "tasks/controller.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "GoogleService"
Cohesion: 0.05
Nodes (12): GoogleUnavailable, GoogleAuth, new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), google_redirects() (+4 more)

### Community 59 - "uuid"
Cohesion: 0.26
Nodes (15): test_csv_header_escapes_formulas(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+7 more)

### Community 60 - "account/controller.py"
Cohesion: 0.07
Nodes (14): SessionCookies, delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service() (+6 more)

### Community 61 - "get"
Cohesion: 0.10
Nodes (13): add_item(), create(), delete(), delete_service(), get(), issue(), pay(), pdf() (+5 more)

### Community 63 - "settings.py"
Cohesion: 0.15
Nodes (6): engine_options(), _settings(), test_every_connection_has_a_statement_and_idle_timeout(), test_pool_is_bounded_and_waits_little(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 64 - "main.py"
Cohesion: 0.14
Nodes (4): health(), ready(), health_service(), HealthService

### Community 65 - "NetworkOut"
Cohesion: 0.11
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "Actor"
Cohesion: 0.11
Nodes (8): add_note(), check(), checklist(), checklists(), delete_note(), edit_note(), months(), summary()

### Community 67 - "ItemsOut"
Cohesion: 0.19
Nodes (6): site_service(), AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 68 - "export.py"
Cohesion: 0.08
Nodes (11): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+3 more)

### Community 69 - "limits.py"
Cohesion: 0.09
Nodes (9): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+1 more)

### Community 70 - "networks/service.py"
Cohesion: 0.17
Nodes (4): network_service(), NetworkIn, ServiceAccountOut, SyncRunOut

### Community 71 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 72 - "test_account.py"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 74 - "NetworkService"
Cohesion: 0.19
Nodes (3): index(), NetworkDetailOut, NetworkService

### Community 75 - "Actor"
Cohesion: 0.13
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 76 - "commissions/controller.py"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 77 - "mine"
Cohesion: 0.17
Nodes (5): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 78 - "CommissionService"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "client_documents/controller.py"
Cohesion: 0.18
Nodes (6): approve(), documents(), download(), reject(), ClientDocumentsOut, RejectDocumentIn

### Community 81 - "people/controller.py"
Cohesion: 0.11
Nodes (9): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), PersonOut, PeopleService (+1 more)

### Community 82 - "commissions/controller.py"
Cohesion: 0.19
Nodes (3): commission_service(), AdjustmentIn, MonthIn

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 85 - "shared/dto.py"
Cohesion: 0.06
Nodes (6): show(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut, default_period()

### Community 86 - "limits.py"
Cohesion: 0.05
Nodes (11): Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, CeleryQueue, RecordingQueue (+3 more)

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "accept"
Cohesion: 0.10
Nodes (15): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), AcceptInvitationIn (+7 more)

### Community 91 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), classify(), classify_many(), delete(), show(), unlinked()

### Community 92 - "results"
Cohesion: 0.15
Nodes (3): results(), client_result_service(), ClientResultService

### Community 95 - "InvoiceServiceOut"
Cohesion: 0.17
Nodes (6): create_service(), services(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 96 - "test_gam_tools.py"
Cohesion: 0.08
Nodes (35): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+27 more)

### Community 97 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 98 - "install"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 127 - "events.py"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 128 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 130 - "CommissionService"
Cohesion: 0.16
Nodes (4): set_settings(), settings(), CommissionSettingsOut, CommissionService

### Community 131 - "SiteListOut"
Cohesion: 0.18
Nodes (3): index(), site_options(), SiteListOut

### Community 134 - "CommissionRuleOut"
Cohesion: 0.21
Nodes (8): _jpeg(), _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), test_phone_photos_pass_and_huge_pngs_are_refused(), test_phone_rotation_from_exif_is_kept(), test_upload_without_session_is_refused_before_reading_the_body()

### Community 135 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 136 - "ReportService"
Cohesion: 0.05
Nodes (20): catalog(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut (+12 more)

### Community 138 - "commissions/dto.py"
Cohesion: 0.24
Nodes (3): CommissionMonthOut, CommissionSettingsIn, dollars()

### Community 139 - "AdUnitOut"
Cohesion: 0.21
Nodes (3): ad_units(), link(), AdUnitOut

### Community 144 - "test_mfa.py"
Cohesion: 0.15
Nodes (16): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+8 more)

### Community 145 - "goals/service.py"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 146 - "datetime"
Cohesion: 0.08
Nodes (12): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query() (+4 more)

### Community 149 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 155 - "company/controller.py"
Cohesion: 0.16
Nodes (5): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 158 - "contracts/controller.py"
Cohesion: 0.06
Nodes (25): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+17 more)

### Community 163 - "manager_change"
Cohesion: 0.13
Nodes (13): client(), engine(), mailer(), _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot() (+5 more)

### Community 168 - "Actor"
Cohesion: 0.11
Nodes (10): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), edit_client_image() (+2 more)

### Community 175 - "_member_client"
Cohesion: 0.08
Nodes (19): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client() (+11 more)

### Community 184 - "fastapi"
Cohesion: 0.06
Nodes (9): channel(), EventSource, _parse(), sse(), StreamLimiter, JsonFormatter, events(), event_service() (+1 more)

### Community 189 - "Services"
Cohesion: 0.03
Nodes (17): _google(), _mailer(), Services, NoEvents, configure_logging(), get_cookies(), get_services(), Settings (+9 more)

### Community 195 - ".of"
Cohesion: 0.12
Nodes (3): query(), ReportQueryIn, ReportRowOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1804 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **96 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `CommissionService`, `.uow`, `Actor`, `SiteChecklistService`, `clients/controller.py`, `ClientService`, `.__init__`, `GamToolService`, `ReportService`, `roles/controller.py`, `.trusted_uow`, `.uow`, `PageOut`, `_month`, `api_keys/controller.py`, `InvitationOut`, `custom_metrics/controller.py`, `SiteService`, `goals/controller.py`, `ReportService`, `company/controller.py`, `mfa/controller.py`, `contracts/controller.py`, `company/controller.py`, `.__init__`, `.__init__`, `invoices/controller.py`, `test_account.py`, `.show`, `documents/controller.py`, `.of_detail`, `networks/service.py`, `SupportTaskService`, `.__init__`, `Services`, `profile/controller.py`, `currencies/controller.py`, `.__init__`, `goals/service.py`, `clients`, `GoogleService`, `tasks/controller.py`, `account/controller.py`, `members/controller.py`, `auth/dto.py`, `.__init__`, `NetworkOut`, `ItemsOut`, `limits.py`, `.__init__`, `networks/service.py`, `TaskQueue`, `NetworkService`, `image`, `people/controller.py`, `commissions/controller.py`, `shared/dto.py`, `accept`, `results`, `modules/results/controller.py`, `InvoiceServiceOut`, `events.py`?**
  _High betweenness centrality (0.113) - this node is a cross-community bridge._
- **Are the 119 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 119 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07422559906487435 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `roles/controller.py`, `.uow`, `Actor`, `SiteChecklistService`, `clients/controller.py`, `ClientService`, `GamToolService`, `ReportService`, `_month`, `SiteListOut`, `.trusted_uow`, `.uow`, `api_keys/controller.py`, `InvitationOut`, `UnitOfWorkFactory`, `SiteService`, `contracts/controller.py`, `ReportQueryIn`, `invoices/controller.py`, `Actor`, `test_account.py`, `.of_detail`, `networks/controller.py`, `SupportTaskService`, `Services`, `goals/service.py`, `tasks/controller.py`, `clients`, `members/controller.py`, `get`, `NetworkOut`, `Actor`, `ItemsOut`, `networks/service.py`, `GoalTemplateOut`, `NetworkService`, `Actor`, `mine`, `image`, `people/controller.py`, `shared/dto.py`, `Actor`, `results`, `InvoiceServiceOut`, `tasks`, `install`, `events.py`?**
  _High betweenness centrality (0.071) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `.uow` be split into smaller, more focused modules?**
  _Cohesion score 0.05007935108446482 - nodes in this community are weakly interconnected._