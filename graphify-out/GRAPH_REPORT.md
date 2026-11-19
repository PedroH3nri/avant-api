# Graph Report - avant-api  (2026-11-19)

## Corpus Check
- 400 files · ~131,928 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 5860 nodes · 16446 edges · 266 communities (141 shown, 125 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2567 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `aa741ce2`
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
- uuid
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
- test_ad_tags.py
- dashboard_templates/controller.py
- invoice_pdf.py
- clients
- modules/facebook/dto.py
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
- modules/facebook/controller.py
- modules/price_rules/dto.py
- TaskQueue
- ClientService
- auth/controller.py
- PriceRuleService
- modules/ad_tags/dto.py
- Services
- test_reports.py
- views/controller.py
- InvoiceService
- pydantic
- client_notes/controller.py
- GamToolService
- modules/rewards/dto.py
- Avant: endpoints da API do MVP
- download
- members/controller.py
- test_api_keys.py
- checklist_items/controller.py
- Bucket
- modules/rewards/controller.py
- account/controller.py
- to_xlsx
- RedisRewardCache
- checklists/controller.py
- SessionCookies
- contracts
- ClientLoaderService
- ProfileService
- clean_code.py
- Limiter
- .of_detail
- ClientAdTagService
- FakeFacebook
- avant-api
- tasks.py
- UnitOfWorkFactory
- pool_metrics.py
- test_hardening.py
- ClientPriceRuleService
- costs/controller.py
- .of
- test_events.py
- CascadeHourOut
- GoogleService
- AdUnitOut
- Avant: grupos na Empresa e imagem da Empresa
- RedisCounter
- Groone Avant: contexto do projeto
- documents/controller.py
- time
- tasks/dto.py
- _csrf
- PublicRewardService
- dollars
- FacebookProfileOut
- updates
- client_documents/controller.py
- Avant: repositório e plano do MVP
- events.py
- Avant: conexão com o GAM
- test_dashboards.py
- company/controller.py
- datetime
- conftest.py
- contracts/controller.py
- commissions/controller.py
- get
- Settings
- Arquitetura do MVP do Avant
- CompanyService
- GoalService
- tasks/controller.py
- LoaderOut
- LoaderService
- test_invitation_mail.py
- .build
- test_company_image.py
- modules/results/controller.py
- CapturingMailer
- shared/http.py
- ContractService
- sites/controller.py
- mark
- create
- SiteService
- test_facebook.py
- reports/service.py
- people/controller.py
- main.py
- FacebookRuleOut
- events/controller.py
- DashboardTemplateOut
- audit/controller.py
- document_response
- LoaderIn
- PriceRuleConfigIn
- PayeeDetailsOut
- postgres
- FacebookAlertSettingOut
- ContractClientRefOut
- BaseModel
- checklists
- MemoryBucket
- _record
- edit_image
- ReportQueryIn
- mine
- account_service
- .run_guarded
- RedisEvents
- goals/controller.py
- RedisKeyValueBuffer
- .of
- PriceRuleHourOut
- team
- internal/rewards/controller.py
- StreamLimiter
- .classify
- .page_saved
- floor_cache.py
- image
- health/controller.py
- _BrokenAuthService
- internal/rewards/controller.py
- ItemsOut
- .change
- DomainError
- RateLimited
- test_account.py
- SiteOut
- networks/controller.py
- goals/service.py
- GoalTemplateIn
- staff/controller.py
- create
- _contract_fields

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 240 edges
2. `PageOut` - 213 edges
3. `_csrf()` - 196 edges
4. `get()` - 193 edges
5. `_onboard_owner()` - 190 edges
6. `UnitOfWorkFactory` - 167 edges
7. `Services` - 167 edges
8. `_staff()` - 92 edges
9. `page_out()` - 89 edges
10. `ReportService` - 79 edges

## Surprising Connections (you probably didn't know these)
- `Onde está o trabalho` --references--> `PriceRuleSiteOut`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/price_rules/dto.py
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/modules/company/controller.py
- `Como funciona` --references--> `TaskMailQueue`  [INFERRED]
  README.md → src/avant_api/app/mail_queue.py
- `Estrutura` --references--> `TaskQueue`  [INFERRED]
  README.md → src/avant_api/app/tasks.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/modules/company/controller.py

## Import Cycles
- None detected.

## Communities (266 total, 125 thin omitted)

### Community 0 - "reward_public/controller.py"
Cohesion: 0.11
Nodes (11): config(), page_views(), preflight(), client_address(), cors(), events(), icon(), leads() (+3 more)

### Community 1 - "InvoiceOut"
Cohesion: 0.09
Nodes (9): add_item(), delete(), delete_service(), issue(), pay(), remove_item(), update_item(), InvoiceOut (+1 more)

### Community 2 - "RoleService"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.06
Nodes (24): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+16 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "_member_client"
Cohesion: 0.08
Nodes (20): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client() (+12 more)

### Community 6 - "PageOut"
Cohesion: 0.07
Nodes (15): FacebookAlertOut, FacebookChangeOut, FacebookObjectDetailOut, FacebookObjectOut, FacebookRuleDecisionOut, object_filter(), period(), accounts() (+7 more)

### Community 7 - "uuid"
Cohesion: 0.10
Nodes (24): ExportsBusy, to_csv(), test_busy_export_answers_503_with_retry_after(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run(), _result(), test_compare_header_follows_the_mode(), test_csv_header_escapes_formulas() (+16 more)

### Community 8 - "steps"
Cohesion: 0.07
Nodes (33): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, jobs (+25 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: conexão com o GAM"
Cohesion: 0.10
Nodes (20): Acesso, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade (+12 more)

### Community 11 - "test_mfa.py"
Cohesion: 0.16
Nodes (16): run_password_reset_tasks(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable() (+8 more)

### Community 12 - "AdTagOut"
Cohesion: 0.13
Nodes (3): forget_tag(), create(), AdTagOut

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.09
Nodes (8): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - ".uow"
Cohesion: 0.08
Nodes (4): people(), set_person(), FacebookPersonIn, FacebookPersonOut

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.08
Nodes (10): InvitationMailNotSent, cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService (+2 more)

### Community 18 - "security.py"
Cohesion: 0.07
Nodes (22): CompanyChanged, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor() (+14 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "test_ad_tags.py"
Cohesion: 0.07
Nodes (22): _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status() (+14 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "modules/facebook/dto.py"
Cohesion: 0.06
Nodes (10): set_budget(), FacebookAccountRefOut, FacebookBudgetIn, FacebookBudgetOut, FacebookCountryOut, FacebookDailyOut, FacebookParentOut, FacebookTotalsOut (+2 more)

### Community 27 - "AdTagService"
Cohesion: 0.12
Nodes (12): delete(), health(), index(), publish(), restore(), set_active(), show(), units() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.07
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), verify(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "currencies/controller.py"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.05
Nodes (18): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned() (+10 more)

### Community 31 - "test_reward_public.py"
Cohesion: 0.09
Nodes (28): reward_cache_key(), browser(), _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), test_upload_without_session_is_refused_before_reading_the_body(), _buffer() (+20 more)

### Community 32 - "RewardOut"
Cohesion: 0.09
Nodes (4): create(), update(), RewardIn, RewardOut

### Community 36 - "test_price_rules.py"
Cohesion: 0.12
Nodes (27): FixedCountries, _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _offerwall_unit(), _present() (+19 more)

### Community 37 - "ad_tag_public/dto.py"
Cohesion: 0.08
Nodes (9): BucketRule, PageViewBlockIn, PageViewIn, PublicAdTagOut, PublicBlockOut, PublicLoaderOut, PublicMgidOut, PublicTagOut (+1 more)

### Community 38 - "modules/facebook/controller.py"
Cohesion: 0.06
Nodes (22): accounts(), alert_settings(), alerts(), changes(), disconnect(), objects(), profiles(), read_alert() (+14 more)

### Community 39 - "modules/price_rules/dto.py"
Cohesion: 0.10
Nodes (6): CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigOut, PriceRuleOut, PriceRuleSiteSummaryOut

### Community 40 - "TaskQueue"
Cohesion: 0.05
Nodes (12): TaskMailQueue, TaskQueue, confirm_network(), register_network(), reject_network(), unassigned_networks(), mcm_service(), ClientNetworkIn (+4 more)

### Community 41 - "ClientService"
Cohesion: 0.05
Nodes (32): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), edit_client() (+24 more)

### Community 42 - "auth/controller.py"
Cohesion: 0.06
Nodes (17): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+9 more)

### Community 43 - "PriceRuleService"
Cohesion: 0.08
Nodes (16): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+8 more)

### Community 44 - "modules/ad_tags/dto.py"
Cohesion: 0.17
Nodes (13): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagHealthDayOut, AdTagHealthOut, AdTagIn, AdTagLiveOut (+5 more)

### Community 45 - "Services"
Cohesion: 0.03
Nodes (27): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, Services, get_services(), public_ad_tag_service() (+19 more)

### Community 46 - "test_reports.py"
Cohesion: 0.08
Nodes (25): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _checked_out(), _checkouts(), PoolWatchingEvents (+17 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "InvoiceService"
Cohesion: 0.10
Nodes (15): create_service(), mine(), return_to_draft(), service_options(), services(), update_service(), AvailableMonthOut, InvoiceItemOut (+7 more)

### Community 49 - "pydantic"
Cohesion: 0.18
Nodes (12): PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicRewardPriceOut, PublicStyleOut (+4 more)

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "GamToolService"
Cohesion: 0.05
Nodes (19): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+11 more)

### Community 52 - "modules/rewards/dto.py"
Cohesion: 0.08
Nodes (13): RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO (+5 more)

### Community 53 - "Avant: endpoints da API do MVP"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+6 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.30
Nodes (9): _bearer(), _create(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit() (+1 more)

### Community 57 - "checklist_items/controller.py"
Cohesion: 0.11
Nodes (9): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+1 more)

### Community 58 - "Bucket"
Cohesion: 0.13
Nodes (5): CountryLookup, Bucket, prices(), PublicPriceFloorsOut, PublicPriceFloorService

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.10
Nodes (14): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+6 more)

### Community 60 - "account/controller.py"
Cohesion: 0.07
Nodes (12): get_session_auth(), delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ForgotPasswordIn (+4 more)

### Community 61 - "to_xlsx"
Cohesion: 0.14
Nodes (6): _csv_cell(), _header(), _metric_label(), _rows(), to_xlsx(), _xlsx_cell()

### Community 62 - "RedisRewardCache"
Cohesion: 0.16
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "checklists/controller.py"
Cohesion: 0.14
Nodes (12): checklist(), site_checklist_service(), ChecklistDetailOut, ChecklistMarkIn, ChecklistMonthOut, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut (+4 more)

### Community 65 - "contracts"
Cohesion: 0.14
Nodes (6): contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract()

### Community 66 - "ClientLoaderService"
Cohesion: 0.13
Nodes (6): delete(), index(), options(), show(), update(), ClientLoaderService

### Community 67 - "ProfileService"
Cohesion: 0.07
Nodes (7): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService

### Community 68 - "clean_code.py"
Cohesion: 0.14
Nodes (7): check_file(), docstring_problems(), inline_comments(), is_exempt(), main(), single_letter_names(), source_files()

### Community 69 - "Limiter"
Cohesion: 0.08
Nodes (11): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+3 more)

