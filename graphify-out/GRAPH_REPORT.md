# Graph Report - avant-api  (2026-11-11)

## Corpus Check
- 376 files · ~119,426 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 5284 nodes · 14878 edges · 253 communities (133 shown, 120 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2449 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `017265d5`
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
- .trusted_uow
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
- clean_code.py
- get
- mfa/controller.py
- fastapi
- reports/service.py
- CapturingMailer
- RewardService
- session-start.sh
- avant-api
- test_price_rules.py
- tasks/dto.py
- modules/ad_tags/dto.py
- ad_tag_public/service.py
- test_alerts.py
- test_gam_tools.py
- documents/controller.py
- modules/price_rules/controller.py
- .save_rule
- Services
- test_reports.py
- networks/service.py
- router.py
- download
- Services
- ExportsBusy
- MemoryCounter
- edit
- test_company_image.py
- members/controller.py
- typing
- clients
- ports.py
- Actor
- account/controller.py
- client_documents/controller.py
- .build
- commissions/controller.py
- SessionCookies
- main.py
- invoices/controller.py
- Settings
- export.py
- Limiter
- test_hardening.py
- ClientAdTagService
- checklists/controller.py
- avant-api
- networks/controller.py
- .of
- test_reward_public.py
- PriceRuleService
- image
- avant_core_access_models
- events.py
- uuid
- .of
- internal/rewards/controller.py
- sites/service.py
- Avant: grupos na Empresa e imagem da Empresa
- tasks/controller.py
- Groone Avant: contexto do projeto
- .assign
- DashboardTemplateOut
- google/controller.py
- PublicRewardService
- Actor
- reward_public/service.py
- dollars
- ad_tag_public/dto.py
- MemoryBucket
- updates
- .of_detail
- Avant: repositório e plano do MVP
- test_account.py
- limits.py
- contracts/controller.py
- RewardCache
- .page
- test_staff_without_permission_and_other_clients
- ad_units
- .run_guarded
- CommissionService
- _marketing_client
- SupportTaskService
- Arquitetura do MVP do Avant
- test_mfa.py
- GoalService
- get
- test_who_sees_and_changes_invoices
- Counter
- Actor
- Actor
- .__init__
- GoalTemplateIn
- checklists/controller.py
- mine
- CompanyService
- SiteService
- modules/loaders/controller.py
- McmService
- image_response
- goals/service.py
- CascadeHourOut
- UserOut
- PayeeDetailsOut
- RedisEvents
- image
- team
- Avant: conexão com o GAM
- edit_image
- create
- UserOut
- events
- health/controller.py
- SupportTaskService
- .of
- test_events.py
- AdTagHealthOut
- networks/controller.py
- receive
- TaskQueue
- FiscalDataOut
- .of_view
- RateLimited
- package.json
- ClientLoaderService
- PriceRuleHistoryOut
- StreamLimiter
- ReportQueryIn
- ClientService
- PageOut
- UnitOfWorkFactory
- person
- .available_months
- forget_tags
- create
- index
- modules/loaders/dto.py
- .classify
- modules/price_rules/dto.py
- shared/dto.py
- RewardBuffer
- MemoryRewardCache
- LoaderOptionOut
- document_response
- PublicPriceFloorService
- set_settings
- NoEvents
- is_exempt
- _BrokenAuthService
- .to_change

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 217 edges
2. `PageOut` - 193 edges
3. `_csrf()` - 182 edges
4. `_onboard_owner()` - 176 edges
5. `get()` - 171 edges
6. `Services` - 165 edges
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

## Communities (253 total, 120 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.14
Nodes (9): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body() (+1 more)

### Community 1 - "invoices/controller.py"
Cohesion: 0.12
Nodes (13): create_service(), service_options(), update_service(), invoice_service(), InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceServiceOut (+5 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (25): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+17 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "_member_client"
Cohesion: 0.07
Nodes (29): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit(), _membership_ids(), test_groups_lifecycle(), _assert_denied() (+21 more)

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (20): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+12 more)

### Community 7 - "goals/controller.py"
Cohesion: 0.18
Nodes (5): delete_template(), role_goals(), set_role_goal(), update_template(), RoleGoalIn

### Community 8 - "steps"
Cohesion: 0.08
Nodes (25): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, jobs, test, name (+17 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.10
Nodes (20): Acesso, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade (+12 more)

### Community 12 - ".trusted_uow"
Cohesion: 0.12
Nodes (3): issue(), InvoiceOut, InvoiceService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.15
Nodes (6): networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "AdTagService"
Cohesion: 0.11
Nodes (12): create(), delete(), index(), publish(), restore(), set_active(), show(), units() (+4 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.11
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.11
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService, InvitationOut

### Community 18 - "security.py"
Cohesion: 0.05
Nodes (25): api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor(), get_auth(), get_session_actor(), get_session_auth() (+17 more)

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
Cohesion: 0.06
Nodes (19): RecordingQueue, client(), engine(), mailer(), settings_for_tests(), _settings(), test_every_connection_has_a_statement_and_idle_timeout(), test_pool_is_bounded_and_waits_little() (+11 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), roles(), set_home(), show(), update(), DashboardTemplateIn (+5 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), single_letter_names(), source_files()

### Community 27 - "get"
Cohesion: 0.09
Nodes (15): hours(), index(), set_floor(), set_status(), settings(), show(), sites(), update_blocks() (+7 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.07
Nodes (11): get_cookies(), confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut (+3 more)

### Community 29 - "fastapi"
Cohesion: 0.10
Nodes (8): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService, result_service(), ResultService

### Community 30 - "reports/service.py"
Cohesion: 0.05
Nodes (17): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+9 more)

### Community 31 - "CapturingMailer"
Cohesion: 0.10
Nodes (37): CapturingMailer, Sent, _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit() (+29 more)

### Community 32 - "RewardService"
Cohesion: 0.08
Nodes (7): create(), forget_pages(), create(), update(), RewardIn, RewardOut, RewardService

### Community 36 - "test_price_rules.py"
Cohesion: 0.09
Nodes (33): FixedCountries, _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _cascade_rule(), _cascade_site() (+25 more)

### Community 38 - "modules/ad_tags/dto.py"
Cohesion: 0.18
Nodes (13): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagDraftIO, AdTagHealthDayOut, AdTagIn, AdTagLiveOut (+5 more)

### Community 39 - "ad_tag_public/service.py"
Cohesion: 0.10
Nodes (8): ad_tag_cache_key(), BucketRule, config(), page_views(), preflight(), public_ad_tag_service(), PageViewIn, PublicAdTagService

### Community 40 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 41 - "test_gam_tools.py"
Cohesion: 0.19
Nodes (10): _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads() (+2 more)

### Community 42 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "modules/price_rules/controller.py"
Cohesion: 0.10
Nodes (15): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+7 more)

### Community 44 - ".save_rule"
Cohesion: 0.16
Nodes (5): create_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 45 - "Services"
Cohesion: 0.03
Nodes (19): Services, GeoLiteCountries, NoCountries, KeyValueBuffer, MemoryKeyValueBuffer, RedisKeyValueBuffer, MemoryRewardBuffer, get_services() (+11 more)

### Community 46 - "test_reports.py"
Cohesion: 0.13
Nodes (17): _checkouts(), test_report_requests_use_few_connections(), query(), _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission(), test_batch_runs_a_screen_with_one_slot_and_tells_how_long_to_wait() (+9 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "router.py"
Cohesion: 0.12
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 49 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "ExportsBusy"
Cohesion: 0.20
Nodes (4): ExportsBusy, export_slot(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 52 - "MemoryCounter"
Cohesion: 0.08
Nodes (13): RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO (+5 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "test_company_image.py"
Cohesion: 0.10
Nodes (13): _check_jpeg_size(), PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image() (+5 more)

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+6 more)

### Community 56 - "typing"
Cohesion: 0.17
Nodes (5): _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "ports.py"
Cohesion: 0.18
Nodes (3): is_cascade_shape(), safe_site_cascades(), site_cascades()

### Community 59 - "Actor"
Cohesion: 0.10
Nodes (10): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+2 more)

### Community 60 - "account/controller.py"
Cohesion: 0.10
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "client_documents/controller.py"
Cohesion: 0.14
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 62 - ".build"
Cohesion: 0.06
Nodes (7): engine_options(), _mailer(), RedisRewardBuffer, RedisRewardCache, CeleryQueue, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "commissions/controller.py"
Cohesion: 0.22
Nodes (7): commission_service(), AdjustmentIn, CommissionMonthOut, CommissionSettingsIn, CommissionSettingsOut, MonthIn, MyCommissionsOut

### Community 64 - "SessionCookies"
Cohesion: 0.06
Nodes (16): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+8 more)

### Community 65 - "main.py"
Cohesion: 0.06
Nodes (20): CompanyChanged, CsrfFailed, error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected() (+12 more)

### Community 66 - "invoices/controller.py"
Cohesion: 0.21
Nodes (5): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 67 - "Settings"
Cohesion: 0.08
Nodes (4): SessionCookies, Settings, verify(), test_closing_deployed_cookies_keeps_them_secure()

### Community 68 - "export.py"
Cohesion: 0.07
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 69 - "Limiter"
Cohesion: 0.15
Nodes (8): TooManyAttempts, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter()

### Community 70 - "test_hardening.py"
Cohesion: 0.16
Nodes (12): _rendered(), test_api_key_never_reaches_the_log(), test_docs_are_closed_in_production(), test_every_response_has_the_content_security_policy(), test_every_response_has_the_security_headers(), test_invalid_bearer_is_limited_per_ip_before_the_database(), counting(), test_policy_has_no_exception_when_the_docs_are_closed() (+4 more)

### Community 71 - "ClientAdTagService"
Cohesion: 0.08
Nodes (14): AdTagOut, create(), delete(), health(), index(), publish(), restore(), set_active() (+6 more)

### Community 72 - "checklists/controller.py"
Cohesion: 0.12
Nodes (5): site_checklist_service(), ChecklistMarkIn, ChecklistNoteIn, ChecklistOut, ChecklistProgressOut

### Community 76 - ".of"
Cohesion: 0.09
Nodes (4): show(), CostLineOut, MonthResultOut, ResultTotalsOut

### Community 77 - "test_reward_public.py"
Cohesion: 0.12
Nodes (18): reward_cache_key(), _buffer(), _cascade_reward(), test_events_and_leads_go_to_the_buffer(), test_icon_route_has_the_ip_limit(), test_public_config_is_cached_and_cleared(), test_reward_page_has_cascade_for_rewards_block(), test_reward_page_has_no_cascade_for_other_country() (+10 more)

### Community 78 - "PriceRuleService"
Cohesion: 0.10
Nodes (4): PriceRuleConfigIn, PriceRuleDetailsOut, PriceRuleOut, stored_drop_tiers()

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 81 - "avant_core_access_models"
Cohesion: 0.09
Nodes (5): results(), ClientResultService, ResultsOut, default_period(), page_out()

### Community 82 - "events.py"
Cohesion: 0.14
Nodes (4): EventSource, _parse(), sse(), EventService

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 85 - "internal/rewards/controller.py"
Cohesion: 0.06
Nodes (12): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+4 more)

### Community 86 - "sites/service.py"
Cohesion: 0.25
Nodes (8): AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn, SitesPatchIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "tasks/controller.py"
Cohesion: 0.22
Nodes (4): change(), comment(), create(), task()

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 91 - ".assign"
Cohesion: 0.25
Nodes (5): Atribuição de sites, GAM, Networks, Sites e ad units, assign_sites()

### Community 92 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 94 - "google/controller.py"
Cohesion: 0.03
Nodes (21): _google(), GoogleFailed, GoogleUnavailable, challenge(), _claims(), GoogleAuth, GoogleOAuth, identity_from_id_token() (+13 more)

### Community 95 - "PublicRewardService"
Cohesion: 0.11
Nodes (3): public_reward_service(), public_control_percent(), PublicRewardService

### Community 96 - "Actor"
Cohesion: 0.15
Nodes (3): adjust(), delete_rule(), settings()

### Community 97 - "reward_public/service.py"
Cohesion: 0.20
Nodes (12): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicRewardPriceOut (+4 more)

### Community 102 - "ad_tag_public/dto.py"
Cohesion: 0.11
Nodes (6): PageViewBlockIn, PublicAdTagOut, PublicBlockOut, PublicLoaderOut, PublicMgidOut, PublicTagOut

### Community 123 - "MemoryBucket"
Cohesion: 0.20
Nodes (5): BucketResult, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - ".of_detail"
Cohesion: 0.14
Nodes (3): ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 130 - "test_account.py"
Cohesion: 0.33
Nodes (7): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 131 - "limits.py"
Cohesion: 0.06
Nodes (5): MemoryCounter, RedisBucket, RedisCounter, KeyValueIn, test_redis_down_is_a_503_not_a_500()

### Community 132 - "contracts/controller.py"
Cohesion: 0.06
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 133 - "RewardCache"
Cohesion: 0.11
Nodes (5): RewardCache, forget_cascades(), forget_floors(), forget_rule(), forget_site()

### Community 134 - ".page"
Cohesion: 0.14
Nodes (3): index(), audit_service(), AuditService

### Community 135 - "test_staff_without_permission_and_other_clients"
Cohesion: 0.38
Nodes (8): _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission(), test_staff_without_permission_and_other_clients()

### Community 138 - "CommissionService"
Cohesion: 0.13
Nodes (5): mine(), _month(), team(), PersonMonthOut, CommissionService

### Community 139 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.19
Nodes (15): run_password_reset_tasks(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable() (+7 more)

### Community 145 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 146 - "get"
Cohesion: 0.08
Nodes (15): health(), metrics(), add_item(), create(), delete(), delete_service(), get(), mine() (+7 more)

### Community 147 - "test_who_sees_and_changes_invoices"
Cohesion: 0.06
Nodes (42): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+34 more)

### Community 149 - "Actor"
Cohesion: 0.13
Nodes (7): ad_units(), delete(), show(), site_options(), sites_of_member(), unlinked(), capped()

### Community 150 - "Actor"
Cohesion: 0.05
Nodes (18): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+10 more)

