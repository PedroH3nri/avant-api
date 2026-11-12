# Graph Report - avant-api  (2026-11-12)

## Corpus Check
- 385 files · ~125,183 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 5474 nodes · 15486 edges · 250 communities (136 shown, 114 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2477 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9db83bf3`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- reward_public/controller.py
- invoices/dto.py
- roles/controller.py
- DashboardService
- Actor
- conftest.py
- gam_tools/dto.py
- test_account.py
- test
- _month
- Avant: models do MVP
- test_mfa.py
- .trusted_uow
- .uow
- inventory/dto.py
- modules/ad_tags/dto.py
- api_keys/controller.py
- PageOut
- security.py
- CustomMetricService
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- test_mail_queue.py
- goals/controller.py
- verify
- image_response
- clean_code.py
- .of
- mfa/controller.py
- fastapi
- ReportService
- test_reward_public.py
- RewardService
- session-start.sh
- avant-api
- test_price_rules.py
- PublicAdTagService
- PriceRuleSiteOut
- mcm/service.py
- mcm/controller.py
- ClientService
- modules/loaders/controller.py
- PriceRuleService
- AdTagService
- Services
- test_reports.py
- networks/service.py
- io
- clients
- Services
- gam_tools/controller.py
- MemoryCounter
- edit
- download
- MemberService
- test_api_keys.py
- clients
- limits.py
- modules/rewards/controller.py
- google/controller.py
- results/dto.py
- test_cache_down_does_not_break_the_page_or_the_save
- checklists/controller.py
- auth/controller.py
- contracts/controller.py
- _marketing_client
- Actor
- export.py
- Limiter
- SupportTaskService
- AdTagOut
- checklists/controller.py
- avant-api
- CeleryQueue
- UnitOfWorkFactory
- create
- typing
- ClientPriceRuleService
- image
- errors.py
- pydantic
- StreamLimiter
- events.py
- dashboards/dto.py
- sites/service.py
- .approve
- RedisCounter
- Groone Avant: contexto do projeto
- pydantic
- SiteChecklistService
- google/controller.py
- tasks/controller.py
- conftest.py
- reward_public/dto.py
- dollars
- GamToolService
- updates
- _month
- Avant: repositório e plano do MVP
- .uow
- client_documents/controller.py
- test_dashboards.py
- RewardCache
- commissions/controller.py
- RedisKeyValueBuffer
- SiteService
- download
- .save_rule
- openapi
- test_settings.py
- Arquitetura do MVP do Avant
- LoaderOptionOut
- GoalService
- tasks
- _staff
- internal/loaders/controller.py
- CommissionService
- .build
- test_reward_public.py
- test_staff_without_permission_and_other_clients
- CapturingMailer
- .of
- sites/controller.py
- _SpyCounter
- networks/controller.py
- SiteService
- CommissionRuleOut
- reports/service.py
- UserOut
- time
- person
- Avant: conexão com o GAM
- .of
- PageOut
- document_response
- receive
- profile/controller.py
- get
- RedisEvents
- network
- modules/loaders/controller.py
- BaseModel
- .page
- company/controller.py
- mine
- .cascade_hours
- client_image
- TaskQueue
- templates
- ExportsBusy
- package.json
- RateLimited
- test_metrics.py
- RedisRewardBuffer
- modules/loaders/dto.py
- Actor
- PriceRuleDetailsOut
- SiteOut
- _BrokenReleaseCounter
- .start
- Counter
- HealthService
- _BrokenAuthService
- settings_for_tests
- TaskPatchIn
- _contract_fields
- UnitOfWorkFactory
- .to_data
- GamToolNetworkOut
- NetworkService
- invalid_variable_names
- GeoLiteCountries
- mcm/dto.py
- StaffService

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 235 edges
2. `PageOut` - 193 edges
3. `_csrf()` - 192 edges
4. `_onboard_owner()` - 186 edges
5. `get()` - 174 edges
6. `UnitOfWorkFactory` - 163 edges
7. `Services` - 162 edges
8. `_staff()` - 89 edges
9. `ReportService` - 79 edges
10. `page_out()` - 79 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/modules/company/controller.py
- `Imagem da Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/08-grupos-e-imagem-da-empresa.md → src/avant_api/modules/company/controller.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Onde está o trabalho` --references--> `PriceRuleSiteOut`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/price_rules/dto.py

## Import Cycles
- None detected.

## Communities (250 total, 114 thin omitted)

### Community 0 - "reward_public/controller.py"
Cohesion: 0.17
Nodes (6): client_address(), events(), icon(), page(), preflight(), read_body()

### Community 1 - "invoices/dto.py"
Cohesion: 0.09
Nodes (17): create_service(), mine(), save_payment_details(), service_options(), services(), invoice_service(), AvailableMonthOut, InvoiceItemOut (+9 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.06
Nodes (22): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+14 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "conftest.py"
Cohesion: 0.06
Nodes (30): _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _manage_inventory(), _membership_ids(), test_groups_lifecycle() (+22 more)

### Community 6 - "gam_tools/dto.py"
Cohesion: 0.11
Nodes (4): GamStepOut, GamToolPersonOut, GamToolRunNetworkOut, GamToolSiteOut

### Community 7 - "test_account.py"
Cohesion: 0.07
Nodes (18): challenge(), ExpectedAsset, load_assets(), SwaggerAsset, SwaggerAssetChanged, _google_round(), _jwt(), _login() (+10 more)

### Community 8 - "test"
Cohesion: 0.07
Nodes (33): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, jobs (+25 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.08
Nodes (25): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+17 more)

### Community 11 - "test_mfa.py"
Cohesion: 0.19
Nodes (16): run_password_reset_tasks(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable() (+8 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.11
Nodes (8): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, RevenueStatusOut

### Community 15 - "modules/ad_tags/dto.py"
Cohesion: 0.17
Nodes (13): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagHealthDayOut, AdTagHealthOut, AdTagIn, AdTagLiveOut (+5 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.08
Nodes (9): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut (+1 more)

### Community 18 - "security.py"
Cohesion: 0.06
Nodes (22): api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor(), get_auth(), get_session_actor(), get_session_auth() (+14 more)

### Community 19 - "CustomMetricService"
Cohesion: 0.08
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "test_mail_queue.py"
Cohesion: 0.06
Nodes (15): memory_services(), MemoryCounter, RecordingQueue, _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _account(), _NoDatabase (+7 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.16
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - ".of"
Cohesion: 0.13
Nodes (3): forget_tag(), create(), AdTagOut

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "fastapi"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.05
Nodes (21): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+13 more)

### Community 31 - "test_reward_public.py"
Cohesion: 0.07
Nodes (37): reward_cache_key(), browser(), client(), engine(), mailer(), _rendered(), test_api_key_never_reaches_the_log(), test_docs_only_for_the_groone_session_with_2fa() (+29 more)

### Community 32 - "RewardService"
Cohesion: 0.09
Nodes (7): create(), forget_pages(), create(), RewardIn, RewardOut, RewardService, PageOut

### Community 36 - "test_price_rules.py"
Cohesion: 0.12
Nodes (27): FixedCountries, _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _offerwall_unit(), _present() (+19 more)

### Community 37 - "PublicAdTagService"
Cohesion: 0.05
Nodes (14): RewardBuffer, config(), page_views(), preflight(), public_ad_tag_service(), PageViewBlockIn, PageViewIn, PublicAdTagOut (+6 more)

### Community 39 - "mcm/service.py"
Cohesion: 0.13
Nodes (4): NetworkIn, ServiceAccountOut, SyncRunOut, enqueue_sync()

### Community 40 - "mcm/controller.py"
Cohesion: 0.13
Nodes (6): confirm_network(), register_network(), reject_network(), unassigned_networks(), McmService, NetworkOut

### Community 41 - "ClientService"
Cohesion: 0.05
Nodes (29): audit(), cancel_owner(), change_status(), client(), client_options(), client_teams(), edit_client(), edit_client_image() (+21 more)

### Community 42 - "modules/loaders/controller.py"
Cohesion: 0.20
Nodes (4): create(), LoaderIn, LoaderOut, LoaderService

### Community 43 - "PriceRuleService"
Cohesion: 0.11
Nodes (14): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+6 more)

### Community 44 - "AdTagService"
Cohesion: 0.12
Nodes (12): delete(), health(), index(), publish(), restore(), set_active(), show(), units() (+4 more)

### Community 45 - "Services"
Cohesion: 0.04
Nodes (16): Services, EventSource, get_services(), company_service(), document_service(), event_service(), EventService, contract_service() (+8 more)

### Community 46 - "test_reports.py"
Cohesion: 0.08
Nodes (27): refresh_levels(), _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _checked_out(), _checkouts() (+19 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "io"
Cohesion: 0.13
Nodes (13): _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads() (+5 more)

### Community 49 - "clients"
Cohesion: 0.07
Nodes (4): clients(), ClientProfileOut, ClientRefOut, image_url()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "gam_tools/controller.py"
Cohesion: 0.18
Nodes (6): ads_txt(), install(), run(), runs(), AdsTxtOut, GamToolRunOut

### Community 52 - "MemoryCounter"
Cohesion: 0.08
Nodes (11): RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO, RewardLeadOut, RewardMetricsOut (+3 more)

### Community 53 - "edit"
Cohesion: 0.10
Nodes (17): API first e chaves de API, Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa (+9 more)

### Community 54 - "download"
Cohesion: 0.12
Nodes (4): documents(), download(), upload(), DocumentService

### Community 55 - "MemberService"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.10
Nodes (16): Sent, MemoryKeyValueBuffer, _bearer(), _create(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke() (+8 more)

### Community 57 - "clients"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "limits.py"
Cohesion: 0.12
Nodes (6): BucketResult, RedisBucket, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.10
Nodes (13): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+5 more)

### Community 60 - "google/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "results/dto.py"
Cohesion: 0.05
Nodes (9): results(), show(), result_service(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut, default_period() (+1 more)

### Community 62 - "test_cache_down_does_not_break_the_page_or_the_save"
Cohesion: 0.16
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "checklists/controller.py"
Cohesion: 0.14
Nodes (8): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), site_checklist_service(), ChecklistNoteIn

### Community 64 - "auth/controller.py"
Cohesion: 0.04
Nodes (22): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), get_invitation(), login(), me() (+14 more)

### Community 65 - "contracts/controller.py"
Cohesion: 0.07
Nodes (18): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+10 more)

### Community 66 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 67 - "Actor"
Cohesion: 0.09
Nodes (4): ad_units(), show(), ClientRewardService, RewardAdUnitGroupOut

### Community 68 - "export.py"
Cohesion: 0.09
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "Limiter"
Cohesion: 0.14
Nodes (10): TooManyAttempts, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter() (+2 more)

### Community 70 - "SupportTaskService"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 71 - "AdTagOut"
Cohesion: 0.12
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 72 - "checklists/controller.py"
Cohesion: 0.14
Nodes (4): ChecklistMarkIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 74 - "CeleryQueue"
Cohesion: 0.14
Nodes (6): CeleryQueue, masked_args(), _CapturingCelery, test_password_reset_task_masks_the_email_in_the_message(), test_tasks_with_ids_only_are_not_masked(), test_queue_does_not_break_the_request_without_broker()

### Community 75 - "UnitOfWorkFactory"
Cohesion: 0.05
Nodes (5): ad_tag_cache_key(), UnitOfWorkFactory, RewardCache, ClientResultService, forget_tags()

### Community 78 - "ClientPriceRuleService"
Cohesion: 0.11
Nodes (14): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+6 more)

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "errors.py"
Cohesion: 0.05
Nodes (21): CompanyChanged, CsrfFailed, error_body(), GoogleFailed, GoogleUnavailable, install(), domain_error(), http_error() (+13 more)

### Community 81 - "pydantic"
Cohesion: 0.14
Nodes (3): PersonOut, person_out(), UserOut

### Community 82 - "StreamLimiter"
Cohesion: 0.15
Nodes (3): StreamLimiter, events(), test_stream_limiter_caps_each_person_and_the_process()

### Community 83 - "events.py"
Cohesion: 0.15
Nodes (10): channel(), _parse(), sse(), _collect(), _event(), ListEvents, test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports() (+2 more)

### Community 85 - "dashboards/dto.py"
Cohesion: 0.09
Nodes (5): DashboardRunOut, WidgetErrorOut, WidgetRunIn, ReportResultOut, _statement_timeout()

### Community 86 - "sites/service.py"
Cohesion: 0.14
Nodes (4): ad_units(), link(), unlinked(), AdUnitOut

### Community 87 - ".approve"
Cohesion: 0.20
Nodes (9): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Imagem da Empresa, Issues, Modelo de dados, Regras, Resumo (+1 more)

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 91 - "pydantic"
Cohesion: 0.19
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 92 - "SiteChecklistService"
Cohesion: 0.13
Nodes (4): checklists(), ChecklistDetailOut, ChecklistOut, SiteChecklistService

### Community 94 - "google/controller.py"
Cohesion: 0.04
Nodes (15): _google(), GoogleAuth, _are_proxy_addresses(), InvalidVariables, _is_smtp_url(), Settings, google_start(), google_status() (+7 more)

### Community 95 - "tasks/controller.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 96 - "conftest.py"
Cohesion: 0.07
Nodes (4): MemoryRewardBuffer, MemoryRewardCache, NoEvents, test_cookies_are_always_secure_with_the_host_prefix()

### Community 97 - "reward_public/dto.py"
Cohesion: 0.07
Nodes (17): BucketRule, leads(), CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut (+9 more)

### Community 127 - "updates"
Cohesion: 0.11
Nodes (17): patterns, patterns, update-types, acoes, dependencias, imagens, dependency-name, patterns (+9 more)

### Community 128 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 131 - "client_documents/controller.py"
Cohesion: 0.26
Nodes (5): client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 132 - "test_dashboards.py"
Cohesion: 0.15
Nodes (11): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request() (+3 more)

### Community 133 - "RewardCache"
Cohesion: 0.14
Nodes (16): CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn, PriceRuleHistoryOut (+8 more)

### Community 134 - "commissions/controller.py"
Cohesion: 0.31
Nodes (5): AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn

### Community 136 - "SiteService"
Cohesion: 0.19
Nodes (4): show(), site_service(), SiteDetailOut, SiteService

### Community 137 - "download"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 138 - ".save_rule"
Cohesion: 0.14
Nodes (6): adjust(), create_rule(), delete_rule(), settings(), update_rule(), CommissionRuleIn

### Community 139 - "openapi"
Cohesion: 0.15
Nodes (4): openapi(), swagger(), swagger_asset(), _swagger_page()

### Community 142 - "test_settings.py"
Cohesion: 0.27
Nodes (8): load_settings(), _environment(), _refused_names(), test_api_starts_with_each_transport(), test_environment_name_changes_nothing(), test_malformed_smtp_url_never_shows_the_value(), test_missing_or_invalid_configuration_stops_the_api(), test_start_error_shows_names_and_never_values()

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 145 - "GoalService"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+10 more)

### Community 146 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 147 - "_staff"
Cohesion: 0.05
Nodes (53): _csrf(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it() (+45 more)

### Community 148 - "internal/loaders/controller.py"
Cohesion: 0.13
Nodes (6): delete(), index(), options(), show(), update(), ClientLoaderService

### Community 149 - "CommissionService"
Cohesion: 0.20
Nodes (3): set_settings(), commission_service(), CommissionService

### Community 150 - ".build"
Cohesion: 0.12
Nodes (3): _mailer(), NoCountries, test_each_transport_builds_its_mailer()

### Community 152 - "test_reward_public.py"
Cohesion: 0.08
Nodes (20): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, _after_first_segment(), _jpeg(), _png(), _put_image() (+12 more)

### Community 153 - "test_staff_without_permission_and_other_clients"
Cohesion: 0.38
Nodes (8): _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission(), test_staff_without_permission_and_other_clients()

### Community 155 - "CapturingMailer"
Cohesion: 0.10
Nodes (39): CapturingMailer, _onboard_owner(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session(), test_team_invitation_flow() (+31 more)

### Community 161 - "sites/controller.py"
Cohesion: 0.17
Nodes (7): classify(), classify_many(), AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 163 - "networks/controller.py"
Cohesion: 0.12
Nodes (9): connect(), disconnect(), options(), service_account(), show(), sync(), sync_runs(), network_service() (+1 more)

### Community 164 - "SiteService"
Cohesion: 0.22
Nodes (3): delete(), members(), SiteMemberOut

### Community 166 - "reports/service.py"
Cohesion: 0.05
Nodes (16): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+8 more)

### Community 167 - "UserOut"
Cohesion: 0.12
Nodes (7): Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PeopleService

### Community 168 - "time"
Cohesion: 0.26
Nodes (3): _content_security_policy(), observe(), _route_template()

### Community 172 - "Avant: conexão com o GAM"
Cohesion: 0.25
Nodes (7): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação

### Community 175 - "PageOut"
Cohesion: 0.07
Nodes (6): index(), audit_service(), AuditService, AuditOut, page_out(), RoleRefOut

### Community 177 - "receive"
Cohesion: 0.16
Nodes (9): POSTGRES_PASSWORD, env, image, options, ports, postgres, cors(), preflight() (+1 more)

### Community 178 - "profile/controller.py"
Cohesion: 0.14
Nodes (7): edit_appearance(), edit_image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 179 - "get"
Cohesion: 0.08
Nodes (16): health(), add_item(), available_months(), create(), delete(), delete_service(), get(), issue() (+8 more)

### Community 182 - "network"
Cohesion: 0.24
Nodes (3): network(), GamToolClientOut, GamToolNetworkDetailOut

### Community 183 - "modules/loaders/controller.py"
Cohesion: 0.21
Nodes (4): delete(), index(), show(), update()

### Community 184 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 185 - ".page"
Cohesion: 0.21
Nodes (3): months(), summary(), ChecklistMonthOut

### Community 186 - "company/controller.py"
Cohesion: 0.07
Nodes (12): edit(), edit_fiscal(), edit_image(), fiscal(), image(), remove_image(), show(), CompanyDetailOut (+4 more)

### Community 192 - "TaskQueue"
Cohesion: 0.08
Nodes (8): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, QueueUnavailable, TaskMailQueue, TaskQueue

### Community 194 - "templates"
Cohesion: 0.17
Nodes (4): DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 196 - "ExportsBusy"
Cohesion: 0.40
Nodes (3): ExportsBusy, test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 197 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 198 - "RateLimited"
Cohesion: 0.12
Nodes (7): Network, Segurança e limites, RateLimited, KeyValueBuffer, KeyValueIn, network_code(), receive_key_values()

### Community 201 - "test_metrics.py"
Cohesion: 0.15
Nodes (4): metrics(), exposition(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 210 - "Actor"
Cohesion: 0.08
Nodes (12): delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active(), set_icon() (+4 more)

### Community 223 - "HealthService"
Cohesion: 0.10
Nodes (5): check_fetch_site(), create_app(), ready(), health_service(), HealthService

### Community 226 - "settings_for_tests"
Cohesion: 0.13
Nodes (11): engine_settings(), restricted_engine(), settings_for_tests(), test_api_does_not_start_with_a_role_that_ignores_rls(), test_database_url_cannot_override_the_timeouts(), test_default_numbers_fit_the_connection_budget(), test_engine_settings_come_from_the_settings(), test_engine_settings_refuse_zero_and_above_the_ceiling() (+3 more)

### Community 231 - "_contract_fields"
Cohesion: 0.13
Nodes (4): create(), index(), site_options(), SiteListOut

### Community 239 - "UnitOfWorkFactory"
Cohesion: 0.07
Nodes (9): CountryLookup, Bucket, is_cascade_shape(), safe_site_cascades(), site_cascades(), prices(), public_price_floor_service(), PublicPriceFloorsOut (+1 more)

### Community 250 - "NetworkService"
Cohesion: 0.16
Nodes (3): index(), NetworkDetailOut, NetworkService

### Community 265 - "StaffService"
Cohesion: 0.14
Nodes (4): invite(), options(), StaffInviteIn, StaffService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2465 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **114 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `invoices/dto.py`, `.uow`, `DashboardService`, `Actor`, `client_documents/controller.py`, `commissions/controller.py`, `gam_tools/dto.py`, `.__init__`, `.__init__`, `RewardCache`, `StaffService`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `modules/ad_tags/dto.py`, `api_keys/controller.py`, `GoalService`, `PageOut`, `CustomMetricService`, `internal/loaders/controller.py`, `CommissionService`, `goals/controller.py`, `mfa/controller.py`, `fastapi`, `.__init__`, `ReportService`, `RewardService`, `sites/controller.py`, `PublicAdTagService`, `reports/service.py`, `mcm/service.py`, `mcm/controller.py`, `ClientService`, `UserOut`, `modules/loaders/controller.py`, `AdTagService`, `PriceRuleService`, `_month`, `PageOut`, `networks/service.py`, `SiteService`, `Services`, `profile/controller.py`, `download`, `MemberService`, `roles/controller.py`, `clients`, `company/controller.py`, `google/controller.py`, `results/dto.py`, `auth/controller.py`, `TaskQueue`, `contracts/controller.py`, `Actor`, `SupportTaskService`, `AdTagOut`, `ClientPriceRuleService`, `image`, `.__init__`, `dashboards/dto.py`, `.__init__`, `.__init__`, `pydantic`, `SiteChecklistService`, `test_redis_buffer_follows_the_worker_contract`, `google/controller.py`, `.__init__`, `tasks/controller.py`, `reward_public/dto.py`, `UnitOfWorkFactory`, `.__init__`, `.__init__`, `NetworkService`, `GamToolService`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._
- **Are the 185 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 185 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `invoices/dto.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08773784355179703 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `RewardService` to `invoices/dto.py`, `roles/controller.py`, `DashboardService`, `Actor`, `RewardCache`, `gam_tools/dto.py`, `SiteService`, `StaffService`, `_month`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `modules/ad_tags/dto.py`, `api_keys/controller.py`, `GoalService`, `security.py`, `tasks`, `internal/loaders/controller.py`, `PageOut`, `.of`, `ReportService`, `sites/controller.py`, `networks/controller.py`, `PriceRuleSiteOut`, `mcm/service.py`, `mcm/controller.py`, `ClientService`, `UserOut`, `modules/loaders/controller.py`, `AdTagService`, `PriceRuleService`, `reports/service.py`, `PageOut`, `clients`, `Services`, `gam_tools/controller.py`, `get`, `modules/loaders/controller.py`, `MemberService`, `modules/rewards/controller.py`, `results/dto.py`, `Actor`, `checklists/controller.py`, `contracts/controller.py`, `Actor`, `SupportTaskService`, `AdTagOut`, `UnitOfWorkFactory`, `ClientPriceRuleService`, `image`, `Actor`, `PriceRuleDetailsOut`, `dashboards/dto.py`, `sites/service.py`, `SiteChecklistService`, `tasks/controller.py`, `_contract_fields`, `GamToolNetworkOut`, `NetworkService`, `GamToolService`?**
  _High betweenness centrality (0.072) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07644110275689223 - nodes in this community are weakly interconnected._