# Graph Report - avant-api  (2026-11-18)

## Corpus Check
- 400 files · ~130,670 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 5785 nodes · 16262 edges · 261 communities (142 shown, 119 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2544 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bbe2fc0c`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- reward_public/controller.py
- InvoiceOut
- RoleService
- DashboardService
- AlertService
- _member_client
- modules/facebook/controller.py
- sqlalchemy
- steps
- schedules/controller.py
- Avant: conexão com o GAM
- test_mfa.py
- Actor
- GroupService
- PageOut
- FacebookService
- api_keys/controller.py
- InvitationOut
- security.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- test_mail_queue.py
- dashboard_templates/controller.py
- invoice_pdf.py
- clients
- .detail
- AdTagService
- mfa/controller.py
- currencies/controller.py
- ReportService
- test_reward_public.py
- RewardOut
- session-start.sh
- avant-api
- test_price_rules.py
- ad_tag_public/dto.py
- Actor
- mcm/service.py
- mcm/controller.py
- ClientService
- auth/controller.py
- PriceRuleService
- objects
- Services
- test_reports.py
- views/controller.py
- InvoiceService
- .of_view
- client_notes/controller.py
- GamToolService
- modules/rewards/dto.py
- Avant: endpoints da API do MVP
- download
- members/controller.py
- test_api_keys.py
- checklist_items/controller.py
- mcm/dto.py
- modules/rewards/controller.py
- account/controller.py
- router.py
- RedisRewardCache
- checklists/controller.py
- SessionCookies
- contracts
- ClientLoaderService
- UserOut
- export.py
- Limiter
- ClientAdTagService
- FakeFacebook
- avant-api
- tasks.py
- RewardCache
- pool_metrics.py
- test_hardening.py
- ClientPriceRuleService
- costs/controller.py
- install
- CommissionService
- test_events.py
- _month
- GoogleService
- AdUnitOut
- Avant: grupos na Empresa e imagem da Empresa
- RedisCounter
- Groone Avant: contexto do projeto
- documents/controller.py
- SiteChecklistService
- google/controller.py
- tasks/dto.py
- _csrf
- PublicRewardService
- ClientDocumentService
- commissions/dto.py
- profiles
- updates
- download
- Avant: repositório e plano do MVP
- test_networks.py
- client_documents/controller.py
- test_dashboards.py
- watch_pool
- datetime
- conftest.py
- objects
- contracts/controller.py
- CommissionRuleOut
- get
- settings_for_tests
- Arquitetura do MVP do Avant
- company/controller.py
- GoalTemplateOut
- tasks/controller.py
- modules/loaders/dto.py
- LoaderService
- test_invitation_mail.py
- .build
- test_company_image.py
- modules/results/controller.py
- CapturingMailer
- shared/http.py
- ContractService
- sites/controller.py
- RewardStyleIO
- create
- SiteService
- LoaderOptionOut
- reports/service.py
- people/controller.py
- main.py
- image
- person
- dashboards/dto.py
- audit/controller.py
- document_response
- test
- profile/controller.py
- PayeeDetailsOut
- postgres
- ContractClientRefOut
- BaseModel
- checklists
- _record
- client_image
- settings.py
- mine
- TaskQueue
- capped
- ad_tag_public/controller.py
- goals/controller.py
- RedisKeyValueBuffer
- test_metrics.py
- RedisRewardBuffer
- GoalService
- internal/rewards/controller.py
- Settings
- floor_cache.py
- .uow
- health/controller.py
- _BrokenAuthService
- rewards/http.py
- test_database.py
- ItemsOut
- .change
- SiteListOut
- DomainError
- ci.yml
- key_values/controller.py
- SupportTaskService
- .trusted_uow
- test_account.py
- .of_detail
- SiteOut
- Actor
- networks/controller.py
- SiteDetailOut
- delete_template
- GeoLiteCountries
- .of
- commissions/controller.py
- _BrokenReleaseCounter
- _contract_fields

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 239 edges
2. `PageOut` - 211 edges
3. `_csrf()` - 195 edges
4. `get()` - 189 edges
5. `_onboard_owner()` - 189 edges
6. `UnitOfWorkFactory` - 169 edges
7. `Services` - 168 edges
8. `_staff()` - 91 edges
9. `page_out()` - 87 edges
10. `ReportService` - 79 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/modules/company/controller.py
- `Onde está o trabalho` --references--> `PriceRuleSiteOut`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/price_rules/dto.py
- `Como funciona` --references--> `Services`  [INFERRED]
  README.md → src/avant_api/app/container.py
- `Estrutura` --references--> `Services`  [INFERRED]
  README.md → src/avant_api/app/container.py

## Import Cycles
- None detected.

## Communities (261 total, 119 thin omitted)

### Community 0 - "reward_public/controller.py"
Cohesion: 0.19
Nodes (7): client_address(), cors(), events(), icon(), leads(), page(), preflight()

### Community 2 - "RoleService"
Cohesion: 0.07
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.09
Nodes (18): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+10 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "_member_client"
Cohesion: 0.08
Nodes (20): _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture() (+12 more)

### Community 6 - "modules/facebook/controller.py"
Cohesion: 0.09
Nodes (17): FacebookAccountIn, FacebookAccountOut, FacebookAccountRefOut, FacebookAlertOut, FacebookChangeOut, FacebookCountryOut, FacebookDailyOut, FacebookObjectDetailOut (+9 more)

### Community 7 - "sqlalchemy"
Cohesion: 0.12
Nodes (6): ExpectedAsset, load_assets(), SwaggerAsset, SwaggerAssetChanged, test_changed_asset_stops_the_start(), test_page_loads_only_checked_files_from_the_api()

### Community 8 - "steps"
Cohesion: 0.21
Nodes (13): AVANT_CORE_ACCESS, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, steps, env, name, run (+5 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: conexão com o GAM"
Cohesion: 0.05
Nodes (36): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+28 more)

### Community 11 - "test_mfa.py"
Cohesion: 0.31
Nodes (13): run_password_reset_tasks(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice() (+5 more)

### Community 12 - "Actor"
Cohesion: 0.09
Nodes (10): add_item(), available_months(), create(), delete(), delete_service(), issue(), pay(), pdf() (+2 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "PageOut"
Cohesion: 0.04
Nodes (15): UnitOfWorkFactory, networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, unassigned_networks() (+7 more)

### Community 15 - "FacebookService"
Cohesion: 0.08
Nodes (6): accounts(), people(), set_person(), facebook_service(), FacebookPersonOut, FacebookService

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.07
Nodes (12): invite(), StaffInviteIn, StaffService, cancel(), create_invitation(), list_invitations(), resend(), invitation_service() (+4 more)

### Community 18 - "security.py"
Cohesion: 0.06
Nodes (23): CompanyChanged, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company() (+15 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "test_mail_queue.py"
Cohesion: 0.08
Nodes (18): RecordingQueue, _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites() (+10 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.07
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - ".detail"
Cohesion: 0.06
Nodes (3): FacebookTotalsOut, micros(), money()

### Community 27 - "AdTagService"
Cohesion: 0.04
Nodes (28): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+20 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.07
Nodes (10): get_session_auth(), confirm(), disable(), new_recovery_codes(), setup(), verify(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.04
Nodes (22): catalog(), create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index() (+14 more)

### Community 31 - "test_reward_public.py"
Cohesion: 0.12
Nodes (21): _buffer(), _cascade_reward(), test_events_and_leads_go_to_the_buffer(), test_icon_route_has_the_ip_limit(), test_price_rule_settings_forget_reward_page(), test_public_config_is_cached_and_cleared(), test_reward_page_has_cascade_for_rewards_block(), test_reward_page_has_no_cascade_for_other_country() (+13 more)

### Community 32 - "RewardOut"
Cohesion: 0.08
Nodes (3): forget_pages(), RewardIn, RewardOut

### Community 36 - "test_price_rules.py"
Cohesion: 0.12
Nodes (27): FixedCountries, _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _offerwall_unit(), _present() (+19 more)

### Community 37 - "ad_tag_public/dto.py"
Cohesion: 0.13
Nodes (6): PageViewBlockIn, PublicAdTagOut, PublicBlockOut, PublicLoaderOut, PublicMgidOut, PublicTagOut

### Community 38 - "Actor"
Cohesion: 0.09
Nodes (7): alert_settings(), changes(), disconnect(), read_alert(), set_alert_settings(), update_account(), FacebookAlertSettingOut

### Community 40 - "mcm/controller.py"
Cohesion: 0.15
Nodes (5): confirm_network(), register_network(), reject_network(), McmService, NetworkOut

### Community 41 - "ClientService"
Cohesion: 0.07
Nodes (32): audit(), cancel_owner(), change_status(), client(), client_options(), client_teams(), edit_client(), edit_client_image() (+24 more)

### Community 42 - "auth/controller.py"
Cohesion: 0.06
Nodes (17): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+9 more)

### Community 43 - "PriceRuleService"
Cohesion: 0.06
Nodes (14): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+6 more)

### Community 44 - "objects"
Cohesion: 0.09
Nodes (5): accounts(), alerts(), changes(), objects(), show_object()

### Community 45 - "Services"
Cohesion: 0.03
Nodes (20): Services, RedisBucket, get_services(), public_ad_tag_service(), api_key_service(), company_service(), facebook_redirects(), google_redirects() (+12 more)

### Community 46 - "test_reports.py"
Cohesion: 0.08
Nodes (26): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _checked_out(), _checkouts(), PoolWatchingEvents (+18 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "InvoiceService"
Cohesion: 0.10
Nodes (17): create_service(), mine(), service_options(), services(), update_item(), update_service(), invoice_service(), AvailableMonthOut (+9 more)

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "GamToolService"
Cohesion: 0.05
Nodes (20): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+12 more)

### Community 52 - "modules/rewards/dto.py"
Cohesion: 0.08
Nodes (12): metrics(), RewardActiveIn, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO (+4 more)

### Community 53 - "Avant: endpoints da API do MVP"
Cohesion: 0.15
Nodes (12): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+4 more)

### Community 54 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.19
Nodes (13): MemoryBucket, _bearer(), _create(), _exercise(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke() (+5 more)

### Community 57 - "checklist_items/controller.py"
Cohesion: 0.11
Nodes (9): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+1 more)

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.10
Nodes (15): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+7 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 62 - "RedisRewardCache"
Cohesion: 0.14
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "checklists/controller.py"
Cohesion: 0.12
Nodes (12): add_note(), check(), checklist(), edit_note(), mark(), ChecklistDetailOut, ChecklistMarkIn, ChecklistNoteIn (+4 more)

### Community 65 - "contracts"
Cohesion: 0.14
Nodes (6): contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract()

### Community 66 - "ClientLoaderService"
Cohesion: 0.12
Nodes (7): delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService

### Community 67 - "UserOut"
Cohesion: 0.12
Nodes (4): person_out(), edit_image(), remove_image(), UserOut

### Community 68 - "export.py"
Cohesion: 0.05
Nodes (20): check_file(), docstring_problems(), inline_comments(), is_exempt(), main(), single_letter_names(), source_files(), dimension_text() (+12 more)

### Community 69 - "Limiter"
Cohesion: 0.08
Nodes (11): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+3 more)

### Community 71 - "ClientAdTagService"
Cohesion: 0.07
Nodes (14): forget_tag(), create(), delete(), health(), index(), publish(), restore(), set_active() (+6 more)

### Community 74 - "tasks.py"
Cohesion: 0.13
Nodes (5): CeleryQueue, masked_args(), _CapturingCelery, test_password_reset_task_masks_the_email_in_the_message(), test_tasks_with_ids_only_are_not_masked()

### Community 75 - "RewardCache"
Cohesion: 0.03
Nodes (21): ad_tag_cache_key(), CountryLookup, InvitationMailNotSent, RateLimited, Bucket, BucketResult, BucketRule, is_cascade_shape() (+13 more)

### Community 76 - "pool_metrics.py"
Cohesion: 0.18
Nodes (4): count_pool_timeout(), _sample(), test_pool_gauges_follow_checkout_and_close(), test_pool_timeouts_count_only_the_pool_wait()

### Community 77 - "test_hardening.py"
Cohesion: 0.17
Nodes (12): _rendered(), test_api_key_never_reaches_the_log(), test_docs_only_for_the_groone_session_with_2fa(), test_every_response_has_the_content_security_policy(), test_every_response_has_the_security_headers(), test_invalid_bearer_is_limited_per_ip_before_the_database(), counting(), test_old_docs_paths_do_not_exist() (+4 more)

### Community 78 - "ClientPriceRuleService"
Cohesion: 0.05
Nodes (30): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+22 more)

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "install"
Cohesion: 0.21
Nodes (9): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), masked_path() (+1 more)

### Community 82 - "CommissionService"
Cohesion: 0.19
Nodes (5): set_settings(), settings(), commission_service(), CommissionSettingsOut, CommissionService

### Community 83 - "test_events.py"
Cohesion: 0.06
Nodes (20): channel(), _parse(), RedisEvents, sse(), StreamLimiter, events(), EventService, _collect() (+12 more)

### Community 84 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 85 - "GoogleService"
Cohesion: 0.07
Nodes (7): GoogleUnavailable, GoogleAuth, google_callback(), google_start(), google_status(), google_unlink(), GoogleService

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (15): Arquitetura, Como trabalhar nos repositórios, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação (+7 more)

### Community 91 - "documents/controller.py"
Cohesion: 0.15
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 92 - "SiteChecklistService"
Cohesion: 0.14
Nodes (3): delete_note(), site_checklist_service(), SiteChecklistService

### Community 94 - "google/controller.py"
Cohesion: 0.09
Nodes (10): _google(), GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), GoogleStatusOut (+2 more)

### Community 95 - "tasks/dto.py"
Cohesion: 0.21
Nodes (3): TaskDataIn, TaskIn, TaskOut

### Community 96 - "_csrf"
Cohesion: 0.06
Nodes (41): browser(), _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked() (+33 more)

### Community 97 - "PublicRewardService"
Cohesion: 0.09
Nodes (15): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicRewardPriceOut (+7 more)

### Community 102 - "commissions/dto.py"
Cohesion: 0.14
Nodes (4): CommissionMonthOut, CommissionSettingsIn, dollars(), MyCommissionsOut

### Community 127 - "updates"
Cohesion: 0.11
Nodes (17): patterns, patterns, update-types, acoes, dependencias, imagens, dependency-name, patterns (+9 more)

### Community 128 - "download"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.22
Nodes (8): Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11), Resumo, Serviços e ferramentas

### Community 130 - "test_networks.py"
Cohesion: 0.38
Nodes (8): _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission(), test_staff_without_permission_and_other_clients()

### Community 131 - "client_documents/controller.py"
Cohesion: 0.23
Nodes (3): client_document_service(), ClientDocumentsOut, RejectDocumentIn

### Community 132 - "test_dashboards.py"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 133 - "watch_pool"
Cohesion: 0.21
Nodes (5): _checked_in(), _checked_out(), _closed(), _opened(), watch_pool()

### Community 134 - "datetime"
Cohesion: 0.05
Nodes (25): refresh_levels(), _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _manage_inventory(), _send() (+17 more)

### Community 135 - "conftest.py"
Cohesion: 0.05
Nodes (18): client(), engine(), mailer(), memory_services(), MemoryKeyValueBuffer, MemoryRewardBuffer, MemoryRewardCache, NoEvents (+10 more)

### Community 137 - "contracts/controller.py"
Cohesion: 0.18
Nodes (6): ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut, _network_ref()

### Community 138 - "CommissionRuleOut"
Cohesion: 0.15
Nodes (3): update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 139 - "get"
Cohesion: 0.12
Nodes (7): openapi(), swagger(), swagger_asset(), _swagger_page(), alerts(), health(), get()

### Community 142 - "settings_for_tests"
Cohesion: 0.18
Nodes (13): load_settings(), settings_for_tests(), _environment(), _refused_names(), test_api_starts_with_each_transport(), test_each_transport_builds_its_mailer(), test_environment_name_changes_nothing(), test_malformed_smtp_url_never_shows_the_value() (+5 more)

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.14
Nodes (13): Ambientes, deploy e backup, Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões (+5 more)

### Community 144 - "company/controller.py"
Cohesion: 0.07
Nodes (14): Imagem da Empresa, edit(), edit_fiscal(), edit_image(), fiscal(), image(), remove_image(), show() (+6 more)

### Community 145 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 146 - "tasks/controller.py"
Cohesion: 0.25
Nodes (6): change(), comment(), create(), task(), TaskCommentIn, TaskDetailOut

### Community 148 - "LoaderService"
Cohesion: 0.12
Nodes (9): create(), delete(), index(), show(), update(), loader_service(), LoaderIn, LoaderOut (+1 more)

### Community 149 - "test_invitation_mail.py"
Cohesion: 0.24
Nodes (10): _assert_mail_not_sent(), _client_with_owner_invitation(), _invite(), _owner_invitation_emails(), _pending_emails(), test_invite_answers_503_when_the_mail_fails(), test_owner_invitation_answers_503_when_the_mail_fails(), test_owner_invitation_resend_answers_503_when_the_mail_fails() (+2 more)

### Community 150 - ".build"
Cohesion: 0.11
Nodes (3): _facebook(), _mailer(), NoCountries

### Community 152 - "test_company_image.py"
Cohesion: 0.08
Nodes (20): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, _after_first_segment(), _jpeg(), _png(), _put_image() (+12 more)

### Community 155 - "CapturingMailer"
Cohesion: 0.07
Nodes (46): ExportsBusy, CapturingMailer, Sent, _error_code(), _onboard_owner(), _owner_invite(), test_cookies_are_always_secure_with_the_host_prefix(), test_csrf_is_required_for_writes() (+38 more)

### Community 160 - "ContractService"
Cohesion: 0.16
Nodes (4): O que já tem, contract(), ContractOut, ContractService

### Community 161 - "sites/controller.py"
Cohesion: 0.25
Nodes (5): AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 164 - "SiteService"
Cohesion: 0.14
Nodes (4): index(), site_service(), SiteMemberOut, SiteService

### Community 166 - "reports/service.py"
Cohesion: 0.04
Nodes (22): QueryTooHeavy, CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn (+14 more)

### Community 167 - "people/controller.py"
Cohesion: 0.14
Nodes (7): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService

### Community 168 - "main.py"
Cohesion: 0.09
Nodes (6): EventSource, _content_security_policy(), observe(), _route_template(), create_app(), event_service()

### Community 174 - "dashboards/dto.py"
Cohesion: 0.12
Nodes (7): DashboardChoiceIn, DashboardIn, DashboardPageOut, DashboardRunOut, DashboardTemplateOut, HomeDashboardOut, WidgetErrorOut

### Community 175 - "audit/controller.py"
Cohesion: 0.13
Nodes (3): index(), audit_service(), AuditService

### Community 177 - "test"
Cohesion: 0.20
Nodes (10): AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, test, image, ports, redis, env (+2 more)

### Community 178 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 179 - "PayeeDetailsOut"
Cohesion: 0.16
Nodes (3): payment_details(), save_payment_details(), PayeeDetailsOut

### Community 180 - "postgres"
Cohesion: 0.33
Nodes (6): POSTGRES_PASSWORD, env, image, options, ports, postgres

### Community 183 - "ContractClientRefOut"
Cohesion: 0.09
Nodes (5): show(), CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 184 - "BaseModel"
Cohesion: 0.11
Nodes (5): TaskClientOut, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 185 - "checklists"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 188 - "_record"
Cohesion: 0.21
Nodes (5): configure_logging(), JsonFormatter, _record(), test_log_keeps_ordinary_messages(), test_log_masks_database_values_in_message_and_stack()

### Community 190 - "settings.py"
Cohesion: 0.12
Nodes (4): _are_proxy_addresses(), invalid_variable_names(), InvalidVariables, _is_smtp_url()

### Community 191 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 192 - "TaskQueue"
Cohesion: 0.08
Nodes (8): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskMailQueue, TaskQueue, enqueue_sync()

### Community 196 - "ad_tag_public/controller.py"
Cohesion: 0.20
Nodes (4): config(), page_views(), preflight(), read_body()

### Community 197 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 198 - "RedisKeyValueBuffer"
Cohesion: 0.13
Nodes (3): KeyValueBuffer, RedisKeyValueBuffer, test_redis_buffer_follows_the_worker_contract()

### Community 201 - "test_metrics.py"
Cohesion: 0.24
Nodes (3): exposition(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 204 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 210 - "internal/rewards/controller.py"
Cohesion: 0.08
Nodes (13): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), set_active() (+5 more)

### Community 211 - "Settings"
Cohesion: 0.16
Nodes (3): Settings, GoogleRedirects, test_google_flow_cookie_is_always_secure()

### Community 214 - "floor_cache.py"
Cohesion: 0.20
Nodes (4): forget_cascades(), forget_floors(), forget_rule(), forget_site()

### Community 223 - "health/controller.py"
Cohesion: 0.14
Nodes (4): metrics(), ready(), health_service(), HealthService

### Community 225 - "rewards/http.py"
Cohesion: 0.18
Nodes (3): csv_response(), lead_filter(), period()

### Community 226 - "test_database.py"
Cohesion: 0.13
Nodes (8): engine_settings(), restricted_engine(), test_api_does_not_start_with_a_role_that_ignores_rls(), test_database_url_cannot_override_the_timeouts(), test_default_numbers_fit_the_connection_budget(), test_engine_settings_come_from_the_settings(), test_engine_settings_refuse_zero_and_above_the_ceiling(), test_every_connection_has_the_timeouts_and_the_service_name()

### Community 227 - "ItemsOut"
Cohesion: 0.13
Nodes (9): ad_units(), assign_sites(), classify(), classify_many(), delete(), members(), show(), unlinked() (+1 more)

### Community 231 - "SiteListOut"
Cohesion: 0.19
Nodes (3): create(), site_options(), SiteListOut

### Community 233 - "DomainError"
Cohesion: 0.12
Nodes (6): FacebookDenied, FacebookNotConfigured, FacebookStateInvalid, oauth_callback(), oauth_start(), FacebookRedirects

### Community 240 - "ci.yml"
Cohesion: 0.18
Nodes (10): jobs, segredos, name, on, pull_request, push, permissions, contents (+2 more)

### Community 242 - "key_values/controller.py"
Cohesion: 0.27
Nodes (3): cors(), preflight(), receive()

### Community 245 - "test_account.py"
Cohesion: 0.10
Nodes (10): MemoryCounter, FakeGoogle, _google_round(), _login(), _SpyCounter, test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password() (+2 more)

### Community 247 - "SiteOut"
Cohesion: 0.15
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 250 - "networks/controller.py"
Cohesion: 0.12
Nodes (11): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+3 more)

### Community 266 - "commissions/controller.py"
Cohesion: 0.15
Nodes (7): adjust(), create_rule(), delete_rule(), mine(), rules(), AdjustmentIn, MonthIn

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2619 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **119 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `PageOut` to `RoleService`, `DashboardService`, `AlertService`, `client_documents/controller.py`, `modules/facebook/controller.py`, `.__init__`, `contracts/controller.py`, `schedules/controller.py`, `GroupService`, `.__init__`, `FacebookService`, `api_keys/controller.py`, `company/controller.py`, `.__init__`, `custom_metrics/controller.py`, `InvitationOut`, `LoaderService`, `.__init__`, `dashboard_templates/controller.py`, `modules/results/controller.py`, `AdTagService`, `mfa/controller.py`, `currencies/controller.py`, `ReportService`, `ContractService`, `sites/controller.py`, `SiteService`, `reports/service.py`, `mcm/service.py`, `mcm/controller.py`, `ClientService`, `auth/controller.py`, `people/controller.py`, `PriceRuleService`, `dashboards/dto.py`, `audit/controller.py`, `InvoiceService`, `views/controller.py`, `client_notes/controller.py`, `GamToolService`, `profile/controller.py`, `members/controller.py`, `checklist_items/controller.py`, `modules/rewards/controller.py`, `account/controller.py`, `checklists/controller.py`, `TaskQueue`, `ClientLoaderService`, `Limiter`, `ClientAdTagService`, `RewardCache`, `GoalService`, `ClientPriceRuleService`, `costs/controller.py`, `CommissionService`, `internal/rewards/controller.py`, `GoogleService`, `.__init__`, `documents/controller.py`, `.__init__`, `.__init__`, `.uow`, `SiteChecklistService`, `.__init__`, `tasks/dto.py`, `ClientDocumentService`, `PublicRewardService`, `commissions/dto.py`, `SupportTaskService`, `.trusted_uow`, `networks/controller.py`, `goals/service.py`?**
  _High betweenness centrality (0.127) - this node is a cross-community bridge._
- **Are the 188 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 188 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `InvoiceOut` be split into smaller, more focused modules?**
  _Cohesion score 0.12043010752688173 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `InvoiceOut`, `RoleService`, `AlertService`, `modules/facebook/controller.py`, `objects`, `contracts/controller.py`, `schedules/controller.py`, `get`, `Actor`, `GroupService`, `FacebookService`, `api_keys/controller.py`, `GoalTemplateOut`, `InvitationOut`, `tasks/controller.py`, `LoaderService`, `clients`, `AdTagService`, `ContractService`, `RewardOut`, `sites/controller.py`, `SiteService`, `Actor`, `mcm/service.py`, `mcm/controller.py`, `ClientService`, `people/controller.py`, `PriceRuleService`, `objects`, `reports/service.py`, `dashboards/dto.py`, `audit/controller.py`, `InvoiceService`, `Services`, `client_notes/controller.py`, `GamToolService`, `members/controller.py`, `checklists`, `modules/rewards/controller.py`, `router.py`, `checklists/controller.py`, `contracts`, `ClientLoaderService`, `goals/controller.py`, `.of_detail`, `ClientAdTagService`, `GoalService`, `ClientPriceRuleService`, `costs/controller.py`, `internal/rewards/controller.py`, `SiteChecklistService`, `tasks/dto.py`, `ItemsOut`, `SupportTaskService`, `.trusted_uow`, `SiteOut`, `networks/controller.py`, `goals/service.py`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._
- **Are the 87 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 87 INFERRED edges - model-reasoned connections that need verification._
- **Should `RoleService` be split into smaller, more focused modules?**
  _Cohesion score 0.07482993197278912 - nodes in this community are weakly interconnected._