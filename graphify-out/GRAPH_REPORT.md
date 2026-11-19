# Graph Report - avant-api  (2026-11-19)

## Corpus Check
- 402 files · ~134,245 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 5980 nodes · 16722 edges · 296 communities (138 shown, 158 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2602 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `13c27235`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- reward_public/controller.py
- InvoiceOut
- RoleService
- DashboardService
- AlertService
- _member_client
- PageOut
- ExportsBusy
- steps
- schedules/controller.py
- Avant: conexão com o GAM
- test_mfa.py
- AdTagOut
- GroupService
- inventory/dto.py
- .uow
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
- mfa/controller.py
- currencies/controller.py
- ReportService
- test_reward_public.py
- RewardIn
- session-start.sh
- avant-api
- test_price_rules.py
- ad_tag_public/dto.py
- Actor
- modules/price_rules/service.py
- TaskQueue
- ClientService
- auth/controller.py
- PriceRuleService
- AdTagUnitDayOut
- Services
- test_reports.py
- views/controller.py
- InvoiceService
- modules/facebook/controller.py
- client_notes/controller.py
- GamToolService
- modules/rewards/dto.py
- Avant: endpoints da API do MVP
- download
- members/controller.py
- test_api_keys.py
- checklist_items/controller.py
- RewardCache
- modules/rewards/controller.py
- account/controller.py
- export.py
- RedisRewardCache
- checklists/controller.py
- contracts
- ClientLoaderService
- ProfileService
- clean_code.py
- Limiter
- .of_detail
- ClientAdTagService
- avant-api
- tasks.py
- UnitOfWorkFactory
- pool_metrics.py
- FacebookService
- ClientPriceRuleService
- costs/controller.py
- shared/dto.py
- modules/ad_tags/dto.py
- test_events.py
- CascadeHourOut
- GoogleService
- AdUnitOut
- Avant: grupos na Empresa e imagem da Empresa
- RedisCounter
- Groone Avant: contexto do projeto
- documents/controller.py
- Actor
- ClientRewardService
- tasks/dto.py
- _csrf
- PublicRewardService
- dollars
- profiles
- updates
- download
- Avant: repositório e plano do MVP
- TaskQueue
- Avant: conexão com o GAM
- test_dashboards.py
- FiscalDataIn
- conftest.py
- test_mail_queue.py
- AdTagVersionOut
- contracts/dto.py
- commissions/controller.py
- get
- Settings
- Arquitetura do MVP do Avant
- CompanyService
- gam_tools/controller.py
- tasks/controller.py
- LoaderOut
- LoaderService
- test_invitation_mail.py
- .build
- test_company_image.py
- avant_core_access_models
- CapturingMailer
- image_response
- ContractService
- sites/controller.py
- mark
- create
- SiteService
- test_facebook.py
- reports/service.py
- people/controller.py
- main.py
- swagger_assets.py
- events/controller.py
- install
- audit/controller.py
- .upload
- GamToolNetworkOut
- PriceRuleDetailsOut
- PayeeDetailsOut
- receive
- alert_settings
- ContractClientRefOut
- BaseModel
- checklists
- limits.py
- _record
- gam_tools/dto.py
- mine
- test_metrics.py
- .run_guarded
- RedisEvents
- .health
- goals/controller.py
- .options
- client_documents/controller.py
- PriceRuleHourOut
- GoalService
- internal/rewards/controller.py
- mcm/service.py
- FakeFacebook
- objects
- floor_cache.py
- image
- gam_tools/service.py
- SyncRunOut
- health/controller.py
- _BrokenAuthService
- avant_core_shared_clock
- RewardAdUnitGroupOut
- ItemsOut
- .change
- SiteListOut
- DomainError
- ContractService
- RateLimited
- SupportTaskService
- test_account.py
- SiteOut
- networks/controller.py
- LoaderOptionOut
- test_ad_tags_and_loaders_panel
- goals/service.py
- GoalTemplateIn
- facebook/http.py
- SiteService
- role_goals
- test_templates_need_the_permission_and_the_groone_company
- get
- _contract_fields
- SiteDetailOut
- count_pool_timeout
- .start
- capped
- ads_txt
- ClientProfileIn
- _BrokenReleaseCounter

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 241 edges
2. `PageOut` - 213 edges
3. `_csrf()` - 197 edges
4. `get()` - 195 edges
5. `_onboard_owner()` - 191 edges
6. `Services` - 167 edges
7. `UnitOfWorkFactory` - 167 edges
8. `_staff()` - 92 edges
9. `page_out()` - 89 edges
10. `FacebookService` - 85 edges

## Surprising Connections (you probably didn't know these)
- `Onde está o trabalho` --references--> `PriceRuleSiteOut`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/price_rules/dto.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/modules/company/controller.py
- `Como funciona` --references--> `Services`  [INFERRED]
  README.md → src/avant_api/app/container.py
- `Estrutura` --references--> `Services`  [INFERRED]
  README.md → src/avant_api/app/container.py
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py

## Import Cycles
- None detected.

## Communities (296 total, 158 thin omitted)

### Community 0 - "reward_public/controller.py"
Cohesion: 0.14
Nodes (9): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body() (+1 more)

### Community 1 - "InvoiceOut"
Cohesion: 0.11
Nodes (5): add_item(), delete(), remove_item(), InvoiceOut, InvoiceService

### Community 2 - "RoleService"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "_member_client"
Cohesion: 0.07
Nodes (23): _membership_ids(), test_groups_lifecycle(), _assert_denied(), _queue(), test_cost_writes_need_permission(), test_member_writes_need_permission(), test_network_sync_and_disconnect_need_permission(), test_role_writes_need_permission() (+15 more)

### Community 6 - "PageOut"
Cohesion: 0.06
Nodes (18): alerts(), rule_decisions(), FacebookAlertOut, FacebookChangeOut, FacebookObjectDetailOut, FacebookObjectOut, FacebookRuleDecisionOut, accounts() (+10 more)

### Community 7 - "ExportsBusy"
Cohesion: 0.22
Nodes (4): ExportsBusy, export_slot(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 8 - "steps"
Cohesion: 0.07
Nodes (33): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, jobs (+25 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: conexão com o GAM"
Cohesion: 0.12
Nodes (16): Acesso, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), Identidade, MemberPermission, PasswordReset (+8 more)

### Community 11 - "test_mfa.py"
Cohesion: 0.18
Nodes (16): run_password_reset_tasks(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable() (+8 more)

### Community 12 - "AdTagOut"
Cohesion: 0.13
Nodes (4): forget_tag(), update(), AdTagIn, AdTagService

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+6 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.13
Nodes (7): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - ".uow"
Cohesion: 0.06
Nodes (7): accounts(), create(), duplicate(), update_account(), FacebookAccountIn, FacebookAccountOut, FacebookJobOut

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.06
Nodes (14): InvitationMailNotSent, invite(), options(), StaffInviteIn, StaffService, cancel(), create_invitation(), list_invitations() (+6 more)

### Community 18 - "security.py"
Cohesion: 0.05
Nodes (22): CsrfFailed, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company(), get_actor(), get_auth() (+14 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (11): check(), create(), delete(), index(), update(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn (+3 more)

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
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "modules/facebook/dto.py"
Cohesion: 0.06
Nodes (8): set_budget(), FacebookAccountRefOut, FacebookBudgetIn, FacebookBudgetOut, FacebookCountryOut, FacebookDailyOut, FacebookParentOut, FacebookTotalsOut

### Community 27 - "AdTagService"
Cohesion: 0.12
Nodes (11): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+3 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.07
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), verify(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "currencies/controller.py"
Cohesion: 0.15
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.05
Nodes (22): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+14 more)

### Community 31 - "test_reward_public.py"
Cohesion: 0.10
Nodes (23): reward_cache_key(), MemoryRewardBuffer, _buffer(), _cascade_reward(), test_events_and_leads_go_to_the_buffer(), test_icon_route_has_the_ip_limit(), test_price_rule_settings_forget_reward_page(), test_public_config_is_cached_and_cleared() (+15 more)

### Community 32 - "RewardIn"
Cohesion: 0.18
Nodes (3): create(), create(), RewardIn

### Community 36 - "test_price_rules.py"
Cohesion: 0.12
Nodes (27): FixedCountries, _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _offerwall_unit(), _present() (+19 more)

### Community 37 - "ad_tag_public/dto.py"
Cohesion: 0.06
Nodes (15): ad_tag_cache_key(), BucketRule, RewardBuffer, config(), page_views(), preflight(), public_ad_tag_service(), PageViewBlockIn (+7 more)

### Community 38 - "Actor"
Cohesion: 0.08
Nodes (10): changes(), disconnect(), edit(), job(), read_alert(), rule(), set_alert_settings(), set_rule() (+2 more)

### Community 39 - "modules/price_rules/service.py"
Cohesion: 0.22
Nodes (11): CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn, PriceRuleOut (+3 more)

### Community 40 - "TaskQueue"
Cohesion: 0.10
Nodes (9): confirm_network(), register_network(), reject_network(), unassigned_networks(), mcm_service(), ClientNetworkIn, McmCandidateOut, McmService (+1 more)

### Community 41 - "ClientService"
Cohesion: 0.05
Nodes (31): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), edit_client() (+23 more)

### Community 42 - "auth/controller.py"
Cohesion: 0.06
Nodes (15): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), AcceptInvitationIn (+7 more)

### Community 43 - "PriceRuleService"
Cohesion: 0.09
Nodes (15): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+7 more)

### Community 45 - "Services"
Cohesion: 0.03
Nodes (24): Services, SessionCookies, get_cookies(), get_services(), get_session_auth(), auth_service(), company_service(), cost_service() (+16 more)

### Community 46 - "test_reports.py"
Cohesion: 0.06
Nodes (57): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _csrf(), _onboard_owner(), _owner_invite() (+49 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "InvoiceService"
Cohesion: 0.13
Nodes (13): create_service(), services(), update_item(), update_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut (+5 more)

### Community 49 - "modules/facebook/controller.py"
Cohesion: 0.05
Nodes (13): set_status(), FacebookAdIn, FacebookAdsetIn, FacebookCardIn, FacebookDraftIn, FacebookEditIn, FacebookPickIn, FacebookAlertSettingOut (+5 more)

### Community 50 - "client_notes/controller.py"
Cohesion: 0.09
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 52 - "modules/rewards/dto.py"
Cohesion: 0.09
Nodes (12): RewardActiveIn, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO, RewardLeadOut (+4 more)

### Community 53 - "Avant: endpoints da API do MVP"
Cohesion: 0.15
Nodes (12): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+4 more)

### Community 54 - "download"
Cohesion: 0.18
Nodes (5): documents(), download(), upload(), document_service(), DocumentService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.20
Nodes (13): MemoryBucket, _bearer(), _create(), _exercise(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke() (+5 more)

### Community 57 - "checklist_items/controller.py"
Cohesion: 0.11
Nodes (9): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+1 more)

### Community 58 - "RewardCache"
Cohesion: 0.06
Nodes (9): CountryLookup, Bucket, is_cascade_shape(), safe_site_cascades(), site_cascades(), RewardCache, prices(), PublicPriceFloorsOut (+1 more)

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.07
Nodes (14): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+6 more)

