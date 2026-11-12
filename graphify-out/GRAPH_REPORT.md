# Graph Report - avant-api  (2026-11-12)

## Corpus Check
- 381 files · ~121,612 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .gz 1)

## Summary
- 5350 nodes · 15165 edges · 256 communities (132 shown, 124 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2459 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9f36ad08`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- PublicRewardService
- invoices/controller.py
- roles/controller.py
- DashboardService
- Actor
- conftest.py
- GamToolService
- Actor
- test
- _month
- Avant: models do MVP
- conftest.py
- .trusted_uow
- .uow
- inventory/dto.py
- AdTagService
- api_keys/controller.py
- PageOut
- security.py
- CustomMetricService
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- test_mail_queue.py
- goals/controller.py
- verify
- .of
- clean_code.py
- get
- mfa/controller.py
- fastapi
- ReportService
- _error_code
- RewardService
- session-start.sh
- avant-api
- test_price_rules.py
- router.py
- test_account.py
- mcm/controller.py
- test_gam_tools.py
- datetime
- PriceRuleService
- Services
- test_reports.py
- networks/service.py
- networks/controller.py
- io
- Services
- .run_guarded
- MemoryCounter
- edit
- test_company_image.py
- MemberService
- test_api_keys.py
- clients
- ContractService
- Actor
- account/controller.py
- DocumentService
- test_cache_down_does_not_break_the_page_or_the_save
- SiteChecklistService
- auth/controller.py
- _BrokenAuthService
- SessionCookies
- export.py
- test_account.py
- members/controller.py
- ClientAdTagService
- checklists/controller.py
- avant-api
- test_metrics.py
- clients
- options
- test_reward_public.py
- PriceRuleService
- image
- install
- results/dto.py
- test_events.py
- uuid
- .export_saved
- internal/rewards/controller.py
- sites/service.py
- RedisCounter
- Groone Avant: contexto do projeto
- .assign
- InvoiceService
- google/controller.py
- audit/service.py
- health/controller.py
- reward_public/dto.py
- commissions/dto.py
- ad_tag_public/dto.py
- contracts
- updates
- PublicRewardService
- Avant: repositório e plano do MVP
- documents.py
- MemoryCounter
- contracts/controller.py
- RewardCache
- _month
- CapturingMailer
- AdUnitOut
- .of
- .save_rule
- settings_for_tests
- Arquitetura do MVP do Avant
- commissions/controller.py
- GoalService
- get
- test_who_sees_and_changes_invoices
- QueueUnavailable
- Actor
- test_checklists_need_permission
- custom_metrics/controller.py
- checklists
- client_documents/controller.py
- CompanyService
- SiteService
- modules/loaders/controller.py
- Actor
- custom_metrics/service.py
- .of
- UserOut
- .update_config
- download
- test_networks.py
- rewards/http.py
- .save_payee_details
- test_alerts.py
- avant_core_access_models
- UserOut
- steps
- page_views
- test_key_values.py
- tasks/controller.py
- verify
- document_response
- forget_site
- AdTagHealthOut
- postgres
- TaskQueue
- openapi
- errors.py
- package.json
- ClientLoaderService
- .cascade_hours
- _month
- Actor
- ClientService
- internal/rewards/controller.py
- _out
- SiteListOut
- .icon
- LoaderOut
- LoaderOut
- modules/loaders/dto.py
- LoaderOptionOut
- test_redis_buffer_follows_the_worker_contract
- image_response
- avant-api
- RewardStyleIO
- main.py
- ClientProfileIn
- _contract_fields
- UnitOfWorkFactory
- .uow

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 224 edges
2. `PageOut` - 193 edges
3. `_csrf()` - 184 edges
4. `_onboard_owner()` - 181 edges
5. `get()` - 173 edges
6. `UnitOfWorkFactory` - 163 edges
7. `Services` - 161 edges
8. `_staff()` - 84 edges
9. `ReportService` - 79 edges
10. `page_out()` - 79 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Onde está o trabalho` --references--> `PriceRuleSiteOut`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/price_rules/dto.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (256 total, 124 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.16
Nodes (8): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body()

### Community 1 - "invoices/controller.py"
Cohesion: 0.14
Nodes (10): payment_details(), service_options(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut (+2 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.10
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.07
Nodes (21): choose(), create_from_template(), delete(), duplicate(), home(), index(), run(), run_all() (+13 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "conftest.py"
Cohesion: 0.06
Nodes (15): refresh_levels(), MemoryRewardCache, test_cookies_are_always_secure_with_the_host_prefix(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture() (+7 more)

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (18): ads_txt(), install(), network(), networks(), run(), runs(), start(), AdsTxtOut (+10 more)

### Community 7 - "Actor"
Cohesion: 0.09
Nodes (12): catalog(), create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin() (+4 more)

### Community 8 - "test"
Cohesion: 0.15
Nodes (12): AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, jobs, test, name, on, pull_request (+4 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.05
Nodes (35): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+27 more)

### Community 11 - "conftest.py"
Cohesion: 0.19
Nodes (16): run_password_reset_tasks(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable() (+8 more)

### Community 12 - ".trusted_uow"
Cohesion: 0.09
Nodes (8): add_item(), create(), issue(), pay(), return_to_draft(), update_item(), InvoiceOut, InvoiceService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.06
Nodes (15): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, PersonOut (+7 more)

### Community 15 - "AdTagService"
Cohesion: 0.07
Nodes (23): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+15 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.11
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService, InvitationOut

### Community 18 - "security.py"
Cohesion: 0.05
Nodes (24): CompanyChanged, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company() (+16 more)

### Community 19 - "CustomMetricService"
Cohesion: 0.15
Nodes (4): create(), CustomMetricIn, CustomMetricOut, CustomMetricService

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "test_mail_queue.py"
Cohesion: 0.06
Nodes (15): memory_services(), NoEvents, RecordingQueue, _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _account(), _NoDatabase (+7 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), roles(), set_home(), show(), update(), DashboardTemplateIn (+5 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.16
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "get"
Cohesion: 0.13
Nodes (13): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+5 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.06
Nodes (15): get_cookies(), get_session_auth(), auth_service(), confirm(), disable(), new_recovery_codes(), setup(), mfa_service() (+7 more)

### Community 29 - "fastapi"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.07
Nodes (26): index(), query(), query_batch(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut (+18 more)

### Community 36 - "test_price_rules.py"
Cohesion: 0.10
Nodes (32): _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _cascade_rule(), _cascade_site(), _company_of() (+24 more)

### Community 37 - "router.py"
Cohesion: 0.08
Nodes (8): invite(), options(), staff(), StaffInviteIn, StaffService, MemberOut, page_out(), PageOut

### Community 39 - "test_account.py"
Cohesion: 0.23
Nodes (6): FakeGoogle, _google_round(), _login(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 40 - "mcm/controller.py"
Cohesion: 0.10
Nodes (9): confirm_network(), register_network(), reject_network(), unassigned_networks(), mcm_service(), ClientNetworkIn, McmCandidateOut, McmService (+1 more)

### Community 41 - "test_gam_tools.py"
Cohesion: 0.19
Nodes (10): _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads() (+2 more)

### Community 42 - "datetime"
Cohesion: 0.13
Nodes (11): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query(), _assert_denied(), _queue(), test_cost_writes_need_permission() (+3 more)

### Community 43 - "PriceRuleService"
Cohesion: 0.07
Nodes (12): history(), hours(), index(), set_floor(), set_status(), settings(), sites(), update_blocks() (+4 more)

### Community 45 - "Services"
Cohesion: 0.03
Nodes (27): Como funciona, Services, KeyValueBuffer, RedisKeyValueBuffer, TaskMailQueue, RedisRewardBuffer, get_services(), ad_tag_service() (+19 more)

### Community 46 - "test_reports.py"
Cohesion: 0.07
Nodes (52): test_change_password_and_sessions(), test_change_password_attempts_are_limited(), _csrf(), _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_every_write_route_refuses_another_site(), test_health_and_metrics() (+44 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "networks/controller.py"
Cohesion: 0.11
Nodes (13): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs(), network_service() (+5 more)

### Community 49 - "io"
Cohesion: 0.30
Nodes (5): _result(), test_compare_header_follows_the_mode(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (8): add(), delete(), edit(), notes(), ClientNoteIn, ClientNoteOut, NotePersonOut, ClientNoteService

### Community 52 - "MemoryCounter"
Cohesion: 0.08
Nodes (12): metrics(), RewardActiveIn, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO (+4 more)

### Community 53 - "edit"
Cohesion: 0.08
Nodes (22): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+14 more)

### Community 54 - "test_company_image.py"
Cohesion: 0.08
Nodes (17): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo() (+9 more)

### Community 55 - "MemberService"
Cohesion: 0.11
Nodes (5): edit(), MemberDetailOut, MemberPatchIn, MemberPermissionsIn, MemberService

### Community 56 - "test_api_keys.py"
Cohesion: 0.17
Nodes (13): MemoryBucket, _bearer(), _create(), _exercise(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke() (+5 more)

### Community 57 - "clients"
Cohesion: 0.13
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 58 - "ContractService"
Cohesion: 0.19
Nodes (4): O que já tem, contract(), ContractOut, ContractService

### Community 59 - "Actor"
Cohesion: 0.09
Nodes (15): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+7 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (10): do_change_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut (+2 more)

### Community 61 - "DocumentService"
Cohesion: 0.12
Nodes (4): documents(), download(), upload(), DocumentService

### Community 62 - "test_cache_down_does_not_break_the_page_or_the_save"
Cohesion: 0.12
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "SiteChecklistService"
Cohesion: 0.10
Nodes (7): check(), checklist(), delete_note(), edit_note(), mark(), ChecklistDetailOut, SiteChecklistService

### Community 64 - "auth/controller.py"
Cohesion: 0.08
Nodes (15): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), AcceptInvitationIn (+7 more)

### Community 67 - "SessionCookies"
Cohesion: 0.11
Nodes (3): SessionCookies, delete_session(), do_reset_password()

### Community 68 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "test_account.py"
Cohesion: 0.09
Nodes (10): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+2 more)

### Community 70 - "members/controller.py"
Cohesion: 0.13
Nodes (7): index(), leave(), options(), remove(), set_permissions(), show(), member_service()

### Community 71 - "ClientAdTagService"
Cohesion: 0.07
Nodes (13): forget_tag(), create(), delete(), health(), index(), publish(), restore(), set_active() (+5 more)

### Community 72 - "checklists/controller.py"
Cohesion: 0.18
Nodes (10): add_note(), site_checklist_service(), ChecklistMarkIn, ChecklistMonthOut, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut (+2 more)

### Community 74 - "test_metrics.py"
Cohesion: 0.15
Nodes (4): metrics(), exposition(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 77 - "test_reward_public.py"
Cohesion: 0.06
Nodes (34): FixedCountries, browser(), client(), engine(), mailer(), MemoryRewardBuffer, _rendered(), test_api_key_never_reaches_the_log() (+26 more)

### Community 78 - "PriceRuleService"
Cohesion: 0.08
Nodes (3): show(), PriceRuleDetailsOut, _recommended_models()

### Community 79 - "image"
Cohesion: 0.09
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "install"
Cohesion: 0.21
Nodes (9): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), masked_path() (+1 more)

### Community 81 - "results/dto.py"
Cohesion: 0.07
Nodes (8): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, default_period(), ResultService

### Community 82 - "test_events.py"
Cohesion: 0.06
Nodes (21): channel(), EventSource, _parse(), RedisEvents, sse(), StreamLimiter, events(), EventService (+13 more)

### Community 83 - "uuid"
Cohesion: 0.12
Nodes (12): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company(), _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client() (+4 more)

### Community 86 - "sites/service.py"
Cohesion: 0.18
Nodes (11): classify(), classify_many(), link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn (+3 more)

### Community 88 - "RedisCounter"
Cohesion: 0.17
Nodes (4): RedisCounter, test_redis_decr_without_key_creates_nothing(), test_redis_limiter(), test_redis_down_is_a_503_not_a_500()

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 91 - ".assign"
Cohesion: 0.40
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 92 - "InvoiceService"
Cohesion: 0.22
Nodes (4): create_service(), update_service(), InvoiceServiceIn, InvoiceServiceOut

### Community 94 - "google/controller.py"
Cohesion: 0.04
Nodes (20): GoogleFailed, GoogleUnavailable, challenge(), _claims(), GoogleAuth, GoogleOAuth, identity_from_id_token(), new_verifier() (+12 more)

### Community 95 - "audit/service.py"
Cohesion: 0.12
Nodes (3): index(), AuditService, AuditOut

### Community 96 - "health/controller.py"
Cohesion: 0.07
Nodes (7): _is_docs_page(), observe(), _route_template(), event_service(), ready(), health_service(), HealthService

### Community 97 - "reward_public/dto.py"
Cohesion: 0.22
Nodes (9): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicQuestionOut, PublicRewardOut, PublicStyleOut, RewardEventIn (+1 more)

### Community 102 - "ad_tag_public/dto.py"
Cohesion: 0.12
Nodes (5): PageViewBlockIn, PublicBlockOut, PublicLoaderOut, PublicMgidOut, PublicTagOut

### Community 123 - "contracts"
Cohesion: 0.14
Nodes (6): contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract()

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "PublicRewardService"
Cohesion: 0.17
Nodes (5): PublicPageOut, PublicRewardPriceOut, RewardEventsIn, RewardLeadIn, PublicRewardService

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 130 - "documents.py"
Cohesion: 0.19
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 131 - "MemoryCounter"
Cohesion: 0.12
Nodes (3): MemoryCounter, _BrokenReleaseCounter, _SpyCounter

### Community 132 - "contracts/controller.py"
Cohesion: 0.17
Nodes (7): ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut, _network_ref(), ContractClientRefOut

### Community 133 - "RewardCache"
Cohesion: 0.21
Nodes (12): CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn, PriceRuleHistoryOut, PriceRuleOut (+4 more)

### Community 134 - "_month"
Cohesion: 0.18
Nodes (4): team(), CommissionMonthOut, CommissionSettingsIn, PersonMonthOut

### Community 135 - "CapturingMailer"
Cohesion: 0.12
Nodes (16): CapturingMailer, Sent, test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages(), test_inventory_lists_come_in_pages(), test_member_options_bring_the_whole_team(), test_members_come_in_pages_of_ten() (+8 more)

### Community 137 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 142 - "settings_for_tests"
Cohesion: 0.19
Nodes (8): settings_for_tests(), _settings(), test_every_connection_has_a_statement_and_idle_timeout(), test_pool_is_bounded_and_waits_little(), test_api_does_not_start_without_redis_or_queue_in_any_env(), test_many_processes_need_the_prometheus_directory(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_in_every_env()

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "commissions/controller.py"
Cohesion: 0.12
Nodes (11): adjust(), create_rule(), delete_rule(), person(), rules(), settings(), update_rule(), commission_service() (+3 more)

### Community 145 - "GoalService"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+10 more)

### Community 146 - "get"
Cohesion: 0.12
Nodes (10): health(), available_months(), delete(), delete_service(), get(), mine(), pdf(), remove_item() (+2 more)

### Community 147 - "test_who_sees_and_changes_invoices"
Cohesion: 0.07
Nodes (34): _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it() (+26 more)

### Community 152 - "test_checklists_need_permission"
Cohesion: 0.39
Nodes (4): _checklists(), test_checklists_need_permission(), test_staff_edits_the_item_list(), test_staff_marks_checks_and_writes_notes()

### Community 153 - "custom_metrics/controller.py"
Cohesion: 0.19
Nodes (4): delete(), index(), update(), custom_metric_service()

### Community 155 - "checklists"
Cohesion: 0.14
Nodes (3): checklists(), months(), summary()

### Community 158 - "client_documents/controller.py"
Cohesion: 0.26
Nodes (5): client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 160 - "CompanyService"
Cohesion: 0.08
Nodes (11): edit_fiscal(), edit_image(), fiscal(), image(), remove_image(), show(), CompanyDetailOut, CompanyFiscalOut (+3 more)

### Community 161 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 162 - "modules/loaders/controller.py"
Cohesion: 0.17
Nodes (5): delete(), options(), show(), update(), loader_service()

### Community 165 - "custom_metrics/service.py"
Cohesion: 0.24
Nodes (3): check(), CustomMetricCheckIn, CustomMetricCheckOut

### Community 166 - ".of"
Cohesion: 0.12
Nodes (3): AdTagBlockIO, AdTagDraftIO, AdTagSettingsIO

### Community 167 - "UserOut"
Cohesion: 0.14
Nodes (7): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), PeopleService

### Community 171 - "download"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 172 - "test_networks.py"
Cohesion: 0.38
Nodes (8): _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission(), test_staff_without_permission_and_other_clients()

### Community 174 - "rewards/http.py"
Cohesion: 0.18
Nodes (3): csv_response(), lead_filter(), period()

### Community 176 - "test_alerts.py"
Cohesion: 0.35
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 178 - "UserOut"
Cohesion: 0.08
Nodes (7): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService

### Community 179 - "steps"
Cohesion: 0.22
Nodes (9): AVANT_CORE_ACCESS, PGPASSWORD, env, name, run, uses, with, steps (+1 more)

### Community 180 - "page_views"
Cohesion: 0.28
Nodes (3): config(), page_views(), preflight()

### Community 183 - "test_key_values.py"
Cohesion: 0.17
Nodes (5): MemoryKeyValueBuffer, _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_the_preflight_answers_with_cors()

### Community 184 - "tasks/controller.py"
Cohesion: 0.05
Nodes (17): change(), comment(), create(), task(), tasks(), TaskClientOut, TaskCommentIn, TaskDataIn (+9 more)

### Community 188 - "forget_site"
Cohesion: 0.24
Nodes (4): forget_cascades(), forget_floors(), forget_rule(), forget_site()

### Community 191 - "postgres"
Cohesion: 0.20
Nodes (10): POSTGRES_PASSWORD, env, image, options, ports, image, ports, postgres (+2 more)

### Community 192 - "TaskQueue"
Cohesion: 0.09
Nodes (3): CeleryQueue, TaskQueue, enqueue_sync()

### Community 195 - "errors.py"
Cohesion: 0.05
Nodes (15): RateLimited, Bucket, BucketResult, BucketRule, RedisBucket, RewardBuffer, public_ad_tag_service(), PageViewIn (+7 more)

### Community 196 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 197 - "ClientLoaderService"
Cohesion: 0.12
Nodes (7): delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService

### Community 201 - "_month"
Cohesion: 0.13
Nodes (4): mine(), _month(), MonthIn, MyCommissionsOut

### Community 202 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), delete(), index(), show(), sites_of_member(), unlinked()

### Community 204 - "ClientService"
Cohesion: 0.05
Nodes (29): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), edit_client() (+21 more)

### Community 210 - "internal/rewards/controller.py"
Cohesion: 0.12
Nodes (11): ad_units(), create(), delete(), delete_lead(), export_leads(), leads(), set_active(), set_icon() (+3 more)

### Community 213 - "SiteListOut"
Cohesion: 0.17
Nodes (3): create(), site_options(), SiteListOut

### Community 215 - "LoaderOut"
Cohesion: 0.14
Nodes (6): forget_tags(), create(), index(), LoaderIn, LoaderOut, LoaderService

### Community 223 - "avant-api"
Cohesion: 0.40
Nodes (4): avant-api, Desenvolvimento, Estrutura, Imagem

### Community 226 - "main.py"
Cohesion: 0.05
Nodes (10): engine_options(), _google(), _mailer(), GeoLiteCountries, NoCountries, PillowImageProcessor, configure_logging(), JsonFormatter (+2 more)

### Community 239 - "UnitOfWorkFactory"
Cohesion: 0.04
Nodes (11): ad_tag_cache_key(), CountryLookup, UnitOfWorkFactory, is_cascade_shape(), safe_site_cascades(), site_cascades(), reward_cache_key(), RewardCache (+3 more)

### Community 244 - ".uow"
Cohesion: 0.08
Nodes (6): create(), update(), dashboard_service(), DashboardIn, DashboardOut, DashboardService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2414 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **124 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `PublicRewardService`, `invoices/controller.py`, `documents.py`, `DashboardService`, `Actor`, `contracts/controller.py`, `GamToolService`, `RewardCache`, `roles/controller.py`, `_month`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `commissions/controller.py`, `GoalService`, `CustomMetricService`, `PageOut`, `Actor`, `goals/controller.py`, `get`, `mfa/controller.py`, `fastapi`, `client_documents/controller.py`, `ReportService`, `CompanyService`, `SiteService`, `custom_metrics/service.py`, `avant_core_shared_clock`, `UserOut`, `mcm/controller.py`, `router.py`, `PriceRuleService`, `networks/service.py`, `networks/controller.py`, `Services`, `UserOut`, `MemberService`, `tasks/controller.py`, `clients`, `ContractService`, `Actor`, `account/controller.py`, `DocumentService`, `SiteChecklistService`, `auth/controller.py`, `TaskQueue`, `.__init__`, `errors.py`, `ClientLoaderService`, `ClientAdTagService`, `checklists/controller.py`, `ClientService`, `image`, `results/dto.py`, `internal/rewards/controller.py`, `.__init__`, `sites/service.py`, `LoaderOut`, `google/controller.py`, `audit/service.py`, `.__init__`, `commissions/dto.py`, `.__init__`, `.uow`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `.__init__`?**
  _High betweenness centrality (0.122) - this node is a cross-community bridge._
- **Are the 175 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 175 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `invoices/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1402116402116402 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `router.py` to `invoices/controller.py`, `roles/controller.py`, `DashboardService`, `Actor`, `contracts/controller.py`, `GamToolService`, `RewardCache`, `_month`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `security.py`, `get`, `PageOut`, `Actor`, `checklists`, `get`, `ReportService`, `RewardService`, `SiteService`, `modules/loaders/controller.py`, `.show`, `avant_core_shared_clock`, `UserOut`, `mcm/controller.py`, `PriceRuleService`, `networks/controller.py`, `Services`, `MemberService`, `tasks/controller.py`, `ContractService`, `Actor`, `SiteChecklistService`, `ClientLoaderService`, `members/controller.py`, `ClientAdTagService`, `checklists/controller.py`, `Actor`, `clients`, `ClientService`, `PriceRuleService`, `image`, `results/dto.py`, `internal/rewards/controller.py`, `internal/rewards/controller.py`, `sites/service.py`, `LoaderOut`, `InvoiceService`, `audit/service.py`, `UnitOfWorkFactory`, `contracts`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09663120567375887 - nodes in this community are weakly interconnected._