# Graph Report - avant-api  (2026-11-05)

## Corpus Check
- 303 files · ~93,433 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4110 nodes · 11270 edges · 197 communities (108 shown, 89 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1873 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `35462249`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _marketing_client
- test_alerts.py
- roles/controller.py
- DashboardService
- Actor
- PageOut
- GamToolService
- commissions/service.py
- steps
- _month
- Avant: models do MVP
- test_api.py
- InvoiceService
- .uow
- router.py
- Groone Avant: contexto do projeto
- api_keys/controller.py
- PageOut
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- Settings
- goals/controller.py
- verify
- image_response
- clean_code.py
- _onboard_owner
- mfa/controller.py
- Avant: repositório e plano do MVP
- reports/service.py
- events.py
- _agent
- session-start.sh
- avant-api
- require_staff
- tasks/controller.py
- CeleryQueue
- test_key_values.py
- clients/controller.py
- test_company_image.py
- documents/controller.py
- _onboard_owner
- SiteChecklistService
- security.py
- uuid
- networks/service.py
- ChecklistDetailOut
- download
- Services
- _month
- MemoryCounter
- edit
- currencies/controller.py
- members/controller.py
- typing
- clients
- key_values/service.py
- test_api_keys.py
- account/controller.py
- client_documents/controller.py
- Actor
- commissions/controller.py
- AuthService
- install
- invoices/controller.py
- sites/controller.py
- export.py
- limits.py
- Actor
- .of
- avant-api
- networks/controller.py
- create_app
- CompanyService
- Actor
- ._out
- image
- ClientDocumentsOut
- CommissionSettingsOut
- test_events.py
- uuid
- ClientService
- results/dto.py
- sites/service.py
- Avant: grupos na Empresa e imagem da Empresa
- receive
- limits.py
- SiteListOut
- UUID
- google/controller.py
- _csrf
- GoalService
- test_internal_assigns_unowned_mcm_network
- test_staff_sees_client_networks_sites_and_revenue_status
- updates
- auth/controller.py
- TaskQueue
- ProfileService
- test_contract_crud
- users
- ad_units
- checklists/service.py
- typing
- main.py
- contracts/controller.py
- Arquitetura do MVP do Avant
- test_mfa.py
- shared/dto.py
- get
- test_who_sees_and_changes_invoices
- InvoiceServiceOut
- SiteService
- Actor
- .save_payee_details
- image
- company/controller.py
- ClientOut
- ExportsBusy
- mcm/service.py
- .change_password
- team
- UserOut
- verify
- document_response
- person
- _member_client
- SiteDetailOut
- UserOut
- .of
- SiteOut
- TooManyAttempts
- .build
- is_exempt
- edit_image
- commissions/dto.py

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 168 edges
2. `_csrf()` - 150 edges
3. `_onboard_owner()` - 150 edges
4. `PageOut` - 145 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 123 edges
8. `ReportService` - 79 edges
9. `_staff()` - 67 edges
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

## Communities (197 total, 89 thin omitted)

### Community 0 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 1 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company()

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "PageOut"
Cohesion: 0.09
Nodes (5): index(), audit_service(), AuditService, AuditOut, page_out()

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (20): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+12 more)

### Community 7 - "commissions/service.py"
Cohesion: 0.15
Nodes (3): update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (21): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+13 more)

