# Graph Report - avant-api  (2026-11-19)

## Corpus Check
- 415 files · ~140,628 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 6299 nodes · 17620 edges · 267 communities (142 shown, 125 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2777 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `75bbb0ce`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- PageOut
- InvoiceService
- roles/controller.py
- DashboardService
- AlertService
- _member_client
- ClientFacebookService
- modules/google_ads/controller.py
- steps
- schedules/controller.py
- Avant: conexão com o GAM
- test_mfa.py
- browser
- GroupService
- inventory/dto.py
- FacebookService
- api_keys/controller.py
- staff/controller.py
- errors.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- _agent
- dashboard_templates/controller.py
- invoice_pdf.py
- router.py
- .uow
- AdTagService
- mfa/controller.py
- UnitOfWorkFactory
- ReportService
- CapturingMailer
- forget_pages
- session-start.sh
- avant-api
- test_price_rules.py
- limits.py
- contracts/controller.py
- modules/price_rules/controller.py
- mcm/controller.py
- .trusted_uow
- auth/controller.py
- PriceRuleService
- modules/ad_tags/dto.py
- Services
- test_reports.py
- views/controller.py
- profile/controller.py
- BaseModel
- client_notes/controller.py
- DashboardTemplateOut
- modules/rewards/service.py
- Avant: endpoints da API do MVP
- client_documents/controller.py
- members/controller.py
- test_api_keys.py
- checklist_items/controller.py
- PublicPriceFloorService
- modules/rewards/controller.py
- account/controller.py
- export.py
- test_cache_down_does_not_break_the_page_or_the_save
- .of
- SessionCookies
- mark
- ClientLoaderService
- .of
- clean_code.py
- pytest
- SupportTaskService
- AdTagOut
- avant-api
- CeleryQueue
- ports.py
- pool_metrics.py
- .of
- ClientPriceRuleService
- costs/controller.py
- test_account.py
- .of
- person
- PriceRuleHourOut
- GoogleService
- AdUnitOut
- Avant: grupos na Empresa e imagem da Empresa
- RedisCounter
- Groone Avant: contexto do projeto
- ResultService
- checklists/controller.py
- ClientRewardService
- tasks/controller.py
- _csrf
- PublicRewardService
- ClientDocumentService
- commissions/dto.py
- test_permission_denied.py
- updates
- verify
- Avant: repositório e plano do MVP
- TaskQueue
- collections_abc
- test_dashboards.py
- Actor
- conftest.py
- test_mail_queue.py
- company/controller.py
- ContractService
- commissions/controller.py
- ads.py
- settings_for_tests
- Arquitetura do MVP do Avant
- test_alerts.py
- GamToolService
- tasks
- modules/loaders/service.py
- LoaderService
- test_invitation_mail.py
- test_events.py
- test_company_image.py
- avant_core_access_models
- _onboard_owner
- image_response
- PayeeDetailsOut
- sites/controller.py
- Settings
- .update
- test_facebook.py
- reports/service.py
- shared/dto.py
- create_app
- swagger_assets.py
- forget_site
- install
- CommissionService
- _SpyCounter
- .of_details
- AdTagVersionOut
- mine
- team
- settings.py
- BaseModel
- checklists
- MemoryBucket
- logs.py
- RewardAdUnitGroupOut
- ReportQueryIn
- .assign
- FakeGoogleAds
- count_pool_timeout
- RedisEvents
- AdTagHealthOut
- adjust
- capped
- test_google_ads_panel
- internal/rewards/controller.py
- mcm/service.py
- FakeFacebook
- PriceRuleHistoryOut
- _BrokenReleaseCounter
- rewards/http.py
- .classify
- RedisKeyValueBuffer
- _BrokenAuthService
- reward_public/service.py
- get
- ItemsOut
- TaskPatchIn
- SiteListOut
- LoaderOut
- RateLimited
- test_key_values.py
- SiteService
- AuthService
- networks/controller.py
- GoalService
- RedisRewardBuffer
- .of
- invoices/controller.py

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

## Communities (267 total, 125 thin omitted)

### Community 0 - "PageOut"
Cohesion: 0.07
Nodes (5): index(), AuditService, AuditOut, page_out(), PageOut

### Community 1 - "InvoiceService"
Cohesion: 0.08
Nodes (13): add_item(), create(), delete(), delete_service(), issue(), pay(), pdf(), remove_item() (+5 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (25): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+17 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "_member_client"
Cohesion: 0.10
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 6 - "ClientFacebookService"
Cohesion: 0.08
Nodes (9): accounts(), alerts(), changes(), objects(), rule(), rule_decisions(), show_object(), client_facebook_service() (+1 more)

### Community 7 - "modules/google_ads/controller.py"
Cohesion: 0.02
Nodes (51): GoogleAdsDenied, GoogleAdsNotConfigured, accounts(), alert_settings(), alerts(), apply_suffix(), changes(), disconnect() (+43 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (38): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, POSTGRES_PASSWORD (+30 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: conexão com o GAM"
Cohesion: 0.05
Nodes (36): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+28 more)

### Community 11 - "test_mfa.py"
Cohesion: 0.31
Nodes (13): run_password_reset_tasks(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice() (+5 more)

### Community 12 - "browser"
Cohesion: 0.08
Nodes (27): browser(), client(), engine(), mailer(), test_change_password_and_sessions(), query(), _rendered(), test_api_key_never_reaches_the_log() (+19 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+6 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.08
Nodes (8): networks(), sites(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, image_url()

### Community 15 - "FacebookService"
Cohesion: 0.02
Nodes (59): FacebookNotConfigured, QueueUnavailable, accounts(), alert_settings(), alerts(), changes(), create(), disconnect() (+51 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "staff/controller.py"
Cohesion: 0.06
Nodes (15): InvitationMailNotSent, invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, cancel() (+7 more)

### Community 18 - "errors.py"
Cohesion: 0.04
Nodes (27): CompanyChanged, CsrfFailed, FacebookDenied, FacebookMediaTooLarge, FacebookStateInvalid, GoogleAdsStateInvalid, NoActiveCompany, QueryTooHeavy (+19 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (11): check(), create(), delete(), index(), update(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn (+3 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "_agent"
Cohesion: 0.18
Nodes (10): _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads() (+2 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), roles(), set_home(), show(), update(), DashboardTemplateIn (+5 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.08
Nodes (12): dollars(), _block(), _dates(), _footer(), _header(), _items(), _line(), _logo() (+4 more)

### Community 27 - "AdTagService"
Cohesion: 0.12
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.11
Nodes (8): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut, MfaService

### Community 29 - "UnitOfWorkFactory"
Cohesion: 0.03
Nodes (6): UnitOfWorkFactory, list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.06
Nodes (20): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+12 more)

### Community 31 - "CapturingMailer"
Cohesion: 0.09
Nodes (23): reward_cache_key(), CapturingMailer, Sent, _buffer(), _cascade_reward(), test_events_and_leads_go_to_the_buffer(), test_icon_route_has_the_ip_limit(), test_price_rule_settings_forget_reward_page() (+15 more)

### Community 32 - "forget_pages"
Cohesion: 0.09
Nodes (3): create(), forget_pages(), RewardIn

### Community 36 - "test_price_rules.py"
Cohesion: 0.08
Nodes (33): FixedCountries, _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _cascade_rule(), _cascade_site() (+25 more)

### Community 37 - "limits.py"
Cohesion: 0.06
Nodes (14): Bucket, BucketRule, RewardBuffer, config(), page_views(), preflight(), PageViewBlockIn, PageViewIn (+6 more)

### Community 38 - "contracts/controller.py"
Cohesion: 0.18
Nodes (7): contract(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract(), ContractOut

### Community 39 - "modules/price_rules/controller.py"
Cohesion: 0.19
Nodes (12): CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn, PriceRuleOut (+4 more)

### Community 40 - "mcm/controller.py"
Cohesion: 0.10
Nodes (8): confirm_network(), register_network(), reject_network(), unassigned_networks(), ClientNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 41 - ".trusted_uow"
Cohesion: 0.05
Nodes (33): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), edit_client() (+25 more)

### Community 42 - "auth/controller.py"
Cohesion: 0.11
Nodes (12): company_image(), do_logout(), login(), me(), set_active_company(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut (+4 more)

### Community 43 - "PriceRuleService"
Cohesion: 0.07
Nodes (12): cascade_hours(), index(), set_floor(), set_status(), settings(), show(), sites(), update_blocks() (+4 more)

### Community 44 - "modules/ad_tags/dto.py"
Cohesion: 0.12
Nodes (11): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagHealthDayOut, AdTagIn, AdTagLiveOut, AdTagPublishIn (+3 more)

### Community 45 - "Services"
Cohesion: 0.02
Nodes (36): Services, new_verifier(), RedisRewardCache, get_auth(), get_cookies(), get_services(), known_companies(), public_ad_tag_service() (+28 more)

### Community 46 - "test_reports.py"
Cohesion: 0.11
Nodes (20): _checked_out(), _checkouts(), PoolWatchingEvents, test_downloads_give_the_connection_back(), test_event_stream_holds_no_connection(), test_report_requests_use_few_connections(), _day(), _metrics() (+12 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "profile/controller.py"
Cohesion: 0.20
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 49 - "BaseModel"
Cohesion: 0.10
Nodes (4): FacebookAdIn, FacebookAdsetIn, FacebookCardIn, FacebookPickIn

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "DashboardTemplateOut"
Cohesion: 0.13
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 52 - "modules/rewards/service.py"
Cohesion: 0.09
Nodes (12): RewardActiveIn, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO, RewardLeadOut (+4 more)

### Community 53 - "Avant: endpoints da API do MVP"
Cohesion: 0.15
Nodes (12): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+4 more)

### Community 54 - "client_documents/controller.py"
Cohesion: 0.06
Nodes (12): documents(), download(), upload(), document_service(), DocumentService, client_document_service(), ClientDocumentOut, RejectDocumentIn (+4 more)

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.33
Nodes (9): _bearer(), _create(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit() (+1 more)

### Community 57 - "checklist_items/controller.py"
Cohesion: 0.11
Nodes (9): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+1 more)

### Community 58 - "PublicPriceFloorService"
Cohesion: 0.14
Nodes (4): CountryLookup, prices(), PublicPriceFloorsOut, PublicPriceFloorService

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.10
Nodes (14): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+6 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "export.py"
Cohesion: 0.08
Nodes (13): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+5 more)

### Community 65 - "mark"
Cohesion: 0.14
Nodes (6): add_note(), check(), delete_note(), edit_note(), mark(), summary()

### Community 66 - "ClientLoaderService"
Cohesion: 0.15
Nodes (7): create(), delete(), index(), options(), show(), update(), ClientLoaderService

### Community 67 - ".of"
Cohesion: 0.09
Nodes (3): edit_image(), image(), remove_image()

### Community 68 - "clean_code.py"
Cohesion: 0.15
Nodes (7): check_file(), docstring_problems(), inline_comments(), is_exempt(), main(), single_letter_names(), source_files()

### Community 69 - "pytest"
Cohesion: 0.08
Nodes (11): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+3 more)

### Community 70 - "SupportTaskService"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 71 - "AdTagOut"
Cohesion: 0.09
Nodes (13): AdTagOut, create(), delete(), health(), index(), publish(), restore(), set_active() (+5 more)

### Community 74 - "CeleryQueue"
Cohesion: 0.19
Nodes (5): CeleryQueue, masked_args(), _CapturingCelery, test_password_reset_task_masks_the_email_in_the_message(), test_tasks_with_ids_only_are_not_masked()

### Community 75 - "ports.py"
Cohesion: 0.06
Nodes (5): ad_tag_cache_key(), is_cascade_shape(), safe_site_cascades(), site_cascades(), RewardCache

### Community 76 - "pool_metrics.py"
Cohesion: 0.15
Nodes (7): _checked_in(), _checked_out(), _closed(), _opened(), watch_pool(), _sample(), test_pool_gauges_follow_checkout_and_close()

### Community 77 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 78 - "ClientPriceRuleService"
Cohesion: 0.08
Nodes (14): cascade_hours(), index(), set_floor(), set_status(), settings(), show(), sites(), update_blocks() (+6 more)

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "test_account.py"
Cohesion: 0.08
Nodes (13): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _google_round(), _jwt() (+5 more)

### Community 83 - "person"
Cohesion: 0.18
Nodes (3): _month(), person(), WindowMonthOut

### Community 84 - "PriceRuleHourOut"
Cohesion: 0.21
Nodes (3): hours(), hours(), PriceRuleHourOut

### Community 85 - "GoogleService"
Cohesion: 0.06
Nodes (10): GoogleUnavailable, GoogleAuth, google_callback(), google_start(), google_status(), google_unlink(), GoogleStatusOut, GoogleRedirects (+2 more)

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (15): Arquitetura, Como trabalhar nos repositórios, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação (+7 more)

### Community 91 - "ResultService"
Cohesion: 0.15
Nodes (3): show(), result_service(), ResultService

### Community 92 - "checklists/controller.py"
Cohesion: 0.14
Nodes (12): checklist(), site_checklist_service(), ChecklistDetailOut, ChecklistMarkIn, ChecklistMonthOut, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut (+4 more)

### Community 94 - "ClientRewardService"
Cohesion: 0.13
Nodes (3): index(), ClientRewardService, RewardOut

### Community 95 - "tasks/controller.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 96 - "_csrf"
Cohesion: 0.06
Nodes (44): _csrf(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions() (+36 more)

### Community 97 - "PublicRewardService"
Cohesion: 0.08
Nodes (12): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body() (+4 more)

### Community 98 - "ClientDocumentService"
Cohesion: 0.09
Nodes (6): approve(), documents(), download(), reject(), ClientDocumentsOut, ClientDocumentService

### Community 102 - "commissions/dto.py"
Cohesion: 0.18
Nodes (3): CommissionMonthOut, CommissionSettingsIn, MonthIn

### Community 123 - "test_permission_denied.py"
Cohesion: 0.11
Nodes (13): _manage_inventory(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query(), _assert_denied(), _queue() (+5 more)

### Community 127 - "updates"
Cohesion: 0.11
Nodes (17): patterns, patterns, update-types, acoes, dependencias, imagens, dependency-name, patterns (+9 more)

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.22
Nodes (8): Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11), Resumo, Serviços e ferramentas

### Community 130 - "TaskQueue"
Cohesion: 0.10
Nodes (8): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskMailQueue, TaskQueue, enqueue_sync()

### Community 131 - "collections_abc"
Cohesion: 0.20
Nodes (4): ExportsBusy, export_slot(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 132 - "test_dashboards.py"
Cohesion: 0.15
Nodes (11): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request() (+3 more)

### Community 133 - "Actor"
Cohesion: 0.23
Nodes (3): set_settings(), settings(), CommissionSettingsOut

### Community 134 - "conftest.py"
Cohesion: 0.05
Nodes (10): refresh_levels(), MemoryRewardBuffer, MemoryRewardCache, NoEvents, _error_code(), test_cookies_are_always_secure_with_the_host_prefix(), test_every_write_route_refuses_another_site(), _scaling_client() (+2 more)

### Community 135 - "test_mail_queue.py"
Cohesion: 0.06
Nodes (13): memory_services(), MemoryCounter, MemoryKeyValueBuffer, RecordingQueue, _account(), _NoDatabase, _NoMail, _services() (+5 more)

### Community 136 - "company/controller.py"
Cohesion: 0.07
Nodes (14): Imagem da Empresa, edit(), edit_fiscal(), edit_image(), fiscal(), remove_image(), show(), company_service() (+6 more)

### Community 137 - "ContractService"
Cohesion: 0.11
Nodes (9): contract_networks(), _contract_fields(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractSummaryOut, _network_ref(), ContractService (+1 more)

### Community 138 - "commissions/controller.py"
Cohesion: 0.23
Nodes (5): create_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 139 - "ads.py"
Cohesion: 0.03
Nodes (4): object_filter(), micros(), money(), period()

### Community 142 - "settings_for_tests"
Cohesion: 0.08
Nodes (21): engine_settings(), restricted_engine(), load_settings(), settings_for_tests(), test_api_does_not_start_with_a_role_that_ignores_rls(), test_database_url_cannot_override_the_timeouts(), test_default_numbers_fit_the_connection_budget(), test_engine_settings_come_from_the_settings() (+13 more)

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.14
Nodes (13): Ambientes, deploy e backup, Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões (+5 more)

### Community 144 - "test_alerts.py"
Cohesion: 0.35
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 145 - "GamToolService"
Cohesion: 0.05
Nodes (19): ads_txt(), install(), network(), networks(), run(), runs(), start(), gam_tool_service() (+11 more)

### Community 146 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 147 - "modules/loaders/service.py"
Cohesion: 0.20
Nodes (5): ClientLoaderIn, LoaderClientOut, LoaderIn, LoaderOptionOut, LoaderTagOut

### Community 148 - "LoaderService"
Cohesion: 0.16
Nodes (8): create(), delete(), index(), options(), show(), update(), loader_service(), LoaderService

### Community 149 - "test_invitation_mail.py"
Cohesion: 0.22
Nodes (10): _assert_mail_not_sent(), _client_with_owner_invitation(), _invite(), _owner_invitation_emails(), _pending_emails(), test_invite_answers_503_when_the_mail_fails(), test_owner_invitation_answers_503_when_the_mail_fails(), test_owner_invitation_resend_answers_503_when_the_mail_fails() (+2 more)

### Community 150 - "test_events.py"
Cohesion: 0.08
Nodes (17): channel(), EventSource, _parse(), sse(), StreamLimiter, events(), EventService, _collect() (+9 more)

### Community 152 - "test_company_image.py"
Cohesion: 0.08
Nodes (20): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, _after_first_segment(), _jpeg(), _png(), _put_image() (+12 more)

### Community 153 - "avant_core_access_models"
Cohesion: 0.10
Nodes (5): results(), client_result_service(), ClientResultService, ResultsOut, default_period()

### Community 155 - "_onboard_owner"
Cohesion: 0.10
Nodes (39): test_change_password_attempts_are_limited(), _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session() (+31 more)

### Community 158 - "image_response"
Cohesion: 0.12
Nodes (3): image(), image_response(), image_upload()

### Community 160 - "PayeeDetailsOut"
Cohesion: 0.22
Nodes (3): payment_details(), save_payment_details(), PayeeDetailsOut

### Community 161 - "sites/controller.py"
Cohesion: 0.25
Nodes (7): AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 162 - "Settings"
Cohesion: 0.07
Nodes (7): _facebook(), _google(), _google_ads(), _mailer(), GeoLiteCountries, NoCountries, Settings

### Community 165 - "test_facebook.py"
Cohesion: 0.25
Nodes (9): _configure(), _connect(), _draft(), _services(), _sync(), test_facebook_control_and_rules(), test_facebook_create_edit_duplicate_lists_and_media(), test_facebook_panel() (+1 more)

### Community 166 - "reports/service.py"
Cohesion: 0.06
Nodes (15): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+7 more)

### Community 167 - "shared/dto.py"
Cohesion: 0.09
Nodes (10): disable(), enable(), reset_mfa(), users(), PersonOut, PeopleService, person_out(), CompanyRefOut (+2 more)

### Community 168 - "create_app"
Cohesion: 0.20
Nodes (4): _content_security_policy(), observe(), _route_template(), create_app()

### Community 171 - "swagger_assets.py"
Cohesion: 0.15
Nodes (5): ExpectedAsset, load_assets(), SwaggerAsset, SwaggerAssetChanged, test_changed_asset_stops_the_start()

### Community 172 - "forget_site"
Cohesion: 0.29
Nodes (3): forget_cascades(), forget_floors(), forget_site()

### Community 174 - "install"
Cohesion: 0.17
Nodes (10): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), _limit_details() (+2 more)

### Community 175 - "CommissionService"
Cohesion: 0.22
Nodes (3): delete_rule(), commission_service(), CommissionService

### Community 183 - "settings.py"
Cohesion: 0.12
Nodes (4): _are_proxy_addresses(), invalid_variable_names(), InvalidVariables, _is_smtp_url()

### Community 184 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 186 - "MemoryBucket"
Cohesion: 0.13
Nodes (6): BucketResult, RedisBucket, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 188 - "logs.py"
Cohesion: 0.17
Nodes (5): configure_logging(), JsonFormatter, _record(), test_log_keeps_ordinary_messages(), test_log_masks_database_values_in_message_and_stack()

### Community 192 - ".assign"
Cohesion: 0.40
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 202 - "test_google_ads_panel"
Cohesion: 0.24
Nodes (6): _configure(), _connect(), _services(), _sync(), test_google_ads_panel(), test_without_the_google_client_the_login_is_unavailable()

### Community 210 - "internal/rewards/controller.py"
Cohesion: 0.10
Nodes (11): ad_units(), delete(), delete_lead(), export_leads(), leads(), metrics(), set_active(), set_icon() (+3 more)

### Community 211 - "mcm/service.py"
Cohesion: 0.20
Nodes (3): NetworkIn, ServiceAccountOut, SyncRunOut

### Community 214 - "PriceRuleHistoryOut"
Cohesion: 0.21
Nodes (3): history(), history(), PriceRuleHistoryOut

### Community 218 - "rewards/http.py"
Cohesion: 0.18
Nodes (3): csv_response(), lead_filter(), period()

### Community 221 - "RedisKeyValueBuffer"
Cohesion: 0.18
Nodes (3): KeyValueBuffer, RedisKeyValueBuffer, test_redis_buffer_follows_the_worker_contract()

### Community 225 - "reward_public/service.py"
Cohesion: 0.12
Nodes (12): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicRewardPriceOut (+4 more)

### Community 226 - "get"
Cohesion: 0.08
Nodes (8): openapi(), swagger(), swagger_asset(), _swagger_page(), health(), available_months(), get(), service_options()

### Community 227 - "ItemsOut"
Cohesion: 0.13
Nodes (9): ad_units(), assign_sites(), delete(), index(), members(), show(), sites_of_member(), unlinked() (+1 more)

### Community 231 - "SiteListOut"
Cohesion: 0.17
Nodes (3): create(), site_options(), SiteListOut

### Community 242 - "RateLimited"
Cohesion: 0.11
Nodes (7): options, RateLimited, cors(), preflight(), receive(), KeyValueIn, receive_key_values()

### Community 245 - "test_key_values.py"
Cohesion: 0.11
Nodes (8): metrics(), exposition(), _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_the_preflight_answers_with_cors(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 248 - "AuthService"
Cohesion: 0.10
Nodes (4): accept(), get_invitation(), auth_service(), AuthService

### Community 250 - "networks/controller.py"
Cohesion: 0.11
Nodes (11): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+3 more)

### Community 256 - "GoalService"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+10 more)

### Community 266 - "invoices/controller.py"
Cohesion: 0.13
Nodes (13): create_service(), mine(), services(), update_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut (+5 more)

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2880 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **125 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `PageOut`, `GoalService`, `InvoiceService`, `DashboardService`, `AlertService`, `TaskQueue`, `ClientFacebookService`, `modules/google_ads/controller.py`, `company/controller.py`, `ContractService`, `invoices/controller.py`, `roles/controller.py`, `schedules/controller.py`, `GroupService`, `inventory/dto.py`, `FacebookService`, `.__init__`, `api_keys/controller.py`, `GamToolService`, `custom_metrics/controller.py`, `.__init__`, `staff/controller.py`, `modules/loaders/service.py`, `dashboard_templates/controller.py`, `LoaderService`, `avant_core_access_models`, `.uow`, `AdTagService`, `mfa/controller.py`, `ReportService`, `sites/controller.py`, `limits.py`, `reports/service.py`, `shared/dto.py`, `mcm/controller.py`, `.trusted_uow`, `auth/controller.py`, `modules/price_rules/controller.py`, `modules/ad_tags/dto.py`, `PriceRuleService`, `CommissionService`, `views/controller.py`, `commissions/service.py`, `client_notes/controller.py`, `profile/controller.py`, `modules/rewards/service.py`, `client_documents/controller.py`, `members/controller.py`, `checklist_items/controller.py`, `PublicPriceFloorService`, `modules/rewards/controller.py`, `account/controller.py`, `ClientLoaderService`, `pytest`, `SupportTaskService`, `AdTagOut`, `ports.py`, `.__init__`, `ClientPriceRuleService`, `costs/controller.py`, `internal/rewards/controller.py`, `mcm/service.py`, `GoogleService`, `ResultService`, `.__init__`, `checklists/controller.py`, `ClientRewardService`, `tasks/controller.py`, `reward_public/service.py`, `ClientDocumentService`, `PublicRewardService`, `.__init__`, `SiteService`, `AuthService`, `networks/controller.py`?**
  _High betweenness centrality (0.113) - this node is a cross-community bridge._
- **Are the 192 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 192 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PageOut` be split into smaller, more focused modules?**
  _Cohesion score 0.06859903381642513 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `GoalService`, `InvoiceService`, `roles/controller.py`, `DashboardService`, `AlertService`, `.of`, `modules/google_ads/controller.py`, `ClientFacebookService`, `ContractService`, `invoices/controller.py`, `schedules/controller.py`, `GroupService`, `inventory/dto.py`, `FacebookService`, `api_keys/controller.py`, `GamToolService`, `staff/controller.py`, `tasks`, `LoaderService`, `modules/loaders/service.py`, `router.py`, `avant_core_access_models`, `AdTagService`, `ReportService`, `forget_pages`, `sites/controller.py`, `.update`, `contracts/controller.py`, `shared/dto.py`, `mcm/controller.py`, `.trusted_uow`, `modules/price_rules/controller.py`, `PriceRuleService`, `modules/ad_tags/dto.py`, `reports/service.py`, `client_notes/controller.py`, `modules/rewards/service.py`, `members/controller.py`, `checklists`, `modules/rewards/controller.py`, `.of`, `ClientLoaderService`, `SupportTaskService`, `AdTagOut`, `ports.py`, `ClientPriceRuleService`, `costs/controller.py`, `internal/rewards/controller.py`, `mcm/service.py`, `checklists/controller.py`, `ClientRewardService`, `tasks/controller.py`, `ItemsOut`, `LoaderOut`, `SiteService`, `networks/controller.py`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Are the 93 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 93 INFERRED edges - model-reasoned connections that need verification._
- **Should `InvoiceService` be split into smaller, more focused modules?**
  _Cohesion score 0.08065458796025717 - nodes in this community are weakly interconnected._