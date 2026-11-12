# Graph Report - wt132-avant-api  (2026-11-12)

## Corpus Check
- 384 files · ~124,752 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 8, .ttf 2, .toml 1)

## Summary
- 5457 nodes · 15449 edges · 242 communities (124 shown, 118 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2475 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `9c39eab6`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- reward_public/controller.py
- test_mfa.py
- roles/controller.py
- .uow
- PageOut
- _member_client
- .of
- ClientService
- steps
- schedules/controller.py
- Avant: conexão com o GAM
- _staff
- .trusted_uow
- GroupService
- require_staff
- modules/ad_tags/dto.py
- api_keys/controller.py
- avant_core_access_models
- main.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- conftest.py
- dashboard_templates/controller.py
- invoice_pdf.py
- image_response
- clean_code.py
- .of
- mfa/controller.py
- currencies/controller.py
- ReportService
- browser
- RewardService
- session-start.sh
- avant-api
- test_price_rules.py
- ad_tag_public/service.py
- internal/results/controller.py
- _BrokenReleaseCounter
- mcm/controller.py
- LoaderService
- Actor
- AdTagService
- Services
- _csrf
- views/controller.py
- test_invitation_mail.py
- .page
- client_notes/controller.py
- GamToolService
- modules/rewards/dto.py
- edit
- download
- members/controller.py
- test_account.py
- ItemsOut
- time
- modules/rewards/controller.py
- account/controller.py
- results/dto.py
- RedisRewardCache
- checklists/controller.py
- auth/controller.py
- O que já tem
- audit/controller.py
- export.py
- Limiter
- openapi
- ClientAdTagService
- avant-api
- _CapturingCelery
- modules/rewards/service.py
- create
- test_hardening.py
- ClientPriceRuleService
- costs/controller.py
- install
- swagger_assets.py
- events.py
- test_events.py
- AdTagHealthOut
- .run_guarded
- sites/service.py
- Avant: grupos na Empresa e imagem da Empresa
- RedisCounter
- Groone Avant: contexto do projeto
- documents/controller.py
- company/controller.py
- errors.py
- page_out
- DashboardTemplateOut
- RewardCache
- reward_public/dto.py
- .of_details
- updates
- contracts/controller.py
- Avant: repositório e plano do MVP
- .export_saved
- mcm/service.py
- test_alerts.py
- PriceRuleService
- mine
- RedisKeyValueBuffer
- show
- client_documents/controller.py
- commissions/controller.py
- .of
- OwnerInvitationOut
- Arquitetura do MVP do Avant
- ClientLoaderService
- GoalTemplateOut
- io
- datetime
- Actor
- MemoryBucket
- test_company_image.py
- goals/controller.py
- CapturingMailer
- dollars
- SiteService
- GoalService
- networks/controller.py
- .page_saved
- configure_logging
- reports/service.py
- shared/dto.py
- ad_units
- internal/loaders/service.py
- document_response
- AdTagUnitDayOut
- profile/controller.py
- get
- RedisEvents
- .of_detail
- modules/loaders/controller.py
- tasks/controller.py
- CompanyService
- TaskQueue
- receive
- limits.py
- delete_template
- test_networks.py
- test_metrics.py
- sites/controller.py
- modules/loaders/dto.py
- internal/rewards/controller.py
- UUID
- SiteOut
- LoaderOptionOut
- Counter
- ContractClientRefOut
- HealthService
- _BrokenAuthService
- .build
- .of
- SiteListOut
- _SpyCounter
- UnitOfWorkFactory
- clients/service.py
- floor_cache.py
- SyncRunOut
- GeoLiteCountries
- RewardBuffer
- RedisRewardBuffer
- create

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
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Onde está o trabalho` --references--> `PriceRuleSiteOut`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/price_rules/dto.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (242 total, 118 thin omitted)

### Community 0 - "reward_public/controller.py"
Cohesion: 0.12
Nodes (9): client_address(), events(), icon(), leads(), page(), preflight(), read_body(), public_reward_service() (+1 more)

### Community 1 - "test_mfa.py"
Cohesion: 0.12
Nodes (22): _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads() (+14 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - ".uow"
Cohesion: 0.05
Nodes (24): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+16 more)

### Community 4 - "PageOut"
Cohesion: 0.10
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "_member_client"
Cohesion: 0.08
Nodes (22): _manage_inventory(), _membership_ids(), test_groups_lifecycle(), _assert_denied(), _queue(), test_cost_writes_need_permission(), test_documents_need_company_edit(), test_member_writes_need_permission() (+14 more)

### Community 7 - "ClientService"
Cohesion: 0.08
Nodes (19): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), clients() (+11 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (38): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, POSTGRES_PASSWORD (+30 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: conexão com o GAM"
Cohesion: 0.05
Nodes (35): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+27 more)

### Community 11 - "_staff"
Cohesion: 0.08
Nodes (30): _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions(), test_groone_role_with_the_whole_catalog() (+22 more)

### Community 12 - ".trusted_uow"
Cohesion: 0.08
Nodes (4): add_item(), update_item(), InvoiceOut, InvoiceService

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "require_staff"
Cohesion: 0.11
Nodes (9): require_staff(), dependency(), networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut (+1 more)

### Community 15 - "modules/ad_tags/dto.py"
Cohesion: 0.10
Nodes (12): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagDraftIO, AdTagHealthDayOut, AdTagIn, AdTagLiveOut (+4 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "avant_core_access_models"
Cohesion: 0.05
Nodes (16): InvitationMailNotSent, invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, cancel() (+8 more)

### Community 18 - "main.py"
Cohesion: 0.05
Nodes (22): CompanyChanged, CsrfFailed, NoActiveCompany, QueryTooHeavy, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site() (+14 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (11): check(), create(), delete(), index(), update(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn (+3 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "conftest.py"
Cohesion: 0.05
Nodes (17): client(), engine(), mailer(), memory_services(), MemoryCounter, MemoryRewardCache, NoEvents, RecordingQueue (+9 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), roles(), set_home(), show(), update(), DashboardTemplateIn (+5 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "image_response"
Cohesion: 0.12
Nodes (3): image(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.16
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "currencies/controller.py"
Cohesion: 0.15
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.05
Nodes (21): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned() (+13 more)

### Community 31 - "browser"
Cohesion: 0.08
Nodes (26): browser(), MemoryRewardBuffer, _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _png() (+18 more)

### Community 32 - "RewardService"
Cohesion: 0.09
Nodes (7): create(), forget_pages(), create(), update(), RewardIn, RewardOut, RewardService

### Community 36 - "test_price_rules.py"
Cohesion: 0.12
Nodes (27): FixedCountries, _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _offerwall_unit(), _present() (+19 more)

### Community 37 - "ad_tag_public/service.py"
Cohesion: 0.06
Nodes (14): ad_tag_cache_key(), BucketRule, config(), page_views(), preflight(), PageViewBlockIn, PageViewIn, PublicAdTagOut (+6 more)

### Community 38 - "internal/results/controller.py"
Cohesion: 0.12
Nodes (5): results(), client_result_service(), ClientResultService, ResultsOut, default_period()

### Community 40 - "mcm/controller.py"
Cohesion: 0.11
Nodes (8): confirm_network(), register_network(), reject_network(), unassigned_networks(), ClientNetworkIn, McmCandidateOut, McmService, NetworkOut

### Community 42 - "LoaderService"
Cohesion: 0.19
Nodes (4): create(), LoaderIn, LoaderOut, LoaderService

### Community 43 - "Actor"
Cohesion: 0.12
Nodes (11): cascade_hours(), history(), hours(), index(), set_floor(), settings(), show(), sites() (+3 more)

### Community 44 - "AdTagService"
Cohesion: 0.09
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 45 - "Services"
Cohesion: 0.03
Nodes (26): Services, get_services(), known_companies(), public_ad_tag_service(), alert_service(), company_service(), custom_metric_service(), health_service() (+18 more)

### Community 46 - "_csrf"
Cohesion: 0.08
Nodes (31): _csrf(), _checked_out(), _checkouts(), PoolWatchingEvents, test_downloads_give_the_connection_back(), test_event_stream_holds_no_connection(), test_report_requests_use_few_connections(), query() (+23 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "test_invitation_mail.py"
Cohesion: 0.24
Nodes (10): _assert_mail_not_sent(), _client_with_owner_invitation(), _invite(), _owner_invitation_emails(), _pending_emails(), test_invite_answers_503_when_the_mail_fails(), test_owner_invitation_answers_503_when_the_mail_fails(), test_owner_invitation_resend_answers_503_when_the_mail_fails() (+2 more)

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "GamToolService"
Cohesion: 0.07
Nodes (17): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+9 more)

### Community 52 - "modules/rewards/dto.py"
Cohesion: 0.07
Nodes (14): ad_units(), RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut (+6 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "test_account.py"
Cohesion: 0.08
Nodes (24): run_password_reset_tasks(), MemoryKeyValueBuffer, _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password() (+16 more)

### Community 57 - "ItemsOut"
Cohesion: 0.12
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 58 - "time"
Cohesion: 0.26
Nodes (3): _content_security_policy(), observe(), _route_template()

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.08
Nodes (12): delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active(), set_icon() (+4 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "results/dto.py"
Cohesion: 0.11
Nodes (3): show(), result_service(), ResultService

### Community 62 - "RedisRewardCache"
Cohesion: 0.14
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "checklists/controller.py"
Cohesion: 0.06
Nodes (20): add_note(), check(), checklist(), checklists(), delete_note(), edit_note(), mark(), months() (+12 more)

### Community 64 - "auth/controller.py"
Cohesion: 0.04
Nodes (21): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), get_invitation(), login(), me() (+13 more)

### Community 67 - "audit/controller.py"
Cohesion: 0.14
Nodes (3): index(), audit_service(), AuditService

### Community 68 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "Limiter"
Cohesion: 0.13
Nodes (9): Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter(), test_refused_reserve_never_touches_the_other_keys() (+1 more)

### Community 70 - "openapi"
Cohesion: 0.15
Nodes (4): openapi(), swagger(), swagger_asset(), _swagger_page()

### Community 71 - "ClientAdTagService"
Cohesion: 0.12
Nodes (12): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+4 more)

### Community 74 - "_CapturingCelery"
Cohesion: 0.17
Nodes (4): masked_args(), _CapturingCelery, test_password_reset_task_masks_the_email_in_the_message(), test_tasks_with_ids_only_are_not_masked()

### Community 77 - "test_hardening.py"
Cohesion: 0.18
Nodes (11): _rendered(), test_api_key_never_reaches_the_log(), test_docs_only_for_the_groone_session_with_2fa(), test_every_response_has_the_content_security_policy(), test_every_response_has_the_security_headers(), test_invalid_bearer_is_limited_per_ip_before_the_database(), counting(), test_old_docs_paths_do_not_exist() (+3 more)

### Community 78 - "ClientPriceRuleService"
Cohesion: 0.08
Nodes (14): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+6 more)

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "install"
Cohesion: 0.21
Nodes (9): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), masked_path() (+1 more)

### Community 81 - "swagger_assets.py"
Cohesion: 0.12
Nodes (6): challenge(), ExpectedAsset, load_assets(), SwaggerAsset, SwaggerAssetChanged, test_changed_asset_stops_the_start()

### Community 82 - "events.py"
Cohesion: 0.08
Nodes (9): TooManyAttempts, channel(), EventSource, _parse(), sse(), StreamLimiter, events(), EventService (+1 more)

### Community 83 - "test_events.py"
Cohesion: 0.27
Nodes (11): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_events_route_refuses_above_the_cap(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports() (+3 more)

### Community 86 - "sites/service.py"
Cohesion: 0.18
Nodes (5): link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "RedisCounter"
Cohesion: 0.14
Nodes (3): RedisCounter, test_redis_decr_without_key_creates_nothing(), test_redis_down_is_a_503_not_a_500()

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 91 - "documents/controller.py"
Cohesion: 0.15
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 92 - "company/controller.py"
Cohesion: 0.20
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 94 - "errors.py"
Cohesion: 0.04
Nodes (17): GoogleFailed, GoogleUnavailable, _claims(), GoogleAuth, GoogleOAuth, identity_from_id_token(), new_verifier(), google_start() (+9 more)

### Community 96 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 97 - "RewardCache"
Cohesion: 0.07
Nodes (10): is_cascade_shape(), safe_site_cascades(), site_cascades(), reward_cache_key(), RewardCache, CachedPage, PublicPageOut, PublicRewardPriceOut (+2 more)

### Community 102 - "reward_public/dto.py"
Cohesion: 0.23
Nodes (9): PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicQuestionOut, PublicRewardOut, PublicStyleOut, RewardEventIn, RewardLeadAnswerIn (+1 more)

### Community 127 - "updates"
Cohesion: 0.11
Nodes (17): patterns, patterns, update-types, acoes, dependencias, imagens, dependency-name, patterns (+9 more)

### Community 128 - "contracts/controller.py"
Cohesion: 0.12
Nodes (13): contract(), contract_networks(), contracts(), finish_contract(), new_contract(), remove_contract(), ContractIn, ContractNetworkOut (+5 more)

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 130 - ".export_saved"
Cohesion: 0.08
Nodes (4): ExportsBusy, export_slot(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 132 - "test_alerts.py"
Cohesion: 0.25
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 133 - "PriceRuleService"
Cohesion: 0.22
Nodes (16): price_rule_service(), CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn (+8 more)

### Community 134 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 135 - "RedisKeyValueBuffer"
Cohesion: 0.15
Nodes (3): KeyValueBuffer, RedisKeyValueBuffer, test_redis_buffer_follows_the_worker_contract()

### Community 137 - "client_documents/controller.py"
Cohesion: 0.17
Nodes (8): approve(), documents(), download(), reject(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 138 - "commissions/controller.py"
Cohesion: 0.06
Nodes (22): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+14 more)

### Community 139 - ".of"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 142 - "OwnerInvitationOut"
Cohesion: 0.23
Nodes (3): owner_invitations(), OwnerInvitationOut, owner_invitation_out()

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "ClientLoaderService"
Cohesion: 0.13
Nodes (6): delete(), index(), options(), show(), update(), ClientLoaderService

### Community 145 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 146 - "io"
Cohesion: 0.31
Nodes (5): _result(), test_compare_header_follows_the_mode(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 147 - "datetime"
Cohesion: 0.05
Nodes (23): refresh_levels(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _networks() (+15 more)

### Community 149 - "MemoryBucket"
Cohesion: 0.28
Nodes (4): MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 152 - "test_company_image.py"
Cohesion: 0.08
Nodes (19): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, _after_first_segment(), _jpeg(), _put_image(), _sharpness() (+11 more)

### Community 153 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 155 - "CapturingMailer"
Cohesion: 0.07
Nodes (45): CapturingMailer, Sent, _error_code(), _onboard_owner(), _owner_invite(), test_cookies_are_always_secure_with_the_host_prefix(), test_csrf_is_required_for_writes(), test_every_write_route_refuses_another_site() (+37 more)

### Community 161 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 162 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 163 - "networks/controller.py"
Cohesion: 0.10
Nodes (13): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+5 more)

### Community 166 - "reports/service.py"
Cohesion: 0.05
Nodes (15): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+7 more)

### Community 167 - "shared/dto.py"
Cohesion: 0.08
Nodes (10): Modelo de dados, Resumo, disable(), enable(), reset_mfa(), users(), PersonOut, PeopleService (+2 more)

### Community 178 - "profile/controller.py"
Cohesion: 0.09
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 179 - "get"
Cohesion: 0.06
Nodes (30): health(), available_months(), create_service(), delete(), delete_service(), get(), issue(), mine() (+22 more)

### Community 183 - "modules/loaders/controller.py"
Cohesion: 0.17
Nodes (5): delete(), index(), show(), update(), loader_service()

### Community 184 - "tasks/controller.py"
Cohesion: 0.05
Nodes (17): change(), comment(), create(), task(), tasks(), TaskClientOut, TaskCommentIn, TaskDataIn (+9 more)

### Community 186 - "CompanyService"
Cohesion: 0.11
Nodes (6): edit_image(), fiscal(), remove_image(), show(), CompanyDetailOut, CompanyService

### Community 192 - "TaskQueue"
Cohesion: 0.08
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskMailQueue, TaskQueue

### Community 193 - "receive"
Cohesion: 0.27
Nodes (4): options, cors(), preflight(), receive()

### Community 195 - "limits.py"
Cohesion: 0.06
Nodes (9): CountryLookup, RateLimited, Bucket, BucketResult, KeyValueIn, receive_key_values(), prices(), PublicPriceFloorsOut (+1 more)

### Community 198 - "test_networks.py"
Cohesion: 0.38
Nodes (8): _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission(), test_staff_without_permission_and_other_clients()

### Community 201 - "test_metrics.py"
Cohesion: 0.15
Nodes (4): metrics(), exposition(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 202 - "sites/controller.py"
Cohesion: 0.15
Nodes (8): assign_sites(), classify(), classify_many(), delete(), site_options(), unlinked(), SitePatchIn, SitesPatchIn

### Community 210 - "internal/rewards/controller.py"
Cohesion: 0.07
Nodes (12): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+4 more)

### Community 213 - "SiteOut"
Cohesion: 0.15
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 218 - "ContractClientRefOut"
Cohesion: 0.17
Nodes (3): _contract_fields(), _network_ref(), ContractClientRefOut

### Community 226 - ".build"
Cohesion: 0.04
Nodes (29): engine_settings(), _google(), _mailer(), restricted_engine(), NoCountries, RedisBucket, _are_proxy_addresses(), invalid_variable_names() (+21 more)

### Community 231 - "SiteListOut"
Cohesion: 0.14
Nodes (3): create(), index(), SiteListOut

### Community 240 - "clients/service.py"
Cohesion: 0.13
Nodes (13): ClientDetailOut, ClientIn, ClientMemberOut, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+5 more)

### Community 245 - "floor_cache.py"
Cohesion: 0.19
Nodes (4): forget_cascades(), forget_floors(), forget_rule(), forget_site()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2455 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **118 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `contracts/controller.py`, `RewardBuffer`, `roles/controller.py`, `.uow`, `PageOut`, `mcm/service.py`, `PriceRuleService`, `ClientService`, `.__init__`, `client_documents/controller.py`, `commissions/controller.py`, `.__init__`, `.trusted_uow`, `GroupService`, `require_staff`, `modules/ad_tags/dto.py`, `api_keys/controller.py`, `avant_core_access_models`, `ClientLoaderService`, `custom_metrics/controller.py`, `dashboard_templates/controller.py`, `.of`, `mfa/controller.py`, `currencies/controller.py`, `ReportService`, `RewardService`, `SiteService`, `GoalService`, `networks/controller.py`, `ad_tag_public/service.py`, `internal/results/controller.py`, `shared/dto.py`, `mcm/controller.py`, `reports/service.py`, `LoaderService`, `internal/loaders/service.py`, `AdTagService`, `schedules/controller.py`, `views/controller.py`, `client_notes/controller.py`, `GamToolService`, `get`, `profile/controller.py`, `members/controller.py`, `tasks/controller.py`, `ItemsOut`, `CompanyService`, `account/controller.py`, `results/dto.py`, `checklists/controller.py`, `auth/controller.py`, `TaskQueue`, `goals/service.py`, `audit/controller.py`, `limits.py`, `ClientAdTagService`, `modules/rewards/service.py`, `ClientPriceRuleService`, `costs/controller.py`, `internal/rewards/controller.py`, `.__init__`, `sites/service.py`, `documents/controller.py`, `company/controller.py`, `.__init__`, `errors.py`, `.__init__`, `.__init__`, `RewardCache`, `clients/service.py`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Are the 183 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 183 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `reward_public/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11822660098522167 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `contracts/controller.py`, `roles/controller.py`, `.uow`, `mcm/service.py`, `PriceRuleService`, `ClientService`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `OwnerInvitationOut`, `modules/ad_tags/dto.py`, `api_keys/controller.py`, `GoalTemplateOut`, `require_staff`, `ClientLoaderService`, `avant_core_access_models`, `goals/controller.py`, `.of`, `RewardService`, `SiteService`, `GoalService`, `networks/controller.py`, `.page_saved`, `internal/results/controller.py`, `shared/dto.py`, `mcm/controller.py`, `Actor`, `LoaderService`, `internal/loaders/service.py`, `AdTagService`, `Actor`, `reports/service.py`, `.page`, `client_notes/controller.py`, `GamToolService`, `get`, `modules/loaders/controller.py`, `tasks/controller.py`, `members/controller.py`, `modules/rewards/controller.py`, `checklists/controller.py`, `goals/service.py`, `O que já tem`, `audit/controller.py`, `ClientAdTagService`, `sites/controller.py`, `modules/rewards/service.py`, `ClientPriceRuleService`, `costs/controller.py`, `internal/rewards/controller.py`, `UUID`, `SiteOut`, `sites/service.py`, `page_out`, `SiteListOut`, `clients/service.py`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_mfa.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11738648947951273 - nodes in this community are weakly interconnected._