### Community 60 - "account/controller.py"
Cohesion: 0.08
Nodes (14): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+6 more)

### Community 61 - "export.py"
Cohesion: 0.09
Nodes (13): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+5 more)

### Community 63 - "checklists/controller.py"
Cohesion: 0.24
Nodes (9): ChecklistDetailOut, ChecklistMarkIn, ChecklistMonthOut, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut (+1 more)

### Community 65 - "contracts"
Cohesion: 0.20
Nodes (5): contract(), contracts(), finish_contract(), new_contract(), remove_contract()

### Community 66 - "ClientLoaderService"
Cohesion: 0.13
Nodes (6): delete(), index(), options(), show(), update(), ClientLoaderService

### Community 67 - "ProfileService"
Cohesion: 0.08
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService, UserOut

### Community 68 - "clean_code.py"
Cohesion: 0.15
Nodes (7): check_file(), docstring_problems(), inline_comments(), is_exempt(), main(), single_letter_names(), source_files()

### Community 69 - "Limiter"
Cohesion: 0.09
Nodes (10): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter() (+2 more)

### Community 71 - "ClientAdTagService"
Cohesion: 0.10
Nodes (12): AdTagOut, create(), delete(), health(), index(), publish(), restore(), set_active() (+4 more)

### Community 74 - "tasks.py"
Cohesion: 0.13
Nodes (5): CeleryQueue, masked_args(), _CapturingCelery, test_password_reset_task_masks_the_email_in_the_message(), test_tasks_with_ids_only_are_not_masked()