### Community 152 - ".__init__"
Cohesion: 0.06
Nodes (7): refresh_levels(), _error_code(), test_deployed_cookies_use_the_host_prefix(), test_every_write_route_refuses_another_site(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 155 - "checklists/controller.py"
Cohesion: 0.11
Nodes (8): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistDetailOut, SiteChecklistService

### Community 158 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 161 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 162 - "modules/loaders/controller.py"
Cohesion: 0.11
Nodes (9): create(), delete(), index(), show(), update(), loader_service(), LoaderIn, LoaderOut (+1 more)

### Community 163 - "McmService"
Cohesion: 0.10
Nodes (9): confirm_network(), register_network(), reject_network(), unassigned_networks(), mcm_service(), ClientNetworkIn, McmCandidateOut, McmService (+1 more)

### Community 164 - "image_response"
Cohesion: 0.15
Nodes (3): client_image(), image_response(), image_upload()

### Community 167 - "UserOut"
Cohesion: 0.11
Nodes (9): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+1 more)

### Community 171 - "RedisEvents"
Cohesion: 0.27
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 174 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 175 - "Avant: conexão com o GAM"
Cohesion: 0.11
Nodes (16): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment, Avant: conexão com o GAM, Caminho conta de serviço (+8 more)

### Community 176 - "edit_image"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 178 - "UserOut"
Cohesion: 0.08
Nodes (9): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService (+1 more)

