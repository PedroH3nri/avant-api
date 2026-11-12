# Graph Report - avant-api  (2026-11-12)

## Corpus Check
- 385 files · ~125,087 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 5471 nodes · 15479 edges · 260 communities (139 shown, 121 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2477 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `2ff5983f`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- PublicRewardService
- invoices/dto.py
- roles/controller.py
- DashboardService
- Actor
- conftest.py
- gam_tools/dto.py
- swagger_assets.py
- test
- _month
- Avant: models do MVP
- test_mfa.py
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
- .of
- mfa/controller.py
- fastapi
- ReportService
- test_reward_public.py
- RewardService
- session-start.sh
- avant-api
- test_price_rules.py
- PublicAdTagService
- floor_cache.py
- mcm/service.py
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
- accept
- modules/rewards/controller.py
- google/controller.py
- avant_core_access_models
- test_cache_down_does_not_break_the_page_or_the_save
- checklists/controller.py
- AuthService
- ContractService
- test_costs_results.py
- Actor
- export.py
- Limiter
- SupportTaskService
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
- ad_tag_public/dto.py
- limits.py
- test_account.py
- AdTagHealthOut
- .run_guarded
- sites/service.py
- .approve
- RedisCounter
- Groone Avant: contexto do projeto
- pydantic
- SiteChecklistService
- google/controller.py
- tasks/controller.py
- test_api.py
- reward_public/dto.py
- ClientDocumentOut
- auth/dto.py
- GamToolService
- updates
- contracts/controller.py
- Avant: repositório e plano do MVP
- .export_saved
- ContractOut
- test_dashboards.py
- RewardCache
- mine
- RedisKeyValueBuffer
- SiteDetailOut
- client_documents/controller.py
- commissions/controller.py
- ContractClientRefOut
- test_settings.py
- Arquitetura do MVP do Avant
- GoalTemplateOut
- tasks
- _staff
- internal/loaders/controller.py
- company/controller.py
- .build
- test_reward_public.py
- goals/controller.py
- CapturingMailer
- .of
- sites/controller.py
- GoalService
- networks/controller.py
- SiteService
- GAM
- reports/service.py
- UserOut
- main.py
- internal/loaders/service.py
- Avant: conexão com o GAM
- Actor
- PageOut
- document_response
- receive
- UserOut
- get
- RedisEvents
- network
- modules/loaders/controller.py
- BaseModel
- .page
- CompanyService
- AdTagVersionOut
- TaskQueue
- postgres
- templates
- key_values/controller.py
- delete_template
- package.json
- receive_key_values
- test_metrics.py
- sites/controller.py
- modules/loaders/dto.py
- Actor
- PriceRuleDetailsOut
- Actor
- image
- .start
- Counter
- O que já tem
- Suporte
- HealthService
- _BrokenAuthService
- RewardAdUnitGroupOut
- settings_for_tests
- remove_image
- TaskPatchIn
- _contract_fields
- UnitOfWorkFactory
- GamToolNetworkOut
- create
- _BrokenRedis
- NetworkService
- checklists/dependencies.py
- invalid_variable_names
- GeoLiteCountries
- mcm/dto.py
- .first_day

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 235 edges
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

## Communities (260 total, 121 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.09
Nodes (11): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body() (+3 more)

### Community 1 - "invoices/dto.py"
Cohesion: 0.06
Nodes (12): dollars(), create_service(), save_payment_details(), update_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOut (+4 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (28): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+20 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "conftest.py"
Cohesion: 0.07
Nodes (24): _membership_ids(), test_groups_lifecycle(), _assert_denied(), _queue(), test_cost_writes_need_permission(), test_documents_need_company_edit(), test_member_writes_need_permission(), test_network_sync_and_disconnect_need_permission() (+16 more)

### Community 6 - "gam_tools/dto.py"
Cohesion: 0.13
Nodes (3): GamStepOut, GamToolPersonOut, GamToolSiteOut

### Community 7 - "swagger_assets.py"
Cohesion: 0.12
Nodes (6): challenge(), ExpectedAsset, load_assets(), SwaggerAsset, SwaggerAssetChanged, test_changed_asset_stops_the_start()

### Community 8 - "test"
Cohesion: 0.07
Nodes (33): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, jobs (+25 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.12
Nodes (15): Acesso, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade, Invitation, MemberPermission (+7 more)

### Community 11 - "test_mfa.py"
Cohesion: 0.12
Nodes (23): run_password_reset_tasks(), _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites() (+15 more)

### Community 12 - ".trusted_uow"
Cohesion: 0.07
Nodes (14): add_item(), delete(), delete_service(), issue(), mine(), pay(), remove_item(), return_to_draft() (+6 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.12
Nodes (8): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, RevenueStatusOut

### Community 15 - "modules/ad_tags/dto.py"
Cohesion: 0.12
Nodes (11): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagHealthDayOut, AdTagIn, AdTagLiveOut, AdTagPublishIn (+3 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.05
Nodes (15): InvitationMailNotSent, invite(), staff(), staff_service(), StaffInviteIn, StaffService, cancel(), create_invitation() (+7 more)

### Community 18 - "security.py"
Cohesion: 0.06
Nodes (24): CompanyChanged, CsrfFailed, ExportsBusy, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site() (+16 more)

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
Nodes (24): client(), engine(), mailer(), memory_services(), Sent, MemoryCounter, MemoryKeyValueBuffer, MemoryRewardCache (+16 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.13
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.16
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 28 - "mfa/controller.py"
Cohesion: 0.07
Nodes (11): auth_service(), confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn (+3 more)

### Community 29 - "fastapi"
Cohesion: 0.13
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.05
Nodes (21): RateLimited, create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index() (+13 more)

### Community 31 - "test_reward_public.py"
Cohesion: 0.09
Nodes (27): browser(), MemoryRewardBuffer, _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _buffer() (+19 more)

### Community 32 - "RewardService"
Cohesion: 0.09
Nodes (5): create(), create(), RewardIn, RewardOut, RewardService

### Community 36 - "test_price_rules.py"
Cohesion: 0.11
Nodes (27): FixedCountries, _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _offerwall_unit(), _present() (+19 more)

### Community 37 - "PublicAdTagService"
Cohesion: 0.07
Nodes (12): ad_tag_cache_key(), Bucket, BucketResult, BucketRule, RewardBuffer, config(), page_views(), preflight() (+4 more)

### Community 38 - "floor_cache.py"
Cohesion: 0.12
Nodes (4): _recommended_models(), forget_cascades(), forget_floors(), forget_site()

### Community 39 - "mcm/service.py"
Cohesion: 0.13
Nodes (4): NetworkIn, ServiceAccountOut, SyncRunOut, enqueue_sync()

### Community 40 - "mcm/controller.py"
Cohesion: 0.13
Nodes (6): confirm_network(), register_network(), reject_network(), unassigned_networks(), McmService, NetworkOut

### Community 41 - "ClientService"
Cohesion: 0.05
Nodes (30): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), clients(), edit_client() (+22 more)

### Community 42 - "modules/loaders/controller.py"
Cohesion: 0.16
Nodes (3): create(), LoaderIn, LoaderOut

### Community 43 - "PriceRuleService"
Cohesion: 0.09
Nodes (13): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+5 more)

### Community 44 - "AdTagService"
Cohesion: 0.12
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 45 - "Services"
Cohesion: 0.03
Nodes (17): Services, EventSource, StreamLimiter, RedisRewardBuffer, get_services(), alert_service(), company_service(), currency_service() (+9 more)

### Community 46 - "test_reports.py"
Cohesion: 0.07
Nodes (49): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _csrf(), _onboard_owner(), _owner_invite() (+41 more)

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
Cohesion: 0.18
Nodes (6): ads_txt(), install(), run(), runs(), AdsTxtOut, GamToolRunOut

### Community 52 - "MemoryCounter"
Cohesion: 0.09
Nodes (12): RewardActiveIn, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO, RewardLeadOut (+4 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "download"
Cohesion: 0.12
Nodes (4): documents(), download(), upload(), DocumentService

### Community 55 - "MemberService"
Cohesion: 0.06
Nodes (16): options(), edit(), index(), leave(), options(), remove(), set_permissions(), show() (+8 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.18
Nodes (13): MemoryBucket, _bearer(), _create(), _exercise(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke() (+5 more)

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "accept"
Cohesion: 0.15
Nodes (6): accept(), company_image(), do_logout(), me(), set_active_company(), MeOut

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.11
Nodes (11): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+3 more)

### Community 60 - "google/controller.py"
Cohesion: 0.06
Nodes (15): SessionCookies, delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service() (+7 more)

### Community 61 - "avant_core_access_models"
Cohesion: 0.05
Nodes (11): cost_service(), document_service(), mcm_service(), results(), client_result_service(), ClientResultService, show(), result_service() (+3 more)

### Community 63 - "checklists/controller.py"
Cohesion: 0.13
Nodes (7): add_note(), check(), checklists(), delete_note(), edit_note(), mark(), months()

### Community 64 - "AuthService"
Cohesion: 0.10
Nodes (3): login(), LoginIn, AuthService

### Community 65 - "ContractService"
Cohesion: 0.12
Nodes (4): contract_networks(), remove_contract(), contract_service(), ContractService

### Community 66 - "test_costs_results.py"
Cohesion: 0.07
Nodes (12): refresh_levels(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _marketing_client() (+4 more)

### Community 67 - "Actor"
Cohesion: 0.12
Nodes (3): index(), client_reward_service(), ClientRewardService

### Community 68 - "export.py"
Cohesion: 0.08
Nodes (13): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+5 more)

### Community 69 - "Limiter"
Cohesion: 0.16
Nodes (8): Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_refused_reserve_never_touches_the_other_keys(), test_release_failure_does_not_break_a_good_attempt()

### Community 70 - "SupportTaskService"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 71 - "AdTagOut"
Cohesion: 0.09
Nodes (13): AdTagOut, create(), delete(), health(), index(), publish(), restore(), set_active() (+5 more)

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
Cohesion: 0.11
Nodes (13): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+5 more)

### Community 79 - "image"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "install"
Cohesion: 0.21
Nodes (9): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), masked_path() (+1 more)

### Community 81 - "ad_tag_public/dto.py"
Cohesion: 0.13
Nodes (5): PageViewBlockIn, PublicBlockOut, PublicLoaderOut, PublicMgidOut, PublicTagOut

### Community 82 - "limits.py"
Cohesion: 0.06
Nodes (7): TooManyAttempts, channel(), _parse(), sse(), RedisBucket, events(), test_stream_limiter_caps_each_person_and_the_process()

### Community 83 - "test_account.py"
Cohesion: 0.09
Nodes (24): _BrokenReleaseCounter, _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login() (+16 more)

### Community 85 - ".run_guarded"
Cohesion: 0.09
Nodes (3): QueryTooHeavy, ReportRowOut, _statement_timeout()

### Community 86 - "sites/service.py"
Cohesion: 0.21
Nodes (3): ad_units(), link(), AdUnitOut

### Community 87 - ".approve"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "RedisCounter"
Cohesion: 0.17
Nodes (4): RedisCounter, test_redis_decr_without_key_creates_nothing(), test_redis_limiter(), test_redis_down_is_a_503_not_a_500()

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 91 - "pydantic"
Cohesion: 0.18
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 92 - "SiteChecklistService"
Cohesion: 0.17
Nodes (3): checklist(), ChecklistDetailOut, SiteChecklistService

### Community 94 - "google/controller.py"
Cohesion: 0.04
Nodes (21): _google(), GoogleFailed, GoogleUnavailable, _claims(), GoogleAuth, GoogleOAuth, identity_from_id_token(), new_verifier() (+13 more)

### Community 95 - "tasks/controller.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 96 - "test_api.py"
Cohesion: 0.20
Nodes (12): _error_code(), test_cookies_are_always_secure_with_the_host_prefix(), test_csrf_is_required_for_writes(), test_every_write_route_refuses_another_site(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session() (+4 more)

### Community 97 - "reward_public/dto.py"
Cohesion: 0.13
Nodes (12): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicRewardPriceOut (+4 more)

### Community 102 - "auth/dto.py"
Cohesion: 0.17
Nodes (7): get_invitation(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginOut, image_url()

### Community 123 - "GamToolService"
Cohesion: 0.19
Nodes (3): gam_tool_service(), GamToolRunNetworkOut, GamToolService

### Community 127 - "updates"
Cohesion: 0.11
Nodes (17): patterns, patterns, update-types, acoes, dependencias, imagens, dependency-name, patterns (+9 more)

### Community 128 - "contracts/controller.py"
Cohesion: 0.20
Nodes (6): ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut, _network_ref()

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 131 - "ContractOut"
Cohesion: 0.20
Nodes (6): contract(), contracts(), edit_contract(), finish_contract(), new_contract(), ContractOut

### Community 132 - "test_dashboards.py"
Cohesion: 0.22
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 133 - "RewardCache"
Cohesion: 0.20
Nodes (15): price_rule_service(), CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn (+7 more)

### Community 134 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 137 - "client_documents/controller.py"
Cohesion: 0.13
Nodes (7): approve(), documents(), download(), reject(), ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 138 - "commissions/controller.py"
Cohesion: 0.06
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 139 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 142 - "test_settings.py"
Cohesion: 0.25
Nodes (7): load_settings(), _environment(), _refused_names(), test_api_starts_with_each_transport(), test_environment_name_changes_nothing(), test_missing_or_invalid_configuration_stops_the_api(), test_start_error_shows_names_and_never_values()

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 145 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 146 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 147 - "_staff"
Cohesion: 0.05
Nodes (38): _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it() (+30 more)

### Community 148 - "internal/loaders/controller.py"
Cohesion: 0.16
Nodes (7): delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService

### Community 149 - "company/controller.py"
Cohesion: 0.32
Nodes (4): CompanyDetailOut, CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 150 - ".build"
Cohesion: 0.14
Nodes (3): _mailer(), NoCountries, test_each_transport_builds_its_mailer()

### Community 152 - "test_reward_public.py"
Cohesion: 0.08
Nodes (20): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, _after_first_segment(), _jpeg(), _png(), _put_image() (+12 more)

### Community 153 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 155 - "CapturingMailer"
Cohesion: 0.15
Nodes (18): CapturingMailer, _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission() (+10 more)

### Community 161 - "sites/controller.py"
Cohesion: 0.19
Nodes (6): site_service(), AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 162 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 163 - "networks/controller.py"
Cohesion: 0.12
Nodes (9): connect(), disconnect(), options(), service_account(), show(), sync(), sync_runs(), network_service() (+1 more)

### Community 164 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 165 - "GAM"
Cohesion: 0.22
Nodes (8): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment, Segurança e limites, network_code()

### Community 166 - "reports/service.py"
Cohesion: 0.05
Nodes (16): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+8 more)

### Community 167 - "UserOut"
Cohesion: 0.10
Nodes (8): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out()

### Community 168 - "main.py"
Cohesion: 0.08
Nodes (6): _content_security_policy(), observe(), _route_template(), _are_proxy_addresses(), InvalidVariables, create_app()

### Community 172 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo

### Community 175 - "PageOut"
Cohesion: 0.07
Nodes (10): index(), audit_service(), AuditService, client_teams(), ClientMemberOut, AuditOut, CompanyRefOut, page_out() (+2 more)

### Community 177 - "receive"
Cohesion: 0.31
Nodes (3): cors(), preflight(), receive()

### Community 178 - "UserOut"
Cohesion: 0.07
Nodes (9): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService (+1 more)

### Community 179 - "get"
Cohesion: 0.07
Nodes (13): openapi(), swagger(), swagger_asset(), _swagger_page(), health(), available_months(), get(), payment_details() (+5 more)

### Community 182 - "network"
Cohesion: 0.24
Nodes (3): network(), GamToolClientOut, GamToolNetworkDetailOut

### Community 183 - "modules/loaders/controller.py"
Cohesion: 0.14
Nodes (8): delete(), index(), options(), show(), update(), loader_service(), LoaderOptionOut, LoaderService

### Community 184 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 186 - "CompanyService"
Cohesion: 0.13
Nodes (5): edit_fiscal(), edit_image(), fiscal(), show(), CompanyService

### Community 192 - "TaskQueue"
Cohesion: 0.09
Nodes (8): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, QueueUnavailable, TaskMailQueue, TaskQueue

### Community 193 - "postgres"
Cohesion: 0.33
Nodes (6): POSTGRES_PASSWORD, env, image, options, ports, postgres

### Community 197 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 201 - "test_metrics.py"
Cohesion: 0.15
Nodes (4): metrics(), exposition(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 202 - "sites/controller.py"
Cohesion: 0.15
Nodes (6): assign_sites(), classify(), classify_many(), delete(), show(), unlinked()

### Community 210 - "Actor"
Cohesion: 0.08
Nodes (13): ad_units(), delete(), delete_lead(), export_leads(), leads(), metrics(), set_active(), set_icon() (+5 more)

### Community 212 - "PriceRuleDetailsOut"
Cohesion: 0.08
Nodes (3): PriceRuleDetailsOut, forget_rule(), stored_drop_tiers()

### Community 213 - "Actor"
Cohesion: 0.13
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 222 - "Suporte"
Cohesion: 0.40
Nodes (5): ApiKey, AuditLog, PasswordReset, Session, Suporte

### Community 223 - "HealthService"
Cohesion: 0.17
Nodes (3): ready(), health_service(), HealthService

### Community 226 - "settings_for_tests"
Cohesion: 0.13
Nodes (11): engine_settings(), restricted_engine(), settings_for_tests(), test_api_does_not_start_with_a_role_that_ignores_rls(), test_database_url_cannot_override_the_timeouts(), test_default_numbers_fit_the_connection_budget(), test_engine_settings_come_from_the_settings(), test_engine_settings_refuse_zero_and_above_the_ceiling() (+3 more)

### Community 231 - "_contract_fields"
Cohesion: 0.18
Nodes (3): index(), site_options(), SiteListOut

### Community 239 - "UnitOfWorkFactory"
Cohesion: 0.05
Nodes (9): CountryLookup, UnitOfWorkFactory, is_cascade_shape(), safe_site_cascades(), site_cascades(), RewardCache, prices(), PublicPriceFloorsOut (+1 more)

### Community 250 - "NetworkService"
Cohesion: 0.16
Nodes (3): index(), NetworkDetailOut, NetworkService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2464 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **121 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `PublicRewardService`, `roles/controller.py`, `DashboardService`, `Actor`, `.__init__`, `RewardCache`, `.__init__`, `.__init__`, `client_documents/controller.py`, `commissions/controller.py`, `.__init__`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `modules/ad_tags/dto.py`, `api_keys/controller.py`, `PageOut`, `_month`, `CustomMetricService`, `internal/loaders/controller.py`, `company/controller.py`, `goals/controller.py`, `mfa/controller.py`, `fastapi`, `ReportService`, `RewardService`, `sites/controller.py`, `GoalService`, `SiteService`, `PublicAdTagService`, `reports/service.py`, `mcm/service.py`, `mcm/controller.py`, `ClientService`, `UserOut`, `internal/loaders/service.py`, `AdTagService`, `PriceRuleService`, `PageOut`, `networks/service.py`, `Services`, `UserOut`, `download`, `modules/loaders/controller.py`, `MemberService`, `clients`, `CompanyService`, `google/controller.py`, `avant_core_access_models`, `goals/service.py`, `AuthService`, `TaskQueue`, `ContractService`, `Actor`, `SupportTaskService`, `AdTagOut`, `checklists/controller.py`, `reward_cache.py`, `ClientPriceRuleService`, `image`, `.__init__`, `gam_tools/service.py`, `pydantic`, `SiteChecklistService`, `test_redis_buffer_follows_the_worker_contract`, `google/controller.py`, `.__init__`, `tasks/controller.py`, `reward_public/dto.py`, `.__init__`, `.__init__`, `NetworkService`, `GamToolService`?**
  _High betweenness centrality (0.093) - this node is a cross-community bridge._
- **Are the 185 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 185 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PublicRewardService` be split into smaller, more focused modules?**
  _Cohesion score 0.09302325581395349 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `contracts/controller.py`, `roles/controller.py`, `DashboardService`, `Actor`, `ContractOut`, `RewardCache`, `_month`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `modules/ad_tags/dto.py`, `api_keys/controller.py`, `GoalTemplateOut`, `.update`, `PageOut`, `internal/loaders/controller.py`, `tasks`, `goals/controller.py`, `.of`, `ReportService`, `RewardService`, `sites/controller.py`, `GoalService`, `networks/controller.py`, `SiteService`, `reports/service.py`, `mcm/service.py`, `mcm/controller.py`, `ClientService`, `UserOut`, `internal/loaders/service.py`, `AdTagService`, `modules/loaders/controller.py`, `PriceRuleService`, `clients`, `Services`, `gam_tools/controller.py`, `get`, `modules/loaders/controller.py`, `MemberService`, `.page`, `modules/rewards/controller.py`, `avant_core_access_models`, `checklists/controller.py`, `goals/service.py`, `ContractService`, `Actor`, `SupportTaskService`, `AdTagOut`, `checklists/controller.py`, `sites/controller.py`, `reward_cache.py`, `ClientPriceRuleService`, `image`, `Actor`, `Actor`, `gam_tools/service.py`, `SiteChecklistService`, `tasks/controller.py`, `_contract_fields`, `GamToolNetworkOut`, `NetworkService`, `GamToolService`?**
  _High betweenness centrality (0.081) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `invoices/dto.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06475485661424607 - nodes in this community are weakly interconnected._