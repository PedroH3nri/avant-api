# Graph Report - wt-avant-api-seguranca  (2026-11-11)

## Corpus Check
- 377 files · ~121,159 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 8, .ttf 2, .toml 1)

## Summary
- 5336 nodes · 15037 edges · 257 communities (128 shown, 129 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2468 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `1fb64ccd`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- PublicRewardService
- conftest.py
- roles/controller.py
- DashboardService
- AlertService
- _member_client
- GamToolService
- avant_core_shared_clock
- steps
- schedules/controller.py
- Avant: models do MVP
- edit_client
- .trusted_uow
- GroupService
- PageOut
- AdTagService
- api_keys/controller.py
- InvitationOut
- security.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- test_mail_queue.py
- dashboard_templates/controller.py
- invoice_pdf.py
- image_response
- clean_code.py
- ClientPriceRuleService
- mfa/controller.py
- currencies/controller.py
- ReportService
- RateLimited
- forget_pages
- session-start.sh
- avant-api
- test_price_rules.py
- MemberOut
- modules/ad_tags/dto.py
- time
- mcm/controller.py
- _staff
- test_alerts.py
- PriceRuleService
- Services
- uuid
- views/controller.py
- clients
- client_notes/controller.py
- .run_guarded
- modules/rewards/service.py
- edit
- PillowImageProcessor
- members/controller.py
- test_api_keys.py
- ItemsOut
- main.py
- RewardService
- account/controller.py
- documents/controller.py
- RedisRewardCache
- MemberService
- auth/controller.py
- main.py
- export.py
- Limiter
- ClientDocumentService
- ClientAdTagService
- checklists/dto.py
- avant-api
- modules/rewards/controller.py
- conftest.py
- .of
- test_reward_public.py
- .of_details
- costs/controller.py
- errors.py
- UnitOfWorkFactory
- events.py
- test_dashboards.py
- AdTagOut
- RewardIn
- sites/controller.py
- Avant: grupos na Empresa e imagem da Empresa
- limits.py
- Groone Avant: contexto do projeto
- DocumentOut
- test_events.py
- google/controller.py
- audit/controller.py
- events/controller.py
- reward_public/service.py
- invoices/service.py
- ad_tag_public/service.py
- RateLimited
- updates
- Avant: repositório e plano do MVP
- tasks/controller.py
- MemoryCounter
- contracts/controller.py
- modules/price_rules/controller.py
- test_account.py
- CapturingMailer
- SiteService
- client_documents/controller.py
- commissions/controller.py
- TaskDetailOut
- tasks/dto.py
- Arquitetura do MVP do Avant
- checklists
- GoalService
- get
- _csrf
- ad_tag_public/dto.py
- pydantic
- .uow
- datetime
- checklists/controller.py
- Counter
- company/controller.py
- UUID
- images.py
- networks/controller.py
- reports/dependencies.py
- members/dto.py
- router.py
- PriceRuleHistoryOut
- google/controller.py
- Avant: conexão com o GAM
- settings_for_tests
- Avant: conexão com o GAM
- AdTagUnitDayOut
- commissions/controller.py
- profile/controller.py
- ExportsBusy
- image_response
- document_response
- BaseModel
- settings_for_tests
- show
- .__init__
- AdTagHealthOut
- postgres
- RewardStyleIO
- test_google_link_and_login
- key_values/controller.py
- modules/loaders/service.py
- LoaderService
- clients
- UUID
- Actor
- internal/rewards/controller.py
- sites_of_member
- .of
- metrics
- .__init__
- leave
- reward_buffer.py
- commissions/dependencies.py
- MfaService
- .approve
- Settings
- .__init__
- Actor
- TaskPatchIn
- UnitOfWorkFactory
- .of
- mcm/service.py
- source_files
- MemoryRewardBuffer
- metrics

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 222 edges
2. `PageOut` - 193 edges
3. `_csrf()` - 184 edges
4. `_onboard_owner()` - 179 edges
5. `get()` - 171 edges
6. `Services` - 167 edges
7. `UnitOfWorkFactory` - 163 edges
8. `_staff()` - 81 edges
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
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/modules/internal/people/controller.py

## Import Cycles
- None detected.

## Communities (257 total, 129 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.15
Nodes (9): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body() (+1 more)

### Community 1 - "conftest.py"
Cohesion: 0.13
Nodes (10): invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut, ReturnedOut, ReturnIn (+2 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.11
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "_member_client"
Cohesion: 0.07
Nodes (24): _membership_ids(), test_groups_lifecycle(), _assert_denied(), _queue(), test_cost_writes_need_permission(), test_documents_need_company_edit(), test_member_writes_need_permission(), test_network_sync_and_disconnect_need_permission() (+16 more)

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (19): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+11 more)

### Community 8 - "steps"
Cohesion: 0.07
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, jobs (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.08
Nodes (25): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+17 more)

### Community 11 - "edit_client"
Cohesion: 0.18
Nodes (16): run_password_reset_tasks(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable() (+8 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+6 more)

### Community 14 - "PageOut"
Cohesion: 0.06
Nodes (9): networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, page_out(), PageOut (+1 more)

### Community 15 - "AdTagService"
Cohesion: 0.11
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "security.py"
Cohesion: 0.07
Nodes (19): CompanyChanged, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor() (+11 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "test_mail_queue.py"
Cohesion: 0.11
Nodes (9): RecordingQueue, _account(), _NoDatabase, _NoMail, _services(), test_forgot_password_only_queues_the_normalized_email(), test_forgot_route_never_sends_the_link_itself(), test_forgot_route_queues_without_database_or_mail_in_every_env() (+1 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), roles(), set_home(), show(), update(), DashboardTemplateIn (+5 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.18
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "ClientPriceRuleService"
Cohesion: 0.08
Nodes (14): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+6 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (7): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut

### Community 29 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.05
Nodes (36): catalog(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+28 more)

### Community 31 - "RateLimited"
Cohesion: 0.09
Nodes (4): RateLimited, BucketResult, BucketRule, prices()

### Community 32 - "forget_pages"
Cohesion: 0.12
Nodes (5): create(), forget_pages(), create(), RewardClientOut, RewardIn

### Community 36 - "test_price_rules.py"
Cohesion: 0.12
Nodes (28): FixedCountries, _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _offerwall_unit(), _present() (+20 more)

### Community 37 - "MemberOut"
Cohesion: 0.10
Nodes (8): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut, RoleRefOut

### Community 38 - "modules/ad_tags/dto.py"
Cohesion: 0.09
Nodes (12): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagDraftIO, AdTagHealthDayOut, AdTagIn, AdTagLiveOut (+4 more)

### Community 39 - "time"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 40 - "mcm/controller.py"
Cohesion: 0.14
Nodes (6): confirm_network(), register_network(), reject_network(), unassigned_networks(), McmService, NetworkOut

### Community 41 - "_staff"
Cohesion: 0.12
Nodes (14): _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads() (+6 more)

### Community 42 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company()

### Community 43 - "PriceRuleService"
Cohesion: 0.12
Nodes (11): cascade_hours(), history(), hours(), index(), set_floor(), settings(), show(), sites() (+3 more)

### Community 45 - "Services"
Cohesion: 0.04
Nodes (20): Services, get_services(), known_companies(), cost_service(), google_service(), group_service(), health_service(), client_ad_tag_service() (+12 more)

### Community 46 - "uuid"
Cohesion: 0.08
Nodes (38): _csrf(), _checkouts(), test_report_requests_use_few_connections(), query(), test_busy_export_answers_503_with_retry_after(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run(), _day() (+30 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 49 - "clients"
Cohesion: 0.10
Nodes (3): Modelo de dados, clients(), ClientRefOut

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 52 - "modules/rewards/service.py"
Cohesion: 0.10
Nodes (9): metrics(), RewardAnswerOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO, RewardLeadOut, RewardMetricsOut, RewardQuestionIn (+1 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (16): API first e chaves de API, Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa (+8 more)

### Community 54 - "PillowImageProcessor"
Cohesion: 0.08
Nodes (18): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness() (+10 more)

### Community 55 - "members/controller.py"
Cohesion: 0.10
Nodes (11): edit(), index(), options(), remove(), set_permissions(), show(), member_service(), MemberDetailOut (+3 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.33
Nodes (9): _bearer(), _create(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit() (+1 more)

### Community 57 - "ItemsOut"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "main.py"
Cohesion: 0.10
Nodes (7): configure_logging(), _is_docs_page(), observe(), _route_template(), check_fetch_site(), create_app(), public_price_floor_service()

### Community 59 - "RewardService"
Cohesion: 0.12
Nodes (12): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+4 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "documents/controller.py"
Cohesion: 0.11
Nodes (7): documents(), download(), upload(), document_service(), DocumentService, document_response(), document_upload()

### Community 62 - "RedisRewardCache"
Cohesion: 0.14
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "MemberService"
Cohesion: 0.15
Nodes (3): site_checklist_service(), ChecklistDetailOut, SiteChecklistService

### Community 64 - "auth/controller.py"
Cohesion: 0.08
Nodes (16): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+8 more)

### Community 65 - "main.py"
Cohesion: 0.11
Nodes (14): JsonFormatter, _BrokenAuthService, _rendered(), test_docs_are_closed_in_production(), test_every_response_has_the_content_security_policy(), test_every_response_has_the_security_headers(), test_invalid_bearer_is_limited_per_ip_before_the_database(), counting() (+6 more)

### Community 68 - "export.py"
Cohesion: 0.08
Nodes (13): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+5 more)

### Community 69 - "Limiter"
Cohesion: 0.10
Nodes (10): Limiter, Rule, _attempt_round(), _BrokenReleaseCounter, _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter() (+2 more)

### Community 71 - "ClientAdTagService"
Cohesion: 0.09
Nodes (13): AdTagOut, create(), delete(), health(), index(), publish(), restore(), set_active() (+5 more)

### Community 72 - "checklists/dto.py"
Cohesion: 0.14
Nodes (6): ChecklistMarkIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "modules/rewards/controller.py"
Cohesion: 0.21
Nodes (3): exposition(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 75 - "conftest.py"
Cohesion: 0.14
Nodes (6): client(), engine(), mailer(), _template(), test_goal_progress_routes(), test_goal_templates_and_role_goal()

### Community 76 - ".of"
Cohesion: 0.13
Nodes (6): service_account(), network_service(), NetworkIn, ServiceAccountOut, SyncRunOut, capped()

### Community 77 - "test_reward_public.py"
Cohesion: 0.11
Nodes (17): _buffer(), _cascade_reward(), test_events_and_leads_go_to_the_buffer(), test_icon_route_has_the_ip_limit(), test_public_config_is_cached_and_cleared(), test_reward_page_has_cascade_for_rewards_block(), test_reward_page_has_no_cascade_for_other_country(), test_reward_page_ignores_malformed_cascade_cache() (+9 more)

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "errors.py"
Cohesion: 0.15
Nodes (8): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), masked_path()

### Community 81 - "UnitOfWorkFactory"
Cohesion: 0.05
Nodes (11): results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut (+3 more)

### Community 82 - "events.py"
Cohesion: 0.07
Nodes (10): channel(), EventSource, NoEvents, _parse(), sse(), StreamLimiter, events(), event_service() (+2 more)

### Community 83 - "test_dashboards.py"
Cohesion: 0.14
Nodes (19): test_change_password_and_sessions(), _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit() (+11 more)

### Community 86 - "sites/controller.py"
Cohesion: 0.19
Nodes (7): classify(), classify_many(), MemberSitesIn, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.20
Nodes (9): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Imagem da Empresa, Issues, Modelo de dados, Regras, Resumo (+1 more)

### Community 88 - "limits.py"
Cohesion: 0.10
Nodes (3): TooManyAttempts, RedisCounter, test_redis_decr_without_key_creates_nothing()

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 92 - "test_events.py"
Cohesion: 0.17
Nodes (6): create_service(), services(), update_service(), InvoiceServiceIn, InvoiceServiceOut, InvoiceService

### Community 94 - "google/controller.py"
Cohesion: 0.07
Nodes (6): GoogleUnavailable, google_callback(), google_start(), google_status(), google_unlink(), GoogleService

### Community 95 - "audit/controller.py"
Cohesion: 0.21
Nodes (3): index(), audit_service(), AuditService

### Community 97 - "reward_public/service.py"
Cohesion: 0.09
Nodes (15): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicRewardPriceOut (+7 more)

### Community 98 - "invoices/service.py"
Cohesion: 0.12
Nodes (4): CommissionMonthOut, CommissionSettingsIn, dollars(), WindowMonthOut

### Community 102 - "ad_tag_public/service.py"
Cohesion: 0.06
Nodes (13): RewardBuffer, config(), page_views(), preflight(), public_ad_tag_service(), PageViewBlockIn, PageViewIn, PublicAdTagOut (+5 more)

### Community 123 - "RateLimited"
Cohesion: 0.19
Nodes (5): MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 127 - "updates"
Cohesion: 0.12
Nodes (15): patterns, update-types, dependencias, imagens, dependency-name, patterns, interval, updates (+7 more)

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 130 - "tasks/controller.py"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 132 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 133 - "modules/price_rules/controller.py"
Cohesion: 0.22
Nodes (16): price_rule_service(), CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn (+8 more)

### Community 135 - "CapturingMailer"
Cohesion: 0.09
Nodes (36): CapturingMailer, Sent, test_change_password_attempts_are_limited(), _error_code(), _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_deployed_cookies_use_the_host_prefix() (+28 more)

### Community 136 - "SiteService"
Cohesion: 0.14
Nodes (6): ad_units(), link(), unlinked(), AdUnitOut, AdUnitPatchIn, SiteService

### Community 137 - "client_documents/controller.py"
Cohesion: 0.17
Nodes (5): approve(), documents(), download(), reject(), client_document_service()

### Community 138 - "commissions/controller.py"
Cohesion: 0.22
Nodes (3): update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 139 - "TaskDetailOut"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 142 - "tasks/dto.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "checklists"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 145 - "GoalService"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+10 more)

### Community 146 - "get"
Cohesion: 0.07
Nodes (16): health(), add_item(), available_months(), create(), delete(), delete_service(), get(), issue() (+8 more)

### Community 147 - "_csrf"
Cohesion: 0.07
Nodes (31): _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it() (+23 more)

### Community 150 - ".uow"
Cohesion: 0.06
Nodes (4): create(), update(), SavedReportIn, SavedReportOut

### Community 152 - "datetime"
Cohesion: 0.07
Nodes (14): refresh_levels(), _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites() (+6 more)

### Community 155 - "checklists/controller.py"
Cohesion: 0.16
Nodes (7): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistNoteIn

### Community 160 - "company/controller.py"
Cohesion: 0.08
Nodes (13): edit(), edit_fiscal(), edit_image(), fiscal(), image(), remove_image(), show(), company_service() (+5 more)

### Community 161 - "UUID"
Cohesion: 0.22
Nodes (3): assign_sites(), members(), SiteMemberOut

### Community 162 - "images.py"
Cohesion: 0.16
Nodes (5): delete(), index(), show(), update(), loader_service()

### Community 163 - "networks/controller.py"
Cohesion: 0.12
Nodes (9): connect(), disconnect(), index(), options(), show(), sync(), sync_runs(), NetworkDetailOut (+1 more)

### Community 164 - "reports/dependencies.py"
Cohesion: 0.15
Nodes (4): set_settings(), settings(), CommissionSettingsOut, CommissionService

### Community 167 - "router.py"
Cohesion: 0.12
Nodes (9): disable(), enable(), reset_mfa(), users(), PersonOut, PeopleService, person_out(), CompanyRefOut (+1 more)

### Community 171 - "google/controller.py"
Cohesion: 0.08
Nodes (8): SessionCookies, new_verifier(), get_cookies(), get_session_auth(), GoogleStatusOut, verify(), client_info(), test_closing_deployed_cookies_keeps_them_secure()

### Community 172 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo

### Community 174 - "settings_for_tests"
Cohesion: 0.28
Nodes (5): settings_for_tests(), test_api_does_not_start_without_redis_or_queue_in_any_env(), test_many_processes_need_the_prometheus_directory(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 177 - "commissions/controller.py"
Cohesion: 0.15
Nodes (7): adjust(), create_rule(), delete_rule(), person(), rules(), AdjustmentIn, MonthIn

### Community 178 - "profile/controller.py"
Cohesion: 0.08
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 180 - "image_response"
Cohesion: 0.27
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 183 - "document_response"
Cohesion: 0.17
Nodes (5): _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 184 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 185 - "settings_for_tests"
Cohesion: 0.25
Nodes (3): ad_units(), RewardAdUnitGroupOut, RewardAdUnitOut

### Community 188 - ".__init__"
Cohesion: 0.19
Nodes (4): forget_cascades(), forget_floors(), forget_rule(), forget_site()

### Community 191 - "postgres"
Cohesion: 0.33
Nodes (6): POSTGRES_PASSWORD, env, image, options, ports, postgres

### Community 192 - "RewardStyleIO"
Cohesion: 0.09
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskMailQueue, TaskQueue

### Community 194 - "test_google_link_and_login"
Cohesion: 0.57
Nodes (5): _google_round(), _login(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 195 - "key_values/controller.py"
Cohesion: 0.06
Nodes (11): Network, Segurança e limites, KeyValueBuffer, MemoryKeyValueBuffer, RedisKeyValueBuffer, cors(), preflight(), receive() (+3 more)

### Community 197 - "LoaderService"
Cohesion: 0.12
Nodes (7): delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService

### Community 201 - "clients"
Cohesion: 0.18
Nodes (3): mine(), _month(), MyCommissionsOut

### Community 204 - "Actor"
Cohesion: 0.05
Nodes (32): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), edit_client() (+24 more)

### Community 210 - "internal/rewards/controller.py"
Cohesion: 0.08
Nodes (14): delete(), delete_lead(), export_leads(), index(), leads(), set_active(), set_icon(), show() (+6 more)

### Community 215 - ".of"
Cohesion: 0.20
Nodes (4): create(), LoaderIn, LoaderOut, LoaderService

### Community 226 - "Settings"
Cohesion: 0.04
Nodes (14): engine_options(), _google(), _mailer(), GeoLiteCountries, NoCountries, GoogleAuth, RedisRewardBuffer, Settings (+6 more)

### Community 231 - "Actor"
Cohesion: 0.13
Nodes (4): create(), index(), site_options(), SiteListOut

### Community 239 - "UnitOfWorkFactory"
Cohesion: 0.04
Nodes (9): CountryLookup, Bucket, UnitOfWorkFactory, is_cascade_shape(), safe_site_cascades(), site_cascades(), RewardCache, PublicPriceFloorsOut (+1 more)

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2403 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **129 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `SupportTaskService`, `conftest.py`, `roles/controller.py`, `DashboardService`, `AlertService`, `contracts/controller.py`, `GamToolService`, `avant_core_shared_clock`, `modules/price_rules/controller.py`, `.__init__`, `schedules/controller.py`, `TaskDetailOut`, `SiteService`, `GroupService`, `PageOut`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `tasks/dto.py`, `custom_metrics/controller.py`, `InvitationOut`, `pydantic`, `.uow`, `dashboard_templates/controller.py`, `ClientPriceRuleService`, `currencies/controller.py`, `ReportService`, `company/controller.py`, `networks/controller.py`, `reports/dependencies.py`, `MemberOut`, `modules/ad_tags/dto.py`, `router.py`, `mcm/controller.py`, `views/controller.py`, `client_notes/controller.py`, `profile/controller.py`, `members/controller.py`, `ItemsOut`, `RewardService`, `account/controller.py`, `documents/controller.py`, `.__init__`, `MemberService`, `auth/controller.py`, `RewardStyleIO`, `.__init__`, `modules/loaders/service.py`, `LoaderService`, `ClientDocumentService`, `ClientAdTagService`, `checklists/dto.py`, `Actor`, `.of`, `costs/controller.py`, `UnitOfWorkFactory`, `.__init__`, `RewardIn`, `sites/controller.py`, `.of`, `test_events.py`, `.__init__`, `google/controller.py`, `audit/controller.py`, `MfaService`, `reward_public/service.py`, `invoices/service.py`, `ad_tag_public/service.py`, `mcm/service.py`, `.__init__`, `.__init__`, `.__init__`, `RewardCache`, `.__init__`?**
  _High betweenness centrality (0.115) - this node is a cross-community bridge._
- **Are the 173 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 173 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `conftest.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1330049261083744 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `conftest.py`, `tasks/controller.py`, `DashboardService`, `AlertService`, `contracts/controller.py`, `GamToolService`, `avant_core_shared_clock`, `modules/price_rules/controller.py`, `roles/controller.py`, `schedules/controller.py`, `TaskDetailOut`, `.trusted_uow`, `GroupService`, `tasks/dto.py`, `AdTagService`, `api_keys/controller.py`, `checklists`, `GoalService`, `get`, `InvitationOut`, `.update`, `checklists/controller.py`, `ClientPriceRuleService`, `ReportService`, `images.py`, `networks/controller.py`, `MemberOut`, `modules/ad_tags/dto.py`, `router.py`, `mcm/controller.py`, `PriceRuleHistoryOut`, `PriceRuleService`, `Services`, `SiteService`, `Actor`, `clients`, `client_notes/controller.py`, `members/controller.py`, `RewardService`, `MemberService`, `modules/loaders/service.py`, `LoaderService`, `ClientAdTagService`, `checklists/dto.py`, `Actor`, `.of`, `costs/controller.py`, `UnitOfWorkFactory`, `internal/rewards/controller.py`, `AdTagOut`, `RewardIn`, `sites/controller.py`, `.of`, `test_events.py`, `audit/controller.py`, `Actor`, `mcm/service.py`?**
  _High betweenness centrality (0.089) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.1141025641025641 - nodes in this community are weakly interconnected._