### Community 70 - ".of_detail"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 71 - "ClientAdTagService"
Cohesion: 0.12
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 74 - "tasks.py"
Cohesion: 0.15
Nodes (5): CeleryQueue, masked_args(), _CapturingCelery, test_password_reset_task_masks_the_email_in_the_message(), test_tasks_with_ids_only_are_not_masked()

### Community 75 - "UnitOfWorkFactory"
Cohesion: 0.04
Nodes (9): ad_tag_cache_key(), UnitOfWorkFactory, is_cascade_shape(), safe_site_cascades(), site_cascades(), RewardCache, forget_tags(), default_period() (+1 more)

### Community 76 - "pool_metrics.py"
Cohesion: 0.05
Nodes (22): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), _limit_details() (+14 more)

### Community 77 - "test_hardening.py"
Cohesion: 0.18
Nodes (11): _rendered(), test_api_key_never_reaches_the_log(), test_docs_only_for_the_groone_session_with_2fa(), test_every_response_has_the_content_security_policy(), test_every_response_has_the_security_headers(), test_invalid_bearer_is_limited_per_ip_before_the_database(), counting(), test_old_docs_paths_do_not_exist() (+3 more)

### Community 78 - "ClientPriceRuleService"
Cohesion: 0.08
Nodes (17): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+9 more)

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 83 - "test_events.py"
Cohesion: 0.27
Nodes (11): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_events_route_refuses_above_the_cap(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports() (+3 more)

### Community 85 - "GoogleService"
Cohesion: 0.05
Nodes (11): GoogleUnavailable, GoogleAuth, new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), GoogleStatusOut (+3 more)

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "RedisCounter"
Cohesion: 0.14
Nodes (3): RedisCounter, test_redis_decr_without_key_creates_nothing(), test_redis_down_is_a_503_not_a_500()

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (15): Arquitetura, Como trabalhar nos repositórios, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação (+7 more)

