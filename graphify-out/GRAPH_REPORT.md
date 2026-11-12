# Graph Report - avant-api  (2026-11-12)

## Corpus Check
- 385 files · ~124,656 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 5467 nodes · 15458 edges · 267 communities (135 shown, 132 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2475 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a8e1798e`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- PublicRewardService
- roles/controller.py
- DashboardService
- Actor
- conftest.py
- gam_tools/dto.py
- clients/controller.py
- test
- _month
- Avant: models do MVP
- _csrf
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
- test_account.py
- goals/controller.py
- verify
- image_response
- clean_code.py
- AdTagOut
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
- test_account.py
- mcm/controller.py
- ClientService
- modules/loaders/controller.py
- PriceRuleService
- AdTagService
- Services
- test_reports.py
- networks/service.py
- test_invitation_mail.py
- clients
- Services
- gam_tools/controller.py
- MemoryCounter
- edit
- download
- MemberService
- test_api_keys.py
- clients
- observe
- modules/rewards/controller.py
- google/controller.py
- avant_core_access_models
- test_cache_down_does_not_break_the_page_or_the_save
- checklists/controller.py
- auth/controller.py
- ContractService
- export.py
- Limiter
- api_docs/controller.py
- AdTagOut
- checklists/controller.py
- avant-api
- CeleryQueue
- reward_cache.py
- create
- browser
- ClientPriceRuleService
- image
- install
- checklists
- test_events.py
- test_events.py
- AdTagHealthOut
- .uow
- sites/service.py
- .approve
- RedisCounter
- Groone Avant: contexto do projeto
- pydantic
- InvoiceService
- google/controller.py
- page_out
- gam_tools/service.py
- reward_public/dto.py
- ad_tag_public/service.py
- BucketRule
- updates
- contracts/controller.py
- Avant: repositório e plano do MVP
- .export_saved
- price_floor_public/controller.py
- test_dashboards.py
- RewardCache
- mine
- test_key_values.py
- SiteService
- client_documents/controller.py
- .save_rule
- ContractClientRefOut
- ContractOut
- Arquitetura do MVP do Avant
- .update
- GoalService
- SiteChecklistService
- conftest.py
- test_settings.py
- .of
- test_reward_public.py
- goals/controller.py
- CapturingMailer
- dollars
- sites/service.py
- team
- networks/controller.py
- test_permission_denied.py
- package.json
- reports/service.py
- UserOut
- _month
- internal/loaders/service.py
- client_documents/controller.py
- .runs
- shared/dto.py
- document_response
- AdTagUnitDayOut
- profile/controller.py
- get
- RedisEvents
- network
- modules/loaders/controller.py
- tasks/controller.py
- commissions/controller.py
- CompanyService
- settings.py
- PayeeDetailsOut
- goals/service.py
- TaskQueue
- postgres
- alerts/dependencies.py
- key_values/controller.py
- GoalTemplateIn
- ClientLoaderService
- test_networks.py
- test_metrics.py
- sites/controller.py
- modules/loaders/dto.py
- Actor
- PriceRuleDetailsOut
- Actor
- LoaderOptionOut
- Counter
- .build
- O que já tem
- HealthService
- _BrokenAuthService
- CommissionService
- settings_for_tests
- UserOut
- _contract_fields
- _SpyCounter
- UnitOfWorkFactory
- clients/controller.py
- image
- CommissionRuleOut
- RewardAdUnitGroupOut
- person
- forget_site
- edit_image
- _scaling_client
- GamToolNetworkOut
- capped
- GeoLiteCountries
- _BrokenRedis
- RedisRewardBuffer
- checklists/dependencies.py
- invalid_variable_names

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 233 edges
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

## Communities (267 total, 132 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.14
Nodes (9): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body() (+1 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (26): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+18 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "conftest.py"
Cohesion: 0.09
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 6 - "gam_tools/dto.py"
Cohesion: 0.13
Nodes (4): GamStepOut, GamToolClientOut, GamToolPersonOut, GamToolSiteOut

### Community 7 - "clients/controller.py"
Cohesion: 0.09
Nodes (11): audit(), cancel_owner(), change_status(), client_image(), client_options(), clients(), edit_client_image(), invite_owner() (+3 more)

### Community 8 - "test"
Cohesion: 0.07
Nodes (33): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, jobs (+25 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.05
Nodes (35): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+27 more)

### Community 11 - "_csrf"
Cohesion: 0.10
Nodes (32): run_password_reset_tasks(), _csrf(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+24 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.11
Nodes (7): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "modules/ad_tags/dto.py"
Cohesion: 0.10
Nodes (12): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagDraftIO, AdTagHealthDayOut, AdTagIn, AdTagLiveOut (+4 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (9): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService (+1 more)

### Community 17 - "PageOut"
Cohesion: 0.09
Nodes (9): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut (+1 more)

### Community 18 - "security.py"
Cohesion: 0.06
Nodes (19): CsrfFailed, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company(), get_actor(), get_auth() (+11 more)

### Community 19 - "CustomMetricService"
Cohesion: 0.08
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "test_account.py"
Cohesion: 0.04
Nodes (16): memory_services(), MemoryCounter, MemoryKeyValueBuffer, MemoryRewardBuffer, MemoryRewardCache, NoEvents, RecordingQueue, _account() (+8 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.16
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "fastapi"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.05
Nodes (22): catalog(), create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index() (+14 more)

### Community 31 - "test_reward_public.py"
Cohesion: 0.10
Nodes (18): FixedCountries, _buffer(), _cascade_reward(), test_events_and_leads_go_to_the_buffer(), test_icon_route_has_the_ip_limit(), test_public_config_is_cached_and_cleared(), test_reward_page_has_cascade_for_rewards_block(), test_reward_page_has_no_cascade_for_other_country() (+10 more)

### Community 32 - "RewardService"
Cohesion: 0.09
Nodes (5): create(), index(), show(), RewardOut, RewardService

### Community 36 - "test_price_rules.py"
Cohesion: 0.10
Nodes (32): _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _cascade_rule(), _cascade_site(), _company_of() (+24 more)

### Community 37 - "PublicAdTagService"
Cohesion: 0.10
Nodes (7): ad_tag_cache_key(), config(), page_views(), preflight(), public_ad_tag_service(), PageViewIn, PublicAdTagService

### Community 38 - "PriceRuleSiteOut"
Cohesion: 0.09
Nodes (4): settings(), update_settings(), PriceRuleSiteOut, _recommended_models()

### Community 39 - "test_account.py"
Cohesion: 0.22
Nodes (9): _BrokenReleaseCounter, _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login() (+1 more)

### Community 40 - "mcm/controller.py"
Cohesion: 0.10
Nodes (9): confirm_network(), register_network(), reject_network(), unassigned_networks(), ClientNetworkIn, McmCandidateOut, McmService, NetworkOut (+1 more)

### Community 41 - "ClientService"
Cohesion: 0.07
Nodes (9): client(), client_teams(), manager_change(), owner_invitations(), client_service(), ClientMemberOut, ClientService, owner_invitation_out() (+1 more)

### Community 42 - "modules/loaders/controller.py"
Cohesion: 0.20
Nodes (4): create(), LoaderIn, LoaderOut, LoaderService

### Community 43 - "PriceRuleService"
Cohesion: 0.08
Nodes (12): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), show(), sites() (+4 more)

### Community 44 - "AdTagService"
Cohesion: 0.09
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 45 - "Services"
Cohesion: 0.03
Nodes (23): Services, get_services(), require(), require_report(), index(), audit_service(), AuditService, company_service() (+15 more)

### Community 46 - "test_reports.py"
Cohesion: 0.08
Nodes (26): refresh_levels(), _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _checked_out(), _checkouts() (+18 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "test_invitation_mail.py"
Cohesion: 0.24
Nodes (10): _assert_mail_not_sent(), _client_with_owner_invitation(), _invite(), _owner_invitation_emails(), _pending_emails(), test_invite_answers_503_when_the_mail_fails(), test_owner_invitation_answers_503_when_the_mail_fails(), test_owner_invitation_resend_answers_503_when_the_mail_fails() (+2 more)

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "gam_tools/controller.py"
Cohesion: 0.16
Nodes (7): ads_txt(), install(), run(), runs(), start(), GamToolRunIn, GamToolRunOut

### Community 52 - "MemoryCounter"
Cohesion: 0.10
Nodes (13): RewardActiveIn, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardIn, RewardLeadAnswerOut, RewardLeadIO (+5 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (16): API first e chaves de API, Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa (+8 more)

### Community 54 - "download"
Cohesion: 0.12
Nodes (4): documents(), download(), upload(), DocumentService

### Community 55 - "MemberService"
Cohesion: 0.06
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+6 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.12
Nodes (15): BucketResult, RedisBucket, MemoryBucket, _bearer(), _create(), _exercise(), _insert_key(), _keys_in_two_companies() (+7 more)

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "observe"
Cohesion: 0.36
Nodes (3): _content_security_policy(), observe(), _route_template()

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.08
Nodes (12): ad_units(), delete(), delete_lead(), export_leads(), leads(), metrics(), set_active(), set_icon() (+4 more)

### Community 60 - "google/controller.py"
Cohesion: 0.08
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "avant_core_access_models"
Cohesion: 0.05
Nodes (9): results(), client_result_service(), ClientResultService, StaffInviteIn, show(), result_service(), ResultsOut, default_period() (+1 more)

### Community 63 - "checklists/controller.py"
Cohesion: 0.13
Nodes (7): add_note(), check(), checklists(), delete_note(), edit_note(), mark(), months()

### Community 64 - "auth/controller.py"
Cohesion: 0.04
Nodes (21): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), get_invitation(), login(), me() (+13 more)

### Community 65 - "ContractService"
Cohesion: 0.12
Nodes (4): contract_networks(), remove_contract(), contract_service(), ContractService

### Community 68 - "export.py"
Cohesion: 0.08
Nodes (13): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+5 more)

### Community 69 - "Limiter"
Cohesion: 0.17
Nodes (8): Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_refused_reserve_never_touches_the_other_keys(), test_release_failure_does_not_break_a_good_attempt()

### Community 70 - "api_docs/controller.py"
Cohesion: 0.15
Nodes (4): openapi(), swagger(), swagger_asset(), _swagger_page()

### Community 71 - "AdTagOut"
Cohesion: 0.12
Nodes (12): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+4 more)

### Community 72 - "checklists/controller.py"
Cohesion: 0.09
Nodes (7): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "CeleryQueue"
Cohesion: 0.14
Nodes (6): CeleryQueue, masked_args(), _CapturingCelery, test_password_reset_task_masks_the_email_in_the_message(), test_tasks_with_ids_only_are_not_masked(), test_queue_does_not_break_the_request_without_broker()

### Community 77 - "browser"
Cohesion: 0.11
Nodes (13): configure_logging(), JsonFormatter, _rendered(), test_api_key_never_reaches_the_log(), test_docs_only_for_the_groone_session_with_2fa(), test_every_response_has_the_content_security_policy(), test_every_response_has_the_security_headers(), test_invalid_bearer_is_limited_per_ip_before_the_database() (+5 more)

### Community 78 - "ClientPriceRuleService"
Cohesion: 0.12
Nodes (14): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+6 more)

### Community 79 - "image"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "install"
Cohesion: 0.21
Nodes (9): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), masked_path() (+1 more)

### Community 82 - "test_events.py"
Cohesion: 0.11
Nodes (5): TooManyAttempts, EventSource, StreamLimiter, events(), EventService

### Community 83 - "test_events.py"
Cohesion: 0.13
Nodes (15): channel(), _parse(), sse(), _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot() (+7 more)

### Community 86 - "sites/service.py"
Cohesion: 0.18
Nodes (5): link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteIn

### Community 87 - ".approve"
Cohesion: 0.20
Nodes (9): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Imagem da Empresa, Issues, Modelo de dados, Regras, Resumo (+1 more)

### Community 88 - "RedisCounter"
Cohesion: 0.14
Nodes (4): RedisCounter, test_redis_decr_without_key_creates_nothing(), test_redis_limiter(), test_redis_down_is_a_503_not_a_500()

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 91 - "pydantic"
Cohesion: 0.19
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 92 - "InvoiceService"
Cohesion: 0.14
Nodes (14): create_service(), services(), update_service(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut (+6 more)

### Community 94 - "google/controller.py"
Cohesion: 0.03
Nodes (24): _google(), CompanyChanged, GoogleFailed, GoogleUnavailable, InvitationMailNotSent, NoActiveCompany, _claims(), GoogleAuth (+16 more)

### Community 97 - "reward_public/dto.py"
Cohesion: 0.11
Nodes (16): reward_cache_key(), CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut (+8 more)

### Community 102 - "ad_tag_public/service.py"
Cohesion: 0.13
Nodes (6): PageViewBlockIn, PublicAdTagOut, PublicBlockOut, PublicLoaderOut, PublicMgidOut, PublicTagOut

### Community 127 - "updates"
Cohesion: 0.11
Nodes (17): patterns, patterns, update-types, acoes, dependencias, imagens, dependency-name, patterns (+9 more)

### Community 128 - "contracts/controller.py"
Cohesion: 0.20
Nodes (6): ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut, _network_ref()

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 130 - ".export_saved"
Cohesion: 0.13
Nodes (4): ExportsBusy, export_slot(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 131 - "price_floor_public/controller.py"
Cohesion: 0.13
Nodes (3): prices(), public_price_floor_service(), PublicPriceFloorsOut

### Community 132 - "test_dashboards.py"
Cohesion: 0.12
Nodes (12): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company(), _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client() (+4 more)

### Community 133 - "RewardCache"
Cohesion: 0.21
Nodes (12): CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn, PriceRuleHistoryOut (+4 more)

### Community 134 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 135 - "test_key_values.py"
Cohesion: 0.18
Nodes (5): _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 136 - "SiteService"
Cohesion: 0.19
Nodes (4): show(), site_service(), SiteDetailOut, SiteService

### Community 137 - "client_documents/controller.py"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 138 - ".save_rule"
Cohesion: 0.14
Nodes (6): adjust(), create_rule(), delete_rule(), settings(), update_rule(), CommissionRuleIn

### Community 139 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 142 - "ContractOut"
Cohesion: 0.20
Nodes (6): contract(), contracts(), edit_contract(), finish_contract(), new_contract(), ContractOut

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 145 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 146 - "SiteChecklistService"
Cohesion: 0.17
Nodes (3): checklist(), ChecklistDetailOut, SiteChecklistService

### Community 147 - "conftest.py"
Cohesion: 0.05
Nodes (39): challenge(), browser(), client(), engine(), mailer(), query(), _networks(), test_contract_crud() (+31 more)

### Community 148 - "test_settings.py"
Cohesion: 0.25
Nodes (7): load_settings(), _environment(), _refused_names(), test_api_starts_with_each_transport(), test_environment_name_changes_nothing(), test_missing_or_invalid_configuration_stops_the_api(), test_start_error_shows_names_and_never_values()

### Community 152 - "test_reward_public.py"
Cohesion: 0.05
Nodes (25): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, ExpectedAsset, load_assets(), SwaggerAsset, SwaggerAssetChanged (+17 more)

### Community 153 - "goals/controller.py"
Cohesion: 0.18
Nodes (5): delete_template(), role_goals(), set_role_goal(), update_template(), RoleGoalIn

### Community 155 - "CapturingMailer"
Cohesion: 0.08
Nodes (42): CapturingMailer, Sent, _error_code(), _onboard_owner(), _owner_invite(), test_cookies_are_always_secure_with_the_host_prefix(), test_csrf_is_required_for_writes(), test_every_write_route_refuses_another_site() (+34 more)

### Community 162 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 163 - "networks/controller.py"
Cohesion: 0.09
Nodes (14): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+6 more)

### Community 164 - "test_permission_denied.py"
Cohesion: 0.11
Nodes (13): _manage_inventory(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query(), _assert_denied(), _queue() (+5 more)

### Community 165 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 166 - "reports/service.py"
Cohesion: 0.06
Nodes (18): CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+10 more)

### Community 167 - "UserOut"
Cohesion: 0.14
Nodes (7): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), PeopleService

### Community 168 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 172 - "client_documents/controller.py"
Cohesion: 0.26
Nodes (5): client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 174 - ".runs"
Cohesion: 0.20
Nodes (3): AdsTxtOut, GamToolRunNetworkOut, GamToolService

### Community 178 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 179 - "get"
Cohesion: 0.08
Nodes (16): health(), add_item(), available_months(), create(), delete(), delete_service(), get(), issue() (+8 more)

### Community 183 - "modules/loaders/controller.py"
Cohesion: 0.21
Nodes (4): delete(), index(), show(), update()

### Community 184 - "tasks/controller.py"
Cohesion: 0.05
Nodes (17): change(), comment(), create(), task(), tasks(), TaskClientOut, TaskCommentIn, TaskDataIn (+9 more)

### Community 185 - "commissions/controller.py"
Cohesion: 0.31
Nodes (5): AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn

### Community 186 - "CompanyService"
Cohesion: 0.07
Nodes (12): edit(), edit_fiscal(), edit_image(), fiscal(), image(), remove_image(), show(), CompanyDetailOut (+4 more)

### Community 190 - "PayeeDetailsOut"
Cohesion: 0.19
Nodes (3): save_payment_details(), update_item(), PayeeDetailsOut

### Community 192 - "TaskQueue"
Cohesion: 0.09
Nodes (8): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, QueueUnavailable, TaskMailQueue, TaskQueue

### Community 193 - "postgres"
Cohesion: 0.33
Nodes (6): POSTGRES_PASSWORD, env, image, options, ports, postgres

### Community 194 - "alerts/dependencies.py"
Cohesion: 0.18
Nodes (3): alert_service(), dashboard_service(), report_service()

### Community 195 - "key_values/controller.py"
Cohesion: 0.09
Nodes (8): RateLimited, KeyValueBuffer, RedisKeyValueBuffer, cors(), preflight(), receive(), KeyValueIn, receive_key_values()

### Community 197 - "ClientLoaderService"
Cohesion: 0.20
Nodes (5): delete(), index(), options(), show(), client_loader_service()

### Community 198 - "test_networks.py"
Cohesion: 0.38
Nodes (8): _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission(), test_staff_without_permission_and_other_clients()

### Community 201 - "test_metrics.py"
Cohesion: 0.15
Nodes (4): metrics(), exposition(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 202 - "sites/controller.py"
Cohesion: 0.13
Nodes (9): ad_units(), assign_sites(), classify(), classify_many(), delete(), members(), unlinked(), SitePatchIn (+1 more)

### Community 210 - "Actor"
Cohesion: 0.10
Nodes (13): create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+5 more)

### Community 212 - "PriceRuleDetailsOut"
Cohesion: 0.08
Nodes (4): update_config(), PriceRuleDetailsOut, forget_rule(), stored_drop_tiers()

### Community 217 - ".build"
Cohesion: 0.14
Nodes (3): _mailer(), NoCountries, test_each_transport_builds_its_mailer()

### Community 225 - "CommissionService"
Cohesion: 0.20
Nodes (3): set_settings(), commission_service(), CommissionService

### Community 226 - "settings_for_tests"
Cohesion: 0.13
Nodes (11): engine_settings(), restricted_engine(), settings_for_tests(), test_api_does_not_start_with_a_role_that_ignores_rls(), test_database_url_cannot_override_the_timeouts(), test_default_numbers_fit_the_connection_budget(), test_engine_settings_come_from_the_settings(), test_engine_settings_refuse_zero_and_above_the_ceiling() (+3 more)

### Community 228 - "UserOut"
Cohesion: 0.17
Nodes (3): PersonOut, person_out(), UserOut

### Community 231 - "_contract_fields"
Cohesion: 0.13
Nodes (4): create(), index(), site_options(), SiteListOut

### Community 239 - "UnitOfWorkFactory"
Cohesion: 0.06
Nodes (9): CountryLookup, Bucket, UnitOfWorkFactory, is_cascade_shape(), safe_site_cascades(), site_cascades(), RewardBuffer, RewardCache (+1 more)

### Community 240 - "clients/controller.py"
Cohesion: 0.10
Nodes (14): edit_client(), register_client(), ClientDetailOut, ClientIn, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn (+6 more)

### Community 245 - "forget_site"
Cohesion: 0.32
Nodes (3): forget_cascades(), forget_floors(), forget_site()

### Community 249 - "_scaling_client"
Cohesion: 0.38
Nodes (3): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2463 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **132 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `.__init__`, `roles/controller.py`, `DashboardService`, `Actor`, `RewardCache`, `.__init__`, `.__init__`, `_month`, `SiteService`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `modules/ad_tags/dto.py`, `api_keys/controller.py`, `GoalService`, `SiteChecklistService`, `CustomMetricService`, `.update`, `PageOut`, `goals/controller.py`, `AdTagOut`, `mfa/controller.py`, `fastapi`, `ReportService`, `RewardService`, `sites/service.py`, `networks/controller.py`, `PublicAdTagService`, `reports/service.py`, `UserOut`, `mcm/controller.py`, `ClientService`, `modules/loaders/controller.py`, `internal/loaders/service.py`, `AdTagService`, `Services`, `client_documents/controller.py`, `.runs`, `networks/service.py`, `PriceRuleService`, `Services`, `profile/controller.py`, `download`, `MemberService`, `tasks/controller.py`, `clients`, `CompanyService`, `commissions/controller.py`, `google/controller.py`, `avant_core_access_models`, `goals/service.py`, `auth/controller.py`, `TaskQueue`, `.__init__`, `ContractService`, `AdTagOut`, `checklists/controller.py`, `reward_cache.py`, `ClientPriceRuleService`, `image`, `Actor`, `.__init__`, `.__init__`, `pydantic`, `.__init__`, `test_redis_buffer_follows_the_worker_contract`, `google/controller.py`, `InvoiceService`, `gam_tools/service.py`, `CommissionService`, `.__init__`, `.__init__`, `UserOut`, `reward_public/dto.py`, `clients/controller.py`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Are the 183 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 183 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PublicRewardService` be split into smaller, more focused modules?**
  _Cohesion score 0.14461538461538462 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `api_keys/controller.py` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `Actor`, `RewardCache`, `clients/controller.py`, `SiteService`, `_month`, `.trusted_uow`, `.uow`, `ContractOut`, `modules/ad_tags/dto.py`, `inventory/dto.py`, `GoalService`, `SiteChecklistService`, `.update`, `PageOut`, `goals/controller.py`, `AdTagOut`, `RewardService`, `sites/service.py`, `networks/controller.py`, `PriceRuleSiteOut`, `UserOut`, `mcm/controller.py`, `ClientService`, `modules/loaders/controller.py`, `internal/loaders/service.py`, `AdTagService`, `Services`, `.runs`, `PriceRuleService`, `shared/dto.py`, `Services`, `gam_tools/controller.py`, `get`, `modules/loaders/controller.py`, `tasks/controller.py`, `MemberService`, `modules/rewards/controller.py`, `avant_core_access_models`, `checklists/controller.py`, `goals/service.py`, `ContractService`, `Actor`, `reports/service.py`, `ClientLoaderService`, `AdTagOut`, `checklists/controller.py`, `sites/controller.py`, `reward_cache.py`, `ClientPriceRuleService`, `image`, `checklists`, `Actor`, `PriceRuleDetailsOut`, `Actor`, `InvoiceService`, `page_out`, `gam_tools/service.py`, `UserOut`, `_contract_fields`, `clients/controller.py`, `GamToolNetworkOut`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07792207792207792 - nodes in this community are weakly interconnected._