### Community 76 - "pool_metrics.py"
Cohesion: 0.15
Nodes (7): _checked_in(), _checked_out(), _closed(), _opened(), watch_pool(), _sample(), test_pool_gauges_follow_checkout_and_close()

### Community 77 - "FacebookService"
Cohesion: 0.09
Nodes (9): FacebookNotConfigured, people(), set_person(), upload_media(), facebook_service(), FacebookMediaOut, FacebookPersonIn, FacebookPersonOut (+1 more)

### Community 78 - "ClientPriceRuleService"
Cohesion: 0.12
Nodes (13): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+5 more)

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 81 - "shared/dto.py"
Cohesion: 0.08
Nodes (4): ClientProfileOut, FiscalDataOut, image_url(), RoleRefOut

### Community 82 - "modules/ad_tags/dto.py"
Cohesion: 0.08
Nodes (9): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagDraftIO, AdTagHealthDayOut, AdTagLiveOut, AdTagSettingsIO (+1 more)

### Community 83 - "test_events.py"
Cohesion: 0.14
Nodes (14): channel(), _parse(), sse(), _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot() (+6 more)

### Community 85 - "GoogleService"
Cohesion: 0.03
Nodes (26): _google(), CompanyChanged, FacebookMediaTooLarge, GoogleFailed, GoogleUnavailable, NoActiveCompany, challenge(), _claims() (+18 more)

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.12
Nodes (14): Company, Empresa e equipe, Invitation, Membership, Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Imagem da Empresa (+6 more)

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (15): Arquitetura, Como trabalhar nos repositórios, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação (+7 more)