### Community 91 - "documents/controller.py"
Cohesion: 0.15
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 94 - "time"
Cohesion: 0.11
Nodes (6): GoogleFailed, _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, test_id_token_claims()

### Community 95 - "tasks/dto.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 96 - "_csrf"
Cohesion: 0.07
Nodes (38): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+30 more)

### Community 97 - "PublicRewardService"
Cohesion: 0.10
Nodes (4): public_reward_service(), CachedPage, public_control_percent(), PublicRewardService

### Community 127 - "updates"
Cohesion: 0.11
Nodes (17): patterns, patterns, update-types, acoes, dependencias, imagens, dependency-name, patterns (+9 more)

### Community 128 - "client_documents/controller.py"
Cohesion: 0.17
Nodes (8): approve(), documents(), download(), reject(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.22
Nodes (8): Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11), Resumo, Serviços e ferramentas

### Community 130 - "events.py"
Cohesion: 0.18
Nodes (4): channel(), EventSource, _parse(), sse()

### Community 131 - "Avant: conexão com o GAM"
Cohesion: 0.11
Nodes (16): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment, Avant: conexão com o GAM, Caminho conta de serviço (+8 more)

### Community 132 - "test_dashboards.py"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 133 - "company/controller.py"
Cohesion: 0.20
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 134 - "datetime"
Cohesion: 0.10
Nodes (13): refresh_levels(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query(), _assert_denied(), _queue() (+5 more)

### Community 135 - "conftest.py"
Cohesion: 0.03
Nodes (22): ChangePasswordIn, client(), engine(), mailer(), memory_services(), MemoryCounter, MemoryKeyValueBuffer, MemoryRewardBuffer (+14 more)

### Community 137 - "contracts/controller.py"
Cohesion: 0.32
Nodes (5): ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut

### Community 138 - "commissions/controller.py"
Cohesion: 0.07
Nodes (22): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+14 more)

