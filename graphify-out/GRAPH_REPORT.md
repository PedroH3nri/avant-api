# Graph Report - avant-api  (2026-11-05)

## Corpus Check
- 297 files · ~91,849 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4036 nodes · 11100 edges · 200 communities (106 shown, 94 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1851 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6b0c4120`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- conftest.py
- test_alerts.py
- roles/controller.py
- DashboardService
- Actor
- PageOut
- gam_tools/controller.py
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
- main.py
- goals/controller.py
- verify
- image
- clean_code.py
- _onboard_owner
- mfa/controller.py
- Avant: repositório e plano do MVP
- reports/service.py
- invoices/controller.py
- Actor
- session-start.sh
- avant-api
- security.py
- BaseModel
- .save_rule
- CommissionService
- Actor
- test_company_image.py
- documents/controller.py
- CapturingMailer
- checklists/controller.py
- security.py
- uuid
- networks/service.py
- SiteChecklistService
- download
- Services
- commissions/dto.py
- .of
- edit
- currencies/controller.py
- members/controller.py
- contracts/controller.py
- clients
- OwnerInvitationOut
- _onboard_owner
- AccountService
- mine
- commissions/controller.py
- GamToolService
- limits.py
- Actor
- ItemsOut
- export.py
- limits.py
- .of
- GoalTemplateOut
- ExportsBusy
- avant-api
- networks/controller.py
- company/controller.py
- shared/dto.py
- profile/controller.py
- image
- download
- people/controller.py
- test_events.py
- uuid
- InvoiceService
- results/dto.py
- _marketing_client
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- Counter
- SiteListOut
- GamToolRunOut
- google/controller.py
- invoices/controller.py
- _csrf
- SiteService
- goals/controller.py
- tasks/controller.py
- GoalService
- updates
- TaskDetailOut
- .start
- image_response
- test_site_category_and_responsible
- ClientService
- UserOut
- users
- mine
- tasks/dto.py
- person
- Actor
- Arquitetura do MVP do Avant
- test_mfa.py
- AuditOut
- DashboardTemplateOut
- dashboards/dependencies.py
- account/dto.py
- UUID
- ReportService
- clients
- .show
- client_image
- edit_client
- mcm/service.py
- .change_password
- .of_detail
- delete_template
- forgot_password
- UnitOfWorkFactory
- document_response
- .available_months
- _member_client
- classify
- events.py
- _month
- TaskPatchIn
- main.py
- TaskQueue
- .payee_details

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 165 edges
2. `_onboard_owner()` - 148 edges
3. `_csrf()` - 147 edges
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

## Communities (200 total, 94 thin omitted)

### Community 0 - "conftest.py"
Cohesion: 0.09
Nodes (4): refresh_levels(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 1 - "test_alerts.py"
Cohesion: 0.35
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.06
Nodes (24): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+16 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "PageOut"
Cohesion: 0.06
Nodes (11): index(), audit_service(), AuditService, invite(), options(), staff(), staff_service(), StaffInviteIn (+3 more)

### Community 6 - "gam_tools/controller.py"
Cohesion: 0.16
Nodes (7): install(), network(), networks(), run(), runs(), GamToolNetworkDetailOut, GamToolNetworkOut

### Community 7 - "gam_tools/dto.py"
Cohesion: 0.13
Nodes (4): GamStepOut, GamToolPersonOut, GamToolRunNetworkOut, GamToolSiteOut

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
Cohesion: 0.12
Nodes (11): RecordingQueue, _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list() (+3 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "shared/dto.py"
Cohesion: 0.09
Nodes (8): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "invitations/controller.py"
Cohesion: 0.11
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "clients/controller.py"
Cohesion: 0.16
Nodes (13): client_service(), ClientDetailOut, ClientIn, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+5 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "main.py"
Cohesion: 0.05
Nodes (20): CompanyChanged, CsrfFailed, error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected() (+12 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.15
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "_onboard_owner"
Cohesion: 0.11
Nodes (17): _checkouts(), test_report_requests_use_few_connections(), test_busy_export_answers_503_with_retry_after(), _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait() (+9 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.06
Nodes (12): get_cookies(), delete_session(), do_reset_password(), confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn (+4 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "reports/service.py"
Cohesion: 0.05
Nodes (17): QueryTooHeavy, catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn (+9 more)

### Community 31 - "invoices/controller.py"
Cohesion: 0.08
Nodes (15): metrics(), add_item(), create(), delete(), delete_service(), get(), issue(), mine() (+7 more)

### Community 32 - "Actor"
Cohesion: 0.14
Nodes (8): cancel_owner(), change_status(), client(), client_options(), edit_client_image(), new_owner(), owner_invitations(), remove_client_image()

### Community 36 - "security.py"
Cohesion: 0.08
Nodes (18): api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor(), get_auth(), get_session_actor(), get_session_auth() (+10 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - ".save_rule"
Cohesion: 0.12
Nodes (7): adjust(), create_rule(), delete_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 39 - "CommissionService"
Cohesion: 0.16
Nodes (4): set_settings(), settings(), CommissionSettingsOut, CommissionService

### Community 41 - "test_company_image.py"
Cohesion: 0.10
Nodes (13): _check_jpeg_size(), PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image() (+5 more)

### Community 42 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "CapturingMailer"
Cohesion: 0.14
Nodes (17): CapturingMailer, Sent, _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission() (+9 more)

### Community 44 - "checklists/controller.py"
Cohesion: 0.17
Nodes (10): site_checklist_service(), ChecklistDetailOut, ChecklistMarkIn, ChecklistMonthOut, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut (+2 more)

### Community 45 - "security.py"
Cohesion: 0.05
Nodes (15): Services, NoEvents, Bucket, get_services(), account_service(), event_service(), google_redirects(), ready() (+7 more)

### Community 46 - "uuid"
Cohesion: 0.25
Nodes (15): _owner_invite(), _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+7 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 49 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "commissions/dto.py"
Cohesion: 0.24
Nodes (3): CommissionMonthOut, CommissionSettingsIn, dollars()

### Community 52 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 53 - "edit"
Cohesion: 0.10
Nodes (17): API first e chaves de API, Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa (+9 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "OwnerInvitationOut"
Cohesion: 0.12
Nodes (4): invite_owner(), register_client(), resend_owner(), owner_invitation_out()

### Community 59 - "_onboard_owner"
Cohesion: 0.13
Nodes (22): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited(), _bearer() (+14 more)

### Community 60 - "AccountService"
Cohesion: 0.14
Nodes (5): do_change_password(), get_sessions(), revoke_others(), SessionOut, AccountService

### Community 61 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 63 - "commissions/controller.py"
Cohesion: 0.19
Nodes (3): commission_service(), AdjustmentIn, MonthIn

### Community 64 - "GamToolService"
Cohesion: 0.19
Nodes (4): ads_txt(), gam_tool_service(), AdsTxtOut, GamToolService

### Community 65 - "limits.py"
Cohesion: 0.06
Nodes (9): BucketResult, BucketRule, MemoryBucket, MemoryCounter, RedisBucket, RedisCounter, _exercise(), test_memory_bucket() (+1 more)

### Community 66 - "Actor"
Cohesion: 0.11
Nodes (8): add_note(), check(), checklist(), checklists(), delete_note(), edit_note(), months(), summary()

### Community 67 - "ItemsOut"
Cohesion: 0.19
Nodes (8): site_service(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "export.py"
Cohesion: 0.07
Nodes (13): JsonFormatter, dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx() (+5 more)

### Community 69 - "limits.py"
Cohesion: 0.18
Nodes (8): TooManyAttempts, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 71 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 72 - "ExportsBusy"
Cohesion: 0.22
Nodes (4): ExportsBusy, export_slot(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 74 - "networks/controller.py"
Cohesion: 0.06
Nodes (17): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+9 more)

### Community 76 - "company/controller.py"
Cohesion: 0.09
Nodes (12): edit(), edit_fiscal(), edit_image(), fiscal(), remove_image(), show(), company_service(), CompanyDetailOut (+4 more)

### Community 78 - "profile/controller.py"
Cohesion: 0.14
Nodes (6): edit_appearance(), image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "download"
Cohesion: 0.14
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 81 - "people/controller.py"
Cohesion: 0.14
Nodes (6): disable(), enable(), reset_mfa(), people_service(), PersonOut, PeopleService

### Community 82 - "test_events.py"
Cohesion: 0.16
Nodes (15): client(), engine(), mailer(), query(), _collect(), _event(), ListEvents, test_events_route() (+7 more)

### Community 83 - "uuid"
Cohesion: 0.18
Nodes (9): _form(), _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit() (+1 more)

### Community 84 - "InvoiceService"
Cohesion: 0.17
Nodes (5): create_service(), service_options(), update_service(), InvoiceServiceOut, InvoiceService

### Community 85 - "results/dto.py"
Cohesion: 0.12
Nodes (5): results(), client_result_service(), ClientResultService, ResultsOut, default_period()

### Community 86 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.20
Nodes (9): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Imagem da Empresa, Issues, Modelo de dados, Regras, Resumo (+1 more)

### Community 88 - "auth/controller.py"
Cohesion: 0.05
Nodes (19): SessionCookies, accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company() (+11 more)

### Community 91 - "SiteListOut"
Cohesion: 0.11
Nodes (5): create(), delete(), index(), site_options(), SiteListOut

### Community 94 - "google/controller.py"
Cohesion: 0.04
Nodes (18): GoogleFailed, GoogleUnavailable, challenge(), _claims(), GoogleAuth, GoogleOAuth, identity_from_id_token(), new_verifier() (+10 more)

### Community 95 - "invoices/controller.py"
Cohesion: 0.21
Nodes (9): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceSummaryOut, ReturnedOut, ReturnIn (+1 more)

### Community 96 - "_csrf"
Cohesion: 0.07
Nodes (37): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+29 more)

### Community 97 - "SiteService"
Cohesion: 0.14
Nodes (3): unlinked(), AdUnitOut, SiteService

### Community 98 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 102 - "tasks/controller.py"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 123 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "TaskDetailOut"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 132 - "test_site_category_and_responsible"
Cohesion: 0.31
Nodes (5): _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search(), test_site_category_and_responsible(), test_sites_and_assignment()

### Community 133 - "ClientService"
Cohesion: 0.24
Nodes (4): client_teams(), ClientMemberOut, ClientService, CompanyRefOut

### Community 134 - "UserOut"
Cohesion: 0.11
Nodes (4): person_out(), edit_image(), remove_image(), UserOut

### Community 135 - "users"
Cohesion: 0.15
Nodes (11): Modelo de dados, Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação (+3 more)

### Community 138 - "tasks/dto.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.21
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+6 more)

### Community 146 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 148 - "account/dto.py"
Cohesion: 0.31
Nodes (4): ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut

### Community 149 - "UUID"
Cohesion: 0.15
Nodes (5): ad_units(), members(), show(), sites_of_member(), SiteMemberOut

### Community 150 - "ReportService"
Cohesion: 0.06
Nodes (20): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+12 more)

### Community 163 - "mcm/service.py"
Cohesion: 0.10
Nodes (6): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService

### Community 175 - "_member_client"
Cohesion: 0.10
Nodes (15): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client() (+7 more)

### Community 180 - "classify"
Cohesion: 0.29
Nodes (3): classify(), classify_many(), link()

### Community 184 - "events.py"
Cohesion: 0.08
Nodes (7): channel(), EventSource, _parse(), sse(), StreamLimiter, events(), EventService

### Community 185 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 189 - "main.py"
Cohesion: 0.05
Nodes (13): engine_options(), _google(), _mailer(), Settings, CeleryQueue, GoogleRedirects, test_closing_deployed_cookies_keeps_them_secure(), test_deployed_cookies_use_the_host_prefix() (+5 more)

### Community 191 - "TaskQueue"
Cohesion: 0.14
Nodes (6): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskQueue

### Community 196 - ".payee_details"
Cohesion: 0.21
Nodes (3): payment_details(), save_payment_details(), PayeeDetailsOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1837 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **94 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `TaskDetailOut`, `roles/controller.py`, `DashboardService`, `Actor`, `PageOut`, `ClientService`, `_month`, `tasks/dto.py`, `InvoiceService`, `.uow`, `shared/dto.py`, `api_keys/controller.py`, `invitations/controller.py`, `clients/controller.py`, `custom_metrics/controller.py`, `ReportService`, `goals/controller.py`, `goals/service.py`, `mfa/controller.py`, `reports/service.py`, `.__init__`, `mcm/service.py`, `CommissionService`, `documents/controller.py`, `checklists/controller.py`, `security.py`, `.__init__`, `networks/service.py`, `SiteChecklistService`, `.__init__`, `Services`, `.__init__`, `.__init__`, `currencies/controller.py`, `contracts/controller.py`, `clients`, `members/controller.py`, `AccountService`, `TaskQueue`, `commissions/controller.py`, `GamToolService`, `.__init__`, `Actor`, `ItemsOut`, `.__init__`, `networks/controller.py`, `.__init__`, `company/controller.py`, `profile/controller.py`, `image`, `download`, `people/controller.py`, `InvoiceService`, `results/dto.py`, `auth/controller.py`, `google/controller.py`, `invoices/controller.py`, `SiteService`, `GoalService`?**
  _High betweenness centrality (0.155) - this node is a cross-community bridge._
- **Are the 124 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 124 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `conftest.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0882936507936508 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `TaskDetailOut`, `roles/controller.py`, `DashboardService`, `Actor`, `ClientService`, `gam_tools/controller.py`, `users`, `_month`, `tasks/dto.py`, `InvoiceService`, `.uow`, `shared/dto.py`, `api_keys/controller.py`, `AuditOut`, `clients/controller.py`, `invitations/controller.py`, `ReportService`, `clients`, `goals/service.py`, `reports/service.py`, `invoices/controller.py`, `Actor`, `mcm/service.py`, `checklists/controller.py`, `SiteChecklistService`, `Services`, `members/controller.py`, `contracts/controller.py`, `OwnerInvitationOut`, `GamToolService`, `Actor`, `ItemsOut`, `GoalTemplateOut`, `networks/controller.py`, `shared/dto.py`, `image`, `people/controller.py`, `InvoiceService`, `results/dto.py`, `SiteListOut`, `GamToolRunOut`, `invoices/controller.py`, `SiteService`, `goals/controller.py`, `tasks/controller.py`, `GoalService`?**
  _High betweenness centrality (0.074) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07562008469449485 - nodes in this community are weakly interconnected._