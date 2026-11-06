# Graph Report - avant-api  (2026-11-06)

## Corpus Check
- 303 files · ~93,874 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 4113 nodes · 11267 edges · 224 communities (119 shown, 105 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1879 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0d00e8bf`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _marketing_client
- MemberOut
- roles/controller.py
- .uow
- AlertService
- audit/controller.py
- GamToolService
- GoalTemplateOut
- steps
- schedules/controller.py
- Avant: conexão com o GAM
- test_api.py
- .trusted_uow
- GroupService
- avant_core_access_models
- Groone Avant: contexto do projeto
- api_keys/controller.py
- PageOut
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- Settings
- dashboard_templates/controller.py
- invoice_pdf.py
- http.py
- clean_code.py
- delete_template
- mfa/controller.py
- Avant: repositório e plano do MVP
- reports/service.py
- events.py
- test_sites.py
- session-start.sh
- avant-api
- require_staff
- BaseModel
- enqueue_sync
- test_key_values.py
- ClientService
- test_company_image.py
- documents/controller.py
- CapturingMailer
- SiteChecklistService
- security.py
- _onboard_owner
- views/controller.py
- checklists/controller.py
- download
- client_notes/controller.py
- mine
- AuthService
- edit
- currencies/controller.py
- members/controller.py
- .build
- ItemsOut
- pydantic
- test_api_keys.py
- account/controller.py
- Actor
- .save_rule
- install
- InvoiceService
- Actor
- export.py
- Limiter
- ReportService
- .of_detail
- avant-api
- NetworkService
- mcm/service.py
- CompanyService
- Actor
- networks/controller.py
- costs/controller.py
- client_documents/controller.py
- test_events.py
- uuid
- invite_owner
- results/dto.py
- sites/controller.py
- Avant: grupos na Empresa e imagem da Empresa
- key_values/controller.py
- limits.py
- index
- GoalService
- GoogleService
- RecordingQueue
- dollars
- goals/controller.py
- test_networks.py
- UserOut
- updates
- auth/controller.py
- O que já tem
- checklists/service.py
- Counter
- contracts/controller.py
- page_out
- shared/dto.py
- FakeGoogle
- SiteService
- invoices/service.py
- time
- ContractOut
- Arquitetura do MVP do Avant
- conftest.py
- contracts/dto.py
- get
- _csrf
- UnitOfWorkFactory
- UUID
- .run_guarded
- SupportTaskService
- tasks/controller.py
- main.py
- members/service.py
- company/controller.py
- _month
- mcm/controller.py
- RedisEvents
- TaskDetailOut
- MemberService
- people/service.py
- document_response
- commissions/controller.py
- test_account.py
- _member_client
- show
- PayeeDetailsOut
- profile/controller.py
- tasks/dto.py
- ResultsOut
- .assign
- internal/results/controller.py
- events
- mine
- pytest
- CommissionService
- ContractService
- internal/results/service.py
- modules/results/controller.py
- Actor
- CommissionRuleOut
- templates
- person
- results
- FiscalDataIn
- .page_saved
- test_checklists_need_permission
- image
- test_staff_sees_client_networks_sites_and_revenue_status
- capped
- TaskPatchIn
- _contract_fields
- source_files

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

## Communities (224 total, 105 thin omitted)

### Community 0 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 1 - "MemberOut"
Cohesion: 0.13
Nodes (5): invite(), options(), StaffInviteIn, StaffService, MemberOut

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - ".uow"
Cohesion: 0.05
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "audit/controller.py"
Cohesion: 0.18
Nodes (3): index(), audit_service(), AuditService

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (19): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+11 more)

### Community 7 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: conexão com o GAM"
Cohesion: 0.05
Nodes (35): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+27 more)

### Community 11 - "test_api.py"
Cohesion: 0.19
Nodes (12): _error_code(), test_csrf_is_required_for_writes(), test_deployed_cookies_use_the_host_prefix(), test_every_write_route_refuses_another_site(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session() (+4 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "avant_core_access_models"
Cohesion: 0.10
Nodes (9): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, people_service() (+1 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.10
Nodes (9): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut (+1 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "Settings"
Cohesion: 0.11
Nodes (6): engine_options(), Settings, test_closing_deployed_cookies_keeps_them_secure(), _settings(), test_every_connection_has_a_statement_and_idle_timeout(), test_pool_is_bounded_and_waits_little()

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.13
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "http.py"
Cohesion: 0.18
Nodes (3): client_info(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (10): get_session_auth(), confirm(), disable(), new_recovery_codes(), setup(), verify(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "reports/service.py"
Cohesion: 0.05
Nodes (18): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn (+10 more)

### Community 31 - "events.py"
Cohesion: 0.13
Nodes (6): channel(), EventSource, _parse(), sse(), StreamLimiter, EventService

### Community 32 - "test_sites.py"
Cohesion: 0.25
Nodes (5): _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search(), test_site_category_and_responsible(), test_sites_and_assignment()

### Community 36 - "require_staff"
Cohesion: 0.21
Nodes (6): require(), dependency(), require_report(), require_session(), require_staff(), dependency()

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 39 - "test_key_values.py"
Cohesion: 0.17
Nodes (5): _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 40 - "ClientService"
Cohesion: 0.11
Nodes (19): edit_client(), new_owner(), register_client(), resend_owner(), client_service(), ClientDetailOut, ClientIn, ClientMemberOut (+11 more)

### Community 41 - "test_company_image.py"
Cohesion: 0.10
Nodes (13): _check_jpeg_size(), PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image() (+5 more)

### Community 42 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "CapturingMailer"
Cohesion: 0.15
Nodes (14): CapturingMailer, client(), engine(), mailer(), query(), test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages() (+6 more)

### Community 44 - "SiteChecklistService"
Cohesion: 0.10
Nodes (6): checklists(), months(), summary(), site_checklist_service(), ChecklistMonthOut, SiteChecklistService

### Community 45 - "security.py"
Cohesion: 0.04
Nodes (27): Services, CompanyChanged, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site() (+19 more)

### Community 46 - "_onboard_owner"
Cohesion: 0.07
Nodes (40): refresh_levels(), _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _onboard_owner(), _checkouts() (+32 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "checklists/controller.py"
Cohesion: 0.16
Nodes (8): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistMarkIn, ChecklistNoteIn

### Community 49 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 52 - "AuthService"
Cohesion: 0.08
Nodes (3): get_invitation(), auth_service(), AuthService

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.15
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.14
Nodes (6): edit(), index(), leave(), options(), remove(), set_permissions()

### Community 56 - ".build"
Cohesion: 0.06
Nodes (7): _google(), _mailer(), NoEvents, MemoryKeyValueBuffer, RedisKeyValueBuffer, MemoryCounter, CeleryQueue

### Community 57 - "ItemsOut"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "pydantic"
Cohesion: 0.05
Nodes (13): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), google_start(), google_redirects() (+5 more)

### Community 59 - "test_api_keys.py"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 63 - ".save_rule"
Cohesion: 0.14
Nodes (6): adjust(), create_rule(), delete_rule(), settings(), update_rule(), CommissionRuleIn

### Community 65 - "install"
Cohesion: 0.25
Nodes (7): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 66 - "InvoiceService"
Cohesion: 0.20
Nodes (6): create_service(), update_service(), invoice_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 67 - "Actor"
Cohesion: 0.17
Nodes (5): classify(), classify_many(), create(), site_options(), sites_of_member()

### Community 68 - "export.py"
Cohesion: 0.08
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 69 - "Limiter"
Cohesion: 0.17
Nodes (7): Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "ReportService"
Cohesion: 0.06
Nodes (17): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned() (+9 more)

### Community 72 - ".of_detail"
Cohesion: 0.10
Nodes (4): ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "NetworkService"
Cohesion: 0.15
Nodes (4): index(), options(), NetworkDetailOut, NetworkService

### Community 75 - "mcm/service.py"
Cohesion: 0.13
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 76 - "CompanyService"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 77 - "Actor"
Cohesion: 0.10
Nodes (8): audit(), cancel_owner(), change_status(), client_image(), client_options(), clients(), edit_client_image(), manager_change()

### Community 78 - "networks/controller.py"
Cohesion: 0.15
Nodes (7): connect(), disconnect(), service_account(), show(), sync(), sync_runs(), network_service()

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "client_documents/controller.py"
Cohesion: 0.14
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 82 - "test_events.py"
Cohesion: 0.28
Nodes (10): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports(), test_redis_source_delivers_published_messages() (+2 more)

### Community 83 - "uuid"
Cohesion: 0.22
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 85 - "results/dto.py"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 86 - "sites/controller.py"
Cohesion: 0.19
Nodes (9): site_service(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn (+1 more)

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "key_values/controller.py"
Cohesion: 0.10
Nodes (8): RateLimited, KeyValueBuffer, Bucket, cors(), preflight(), receive(), KeyValueIn, receive_key_values()

### Community 89 - "limits.py"
Cohesion: 0.06
Nodes (13): ExportsBusy, BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, create_app(), _exercise() (+5 more)

### Community 92 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 94 - "GoogleService"
Cohesion: 0.07
Nodes (6): GoogleUnavailable, GoogleAuth, google_callback(), google_status(), google_unlink(), GoogleService

### Community 96 - "RecordingQueue"
Cohesion: 0.21
Nodes (9): RecordingQueue, _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites() (+1 more)

### Community 97 - "dollars"
Cohesion: 0.12
Nodes (3): dollars(), available_months(), AvailableMonthOut

### Community 98 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 102 - "test_networks.py"
Cohesion: 0.26
Nodes (8): Sent, _owner_invite(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 123 - "UserOut"
Cohesion: 0.14
Nodes (4): edit_image(), remove_image(), ProfileService, UserOut

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "auth/controller.py"
Cohesion: 0.08
Nodes (15): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), login(), me(), set_active_company() (+7 more)

### Community 129 - "O que já tem"
Cohesion: 0.20
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics()

### Community 132 - "contracts/controller.py"
Cohesion: 0.17
Nodes (6): contract(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract()

### Community 133 - "page_out"
Cohesion: 0.12
Nodes (3): client_teams(), owner_invitations(), page_out()

### Community 134 - "shared/dto.py"
Cohesion: 0.11
Nodes (3): AuditOut, FiscalDataOut, RoleRefOut

### Community 136 - "SiteService"
Cohesion: 0.15
Nodes (5): ad_units(), link(), unlinked(), AdUnitOut, SiteService

### Community 138 - "invoices/service.py"
Cohesion: 0.18
Nodes (7): service_options(), InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, ReturnedOut, ReturnIn, ServiceItemIn

### Community 139 - "time"
Cohesion: 0.09
Nodes (6): observe(), _route_template(), health(), ready(), health_service(), HealthService

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "conftest.py"
Cohesion: 0.09
Nodes (16): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+8 more)

### Community 145 - "contracts/dto.py"
Cohesion: 0.16
Nodes (6): ContractIn, ContractNetworkRefOut, ContractSummaryOut, _network_ref(), ClientRefOut, ContractClientRefOut

### Community 146 - "get"
Cohesion: 0.11
Nodes (14): add_item(), create(), delete(), delete_service(), get(), issue(), mine(), pay() (+6 more)

### Community 147 - "_csrf"
Cohesion: 0.07
Nodes (38): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+30 more)

### Community 149 - "UUID"
Cohesion: 0.16
Nodes (4): assign_sites(), delete(), members(), SiteMemberOut

### Community 150 - ".run_guarded"
Cohesion: 0.07
Nodes (4): QueryTooHeavy, ReportQueryIn, export_slot(), _statement_timeout()

### Community 152 - "SupportTaskService"
Cohesion: 0.15
Nodes (4): tasks(), support_task_service(), TaskOut, SupportTaskService

### Community 153 - "tasks/controller.py"
Cohesion: 0.22
Nodes (4): change(), comment(), create(), task()

### Community 158 - "members/service.py"
Cohesion: 0.20
Nodes (4): DirectPermissionIn, DirectPermissionOut, MemberPatchIn, MemberPermissionsIn

### Community 160 - "company/controller.py"
Cohesion: 0.18
Nodes (4): company_service(), CompanyFiscalOut, CompanyPatchIn, image_url()

### Community 162 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 163 - "mcm/controller.py"
Cohesion: 0.12
Nodes (8): confirm_network(), register_network(), unassigned_networks(), mcm_service(), ClientNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 166 - "MemberService"
Cohesion: 0.21
Nodes (3): show(), MemberDetailOut, MemberService

### Community 167 - "people/service.py"
Cohesion: 0.11
Nodes (10): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), PersonOut, PeopleService (+2 more)

### Community 172 - "commissions/controller.py"
Cohesion: 0.31
Nodes (5): AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn

### Community 174 - "test_account.py"
Cohesion: 0.33
Nodes (7): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 175 - "_member_client"
Cohesion: 0.10
Nodes (15): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client() (+7 more)

### Community 177 - "PayeeDetailsOut"
Cohesion: 0.21
Nodes (3): payment_details(), save_payment_details(), PayeeDetailsOut

### Community 178 - "profile/controller.py"
Cohesion: 0.13
Nodes (4): edit_appearance(), image(), AppearanceIn, AppearanceOut

### Community 182 - ".assign"
Cohesion: 0.16
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 188 - "pytest"
Cohesion: 0.22
Nodes (4): TooManyAttempts, test_stream_limiter_caps_each_person_and_the_process(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 189 - "CommissionService"
Cohesion: 0.20
Nodes (3): set_settings(), commission_service(), CommissionService

### Community 190 - "ContractService"
Cohesion: 0.24
Nodes (4): contract_networks(), contract_service(), ContractNetworkOut, ContractService

### Community 201 - "FiscalDataIn"
Cohesion: 0.18
Nodes (4): edit_fiscal(), edit_image(), fiscal(), FiscalDataIn

### Community 203 - "test_checklists_need_permission"
Cohesion: 0.39
Nodes (4): _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list(), test_staff_marks_checks_and_writes_notes()

### Community 210 - "test_staff_sees_client_networks_sites_and_revenue_status"
Cohesion: 0.38
Nodes (3): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1868 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **105 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `MemberOut`, `checklists/service.py`, `.uow`, `AlertService`, `audit/controller.py`, `GamToolService`, `roles/controller.py`, `SiteService`, `.__init__`, `invoices/service.py`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `avant_core_access_models`, `api_keys/controller.py`, `contracts/dto.py`, `PageOut`, `custom_metrics/controller.py`, `dashboard_templates/controller.py`, `SupportTaskService`, `mfa/controller.py`, `members/service.py`, `reports/service.py`, `company/controller.py`, `mcm/controller.py`, `MemberService`, `people/service.py`, `ClientService`, `documents/controller.py`, `SiteChecklistService`, `commissions/controller.py`, `views/controller.py`, `client_notes/controller.py`, `tasks/dto.py`, `AuthService`, `profile/controller.py`, `currencies/controller.py`, `internal/results/controller.py`, `.__init__`, `pydantic`, `ItemsOut`, `account/controller.py`, `CommissionService`, `ContractService`, `internal/results/service.py`, `avant_core_shared_clock`, `modules/results/controller.py`, `InvoiceService`, `ReportService`, `.__init__`, `NetworkService`, `mcm/service.py`, `CompanyService`, `costs/controller.py`, `client_documents/controller.py`, `goals/service.py`, `sites/controller.py`, `.__init__`, `GoalService`, `.__init__`, `GoogleService`, `.__init__`, `UserOut`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Are the 127 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 127 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `MemberOut` be split into smaller, more focused modules?**
  _Cohesion score 0.12648221343873517 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `MemberOut`, `checklists/service.py`, `.uow`, `AlertService`, `audit/controller.py`, `shared/dto.py`, `page_out`, `contracts/controller.py`, `GamToolService`, `GoalTemplateOut`, `invoices/service.py`, `.trusted_uow`, `GroupService`, `ContractOut`, `avant_core_access_models`, `api_keys/controller.py`, `contracts/dto.py`, `get`, `roles/controller.py`, `SupportTaskService`, `tasks/controller.py`, `members/service.py`, `reports/service.py`, `mcm/controller.py`, `MemberService`, `people/service.py`, `ClientService`, `.of`, `SiteChecklistService`, `security.py`, `schedules/controller.py`, `SiteService`, `checklists/controller.py`, `client_notes/controller.py`, `tasks/dto.py`, `internal/results/controller.py`, `members/controller.py`, `ContractService`, `Actor`, `internal/results/service.py`, `avant_core_shared_clock`, `InvoiceService`, `results`, `NetworkService`, `mcm/service.py`, `.page_saved`, `Actor`, `networks/controller.py`, `costs/controller.py`, `goals/service.py`, `sites/controller.py`, `index`, `GoalService`, `goals/controller.py`?**
  _High betweenness centrality (0.083) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08176100628930817 - nodes in this community are weakly interconnected._