# Graph Report - avant-api  (2026-11-11)

## Corpus Check
- 374 files · ~118,190 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 5235 nodes · 14746 edges · 255 communities (134 shown, 121 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2422 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `6f8eeea1`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- PublicRewardService
- test_alerts.py
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
- .uow
- inventory/dto.py
- AdTagService
- api_keys/controller.py
- PageOut
- security.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- container.py
- goals/controller.py
- verify
- networks/service.py
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
- AdTagUnitDayOut
- PublicAdTagService
- ProfileService
- test_gam_tools.py
- documents/controller.py
- modules/price_rules/controller.py
- PriceRuleSiteOut
- Services
- _csrf
- networks/service.py
- .page
- download
- Services
- DomainError
- MemoryCounter
- edit
- test_company_image.py
- members/controller.py
- typing
- clients
- google.py
- modules/rewards/service.py
- account/controller.py
- client_documents/controller.py
- Actor
- commissions/controller.py
- SessionCookies
- install
- invoices/controller.py
- export.py
- limits.py
- test_hardening.py
- ClientAdTagService
- checklists/dto.py
- avant-api
- networks/controller.py
- .of
- test_reward_public.py
- PriceRuleService
- image
- ClientDocumentsOut
- UnitOfWorkFactory
- events.py
- uuid
- .of
- internal/rewards/controller.py
- sites/service.py
- Avant: grupos na Empresa e imagem da Empresa
- tasks/controller.py
- Groone Avant: contexto do projeto
- .assign
- LoaderService
- google/controller.py
- PublicRewardService
- download
- reward_public/service.py
- dollars
- ad_tag_public/dto.py
- MemoryBucket
- updates
- Avant: repositório e plano do MVP
- PriceRuleConfigIn
- Settings
- contracts/controller.py
- RewardCache
- .page
- test_staff_without_permission_and_other_clients
- ad_units
- to_csv
- PriceRuleHourOut
- SupportTaskService
- Arquitetura do MVP do Avant
- test_mfa.py
- GoalService
- InvoiceService
- test_who_sees_and_changes_invoices
- middleware.py
- Actor
- Actor
- .__init__
- GoalTemplateIn
- checklists/controller.py
- goals/dto.py
- CompanyService
- SiteService
- modules/loaders/controller.py
- McmService
- image_response
- RoleGoalOut
- ad_tag_public/service.py
- UserOut
- PayeeDetailsOut
- test_report_export.py
- image
- team
- Avant: conexão com o GAM
- Actor
- create
- profile/controller.py
- api_keys/controller.py
- health/controller.py
- SupportTaskService
- .of
- .of
- test_permissions_on_keys
- AdTagHealthOut
- networks/controller.py
- receive
- TaskQueue
- ci.yml
- RateLimited
- package.json
- ClientLoaderService
- CascadeHourOut
- ClientService
- rewards/http.py
- RewardStyleIO
- show
- gam_tools/dependencies.py
- forget_tags
- create
- SiteListOut
- modules/loaders/dto.py
- .to_data
- create
- internal/price_rules/dto.py
- shared/dto.py
- logs.py
- LoaderOptionOut
- document_response
- PublicPriceFloorService
- Empresa e equipe
- ad_tag_public/dependencies.py
- modules/ad_tags/dependencies.py
- checklists/dependencies.py
- inventory/dependencies.py
- internal/rewards/dependencies.py
- modules/rewards/dependencies.py
- _BrokenAuthService
- .to_change

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 213 edges
2. `PageOut` - 193 edges
3. `_csrf()` - 181 edges
4. `_onboard_owner()` - 173 edges
5. `get()` - 171 edges
6. `UnitOfWorkFactory` - 163 edges
7. `Services` - 161 edges
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

## Communities (255 total, 121 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.12
Nodes (10): page_views(), preflight(), client_address(), cors(), events(), icon(), leads(), page() (+2 more)

### Community 1 - "test_alerts.py"
Cohesion: 0.11
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "_member_client"
Cohesion: 0.10
Nodes (17): _membership_ids(), test_groups_lifecycle(), _assert_denied(), test_cost_writes_need_permission(), test_documents_need_company_edit(), test_member_writes_need_permission(), test_network_sync_and_disconnect_need_permission(), test_role_writes_need_permission() (+9 more)

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (19): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+11 more)

### Community 7 - "goals/controller.py"
Cohesion: 0.22
Nodes (3): delete_template(), role_goals(), set_role_goal()

