# Graph Report - avant-api  (2026-11-11)

## Corpus Check
- 376 files · ~120,733 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 11 file(s) not represented in the graph (top: (none) 7, .ttf 2, .gz 1)

## Summary
- 5322 nodes · 14995 edges · 253 communities (127 shown, 126 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2466 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `7b916d16`
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
- .of
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
- shared/dto.py
- clean_code.py
- get
- mfa/controller.py
- fastapi
- ReportService
- CapturingMailer
- RewardService
- session-start.sh
- avant-api
- test_price_rules.py
- router.py
- modules/ad_tags/dto.py
- GoogleFailed
- mcm/controller.py
- test_gam_tools.py
- documents/controller.py
- modules/price_rules/controller.py
- AuthService
- Services
- test_reports.py
- networks/service.py
- router.py
- datetime
- Services
- ReportQueryIn
- MemoryCounter
- edit
- test_company_image.py
- members/controller.py
- test_api_keys.py
- clients
- main.py
- Actor
- account/controller.py
- client_documents/controller.py
- test_cache_down_does_not_break_the_page_or_the_save
- SiteChecklistService
- auth/controller.py
- test_hardening.py
- invoices/controller.py
- Settings
- export.py
- test_account.py
- documents/controller.py
- ClientAdTagService
- checklists/controller.py
- avant-api
- PageOut
- avant_core_access_models
- test_reward_public.py
- PriceRuleService
- image
- install
- results/dto.py
- test_events.py
- uuid
- .of
- internal/rewards/controller.py
- sites/service.py
- Avant: grupos na Empresa e imagem da Empresa
- RedisCounter
- Groone Avant: contexto do projeto
- .assign
- test_events.py
- google/controller.py
- audit/controller.py
- health/controller.py
- reward_public/service.py
- dollars
- ad_tag_public/dto.py
- limits.py
- updates
- SupportTaskService
- Avant: repositório e plano do MVP
- tasks/controller.py
- MemoryCounter
- contracts/controller.py
- RewardCache
- test_account.py
- test_staff_without_permission_and_other_clients
- AdUnitOut
- .run_guarded
- commissions/controller.py
- TaskDetailOut
- tasks/dto.py
- Arquitetura do MVP do Avant
- GoalTemplateOut
- get
- test_who_sees_and_changes_invoices
- internal/loaders/service.py
- UUID
- Actor
- datetime
- delete_template
- checklists/controller.py
- mine
- image_url
- SiteService
- modules/loaders/controller.py
- networks/controller.py
- alerts/dependencies.py
- .of
- UserOut
- PriceRuleHistoryOut
- Settings
- image
- GoalService
- Avant: conexão com o GAM
- fiscal
- Counter
- UserOut
- Actor
- RedisEvents
- document_response
- BaseModel
- verify
- .page_saved
- AdTagHealthOut
- receive
- TaskQueue
- .of
- .of_view
- time
- package.json
- ClientLoaderService
- clients
- show
- ClientService
- internal/rewards/controller.py
- client_image
- SiteListOut
- LoaderOut
- create
- modules/loaders/dto.py
- .classify
- RedisRewardBuffer
- _recommended_models
- events/controller.py
- ClientDocumentsOut
- typing
- MemoryRewardCache
- shared/http.py
- capped
- TaskPatchIn
- UnitOfWorkFactory
- NoEvents
- _BrokenReleaseCounter
- source_files
- internal/ad_tags/service.py

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 221 edges
2. `PageOut` - 193 edges
3. `_csrf()` - 184 edges
4. `_onboard_owner()` - 178 edges
5. `get()` - 171 edges
6. `Services` - 165 edges
7. `UnitOfWorkFactory` - 163 edges
8. `_staff()` - 81 edges
9. `ReportService` - 79 edges
10. `page_out()` - 79 edges

## Surprising Connections (you probably didn't know these)
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/modules/internal/people/controller.py
- `Onde está o trabalho` --references--> `PriceRuleSiteOut`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/price_rules/dto.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (253 total, 126 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.16
Nodes (9): options, client_address(), cors(), events(), icon(), leads(), page(), preflight() (+1 more)

### Community 1 - "invoices/controller.py"
Cohesion: 0.11
Nodes (15): payment_details(), save_payment_details(), update_service(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut (+7 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (26): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+18 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "_member_client"
Cohesion: 0.07
Nodes (24): _membership_ids(), test_groups_lifecycle(), _assert_denied(), _queue(), test_cost_writes_need_permission(), test_documents_need_company_edit(), test_member_writes_need_permission(), test_network_sync_and_disconnect_need_permission() (+16 more)

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (19): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+11 more)

### Community 7 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 8 - "steps"
Cohesion: 0.06
Nodes (30): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+22 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (21): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+13 more)

### Community 12 - ".trusted_uow"
Cohesion: 0.08
Nodes (6): issue(), pay(), service_options(), update_item(), InvoiceOut, InvoiceService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.12
Nodes (7): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "AdTagService"
Cohesion: 0.09
Nodes (14): create(), delete(), index(), publish(), restore(), set_active(), show(), units() (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.11
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.09
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "security.py"
Cohesion: 0.08
Nodes (22): CompanyChanged, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company() (+14 more)

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
Cohesion: 0.10
Nodes (9): RecordingQueue, _account(), _NoDatabase, _NoMail, _services(), test_forgot_password_only_queues_the_normalized_email(), test_forgot_route_never_sends_the_link_itself(), test_forgot_route_queues_without_database_or_mail_in_every_env() (+1 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "shared/dto.py"
Cohesion: 0.10
Nodes (6): client_teams(), ClientMemberOut, ClientProfileIn, CompanyRefOut, RevenueStatusOut, RoleRefOut

### Community 26 - "clean_code.py"
Cohesion: 0.18
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "get"
Cohesion: 0.08
Nodes (15): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+7 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (9): AcceptInvitationIn, confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "fastapi"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.05
Nodes (17): catalog(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut (+9 more)

### Community 31 - "CapturingMailer"
Cohesion: 0.08
Nodes (31): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _error_code(), _onboard_owner(), _owner_invite() (+23 more)

### Community 36 - "test_price_rules.py"
Cohesion: 0.12
Nodes (27): CapturingMailer, _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _offerwall_unit(), _present() (+19 more)

### Community 37 - "router.py"
Cohesion: 0.10
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 38 - "modules/ad_tags/dto.py"
Cohesion: 0.09
Nodes (11): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagDraftIO, AdTagHealthDayOut, AdTagIn, AdTagLiveOut, AdTagPublishIn (+3 more)

### Community 39 - "GoogleFailed"
Cohesion: 0.11
Nodes (6): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle

### Community 40 - "mcm/controller.py"
Cohesion: 0.11
Nodes (9): confirm_network(), register_network(), reject_network(), unassigned_networks(), mcm_service(), ClientNetworkIn, McmCandidateOut, McmService (+1 more)

### Community 41 - "test_gam_tools.py"
Cohesion: 0.12
Nodes (23): run_password_reset_tasks(), _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites() (+15 more)

### Community 42 - "documents/controller.py"
Cohesion: 0.09
Nodes (5): documents(), download(), upload(), document_service(), DocumentService

### Community 43 - "modules/price_rules/controller.py"
Cohesion: 0.07
Nodes (13): cascade_hours(), hours(), index(), set_floor(), set_status(), settings(), show(), sites() (+5 more)

### Community 44 - "AuthService"
Cohesion: 0.11
Nodes (3): get_invitation(), InvitationPreviewOut, AuthService

### Community 45 - "Services"
Cohesion: 0.04
Nodes (13): Services, PillowImageProcessor, MemoryRewardBuffer, get_services(), account_service(), public_ad_tag_service(), auth_service(), company_service() (+5 more)

### Community 46 - "test_reports.py"
Cohesion: 0.07
Nodes (24): client(), engine(), mailer(), Sent, _checkouts(), test_report_requests_use_few_connections(), query(), test_busy_export_answers_503_with_retry_after() (+16 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "router.py"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 49 - "datetime"
Cohesion: 0.15
Nodes (19): _result(), test_compare_header_follows_the_mode(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast(), _ana_id(), _report(), test_chart_options_keep_metric_styles() (+11 more)

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 52 - "MemoryCounter"
Cohesion: 0.08
Nodes (13): RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO (+5 more)

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "test_company_image.py"
Cohesion: 0.08
Nodes (17): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo() (+9 more)

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.15
Nodes (13): _bearer(), _create(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit() (+5 more)

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "main.py"
Cohesion: 0.11
Nodes (6): configure_logging(), _is_docs_page(), observe(), _route_template(), create_app(), public_price_floor_service()

### Community 59 - "Actor"
Cohesion: 0.10
Nodes (14): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+6 more)

### Community 60 - "account/controller.py"
Cohesion: 0.10
Nodes (12): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn (+4 more)

### Community 61 - "client_documents/controller.py"
Cohesion: 0.13
Nodes (7): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentService

### Community 62 - "test_cache_down_does_not_break_the_page_or_the_save"
Cohesion: 0.12
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "SiteChecklistService"
Cohesion: 0.15
Nodes (3): ChecklistDetailOut, ChecklistOut, SiteChecklistService

### Community 64 - "auth/controller.py"
Cohesion: 0.09
Nodes (13): accept(), company_image(), do_logout(), login(), me(), set_active_company(), ActiveCompanyIn, CompanyOut (+5 more)

### Community 65 - "test_hardening.py"
Cohesion: 0.11
Nodes (15): JsonFormatter, _BrokenAuthService, _rendered(), test_api_key_never_reaches_the_log(), test_docs_are_closed_in_production(), test_every_response_has_the_content_security_policy(), test_every_response_has_the_security_headers(), test_invalid_bearer_is_limited_per_ip_before_the_database() (+7 more)

### Community 66 - "invoices/controller.py"
Cohesion: 0.19
Nodes (8): edit_fiscal(), edit_image(), show(), CompanyDetailOut, CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 67 - "Settings"
Cohesion: 0.11
Nodes (3): SessionCookies, get_cookies(), test_closing_deployed_cookies_keeps_them_secure()

### Community 68 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "test_account.py"
Cohesion: 0.15
Nodes (8): Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_refused_reserve_never_touches_the_other_keys(), test_release_failure_does_not_break_a_good_attempt()

### Community 70 - "documents/controller.py"
Cohesion: 0.16
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 71 - "ClientAdTagService"
Cohesion: 0.12
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 72 - "checklists/controller.py"
Cohesion: 0.13
Nodes (5): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 76 - "avant_core_access_models"
Cohesion: 0.16
Nodes (3): ServiceAccountOut, SyncRunOut, enqueue_sync()

### Community 77 - "test_reward_public.py"
Cohesion: 0.10
Nodes (19): FixedCountries, _buffer(), _cascade_reward(), test_events_and_leads_go_to_the_buffer(), test_icon_route_has_the_ip_limit(), test_public_config_is_cached_and_cleared(), test_reward_page_has_cascade_for_rewards_block(), test_reward_page_has_no_cascade_for_other_country() (+11 more)

### Community 78 - "PriceRuleService"
Cohesion: 0.08
Nodes (4): update_config(), PriceRuleDetailsOut, forget_rule(), stored_drop_tiers()

### Community 79 - "image"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "install"
Cohesion: 0.13
Nodes (9): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), masked_path() (+1 more)

### Community 81 - "results/dto.py"
Cohesion: 0.05
Nodes (11): results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut (+3 more)

### Community 82 - "test_events.py"
Cohesion: 0.08
Nodes (9): TooManyAttempts, channel(), EventSource, _parse(), sse(), StreamLimiter, events(), EventService (+1 more)

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 85 - "internal/rewards/controller.py"
Cohesion: 0.10
Nodes (4): create(), show(), ClientRewardService, RewardOut

### Community 86 - "sites/service.py"
Cohesion: 0.25
Nodes (8): AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn, SitesPatchIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "RedisCounter"
Cohesion: 0.18
Nodes (3): RedisCounter, test_redis_decr_without_key_creates_nothing(), test_redis_limiter()

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 91 - ".assign"
Cohesion: 0.25
Nodes (5): Atribuição de sites, GAM, Networks, Sites e ad units, assign_sites()

### Community 92 - "test_events.py"
Cohesion: 0.28
Nodes (10): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports(), test_redis_source_delivers_published_messages() (+2 more)

### Community 94 - "google/controller.py"
Cohesion: 0.05
Nodes (12): GoogleUnavailable, GoogleAuth, new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), google_redirects() (+4 more)

### Community 95 - "audit/controller.py"
Cohesion: 0.18
Nodes (3): index(), audit_service(), AuditService

### Community 96 - "health/controller.py"
Cohesion: 0.17
Nodes (3): ready(), health_service(), HealthService

### Community 97 - "reward_public/service.py"
Cohesion: 0.07
Nodes (18): RewardBuffer, reward_cache_key(), public_reward_service(), CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut (+10 more)

### Community 102 - "ad_tag_public/dto.py"
Cohesion: 0.08
Nodes (12): BucketRule, config(), page_views(), preflight(), PageViewBlockIn, PageViewIn, PublicAdTagOut, PublicBlockOut (+4 more)

### Community 123 - "limits.py"
Cohesion: 0.12
Nodes (6): BucketResult, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "SupportTaskService"
Cohesion: 0.15
Nodes (4): tasks(), support_task_service(), TaskOut, SupportTaskService

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 130 - "tasks/controller.py"
Cohesion: 0.22
Nodes (4): change(), comment(), create(), task()

### Community 132 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 133 - "RewardCache"
Cohesion: 0.14
Nodes (14): CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn, PriceRuleOut (+6 more)

### Community 134 - "test_account.py"
Cohesion: 0.15
Nodes (14): _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_id_token_claims() (+6 more)

### Community 135 - "test_staff_without_permission_and_other_clients"
Cohesion: 0.38
Nodes (8): _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission(), test_staff_without_permission_and_other_clients()

### Community 136 - "AdUnitOut"
Cohesion: 0.16
Nodes (4): ad_units(), link(), unlinked(), AdUnitOut

### Community 137 - ".run_guarded"
Cohesion: 0.12
Nodes (4): ExportsBusy, QueryTooHeavy, export_slot(), _statement_timeout()

### Community 138 - "commissions/controller.py"
Cohesion: 0.06
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 145 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 146 - "get"
Cohesion: 0.07
Nodes (15): health(), metrics(), add_item(), available_months(), create(), create_service(), delete(), delete_service() (+7 more)

### Community 147 - "test_who_sees_and_changes_invoices"
Cohesion: 0.07
Nodes (38): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+30 more)

### Community 150 - "Actor"
Cohesion: 0.05
Nodes (18): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned() (+10 more)

### Community 152 - "datetime"
Cohesion: 0.07
Nodes (16): refresh_levels(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _marketing_client() (+8 more)

### Community 155 - "checklists/controller.py"
Cohesion: 0.14
Nodes (7): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), site_checklist_service()

### Community 158 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 161 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 162 - "modules/loaders/controller.py"
Cohesion: 0.12
Nodes (8): delete(), index(), options(), show(), update(), loader_service(), LoaderOptionOut, LoaderService

### Community 163 - "networks/controller.py"
Cohesion: 0.12
Nodes (11): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+3 more)

### Community 167 - "UserOut"
Cohesion: 0.11
Nodes (9): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+1 more)

### Community 171 - "Settings"
Cohesion: 0.06
Nodes (14): engine_options(), _google(), _mailer(), GeoLiteCountries, NoCountries, Settings, CeleryQueue, settings_for_tests() (+6 more)

### Community 174 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 175 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo

### Community 178 - "UserOut"
Cohesion: 0.10
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 184 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 191 - "receive"
Cohesion: 0.27
Nodes (3): cors(), preflight(), receive()

### Community 192 - "TaskQueue"
Cohesion: 0.09
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskMailQueue, TaskQueue

### Community 195 - "time"
Cohesion: 0.10
Nodes (7): Network, Segurança e limites, RateLimited, KeyValueBuffer, KeyValueIn, network_code(), receive_key_values()

### Community 196 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 197 - "ClientLoaderService"
Cohesion: 0.12
Nodes (7): delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService

### Community 204 - "ClientService"
Cohesion: 0.06
Nodes (27): audit(), cancel_owner(), change_status(), client(), client_options(), edit_client(), edit_client_image(), invite_owner() (+19 more)

### Community 210 - "internal/rewards/controller.py"
Cohesion: 0.07
Nodes (14): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+6 more)

### Community 215 - "LoaderOut"
Cohesion: 0.17
Nodes (3): create(), LoaderIn, LoaderOut

### Community 219 - ".classify"
Cohesion: 0.20
Nodes (4): classify(), classify_many(), site_options(), sites_of_member()

### Community 226 - "typing"
Cohesion: 0.07
Nodes (3): MemoryKeyValueBuffer, RedisKeyValueBuffer, test_redis_buffer_follows_the_worker_contract()

### Community 239 - "UnitOfWorkFactory"
Cohesion: 0.04
Nodes (10): CountryLookup, Bucket, UnitOfWorkFactory, is_cascade_shape(), safe_site_cascades(), site_cascades(), RewardCache, prices() (+2 more)

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2402 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **126 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `SupportTaskService`, `invoices/controller.py`, `roles/controller.py`, `DashboardService`, `Actor`, `contracts/controller.py`, `GamToolService`, `RewardCache`, `_month`, `commissions/controller.py`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `tasks/dto.py`, `PageOut`, `custom_metrics/controller.py`, `internal/loaders/service.py`, `Actor`, `goals/controller.py`, `shared/dto.py`, `get`, `mfa/controller.py`, `fastapi`, `ReportService`, `SiteService`, `modules/loaders/controller.py`, `networks/controller.py`, `goals/service.py`, `router.py`, `UserOut`, `mcm/controller.py`, `documents/controller.py`, `modules/price_rules/controller.py`, `AuthService`, `GoalService`, `networks/service.py`, `Services`, `UserOut`, `members/controller.py`, `clients`, `Actor`, `.__init__`, `account/controller.py`, `.__init__`, `SiteChecklistService`, `client_documents/controller.py`, `TaskQueue`, `invoices/controller.py`, `ClientLoaderService`, `documents/controller.py`, `ClientAdTagService`, `PageOut`, `ClientService`, `avant_core_access_models`, `image`, `results/dto.py`, `.__init__`, `internal/rewards/controller.py`, `sites/service.py`, `.__init__`, `google/controller.py`, `audit/controller.py`, `.__init__`, `reward_public/service.py`, `ad_tag_public/dto.py`, `.__init__`, `.__init__`, `.__init__`, `internal/ad_tags/service.py`, `.__init__`, `.__init__`?**
  _High betweenness centrality (0.106) - this node is a cross-community bridge._
- **Are the 172 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 172 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `invoices/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10953058321479374 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `SupportTaskService`, `invoices/controller.py`, `tasks/controller.py`, `DashboardService`, `Actor`, `contracts/controller.py`, `GamToolService`, `goals/controller.py`, `RewardCache`, `roles/controller.py`, `_month`, `AdUnitOut`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `GoalTemplateOut`, `get`, `tasks/dto.py`, `internal/loaders/service.py`, `PageOut`, `UUID`, `shared/dto.py`, `checklists/controller.py`, `get`, `ReportService`, `RewardService`, `SiteService`, `modules/loaders/controller.py`, `networks/controller.py`, `goals/service.py`, `router.py`, `UserOut`, `mcm/controller.py`, `modules/price_rules/controller.py`, `GoalService`, `router.py`, `Services`, `members/controller.py`, `.page_saved`, `Actor`, `SiteChecklistService`, `ClientLoaderService`, `ClientAdTagService`, `clients`, `ClientService`, `avant_core_access_models`, `PriceRuleService`, `image`, `results/dto.py`, `internal/rewards/controller.py`, `.of`, `internal/rewards/controller.py`, `sites/service.py`, `LoaderOut`, `audit/controller.py`, `internal/ad_tags/service.py`?**
  _High betweenness centrality (0.088) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07441016333938294 - nodes in this community are weakly interconnected._