### Community 139 - "get"
Cohesion: 0.09
Nodes (9): openapi(), swagger(), swagger_asset(), _swagger_page(), health(), available_months(), get(), pdf() (+1 more)

### Community 142 - "Settings"
Cohesion: 0.05
Nodes (27): engine_settings(), _mailer(), restricted_engine(), _are_proxy_addresses(), invalid_variable_names(), InvalidVariables, _is_smtp_url(), load_settings() (+19 more)

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.14
Nodes (13): Ambientes, deploy e backup, Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões (+5 more)

### Community 144 - "CompanyService"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 145 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 146 - "tasks/controller.py"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 147 - "LoaderOut"
Cohesion: 0.17
Nodes (4): index(), LoaderClientOut, LoaderOut, LoaderTagOut

### Community 148 - "LoaderService"
Cohesion: 0.13
Nodes (8): create(), delete(), options(), show(), update(), loader_service(), LoaderOptionOut, LoaderService

### Community 149 - "test_invitation_mail.py"
Cohesion: 0.24
Nodes (10): _assert_mail_not_sent(), _client_with_owner_invitation(), _invite(), _owner_invitation_emails(), _pending_emails(), test_invite_answers_503_when_the_mail_fails(), test_owner_invitation_answers_503_when_the_mail_fails(), test_owner_invitation_resend_answers_503_when_the_mail_fails() (+2 more)

### Community 150 - ".build"
Cohesion: 0.06
Nodes (7): _facebook(), _google(), GeoLiteCountries, NoCountries, RedisBucket, RedisRewardBuffer, RewardBuffer

### Community 152 - "test_company_image.py"
Cohesion: 0.05
Nodes (23): challenge(), _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, ExpectedAsset, load_assets(), SwaggerAsset (+15 more)

