# Graph Report - avant-api  (2026-11-20)

## Corpus Check
- 416 files · ~140,964 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 6308 nodes · 17641 edges · 290 communities (147 shown, 143 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2777 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `bc6b04b7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- objects
- .trusted_uow
- roles/controller.py
- DashboardService
- AlertService
- _member_client
- ClientFacebookService
- GoogleAdsService
- steps
- schedules/controller.py
- Avant: conexão com o GAM
- test_mfa.py
- test_hardening.py
- GroupService
- inventory/dto.py
- .uow
- api_keys/controller.py
- staff/controller.py
- errors.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- modules/google_ads/controller.py
- dashboard_templates/controller.py
- invoice_pdf.py
- router.py
- ReportService
- AdTagService
- mfa/controller.py
- currencies/controller.py
- reports/controller.py
- CapturingMailer
- forget_pages
- session-start.sh
- avant-api
- test_price_rules.py
- PublicAdTagService
- DomainError
- get
- mcm/controller.py
- .trusted_uow
- auth/controller.py
- PriceRuleService
- modules/ad_tags/dto.py
- Services
- CapturingMailer
- views/controller.py
- profile/controller.py
- modules/facebook/controller.py
- client_notes/controller.py
- templates
- modules/rewards/service.py
- Avant: endpoints da API do MVP
- DocumentService
- members/controller.py
- test_api_keys.py
- checklist_items/controller.py
- price_floor_public/service.py
- modules/rewards/controller.py
- account/controller.py
- export.py
- test_cache_down_does_not_break_the_page_or_the_save
- ads.py
- SessionCookies
- SiteChecklistService
- ClientLoaderService
- .of
- clean_code.py
- pytest
- SupportTaskService
- AdTagOut
- avant-api
- CeleryQueue
- UnitOfWorkFactory
- pool_metrics.py
- staff/controller.py
- ClientPriceRuleService
- costs/controller.py
- GoogleFailed
- clients/service.py
- Actor
- ad_tag_public/dto.py
- GoogleService
- AdUnitOut
- Avant: grupos na Empresa e imagem da Empresa
- RedisCounter
- Groone Avant: contexto do projeto
- oauth_callback
- checklists
- tasks/controller.py
- _csrf
- PublicRewardService
- ClientDocumentService
- dollars
- documents.py
- updates
- Avant: conexão com o GAM
- Avant: repositório e plano do MVP
- TaskQueue
- collections_abc
- test_dashboards.py
- audit/controller.py
- datetime
- conftest.py
- CompanyService
- contracts/controller.py
- commissions/controller.py
- FacebookAlertSettingOut
- Arquitetura do MVP do Avant
- test_alerts.py
- GamToolService
- tasks
- modules/loaders/service.py
- LoaderService
- test_invitation_mail.py
- events.py
- test_company_image.py
- avant_core_access_models
- test_api.py
- image_response
- sites/controller.py
- Settings
- StreamLimiter
- FacebookRuleIn
- test_facebook.py
- reports/service.py
- shared/dto.py
- mine
- swagger_assets.py
- forget_site
- errors.py
- receive
- goals/controller.py
- GoalService
- AdTagVersionOut
- set_person
- ClientDocumentOut
- main.py
- BaseModel
- checklists
- reward_public/service.py
- logs.py
- RewardAdUnitGroupOut
- team
- SiteService
- FakeGoogleAds
- company/controller.py
- RedisEvents
- AdTagHealthOut
- google_status
- ._adapters
- capped
- CompanyFiscalOut
- internal/rewards/controller.py
- mcm/service.py
- FakeFacebook
- .detail
- objects
- test_account.py
- FacebookControlOut
- .classify
- RedisKeyValueBuffer
- HealthService
- _BrokenAuthService
- reward_public/dto.py
- openapi
- ItemsOut
- TaskPatchIn
- google_start
- .of
- AdTagUnitDayOut
- pydantic
- SupportTaskService
- Actor
- metrics
- checklists/dto.py
- .assign
- document_response
- networks/controller.py
- LoaderOptionOut
- .page_saved
- GoalTemplateOut
- revoke
- image
- client_image
- RewardStyleIO
- delete_template
- pdf
- FakeGoogle

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 246 edges
2. `PageOut` - 233 edges
3. `get()` - 214 edges
4. `_csrf()` - 201 edges
5. `_onboard_owner()` - 196 edges
6. `UnitOfWorkFactory` - 175 edges
7. `Services` - 174 edges
8. `page_out()` - 97 edges
9. `_staff()` - 94 edges
10. `FacebookService` - 88 edges

## Surprising Connections (you probably didn't know these)
- `Onde está o trabalho` --references--> `PriceRuleSiteOut`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/price_rules/dto.py
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `Como funciona` --references--> `Services`  [INFERRED]
  README.md → src/avant_api/app/container.py
- `Estrutura` --references--> `Services`  [INFERRED]
  README.md → src/avant_api/app/container.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/modules/company/controller.py

## Import Cycles
- None detected.

## Communities (290 total, 143 thin omitted)

### Community 0 - "objects"
Cohesion: 0.08
Nodes (6): accounts(), alerts(), changes(), keywords(), objects(), show_object()

### Community 1 - ".trusted_uow"
Cohesion: 0.06
Nodes (29): FiscalDataIn, add_item(), available_months(), create_service(), delete(), delete_service(), issue(), mine() (+21 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "_member_client"
Cohesion: 0.07
Nodes (24): _membership_ids(), test_groups_lifecycle(), _assert_denied(), _queue(), test_cost_writes_need_permission(), test_documents_need_company_edit(), test_member_writes_need_permission(), test_network_sync_and_disconnect_need_permission() (+16 more)

### Community 6 - "ClientFacebookService"
Cohesion: 0.07
Nodes (14): FacebookAlertOut, FacebookChangeOut, FacebookObjectDetailOut, FacebookObjectOut, FacebookRuleDecisionOut, FacebookRuleOut, accounts(), alerts() (+6 more)

### Community 7 - "GoogleAdsService"
Cohesion: 0.06
Nodes (4): GoogleAdsNotConfigured, update_account(), google_ads_service(), GoogleAdsService

### Community 8 - "steps"
Cohesion: 0.07
Nodes (33): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, jobs (+25 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: conexão com o GAM"
Cohesion: 0.10
Nodes (20): Acesso, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade (+12 more)

### Community 11 - "test_mfa.py"
Cohesion: 0.11
Nodes (23): run_password_reset_tasks(), _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites() (+15 more)

### Community 12 - "test_hardening.py"
Cohesion: 0.17
Nodes (12): _rendered(), test_api_key_never_reaches_the_log(), test_docs_only_for_the_groone_session_with_2fa(), test_every_response_has_the_content_security_policy(), test_every_response_has_the_security_headers(), test_invalid_bearer_is_limited_per_ip_before_the_database(), counting(), test_old_docs_paths_do_not_exist() (+4 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.12
Nodes (7): networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, PageOut

### Community 15 - ".uow"
Cohesion: 0.06
Nodes (10): accounts(), people(), set_person(), update_account(), facebook_service(), FacebookAccountIn, FacebookAccountOut, FacebookPersonIn (+2 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.12
Nodes (6): create(), index(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "staff/controller.py"
Cohesion: 0.08
Nodes (9): InvitationMailNotSent, cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService, InvitationOut (+1 more)

### Community 18 - "errors.py"
Cohesion: 0.06
Nodes (20): CompanyChanged, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor(), get_auth() (+12 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (11): check(), create(), delete(), index(), update(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn (+3 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "modules/google_ads/controller.py"
Cohesion: 0.10
Nodes (20): GoogleAdsAccountIn, GoogleAdsAccountOut, GoogleAdsAccountRefOut, GoogleAdsAlertOut, GoogleAdsAlertSettingOut, GoogleAdsChangeOut, GoogleAdsDailyOut, GoogleAdsKeywordOut (+12 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "ReportService"
Cohesion: 0.06
Nodes (3): pinned(), SavedReportOut, ReportService

### Community 27 - "AdTagService"
Cohesion: 0.12
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.06
Nodes (14): get_cookies(), google_redirects(), google_service(), GoogleStatusOut, GoogleRedirects, confirm(), disable(), new_recovery_codes() (+6 more)

### Community 29 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "reports/controller.py"
Cohesion: 0.07
Nodes (16): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), query() (+8 more)

### Community 31 - "CapturingMailer"
Cohesion: 0.09
Nodes (22): FixedCountries, _buffer(), _cascade_reward(), test_events_and_leads_go_to_the_buffer(), test_icon_route_has_the_ip_limit(), test_price_rule_settings_forget_reward_page(), test_public_config_is_cached_and_cleared(), test_reward_page_has_cascade_for_rewards_block() (+14 more)

### Community 32 - "forget_pages"
Cohesion: 0.09
Nodes (6): forget_pages(), create(), update(), RewardIn, RewardOut, RewardService

### Community 36 - "test_price_rules.py"
Cohesion: 0.14
Nodes (26): _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _offerwall_unit(), _present(), _rule() (+18 more)

### Community 37 - "PublicAdTagService"
Cohesion: 0.09
Nodes (8): RedisRewardBuffer, RewardBuffer, config(), page_views(), preflight(), public_ad_tag_service(), PageViewIn, PublicAdTagService

### Community 38 - "DomainError"
Cohesion: 0.07
Nodes (8): FacebookDenied, FacebookMediaTooLarge, FacebookNotConfigured, FacebookStateInvalid, QueueUnavailable, oauth_callback(), oauth_start(), media_upload()

### Community 39 - "get"
Cohesion: 0.10
Nodes (13): accounts(), alert_settings(), alerts(), changes(), keywords(), logins(), objects(), people() (+5 more)

### Community 40 - "mcm/controller.py"
Cohesion: 0.11
Nodes (9): confirm_network(), register_network(), reject_network(), unassigned_networks(), mcm_service(), ClientNetworkIn, McmCandidateOut, McmService (+1 more)

### Community 41 - ".trusted_uow"
Cohesion: 0.06
Nodes (29): audit(), cancel_owner(), change_status(), client(), client_options(), client_teams(), edit_client(), edit_client_image() (+21 more)

### Community 42 - "auth/controller.py"
Cohesion: 0.07
Nodes (18): SessionCookies, accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company() (+10 more)

### Community 43 - "PriceRuleService"
Cohesion: 0.06
Nodes (14): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+6 more)

### Community 44 - "modules/ad_tags/dto.py"
Cohesion: 0.11
Nodes (11): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagDraftIO, AdTagHealthDayOut, AdTagIn, AdTagLiveOut (+3 more)

### Community 45 - "Services"
Cohesion: 0.03
Nodes (31): Services, get_services(), account_service(), alert_service(), api_key_service(), auth_service(), company_service(), custom_metric_service() (+23 more)

### Community 46 - "CapturingMailer"
Cohesion: 0.06
Nodes (55): CapturingMailer, _onboard_owner(), _checked_out(), _checkouts(), PoolWatchingEvents, test_downloads_give_the_connection_back(), test_event_stream_holds_no_connection(), test_report_requests_use_few_connections() (+47 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "profile/controller.py"
Cohesion: 0.18
Nodes (4): edit_appearance(), AppearanceIn, AppearanceOut, ProfileService

### Community 49 - "modules/facebook/controller.py"
Cohesion: 0.05
Nodes (12): create(), edit(), profiles(), FacebookAdIn, FacebookAdsetIn, FacebookCardIn, FacebookDraftIn, FacebookEditIn (+4 more)

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (8): add(), delete(), edit(), notes(), ClientNoteIn, ClientNoteOut, NotePersonOut, ClientNoteService

### Community 52 - "modules/rewards/service.py"
Cohesion: 0.08
Nodes (13): metrics(), metrics(), RewardActiveIn, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut (+5 more)

### Community 53 - "Avant: endpoints da API do MVP"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "DocumentService"
Cohesion: 0.12
Nodes (4): documents(), download(), upload(), DocumentService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.16
Nodes (14): BucketResult, MemoryBucket, _bearer(), _create(), _exercise(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company() (+6 more)

### Community 57 - "checklist_items/controller.py"
Cohesion: 0.11
Nodes (9): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+1 more)

### Community 58 - "price_floor_public/service.py"
Cohesion: 0.07
Nodes (7): CountryLookup, is_cascade_shape(), safe_site_cascades(), site_cascades(), prices(), PublicPriceFloorsOut, PublicPriceFloorService

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.08
Nodes (12): delete(), delete_lead(), export_leads(), index(), leads(), set_active(), set_icon(), show() (+4 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (12): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn (+4 more)

### Community 61 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 62 - "test_cache_down_does_not_break_the_page_or_the_save"
Cohesion: 0.14
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "ads.py"
Cohesion: 0.08
Nodes (3): micros(), money(), period()

### Community 65 - "SiteChecklistService"
Cohesion: 0.09
Nodes (8): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistDetailOut, SiteChecklistService

### Community 66 - "ClientLoaderService"
Cohesion: 0.15
Nodes (8): create(), delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService

### Community 67 - ".of"
Cohesion: 0.14
Nodes (3): edit_image(), remove_image(), UserOut

### Community 68 - "clean_code.py"
Cohesion: 0.09
Nodes (10): check_file(), docstring_problems(), inline_comments(), is_exempt(), main(), single_letter_names(), source_files(), exposition() (+2 more)

### Community 69 - "pytest"
Cohesion: 0.09
Nodes (11): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+3 more)

### Community 71 - "AdTagOut"
Cohesion: 0.09
Nodes (13): forget_tag(), AdTagOut, create(), delete(), health(), index(), publish(), restore() (+5 more)

### Community 74 - "CeleryQueue"
Cohesion: 0.19
Nodes (5): CeleryQueue, masked_args(), _CapturingCelery, test_password_reset_task_masks_the_email_in_the_message(), test_tasks_with_ids_only_are_not_masked()

### Community 75 - "UnitOfWorkFactory"
Cohesion: 0.04
Nodes (5): ad_tag_cache_key(), UnitOfWorkFactory, RewardCache, forget_tags(), page_out()

### Community 76 - "pool_metrics.py"
Cohesion: 0.13
Nodes (8): _checked_in(), _checked_out(), _closed(), _opened(), watch_pool(), _sample(), test_pool_gauges_follow_checkout_and_close(), test_pool_timeouts_count_only_the_pool_wait()

### Community 77 - "staff/controller.py"
Cohesion: 0.11
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 78 - "ClientPriceRuleService"
Cohesion: 0.07
Nodes (28): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+20 more)

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "GoogleFailed"
Cohesion: 0.15
Nodes (4): GoogleFailed, _claims(), GoogleOAuth, identity_from_id_token()

### Community 81 - "clients/service.py"
Cohesion: 0.12
Nodes (5): ClientMemberOut, ClientProfileIn, CompanyRefOut, RevenueStatusOut, RoleRefOut

### Community 82 - "Actor"
Cohesion: 0.10
Nodes (9): alerts(), changes(), disconnect(), duplicate(), job(), read_alert(), rule_decisions(), upload_media() (+1 more)

### Community 83 - "ad_tag_public/dto.py"
Cohesion: 0.13
Nodes (6): PageViewBlockIn, PublicAdTagOut, PublicBlockOut, PublicLoaderOut, PublicMgidOut, PublicTagOut

### Community 85 - "GoogleService"
Cohesion: 0.12
Nodes (4): GoogleUnavailable, GoogleAuth, google_callback(), GoogleService

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (15): Arquitetura, Como trabalhar nos repositórios, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação (+7 more)

### Community 91 - "oauth_callback"
Cohesion: 0.13
Nodes (5): GoogleAdsDenied, GoogleAdsStateInvalid, oauth_callback(), oauth_start(), GoogleAdsRedirects

### Community 96 - "_csrf"
Cohesion: 0.05
Nodes (43): browser(), _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock (+35 more)

### Community 97 - "PublicRewardService"
Cohesion: 0.14
Nodes (9): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body() (+1 more)

### Community 98 - "ClientDocumentService"
Cohesion: 0.15
Nodes (7): approve(), documents(), download(), reject(), ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 102 - "dollars"
Cohesion: 0.09
Nodes (3): dollars(), InvoiceItemOut, ReturnedOut

### Community 123 - "documents.py"
Cohesion: 0.18
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 127 - "updates"
Cohesion: 0.11
Nodes (17): patterns, patterns, update-types, acoes, dependencias, imagens, dependency-name, patterns (+9 more)

### Community 128 - "Avant: conexão com o GAM"
Cohesion: 0.11
Nodes (16): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment, Avant: conexão com o GAM, Caminho conta de serviço (+8 more)

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.22
Nodes (8): Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11), Resumo, Serviços e ferramentas

### Community 130 - "TaskQueue"
Cohesion: 0.11
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskMailQueue, TaskQueue

### Community 131 - "collections_abc"
Cohesion: 0.22
Nodes (4): ExportsBusy, export_slot(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 132 - "test_dashboards.py"
Cohesion: 0.20
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 133 - "audit/controller.py"
Cohesion: 0.15
Nodes (3): index(), audit_service(), AuditService

### Community 134 - "datetime"
Cohesion: 0.06
Nodes (18): refresh_levels(), _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites() (+10 more)

### Community 135 - "conftest.py"
Cohesion: 0.03
Nodes (28): client(), engine(), mailer(), memory_services(), MemoryCounter, MemoryKeyValueBuffer, MemoryRewardBuffer, MemoryRewardCache (+20 more)

### Community 136 - "CompanyService"
Cohesion: 0.19
Nodes (4): show(), CompanyDetailOut, CompanyPatchIn, CompanyService

### Community 137 - "contracts/controller.py"
Cohesion: 0.05
Nodes (20): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+12 more)

### Community 138 - "commissions/controller.py"
Cohesion: 0.06
Nodes (22): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+14 more)

### Community 142 - "FacebookAlertSettingOut"
Cohesion: 0.15
Nodes (3): alert_settings(), set_alert_settings(), FacebookAlertSettingOut

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.14
Nodes (13): Ambientes, deploy e backup, Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões (+5 more)

### Community 144 - "test_alerts.py"
Cohesion: 0.17
Nodes (7): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), test_null_byte_in_search_and_report_filter_is_invalid_input(), test_public_page_url_with_brackets_is_just_not_found()

### Community 145 - "GamToolService"
Cohesion: 0.05
Nodes (18): ads_txt(), install(), network(), networks(), run(), runs(), start(), AdsTxtOut (+10 more)

### Community 146 - "tasks"
Cohesion: 0.22
Nodes (4): change(), comment(), create(), task()

### Community 147 - "modules/loaders/service.py"
Cohesion: 0.11
Nodes (3): ClientLoaderIn, LoaderClientOut, LoaderTagOut

### Community 148 - "LoaderService"
Cohesion: 0.13
Nodes (8): create(), delete(), index(), show(), update(), LoaderIn, LoaderOut, LoaderService

### Community 149 - "test_invitation_mail.py"
Cohesion: 0.24
Nodes (10): _assert_mail_not_sent(), _client_with_owner_invitation(), _invite(), _owner_invitation_emails(), _pending_emails(), test_invite_answers_503_when_the_mail_fails(), test_owner_invitation_answers_503_when_the_mail_fails(), test_owner_invitation_resend_answers_503_when_the_mail_fails() (+2 more)

### Community 150 - "events.py"
Cohesion: 0.15
Nodes (11): channel(), _parse(), sse(), _collect(), _event(), ListEvents, test_facebook_job_updates_reach_who_sees_facebook(), test_gam_tool_runs_reach_who_sees_the_gam_tools() (+3 more)

### Community 152 - "test_company_image.py"
Cohesion: 0.08
Nodes (20): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, _after_first_segment(), _jpeg(), _png(), _put_image() (+12 more)

### Community 153 - "avant_core_access_models"
Cohesion: 0.05
Nodes (11): results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut (+3 more)

### Community 155 - "test_api.py"
Cohesion: 0.12
Nodes (21): Sent, _error_code(), _owner_invite(), test_csrf_is_required_for_writes(), test_every_write_route_refuses_another_site(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit() (+13 more)

### Community 158 - "image_response"
Cohesion: 0.15
Nodes (3): image(), image_response(), image_upload()

### Community 161 - "sites/controller.py"
Cohesion: 0.20
Nodes (9): create(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn (+1 more)

### Community 162 - "Settings"
Cohesion: 0.05
Nodes (22): engine_settings(), _facebook(), _google(), _google_ads(), _mailer(), restricted_engine(), GeoLiteCountries, NoCountries (+14 more)

### Community 163 - "StreamLimiter"
Cohesion: 0.15
Nodes (3): StreamLimiter, events(), test_stream_limiter_caps_each_person_and_the_process()

### Community 164 - "FacebookRuleIn"
Cohesion: 0.14
Nodes (3): rule(), set_rule(), FacebookRuleIn

### Community 165 - "test_facebook.py"
Cohesion: 0.11
Nodes (15): _configure(), _connect(), _draft(), _services(), _sync(), test_facebook_control_and_rules(), test_facebook_create_edit_duplicate_lists_and_media(), test_facebook_panel() (+7 more)

### Community 166 - "reports/service.py"
Cohesion: 0.05
Nodes (19): QueryTooHeavy, catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn (+11 more)

### Community 167 - "shared/dto.py"
Cohesion: 0.11
Nodes (7): disable(), enable(), reset_mfa(), users(), PersonOut, PeopleService, person_out()

### Community 168 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 171 - "swagger_assets.py"
Cohesion: 0.13
Nodes (6): challenge(), ExpectedAsset, load_assets(), SwaggerAsset, SwaggerAssetChanged, test_changed_asset_stops_the_start()

### Community 172 - "forget_site"
Cohesion: 0.19
Nodes (5): reward_cache_key(), forget_cascades(), forget_floors(), forget_rule(), forget_site()

### Community 174 - "errors.py"
Cohesion: 0.13
Nodes (12): error_body(), install(), database_data_error(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error() (+4 more)

### Community 175 - "receive"
Cohesion: 0.16
Nodes (9): POSTGRES_PASSWORD, env, image, options, ports, postgres, cors(), preflight() (+1 more)

### Community 176 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 177 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 180 - "set_person"
Cohesion: 0.15
Nodes (5): apply_suffix(), disconnect(), read_alert(), set_alert_settings(), set_person()

### Community 183 - "main.py"
Cohesion: 0.05
Nodes (19): CsrfFailed, EventSource, check_fetch_site(), _are_proxy_addresses(), invalid_variable_names(), InvalidVariables, _is_smtp_url(), load_settings() (+11 more)

### Community 184 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 185 - "checklists"
Cohesion: 0.21
Nodes (3): months(), summary(), ChecklistMonthOut

### Community 186 - "reward_public/service.py"
Cohesion: 0.07
Nodes (9): RateLimited, Bucket, BucketRule, CachedPage, PublicPageOut, PublicRewardPriceOut, RewardLeadIn, public_control_percent() (+1 more)

### Community 188 - "logs.py"
Cohesion: 0.17
Nodes (5): configure_logging(), JsonFormatter, _record(), test_log_keeps_ordinary_messages(), test_log_masks_database_values_in_message_and_stack()

### Community 192 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 194 - "company/controller.py"
Cohesion: 0.21
Nodes (4): edit_fiscal(), edit_image(), fiscal(), remove_image()

### Community 198 - "._adapters"
Cohesion: 0.11
Nodes (3): options(), FacebookOptionOut, _CachedOptions

### Community 210 - "internal/rewards/controller.py"
Cohesion: 0.11
Nodes (13): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), set_active() (+5 more)

### Community 213 - ".detail"
Cohesion: 0.06
Nodes (8): set_budget(), FacebookAccountRefOut, FacebookBudgetIn, FacebookBudgetOut, FacebookCountryOut, FacebookDailyOut, FacebookParentOut, FacebookTotalsOut

### Community 215 - "test_account.py"
Cohesion: 0.21
Nodes (10): _BrokenReleaseCounter, _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login() (+2 more)

### Community 218 - "FacebookControlOut"
Cohesion: 0.24
Nodes (3): set_status(), FacebookControlOut, FacebookStatusIn

### Community 221 - "RedisKeyValueBuffer"
Cohesion: 0.15
Nodes (3): KeyValueBuffer, RedisKeyValueBuffer, test_redis_buffer_follows_the_worker_contract()

### Community 225 - "reward_public/dto.py"
Cohesion: 0.23
Nodes (9): PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicQuestionOut, PublicRewardOut, PublicStyleOut, RewardEventIn, RewardEventsIn (+1 more)

### Community 226 - "openapi"
Cohesion: 0.15
Nodes (4): openapi(), swagger(), swagger_asset(), _swagger_page()

### Community 227 - "ItemsOut"
Cohesion: 0.12
Nodes (9): ad_units(), assign_sites(), delete(), index(), show(), site_options(), sites_of_member(), unlinked() (+1 more)

### Community 239 - "google_start"
Cohesion: 0.22
Nodes (3): new_verifier(), google_start(), test_google_flow_cookie_is_always_secure()

### Community 242 - "pydantic"
Cohesion: 0.10
Nodes (5): _content_security_policy(), observe(), _route_template(), KeyValueIn, receive_key_values()

### Community 243 - "SupportTaskService"
Cohesion: 0.15
Nodes (4): tasks(), support_task_service(), TaskOut, SupportTaskService

### Community 246 - "checklists/dto.py"
Cohesion: 0.11
Nodes (6): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 247 - ".assign"
Cohesion: 0.10
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 250 - "networks/controller.py"
Cohesion: 0.10
Nodes (14): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+6 more)

### Community 256 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2885 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **143 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `.trusted_uow`, `TaskQueue`, `DashboardService`, `AlertService`, `audit/controller.py`, `ClientFacebookService`, `GoogleAdsService`, `CompanyService`, `contracts/controller.py`, `.__init__`, `commissions/controller.py`, `roles/controller.py`, `GroupService`, `inventory/dto.py`, `.uow`, `.__init__`, `api_keys/controller.py`, `GamToolService`, `custom_metrics/controller.py`, `.__init__`, `staff/controller.py`, `modules/google_ads/controller.py`, `dashboard_templates/controller.py`, `.__init__`, `avant_core_access_models`, `ReportService`, `AdTagService`, `.__init__`, `currencies/controller.py`, `mfa/controller.py`, `forget_pages`, `sites/controller.py`, `PublicAdTagService`, `reports/service.py`, `shared/dto.py`, `mcm/controller.py`, `.trusted_uow`, `auth/controller.py`, `PriceRuleService`, `schedules/controller.py`, `views/controller.py`, `profile/controller.py`, `modules/facebook/controller.py`, `client_notes/controller.py`, `GoalService`, `DocumentService`, `members/controller.py`, `checklist_items/controller.py`, `price_floor_public/service.py`, `reward_public/service.py`, `account/controller.py`, `SiteService`, `SiteChecklistService`, `ClientLoaderService`, `._adapters`, `AdTagOut`, `.__init__`, `staff/controller.py`, `ClientPriceRuleService`, `costs/controller.py`, `clients/service.py`, `internal/rewards/controller.py`, `mcm/service.py`, `GoogleService`, `.__init__`, `tasks/controller.py`, `ClientDocumentService`, `LoaderService`, `SupportTaskService`, `networks/controller.py`, `documents.py`, `goals/service.py`?**
  _High betweenness centrality (0.119) - this node is a cross-community bridge._
- **Are the 192 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 192 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `objects` be split into smaller, more focused modules?**
  _Cohesion score 0.07936507936507936 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `inventory/dto.py` to `GoalTemplateOut`, `objects`, `.trusted_uow`, `DashboardService`, `AlertService`, `audit/controller.py`, `.of`, `GoogleAdsService`, `ClientFacebookService`, `contracts/controller.py`, `roles/controller.py`, `schedules/controller.py`, `GroupService`, `.uow`, `api_keys/controller.py`, `GamToolService`, `tasks`, `staff/controller.py`, `LoaderService`, `modules/google_ads/controller.py`, `router.py`, `avant_core_access_models`, `AdTagService`, `forget_pages`, `sites/controller.py`, `reports/service.py`, `get`, `mcm/controller.py`, `.trusted_uow`, `shared/dto.py`, `PriceRuleService`, `Services`, `goals/controller.py`, `modules/facebook/controller.py`, `client_notes/controller.py`, `GoalService`, `members/controller.py`, `modules/rewards/controller.py`, `team`, `SiteService`, `SiteChecklistService`, `ClientLoaderService`, `AdTagOut`, `UnitOfWorkFactory`, `staff/controller.py`, `ClientPriceRuleService`, `costs/controller.py`, `clients/service.py`, `Actor`, `mcm/service.py`, `internal/rewards/controller.py`, `objects`, `checklists`, `ClientRewardService`, `tasks/controller.py`, `ItemsOut`, `LoaderOut`, `SupportTaskService`, `.assign`, `networks/controller.py`, `.page_saved`, `goals/service.py`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Are the 93 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 93 INFERRED edges - model-reasoned connections that need verification._
- **Should `.trusted_uow` be split into smaller, more focused modules?**
  _Cohesion score 0.05567765567765568 - nodes in this community are weakly interconnected._