### Community 180 - "health/controller.py"
Cohesion: 0.17
Nodes (3): ready(), health_service(), HealthService

### Community 182 - "SupportTaskService"
Cohesion: 0.15
Nodes (4): tasks(), support_task_service(), TaskOut, SupportTaskService

### Community 184 - ".of"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 186 - "test_events.py"
Cohesion: 0.23
Nodes (10): channel(), _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports() (+2 more)

### Community 190 - "networks/controller.py"
Cohesion: 0.13
Nodes (12): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs(), network_service() (+4 more)

### Community 191 - "receive"
Cohesion: 0.16
Nodes (9): POSTGRES_PASSWORD, env, image, options, ports, postgres, cors(), preflight() (+1 more)

### Community 192 - "TaskQueue"
Cohesion: 0.09
Nodes (8): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskMailQueue, TaskQueue, enqueue_sync()

### Community 196 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 197 - "ClientLoaderService"
Cohesion: 0.11
Nodes (7): delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService

### Community 198 - "PriceRuleHistoryOut"
Cohesion: 0.12
Nodes (3): history(), PriceRuleHistoryOut, PriceRuleHourOut

### Community 204 - "ClientService"
Cohesion: 0.06
Nodes (30): audit(), cancel_owner(), change_status(), client(), client_options(), client_teams(), clients(), edit_client() (+22 more)

