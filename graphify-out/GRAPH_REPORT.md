# Graph Report - avant-api  (2026-11-04)

## Corpus Check
- 290 files · ~90,215 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .rdb 1)

## Summary
- 3952 nodes · 10866 edges · 208 communities (111 shown, 97 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 1825 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0123b1fe`
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
- PageOut
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- errors.py
- goals/controller.py
- verify
- main.py
- clean_code.py
- test_reports.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- reports/controller.py
- test_api.py
- session-start.sh
- avant-api
- NoEvents
- BaseModel
- invoices/controller.py
- commissions/controller.py
- test_account.py
- company/controller.py
- documents/controller.py
- test_networks.py
- checklists/controller.py
- security.py
- test_contracts.py
- networks/service.py
- SupportTaskService
- download
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
- Settings
- health/controller.py
- NetworkOut
- Actor
- ItemsOut
- export.py
- limits.py
- contracts/controller.py
- GoalTemplateOut
- test_account.py
- avant-api
- networks/controller.py
- Actor
- mine
- OwnerInvitationOut
- Arquitetura do MVP do Avant
- image
- client_documents/controller.py
- people/controller.py
- commissions/dto.py
- uuid
- clients
- modules/results/controller.py
- limits.py
- Avant: grupos na Empresa e imagem da Empresa
- auth/controller.py
- SessionCookies
- Actor
- SiteChecklistService
- options
- InvoiceServiceOut
- _csrf
- tasks
- goals/controller.py
- GoalService
- _month
- SiteOut
- CommissionService
- SiteListOut
- Actor
- test_company_image.py
- sites/controller.py
- ReportService
- ad_units
- .of
- .of
- test_mfa.py
- Avant: conexão com o GAM
- test_costs_results.py
- ContractClientRefOut
- contracts
- SiteService
- MemoryCounter
- ReportService
- image
- company/controller.py
- ContractOut
- .of
- conftest.py
- Actor
- Actor
- create_app
- Actor
- document_response
- dollars
- RedisEvents
- _member_client
- O que já tem
- .of
- mine
- .fiscal
- person
- events.py
- clients
- TaskPatchIn
- security.py
- CommissionRuleOut
- delete_template
- index
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

## Communities (208 total, 97 thin omitted)

### Community 0 - "test_gam_tools.py"
Cohesion: 0.11
Nodes (11): RecordingQueue, _network(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads(), _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list() (+3 more)

### Community 1 - "typing"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company()

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.05
Nodes (25): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+17 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

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
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (22): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+14 more)

### Community 11 - "images.py"
Cohesion: 0.13
Nodes (6): _check_jpeg_size(), PillowImageProcessor, _sharpness(), _striped_logo(), test_phone_rotation_from_exif_is_kept(), test_wide_and_palette_logos_stay_sharp()

### Community 12 - ".trusted_uow"
Cohesion: 0.11
Nodes (5): add_item(), create(), update_item(), InvoiceOut, InvoiceService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "PageOut"
Cohesion: 0.12
Nodes (7): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.11
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "PageOut"
Cohesion: 0.07
Nodes (6): UnitOfWorkFactory, index(), audit_service(), AuditService, page_out(), PageOut

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "errors.py"
Cohesion: 0.12
Nodes (11): CompanyChanged, CsrfFailed, error_body(), install(), domain_error(), http_error(), unexpected(), validation_error() (+3 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "main.py"
Cohesion: 0.07
Nodes (6): get_cookies(), GoogleStatusOut, mfa_service(), client_info(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "test_reports.py"
Cohesion: 0.17
Nodes (15): CapturingMailer, _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait(), test_catalog_hides_internal_metrics(), test_display_currency_and_query_in_another_currency() (+7 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.11
Nodes (8): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut, MfaService

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "reports/controller.py"
Cohesion: 0.08
Nodes (15): catalog(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+7 more)

### Community 32 - "test_api.py"
Cohesion: 0.32
Nodes (7): test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session(), test_team_invitation_flow(), test_validation_error_format()

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - "invoices/controller.py"
Cohesion: 0.18
Nodes (10): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn (+2 more)

### Community 39 - "commissions/controller.py"
Cohesion: 0.16
Nodes (6): adjust(), create_rule(), delete_rule(), rules(), update_rule(), CommissionRuleIn

### Community 40 - "test_account.py"
Cohesion: 0.12
Nodes (7): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 41 - "company/controller.py"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 42 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "test_networks.py"
Cohesion: 0.47
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 44 - "checklists/controller.py"
Cohesion: 0.17
Nodes (9): site_checklist_service(), ChecklistDetailOut, ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut (+1 more)

### Community 45 - "security.py"
Cohesion: 0.09
Nodes (15): api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor(), get_auth(), get_session_actor(), get_session_auth() (+7 more)

### Community 46 - "test_contracts.py"
Cohesion: 0.15
Nodes (6): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission()

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "SupportTaskService"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 49 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "UserOut"
Cohesion: 0.08
Nodes (9): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService (+1 more)

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.12
Nodes (9): edit(), set_permissions(), show(), member_service(), DirectPermissionIn, MemberDetailOut, MemberPatchIn, MemberPermissionsIn (+1 more)

### Community 56 - "tasks/controller.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 57 - "clients"
Cohesion: 0.12
Nodes (8): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService

### Community 58 - "GoogleService"
Cohesion: 0.06
Nodes (8): GoogleUnavailable, GoogleAuth, new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), GoogleService

### Community 59 - "uuid"
Cohesion: 0.17
Nodes (26): test_change_password_and_sessions(), _onboard_owner(), _owner_invite(), test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team() (+18 more)

### Community 60 - "account/controller.py"
Cohesion: 0.10
Nodes (12): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn (+4 more)

### Community 61 - "get"
Cohesion: 0.09
Nodes (14): available_months(), delete(), delete_service(), get(), issue(), mine(), pay(), payment_details() (+6 more)

### Community 63 - "Settings"
Cohesion: 0.06
Nodes (7): _google(), _mailer(), Settings, CeleryQueue, GoogleRedirects, test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 64 - "health/controller.py"
Cohesion: 0.16
Nodes (3): ready(), health_service(), HealthService

### Community 65 - "NetworkOut"
Cohesion: 0.11
Nodes (7): assign_network(), unassigned_networks(), mcm_service(), AssignNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 66 - "Actor"
Cohesion: 0.18
Nodes (5): add_note(), check(), checklist(), edit_note(), mark()

### Community 67 - "ItemsOut"
Cohesion: 0.18
Nodes (5): link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteIn

### Community 68 - "export.py"
Cohesion: 0.08
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 69 - "limits.py"
Cohesion: 0.09
Nodes (9): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+1 more)

### Community 70 - "contracts/controller.py"
Cohesion: 0.23
Nodes (6): contract_service(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut

### Community 71 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 72 - "test_account.py"
Cohesion: 0.09
Nodes (14): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _google_round(), _jwt() (+6 more)

### Community 74 - "networks/controller.py"
Cohesion: 0.08
Nodes (14): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+6 more)

### Community 75 - "Actor"
Cohesion: 0.17
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 76 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 77 - "OwnerInvitationOut"
Cohesion: 0.17
Nodes (5): invite_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 78 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "client_documents/controller.py"
Cohesion: 0.14
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 81 - "people/controller.py"
Cohesion: 0.10
Nodes (8): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out()

### Community 82 - "commissions/dto.py"
Cohesion: 0.17
Nodes (5): AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 85 - "modules/results/controller.py"
Cohesion: 0.07
Nodes (6): results(), ClientResultService, show(), ResultsOut, default_period(), ResultService

### Community 86 - "limits.py"
Cohesion: 0.07
Nodes (8): BucketResult, BucketRule, MemoryBucket, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "auth/controller.py"
Cohesion: 0.07
Nodes (16): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+8 more)

### Community 91 - "Actor"
Cohesion: 0.17
Nodes (5): assign_sites(), delete(), index(), show(), unlinked()

### Community 92 - "SiteChecklistService"
Cohesion: 0.15
Nodes (5): checklists(), months(), summary(), ChecklistMonthOut, SiteChecklistService

### Community 94 - "options"
Cohesion: 0.14
Nodes (3): leave(), options(), remove()

### Community 95 - "InvoiceServiceOut"
Cohesion: 0.20
Nodes (5): create_service(), save_payment_details(), update_service(), InvoiceServiceIn, InvoiceServiceOut

### Community 96 - "_csrf"
Cohesion: 0.12
Nodes (27): _csrf(), _admin_role(), NextMonthClock, test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions(), test_groone_role_with_the_whole_catalog() (+19 more)

### Community 97 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 98 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 127 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 128 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 129 - "SiteOut"
Cohesion: 0.21
Nodes (3): sites_of_member(), SiteDetailOut, SiteOut

### Community 130 - "CommissionService"
Cohesion: 0.18
Nodes (3): set_settings(), commission_service(), CommissionService

### Community 131 - "SiteListOut"
Cohesion: 0.18
Nodes (4): create(), site_options(), SiteListOut, ItemsOut

### Community 134 - "test_company_image.py"
Cohesion: 0.14
Nodes (10): _jpeg(), _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), test_phone_photos_pass_and_huge_pngs_are_refused(), test_upload_without_session_is_refused_before_reading_the_body(), _png() (+2 more)

### Community 135 - "sites/controller.py"
Cohesion: 0.26
Nodes (4): classify(), classify_many(), SitePatchIn, SitesPatchIn

### Community 136 - "ReportService"
Cohesion: 0.06
Nodes (21): templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn (+13 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.31
Nodes (11): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+3 more)

### Community 145 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 146 - "test_costs_results.py"
Cohesion: 0.08
Nodes (13): _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _support(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check() (+5 more)

### Community 147 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 148 - "contracts"
Cohesion: 0.18
Nodes (4): contract_networks(), contracts(), edit_contract(), remove_contract()

### Community 149 - "SiteService"
Cohesion: 0.18
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 152 - "ReportService"
Cohesion: 0.06
Nodes (5): create(), pinned(), SavedReportIn, SavedReportOut, ReportService

### Community 155 - "company/controller.py"
Cohesion: 0.16
Nodes (5): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 158 - "ContractOut"
Cohesion: 0.18
Nodes (4): contract(), finish_contract(), ContractOut, ContractService

### Community 163 - "conftest.py"
Cohesion: 0.09
Nodes (19): client(), engine(), mailer(), Sent, _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys() (+11 more)

### Community 166 - "create_app"
Cohesion: 0.09
Nodes (6): configure_logging(), JsonFormatter, observe(), _route_template(), create_app(), health()

### Community 168 - "Actor"
Cohesion: 0.11
Nodes (10): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), edit_client_image() (+2 more)

### Community 175 - "_member_client"
Cohesion: 0.10
Nodes (16): _membership_ids(), test_groups_lifecycle(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client(), _inventory(), test_manual_site(), test_site_category_and_responsible() (+8 more)

### Community 176 - "O que já tem"
Cohesion: 0.22
Nodes (6): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem, metrics()

### Community 184 - "events.py"
Cohesion: 0.09
Nodes (7): channel(), EventSource, _parse(), sse(), StreamLimiter, events(), EventService

### Community 189 - "security.py"
Cohesion: 0.05
Nodes (15): Services, Bucket, get_services(), require_staff(), account_service(), alert_service(), event_service(), google_redirects() (+7 more)

### Community 201 - "TaskQueue"
Cohesion: 0.12
Nodes (3): Estrutura, TaskQueue, enqueue_sync()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 1800 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **97 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `PageOut` to `CommissionService`, `.uow`, `Actor`, `ClientService`, `clients/controller.py`, `.__init__`, `GamToolService`, `ReportService`, `roles/controller.py`, `_month`, `.trusted_uow`, `.uow`, `PageOut`, `api_keys/controller.py`, `InvitationOut`, `custom_metrics/controller.py`, `SiteService`, `goals/controller.py`, `ReportService`, `main.py`, `company/controller.py`, `mfa/controller.py`, `ContractOut`, `company/controller.py`, `.__init__`, `invoices/controller.py`, `test_account.py`, `company/controller.py`, `documents/controller.py`, `checklists/controller.py`, `networks/service.py`, `SupportTaskService`, `Services`, `UserOut`, `currencies/controller.py`, `goals/service.py`, `tasks/controller.py`, `clients`, `GoogleService`, `members/controller.py`, `account/controller.py`, `.__init__`, `NetworkOut`, `.__init__`, `ItemsOut`, `limits.py`, `contracts/controller.py`, `.__init__`, `TaskQueue`, `.__init__`, `.__init__`, `.__init__`, `networks/controller.py`, `image`, `client_documents/controller.py`, `people/controller.py`, `commissions/dto.py`, `modules/results/controller.py`, `auth/controller.py`, `SiteChecklistService`, `GoalService`?**
  _High betweenness centrality (0.141) - this node is a cross-community bridge._
- **Are the 119 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 119 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `test_gam_tools.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11088709677419355 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `roles/controller.py`, `.uow`, `Actor`, `ClientService`, `clients/controller.py`, `GamToolService`, `ReportService`, `_month`, `sites/controller.py`, `.trusted_uow`, `.uow`, `PageOut`, `api_keys/controller.py`, `InvitationOut`, `contracts`, `SiteService`, `ContractOut`, `invoices/controller.py`, `Actor`, `test_account.py`, `checklists/controller.py`, `SupportTaskService`, `Services`, `goals/service.py`, `tasks/controller.py`, `clients`, `members/controller.py`, `get`, `security.py`, `NetworkOut`, `index`, `ItemsOut`, `contracts/controller.py`, `GoalTemplateOut`, `networks/controller.py`, `Actor`, `OwnerInvitationOut`, `image`, `people/controller.py`, `modules/results/controller.py`, `Actor`, `SiteChecklistService`, `tasks`, `goals/controller.py`, `GoalService`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Are the 59 inferred relationships involving `PageOut` (e.g. with `events()` and `AlertPageOut`) actually correct?**
  _`PageOut` has 59 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07231638418079096 - nodes in this community are weakly interconnected._