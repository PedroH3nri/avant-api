# Graph Report - avant-api  (2026-11-19)

## Corpus Check
- 415 files · ~140,164 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 6296 nodes · 17614 edges · 293 communities (151 shown, 142 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2781 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a5eda24b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- ClientGoogleAdsService
- .trusted_uow
- roles/controller.py
- DashboardService
- AlertService
- _csrf
- PageOut
- modules/google_ads/controller.py
- steps
- schedules/controller.py
- Avant: models do MVP
- test_mfa.py
- GoogleAdsService
- GroupService
- inventory/controller.py
- FacebookService
- api_keys/controller.py
- InvitationOut
- security.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- test_gam_tools.py
- dashboard_templates/controller.py
- invoice_pdf.py
- clients
- modules/facebook/dto.py
- AdTagService
- MfaService
- currencies/controller.py
- .uow
- browser
- RewardService
- session-start.sh
- avant-api
- test_price_rules.py
- ad_tag_public/service.py
- FacebookRuleOut
- modules/price_rules/dto.py
- mcm/controller.py
- ClientService
- auth/controller.py
- PriceRuleService
- modules/ad_tags/dto.py
- Services
- CapturingMailer
- SavedViewService
- Actor
- modules/facebook/controller.py
- client_notes/controller.py
- modules/rewards/controller.py
- edit
- DocumentService
- members/controller.py
- test_account.py
- checklist_items/controller.py
- Bucket
- Actor
- account/controller.py
- export.py
- RedisRewardCache
- DomainError
- SessionCookies
- Actor
- ClientLoaderService
- UserOut
- clean_code.py
- Limiter
- SupportTaskService
- ClientAdTagService
- avant-api
- CeleryQueue
- RewardCache
- pool_metrics.py
- Actor
- ClientPriceRuleService
- costs/controller.py
- GoogleFailed
- clients/service.py
- .of
- test_events.py
- PriceRuleHourOut
- google/controller.py
- AdUnitOut
- Avant: grupos na Empresa e imagem da Empresa
- RedisCounter
- Groone Avant: contexto do projeto
- documents/controller.py
- checklists/controller.py
- tasks/controller.py
- _staff
- PublicRewardService
- ClientDocumentService
- dollars
- _marketing_client
- updates
- download
- Avant: repositório e plano do MVP
- TaskQueue
- objects
- test_dashboards.py
- .update_fiscal
- conftest.py
- test_mail_queue.py
- company/controller.py
- contracts/controller.py
- commissions/controller.py
- settings_for_tests
- Arquitetura do MVP do Avant
- GamToolService
- tasks
- modules/loaders/dto.py
- LoaderService
- test_invitation_mail.py
- events/controller.py
- test_company_image.py
- results/dto.py
- _onboard_owner
- shared/http.py
- pydantic
- sites/controller.py
- .build
- create
- SiteService
- test_facebook.py
- reports/service.py
- people/controller.py
- main.py
- test_swagger_assets.py
- StreamLimiter
- errors.py
- audit/controller.py
- document_response
- .of_detail
- PriceRuleConfigIn
- test_database.py
- key_values/controller.py
- FacebookAlertSettingOut
- settings.py
- BaseModel
- checklists
- limits.py
- logs.py
- gam_tools/service.py
- ReportResultOut
- mine
- Settings
- FakeGoogleAds
- events.py
- RedisEvents
- AdTagHealthOut
- goals/controller.py
- .options
- client_documents/dto.py
- test_google_ads_panel
- GoalService
- internal/rewards/controller.py
- networks/service.py
- FakeFacebook
- objects
- PriceRuleSiteOut
- image
- rewards/http.py
- .classify
- RedisKeyValueBuffer
- NetworkService
- health/controller.py
- _BrokenAuthService
- UnitOfWorkFactory
- get
- ItemsOut
- TaskPatchIn
- .of
- typing
- edit_image
- test_key_values.py
- checklists/dto.py
- .assign
- networks/controller.py
- LoaderOptionOut
- test_ad_tags_and_loaders_panel
- media.py
- GoalTemplateOut
- client_image
- postgres
- RedisRewardBuffer
- delete_template
- Actor
- invoices/controller.py
- account_service
- GeoLiteCountries
- create
- networks/dependencies.py

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 244 edges
2. `PageOut` - 233 edges
3. `get()` - 214 edges
4. `_csrf()` - 199 edges
5. `_onboard_owner()` - 194 edges
6. `UnitOfWorkFactory` - 175 edges
7. `Services` - 174 edges
8. `page_out()` - 97 edges
9. `_staff()` - 94 edges
10. `FacebookService` - 88 edges

## Surprising Connections (you probably didn't know these)
- `Onde está o trabalho` --references--> `PriceRuleSiteOut`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/price_rules/dto.py
- `Como funciona` --references--> `Services`  [INFERRED]
  README.md → src/avant_api/app/container.py
- `Estrutura` --references--> `Services`  [INFERRED]
  README.md → src/avant_api/app/container.py
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/modules/company/controller.py

## Import Cycles
- None detected.

## Communities (293 total, 142 thin omitted)

### Community 0 - "ClientGoogleAdsService"
Cohesion: 0.06
Nodes (9): keywords(), GoogleAdsKeywordOut, accounts(), alerts(), changes(), keywords(), objects(), show_object() (+1 more)

### Community 1 - ".trusted_uow"
Cohesion: 0.08
Nodes (4): services(), invoice_service(), InvoiceOut, InvoiceService

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (26): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+18 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "_csrf"
Cohesion: 0.06
Nodes (41): _csrf(), test_busy_export_answers_503_with_retry_after(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _result() (+33 more)

### Community 6 - "PageOut"
Cohesion: 0.06
Nodes (15): FacebookAlertOut, FacebookChangeOut, FacebookObjectDetailOut, FacebookObjectOut, FacebookRuleDecisionOut, accounts(), alerts(), changes() (+7 more)

### Community 7 - "modules/google_ads/controller.py"
Cohesion: 0.09
Nodes (16): GoogleAdsAccountIn, GoogleAdsAccountRefOut, GoogleAdsAlertOut, GoogleAdsAlertSettingOut, GoogleAdsChangeOut, GoogleAdsDailyOut, GoogleAdsLoginOut, GoogleAdsObjectDetailOut (+8 more)

### Community 8 - "steps"
Cohesion: 0.07
Nodes (33): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, jobs (+25 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (21): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+13 more)

### Community 11 - "test_mfa.py"
Cohesion: 0.19
Nodes (16): run_password_reset_tasks(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable() (+8 more)

### Community 12 - "GoogleAdsService"
Cohesion: 0.09
Nodes (5): GoogleAdsNotConfigured, accounts(), update_account(), GoogleAdsAccountOut, GoogleAdsService

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/controller.py"
Cohesion: 0.12
Nodes (7): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "FacebookService"
Cohesion: 0.05
Nodes (12): FacebookNotConfigured, alerts(), people(), profiles(), rule_decisions(), set_budget(), set_status(), FacebookBudgetIn (+4 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.11
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.06
Nodes (13): invite(), options(), StaffInviteIn, StaffService, cancel(), create_invitation(), list_invitations(), resend() (+5 more)

### Community 18 - "security.py"
Cohesion: 0.06
Nodes (25): CompanyChanged, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company() (+17 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "test_gam_tools.py"
Cohesion: 0.19
Nodes (10): _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads() (+2 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), roles(), set_home(), show(), update(), DashboardTemplateIn (+5 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "modules/facebook/dto.py"
Cohesion: 0.06
Nodes (12): set_person(), FacebookAccountRefOut, FacebookCountryOut, FacebookDailyOut, FacebookParentOut, FacebookPersonIn, FacebookPersonOut, FacebookProfileOut (+4 more)

### Community 27 - "AdTagService"
Cohesion: 0.09
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 28 - "MfaService"
Cohesion: 0.07
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - ".uow"
Cohesion: 0.05
Nodes (8): create(), duplicate(), pinned(), update(), SavedReportIn, SavedReportOut, export_slot(), ReportService

### Community 31 - "browser"
Cohesion: 0.07
Nodes (34): reward_cache_key(), browser(), _rendered(), test_api_key_never_reaches_the_log(), test_docs_only_for_the_groone_session_with_2fa(), test_every_response_has_the_content_security_policy(), test_every_response_has_the_security_headers(), test_invalid_bearer_is_limited_per_ip_before_the_database() (+26 more)

### Community 32 - "RewardService"
Cohesion: 0.09
Nodes (6): forget_pages(), create(), update(), RewardIn, RewardOut, RewardService

### Community 36 - "test_price_rules.py"
Cohesion: 0.12
Nodes (27): FixedCountries, _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _offerwall_unit(), _present() (+19 more)

### Community 37 - "ad_tag_public/service.py"
Cohesion: 0.06
Nodes (14): RateLimited, RewardBuffer, config(), page_views(), preflight(), public_ad_tag_service(), PageViewBlockIn, PageViewIn (+6 more)

### Community 38 - "FacebookRuleOut"
Cohesion: 0.17
Nodes (4): rule(), set_rule(), FacebookRuleIn, FacebookRuleOut

### Community 39 - "modules/price_rules/dto.py"
Cohesion: 0.13
Nodes (11): CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigOut, PriceRuleDetailsOut, PriceRuleFloorIn, PriceRuleOut (+3 more)

### Community 40 - "mcm/controller.py"
Cohesion: 0.11
Nodes (8): confirm_network(), register_network(), reject_network(), unassigned_networks(), ClientNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 41 - "ClientService"
Cohesion: 0.06
Nodes (22): audit(), cancel_owner(), change_status(), client(), client_options(), client_teams(), edit_client(), edit_client_image() (+14 more)

### Community 42 - "auth/controller.py"
Cohesion: 0.07
Nodes (17): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+9 more)

### Community 43 - "PriceRuleService"
Cohesion: 0.10
Nodes (15): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+7 more)

### Community 44 - "modules/ad_tags/dto.py"
Cohesion: 0.19
Nodes (12): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagHealthDayOut, AdTagIn, AdTagLiveOut, AdTagPublishIn (+4 more)

### Community 45 - "Services"
Cohesion: 0.04
Nodes (14): Services, NoCountries, get_services(), ad_tag_service(), client_document_service(), dashboard_template_service(), mcm_service(), saved_view_service() (+6 more)

### Community 46 - "CapturingMailer"
Cohesion: 0.07
Nodes (30): CapturingMailer, client(), engine(), mailer(), _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client() (+22 more)

### Community 47 - "SavedViewService"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "Actor"
Cohesion: 0.09
Nodes (10): catalog(), create_from_template(), delete(), export(), export_saved(), index(), pin(), run() (+2 more)

### Community 49 - "modules/facebook/controller.py"
Cohesion: 0.04
Nodes (18): FacebookDenied, FacebookStateInvalid, create(), edit(), oauth_callback(), oauth_start(), facebook_redirects(), facebook_service() (+10 more)

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 52 - "modules/rewards/controller.py"
Cohesion: 0.09
Nodes (14): ad_units(), RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut (+6 more)

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "DocumentService"
Cohesion: 0.11
Nodes (5): documents(), download(), upload(), document_service(), DocumentService

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (16): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+8 more)

### Community 56 - "test_account.py"
Cohesion: 0.13
Nodes (17): _BrokenReleaseCounter, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited() (+9 more)

### Community 57 - "checklist_items/controller.py"
Cohesion: 0.11
Nodes (9): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+1 more)

### Community 58 - "Bucket"
Cohesion: 0.09
Nodes (6): CountryLookup, Bucket, prices(), public_price_floor_service(), PublicPriceFloorsOut, PublicPriceFloorService

### Community 59 - "Actor"
Cohesion: 0.11
Nodes (9): delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active(), set_icon() (+1 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (12): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn (+4 more)

### Community 61 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 62 - "RedisRewardCache"
Cohesion: 0.14
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "DomainError"
Cohesion: 0.10
Nodes (7): GoogleAdsDenied, GoogleAdsStateInvalid, oauth_callback(), oauth_start(), google_ads_redirects(), google_ads_service(), GoogleAdsRedirects

### Community 65 - "Actor"
Cohesion: 0.10
Nodes (8): apply_suffix(), changes(), disconnect(), people(), read_alert(), set_alert_settings(), set_person(), GoogleAdsPersonOut

### Community 66 - "ClientLoaderService"
Cohesion: 0.18
Nodes (7): delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService

### Community 67 - "UserOut"
Cohesion: 0.09
Nodes (9): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService (+1 more)

### Community 68 - "clean_code.py"
Cohesion: 0.15
Nodes (7): check_file(), docstring_problems(), inline_comments(), is_exempt(), main(), single_letter_names(), source_files()

### Community 69 - "Limiter"
Cohesion: 0.10
Nodes (10): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter() (+2 more)

### Community 70 - "SupportTaskService"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 71 - "ClientAdTagService"
Cohesion: 0.08
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 74 - "CeleryQueue"
Cohesion: 0.19
Nodes (5): CeleryQueue, masked_args(), _CapturingCelery, test_password_reset_task_masks_the_email_in_the_message(), test_tasks_with_ids_only_are_not_masked()

### Community 75 - "RewardCache"
Cohesion: 0.05
Nodes (8): ad_tag_cache_key(), RewardCache, forget_tag(), forget_tags(), forget_cascades(), forget_floors(), forget_rule(), forget_site()

### Community 76 - "pool_metrics.py"
Cohesion: 0.08
Nodes (11): _checked_in(), _checked_out(), _closed(), _opened(), watch_pool(), exposition(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process() (+3 more)

### Community 77 - "Actor"
Cohesion: 0.07
Nodes (11): accounts(), changes(), disconnect(), duplicate(), job(), read_alert(), set_alert_settings(), update_account() (+3 more)

### Community 78 - "ClientPriceRuleService"
Cohesion: 0.12
Nodes (14): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+6 more)

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "GoogleFailed"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 81 - "clients/service.py"
Cohesion: 0.11
Nodes (13): ClientIn, ClientMemberOut, ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn, ManagerChangeOut (+5 more)

### Community 83 - "test_events.py"
Cohesion: 0.29
Nodes (11): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_events_route_refuses_above_the_cap(), test_facebook_job_updates_reach_who_sees_facebook(), test_gam_tool_runs_reach_who_sees_the_gam_tools() (+3 more)

### Community 85 - "google/controller.py"
Cohesion: 0.08
Nodes (8): GoogleUnavailable, GoogleAuth, new_verifier(), google_callback(), google_start(), google_redirects(), google_service(), GoogleService

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "RedisCounter"
Cohesion: 0.17
Nodes (3): RedisCounter, test_redis_decr_without_key_creates_nothing(), test_redis_down_is_a_503_not_a_500()

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (15): Arquitetura, Como trabalhar nos repositórios, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação (+7 more)

### Community 92 - "checklists/controller.py"
Cohesion: 0.09
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), site_checklist_service(), ChecklistDetailOut (+2 more)

### Community 95 - "tasks/controller.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 96 - "_staff"
Cohesion: 0.06
Nodes (37): _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions() (+29 more)

### Community 97 - "PublicRewardService"
Cohesion: 0.06
Nodes (23): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body() (+15 more)

### Community 123 - "_marketing_client"
Cohesion: 0.11
Nodes (13): _manage_inventory(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query(), _assert_denied(), _queue() (+5 more)

### Community 127 - "updates"
Cohesion: 0.11
Nodes (17): patterns, patterns, update-types, acoes, dependencias, imagens, dependency-name, patterns (+9 more)

### Community 128 - "download"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.22
Nodes (8): Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11), Resumo, Serviços e ferramentas

### Community 130 - "TaskQueue"
Cohesion: 0.09
Nodes (8): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, QueueUnavailable, TaskMailQueue, TaskQueue

### Community 131 - "objects"
Cohesion: 0.11
Nodes (4): objects(), placements(), search_terms(), show_object()

### Community 132 - "test_dashboards.py"
Cohesion: 0.14
Nodes (11): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company(), _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client() (+3 more)

### Community 134 - "conftest.py"
Cohesion: 0.06
Nodes (7): refresh_levels(), MemoryRewardBuffer, MemoryRewardCache, NoEvents, _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 135 - "test_mail_queue.py"
Cohesion: 0.06
Nodes (13): memory_services(), MemoryCounter, RecordingQueue, _SpyCounter, _account(), _NoDatabase, _NoMail, _services() (+5 more)

### Community 136 - "company/controller.py"
Cohesion: 0.21
Nodes (7): show(), company_service(), CompanyDetailOut, CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 137 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 138 - "commissions/controller.py"
Cohesion: 0.06
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 142 - "settings_for_tests"
Cohesion: 0.18
Nodes (13): load_settings(), settings_for_tests(), _environment(), _refused_names(), test_api_starts_with_each_transport(), test_each_transport_builds_its_mailer(), test_environment_name_changes_nothing(), test_malformed_smtp_url_never_shows_the_value() (+5 more)

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.14
Nodes (13): Ambientes, deploy e backup, Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões (+5 more)

### Community 145 - "GamToolService"
Cohesion: 0.12
Nodes (11): ads_txt(), install(), network(), networks(), run(), runs(), gam_tool_service(), AdsTxtOut (+3 more)

### Community 146 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 148 - "LoaderService"
Cohesion: 0.14
Nodes (8): create(), delete(), index(), show(), update(), LoaderIn, LoaderOut, LoaderService

### Community 149 - "test_invitation_mail.py"
Cohesion: 0.24
Nodes (10): _assert_mail_not_sent(), _client_with_owner_invitation(), _invite(), _owner_invitation_emails(), _pending_emails(), test_invite_answers_503_when_the_mail_fails(), test_owner_invitation_answers_503_when_the_mail_fails(), test_owner_invitation_resend_answers_503_when_the_mail_fails() (+2 more)

### Community 150 - "events/controller.py"
Cohesion: 0.13
Nodes (4): EventSource, events(), event_service(), EventService

### Community 152 - "test_company_image.py"
Cohesion: 0.08
Nodes (20): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, _after_first_segment(), _jpeg(), _png(), _put_image() (+12 more)

### Community 153 - "results/dto.py"
Cohesion: 0.05
Nodes (11): results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut (+3 more)

### Community 155 - "_onboard_owner"
Cohesion: 0.12
Nodes (29): Sent, _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session() (+21 more)

### Community 160 - "pydantic"
Cohesion: 0.11
Nodes (3): google_status(), google_unlink(), GoogleStatusOut

### Community 161 - "sites/controller.py"
Cohesion: 0.20
Nodes (9): create(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn (+1 more)

### Community 162 - ".build"
Cohesion: 0.10
Nodes (4): _facebook(), _google(), _google_ads(), _mailer()

### Community 164 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 165 - "test_facebook.py"
Cohesion: 0.25
Nodes (9): _configure(), _connect(), _draft(), _services(), _sync(), test_facebook_control_and_rules(), test_facebook_create_edit_duplicate_lists_and_media(), test_facebook_panel() (+1 more)

### Community 166 - "reports/service.py"
Cohesion: 0.06
Nodes (24): QueryTooHeavy, query_batch(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut (+16 more)

### Community 167 - "people/controller.py"
Cohesion: 0.12
Nodes (7): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService

### Community 168 - "main.py"
Cohesion: 0.08
Nodes (9): configure_logging(), _content_security_policy(), observe(), _route_template(), create_app(), openapi(), swagger(), swagger_asset() (+1 more)

### Community 171 - "test_swagger_assets.py"
Cohesion: 0.10
Nodes (8): ExpectedAsset, load_assets(), SwaggerAsset, SwaggerAssetChanged, _error_code(), test_every_write_route_refuses_another_site(), test_changed_asset_stops_the_start(), test_page_loads_only_checked_files_from_the_api()

### Community 172 - "StreamLimiter"
Cohesion: 0.25
Nodes (3): TooManyAttempts, StreamLimiter, test_stream_limiter_caps_each_person_and_the_process()

### Community 174 - "errors.py"
Cohesion: 0.07
Nodes (15): error_body(), ExportsBusy, install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error() (+7 more)

### Community 175 - "audit/controller.py"
Cohesion: 0.15
Nodes (3): index(), audit_service(), AuditService

### Community 179 - "test_database.py"
Cohesion: 0.13
Nodes (8): engine_settings(), restricted_engine(), test_api_does_not_start_with_a_role_that_ignores_rls(), test_database_url_cannot_override_the_timeouts(), test_default_numbers_fit_the_connection_budget(), test_engine_settings_come_from_the_settings(), test_engine_settings_refuse_zero_and_above_the_ceiling(), test_every_connection_has_the_timeouts_and_the_service_name()

### Community 180 - "key_values/controller.py"
Cohesion: 0.27
Nodes (3): cors(), preflight(), receive()

### Community 183 - "settings.py"
Cohesion: 0.12
Nodes (4): _are_proxy_addresses(), invalid_variable_names(), InvalidVariables, _is_smtp_url()

### Community 184 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 185 - "checklists"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 186 - "limits.py"
Cohesion: 0.14
Nodes (7): BucketResult, BucketRule, RedisBucket, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 188 - "logs.py"
Cohesion: 0.19
Nodes (4): JsonFormatter, _record(), test_log_keeps_ordinary_messages(), test_log_masks_database_values_in_message_and_stack()

### Community 189 - "gam_tools/service.py"
Cohesion: 0.11
Nodes (6): start(), GamStepOut, GamToolPersonOut, GamToolRunIn, GamToolRunNetworkOut, GamToolRunOut

### Community 191 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 192 - "Settings"
Cohesion: 0.15
Nodes (3): Settings, GoogleRedirects, test_google_flow_cookie_is_always_secure()

### Community 194 - "events.py"
Cohesion: 0.22
Nodes (3): channel(), _parse(), sse()

### Community 195 - "RedisEvents"
Cohesion: 0.27
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 197 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 198 - ".options"
Cohesion: 0.10
Nodes (3): options(), FacebookOptionOut, _CachedOptions

### Community 201 - "client_documents/dto.py"
Cohesion: 0.18
Nodes (4): ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, DocumentOut

### Community 202 - "test_google_ads_panel"
Cohesion: 0.24
Nodes (6): _configure(), _connect(), _services(), _sync(), test_google_ads_panel(), test_without_the_google_client_the_login_is_unavailable()

### Community 204 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 210 - "internal/rewards/controller.py"
Cohesion: 0.10
Nodes (14): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+6 more)

### Community 211 - "networks/service.py"
Cohesion: 0.14
Nodes (4): NetworkIn, ServiceAccountOut, SyncRunOut, enqueue_sync()

### Community 218 - "rewards/http.py"
Cohesion: 0.18
Nodes (3): csv_response(), lead_filter(), period()

### Community 223 - "health/controller.py"
Cohesion: 0.14
Nodes (4): metrics(), ready(), health_service(), HealthService

### Community 225 - "UnitOfWorkFactory"
Cohesion: 0.07
Nodes (5): UnitOfWorkFactory, is_cascade_shape(), safe_site_cascades(), site_cascades(), page_out()

### Community 226 - "get"
Cohesion: 0.20
Nodes (5): alert_settings(), alerts(), logins(), health(), get()

### Community 227 - "ItemsOut"
Cohesion: 0.12
Nodes (9): ad_units(), assign_sites(), delete(), index(), show(), site_options(), sites_of_member(), unlinked() (+1 more)

### Community 242 - "typing"
Cohesion: 0.07
Nodes (14): Network, Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação (+6 more)

### Community 244 - "edit_image"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 245 - "test_key_values.py"
Cohesion: 0.19
Nodes (5): MemoryKeyValueBuffer, _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_the_preflight_answers_with_cors()

### Community 246 - "checklists/dto.py"
Cohesion: 0.10
Nodes (6): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 247 - ".assign"
Cohesion: 0.10
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 250 - "networks/controller.py"
Cohesion: 0.12
Nodes (9): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+1 more)

### Community 253 - "test_ad_tags_and_loaders_panel"
Cohesion: 0.33
Nodes (5): _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back()

### Community 256 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 258 - "postgres"
Cohesion: 0.33
Nodes (6): POSTGRES_PASSWORD, env, image, options, ports, postgres

### Community 266 - "invoices/controller.py"
Cohesion: 0.08
Nodes (27): add_item(), available_months(), create_service(), delete(), delete_service(), issue(), mine(), pay() (+19 more)

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2878 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **142 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `ClientGoogleAdsService`, `.trusted_uow`, `TaskQueue`, `DashboardService`, `AlertService`, `roles/controller.py`, `PageOut`, `modules/google_ads/controller.py`, `company/controller.py`, `contracts/controller.py`, `commissions/controller.py`, `invoices/controller.py`, `GoogleAdsService`, `GroupService`, `inventory/controller.py`, `FacebookService`, `.__init__`, `api_keys/controller.py`, `.__init__`, `custom_metrics/controller.py`, `GamToolService`, `.__init__`, `InvitationOut`, `dashboard_templates/controller.py`, `LoaderService`, `results/dto.py`, `AdTagService`, `MfaService`, `currencies/controller.py`, `.uow`, `.__init__`, `RewardService`, `.__init__`, `.__init__`, `sites/controller.py`, `SiteService`, `ad_tag_public/service.py`, `reports/service.py`, `people/controller.py`, `mcm/controller.py`, `ClientService`, `auth/controller.py`, `PriceRuleService`, `schedules/controller.py`, `audit/controller.py`, `SavedViewService`, `modules/facebook/controller.py`, `client_notes/controller.py`, `DocumentService`, `members/controller.py`, `checklist_items/controller.py`, `Bucket`, `account/controller.py`, `gam_tools/service.py`, `ClientLoaderService`, `UserOut`, `.options`, `ClientAdTagService`, `SupportTaskService`, `RewardCache`, `GoalService`, `ClientPriceRuleService`, `costs/controller.py`, `clients/service.py`, `internal/rewards/controller.py`, `networks/service.py`, `google/controller.py`, `documents/controller.py`, `.__init__`, `checklists/controller.py`, `NetworkService`, `tasks/controller.py`, `PublicRewardService`, `ClientDocumentService`, `.__init__`, `goals/service.py`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Are the 192 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 192 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `ClientGoogleAdsService` be split into smaller, more focused modules?**
  _Cohesion score 0.06352941176470588 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `GoalTemplateOut`, `ClientGoogleAdsService`, `.trusted_uow`, `DashboardService`, `AlertService`, `objects`, `roles/controller.py`, `modules/google_ads/controller.py`, `contracts/controller.py`, `invoices/controller.py`, `schedules/controller.py`, `GoogleAdsService`, `GroupService`, `inventory/controller.py`, `FacebookService`, `api_keys/controller.py`, `GamToolService`, `security.py`, `InvitationOut`, `tasks`, `LoaderService`, `clients`, `results/dto.py`, `AdTagService`, `RewardService`, `sites/controller.py`, `SiteService`, `reports/service.py`, `people/controller.py`, `mcm/controller.py`, `ClientService`, `PriceRuleService`, `audit/controller.py`, `modules/facebook/controller.py`, `client_notes/controller.py`, `.runs`, `modules/rewards/controller.py`, `members/controller.py`, `checklists`, `Actor`, `gam_tools/service.py`, `Actor`, `ClientLoaderService`, `goals/controller.py`, `SupportTaskService`, `ClientAdTagService`, `RewardCache`, `GoalService`, `Actor`, `ClientPriceRuleService`, `costs/controller.py`, `clients/service.py`, `internal/rewards/controller.py`, `networks/service.py`, `objects`, `PriceRuleSiteOut`, `checklists/controller.py`, `Actor`, `tasks/controller.py`, `NetworkService`, `UnitOfWorkFactory`, `get`, `ItemsOut`, `.update`, `.assign`, `networks/controller.py`, `goals/service.py`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **Are the 97 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 97 INFERRED edges - model-reasoned connections that need verification._
- **Should `.trusted_uow` be split into smaller, more focused modules?**
  _Cohesion score 0.07622504537205081 - nodes in this community are weakly interconnected._