# Graph Report - avant-api  (2026-11-13)

## Corpus Check
- 387 files · ~125,669 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 5494 nodes · 15551 edges · 273 communities (152 shown, 121 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2486 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `cfbc9c06`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- InvoiceService
- roles/controller.py
- sites/controller.py
- clients/controller.py
- _member_client
- gam_tools/dto.py
- conftest.py
- steps
- _month
- Avant: models do MVP
- _member_client
- get
- GroupService
- PageOut
- modules/ad_tags/controller.py
- api_keys/service.py
- InvitationOut
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- test_mail_queue.py
- goals/controller.py
- invoice_pdf.py
- clients/controller.py
- clean_code.py
- AdTagService
- mfa/controller.py
- Avant: repositório e plano do MVP
- ReportService
- metrics
- .uow
- session-start.sh
- avant-api
- clients/service.py
- test_api_keys.py
- networks/dto.py
- test_account.py
- company/controller.py
- auth/controller.py
- install
- _onboard_owner
- Services
- test_reports.py
- networks/service.py
- invoices/controller.py
- .of_view
- Services
- BaseModel
- UnitOfWorkFactory
- .assign
- download
- members/controller.py
- test_api_keys.py
- router.py
- mcm/controller.py
- GoalTemplateIn
- account/controller.py
- CommissionService
- mine
- goals/service.py
- SessionCookies
- contracts/controller.py
- _marketing_client
- ReportService
- limits.py
- auth/controller.py
- test_costs_results.py
- google/controller.py
- avant-api
- TaskQueue
- UnitOfWorkFactory
- pool_metrics.py
- test_hardening.py
- commissions/dto.py
- ContractOut
- install
- events.py
- events.py
- GoogleService
- AdUnitOut
- Avant: grupos na Empresa e imagem da Empresa
- google_status
- ._mail_in_deployed_envs
- UserOut
- ContractService
- google/controller.py
- .page_saved
- _csrf
- PublicRewardService
- dollars
- reports/__init__.py
- SiteService
- reward_public/service.py
- templates
- .export_saved
- client_documents/controller.py
- ClientService
- modules/price_rules/service.py
- conftest.py
- test_key_values.py
- UUID
- contracts/dto.py
- commissions/controller.py
- CommissionRuleOut
- avant-api
- PageOut
- company/controller.py
- GoalTemplateOut
- .list_all
- LoaderService
- test_invitation_mail.py
- .create
- .of
- modules/results/controller.py
- CapturingMailer
- mfa/controller.py
- O que já tem
- sites/controller.py
- networks/controller.py
- SiteService
- AdTagOut
- reports/service.py
- people/controller.py
- main.py
- Avant: conexão com o GAM
- DashboardTemplateOut
- audit/controller.py
- document_response
- test
- UserOut
- PayeeDetailsOut
- RedisEvents
- google_status
- .of
- BaseModel
- checklists
- CompanyService
- logs.py
- ._required_services
- mine
- TaskQueue
- image
- capped
- ad_tag_public/controller.py
- goals/controller.py
- RedisKeyValueBuffer
- test_metrics.py
- RewardBuffer
- GoalService
- internal/rewards/controller.py
- Settings
- PriceRuleService
- forget_site
- GamToolRunOut
- Counter
- .run_guarded
- health/controller.py
- _BrokenAuthService
- rewards/http.py
- settings_for_tests
- Actor
- TaskPatchIn
- Actor
- DomainError
- .floors
- ci.yml
- key_values/controller.py
- OwnerInvitationOut
- _SpyCounter
- .assign
- Actor
- alerts/dependencies.py
- NetworkDetailOut
- edit_image
- PriceRuleHistoryOut
- show
- delete_template
- GeoLiteCountries
- FakeGoogle
- ports.py
- .first_day
- _BrokenReleaseCounter
- _contract_fields

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 236 edges
2. `PageOut` - 193 edges
3. `_csrf()` - 193 edges
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

## Communities (273 total, 121 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.17
Nodes (6): client_address(), icon(), leads(), page(), preflight(), RewardLeadIn

### Community 1 - "InvoiceService"
Cohesion: 0.09
Nodes (9): add_item(), delete(), delete_service(), issue(), pay(), remove_item(), update_item(), InvoiceOut (+1 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "sites/controller.py"
Cohesion: 0.05
Nodes (25): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+17 more)

### Community 4 - "clients/controller.py"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "_member_client"
Cohesion: 0.07
Nodes (25): _manage_inventory(), _membership_ids(), test_groups_lifecycle(), _assert_denied(), _queue(), test_cost_writes_need_permission(), test_documents_need_company_edit(), test_member_writes_need_permission() (+17 more)

### Community 6 - "gam_tools/dto.py"
Cohesion: 0.12
Nodes (5): AdsTxtOut, GamStepOut, GamToolClientOut, GamToolPersonOut, GamToolSiteOut

### Community 7 - "conftest.py"
Cohesion: 0.09
Nodes (8): ExpectedAsset, load_assets(), SwaggerAsset, SwaggerAssetChanged, _error_code(), test_every_write_route_refuses_another_site(), test_changed_asset_stops_the_start(), test_page_loads_only_checked_files_from_the_api()

### Community 8 - "steps"
Cohesion: 0.21
Nodes (13): AVANT_CORE_ACCESS, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, steps, env, name, run (+5 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.10
Nodes (20): Acesso, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade (+12 more)

### Community 11 - "_member_client"
Cohesion: 0.19
Nodes (20): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+12 more)

### Community 12 - "get"
Cohesion: 0.13
Nodes (9): health(), available_months(), get(), mine(), payment_details(), pdf(), service_options(), services() (+1 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "PageOut"
Cohesion: 0.06
Nodes (9): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, page_out() (+1 more)

### Community 15 - "modules/ad_tags/controller.py"
Cohesion: 0.23
Nodes (13): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagDraftIO, AdTagHealthDayOut, AdTagIn, AdTagLiveOut (+5 more)

### Community 16 - "api_keys/service.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.09
Nodes (9): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut (+1 more)

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.09
Nodes (20): CsrfFailed, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company(), get_actor(), get_auth() (+12 more)

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
Nodes (16): client(), engine(), mailer(), memory_services(), MemoryCounter, RecordingQueue, test_stream_limiter_caps_each_person_and_the_process(), _account() (+8 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "clients/controller.py"
Cohesion: 0.08
Nodes (17): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), clients() (+9 more)

### Community 26 - "clean_code.py"
Cohesion: 0.16
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "AdTagService"
Cohesion: 0.11
Nodes (3): health(), AdTagHealthOut, AdTagService

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), verify(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.05
Nodes (20): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+12 more)

### Community 31 - "metrics"
Cohesion: 0.09
Nodes (25): FixedCountries, reward_cache_key(), MemoryRewardBuffer, _png(), _buffer(), _cascade_reward(), test_events_and_leads_go_to_the_buffer(), test_icon_route_has_the_ip_limit() (+17 more)

### Community 32 - ".uow"
Cohesion: 0.09
Nodes (6): forget_pages(), create(), update(), RewardIn, RewardOut, RewardService

### Community 36 - "clients/service.py"
Cohesion: 0.11
Nodes (31): _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _cascade_rule(), _cascade_site(), _company_of() (+23 more)

### Community 37 - "test_api_keys.py"
Cohesion: 0.05
Nodes (13): RateLimited, BucketResult, BucketRule, PageViewBlockIn, PageViewIn, PublicAdTagOut, PublicBlockOut, PublicLoaderOut (+5 more)

### Community 40 - "test_account.py"
Cohesion: 0.15
Nodes (4): register_network(), McmService, NetworkOut, enqueue_sync()

### Community 41 - "company/controller.py"
Cohesion: 0.06
Nodes (16): register_client(), client_service(), ClientDetailOut, ClientIn, ClientMemberOut, ClientOptionOut, ClientOut, ClientPatchIn (+8 more)

### Community 42 - "auth/controller.py"
Cohesion: 0.12
Nodes (10): get_invitation(), auth_service(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut (+2 more)

### Community 43 - "install"
Cohesion: 0.12
Nodes (14): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+6 more)

### Community 44 - "_onboard_owner"
Cohesion: 0.11
Nodes (10): create(), delete(), index(), publish(), restore(), set_active(), show(), units() (+2 more)

### Community 45 - "Services"
Cohesion: 0.04
Nodes (17): Services, NoCountries, RedisBucket, get_services(), public_ad_tag_service(), ad_tag_service(), company_service(), cost_service() (+9 more)

### Community 46 - "test_reports.py"
Cohesion: 0.08
Nodes (26): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _checked_out(), _checkouts(), PoolWatchingEvents (+18 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "invoices/controller.py"
Cohesion: 0.14
Nodes (13): create_service(), return_to_draft(), update_service(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut (+5 more)

### Community 50 - "Services"
Cohesion: 0.08
Nodes (8): add(), delete(), edit(), notes(), ClientNoteIn, ClientNoteOut, NotePersonOut, ClientNoteService

### Community 51 - "BaseModel"
Cohesion: 0.12
Nodes (10): ads_txt(), install(), network(), networks(), run(), runs(), gam_tool_service(), GamToolNetworkDetailOut (+2 more)

### Community 52 - "UnitOfWorkFactory"
Cohesion: 0.09
Nodes (14): ad_units(), RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut (+6 more)

### Community 53 - ".assign"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (16): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+8 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.13
Nodes (16): run_password_reset_tasks(), Sent, MemoryBucket, _bearer(), _create(), _exercise(), _insert_key(), _keys_in_two_companies() (+8 more)

### Community 57 - "router.py"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "mcm/controller.py"
Cohesion: 0.12
Nodes (6): confirm_network(), reject_network(), unassigned_networks(), mcm_service(), ClientNetworkIn, McmCandidateOut

### Community 59 - "GoalTemplateIn"
Cohesion: 0.11
Nodes (9): delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active(), set_icon() (+1 more)

### Community 60 - "account/controller.py"
Cohesion: 0.07
Nodes (14): get_cookies(), delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service() (+6 more)

### Community 61 - "CommissionService"
Cohesion: 0.10
Nodes (5): results(), client_result_service(), ClientResultService, ResultsOut, default_period()

### Community 62 - "mine"
Cohesion: 0.14
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "goals/service.py"
Cohesion: 0.16
Nodes (7): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistNoteIn

### Community 64 - "SessionCookies"
Cohesion: 0.09
Nodes (10): SessionCookies, accept(), company_image(), do_logout(), login(), me(), set_active_company(), MeOut (+2 more)

### Community 65 - "contracts/controller.py"
Cohesion: 0.14
Nodes (9): contract(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract(), contract_service(), ContractOut (+1 more)

### Community 66 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 68 - "ReportService"
Cohesion: 0.08
Nodes (13): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+5 more)

### Community 69 - "limits.py"
Cohesion: 0.15
Nodes (9): Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter(), test_refused_reserve_never_touches_the_other_keys() (+1 more)

### Community 70 - "auth/controller.py"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 71 - "test_costs_results.py"
Cohesion: 0.14
Nodes (11): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+3 more)

### Community 72 - "google/controller.py"
Cohesion: 0.14
Nodes (6): ChecklistMarkIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "TaskQueue"
Cohesion: 0.15
Nodes (5): CeleryQueue, masked_args(), _CapturingCelery, test_password_reset_task_masks_the_email_in_the_message(), test_tasks_with_ids_only_are_not_masked()

### Community 75 - "UnitOfWorkFactory"
Cohesion: 0.04
Nodes (11): ad_tag_cache_key(), CountryLookup, GoogleUnavailable, Bucket, UnitOfWorkFactory, is_cascade_shape(), safe_site_cascades(), site_cascades() (+3 more)

### Community 76 - "pool_metrics.py"
Cohesion: 0.13
Nodes (8): _checked_in(), _checked_out(), _closed(), _opened(), watch_pool(), _sample(), test_pool_gauges_follow_checkout_and_close(), test_pool_timeouts_count_only_the_pool_wait()

### Community 77 - "test_hardening.py"
Cohesion: 0.18
Nodes (11): _rendered(), test_api_key_never_reaches_the_log(), test_docs_only_for_the_groone_session_with_2fa(), test_every_response_has_the_content_security_policy(), test_every_response_has_the_security_headers(), test_invalid_bearer_is_limited_per_ip_before_the_database(), counting(), test_old_docs_paths_do_not_exist() (+3 more)

### Community 78 - "commissions/dto.py"
Cohesion: 0.12
Nodes (13): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+5 more)

### Community 79 - "ContractOut"
Cohesion: 0.09
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "install"
Cohesion: 0.17
Nodes (10): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), masked_path() (+2 more)

