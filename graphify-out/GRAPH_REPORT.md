# Graph Report - avant-api  (2026-11-04)

## Corpus Check
- 290 files · ~89,831 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3934 nodes · 10812 edges · 203 communities (105 shown, 98 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1814 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6491fcf2`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- typing
- roles/controller.py
- .uow
- Actor
- ClientService
- GamToolNetworkOut
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
- PageOut
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- gam_tools/controller.py
- goals/controller.py
- verify
- http.py
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- .export_saved
- _onboard_owner
- session-start.sh
- avant-api
- .build
- BaseModel
- invoices/controller.py
- CommissionService
- test_account.py
- company/controller.py
- documents/controller.py
- test_networks.py
- checklists/dto.py
- security.py
- io
- networks/service.py
- SupportTaskService
- avant_core_shared_clock
- Services
- UserOut
- DashboardTemplateOut
- edit
- currencies/controller.py
- members/controller.py
- tasks/controller.py
- clients
- GoogleService
- uuid
- account/controller.py
- get
- networks/controller.py
- main.py
- health/controller.py
- NetworkOut
- Actor
- ItemsOut
- export.py
- limits.py
- contracts/dto.py
- GoalService
- google/controller.py
- avant-api
- NetworkService
- gam_tools/dto.py
- test_account.py
- Arquitetura do MVP do Avant
- image
- ClientDocumentService
- people/controller.py
- _month
- uuid
- clients
- modules/results/controller.py
- limits.py
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- SessionCookies
- Actor
- SiteChecklistService
- google_status
- .save_payee_details
- _staff
- tasks
- networks/service.py
- events/controller.py
- .run_guarded
- test_report_export.py
- SiteListOut
- ChecklistDetailOut
- UnitOfWorkFactory
- test_company_image.py
- test_staff_manage_templates_and_clients_see_them_by_role
- ReportService
- checklists
- AdUnitOut
- .of
- .start
- test_mfa.py
- Avant: conexão com o GAM
- test_costs_results.py
- ContractClientRefOut
- contracts/controller.py
- SiteService
- MemoryCounter
- ReportService
- company/controller.py
- company/controller.py
- ContractOut
- ContractService
- test_api_keys.py
- logs.py
- middleware.py
- .to_data
- client_image
- events
- dollars
- RedisEvents
- conftest.py
- O que já tem
- audit/controller.py
- FakeGoogle
- google/dto.py
- events/controller.py
- TaskPatchIn
- Services
- SupportTaskService
- GAM
- gam_tools/service.py

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 157 edges
2. `PageOut` - 145 edges
3. `_onboard_owner()` - 140 edges
4. `_csrf()` - 139 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 117 edges
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

## Communities (203 total, 98 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.13
Nodes (18): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+10 more)

### Community 1 - "typing"
Cohesion: 0.18
Nodes (6): RecordingQueue, _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - ".uow"
Cohesion: 0.06
Nodes (25): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+17 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "ClientService"
Cohesion: 0.05
Nodes (28): audit(), cancel_owner(), change_status(), client(), client_options(), client_teams(), edit_client(), edit_client_image() (+20 more)

### Community 6 - "GamToolNetworkOut"
Cohesion: 0.16
Nodes (5): network(), GamToolClientOut, GamToolNetworkDetailOut, GamToolNetworkOut, GamToolSiteOut

### Community 7 - "GamToolService"
Cohesion: 0.20
Nodes (4): run(), GamToolRunNetworkOut, GamToolRunOut, GamToolService

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
Cohesion: 0.13
Nodes (6): _check_jpeg_size(), PillowImageProcessor, _sharpness(), _striped_logo(), test_phone_rotation_from_exif_is_kept(), test_wide_and_palette_logos_stay_sharp()

### Community 12 - ".trusted_uow"
Cohesion: 0.08
Nodes (10): add_item(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft(), update_item() (+2 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "PageOut"
Cohesion: 0.11
Nodes (9): networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, page_out(), PageOut (+1 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.11
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService

### Community 18 - "PageOut"
Cohesion: 0.12
Nodes (3): index(), AuditService, AuditOut

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (11): check(), create(), delete(), index(), update(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn (+3 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "gam_tools/controller.py"
Cohesion: 0.19
Nodes (5): ads_txt(), install(), networks(), runs(), AdsTxtOut

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
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.23
Nodes (14): _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas() (+6 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 32 - "_onboard_owner"
Cohesion: 0.21
Nodes (17): _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session(), test_team_invitation_flow(), test_validation_error_format() (+9 more)

### Community 36 - ".build"
Cohesion: 0.08
Nodes (6): _google(), _mailer(), NoEvents, GoogleOAuth, RedisBucket, CeleryQueue

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - "invoices/controller.py"
Cohesion: 0.13
Nodes (14): create_service(), update_service(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceServiceOut (+6 more)

### Community 39 - "CommissionService"
Cohesion: 0.06
Nodes (16): adjust(), create_rule(), delete_rule(), mine(), person(), rules(), set_settings(), settings() (+8 more)

### Community 40 - "test_account.py"
Cohesion: 0.11
Nodes (7): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, InvitationOut

### Community 41 - "company/controller.py"
Cohesion: 0.17
Nodes (3): show(), CompanyDetailOut, CompanyService

### Community 42 - "documents/controller.py"
Cohesion: 0.06
Nodes (10): documents(), download(), upload(), document_service(), DocumentService, client_document_service(), document_response(), document_upload() (+2 more)

### Community 43 - "test_networks.py"
Cohesion: 0.26
Nodes (8): Sent, _owner_invite(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 44 - "checklists/dto.py"
Cohesion: 0.11
Nodes (6): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 45 - "security.py"
Cohesion: 0.06
Nodes (21): CompanyChanged, CsrfFailed, NoActiveCompany, RateLimited, api_key_actor(), bearer_token(), check_csrf(), check_tab_company() (+13 more)

### Community 46 - "io"
Cohesion: 0.24
Nodes (6): _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), test_xlsx_header_is_text_without_control_characters()

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 50 - "Services"
Cohesion: 0.08
Nodes (8): add(), delete(), edit(), notes(), ClientNoteIn, ClientNoteOut, NotePersonOut, ClientNoteService

### Community 51 - "UserOut"
Cohesion: 0.10
Nodes (7): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.16
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.08
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+6 more)

### Community 57 - "clients"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "GoogleService"
Cohesion: 0.11
Nodes (5): GoogleUnavailable, GoogleAuth, google_callback(), google_start(), GoogleService

### Community 59 - "uuid"
Cohesion: 0.14
Nodes (18): CapturingMailer, _ana_id(), _report(), test_chart_options_keep_metric_styles(), test_custom_metric_in_reports_preview_export_and_in_use(), test_export_saved_report_csv_and_xlsx(), test_invalid_reports_are_refused(), test_manager_edits_and_runs_with_own_sites_and_currency() (+10 more)

### Community 60 - "account/controller.py"
Cohesion: 0.10
Nodes (12): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn (+4 more)

### Community 61 - "get"
Cohesion: 0.13
Nodes (8): available_months(), get(), mine(), payment_details(), pdf(), service_options(), services(), team()

### Community 62 - "networks/controller.py"
Cohesion: 0.16
Nodes (7): disconnect(), index(), service_account(), show(), sync(), sync_runs(), network_service()

### Community 63 - "main.py"
Cohesion: 0.05
Nodes (16): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error(), QueryTooHeavy, configure_logging() (+8 more)

### Community 64 - "health/controller.py"
Cohesion: 0.15
Nodes (4): health(), ready(), health_service(), HealthService

### Community 65 - "NetworkOut"
Cohesion: 0.09
Nodes (7): assign_network(), unassigned_networks(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut, enqueue_sync()

### Community 66 - "Actor"
Cohesion: 0.18
Nodes (5): add_note(), check(), checklist(), delete_note(), edit_note()

### Community 67 - "ItemsOut"
Cohesion: 0.18
Nodes (11): classify(), classify_many(), link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn (+3 more)

### Community 68 - "export.py"
Cohesion: 0.13
Nodes (3): dimension_text(), _csv_cell(), _xlsx_cell()

### Community 69 - "limits.py"
Cohesion: 0.10
Nodes (9): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+1 more)

### Community 70 - "contracts/dto.py"
Cohesion: 0.13
Nodes (7): contract_networks(), _contract_fields(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractSummaryOut, _network_ref()

### Community 71 - "GoalService"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+10 more)

### Community 72 - "google/controller.py"
Cohesion: 0.11
Nodes (7): GoogleFailed, challenge(), _claims(), identity_from_id_token(), new_verifier(), _jwt(), test_id_token_claims()

### Community 74 - "NetworkService"
Cohesion: 0.17
Nodes (5): connect(), options(), NetworkDetailOut, NetworkIn, NetworkService

### Community 77 - "test_account.py"
Cohesion: 0.33
Nodes (7): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 78 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "ClientDocumentService"
Cohesion: 0.09
Nodes (8): approve(), documents(), download(), reject(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 81 - "people/controller.py"
Cohesion: 0.07
Nodes (12): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), PersonOut, PeopleService (+4 more)

### Community 82 - "_month"
Cohesion: 0.25
Nodes (3): _month(), MonthIn, create()

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 85 - "modules/results/controller.py"
Cohesion: 0.09
Nodes (7): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, ResultService

### Community 86 - "limits.py"
Cohesion: 0.08
Nodes (7): BucketResult, BucketRule, MemoryBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.09
Nodes (17): SessionCookies, accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company() (+9 more)

### Community 91 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), delete(), index(), show(), sites_of_member(), unlinked()

### Community 92 - "SiteChecklistService"
Cohesion: 0.13
Nodes (4): months(), summary(), ChecklistMonthOut, SiteChecklistService

### Community 96 - "_staff"
Cohesion: 0.08
Nodes (23): _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal(), _staff() (+15 more)

### Community 97 - "tasks"
Cohesion: 0.22
Nodes (4): change(), comment(), create(), task()

### Community 127 - "events/controller.py"
Cohesion: 0.24
Nodes (3): EventSource, event_service(), EventService

### Community 129 - "test_report_export.py"
Cohesion: 0.22
Nodes (3): _result(), test_csv_header_escapes_formulas(), test_xlsx_with_the_row_limit_is_fast()

### Community 131 - "SiteListOut"
Cohesion: 0.17
Nodes (3): create(), site_options(), SiteListOut

### Community 134 - "test_company_image.py"
Cohesion: 0.24
Nodes (7): _jpeg(), _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), test_phone_photos_pass_and_huge_pngs_are_refused(), test_upload_without_session_is_refused_before_reading_the_body()

### Community 135 - "test_staff_manage_templates_and_clients_see_them_by_role"
Cohesion: 0.24
Nodes (3): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company()

### Community 136 - "ReportService"
Cohesion: 0.06
Nodes (27): Bucket, catalog(), index(), query(), query_batch(), templates(), CustomCatalogMetricOut, DimensionOut (+19 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.20
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+6 more)

### Community 145 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Segurança e limites

### Community 146 - "test_costs_results.py"
Cohesion: 0.08
Nodes (12): _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _marketing_client() (+4 more)

### Community 147 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 148 - "contracts/controller.py"
Cohesion: 0.20
Nodes (5): contract(), contracts(), finish_contract(), new_contract(), remove_contract()

### Community 149 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 152 - "ReportService"
Cohesion: 0.06
Nodes (12): create(), create_from_template(), delete(), duplicate(), pin(), pinned(), run(), show() (+4 more)

### Community 153 - "company/controller.py"
Cohesion: 0.14
Nodes (5): edit_image(), fiscal(), image(), remove_image(), company_service()

### Community 155 - "company/controller.py"
Cohesion: 0.20
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 160 - "ContractService"
Cohesion: 0.19
Nodes (4): edit_contract(), contract_service(), ContractPatchIn, ContractService

### Community 163 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 172 - "dollars"
Cohesion: 0.07
Nodes (4): team(), CommissionMonthOut, dollars(), PersonMonthOut

### Community 174 - "RedisEvents"
Cohesion: 0.47
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 175 - "conftest.py"
Cohesion: 0.06
Nodes (21): client(), engine(), mailer(), _event(), test_events_route(), _membership_ids(), test_groups_lifecycle(), _png() (+13 more)

### Community 176 - "O que já tem"
Cohesion: 0.20
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, metrics()

### Community 184 - "events/controller.py"
Cohesion: 0.16
Nodes (7): channel(), _parse(), sse(), _collect(), ListEvents, test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 189 - "Services"
Cohesion: 0.04
Nodes (21): Services, get_services(), account_service(), alert_service(), api_key_service(), auth_service(), currency_service(), custom_metric_service() (+13 more)

### Community 192 - "SupportTaskService"
Cohesion: 0.15
Nodes (4): tasks(), support_task_service(), TaskOut, SupportTaskService

### Community 193 - "GAM"
Cohesion: 0.40
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1794 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **98 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `roles/controller.py`, `.uow`, `Actor`, `ClientService`, `GamToolService`, `ReportService`, `_month`, `.trusted_uow`, `.uow`, `PageOut`, `api_keys/controller.py`, `InvitationOut`, `PageOut`, `custom_metrics/controller.py`, `SiteService`, `goals/controller.py`, `company/controller.py`, `mfa/controller.py`, `company/controller.py`, `ContractService`, `.__init__`, `invoices/controller.py`, `CommissionService`, `test_account.py`, `company/controller.py`, `documents/controller.py`, `networks/service.py`, `avant_core_shared_clock`, `Services`, `UserOut`, `currencies/controller.py`, `members/controller.py`, `tasks/controller.py`, `.__init__`, `GoogleService`, `clients`, `account/controller.py`, `Services`, `SupportTaskService`, `NetworkOut`, `.__init__`, `ItemsOut`, `.__init__`, `contracts/dto.py`, `GoalService`, `gam_tools/service.py`, `NetworkService`, `image`, `ClientDocumentService`, `people/controller.py`, `modules/results/controller.py`, `auth/controller.py`, `SiteChecklistService`, `networks/service.py`?**
  _High betweenness centrality (0.142) - this node is a cross-community bridge._
- **Are the 118 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 118 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_csrf` be split into smaller, more focused modules?**
  _Cohesion score 0.12944523470839261 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `roles/controller.py`, `.uow`, `Actor`, `ClientService`, `GamToolService`, `ReportService`, `checklists`, `_month`, `.trusted_uow`, `.uow`, `api_keys/controller.py`, `InvitationOut`, `PageOut`, `contracts/controller.py`, `SiteService`, `gam_tools/controller.py`, `ContractOut`, `ContractService`, `invoices/controller.py`, `test_account.py`, `security.py`, `audit/controller.py`, `avant_core_shared_clock`, `Services`, `members/controller.py`, `tasks/controller.py`, `get`, `networks/controller.py`, `.networks`, `SupportTaskService`, `NetworkOut`, `ItemsOut`, `contracts/dto.py`, `GoalService`, `gam_tools/service.py`, `NetworkService`, `Actor`, `image`, `people/controller.py`, `clients`, `modules/results/controller.py`, `Actor`, `SiteChecklistService`, `tasks`, `networks/service.py`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07792207792207792 - nodes in this community are weakly interconnected._