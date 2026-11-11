# Graph Report - avant-api  (2026-11-11)

## Corpus Check
- 373 files · ~116,502 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 5197 nodes · 14608 edges · 238 communities (128 shown, 110 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 2411 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `4192660a`
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
- DashboardTemplateOut
- InvoiceService
- .uow
- inventory/dto.py
- AdTagService
- api_keys/controller.py
- PageOut
- security.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- typing
- goals/controller.py
- verify
- Actor
- clean_code.py
- ClientPriceRuleService
- mfa/controller.py
- floor_cache.py
- reports/service.py
- CapturingMailer
- RewardService
- session-start.sh
- avant-api
- test_price_rules.py
- tasks/controller.py
- modules/ad_tags/dto.py
- PublicAdTagService
- clients/controller.py
- test_company_image.py
- documents/controller.py
- test_alerts.py
- SiteChecklistService
- Services
- uuid
- networks/service.py
- ChecklistDetailOut
- .upload
- Services
- _month
- MemoryCounter
- edit
- currencies/controller.py
- members/controller.py
- typing
- clients
- key_values/service.py
- modules/rewards/controller.py
- account/controller.py
- client_documents/controller.py
- Actor
- commissions/controller.py
- SessionCookies
- errors.py
- invoices/controller.py
- export.py
- limits.py
- Actor
- ClientAdTagService
- .of
- avant-api
- networks/controller.py
- ClientService
- test_events.py
- test_reward_public.py
- PriceRuleService
- image
- ClientDocumentsOut
- results/dto.py
- events.py
- uuid
- .of
- internal/rewards/controller.py
- sites/service.py
- Avant: grupos na Empresa e imagem da Empresa
- price_floor_public/service.py
- Groone Avant: contexto do projeto
- Actor
- LoaderService
- google/controller.py
- modules/price_rules/controller.py
- _csrf
- reward_public/service.py
- invoices/controller.py
- ad_tag_public/dto.py
- MemoryBucket
- updates
- auth/controller.py
- Avant: repositório e plano do MVP
- PriceRuleConfigIn
- main.py
- contracts/controller.py
- UnitOfWorkFactory
- .page
- test_staff_without_permission_and_other_clients
- ad_units
- clients
- typing
- PriceRuleHourOut
- .assign
- Arquitetura do MVP do Avant
- test_mfa.py
- GoalService
- get
- test_who_sees_and_changes_invoices
- test_database.py
- SiteService
- Actor
- .__init__
- GoalTemplateIn
- alerts/dependencies.py
- mine
- .show
- ClientOut
- image
- TaskQueue
- image_response
- goals/service.py
- test_account.py
- UserOut
- clients/controller.py
- AdTagUnitDayOut
- image
- team
- client_documents/service.py
- Actor
- Actor
- UserOut
- .update_fiscal
- health/controller.py
- SiteOut
- AdTagVersionOut
- Avant: conexão com o GAM
- test_permissions_on_keys
- AdTagHealthOut
- capped
- .of
- test_staff_sees_client_networks_sites_and_revenue_status
- AuditOut
- key_values/service.py
- package.json
- .update
- _site
- clients/controller.py
- RewardStyleIO
- show
- UserOut
- edit_image
- create
- UUID
- client_documents/dependencies.py
- source_files
- Actor

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 204 edges
2. `PageOut` - 193 edges
3. `_csrf()` - 173 edges
4. `get()` - 171 edges
5. `_onboard_owner()` - 164 edges
6. `UnitOfWorkFactory` - 163 edges
7. `Services` - 161 edges
8. `_staff()` - 80 edges
9. `ReportService` - 79 edges
10. `page_out()` - 79 edges

## Surprising Connections (you probably didn't know these)
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/internal/contracts/controller.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py
- `Pipeline` --references--> `main()`  [INFERRED]
  docs/decisoes/07-repositorios-e-plano.md → scripts/clean_code.py
- `Primeira semana (23/10 a 02/11)` --references--> `main()`  [INFERRED]
  docs/decisoes/07-repositorios-e-plano.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (238 total, 110 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.07
Nodes (11): BucketResult, BucketRule, cors(), events(), icon(), leads(), page(), preflight() (+3 more)

### Community 1 - "test_alerts.py"
Cohesion: 0.10
Nodes (5): invite(), options(), staff(), StaffInviteIn, StaffService

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.06
Nodes (25): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+17 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "_member_client"
Cohesion: 0.10
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (19): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+11 more)

### Community 7 - "goals/controller.py"
Cohesion: 0.18
Nodes (5): delete_template(), role_goals(), set_role_goal(), update_template(), RoleGoalIn

### Community 8 - "steps"
Cohesion: 0.08
Nodes (25): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, jobs, test, name (+17 more)

### Community 9 - "_month"
Cohesion: 0.08
Nodes (11): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+3 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (21): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+13 more)