### Community 82 - "events.py"
Cohesion: 0.10
Nodes (5): TooManyAttempts, EventSource, StreamLimiter, events(), EventService

### Community 83 - "events.py"
Cohesion: 0.17
Nodes (10): channel(), _parse(), sse(), _collect(), _event(), ListEvents, test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports() (+2 more)

### Community 85 - "GoogleService"
Cohesion: 0.11
Nodes (3): GoogleAuth, google_service(), GoogleService

### Community 86 - "AdUnitOut"
Cohesion: 0.16
Nodes (4): ad_units(), link(), unlinked(), AdUnitOut

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "google_status"
Cohesion: 0.14
Nodes (3): RedisCounter, test_redis_decr_without_key_creates_nothing(), test_redis_down_is_a_503_not_a_500()

### Community 89 - "._mail_in_deployed_envs"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 91 - "UserOut"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 92 - "ContractService"
Cohesion: 0.15
Nodes (3): site_checklist_service(), ChecklistDetailOut, SiteChecklistService

### Community 94 - "google/controller.py"
Cohesion: 0.11
Nodes (9): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), google_start(), _jwt() (+1 more)

### Community 95 - ".page_saved"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 96 - "_csrf"
Cohesion: 0.05
Nodes (57): browser(), _csrf(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+49 more)

