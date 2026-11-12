# Graph Report - avant-api  (2026-11-11)

## Corpus Check
- 378 files · ~121,038 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .gz 1)

## Summary
- 5335 nodes · 15030 edges · 251 communities (132 shown, 119 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2468 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `28b248dd`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- PublicRewardService
- invoices/controller.py
- roles/controller.py
- DashboardService
- Actor
- _member_client
- GamToolService
- goals/controller.py
- steps
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
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- test_mail_queue.py
- goals/controller.py
- verify
- clients/controller.py
- clean_code.py
- get
- mfa/controller.py
- fastapi
- ReportService
- test_api.py
- RewardService
- session-start.sh
- avant-api
- test_price_rules.py
- router.py
- modules/ad_tags/dto.py
- GoogleFailed
- mcm/controller.py
- test_gam_tools.py
- datetime
- modules/price_rules/controller.py
- Services
- test_reports.py
- networks/service.py
- networks/controller.py
- io
- Services
- ReportQueryIn
- MemoryCounter
- edit
- test_company_image.py
- members/controller.py
- test_api_keys.py
- clients
- middleware.py
- Actor
- account/controller.py
- avant_core_access_models
- test_cache_down_does_not_break_the_page_or_the_save
- SiteChecklistService
- auth/controller.py
- test_hardening.py
- company/controller.py
- Settings
- export.py
- test_account.py
- UUID
- ClientAdTagService
- checklists/controller.py
- avant-api
- test_metrics.py
- .fiscal
- avant_core_access_models
- test_reward_public.py
- PriceRuleService
- image
- install
- results/dto.py
- test_events.py
- uuid
- .of
- sites/service.py
- Avant: grupos na Empresa e imagem da Empresa
- RedisCounter
- Groone Avant: contexto do projeto
- .assign
- InvoiceService
- google/controller.py
- PageOut
- health/controller.py
- reward_public/service.py
- commissions/dto.py
- ad_tag_public/dto.py
- limits.py
- updates
- Avant: repositório e plano do MVP
- tasks/controller.py
- MemoryCounter
- contracts/controller.py
- RewardCache
- _month
- CapturingMailer
- AdUnitOut
- to_csv
- .save_rule
- TaskDetailOut
- tasks/dto.py
- Arquitetura do MVP do Avant
- CommissionService
- GoalTemplateOut
- get
- test_who_sees_and_changes_invoices
- enqueue_sync
- index
- Actor
- test_ad_tags.py
- delete_template
- checklists/controller.py
- mine
- image_url
- SiteService
- modules/loaders/controller.py
- networks/controller.py
- Actor
- .of
- UserOut
- UUID
- avant_core_shared_errors
- image
- GoalService
- PayeeDetailsOut
- fiscal
- commissions/controller.py
- UserOut
- Actor
- RedisEvents
- test_key_values.py
- BaseModel
- RewardAdUnitGroupOut
- .page_saved
- forget_site
- AdTagHealthOut
- receive
- TaskQueue
- AdTagVersionOut
- RateLimited
- package.json
- ClientLoaderService
- .cascade_hours
- mine
- Actor
- ClientService
- internal/rewards/controller.py
- SiteListOut
- templates
- LoaderOut
- LoaderOut
- person
- modules/loaders/dto.py
- .classify
- LoaderOptionOut
- PriceRuleSiteOut
- delete_rule
- RewardStyleIO
- container.py
- MemoryRewardCache
- site_options
- TaskPatchIn
- UnitOfWorkFactory
- company/dto.py
- mcm/dto.py

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 222 edges
2. `PageOut` - 193 edges
3. `_csrf()` - 184 edges
4. `_onboard_owner()` - 179 edges
5. `get()` - 171 edges
6. `Services` - 167 edges
7. `UnitOfWorkFactory` - 163 edges
8. `_staff()` - 81 edges
9. `ReportService` - 79 edges
10. `page_out()` - 79 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/modules/internal/people/controller.py
- `Onde está o trabalho` --references--> `PriceRuleSiteOut`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/price_rules/dto.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (251 total, 119 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.13
Nodes (9): cors(), events(), icon(), leads(), page(), preflight(), read_body(), public_reward_service() (+1 more)

### Community 1 - "invoices/controller.py"
Cohesion: 0.19
Nodes (9): update_item(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, ReturnedOut, ReturnIn (+1 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "_member_client"
Cohesion: 0.09
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (20): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+12 more)

### Community 7 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 8 - "steps"
Cohesion: 0.08
Nodes (25): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, jobs, test, name (+17 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.05
Nodes (36): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+28 more)

### Community 11 - "conftest.py"
Cohesion: 0.12
Nodes (19): client(), engine(), mailer(), run_password_reset_tasks(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable() (+11 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.08
Nodes (9): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService (+1 more)

### Community 15 - "AdTagService"
Cohesion: 0.12
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "security.py"
Cohesion: 0.07
Nodes (23): CompanyChanged, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company() (+15 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "test_mail_queue.py"
Cohesion: 0.08
Nodes (14): RecordingQueue, settings_for_tests(), _account(), _NoDatabase, _NoMail, _services(), test_forgot_password_only_queues_the_normalized_email(), test_forgot_route_never_sends_the_link_itself() (+6 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "clients/controller.py"
Cohesion: 0.06
Nodes (14): edit_client(), register_client(), client_service(), ClientIn, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn (+6 more)

### Community 26 - "clean_code.py"
Cohesion: 0.16
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "get"
Cohesion: 0.13
Nodes (13): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+5 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "fastapi"
Cohesion: 0.15
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.05
Nodes (18): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn (+10 more)

### Community 31 - "test_api.py"
Cohesion: 0.20
Nodes (12): _error_code(), test_csrf_is_required_for_writes(), test_deployed_cookies_use_the_host_prefix(), test_every_write_route_refuses_another_site(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session() (+4 more)

### Community 32 - "RewardService"
Cohesion: 0.09
Nodes (6): forget_pages(), create(), update(), RewardIn, RewardOut, RewardService

### Community 36 - "test_price_rules.py"
Cohesion: 0.14
Nodes (27): _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _offerwall_unit(), _present(), _rule() (+19 more)

### Community 37 - "router.py"
Cohesion: 0.12
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 38 - "modules/ad_tags/dto.py"
Cohesion: 0.12
Nodes (11): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagHealthDayOut, AdTagIn, AdTagLiveOut, AdTagPublishIn (+3 more)

### Community 39 - "GoogleFailed"
Cohesion: 0.09
Nodes (12): GoogleFailed, challenge(), _claims(), identity_from_id_token(), FakeGoogle, _google_round(), _jwt(), _login() (+4 more)

### Community 40 - "mcm/controller.py"
Cohesion: 0.13
Nodes (6): confirm_network(), register_network(), reject_network(), unassigned_networks(), McmService, NetworkOut

### Community 41 - "test_gam_tools.py"
Cohesion: 0.17
Nodes (10): _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads() (+2 more)

### Community 42 - "datetime"
Cohesion: 0.10
Nodes (13): refresh_levels(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query(), _assert_denied(), _queue() (+5 more)

### Community 43 - "modules/price_rules/controller.py"
Cohesion: 0.12
Nodes (14): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+6 more)

### Community 45 - "Services"
Cohesion: 0.03
Nodes (18): Services, get_cookies(), get_services(), Settings, auth_service(), event_service(), google_status(), google_redirects() (+10 more)

### Community 46 - "test_reports.py"
Cohesion: 0.07
Nodes (39): test_change_password_attempts_are_limited(), _onboard_owner(), _checkouts(), test_report_requests_use_few_connections(), query(), test_busy_export_answers_503_with_retry_after(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run() (+31 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "networks/controller.py"
Cohesion: 0.14
Nodes (8): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs(), network_service()

### Community 49 - "io"
Cohesion: 0.31
Nodes (5): _result(), test_compare_header_follows_the_mode(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "ReportQueryIn"
Cohesion: 0.07
Nodes (4): QueryTooHeavy, ReportQueryIn, export_slot(), _statement_timeout()

### Community 52 - "MemoryCounter"
Cohesion: 0.08
Nodes (13): metrics(), metrics(), RewardActiveIn, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut (+5 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "test_company_image.py"
Cohesion: 0.11
Nodes (15): PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client() (+7 more)

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.30
Nodes (9): _bearer(), _create(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit() (+1 more)

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "middleware.py"
Cohesion: 0.23
Nodes (3): _is_docs_page(), observe(), _route_template()

### Community 59 - "Actor"
Cohesion: 0.08
Nodes (12): delete(), delete_lead(), export_leads(), index(), leads(), set_active(), set_icon(), show() (+4 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "avant_core_access_models"
Cohesion: 0.04
Nodes (18): documents(), download(), upload(), document_service(), DocumentService, approve(), documents(), download() (+10 more)

### Community 62 - "test_cache_down_does_not_break_the_page_or_the_save"
Cohesion: 0.16
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 64 - "auth/controller.py"
Cohesion: 0.09
Nodes (16): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), AcceptInvitationIn (+8 more)

### Community 65 - "test_hardening.py"
Cohesion: 0.09
Nodes (17): configure_logging(), JsonFormatter, create_app(), _BrokenAuthService, _rendered(), test_api_key_never_reaches_the_log(), test_docs_are_closed_in_production(), test_every_response_has_the_content_security_policy() (+9 more)

### Community 66 - "company/controller.py"
Cohesion: 0.20
Nodes (3): company_service(), CompanyPatchIn, CompanyService

### Community 68 - "export.py"
Cohesion: 0.12
Nodes (3): dimension_text(), _csv_cell(), _xlsx_cell()

### Community 69 - "test_account.py"
Cohesion: 0.09
Nodes (10): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter() (+2 more)

### Community 70 - "UUID"
Cohesion: 0.13
Nodes (7): add_item(), create(), delete(), delete_service(), issue(), remove_item(), return_to_draft()

### Community 71 - "ClientAdTagService"
Cohesion: 0.09
Nodes (13): AdTagOut, create(), delete(), health(), index(), publish(), restore(), set_active() (+5 more)

### Community 72 - "checklists/controller.py"
Cohesion: 0.17
Nodes (10): site_checklist_service(), ChecklistDetailOut, ChecklistMarkIn, ChecklistMonthOut, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut (+2 more)

### Community 74 - "test_metrics.py"
Cohesion: 0.13
Nodes (4): metrics(), exposition(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 75 - ".fiscal"
Cohesion: 0.18
Nodes (3): edit_fiscal(), CompanyFiscalOut, FiscalDataIn

### Community 76 - "avant_core_access_models"
Cohesion: 0.16
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 77 - "test_reward_public.py"
Cohesion: 0.09
Nodes (19): FixedCountries, reward_cache_key(), _buffer(), _cascade_reward(), test_events_and_leads_go_to_the_buffer(), test_icon_route_has_the_ip_limit(), test_public_config_is_cached_and_cleared(), test_reward_page_has_cascade_for_rewards_block() (+11 more)

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "install"
Cohesion: 0.09
Nodes (10): error_body(), ExportsBusy, install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error() (+2 more)

### Community 81 - "results/dto.py"
Cohesion: 0.05
Nodes (11): results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut (+3 more)

### Community 82 - "test_events.py"
Cohesion: 0.07
Nodes (17): TooManyAttempts, channel(), EventSource, _parse(), sse(), StreamLimiter, events(), EventService (+9 more)

### Community 83 - "uuid"
Cohesion: 0.13
Nodes (14): test_change_password_and_sessions(), _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), _kpi() (+6 more)

### Community 86 - "sites/service.py"
Cohesion: 0.22
Nodes (9): classify_many(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn (+1 more)

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 91 - ".assign"
Cohesion: 0.40
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 92 - "InvoiceService"
Cohesion: 0.24
Nodes (5): create_service(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 94 - "google/controller.py"
Cohesion: 0.06
Nodes (7): GoogleUnavailable, GoogleAuth, new_verifier(), google_callback(), google_start(), google_unlink(), GoogleService

### Community 95 - "PageOut"
Cohesion: 0.07
Nodes (8): index(), audit_service(), AuditService, audit(), AuditOut, page_out(), PageOut, RoleRefOut

### Community 96 - "health/controller.py"
Cohesion: 0.17
Nodes (3): ready(), health_service(), HealthService

### Community 97 - "reward_public/service.py"
Cohesion: 0.09
Nodes (15): BucketRule, CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut (+7 more)

### Community 102 - "ad_tag_public/dto.py"
Cohesion: 0.06
Nodes (14): RewardBuffer, config(), page_views(), preflight(), public_ad_tag_service(), PageViewBlockIn, PageViewIn, PublicAdTagOut (+6 more)

### Community 123 - "limits.py"
Cohesion: 0.20
Nodes (5): BucketResult, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 130 - "tasks/controller.py"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 131 - "MemoryCounter"
Cohesion: 0.12
Nodes (3): MemoryCounter, _BrokenReleaseCounter, _SpyCounter

### Community 132 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 133 - "RewardCache"
Cohesion: 0.25
Nodes (12): CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn, PriceRuleHistoryOut, PriceRuleHourOut (+4 more)

### Community 134 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 135 - "CapturingMailer"
Cohesion: 0.11
Nodes (23): CapturingMailer, Sent, _owner_invite(), test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_events_route_refuses_above_the_cap(), _clients_viewer(), _queue() (+15 more)

### Community 137 - "to_csv"
Cohesion: 0.27
Nodes (5): _header(), _metric_label(), _rows(), to_csv(), to_xlsx()

### Community 138 - ".save_rule"
Cohesion: 0.20
Nodes (4): adjust(), create_rule(), update_rule(), CommissionRuleIn

### Community 139 - "TaskDetailOut"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 142 - "tasks/dto.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "CommissionService"
Cohesion: 0.23
Nodes (3): rules(), CommissionRuleOut, CommissionService

### Community 145 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 146 - "get"
Cohesion: 0.10
Nodes (9): health(), available_months(), get(), mine(), payment_details(), pdf(), service_options(), services() (+1 more)

### Community 147 - "test_who_sees_and_changes_invoices"
Cohesion: 0.07
Nodes (38): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+30 more)

### Community 150 - "Actor"
Cohesion: 0.06
Nodes (17): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned() (+9 more)

### Community 152 - "test_ad_tags.py"
Cohesion: 0.10
Nodes (12): _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status() (+4 more)

### Community 155 - "checklists/controller.py"
Cohesion: 0.11
Nodes (8): add_note(), check(), checklist(), checklists(), delete_note(), edit_note(), months(), summary()

### Community 158 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 161 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 162 - "modules/loaders/controller.py"
Cohesion: 0.21
Nodes (4): delete(), options(), show(), update()

### Community 163 - "networks/controller.py"
Cohesion: 0.16
Nodes (3): options(), NetworkDetailOut, NetworkService

### Community 164 - "Actor"
Cohesion: 0.23
Nodes (3): set_settings(), settings(), CommissionSettingsOut

### Community 167 - "UserOut"
Cohesion: 0.10
Nodes (9): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+1 more)

### Community 171 - "avant_core_shared_errors"
Cohesion: 0.22
Nodes (3): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans()

### Community 174 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 176 - "fiscal"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 177 - "commissions/controller.py"
Cohesion: 0.22
Nodes (4): commission_service(), AdjustmentIn, CommissionSettingsIn, MonthIn

### Community 178 - "UserOut"
Cohesion: 0.07
Nodes (9): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService (+1 more)

### Community 183 - "test_key_values.py"
Cohesion: 0.31
Nodes (4): _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_the_preflight_answers_with_cors()

### Community 184 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 188 - "forget_site"
Cohesion: 0.27
Nodes (3): forget_cascades(), forget_floors(), forget_site()

### Community 191 - "receive"
Cohesion: 0.16
Nodes (9): POSTGRES_PASSWORD, env, image, options, ports, postgres, cors(), preflight() (+1 more)

### Community 192 - "TaskQueue"
Cohesion: 0.09
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskMailQueue, TaskQueue

### Community 195 - "RateLimited"
Cohesion: 0.08
Nodes (7): CountryLookup, RateLimited, Bucket, KeyValueIn, receive_key_values(), prices(), PublicPriceFloorService

### Community 196 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 197 - "ClientLoaderService"
Cohesion: 0.13
Nodes (6): delete(), index(), options(), show(), update(), ClientLoaderService

### Community 202 - "Actor"
Cohesion: 0.15
Nodes (6): ad_units(), assign_sites(), delete(), show(), sites_of_member(), unlinked()

### Community 204 - "ClientService"
Cohesion: 0.05
Nodes (20): cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), clients(), edit_client_image() (+12 more)

### Community 210 - "internal/rewards/controller.py"
Cohesion: 0.11
Nodes (13): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), set_active() (+5 more)

### Community 215 - "LoaderOut"
Cohesion: 0.15
Nodes (4): create(), loader_service(), LoaderIn, LoaderService

### Community 216 - "LoaderOut"
Cohesion: 0.15
Nodes (4): create(), index(), ClientLoaderIn, LoaderOut

### Community 226 - "container.py"
Cohesion: 0.03
Nodes (18): engine_options(), _google(), _mailer(), GeoLiteCountries, NoCountries, NoEvents, GoogleOAuth, KeyValueBuffer (+10 more)

### Community 239 - "UnitOfWorkFactory"
Cohesion: 0.04
Nodes (7): ad_tag_cache_key(), UnitOfWorkFactory, is_cascade_shape(), safe_site_cascades(), site_cascades(), RewardCache, forget_tags()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2407 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **119 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `.__init__`, `invoices/controller.py`, `roles/controller.py`, `DashboardService`, `Actor`, `contracts/controller.py`, `GamToolService`, `RewardCache`, `_month`, `TaskDetailOut`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `CommissionService`, `tasks/dto.py`, `custom_metrics/controller.py`, `PageOut`, `Actor`, `goals/controller.py`, `clients/controller.py`, `get`, `mfa/controller.py`, `fastapi`, `ReportService`, `RewardService`, `SiteService`, `networks/controller.py`, `goals/service.py`, `modules/ad_tags/dto.py`, `UserOut`, `mcm/controller.py`, `router.py`, `modules/price_rules/controller.py`, `GoalService`, `networks/service.py`, `Services`, `UserOut`, `members/controller.py`, `clients`, `account/controller.py`, `avant_core_access_models`, `.__init__`, `SiteChecklistService`, `auth/controller.py`, `TaskQueue`, `company/controller.py`, `RateLimited`, `ClientLoaderService`, `ClientAdTagService`, `checklists/controller.py`, `ClientService`, `avant_core_access_models`, `image`, `results/dto.py`, `internal/rewards/controller.py`, `.__init__`, `sites/service.py`, `LoaderOut`, `InvoiceService`, `.__init__`, `google/controller.py`, `PageOut`, `.__init__`, `commissions/dto.py`, `reward_public/service.py`, `ad_tag_public/dto.py`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `.__init__`?**
  _High betweenness centrality (0.108) - this node is a cross-community bridge._
- **Are the 173 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 173 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PublicRewardService` be split into smaller, more focused modules?**
  _Cohesion score 0.1282051282051282 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `invoices/controller.py`, `tasks/controller.py`, `DashboardService`, `Actor`, `contracts/controller.py`, `GamToolService`, `goals/controller.py`, `RewardCache`, `roles/controller.py`, `_month`, `TaskDetailOut`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `GoalTemplateOut`, `get`, `security.py`, `tasks/dto.py`, `PageOut`, `index`, `clients/controller.py`, `checklists/controller.py`, `get`, `ReportService`, `RewardService`, `SiteService`, `modules/loaders/controller.py`, `networks/controller.py`, `goals/service.py`, `modules/ad_tags/dto.py`, `UserOut`, `mcm/controller.py`, `router.py`, `UUID`, `modules/price_rules/controller.py`, `AdUnitOut`, `GoalService`, `networks/controller.py`, `Services`, `members/controller.py`, `.page_saved`, `Actor`, `SiteChecklistService`, `ClientLoaderService`, `ClientAdTagService`, `checklists/controller.py`, `Actor`, `ClientService`, `avant_core_access_models`, `PriceRuleService`, `image`, `results/dto.py`, `internal/rewards/controller.py`, `.of`, `internal/rewards/controller.py`, `sites/service.py`, `LoaderOut`, `LoaderOut`, `InvoiceService`, `UnitOfWorkFactory`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07422559906487435 - nodes in this community are weakly interconnected._