### Community 11 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 12 - "InvoiceService"
Cohesion: 0.08
Nodes (10): add_item(), delete(), delete_service(), issue(), pay(), remove_item(), return_to_draft(), update_item() (+2 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.08
Nodes (8): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "AdTagService"
Cohesion: 0.11
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.11
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), InviteIn, InvitationService, InvitationOut

### Community 18 - "security.py"
Cohesion: 0.08
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

### Community 22 - "typing"
Cohesion: 0.04
Nodes (11): _google(), _mailer(), GeoLiteCountries, NoCountries, NoEvents, MemoryCounter, MemoryRewardBuffer, RedisRewardBuffer (+3 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "Actor"
Cohesion: 0.13
Nodes (8): cascade_hours(), history(), index(), set_status(), settings(), sites(), update_blocks(), update_settings()

### Community 26 - "clean_code.py"
Cohesion: 0.18
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "ClientPriceRuleService"
Cohesion: 0.12
Nodes (14): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+6 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.09
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "floor_cache.py"
Cohesion: 0.19
Nodes (4): forget_cascades(), forget_floors(), forget_rule(), forget_site()

### Community 30 - "reports/service.py"
Cohesion: 0.05
Nodes (16): QueryTooHeavy, catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn (+8 more)

### Community 31 - "CapturingMailer"
Cohesion: 0.07
Nodes (44): CapturingMailer, Sent, _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit() (+36 more)

### Community 32 - "RewardService"
Cohesion: 0.09
Nodes (6): create(), forget_pages(), create(), RewardIn, RewardOut, RewardService

### Community 36 - "test_price_rules.py"
Cohesion: 0.15
Nodes (25): _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _present(), _rule(), _seed_caches() (+17 more)

### Community 37 - "tasks/controller.py"
Cohesion: 0.05
Nodes (17): change(), comment(), create(), task(), tasks(), TaskClientOut, TaskCommentIn, TaskDataIn (+9 more)

### Community 38 - "modules/ad_tags/dto.py"
Cohesion: 0.11
Nodes (11): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagDraftIO, AdTagHealthDayOut, AdTagIn, AdTagLiveOut (+3 more)

### Community 39 - "PublicAdTagService"
Cohesion: 0.08
Nodes (11): Bucket, RewardBuffer, RewardCache, config(), page_views(), preflight(), public_ad_tag_service(), PageViewIn (+3 more)

### Community 40 - "clients/controller.py"
Cohesion: 0.20
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 41 - "test_company_image.py"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 42 - "documents/controller.py"
Cohesion: 0.12
Nodes (7): documents(), download(), upload(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "test_alerts.py"
Cohesion: 0.15
Nodes (7): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), _form()

### Community 44 - "SiteChecklistService"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 45 - "Services"
Cohesion: 0.04
Nodes (16): Services, get_services(), company_service(), document_service(), client_ad_tag_service(), gam_tool_service(), client_loader_service(), staff_service() (+8 more)

### Community 46 - "uuid"
Cohesion: 0.13
Nodes (18): refresh_levels(), test_busy_export_answers_503_with_retry_after(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run(), _day(), _metrics(), _row(), test_batch_refuses_bad_sections_and_needs_permission() (+10 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "ChecklistDetailOut"
Cohesion: 0.11
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), site_checklist_service(), ChecklistDetailOut (+2 more)

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "_month"
Cohesion: 0.14
Nodes (5): _check_jpeg_size(), PillowImageProcessor, _sharpness(), _striped_logo(), test_wide_and_palette_logos_stay_sharp()

### Community 52 - "MemoryCounter"
Cohesion: 0.08
Nodes (13): metrics(), RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut (+5 more)

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.06
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "typing"
Cohesion: 0.08
Nodes (8): KeyValueBuffer, MemoryKeyValueBuffer, RedisKeyValueBuffer, _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 57 - "clients"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "key_values/service.py"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.10
Nodes (12): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+4 more)

### Community 60 - "account/controller.py"
Cohesion: 0.08
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "client_documents/controller.py"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 62 - "Actor"
Cohesion: 0.12
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "commissions/controller.py"
Cohesion: 0.06
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 64 - "SessionCookies"
Cohesion: 0.09
Nodes (16): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), login(), me(), set_active_company() (+8 more)