### Community 91 - "documents/controller.py"
Cohesion: 0.19
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 96 - "_csrf"
Cohesion: 0.07
Nodes (33): _admin_role(), NextMonthClock, test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions(), test_groone_role_with_the_whole_catalog(), test_manager_change_preview() (+25 more)

### Community 97 - "PublicRewardService"
Cohesion: 0.09
Nodes (14): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicRewardPriceOut (+6 more)

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
Cohesion: 0.11
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskMailQueue, TaskQueue

### Community 131 - "Avant: conexão com o GAM"
Cohesion: 0.11
Nodes (16): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment, Avant: conexão com o GAM, Caminho conta de serviço (+8 more)

### Community 132 - "test_dashboards.py"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 133 - "FiscalDataIn"
Cohesion: 0.13
Nodes (5): edit_fiscal(), edit_image(), fiscal(), CompanyFiscalOut, FiscalDataIn

### Community 134 - "conftest.py"
Cohesion: 0.04
Nodes (31): browser(), refresh_levels(), _error_code(), test_cookies_are_always_secure_with_the_host_prefix(), test_every_write_route_refuses_another_site(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews() (+23 more)

### Community 135 - "test_mail_queue.py"
Cohesion: 0.05
Nodes (13): MemoryCounter, MemoryRewardCache, NoEvents, RecordingQueue, _SpyCounter, _account(), _NoDatabase, _NoMail (+5 more)

### Community 137 - "contracts/dto.py"
Cohesion: 0.16
Nodes (7): contract_networks(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractSummaryOut, _network_ref(), ContractClientRefOut

### Community 138 - "commissions/controller.py"
Cohesion: 0.06
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 139 - "get"
Cohesion: 0.15
Nodes (4): openapi(), swagger(), swagger_asset(), _swagger_page()

### Community 142 - "Settings"
Cohesion: 0.04
Nodes (32): engine_settings(), _mailer(), restricted_engine(), _are_proxy_addresses(), invalid_variable_names(), InvalidVariables, _is_smtp_url(), load_settings() (+24 more)

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.14
Nodes (13): Ambientes, deploy e backup, Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões (+5 more)

### Community 144 - "CompanyService"
Cohesion: 0.17
Nodes (5): remove_image(), show(), CompanyDetailOut, CompanyPatchIn, CompanyService

### Community 145 - "gam_tools/controller.py"
Cohesion: 0.19
Nodes (6): install(), network(), networks(), run(), runs(), GamToolRunOut

### Community 146 - "tasks/controller.py"
Cohesion: 0.22
Nodes (4): change(), comment(), create(), task()

### Community 148 - "LoaderService"
Cohesion: 0.12
Nodes (9): create(), delete(), index(), show(), update(), loader_service(), LoaderIn, LoaderOut (+1 more)

### Community 149 - "test_invitation_mail.py"
Cohesion: 0.24
Nodes (10): _assert_mail_not_sent(), _client_with_owner_invitation(), _invite(), _owner_invitation_emails(), _pending_emails(), test_invite_answers_503_when_the_mail_fails(), test_owner_invitation_answers_503_when_the_mail_fails(), test_owner_invitation_resend_answers_503_when_the_mail_fails() (+2 more)

### Community 150 - ".build"
Cohesion: 0.05
Nodes (12): _facebook(), GeoLiteCountries, NoCountries, EventSource, StreamLimiter, RedisKeyValueBuffer, RedisBucket, RedisRewardBuffer (+4 more)

### Community 152 - "test_company_image.py"
Cohesion: 0.08
Nodes (20): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, _after_first_segment(), _jpeg(), _png(), _put_image() (+12 more)

### Community 153 - "avant_core_access_models"
Cohesion: 0.07
Nodes (8): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, default_period(), ResultService

### Community 155 - "CapturingMailer"
Cohesion: 0.12
Nodes (20): CapturingMailer, mailer(), Sent, _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client() (+12 more)

### Community 161 - "sites/controller.py"
Cohesion: 0.19
Nodes (6): site_service(), AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 162 - "mark"
Cohesion: 0.13
Nodes (7): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), months()

### Community 165 - "test_facebook.py"
Cohesion: 0.20
Nodes (9): _configure(), _connect(), _draft(), _services(), _sync(), test_facebook_control_and_rules(), test_facebook_create_edit_duplicate_lists_and_media(), test_facebook_panel() (+1 more)

### Community 166 - "reports/service.py"
Cohesion: 0.05
Nodes (18): catalog(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut (+10 more)

### Community 167 - "people/controller.py"
Cohesion: 0.11
Nodes (9): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+1 more)

### Community 168 - "main.py"
Cohesion: 0.20
Nodes (3): _content_security_policy(), observe(), _route_template()

### Community 171 - "swagger_assets.py"
Cohesion: 0.15
Nodes (5): ExpectedAsset, load_assets(), SwaggerAsset, SwaggerAssetChanged, test_changed_asset_stops_the_start()

### Community 172 - "events/controller.py"
Cohesion: 0.14
Nodes (3): TooManyAttempts, events(), test_stream_limiter_caps_each_person_and_the_process()

### Community 174 - "install"
Cohesion: 0.18
Nodes (10): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), _limit_details() (+2 more)