### Community 153 - "modules/results/controller.py"
Cohesion: 0.13
Nodes (4): show(), result_service(), ResultsOut, ResultService

### Community 155 - "CapturingMailer"
Cohesion: 0.10
Nodes (33): CapturingMailer, Sent, _error_code(), _onboard_owner(), _owner_invite(), test_cookies_are_always_secure_with_the_host_prefix(), test_csrf_is_required_for_writes(), test_every_write_route_refuses_another_site() (+25 more)

### Community 158 - "shared/http.py"
Cohesion: 0.13
Nodes (4): get_auth(), client_info(), image_response(), image_upload()

### Community 160 - "ContractService"
Cohesion: 0.19
Nodes (4): O que já tem, contract(), ContractOut, ContractService

### Community 161 - "sites/controller.py"
Cohesion: 0.20
Nodes (9): create(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn (+1 more)

### Community 162 - "mark"
Cohesion: 0.14
Nodes (6): add_note(), check(), delete_note(), edit_note(), mark(), summary()

### Community 164 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 165 - "test_facebook.py"
Cohesion: 0.25
Nodes (7): _configure(), _connect(), _services(), _sync(), test_facebook_control_and_rules(), test_facebook_panel(), test_without_the_meta_app_the_login_is_unavailable()

### Community 166 - "reports/service.py"
Cohesion: 0.04
Nodes (18): catalog(), CustomCatalogMetricOut, dimension_text(), DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn (+10 more)

### Community 167 - "people/controller.py"
Cohesion: 0.08
Nodes (11): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+3 more)

### Community 168 - "main.py"
Cohesion: 0.11
Nodes (6): _content_security_policy(), observe(), _route_template(), check_fetch_site(), create_app(), results()

### Community 171 - "FacebookRuleOut"
Cohesion: 0.16
Nodes (3): FacebookRuleIn, FacebookRuleOut, rule()

### Community 172 - "events/controller.py"
Cohesion: 0.17
Nodes (3): events(), event_service(), EventService

### Community 174 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 175 - "audit/controller.py"
Cohesion: 0.12
Nodes (4): index(), audit_service(), AuditService, AuditOut

### Community 179 - "PayeeDetailsOut"
Cohesion: 0.21
Nodes (3): payment_details(), save_payment_details(), PayeeDetailsOut

### Community 180 - "postgres"
Cohesion: 0.33
Nodes (6): POSTGRES_PASSWORD, env, image, options, ports, postgres

### Community 183 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 184 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 186 - "MemoryBucket"
Cohesion: 0.20
Nodes (5): BucketResult, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 188 - "_record"
Cohesion: 0.17
Nodes (5): configure_logging(), JsonFormatter, _record(), test_log_keeps_ordinary_messages(), test_log_masks_database_values_in_message_and_stack()

### Community 191 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 197 - "goals/controller.py"
Cohesion: 0.18
Nodes (5): delete_template(), role_goals(), set_role_goal(), update_template(), RoleGoalIn

### Community 198 - "RedisKeyValueBuffer"
Cohesion: 0.15
Nodes (3): KeyValueBuffer, RedisKeyValueBuffer, test_redis_buffer_follows_the_worker_contract()

### Community 204 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 210 - "internal/rewards/controller.py"
Cohesion: 0.07
Nodes (11): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+3 more)

### Community 214 - "floor_cache.py"
Cohesion: 0.22
Nodes (4): forget_cascades(), forget_floors(), forget_rule(), forget_site()

### Community 223 - "health/controller.py"
Cohesion: 0.14
Nodes (4): metrics(), ready(), health_service(), HealthService

### Community 225 - "internal/rewards/controller.py"
Cohesion: 0.12
Nodes (4): client_reward_service(), forget_pages(), lead_filter(), period()

### Community 227 - "ItemsOut"
Cohesion: 0.12
Nodes (9): ad_units(), assign_sites(), delete(), index(), show(), site_options(), sites_of_member(), unlinked() (+1 more)

### Community 233 - "DomainError"
Cohesion: 0.08
Nodes (6): FacebookDenied, FacebookNotConfigured, FacebookStateInvalid, oauth_callback(), oauth_start(), FacebookRedirects

### Community 242 - "RateLimited"
Cohesion: 0.10
Nodes (6): RateLimited, cors(), preflight(), receive(), KeyValueIn, receive_key_values()