### Community 65 - "errors.py"
Cohesion: 0.08
Nodes (11): CompanyChanged, error_body(), ExportsBusy, install(), domain_error(), http_error(), redis_unavailable(), unexpected() (+3 more)

### Community 66 - "invoices/controller.py"
Cohesion: 0.25
Nodes (6): show(), CompanyDetailOut, CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 68 - "export.py"
Cohesion: 0.11
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "limits.py"
Cohesion: 0.10
Nodes (9): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+1 more)

### Community 70 - "Actor"
Cohesion: 0.07
Nodes (16): create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned(), query() (+8 more)

### Community 71 - "ClientAdTagService"
Cohesion: 0.09
Nodes (13): AdTagOut, create(), delete(), health(), index(), publish(), restore(), set_active() (+5 more)

### Community 72 - ".of"
Cohesion: 0.09
Nodes (6): ChecklistMarkIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "networks/controller.py"
Cohesion: 0.08
Nodes (14): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+6 more)

### Community 75 - "ClientService"
Cohesion: 0.14
Nodes (3): edit_client(), remove_client_image(), ClientOut

### Community 76 - "test_events.py"
Cohesion: 0.28
Nodes (10): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports(), test_redis_source_delivers_published_messages() (+2 more)

### Community 77 - "test_reward_public.py"
Cohesion: 0.07
Nodes (25): FixedCountries, reward_cache_key(), _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), test_upload_without_session_is_refused_before_reading_the_body(), _buffer() (+17 more)