### Community 8 - "steps"
Cohesion: 0.08
Nodes (25): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, test, env (+17 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (21): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+13 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.11
Nodes (8): templates(), networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, PageOut

### Community 15 - "AdTagService"
Cohesion: 0.12
Nodes (11): delete(), health(), index(), publish(), restore(), set_active(), show(), units() (+3 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.16
Nodes (5): create(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.09
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService, InvitationOut

### Community 18 - "security.py"
Cohesion: 0.07
Nodes (21): CsrfFailed, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company(), get_actor(), get_auth() (+13 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "container.py"
Cohesion: 0.04
Nodes (10): GeoLiteCountries, NoCountries, KeyValueBuffer, MemoryRewardBuffer, RedisRewardBuffer, RewardBuffer, CeleryQueue, RecordingQueue (+2 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "networks/service.py"
Cohesion: 0.14
Nodes (4): NetworkIn, ServiceAccountOut, SyncRunOut, enqueue_sync()

### Community 26 - "clean_code.py"
Cohesion: 0.14
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "get"
Cohesion: 0.09
Nodes (16): health(), metrics(), get(), cascade_hours(), history(), hours(), index(), set_floor() (+8 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (8): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut, MfaService

### Community 29 - "fastapi"
Cohesion: 0.09
Nodes (7): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService, event_service()

### Community 30 - "reports/service.py"
Cohesion: 0.04
Nodes (26): QueryTooHeavy, query_batch(), templates(), report_service(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut (+18 more)

### Community 31 - "CapturingMailer"
Cohesion: 0.08
Nodes (38): CapturingMailer, Sent, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login() (+30 more)

### Community 32 - "RewardService"
Cohesion: 0.08
Nodes (13): create(), delete(), delete_lead(), export_leads(), index(), leads(), set_active(), set_icon() (+5 more)

### Community 36 - "test_price_rules.py"
Cohesion: 0.10
Nodes (32): _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _cascade_rule(), _cascade_site(), _company_of() (+24 more)

### Community 39 - "PublicAdTagService"
Cohesion: 0.12
Nodes (3): config(), PageViewIn, PublicAdTagService

### Community 40 - "ProfileService"
Cohesion: 0.24
Nodes (4): edit_appearance(), AppearanceIn, AppearanceOut, ProfileService

### Community 41 - "test_gam_tools.py"
Cohesion: 0.13
Nodes (14): _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads() (+6 more)

### Community 42 - "documents/controller.py"
Cohesion: 0.15
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "modules/price_rules/controller.py"
Cohesion: 0.14
Nodes (10): cascade_hours(), index(), set_floor(), settings(), sites(), update_blocks(), update_config(), update_settings() (+2 more)

### Community 45 - "Services"
Cohesion: 0.03
Nodes (14): Services, get_services(), account_service(), api_key_service(), company_service(), cost_service(), client_ad_tag_service(), client_note_service() (+6 more)

### Community 46 - "_csrf"
Cohesion: 0.08
Nodes (39): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _csrf(), _checkouts(), test_report_requests_use_few_connections() (+31 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 49 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (8): add(), delete(), edit(), notes(), ClientNoteIn, ClientNoteOut, NotePersonOut, ClientNoteService

### Community 51 - "DomainError"
Cohesion: 0.22
Nodes (5): CompanyChanged, ExportsBusy, NoActiveCompany, test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 52 - "MemoryCounter"
Cohesion: 0.09
Nodes (12): ad_units(), RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut (+4 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "test_company_image.py"
Cohesion: 0.08
Nodes (15): _check_jpeg_size(), PillowImageProcessor, client(), engine(), mailer(), _jpeg(), _put_image(), _sharpness() (+7 more)

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+6 more)

### Community 56 - "typing"
Cohesion: 0.09
Nodes (7): MemoryKeyValueBuffer, RedisKeyValueBuffer, _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 57 - "clients"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "google.py"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 59 - "modules/rewards/service.py"
Cohesion: 0.13
Nodes (3): metrics(), metrics(), RewardMetricsOut

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (12): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), ChangePasswordIn, ForgotPasswordIn (+4 more)

### Community 61 - "client_documents/controller.py"
Cohesion: 0.23
Nodes (3): client_document_service(), ClientDocumentsOut, RejectDocumentIn

### Community 62 - "Actor"
Cohesion: 0.14
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "commissions/controller.py"
Cohesion: 0.09
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 64 - "SessionCookies"
Cohesion: 0.06
Nodes (21): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), get_invitation(), login(), me() (+13 more)

### Community 65 - "install"
Cohesion: 0.21
Nodes (9): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), masked_path() (+1 more)

### Community 66 - "invoices/controller.py"
Cohesion: 0.13
Nodes (6): edit_fiscal(), edit_image(), fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 68 - "export.py"
Cohesion: 0.13
Nodes (3): dimension_text(), _csv_cell(), _xlsx_cell()

### Community 69 - "limits.py"
Cohesion: 0.06
Nodes (10): TooManyAttempts, Counter, Limiter, RedisCounter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round() (+2 more)

### Community 70 - "test_hardening.py"
Cohesion: 0.20
Nodes (9): _rendered(), test_api_key_never_reaches_the_log(), test_docs_are_closed_in_production(), test_every_response_has_the_content_security_policy(), test_every_response_has_the_security_headers(), test_invalid_bearer_is_limited_per_ip_before_the_database(), test_redis_down_is_a_503_not_a_500(), test_swagger_page_keeps_working_without_the_policy() (+1 more)

### Community 71 - "ClientAdTagService"
Cohesion: 0.09
Nodes (11): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+3 more)

### Community 72 - "checklists/dto.py"
Cohesion: 0.09
Nodes (5): ChecklistMarkIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "networks/controller.py"
Cohesion: 0.14
Nodes (3): index(), NetworkDetailOut, NetworkService

### Community 76 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 77 - "test_reward_public.py"
Cohesion: 0.09
Nodes (20): FixedCountries, reward_cache_key(), _png(), _buffer(), _cascade_reward(), test_events_and_leads_go_to_the_buffer(), test_icon_route_has_the_ip_limit(), test_public_config_is_cached_and_cleared() (+12 more)

### Community 78 - "PriceRuleService"
Cohesion: 0.10
Nodes (5): set_status(), show(), PriceRuleDetailsOut, PriceRuleStatusIn, PriceRuleService

### Community 79 - "image"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 81 - "UnitOfWorkFactory"
Cohesion: 0.05
Nodes (10): UnitOfWorkFactory, results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, default_period() (+2 more)

### Community 82 - "events.py"
Cohesion: 0.06
Nodes (20): channel(), EventSource, _parse(), RedisEvents, sse(), StreamLimiter, events(), EventService (+12 more)

### Community 83 - "uuid"
Cohesion: 0.15
Nodes (11): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request() (+3 more)

### Community 84 - ".of"
Cohesion: 0.12
Nodes (4): forget_tag(), create(), AdTagCreateIn, AdTagOut

### Community 85 - "internal/rewards/controller.py"
Cohesion: 0.11
Nodes (12): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), set_active() (+4 more)

### Community 86 - "sites/service.py"
Cohesion: 0.19
Nodes (6): site_service(), AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

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
Cohesion: 0.13
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 94 - "google/controller.py"
Cohesion: 0.05
Nodes (12): GoogleUnavailable, GoogleAuth, new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), google_redirects() (+4 more)

### Community 95 - "PublicRewardService"
Cohesion: 0.08
Nodes (9): BucketRule, public_reward_service(), CachedPage, PublicPageOut, PublicRewardPriceOut, RewardEventsIn, RewardLeadIn, public_control_percent() (+1 more)

### Community 96 - "download"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 97 - "reward_public/service.py"
Cohesion: 0.27
Nodes (8): PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicQuestionOut, PublicRewardOut, PublicStyleOut, RewardEventIn, RewardLeadAnswerIn

### Community 98 - "dollars"
Cohesion: 0.13
Nodes (3): dollars(), AvailableMonthOut, InvoiceItemOut

### Community 102 - "ad_tag_public/dto.py"
Cohesion: 0.13
Nodes (6): PageViewBlockIn, PublicAdTagOut, PublicBlockOut, PublicLoaderOut, PublicMgidOut, PublicTagOut

### Community 123 - "MemoryBucket"
Cohesion: 0.16
Nodes (6): BucketResult, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 131 - "Settings"
Cohesion: 0.06
Nodes (11): engine_options(), _google(), _mailer(), NoEvents, MemoryCounter, MemoryRewardCache, Settings, create_app() (+3 more)

### Community 132 - "contracts/controller.py"
Cohesion: 0.06
Nodes (23): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, contract(), contract_networks() (+15 more)

### Community 133 - "RewardCache"
Cohesion: 0.10
Nodes (9): is_cascade_shape(), safe_site_cascades(), site_cascades(), RewardCache, PriceRuleSettingsIn, forget_cascades(), forget_floors(), forget_rule() (+1 more)

### Community 134 - ".page"
Cohesion: 0.12
Nodes (4): index(), audit_service(), AuditService, AuditOut

### Community 135 - "test_staff_without_permission_and_other_clients"
Cohesion: 0.38
Nodes (8): _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission(), test_staff_without_permission_and_other_clients()

### Community 136 - "ad_units"
Cohesion: 0.21
Nodes (3): ad_units(), link(), AdUnitOut

### Community 137 - "to_csv"
Cohesion: 0.27
Nodes (5): _header(), _metric_label(), _rows(), to_csv(), to_xlsx()

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.21
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+6 more)

### Community 145 - "GoalService"
Cohesion: 0.23
Nodes (3): template_options(), GoalTemplateOut, GoalService

### Community 146 - "InvoiceService"
Cohesion: 0.07
Nodes (24): add_item(), available_months(), create_service(), delete(), delete_service(), issue(), mine(), pay() (+16 more)

### Community 147 - "test_who_sees_and_changes_invoices"
Cohesion: 0.06
Nodes (37): _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it() (+29 more)

### Community 148 - "middleware.py"
Cohesion: 0.23
Nodes (3): _is_docs_page(), observe(), _route_template()

### Community 149 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), classify(), classify_many(), delete(), show(), unlinked()

### Community 150 - "Actor"
Cohesion: 0.04
Nodes (18): catalog(), create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index() (+10 more)

### Community 152 - ".__init__"
Cohesion: 0.07
Nodes (10): refresh_levels(), test_deployed_cookies_use_the_host_prefix(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check() (+2 more)

### Community 153 - "GoalTemplateIn"
Cohesion: 0.20
Nodes (3): create_template(), update_template(), GoalTemplateIn

### Community 155 - "checklists/controller.py"
Cohesion: 0.11
Nodes (13): add_note(), check(), checklist(), checklists(), delete_note(), edit_note(), mark(), months() (+5 more)

### Community 158 - "goals/dto.py"
Cohesion: 0.14
Nodes (4): mine(), GoalProgressOut, PersonGoalOut, RoleGoalIn

### Community 160 - "CompanyService"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 161 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 162 - "modules/loaders/controller.py"
Cohesion: 0.14
Nodes (8): delete(), index(), options(), show(), update(), loader_service(), LoaderOut, LoaderService

### Community 163 - "McmService"
Cohesion: 0.10
Nodes (9): confirm_network(), register_network(), reject_network(), unassigned_networks(), mcm_service(), ClientNetworkIn, McmCandidateOut, McmService (+1 more)

### Community 167 - "UserOut"
Cohesion: 0.14
Nodes (5): disable(), enable(), reset_mfa(), users(), PeopleService

### Community 171 - "test_report_export.py"
Cohesion: 0.28
Nodes (3): _result(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 174 - "team"
Cohesion: 0.16
Nodes (3): _month(), team(), TeamGoalsOut

### Community 175 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo

### Community 178 - "profile/controller.py"
Cohesion: 0.15
Nodes (4): edit_image(), image(), remove_image(), profile_service()

### Community 180 - "health/controller.py"
Cohesion: 0.17
Nodes (3): ready(), health_service(), HealthService

### Community 182 - "SupportTaskService"
Cohesion: 0.15
Nodes (4): tasks(), support_task_service(), TaskOut, SupportTaskService

### Community 183 - ".of"
Cohesion: 0.09
Nodes (11): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagDraftIO, AdTagHealthDayOut, AdTagIn, AdTagLiveOut, AdTagPublishIn (+3 more)

### Community 184 - ".of"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 186 - "test_permissions_on_keys"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 190 - "networks/controller.py"
Cohesion: 0.13
Nodes (8): connect(), disconnect(), options(), service_account(), show(), sync(), sync_runs(), capped()

### Community 191 - "receive"
Cohesion: 0.31
Nodes (3): cors(), preflight(), receive()

### Community 193 - "ci.yml"
Cohesion: 0.29
Nodes (6): jobs, name, on, pull_request, push, branches

### Community 195 - "RateLimited"
Cohesion: 0.13
Nodes (7): Network, Segurança e limites, RateLimited, Bucket, KeyValueIn, network_code(), receive_key_values()

### Community 196 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 197 - "ClientLoaderService"
Cohesion: 0.12
Nodes (6): delete(), index(), show(), update(), client_loader_service(), ClientLoaderService

### Community 198 - "CascadeHourOut"
Cohesion: 0.12
Nodes (3): history(), CascadeHourOut, PriceRuleHistoryOut

### Community 204 - "ClientService"
Cohesion: 0.04
Nodes (30): Modelo de dados, audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams() (+22 more)

### Community 210 - "rewards/http.py"
Cohesion: 0.18
Nodes (3): csv_response(), lead_filter(), period()

### Community 217 - "SiteListOut"
Cohesion: 0.18
Nodes (3): index(), site_options(), SiteListOut

### Community 222 - "internal/price_rules/dto.py"
Cohesion: 0.10
Nodes (6): CascadeTryOut, PriceRuleBlockOut, PriceRuleConfigOut, PriceRuleFloorIn, PriceRuleOut, PriceRuleSiteSummaryOut

### Community 223 - "shared/dto.py"
Cohesion: 0.06
Nodes (13): ClientMemberOut, ClientProfileOut, ClientRefOut, PersonOut, person_out(), CompanyRefOut, ContractClientRefOut, FiscalDataOut (+5 more)

### Community 239 - "PublicPriceFloorService"
Cohesion: 0.12
Nodes (5): CountryLookup, prices(), public_price_floor_service(), PublicPriceFloorsOut, PublicPriceFloorService

### Community 240 - "Empresa e equipe"
Cohesion: 0.50
Nodes (4): Company, Empresa e equipe, Invitation, Membership

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2371 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **121 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `test_alerts.py`, `roles/controller.py`, `DashboardService`, `Actor`, `RewardCache`, `.page`, `contracts/controller.py`, `GamToolService`, `_month`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `InvoiceService`, `custom_metrics/controller.py`, `PageOut`, `Actor`, `goals/controller.py`, `networks/service.py`, `checklists/controller.py`, `get`, `fastapi`, `mfa/controller.py`, `reports/service.py`, `CompanyService`, `RewardService`, `modules/loaders/controller.py`, `McmService`, `SiteService`, `tasks/dto.py`, `ad_tag_public/service.py`, `PublicAdTagService`, `UserOut`, `ProfileService`, `documents/controller.py`, `networks/service.py`, `Services`, `SupportTaskService`, `members/controller.py`, `.__init__`, `clients`, `modules/rewards/service.py`, `.__init__`, `account/controller.py`, `client_documents/controller.py`, `commissions/controller.py`, `SessionCookies`, `limits.py`, `ClientLoaderService`, `ClientAdTagService`, `networks/controller.py`, `ClientService`, `PriceRuleService`, `image`, `ClientDocumentsOut`, `.__init__`, `.of`, `internal/rewards/controller.py`, `sites/service.py`, `google/controller.py`, `shared/dto.py`, `.__init__`, `.__init__`, `.__init__`, `PublicRewardService`, `PublicPriceFloorService`, `.__init__`, `.__init__`, `.__init__`, `.__init__`?**
  _High betweenness centrality (0.122) - this node is a cross-community bridge._
- **Are the 166 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 166 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PublicRewardService` be split into smaller, more focused modules?**
  _Cohesion score 0.11931818181818182 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `inventory/dto.py` to `test_alerts.py`, `roles/controller.py`, `DashboardService`, `Actor`, `contracts/controller.py`, `.page`, `GamToolService`, `RewardCache`, `_month`, `.trusted_uow`, `.uow`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `security.py`, `InvoiceService`, `PageOut`, `Actor`, `networks/service.py`, `checklists/controller.py`, `get`, `reports/service.py`, `RewardService`, `SiteService`, `modules/loaders/controller.py`, `McmService`, `tasks/dto.py`, `UserOut`, `modules/price_rules/controller.py`, `PriceRuleSiteOut`, `.page`, `Actor`, `Services`, `api_keys/controller.py`, `SupportTaskService`, `members/controller.py`, `modules/rewards/service.py`, `networks/controller.py`, `ClientLoaderService`, `ClientAdTagService`, `networks/controller.py`, `ClientService`, `PriceRuleService`, `image`, `UnitOfWorkFactory`, `.of`, `internal/rewards/controller.py`, `sites/service.py`, `tasks/controller.py`, `SiteListOut`, `.page`, `.assign`, `shared/dto.py`?**
  _High betweenness centrality (0.098) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_alerts.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10582010582010581 - nodes in this community are weakly interconnected._