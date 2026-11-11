# Graph Report - avant-api  (2026-11-11)

## Corpus Check
- 373 files · ~117,016 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 5202 nodes · 14620 edges · 254 communities (132 shown, 122 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2411 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `df7807b5`
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
- .catalog
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
- reward_buffer.py
- goals/controller.py
- verify
- networks/controller.py
- clean_code.py
- ClientPriceRuleService
- mfa/controller.py
- floor_cache.py
- reports/service.py
- _onboard_owner
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
- CapturingMailer
- networks/service.py
- ChecklistDetailOut
- download
- Services
- _month
- MemoryCounter
- edit
- test_company_image.py
- members/controller.py
- typing
- clients
- FakeGoogle
- modules/rewards/controller.py
- account/controller.py
- client_documents/controller.py
- Actor
- commissions/controller.py
- SessionCookies
- install
- invoices/controller.py
- .open
- export.py
- limits.py
- Actor
- ClientAdTagService
- .of
- avant-api
- networks/controller.py
- .of
- test_events.py
- test_reward_public.py
- PriceRuleService
- image
- results/dto.py
- events.py
- uuid
- .of
- internal/rewards/controller.py
- sites/service.py
- Avant: grupos na Empresa e imagem da Empresa
- RateLimited
- Groone Avant: contexto do projeto
- .assign
- LoaderService
- google/controller.py
- PublicRewardService
- checklists/controller.py
- reward_public/service.py
- invoices/controller.py
- ad_tag_public/dto.py
- limits.py
- updates
- Avant: repositório e plano do MVP
- stored_drop_tiers
- main.py
- contracts/controller.py
- UnitOfWorkFactory
- .page
- test_staff_without_permission_and_other_clients
- ad_units
- clients
- typing
- SupportTaskService
- Arquitetura do MVP do Avant
- test_mfa.py
- GoalService
- get
- test_who_sees_and_changes_invoices
- gam_tools/controller.py
- UUID
- Actor
- .__init__
- GoalTemplateIn
- mark
- mine
- CompanyService
- ClientOut
- modules/loaders/controller.py
- McmService
- image_response
- goals/service.py
- test_account.py
- UserOut
- client_image
- image
- team
- GamToolNetworkOut
- Actor
- UserOut
- health/controller.py
- tasks
- .of
- test_permissions_on_keys
- capped
- gam_tools/dto.py
- TaskQueue
- .of_view
- key_values/service.py
- package.json
- ClientLoaderService
- CascadeHourOut
- _site
- .of
- ClientService
- rewards/http.py
- show
- gam_tools/service.py
- edit_image
- create
- index
- modules/loaders/dto.py
- .to_data
- countries.py
- shared/dto.py
- logs.py
- LoaderOptionOut
- document_response
- price_floor_public/controller.py
- .of
- postgres
- .start
- ads_txt
- router.py
- tasks/dependencies.py

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 204 edges
2. `PageOut` - 193 edges
3. `_csrf()` - 172 edges
4. `get()` - 171 edges
5. `_onboard_owner()` - 164 edges
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
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (254 total, 122 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.12
Nodes (9): client_address(), events(), icon(), leads(), page(), preflight(), read_body(), RewardEventsIn (+1 more)

### Community 1 - "test_alerts.py"
Cohesion: 0.12
Nodes (4): invite(), options(), StaffInviteIn, StaffService

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (24): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+16 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "_member_client"
Cohesion: 0.10
Nodes (17): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

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
Cohesion: 0.05
Nodes (36): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+28 more)

### Community 11 - ".catalog"
Cohesion: 0.08
Nodes (4): templates(), DashboardTemplateOut, catalog(), LabelOut

### Community 12 - "InvoiceService"
Cohesion: 0.07
Nodes (9): add_item(), create_service(), remove_item(), services(), update_item(), update_service(), InvoiceOut, InvoiceServiceOut (+1 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.12
Nodes (7): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "AdTagService"
Cohesion: 0.12
Nodes (12): delete(), health(), index(), publish(), restore(), set_active(), show(), units() (+4 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.11
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.09
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "security.py"
Cohesion: 0.05
Nodes (23): api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor(), get_auth(), get_session_actor(), get_session_auth() (+15 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "networks/controller.py"
Cohesion: 0.08
Nodes (8): mcm_service(), ClientNetworkIn, McmCandidateOut, service_account(), network_service(), NetworkIn, ServiceAccountOut, SyncRunOut

### Community 26 - "clean_code.py"
Cohesion: 0.15
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "ClientPriceRuleService"
Cohesion: 0.05
Nodes (17): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+9 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "floor_cache.py"
Cohesion: 0.27
Nodes (3): forget_cascades(), forget_floors(), forget_site()

### Community 30 - "reports/service.py"
Cohesion: 0.06
Nodes (23): query_batch(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn (+15 more)

### Community 31 - "_onboard_owner"
Cohesion: 0.11
Nodes (31): _onboard_owner(), _owner_invite(), test_busy_export_answers_503_with_retry_after(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run(), test_costs_and_reports_come_in_pages(), test_internal_client_lists_come_in_pages(), test_internal_lists_come_in_pages() (+23 more)

### Community 32 - "RewardService"
Cohesion: 0.08
Nodes (7): forget_pages(), create(), index(), update(), RewardIn, RewardOut, RewardService

### Community 36 - "test_price_rules.py"
Cohesion: 0.14
Nodes (27): _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _offerwall_unit(), _present(), _rule() (+19 more)

### Community 37 - "tasks/controller.py"
Cohesion: 0.20
Nodes (10): TaskClientOut, TaskCommentIn, TaskDataIn, TaskEventOut, TaskIn, TaskNetworkOut, TaskOut, TaskPatchIn (+2 more)

### Community 38 - "modules/ad_tags/dto.py"
Cohesion: 0.17
Nodes (13): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagHealthDayOut, AdTagHealthOut, AdTagIn, AdTagLiveOut (+5 more)

### Community 39 - "PublicAdTagService"
Cohesion: 0.12
Nodes (7): config(), page_views(), preflight(), public_ad_tag_service(), PageViewIn, PublicAdTagService, cors()

### Community 40 - "clients/controller.py"
Cohesion: 0.12
Nodes (6): edit_appearance(), image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 41 - "test_company_image.py"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 42 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 43 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company()

### Community 44 - "SiteChecklistService"
Cohesion: 0.21
Nodes (3): months(), summary(), ChecklistMonthOut

### Community 45 - "Services"
Cohesion: 0.05
Nodes (13): Services, get_services(), known_companies(), alert_service(), company_service(), dashboard_service(), contract_service(), client_result_service() (+5 more)

### Community 46 - "CapturingMailer"
Cohesion: 0.08
Nodes (22): CapturingMailer, client(), engine(), mailer(), Sent, _checkouts(), test_report_requests_use_few_connections(), query() (+14 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "ChecklistDetailOut"
Cohesion: 0.13
Nodes (4): checklist(), site_checklist_service(), ChecklistDetailOut, SiteChecklistService

### Community 49 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "_month"
Cohesion: 0.12
Nodes (3): ExportsBusy, _check_jpeg_size(), PillowImageProcessor

### Community 52 - "MemoryCounter"
Cohesion: 0.09
Nodes (14): reward_service(), RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut (+6 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "test_company_image.py"
Cohesion: 0.15
Nodes (11): _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), test_phone_photos_pass_and_huge_pngs_are_refused() (+3 more)

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "typing"
Cohesion: 0.09
Nodes (7): MemoryKeyValueBuffer, RedisKeyValueBuffer, _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.11
Nodes (9): ad_units(), delete(), delete_lead(), export_leads(), leads(), metrics(), set_active(), set_icon() (+1 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "client_documents/controller.py"
Cohesion: 0.14
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 62 - "Actor"
Cohesion: 0.14
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "commissions/controller.py"
Cohesion: 0.06
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 64 - "SessionCookies"
Cohesion: 0.07
Nodes (17): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+9 more)

### Community 65 - "install"
Cohesion: 0.25
Nodes (7): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 66 - "invoices/controller.py"
Cohesion: 0.19
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 67 - ".open"
Cohesion: 0.11
Nodes (3): SessionCookies, get_cookies(), test_closing_deployed_cookies_keeps_them_secure()

### Community 68 - "export.py"
Cohesion: 0.08
Nodes (12): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell() (+4 more)

### Community 69 - "limits.py"
Cohesion: 0.09
Nodes (9): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter() (+1 more)

### Community 70 - "Actor"
Cohesion: 0.08
Nodes (10): delete(), export(), export_saved(), index(), pin(), pinned(), run(), show() (+2 more)

### Community 71 - "ClientAdTagService"
Cohesion: 0.12
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 72 - ".of"
Cohesion: 0.17
Nodes (3): ChecklistNoteOut, ChecklistPersonOut, ChecklistRowOut

### Community 74 - "networks/controller.py"
Cohesion: 0.11
Nodes (9): connect(), disconnect(), index(), options(), show(), sync(), sync_runs(), NetworkDetailOut (+1 more)

### Community 76 - "test_events.py"
Cohesion: 0.28
Nodes (10): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports(), test_redis_source_delivers_published_messages() (+2 more)

### Community 77 - "test_reward_public.py"
Cohesion: 0.09
Nodes (18): FixedCountries, _buffer(), _cascade_reward(), test_events_and_leads_go_to_the_buffer(), test_icon_route_has_the_ip_limit(), test_public_config_is_cached_and_cleared(), test_reward_page_has_cascade_for_rewards_block(), test_reward_page_has_no_cascade_for_other_country() (+10 more)

### Community 78 - "PriceRuleService"
Cohesion: 0.07
Nodes (27): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+19 more)

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 81 - "results/dto.py"
Cohesion: 0.06
Nodes (8): results(), ClientResultService, show(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut, default_period()

### Community 82 - "events.py"
Cohesion: 0.07
Nodes (10): channel(), EventSource, NoEvents, _parse(), sse(), StreamLimiter, events(), event_service() (+2 more)

### Community 83 - "uuid"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - ".of"
Cohesion: 0.13
Nodes (3): forget_tag(), create(), AdTagOut

### Community 85 - "internal/rewards/controller.py"
Cohesion: 0.10
Nodes (14): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+6 more)

### Community 86 - "sites/service.py"
Cohesion: 0.19
Nodes (9): site_service(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn (+1 more)

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "RateLimited"
Cohesion: 0.14
Nodes (3): RateLimited, BucketRule, prices()

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 91 - ".assign"
Cohesion: 0.16
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 92 - "LoaderService"
Cohesion: 0.20
Nodes (4): create(), LoaderIn, LoaderOut, LoaderService

### Community 94 - "google/controller.py"
Cohesion: 0.03
Nodes (24): _google(), CompanyChanged, CsrfFailed, GoogleFailed, GoogleUnavailable, NoActiveCompany, QueryTooHeavy, challenge() (+16 more)

### Community 95 - "PublicRewardService"
Cohesion: 0.11
Nodes (5): reward_cache_key(), public_reward_service(), PublicRewardPriceOut, public_control_percent(), PublicRewardService

### Community 96 - "checklists/controller.py"
Cohesion: 0.17
Nodes (4): checklists(), ChecklistMarkIn, ChecklistNoteIn, ChecklistOut

### Community 97 - "reward_public/service.py"
Cohesion: 0.22
Nodes (10): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicStyleOut (+2 more)

### Community 98 - "invoices/controller.py"
Cohesion: 0.12
Nodes (13): available_months(), save_payment_details(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceSummaryOut (+5 more)

### Community 102 - "ad_tag_public/dto.py"
Cohesion: 0.13
Nodes (6): PageViewBlockIn, PublicAdTagOut, PublicBlockOut, PublicLoaderOut, PublicMgidOut, PublicTagOut

### Community 123 - "limits.py"
Cohesion: 0.06
Nodes (8): BucketResult, MemoryBucket, MemoryCounter, RedisBucket, RedisCounter, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 131 - "main.py"
Cohesion: 0.04
Nodes (18): engine_options(), _mailer(), observe(), _route_template(), MemoryRewardCache, check_fetch_site(), Settings, CeleryQueue (+10 more)

### Community 132 - "contracts/controller.py"
Cohesion: 0.06
Nodes (23): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, O que já tem, contract(), contract_networks() (+15 more)

### Community 133 - "UnitOfWorkFactory"
Cohesion: 0.04
Nodes (11): ad_tag_cache_key(), CountryLookup, Bucket, UnitOfWorkFactory, is_cascade_shape(), safe_site_cascades(), site_cascades(), RewardBuffer (+3 more)

### Community 134 - ".page"
Cohesion: 0.10
Nodes (5): index(), audit_service(), AuditService, page_out(), PageOut

### Community 135 - "test_staff_without_permission_and_other_clients"
Cohesion: 0.38
Nodes (8): _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission(), test_staff_without_permission_and_other_clients()

### Community 136 - "ad_units"
Cohesion: 0.15
Nodes (5): ad_units(), link(), unlinked(), AdUnitOut, SiteService

### Community 142 - "SupportTaskService"
Cohesion: 0.19
Nodes (4): comment(), create(), TaskDetailOut, SupportTaskService

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "test_mfa.py"
Cohesion: 0.21
Nodes (14): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code() (+6 more)

### Community 145 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 146 - "get"
Cohesion: 0.07
Nodes (14): health(), metrics(), create(), delete(), delete_service(), get(), issue(), mine() (+6 more)

### Community 147 - "test_who_sees_and_changes_invoices"
Cohesion: 0.05
Nodes (48): _csrf(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it() (+40 more)

### Community 148 - "gam_tools/controller.py"
Cohesion: 0.19
Nodes (6): install(), network(), networks(), run(), runs(), GamToolRunOut

### Community 149 - "UUID"
Cohesion: 0.16
Nodes (4): assign_sites(), delete(), members(), SiteMemberOut

### Community 150 - "Actor"
Cohesion: 0.06
Nodes (6): create(), create_from_template(), duplicate(), SavedReportOut, export_slot(), ReportService

### Community 152 - ".__init__"
Cohesion: 0.07
Nodes (17): refresh_levels(), _error_code(), test_csrf_is_required_for_writes(), test_deployed_cookies_use_the_host_prefix(), test_every_write_route_refuses_another_site(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit() (+9 more)

### Community 155 - "mark"
Cohesion: 0.17
Nodes (5): add_note(), check(), delete_note(), edit_note(), mark()

### Community 158 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 160 - "CompanyService"
Cohesion: 0.21
Nodes (3): show(), CompanyDetailOut, CompanyService

### Community 162 - "modules/loaders/controller.py"
Cohesion: 0.17
Nodes (5): delete(), index(), show(), update(), loader_service()

### Community 163 - "McmService"
Cohesion: 0.13
Nodes (6): confirm_network(), register_network(), reject_network(), unassigned_networks(), McmService, NetworkOut

### Community 164 - "image_response"
Cohesion: 0.16
Nodes (3): client_info(), image_response(), image_upload()

### Community 166 - "test_account.py"
Cohesion: 0.33
Nodes (7): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 167 - "UserOut"
Cohesion: 0.11
Nodes (8): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out()

### Community 174 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 175 - "GamToolNetworkOut"
Cohesion: 0.18
Nodes (4): GamToolClientOut, GamToolNetworkDetailOut, GamToolNetworkOut, GamToolSiteOut

### Community 177 - "Actor"
Cohesion: 0.17
Nodes (5): classify(), classify_many(), create(), site_options(), sites_of_member()

### Community 178 - "UserOut"
Cohesion: 0.12
Nodes (3): edit_image(), remove_image(), UserOut

### Community 180 - "health/controller.py"
Cohesion: 0.17
Nodes (3): ready(), health_service(), HealthService

### Community 182 - "tasks"
Cohesion: 0.15
Nodes (3): change(), task(), tasks()

### Community 186 - "test_permissions_on_keys"
Cohesion: 0.38
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 195 - "key_values/service.py"
Cohesion: 0.12
Nodes (6): KeyValueBuffer, cors(), preflight(), receive(), KeyValueIn, receive_key_values()

### Community 196 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 197 - "ClientLoaderService"
Cohesion: 0.12
Nodes (7): delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService

### Community 201 - "_site"
Cohesion: 0.33
Nodes (5): _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back()

### Community 204 - "ClientService"
Cohesion: 0.05
Nodes (28): audit(), cancel_owner(), change_status(), client(), client_options(), edit_client(), edit_client_image(), invite_owner() (+20 more)

### Community 210 - "rewards/http.py"
Cohesion: 0.18
Nodes (3): csv_response(), lead_filter(), period()

### Community 215 - "edit_image"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 223 - "shared/dto.py"
Cohesion: 0.11
Nodes (4): client_teams(), ClientMemberOut, CompanyRefOut, RoleRefOut

### Community 241 - "postgres"
Cohesion: 0.33
Nodes (6): POSTGRES_PASSWORD, env, image, options, ports, postgres

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2362 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **122 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `test_alerts.py`, `roles/controller.py`, `DashboardService`, `Actor`, `contracts/controller.py`, `.page`, `GamToolService`, `ad_units`, `_month`, `InvoiceService`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `security.py`, `custom_metrics/controller.py`, `SupportTaskService`, `PageOut`, `Actor`, `goals/controller.py`, `networks/controller.py`, `ClientPriceRuleService`, `mfa/controller.py`, `reports/service.py`, `CompanyService`, `RewardService`, `McmService`, `goals/service.py`, `modules/ad_tags/dto.py`, `PublicAdTagService`, `UserOut`, `tasks/controller.py`, `documents/controller.py`, `clients/controller.py`, `Services`, `networks/service.py`, `ChecklistDetailOut`, `Services`, `MemoryCounter`, `members/controller.py`, `.__init__`, `clients`, `.__init__`, `account/controller.py`, `client_documents/controller.py`, `commissions/controller.py`, `SessionCookies`, `TaskQueue`, `invoices/controller.py`, `limits.py`, `ClientLoaderService`, `ClientAdTagService`, `networks/controller.py`, `ClientService`, `PriceRuleService`, `image`, `results/dto.py`, `.__init__`, `internal/rewards/controller.py`, `gam_tools/service.py`, `sites/service.py`, `.__init__`, `LoaderService`, `google/controller.py`, `PublicRewardService`, `checklists/controller.py`, `.__init__`, `invoices/controller.py`, `.__init__`, `.__init__`, `.__init__`, `.__init__`?**
  _High betweenness centrality (0.136) - this node is a cross-community bridge._
- **Are the 159 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 159 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PublicRewardService` be split into smaller, more focused modules?**
  _Cohesion score 0.11954022988505747 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `.page` to `test_alerts.py`, `roles/controller.py`, `DashboardService`, `Actor`, `UnitOfWorkFactory`, `contracts/controller.py`, `GamToolService`, `goals/controller.py`, `clients`, `_month`, `ad_units`, `InvoiceService`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `get`, `SupportTaskService`, `gam_tools/controller.py`, `PageOut`, `networks/controller.py`, `ClientPriceRuleService`, `reports/service.py`, `RewardService`, `modules/loaders/controller.py`, `McmService`, `goals/service.py`, `modules/ad_tags/dto.py`, `UserOut`, `tasks/controller.py`, `Actor`, `Services`, `ChecklistDetailOut`, `Actor`, `Services`, `MemoryCounter`, `tasks`, `members/controller.py`, `modules/rewards/controller.py`, `ClientLoaderService`, `ClientAdTagService`, `networks/controller.py`, `ClientService`, `PriceRuleService`, `image`, `results/dto.py`, `.of`, `internal/rewards/controller.py`, `gam_tools/service.py`, `sites/service.py`, `index`, `LoaderService`, `shared/dto.py`, `checklists/controller.py`, `invoices/controller.py`, `router.py`?**
  _High betweenness centrality (0.104) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_alerts.py` be split into smaller, more focused modules?**
  _Cohesion score 0.12333333333333334 - nodes in this community are weakly interconnected._