### Community 78 - "PriceRuleService"
Cohesion: 0.09
Nodes (5): set_floor(), show(), price_rule_service(), PriceRuleDetailsOut, PriceRuleService

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 81 - "results/dto.py"
Cohesion: 0.05
Nodes (10): results(), client_result_service(), ClientResultService, show(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut (+2 more)

### Community 82 - "events.py"
Cohesion: 0.08
Nodes (9): channel(), EventSource, _parse(), sse(), StreamLimiter, events(), event_service(), EventService (+1 more)

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 85 - "internal/rewards/controller.py"
Cohesion: 0.08
Nodes (13): ad_units(), delete(), delete_lead(), export_leads(), leads(), set_active(), set_icon(), show() (+5 more)

### Community 86 - "sites/service.py"
Cohesion: 0.25
Nodes (8): AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn, SitesPatchIn

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "price_floor_public/service.py"
Cohesion: 0.09
Nodes (7): CountryLookup, is_cascade_shape(), safe_site_cascades(), site_cascades(), prices(), PublicPriceFloorsOut, PublicPriceFloorService

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 92 - "LoaderService"
Cohesion: 0.05
Nodes (19): create(), delete(), index(), options(), show(), update(), create(), delete() (+11 more)

### Community 94 - "google/controller.py"
Cohesion: 0.04
Nodes (15): GoogleUnavailable, GoogleAuth, new_verifier(), Settings, google_callback(), google_start(), google_status(), google_unlink() (+7 more)

### Community 95 - "modules/price_rules/controller.py"
Cohesion: 0.27
Nodes (12): CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigOut, PriceRuleFloorIn, PriceRuleHistoryOut, PriceRuleOut (+4 more)

### Community 96 - "_csrf"
Cohesion: 0.19
Nodes (10): _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads() (+2 more)

### Community 97 - "reward_public/service.py"
Cohesion: 0.14
Nodes (13): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicRewardPriceOut (+5 more)

### Community 98 - "invoices/controller.py"
Cohesion: 0.09
Nodes (16): create_service(), payment_details(), save_payment_details(), update_service(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn (+8 more)

### Community 102 - "ad_tag_public/dto.py"
Cohesion: 0.12
Nodes (5): PageViewBlockIn, PublicBlockOut, PublicLoaderOut, PublicMgidOut, PublicTagOut

### Community 123 - "MemoryBucket"
Cohesion: 0.16
Nodes (5): MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "auth/controller.py"
Cohesion: 0.08
Nodes (4): get_invitation(), auth_service(), InvitationPreviewOut, AuthService

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 130 - "PriceRuleConfigIn"
Cohesion: 0.21
Nodes (3): update_config(), PriceRuleConfigIn, stored_drop_tiers()

### Community 131 - "main.py"
Cohesion: 0.06
Nodes (9): RedisCounter, configure_logging(), JsonFormatter, observe(), _route_template(), create_app(), test_docs_are_closed_in_production(), test_every_response_has_the_security_headers() (+1 more)

### Community 132 - "contracts/controller.py"
Cohesion: 0.06
Nodes (24): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, contract(), contract_networks() (+16 more)

### Community 133 - "UnitOfWorkFactory"
Cohesion: 0.06
Nodes (4): ad_tag_cache_key(), UnitOfWorkFactory, forget_tags(), page_out()

### Community 134 - ".page"
Cohesion: 0.10
Nodes (5): index(), audit_service(), AuditService, SchedulePageOut, PageOut

### Community 135 - "test_staff_without_permission_and_other_clients"
Cohesion: 0.38
Nodes (8): _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission(), test_staff_without_permission_and_other_clients()

### Community 136 - "ad_units"
Cohesion: 0.16
Nodes (4): ad_units(), link(), unlinked(), AdUnitOut

### Community 142 - ".assign"
Cohesion: 0.25
Nodes (5): Atribuição de sites, GAM, Networks, Sites e ad units, assign_sites()

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.38
Nodes (11): _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice(), test_reset_link_burns_after_five_wrong_codes() (+3 more)

### Community 145 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 146 - "get"
Cohesion: 0.10
Nodes (9): health(), metrics(), available_months(), get(), mine(), pdf(), service_options(), services() (+1 more)

### Community 147 - "test_who_sees_and_changes_invoices"
Cohesion: 0.06
Nodes (44): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+36 more)

### Community 148 - "test_database.py"
Cohesion: 0.31
Nodes (4): engine_options(), _settings(), test_every_connection_has_a_statement_and_idle_timeout(), test_pool_is_bounded_and_waits_little()

### Community 149 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 150 - "Actor"
Cohesion: 0.06
Nodes (5): create(), SavedReportIn, SavedReportOut, export_slot(), ReportService

### Community 152 - ".__init__"
Cohesion: 0.07
Nodes (10): client(), engine(), mailer(), _error_code(), test_deployed_cookies_use_the_host_prefix(), test_every_write_route_refuses_another_site(), _jpeg(), test_phone_photos_pass_and_huge_pngs_are_refused() (+2 more)

### Community 158 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 163 - "TaskQueue"
Cohesion: 0.06
Nodes (11): TaskQueue, confirm_network(), register_network(), reject_network(), unassigned_networks(), mcm_service(), ClientNetworkIn, McmCandidateOut (+3 more)

### Community 164 - "image_response"
Cohesion: 0.16
Nodes (3): client_info(), image_response(), image_upload()

### Community 166 - "test_account.py"
Cohesion: 0.33
Nodes (7): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 167 - "UserOut"
Cohesion: 0.12
Nodes (7): Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PeopleService

### Community 168 - "clients/controller.py"
Cohesion: 0.10
Nodes (11): cancel_owner(), change_status(), client(), client_image(), client_options(), edit_client_image(), invite_owner(), manager_change() (+3 more)

### Community 174 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 177 - "Actor"
Cohesion: 0.20
Nodes (4): classify(), classify_many(), site_options(), sites_of_member()

### Community 180 - "health/controller.py"
Cohesion: 0.17
Nodes (3): ready(), health_service(), HealthService

### Community 184 - "Avant: conexão com o GAM"
Cohesion: 0.25
Nodes (7): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação

### Community 186 - "test_permissions_on_keys"
Cohesion: 0.50
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 192 - "test_staff_sees_client_networks_sites_and_revenue_status"
Cohesion: 0.38
Nodes (3): _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 195 - "key_values/service.py"
Cohesion: 0.08
Nodes (14): Network, Segurança e limites, POSTGRES_PASSWORD, env, image, options, ports, postgres (+6 more)

### Community 196 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 201 - "_site"
Cohesion: 0.33
Nodes (5): _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back()

### Community 204 - "clients/controller.py"
Cohesion: 0.12
Nodes (14): owner_invitations(), client_service(), ClientDetailOut, ClientIn, ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+6 more)