### Community 175 - "audit/controller.py"
Cohesion: 0.17
Nodes (3): index(), audit_service(), AuditService

### Community 177 - "GamToolNetworkOut"
Cohesion: 0.18
Nodes (4): GamToolClientOut, GamToolNetworkDetailOut, GamToolNetworkOut, GamToolSiteOut

### Community 178 - "PriceRuleDetailsOut"
Cohesion: 0.09
Nodes (3): PriceRuleDetailsOut, forget_rule(), stored_drop_tiers()

### Community 180 - "receive"
Cohesion: 0.16
Nodes (9): POSTGRES_PASSWORD, env, image, options, ports, postgres, cors(), preflight() (+1 more)

### Community 183 - "ContractClientRefOut"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 184 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 188 - "_record"
Cohesion: 0.17
Nodes (5): configure_logging(), JsonFormatter, _record(), test_log_keeps_ordinary_messages(), test_log_masks_database_values_in_message_and_stack()

### Community 191 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 192 - "test_metrics.py"
Cohesion: 0.18
Nodes (4): metrics(), exposition(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 195 - "RedisEvents"
Cohesion: 0.31
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 197 - "goals/controller.py"
Cohesion: 0.21
Nodes (4): delete_template(), set_role_goal(), templates(), update_template()

### Community 198 - ".options"
Cohesion: 0.16
Nodes (3): options(), FacebookOptionOut, _CachedOptions

### Community 201 - "client_documents/controller.py"
Cohesion: 0.26
Nodes (5): client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 204 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 210 - "internal/rewards/controller.py"
Cohesion: 0.08
Nodes (13): delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active(), set_icon() (+5 more)

### Community 214 - "floor_cache.py"
Cohesion: 0.23
Nodes (3): forget_cascades(), forget_floors(), forget_site()

### Community 227 - "ItemsOut"
Cohesion: 0.15
Nodes (8): assign_sites(), classify(), classify_many(), link(), show(), site_options(), unlinked(), ItemsOut

### Community 231 - "SiteListOut"
Cohesion: 0.15
Nodes (3): create(), index(), SiteListOut

### Community 233 - "DomainError"
Cohesion: 0.14
Nodes (5): FacebookDenied, FacebookStateInvalid, oauth_callback(), oauth_start(), FacebookRedirects

### Community 240 - "ContractService"
Cohesion: 0.19
Nodes (4): edit_contract(), contract_service(), ContractPatchIn, ContractService

### Community 242 - "RateLimited"
Cohesion: 0.10
Nodes (4): RateLimited, KeyValueBuffer, KeyValueIn, receive_key_values()

### Community 243 - "SupportTaskService"
Cohesion: 0.15
Nodes (4): tasks(), support_task_service(), TaskOut, SupportTaskService

### Community 245 - "test_account.py"
Cohesion: 0.12
Nodes (12): MemoryKeyValueBuffer, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited() (+4 more)

### Community 247 - "SiteOut"
Cohesion: 0.13
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 250 - "networks/controller.py"
Cohesion: 0.11
Nodes (12): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+4 more)