### Community 245 - "test_account.py"
Cohesion: 0.13
Nodes (12): _BrokenReleaseCounter, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited() (+4 more)

### Community 247 - "SiteOut"
Cohesion: 0.10
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 250 - "networks/controller.py"
Cohesion: 0.08
Nodes (14): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+6 more)

### Community 265 - "staff/controller.py"
Cohesion: 0.11
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2662 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **125 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `client_documents/controller.py`, `InvoiceOut`, `RoleService`, `DashboardService`, `AlertService`, `company/controller.py`, `PageOut`, `conftest.py`, `.__init__`, `contracts/controller.py`, `commissions/controller.py`, `staff/controller.py`, `schedules/controller.py`, `GroupService`, `inventory/dto.py`, `.uow`, `api_keys/controller.py`, `CompanyService`, `GoalService`, `custom_metrics/controller.py`, `.__init__`, `security.py`, `InvitationOut`, `dashboard_templates/controller.py`, `LoaderService`, `modules/results/controller.py`, `AdTagService`, `mfa/controller.py`, `currencies/controller.py`, `ReportService`, `ContractService`, `sites/controller.py`, `SiteService`, `ad_tag_public/dto.py`, `reports/service.py`, `people/controller.py`, `TaskQueue`, `ClientService`, `auth/controller.py`, `PriceRuleService`, `modules/ad_tags/dto.py`, `audit/controller.py`, `InvoiceService`, `views/controller.py`, `client_notes/controller.py`, `GamToolService`, `pydantic`, `members/controller.py`, `checklist_items/controller.py`, `Bucket`, `modules/rewards/controller.py`, `account/controller.py`, `checklists/controller.py`, `ClientLoaderService`, `ProfileService`, `Limiter`, `.of_detail`, `ClientAdTagService`, `ClientPriceRuleService`, `costs/controller.py`, `internal/rewards/controller.py`, `GoogleService`, `documents/controller.py`, `.__init__`, `.__init__`, `tasks/dto.py`, `internal/rewards/controller.py`, `PublicRewardService`, `DomainError`, `.__init__`, `.__init__`, `.__init__`, `networks/controller.py`, `goals/service.py`?**
  _High betweenness centrality (0.126) - this node is a cross-community bridge._
- **Are the 180 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 180 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `reward_public/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11428571428571428 - nodes in this community are weakly interconnected._
- **Why does `get()` connect `get` to `reward_public/controller.py`, `client_documents/controller.py`, `InvoiceOut`, `DashboardService`, `AlertService`, `RoleService`, `PageOut`, `staff/controller.py`, `commissions/controller.py`, `schedules/controller.py`, `GroupService`, `inventory/dto.py`, `.uow`, `api_keys/controller.py`, `CompanyService`, `GoalService`, `custom_metrics/controller.py`, `tasks/controller.py`, `InvitationOut`, `LoaderOut`, `dashboard_templates/controller.py`, `LoaderService`, `clients`, `modules/results/controller.py`, `AdTagService`, `currencies/controller.py`, `ReportService`, `ContractService`, `mark`, `SiteService`, `modules/facebook/controller.py`, `people/controller.py`, `TaskQueue`, `ClientService`, `auth/controller.py`, `FacebookRuleOut`, `events/controller.py`, `main.py`, `DashboardTemplateOut`, `audit/controller.py`, `InvoiceService`, `views/controller.py`, `client_notes/controller.py`, `GamToolService`, `PayeeDetailsOut`, `download`, `members/controller.py`, `checklist_items/controller.py`, `checklists`, `Bucket`, `account/controller.py`, `edit_image`, `modules/rewards/controller.py`, `checklists/controller.py`, `mine`, `contracts`, `ClientLoaderService`, `ProfileService`, `reports/service.py`, `goals/controller.py`, `ClientAdTagService`, `team`, `ClientPriceRuleService`, `costs/controller.py`, `internal/rewards/controller.py`, `GoogleService`, `.page_saved`, `image`, `PriceRuleService`, `health/controller.py`, `ItemsOut`, `DomainError`, `networks/controller.py`?**
  _High betweenness centrality (0.079) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `InvoiceOut` be split into smaller, more focused modules?**
  _Cohesion score 0.08665269042627533 - nodes in this community are weakly interconnected._