### Community 11 - "test_api.py"
Cohesion: 0.11
Nodes (3): _error_code(), test_deployed_cookies_use_the_host_prefix(), test_every_write_route_refuses_another_site()

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "router.py"
Cohesion: 0.08
Nodes (9): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService (+1 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.13
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.04
Nodes (16): UnitOfWorkFactory, invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, cancel() (+8 more)

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
Cohesion: 0.07
Nodes (9): engine_options(), _mailer(), SessionCookies, get_cookies(), Settings, test_closing_deployed_cookies_keeps_them_secure(), _settings(), test_every_connection_has_a_statement_and_idle_timeout() (+1 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "image_response"
Cohesion: 0.13
Nodes (3): image(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 27 - "_onboard_owner"
Cohesion: 0.09
Nodes (21): client(), engine(), mailer(), refresh_levels(), _checkouts(), test_report_requests_use_few_connections(), query(), _day() (+13 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (8): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut, MfaService

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "reports/service.py"
Cohesion: 0.05
Nodes (30): alert_service(), create(), pinned(), query_batch(), templates(), update(), report_service(), CustomCatalogMetricOut (+22 more)

### Community 31 - "events.py"
Cohesion: 0.16
Nodes (4): channel(), EventSource, _parse(), sse()

### Community 32 - "_agent"
Cohesion: 0.22
Nodes (6): _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list(), test_staff_marks_checks_and_writes_notes(), _agent(), test_staff_opens_assigns_and_comments_on_tasks()

### Community 36 - "require_staff"
Cohesion: 0.06
Nodes (25): CompanyChanged, CsrfFailed, NoActiveCompany, QueryTooHeavy, RateLimited, api_key_actor(), bearer_token(), check_csrf() (+17 more)

### Community 37 - "tasks/controller.py"
Cohesion: 0.05
Nodes (18): change(), comment(), create(), task(), tasks(), support_task_service(), TaskClientOut, TaskCommentIn (+10 more)

### Community 38 - "CeleryQueue"
Cohesion: 0.17
Nodes (3): CeleryQueue, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 39 - "test_key_values.py"
Cohesion: 0.31
Nodes (4): _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_the_preflight_answers_with_cors()

### Community 40 - "clients/controller.py"
Cohesion: 0.18
Nodes (10): client_options(), ClientIn, ClientMemberOut, ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn (+2 more)

### Community 41 - "test_company_image.py"
Cohesion: 0.10
Nodes (13): _check_jpeg_size(), PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image() (+5 more)

### Community 42 - "documents/controller.py"
Cohesion: 0.16
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 43 - "_onboard_owner"
Cohesion: 0.14
Nodes (27): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited(), _onboard_owner() (+19 more)

### Community 44 - "SiteChecklistService"
Cohesion: 0.12
Nodes (4): months(), summary(), ChecklistMonthOut, SiteChecklistService

### Community 45 - "security.py"
Cohesion: 0.04
Nodes (14): Services, get_services(), auth_service(), cost_service(), client_note_service(), client_service(), goal_service(), mcm_service() (+6 more)

### Community 46 - "uuid"
Cohesion: 0.08
Nodes (24): CapturingMailer, Sent, test_busy_export_answers_503_with_retry_after(), _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast(), _ana_id() (+16 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "ChecklistDetailOut"
Cohesion: 0.12
Nodes (11): add_note(), check(), checklist(), checklists(), delete_note(), edit_note(), mark(), ChecklistDetailOut (+3 more)

### Community 49 - "download"
Cohesion: 0.09
Nodes (5): documents(), download(), upload(), document_service(), DocumentService

### Community 50 - "Services"
Cohesion: 0.08
Nodes (8): add(), delete(), edit(), notes(), ClientNoteIn, ClientNoteOut, NotePersonOut, ClientNoteService

### Community 51 - "_month"
Cohesion: 0.18
Nodes (3): mine(), _month(), MyCommissionsOut

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+6 more)

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "key_values/service.py"
Cohesion: 0.13
Nodes (7): Network, Segurança e limites, KeyValueBuffer, Bucket, KeyValueIn, network_code(), receive_key_values()

### Community 59 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 60 - "account/controller.py"
Cohesion: 0.08
Nodes (14): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+6 more)

### Community 61 - "client_documents/controller.py"
Cohesion: 0.13
Nodes (7): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentService

### Community 63 - "commissions/controller.py"
Cohesion: 0.13
Nodes (8): adjust(), create_rule(), delete_rule(), rules(), settings(), commission_service(), AdjustmentIn, CommissionService

### Community 64 - "AuthService"
Cohesion: 0.12
Nodes (3): get_invitation(), InvitationPreviewOut, AuthService

### Community 65 - "install"
Cohesion: 0.25
Nodes (7): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 66 - "invoices/controller.py"
Cohesion: 0.20
Nodes (9): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn (+1 more)

### Community 67 - "sites/controller.py"
Cohesion: 0.15
Nodes (8): assign_sites(), classify(), classify_many(), delete(), site_options(), unlinked(), SitePatchIn, SitesPatchIn

### Community 68 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "limits.py"
Cohesion: 0.10
Nodes (9): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+1 more)

### Community 70 - "Actor"
Cohesion: 0.10
Nodes (11): catalog(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), query() (+3 more)

### Community 72 - ".of"
Cohesion: 0.14
Nodes (3): ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 74 - "networks/controller.py"
Cohesion: 0.07
Nodes (15): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+7 more)

### Community 75 - "create_app"
Cohesion: 0.15
Nodes (4): RedisCounter, test_docs_are_closed_in_production(), test_every_response_has_the_security_headers(), test_redis_down_is_a_503_not_a_500()

### Community 76 - "CompanyService"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 77 - "Actor"
Cohesion: 0.12
Nodes (9): audit(), cancel_owner(), change_status(), client_image(), client_teams(), edit_client_image(), manager_change(), new_owner() (+1 more)

### Community 79 - "image"
Cohesion: 0.09
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 82 - "test_events.py"
Cohesion: 0.28
Nodes (10): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports(), test_redis_source_delivers_published_messages() (+2 more)

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - "ClientService"
Cohesion: 0.18
Nodes (6): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, ClientService, owner_invitation_out()

### Community 85 - "results/dto.py"
Cohesion: 0.05
Nodes (10): results(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut (+2 more)

### Community 86 - "sites/service.py"
Cohesion: 0.18
Nodes (5): link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "receive"
Cohesion: 0.31
Nodes (3): cors(), preflight(), receive()

### Community 89 - "limits.py"
Cohesion: 0.14
Nodes (7): BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 91 - "SiteListOut"
Cohesion: 0.14
Nodes (3): create(), index(), SiteListOut

### Community 92 - "UUID"
Cohesion: 0.13
Nodes (8): add_item(), create(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft()

### Community 94 - "google/controller.py"
Cohesion: 0.03
Nodes (21): _google(), GoogleFailed, GoogleUnavailable, challenge(), _claims(), GoogleAuth, GoogleOAuth, identity_from_id_token() (+13 more)

### Community 96 - "_csrf"
Cohesion: 0.07
Nodes (40): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+32 more)

### Community 98 - "GoalService"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+10 more)

### Community 102 - "test_internal_assigns_unowned_mcm_network"
Cohesion: 0.50
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 123 - "test_staff_sees_client_networks_sites_and_revenue_status"
Cohesion: 0.38
Nodes (3): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "auth/controller.py"
Cohesion: 0.12
Nodes (13): accept(), company_image(), do_logout(), login(), me(), set_active_company(), AcceptInvitationIn, ActiveCompanyIn (+5 more)

### Community 130 - "ProfileService"
Cohesion: 0.29
Nodes (3): edit_appearance(), AppearanceIn, AppearanceOut

### Community 132 - "test_contract_crud"
Cohesion: 0.38
Nodes (3): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission()

### Community 135 - "users"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo

### Community 139 - "main.py"
Cohesion: 0.07
Nodes (8): observe(), _route_template(), check_fetch_site(), create_app(), health(), ready(), health_service(), HealthService

### Community 142 - "contracts/controller.py"
Cohesion: 0.06
Nodes (25): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics(), contract() (+17 more)

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.38
Nodes (11): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+3 more)

### Community 146 - "get"
Cohesion: 0.11
Nodes (8): available_months(), get(), mine(), payment_details(), pdf(), service_options(), services(), team()

### Community 147 - "test_who_sees_and_changes_invoices"
Cohesion: 0.53
Nodes (3): test_invoice_lifecycle(), test_who_sees_and_changes_invoices(), _validated_month()

### Community 148 - "InvoiceServiceOut"
Cohesion: 0.19
Nodes (5): create_service(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 149 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 160 - "company/controller.py"
Cohesion: 0.17
Nodes (5): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 161 - "ClientOut"
Cohesion: 0.11
Nodes (4): clients(), edit_client(), register_client(), ClientOut

### Community 162 - "ExportsBusy"
Cohesion: 0.25
Nodes (3): ExportsBusy, test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 163 - "mcm/service.py"
Cohesion: 0.09
Nodes (6): assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 167 - "UserOut"
Cohesion: 0.11
Nodes (8): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out()

### Community 175 - "_member_client"
Cohesion: 0.10
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 178 - "UserOut"
Cohesion: 0.16
Nodes (4): edit_image(), remove_image(), ProfileService, UserOut

### Community 182 - "SiteOut"
Cohesion: 0.15
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 184 - "TooManyAttempts"
Cohesion: 0.15
Nodes (3): StreamLimiter, events(), test_stream_limiter_caps_each_person_and_the_process()

### Community 192 - ".build"
Cohesion: 0.11
Nodes (3): NoEvents, MemoryKeyValueBuffer, RecordingQueue

### Community 216 - "commissions/dto.py"
Cohesion: 0.17
Nodes (4): CommissionMonthOut, CommissionSettingsIn, dollars(), MonthIn

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1868 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **89 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `PageOut` to `TaskQueue`, `roles/controller.py`, `DashboardService`, `Actor`, `PageOut`, `.__init__`, `commissions/service.py`, `GamToolService`, `checklists/service.py`, `_month`, `InvoiceService`, `.uow`, `contracts/controller.py`, `router.py`, `api_keys/controller.py`, `custom_metrics/controller.py`, `InvoiceServiceOut`, `SiteService`, `Actor`, `goals/controller.py`, `.__init__`, `mfa/controller.py`, `reports/service.py`, `company/controller.py`, `mcm/service.py`, `.__init__`, `tasks/controller.py`, `UserOut`, `documents/controller.py`, `SiteChecklistService`, `security.py`, `networks/service.py`, `download`, `Services`, `UserOut`, `currencies/controller.py`, `members/controller.py`, `.__init__`, `clients`, `account/controller.py`, `client_documents/controller.py`, `commissions/controller.py`, `AuthService`, `invoices/controller.py`, `.__init__`, `networks/controller.py`, `CompanyService`, `image`, `ClientService`, `results/dto.py`, `sites/service.py`, `google/controller.py`, `GoalService`?**
  _High betweenness centrality (0.165) - this node is a cross-community bridge._
- **Are the 127 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 127 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07441016333938294 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `roles/controller.py`, `DashboardService`, `Actor`, `PageOut`, `.page`, `GamToolService`, `checklists/service.py`, `_month`, `InvoiceService`, `.uow`, `contracts/controller.py`, `router.py`, `api_keys/controller.py`, `shared/dto.py`, `get`, `InvoiceServiceOut`, `SiteService`, `reports/service.py`, `ClientOut`, `mcm/service.py`, `tasks/controller.py`, `UserOut`, `clients/controller.py`, `SiteChecklistService`, `security.py`, `ChecklistDetailOut`, `Services`, `SiteOut`, `members/controller.py`, `invoices/controller.py`, `sites/controller.py`, `networks/controller.py`, `Actor`, `image`, `ClientService`, `results/dto.py`, `sites/service.py`, `SiteListOut`, `GoalService`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `DashboardService` be split into smaller, more focused modules?**
  _Cohesion score 0.048514538558786346 - nodes in this community are weakly interconnected._