### Community 214 - "UserOut"
Cohesion: 0.23
Nodes (5): PersonOut, person_out(), CompanyRefOut, RoleRefOut, UserOut

### Community 223 - "Actor"
Cohesion: 0.11
Nodes (3): client_teams(), ClientMemberOut, ClientService

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2359 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **110 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `auth/controller.py`, `test_alerts.py`, `PublicRewardService`, `DashboardService`, `Actor`, `contracts/controller.py`, `.page`, `GamToolService`, `roles/controller.py`, `_month`, `InvoiceService`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `PageOut`, `custom_metrics/controller.py`, `SiteService`, `Actor`, `goals/controller.py`, `ClientPriceRuleService`, `mfa/controller.py`, `reports/service.py`, `RewardService`, `TaskQueue`, `goals/service.py`, `tasks/controller.py`, `PublicAdTagService`, `UserOut`, `clients/controller.py`, `documents/controller.py`, `client_documents/service.py`, `ChecklistDetailOut`, `Actor`, `Services`, `networks/service.py`, `currencies/controller.py`, `members/controller.py`, `.__init__`, `clients`, `.__init__`, `account/controller.py`, `commissions/controller.py`, `SessionCookies`, `invoices/controller.py`, `.update`, `ClientAdTagService`, `networks/controller.py`, `clients/controller.py`, `PriceRuleService`, `image`, `ClientDocumentsOut`, `results/dto.py`, `.__init__`, `UserOut`, `sites/service.py`, `price_floor_public/service.py`, `.__init__`, `LoaderService`, `google/controller.py`, `Actor`, `.__init__`, `.__init__`, `invoices/controller.py`, `modules/price_rules/controller.py`, `.__init__`, `reward_public/service.py`, `.__init__`, `.__init__`?**
  _High betweenness centrality (0.125) - this node is a cross-community bridge._
- **Are the 159 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 159 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PublicRewardService` be split into smaller, more focused modules?**
  _Cohesion score 0.07058823529411765 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `.page` to `test_alerts.py`, `roles/controller.py`, `DashboardService`, `Actor`, `UnitOfWorkFactory`, `contracts/controller.py`, `GamToolService`, `goals/controller.py`, `clients`, `ad_units`, `InvoiceService`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `get`, `PageOut`, `SiteService`, `Actor`, `ClientPriceRuleService`, `reports/service.py`, `RewardService`, `TaskQueue`, `goals/service.py`, `tasks/controller.py`, `UserOut`, `SiteChecklistService`, `ChecklistDetailOut`, `Actor`, `Services`, `SiteOut`, `members/controller.py`, `modules/rewards/controller.py`, `AuditOut`, `.update`, `ClientAdTagService`, `networks/controller.py`, `clients/controller.py`, `PriceRuleService`, `image`, `results/dto.py`, `Actor`, `.of`, `internal/rewards/controller.py`, `UserOut`, `sites/service.py`, `UUID`, `LoaderService`, `Actor`, `modules/price_rules/controller.py`, `invoices/controller.py`?**
  _High betweenness centrality (0.105) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_alerts.py` be split into smaller, more focused modules?**
  _Cohesion score 0.09655172413793103 - nodes in this community are weakly interconnected._