### Community 210 - "PageOut"
Cohesion: 0.11
Nodes (5): reward_service(), csv_response(), lead_filter(), period(), PageOut

### Community 222 - "modules/price_rules/dto.py"
Cohesion: 0.11
Nodes (6): CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigOut, PriceRuleSettingsIn, _recommended_models()

### Community 223 - "shared/dto.py"
Cohesion: 0.11
Nodes (3): image_url(), RevenueStatusOut, RoleRefOut

### Community 239 - "PublicPriceFloorService"
Cohesion: 0.11
Nodes (5): CountryLookup, Bucket, prices(), PublicPriceFloorsOut, PublicPriceFloorService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2391 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **120 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `invoices/controller.py`, `roles/controller.py`, `DashboardService`, `Actor`, `contracts/controller.py`, `.page`, `GamToolService`, `RewardCache`, `_month`, `CommissionService`, `.trusted_uow`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `security.py`, `custom_metrics/controller.py`, `PageOut`, `Actor`, `goals/controller.py`, `networks/service.py`, `checklists/controller.py`, `get`, `fastapi`, `mfa/controller.py`, `reports/service.py`, `RewardService`, `SiteService`, `modules/loaders/controller.py`, `McmService`, `goals/service.py`, `modules/ad_tags/dto.py`, `ad_tag_public/service.py`, `UserOut`, `tasks/dto.py`, `documents/controller.py`, `modules/price_rules/controller.py`, `networks/service.py`, `Services`, `UserOut`, `MemoryCounter`, `SupportTaskService`, `members/controller.py`, `.__init__`, `ports.py`, `clients`, `.__init__`, `account/controller.py`, `client_documents/controller.py`, `commissions/controller.py`, `SessionCookies`, `TaskQueue`, `invoices/controller.py`, `networks/controller.py`, `ClientLoaderService`, `ClientAdTagService`, `checklists/controller.py`, `ClientService`, `image`, `avant_core_access_models`, `PageOut`, `internal/rewards/controller.py`, `sites/service.py`, `forget_tags`, `google/controller.py`, `PublicRewardService`, `.__init__`, `.__init__`, `RewardBuffer`, `PublicPriceFloorService`, `.__init__`, `.__init__`, `.__init__`, `.__init__`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Are the 168 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 168 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PublicRewardService` be split into smaller, more focused modules?**
  _Cohesion score 0.14245014245014245 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `invoices/controller.py`, `roles/controller.py`, `DashboardService`, `Actor`, `contracts/controller.py`, `.page`, `GamToolService`, `goals/controller.py`, `RewardCache`, `_month`, `.trusted_uow`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `get`, `security.py`, `PageOut`, `Actor`, `Actor`, `networks/service.py`, `checklists/controller.py`, `get`, `reports/service.py`, `RewardService`, `SiteService`, `modules/loaders/controller.py`, `McmService`, `goals/service.py`, `modules/ad_tags/dto.py`, `UserOut`, `tasks/dto.py`, `modules/price_rules/controller.py`, `ad_units`, `router.py`, `Services`, `MemoryCounter`, `SupportTaskService`, `members/controller.py`, `Actor`, `networks/controller.py`, `ClientLoaderService`, `ClientAdTagService`, `checklists/controller.py`, `networks/controller.py`, `ClientService`, `PriceRuleService`, `image`, `avant_core_access_models`, `.of`, `internal/rewards/controller.py`, `sites/service.py`, `forget_tags`, `tasks/controller.py`, `index`, `shared/dto.py`?**
  _High betweenness centrality (0.085) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `invoices/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11587301587301588 - nodes in this community are weakly interconnected._