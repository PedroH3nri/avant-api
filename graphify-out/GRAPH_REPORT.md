# Graph Report - avant-api  (2026-11-05)

## Corpus Check
- 293 files · ~90,927 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 3979 nodes · 10944 edges · 206 communities (109 shown, 97 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1830 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a752ac93`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- test_gam_tools.py
- typing
- roles/controller.py
- DashboardService
- Actor
- profile/controller.py
- test_account.py
- GamToolService
- steps
- _month
- Avant: models do MVP
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
- install
- goals/controller.py
- verify
- http.py
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- ReportService
- Actor
- session-start.sh
- avant-api
- require_staff
- BaseModel
- CommissionService
- .save_rule
- CompanyService
- documents/controller.py
- _onboard_owner
- months
- Services
- reports/service.py
- networks/service.py
- ContractClientRefOut
- UnitOfWorkFactory
- Services
- dollars
- .authenticate
- edit
- currencies/controller.py
- members/controller.py
- ContractOut
- clients
- GoogleService
- uuid
- account/controller.py
- contracts/controller.py
- commissions/controller.py
- main.py
- get
- Actor
- ItemsOut
- export.py
- limits.py
- .of_view
- GoalTemplateOut
- FakeGoogle
- avant-api
- networks/controller.py
- SupportTaskService
- mine
- .square_webp
- image
- client_documents/controller.py
- people/controller.py
- conftest.py
- uuid
- test_sites.py
- fastapi
- limits.py
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- O que já tem
- Actor
- errors.py
- UserOut
- invoices/controller.py
- test_gam_tools.py
- .of
- Actor
- tasks/controller.py
- team
- TaskDetailOut
- .assign
- AdUnitOut
- site_options
- image
- ClientService
- users
- decimal
- .page_saved
- tasks/dto.py
- GAM
- GoalService
- Arquitetura do MVP do Avant
- test_mfa.py
- DashboardTemplateOut
- sqlalchemy
- client_documents/service.py
- UUID
- SiteService
- .run_guarded
- InvoiceService
- image
- UnitOfWorkFactory
- contracts/dto.py
- company/controller.py
- edit_client
- mcm/service.py
- .owner_invitations
- new_owner
- update
- MemoryCounter
- clients/controller.py
- document_response
- .list_all
- _member_client
- .page_saved
- team
- .classify
- edit_image
- goals/service.py
- test_events.py
- _month
- TaskPatchIn
- main.py
- source_files
- Bucket
- metrics
- .export_saved
- update_item
- SessionCookies

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 159 edges
2. `PageOut` - 145 edges
3. `_onboard_owner()` - 142 edges
4. `_csrf()` - 141 edges
5. `UnitOfWorkFactory` - 127 edges
6. `get()` - 125 edges
7. `Services` - 118 edges
8. `ReportService` - 79 edges
9. `_staff()` - 65 edges
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

## Communities (206 total, 97 thin omitted)

### Community 0 - "test_gam_tools.py"
Cohesion: 0.13
Nodes (10): _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list(), test_staff_marks_checks_and_writes_notes() (+2 more)

### Community 1 - "typing"
Cohesion: 0.25
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.06
Nodes (24): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+16 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "profile/controller.py"
Cohesion: 0.20
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 6 - "test_account.py"
Cohesion: 0.31
Nodes (9): _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_id_token_claims() (+1 more)

### Community 7 - "GamToolService"
Cohesion: 0.06
Nodes (18): ads_txt(), install(), network(), networks(), run(), runs(), start(), AdsTxtOut (+10 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.10
Nodes (20): Acesso, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade (+12 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "PageOut"
Cohesion: 0.15
Nodes (7): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.06
Nodes (13): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, cancel(), create_invitation() (+5 more)

### Community 18 - "PageOut"
Cohesion: 0.09
Nodes (4): index(), AuditService, page_out(), PageOut

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.20
Nodes (8): check(), create(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn, CustomMetricOut, CustomMetricService

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
Cohesion: 0.07
Nodes (13): create(), delete(), index(), roles(), set_home(), show(), update(), DashboardTemplateIn (+5 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "http.py"
Cohesion: 0.18
Nodes (3): client_info(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "test_reports.py"
Cohesion: 0.23
Nodes (14): _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency(), test_export_csv_uses_names_and_escapes_formulas() (+6 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (11): get_cookies(), auth_service(), confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn (+3 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "ReportService"
Cohesion: 0.06
Nodes (19): catalog(), create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin() (+11 more)

### Community 32 - "Actor"
Cohesion: 0.12
Nodes (9): cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), edit_client_image(), manager_change() (+1 more)

### Community 36 - "require_staff"
Cohesion: 0.09
Nodes (13): NoActiveCompany, check_tab_company(), get_auth(), get_session_actor(), get_session_auth(), require(), dependency(), require_report() (+5 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 39 - ".save_rule"
Cohesion: 0.12
Nodes (8): adjust(), create_rule(), delete_rule(), person(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 41 - "CompanyService"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 42 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "_onboard_owner"
Cohesion: 0.12
Nodes (16): CapturingMailer, Sent, _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session() (+8 more)

### Community 45 - "Services"
Cohesion: 0.03
Nodes (24): Services, api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_services(), optional_auth(), alert_service() (+16 more)

### Community 46 - "reports/service.py"
Cohesion: 0.05
Nodes (16): CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn, PreviewPointOut (+8 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "ContractClientRefOut"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 49 - "UnitOfWorkFactory"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "dollars"
Cohesion: 0.12
Nodes (3): mine(), dollars(), MyCommissionsOut

### Community 52 - ".authenticate"
Cohesion: 0.09
Nodes (3): accept(), get_invitation(), AuthService

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.15
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+6 more)

### Community 57 - "clients"
Cohesion: 0.12
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 58 - "GoogleService"
Cohesion: 0.04
Nodes (17): GoogleFailed, GoogleUnavailable, challenge(), _claims(), GoogleAuth, GoogleOAuth, identity_from_id_token(), new_verifier() (+9 more)

### Community 59 - "uuid"
Cohesion: 0.19
Nodes (24): _onboard_owner(), test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten(), test_option_lists_keep_the_permissions() (+16 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "contracts/controller.py"
Cohesion: 0.13
Nodes (9): contract(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract(), contract_service(), ContractPatchIn (+1 more)

### Community 63 - "commissions/controller.py"
Cohesion: 0.24
Nodes (8): set_settings(), AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn, PersonMonthOut, WindowMonthOut

### Community 64 - "main.py"
Cohesion: 0.14
Nodes (4): health(), ready(), health_service(), HealthService

### Community 65 - "get"
Cohesion: 0.15
Nodes (7): available_months(), get(), mine(), payment_details(), pdf(), service_options(), services()

### Community 66 - "Actor"
Cohesion: 0.10
Nodes (11): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), summary(), ChecklistDetailOut (+3 more)

### Community 67 - "ItemsOut"
Cohesion: 0.24
Nodes (8): AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn, SitesPatchIn

### Community 68 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "limits.py"
Cohesion: 0.10
Nodes (9): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+1 more)

### Community 74 - "networks/controller.py"
Cohesion: 0.07
Nodes (14): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+6 more)

### Community 75 - "SupportTaskService"
Cohesion: 0.15
Nodes (4): tasks(), support_task_service(), TaskOut, SupportTaskService

### Community 76 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 77 - ".square_webp"
Cohesion: 0.17
Nodes (4): _check_jpeg_size(), _sharpness(), _striped_logo(), test_wide_and_palette_logos_stay_sharp()

### Community 79 - "image"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "client_documents/controller.py"
Cohesion: 0.14
Nodes (6): approve(), documents(), download(), reject(), ClientDocumentOut, ClientDocumentService

### Community 81 - "people/controller.py"
Cohesion: 0.14
Nodes (5): disable(), enable(), reset_mfa(), people_service(), PeopleService

### Community 82 - "conftest.py"
Cohesion: 0.09
Nodes (16): client(), engine(), mailer(), _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit() (+8 more)

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - "test_sites.py"
Cohesion: 0.25
Nodes (5): _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search(), test_site_category_and_responsible(), test_sites_and_assignment()

### Community 85 - "fastapi"
Cohesion: 0.07
Nodes (8): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, default_period(), ResultService

### Community 86 - "limits.py"
Cohesion: 0.07
Nodes (11): BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket() (+3 more)

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.11
Nodes (13): company_image(), do_logout(), login(), me(), set_active_company(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut (+5 more)

### Community 89 - "O que já tem"
Cohesion: 0.33
Nodes (5): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem

### Community 91 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), delete(), index(), show(), sites_of_member(), unlinked()

### Community 92 - "errors.py"
Cohesion: 0.12
Nodes (4): CompanyChanged, CsrfFailed, RateLimited, PillowImageProcessor

### Community 94 - "UserOut"
Cohesion: 0.23
Nodes (5): PersonOut, person_out(), CompanyRefOut, RoleRefOut, UserOut

### Community 95 - "invoices/controller.py"
Cohesion: 0.23
Nodes (11): create_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceServiceOut, InvoiceSummaryOut, PayeeDetailsOut (+3 more)

### Community 96 - "test_gam_tools.py"
Cohesion: 0.08
Nodes (34): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+26 more)

### Community 98 - "Actor"
Cohesion: 0.18
Nodes (5): delete_template(), role_goals(), set_role_goal(), update_template(), RoleGoalIn

### Community 102 - "tasks/controller.py"
Cohesion: 0.22
Nodes (4): change(), comment(), create(), task()

### Community 127 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 129 - ".assign"
Cohesion: 0.14
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 130 - "AdUnitOut"
Cohesion: 0.21
Nodes (3): ad_units(), link(), AdUnitOut

### Community 133 - "ClientService"
Cohesion: 0.13
Nodes (4): audit(), client_service(), ClientService, AuditOut

### Community 135 - "users"
Cohesion: 0.15
Nodes (11): Modelo de dados, Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação (+3 more)

### Community 136 - "decimal"
Cohesion: 0.21
Nodes (4): _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 137 - ".page_saved"
Cohesion: 0.09
Nodes (6): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 139 - "GAM"
Cohesion: 0.33
Nodes (6): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment

### Community 142 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.20
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+6 more)

### Community 145 - "DashboardTemplateOut"
Cohesion: 0.21
Nodes (3): templates(), DashboardTemplateOut, LabelOut

### Community 146 - "sqlalchemy"
Cohesion: 0.08
Nodes (13): refresh_levels(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status() (+5 more)

### Community 148 - "UUID"
Cohesion: 0.13
Nodes (8): add_item(), create(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft()

### Community 149 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 153 - "image"
Cohesion: 0.17
Nodes (3): edit_image(), image(), remove_image()

### Community 155 - "UnitOfWorkFactory"
Cohesion: 0.05
Nodes (3): UnitOfWorkFactory, TaskQueue, enqueue_sync()

### Community 158 - "contracts/dto.py"
Cohesion: 0.11
Nodes (9): contract_networks(), _contract_fields(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractSummaryOut, _network_ref(), ClientRefOut (+1 more)

### Community 160 - "company/controller.py"
Cohesion: 0.19
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 163 - "mcm/service.py"
Cohesion: 0.10
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 164 - ".owner_invitations"
Cohesion: 0.18
Nodes (3): invite_owner(), owner_invitations(), owner_invitation_out()

### Community 165 - "new_owner"
Cohesion: 0.18
Nodes (3): new_owner(), register_client(), resend_owner()

### Community 166 - "update"
Cohesion: 0.22
Nodes (3): delete(), index(), update()

### Community 168 - "clients/controller.py"
Cohesion: 0.19
Nodes (13): ClientDetailOut, ClientIn, ClientMemberOut, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+5 more)

### Community 175 - "_member_client"
Cohesion: 0.10
Nodes (15): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client() (+7 more)

### Community 184 - "test_events.py"
Cohesion: 0.05
Nodes (21): channel(), EventSource, _parse(), RedisEvents, sse(), StreamLimiter, events(), event_service() (+13 more)

### Community 189 - "main.py"
Cohesion: 0.04
Nodes (17): engine_options(), _google(), _mailer(), NoEvents, configure_logging(), JsonFormatter, observe(), _route_template() (+9 more)

### Community 196 - "update_item"
Cohesion: 0.14
Nodes (3): save_payment_details(), update_item(), update_service()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1809 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **97 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `roles/controller.py`, `DashboardService`, `Actor`, `ClientService`, `profile/controller.py`, `GamToolService`, `_month`, `tasks/dto.py`, `.__init__`, `.trusted_uow`, `.uow`, `GoalService`, `PageOut`, `api_keys/controller.py`, `InvitationOut`, `PageOut`, `custom_metrics/controller.py`, `client_documents/service.py`, `SiteService`, `goals/controller.py`, `InvoiceService`, `mfa/controller.py`, `contracts/dto.py`, `company/controller.py`, `company/controller.py`, `ReportService`, `.__init__`, `mcm/service.py`, `CommissionService`, `clients/controller.py`, `CompanyService`, `documents/controller.py`, `reports/service.py`, `networks/service.py`, `.__init__`, `Services`, `.authenticate`, `currencies/controller.py`, `goals/service.py`, `members/controller.py`, `clients`, `GoogleService`, `.of`, `account/controller.py`, `contracts/controller.py`, `commissions/controller.py`, `Bucket`, `Actor`, `ItemsOut`, `.__init__`, `.__init__`, `SupportTaskService`, `networks/controller.py`, `image`, `client_documents/controller.py`, `people/controller.py`, `fastapi`, `auth/controller.py`, `UserOut`, `invoices/controller.py`?**
  _High betweenness centrality (0.117) - this node is a cross-community bridge._
- **Are the 120 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 120 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_gam_tools.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12807881773399016 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `.assign`, `roles/controller.py`, `DashboardService`, `Actor`, `ClientService`, `GamToolService`, `users`, `_month`, `tasks/dto.py`, `.uow`, `GoalService`, `PageOut`, `api_keys/controller.py`, `InvitationOut`, `SiteService`, `InvoiceService`, `contracts/dto.py`, `Actor`, `mcm/service.py`, `.owner_invitations`, `clients/controller.py`, `Actor`, `months`, `reports/service.py`, `.page_saved`, `Services`, `team`, `goals/service.py`, `ContractOut`, `members/controller.py`, `contracts/controller.py`, `get`, `Actor`, `ItemsOut`, `.of_view`, `networks/controller.py`, `SupportTaskService`, `image`, `people/controller.py`, `fastapi`, `Actor`, `UserOut`, `invoices/controller.py`, `Actor`, `tasks/controller.py`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07581453634085213 - nodes in this community are weakly interconnected._