### Community 97 - "PublicRewardService"
Cohesion: 0.12
Nodes (4): events(), RewardEventsIn, public_control_percent(), PublicRewardService

### Community 127 - "SiteService"
Cohesion: 0.11
Nodes (17): patterns, patterns, update-types, acoes, dependencias, imagens, dependency-name, patterns (+9 more)

### Community 128 - "reward_public/service.py"
Cohesion: 0.19
Nodes (11): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicRewardPriceOut (+3 more)

### Community 129 - "templates"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 130 - ".export_saved"
Cohesion: 0.07
Nodes (6): ExportsBusy, query(), ReportQueryIn, export_slot(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 131 - "client_documents/controller.py"
Cohesion: 0.14
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 132 - "ClientService"
Cohesion: 0.18
Nodes (9): _form(), _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit() (+1 more)

### Community 133 - "modules/price_rules/service.py"
Cohesion: 0.26
Nodes (13): CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn, PriceRuleHourOut (+5 more)

### Community 134 - "conftest.py"
Cohesion: 0.06
Nodes (6): refresh_levels(), MemoryRewardCache, NoEvents, _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 135 - "test_key_values.py"
Cohesion: 0.17
Nodes (5): MemoryKeyValueBuffer, _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_the_preflight_answers_with_cors()

### Community 137 - "contracts/dto.py"
Cohesion: 0.16
Nodes (7): contract_networks(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractSummaryOut, _network_ref(), ContractClientRefOut

### Community 138 - "commissions/controller.py"
Cohesion: 0.06
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 139 - "CommissionRuleOut"
Cohesion: 0.10
Nodes (5): openapi(), swagger(), swagger_asset(), _swagger_page(), event_service()

### Community 142 - "avant-api"
Cohesion: 0.24
Nodes (9): load_settings(), _environment(), _refused_names(), test_api_starts_with_each_transport(), test_environment_name_changes_nothing(), test_malformed_smtp_url_never_shows_the_value(), test_missing_or_invalid_configuration_stops_the_api(), test_queue_does_not_break_the_request_without_broker() (+1 more)

### Community 143 - "PageOut"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "company/controller.py"
Cohesion: 0.16
Nodes (5): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 145 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 146 - ".list_all"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 148 - "LoaderService"
Cohesion: 0.04
Nodes (23): create(), delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService (+15 more)

### Community 149 - "test_invitation_mail.py"
Cohesion: 0.22
Nodes (10): _assert_mail_not_sent(), _client_with_owner_invitation(), _invite(), _owner_invitation_emails(), _pending_emails(), test_invite_answers_503_when_the_mail_fails(), test_owner_invitation_answers_503_when_the_mail_fails(), test_owner_invitation_resend_answers_503_when_the_mail_fails() (+2 more)

### Community 150 - ".create"
Cohesion: 0.13
Nodes (3): _google(), _mailer(), test_each_transport_builds_its_mailer()

### Community 152 - ".of"
Cohesion: 0.09
Nodes (16): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, _after_first_segment(), _jpeg(), _sharpness(), _striped_logo() (+8 more)

### Community 153 - "modules/results/controller.py"
Cohesion: 0.13
Nodes (3): show(), result_service(), ResultService

### Community 155 - "CapturingMailer"
Cohesion: 0.08
Nodes (48): CapturingMailer, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited() (+40 more)

### Community 158 - "mfa/controller.py"
Cohesion: 0.14
Nodes (3): client_info(), image_response(), image_upload()

### Community 161 - "sites/controller.py"
Cohesion: 0.25
Nodes (8): AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn, SitesPatchIn

### Community 163 - "networks/controller.py"
Cohesion: 0.19
Nodes (6): disconnect(), options(), service_account(), show(), sync(), sync_runs()

### Community 164 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 165 - "AdTagOut"
Cohesion: 0.13
Nodes (3): forget_tag(), AdTagOut, update()

### Community 166 - "reports/service.py"
Cohesion: 0.05
Nodes (15): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+7 more)

### Community 167 - "people/controller.py"
Cohesion: 0.10
Nodes (8): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out()

### Community 168 - "main.py"
Cohesion: 0.14
Nodes (5): _content_security_policy(), observe(), _route_template(), create_app(), public_price_floor_service()

### Community 172 - "Avant: conexão com o GAM"
Cohesion: 0.11
Nodes (16): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment, Avant: conexão com o GAM, Caminho conta de serviço (+8 more)

### Community 174 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 175 - "audit/controller.py"
Cohesion: 0.15
Nodes (3): index(), audit_service(), AuditService

### Community 177 - "test"
Cohesion: 0.12
Nodes (16): AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, POSTGRES_PASSWORD, test, env, image, options (+8 more)

### Community 178 - "UserOut"
Cohesion: 0.08
Nodes (9): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService (+1 more)

### Community 180 - "RedisEvents"
Cohesion: 0.27
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 182 - "google_status"
Cohesion: 0.12
Nodes (3): google_status(), google_unlink(), GoogleStatusOut

### Community 183 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 184 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 185 - "checklists"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 188 - "logs.py"
Cohesion: 0.17
Nodes (5): configure_logging(), JsonFormatter, _record(), test_log_keeps_ordinary_messages(), test_log_masks_database_values_in_message_and_stack()

### Community 190 - "._required_services"
Cohesion: 0.12
Nodes (4): _are_proxy_addresses(), invalid_variable_names(), InvalidVariables, _is_smtp_url()

### Community 191 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 192 - "TaskQueue"
Cohesion: 0.11
Nodes (8): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, QueueUnavailable, TaskMailQueue, TaskQueue

### Community 196 - "ad_tag_public/controller.py"
Cohesion: 0.18
Nodes (5): config(), page_views(), preflight(), cors(), read_body()

### Community 197 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 198 - "RedisKeyValueBuffer"
Cohesion: 0.13
Nodes (3): KeyValueBuffer, RedisKeyValueBuffer, test_redis_buffer_follows_the_worker_contract()

### Community 201 - "test_metrics.py"
Cohesion: 0.24
Nodes (3): exposition(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 204 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 210 - "internal/rewards/controller.py"
Cohesion: 0.10
Nodes (14): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+6 more)

### Community 211 - "Settings"
Cohesion: 0.20
Nodes (3): Settings, GoogleRedirects, test_google_flow_cookie_is_always_secure()

### Community 212 - "PriceRuleService"
Cohesion: 0.09
Nodes (3): PriceRuleDetailsOut, forget_rule(), stored_drop_tiers()

### Community 214 - "forget_site"
Cohesion: 0.23
Nodes (3): forget_cascades(), forget_floors(), forget_site()

### Community 223 - "health/controller.py"
Cohesion: 0.14
Nodes (4): metrics(), ready(), health_service(), HealthService

### Community 225 - "rewards/http.py"
Cohesion: 0.18
Nodes (3): csv_response(), lead_filter(), period()

### Community 226 - "settings_for_tests"
Cohesion: 0.13
Nodes (11): engine_settings(), restricted_engine(), settings_for_tests(), test_api_does_not_start_with_a_role_that_ignores_rls(), test_database_url_cannot_override_the_timeouts(), test_default_numbers_fit_the_connection_budget(), test_engine_settings_come_from_the_settings(), test_engine_settings_refuse_zero_and_above_the_ceiling() (+3 more)

### Community 227 - "Actor"
Cohesion: 0.20
Nodes (4): classify(), classify_many(), site_options(), sites_of_member()

### Community 233 - "DomainError"
Cohesion: 0.18
Nodes (4): CompanyChanged, InvitationMailNotSent, NoActiveCompany, QueryTooHeavy

### Community 240 - "ci.yml"
Cohesion: 0.18
Nodes (10): jobs, segredos, name, on, pull_request, push, permissions, contents (+2 more)

### Community 242 - "key_values/controller.py"
Cohesion: 0.27
Nodes (3): cors(), preflight(), receive()

### Community 244 - "OwnerInvitationOut"
Cohesion: 0.27
Nodes (3): owner_invitations(), OwnerInvitationOut, owner_invitation_out()

### Community 247 - ".assign"
Cohesion: 0.25
Nodes (5): Atribuição de sites, GAM, Networks, Sites e ad units, assign_sites()

### Community 250 - "NetworkDetailOut"
Cohesion: 0.13
Nodes (5): connect(), index(), NetworkDetailOut, NetworkIn, NetworkService

### Community 252 - "edit_image"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 265 - "ports.py"
Cohesion: 0.11
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2470 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **121 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `InvoiceService`, `roles/controller.py`, `sites/controller.py`, `clients/controller.py`, `client_documents/controller.py`, `.__init__`, `gam_tools/service.py`, `.__init__`, `contracts/dto.py`, `commissions/controller.py`, `modules/price_rules/service.py`, `ports.py`, `GroupService`, `PageOut`, `.__init__`, `api_keys/service.py`, `company/controller.py`, `.__init__`, `custom_metrics/controller.py`, `.__init__`, `LoaderService`, `InvitationOut`, `goals/controller.py`, `modules/results/controller.py`, `AdTagService`, `mfa/controller.py`, `Avant: repositório e plano do MVP`, `ReportService`, `.uow`, `sites/controller.py`, `SiteService`, `test_api_keys.py`, `reports/service.py`, `people/controller.py`, `test_account.py`, `company/controller.py`, `auth/controller.py`, `install`, `.__init__`, `_month`, `audit/controller.py`, `invoices/controller.py`, `networks/service.py`, `Services`, `BaseModel`, `UserOut`, `members/controller.py`, `router.py`, `account/controller.py`, `CommissionService`, `TaskQueue`, `contracts/controller.py`, `auth/controller.py`, `test_costs_results.py`, `google/controller.py`, `GoalService`, `commissions/dto.py`, `ContractOut`, `.__init__`, `internal/rewards/controller.py`, `GoogleService`, `UserOut`, `.__init__`, `.__init__`, `ContractService`, `.__init__`, `.page_saved`, `PublicRewardService`, `.__init__`, `NetworkDetailOut`, `goals/service.py`?**
  _High betweenness centrality (0.120) - this node is a cross-community bridge._
- **Are the 186 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 186 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `InvoiceService` be split into smaller, more focused modules?**
  _Cohesion score 0.08506493506493507 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `InvoiceService`, `roles/controller.py`, `sites/controller.py`, `clients/controller.py`, `gam_tools/service.py`, `modules/price_rules/service.py`, `UUID`, `contracts/dto.py`, `ports.py`, `_month`, `get`, `GroupService`, `modules/ad_tags/controller.py`, `api_keys/service.py`, `GoalTemplateOut`, `.list_all`, `InvitationOut`, `LoaderService`, `clients/controller.py`, `AdTagService`, `ReportService`, `O que já tem`, `.uow`, `sites/controller.py`, `networks/controller.py`, `SiteService`, `UUID`, `people/controller.py`, `test_account.py`, `company/controller.py`, `reports/service.py`, `install`, `_onboard_owner`, `audit/controller.py`, `invoices/controller.py`, `Services`, `BaseModel`, `UnitOfWorkFactory`, `members/controller.py`, `checklists`, `mcm/controller.py`, `GoalTemplateIn`, `CommissionService`, `goals/service.py`, `contracts/controller.py`, `test_mfa.py`, `goals/controller.py`, `auth/controller.py`, `test_costs_results.py`, `google/controller.py`, `UnitOfWorkFactory`, `GoalService`, `commissions/dto.py`, `ContractOut`, `internal/rewards/controller.py`, `PriceRuleService`, `AdUnitOut`, `ContractService`, `.page_saved`, `OwnerInvitationOut`, `NetworkDetailOut`, `reports/__init__.py`, `goals/service.py`?**
  _High betweenness centrality (0.082) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07562008469449485 - nodes in this community are weakly interconnected._