### Community 253 - "test_ad_tags_and_loaders_panel"
Cohesion: 0.33
Nodes (5): _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back()

### Community 256 - "GoalTemplateIn"
Cohesion: 0.16
Nodes (4): create_template(), template_options(), GoalTemplateIn, GoalTemplateOut

### Community 265 - "test_templates_need_the_permission_and_the_groone_company"
Cohesion: 0.38
Nodes (3): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company()

### Community 266 - "get"
Cohesion: 0.08
Nodes (13): health(), available_months(), create(), delete_service(), get(), issue(), mine(), pay() (+5 more)

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2726 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **158 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `InvoiceOut`, `TaskQueue`, `DashboardService`, `AlertService`, `RoleService`, `PageOut`, `SiteService`, `contracts/dto.py`, `commissions/controller.py`, `schedules/controller.py`, `AdTagOut`, `GroupService`, `inventory/dto.py`, `.uow`, `.__init__`, `api_keys/controller.py`, `CompanyService`, `custom_metrics/controller.py`, `.__init__`, `InvitationOut`, `LoaderService`, `dashboard_templates/controller.py`, `avant_core_access_models`, `mfa/controller.py`, `currencies/controller.py`, `ReportService`, `sites/controller.py`, `ad_tag_public/dto.py`, `reports/service.py`, `people/controller.py`, `TaskQueue`, `ClientService`, `auth/controller.py`, `modules/price_rules/service.py`, `PriceRuleService`, `audit/controller.py`, `InvoiceService`, `modules/facebook/controller.py`, `client_notes/controller.py`, `GamToolService`, `views/controller.py`, `modules/rewards/dto.py`, `download`, `members/controller.py`, `checklist_items/controller.py`, `RewardCache`, `modules/rewards/controller.py`, `account/controller.py`, `checklists/controller.py`, `ClientLoaderService`, `ProfileService`, `Limiter`, `ClientAdTagService`, `client_documents/controller.py`, `GoalService`, `ClientPriceRuleService`, `costs/controller.py`, `mcm/service.py`, `GoogleService`, `gam_tools/service.py`, `documents/controller.py`, `.__init__`, `Actor`, `.__init__`, `ClientRewardService`, `tasks/dto.py`, `avant_core_shared_clock`, `PublicRewardService`, `.__init__`, `ContractService`, `SupportTaskService`, `networks/controller.py`, `goals/service.py`?**
  _High betweenness centrality (0.107) - this node is a cross-community bridge._
- **Are the 177 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 177 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `reward_public/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.14245014245014245 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `InvoiceOut`, `RoleService`, `DashboardService`, `AlertService`, `SiteService`, `contracts/dto.py`, `get`, `schedules/controller.py`, `AdTagOut`, `GroupService`, `inventory/dto.py`, `.uow`, `api_keys/controller.py`, `gam_tools/controller.py`, `security.py`, `InvitationOut`, `tasks/controller.py`, `LoaderService`, `clients`, `avant_core_access_models`, `AdTagService`, `ReportService`, `ContractService`, `sites/controller.py`, `Actor`, `people/controller.py`, `TaskQueue`, `ClientService`, `modules/price_rules/service.py`, `PriceRuleService`, `reports/service.py`, `Services`, `audit/controller.py`, `InvoiceService`, `modules/facebook/controller.py`, `client_notes/controller.py`, `GamToolService`, `PriceRuleDetailsOut`, `modules/rewards/dto.py`, `members/controller.py`, `checklists`, `modules/rewards/controller.py`, `checklists/controller.py`, `contracts`, `ClientLoaderService`, `goals/controller.py`, `ClientAdTagService`, `GoalService`, `ClientPriceRuleService`, `costs/controller.py`, `shared/dto.py`, `internal/rewards/controller.py`, `mcm/service.py`, `objects`, `AdUnitOut`, `gam_tools/service.py`, `Actor`, `ClientRewardService`, `tasks/dto.py`, `avant_core_shared_clock`, `ItemsOut`, `SiteListOut`, `ContractService`, `SupportTaskService`, `networks/controller.py`, `goals/service.py`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `InvoiceOut` be split into smaller, more focused modules?**
  _Cohesion score 0.10676532769556026 - nodes in this community are weakly interconnected._