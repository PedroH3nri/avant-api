# Graph Report - avant-api  (2026-11-11)

## Corpus Check
- 373 files · ~116,296 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 10 file(s) not represented in the graph (top: (none) 7, .ttf 2, .lock 1)

## Summary
- 5193 nodes · 14592 edges · 239 communities (132 shown, 107 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 2410 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `42e91bb7`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _marketing_client
- test_alerts.py
- roles/controller.py
- DashboardService
- Actor
- PageOut
- GamToolService
- goals/controller.py
- steps
- _month
- Avant: models do MVP
- templates
- InvoiceService
- .uow
- inventory/dto.py
- AdTagService
- api_keys/controller.py
- PageOut
- MemoryCounter
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- main.py
- goals/controller.py
- verify
- PriceRuleService
- Groone Avant: contexto do projeto
- ClientPriceRuleService
- mfa/controller.py
- RewardCache
- reports/service.py
- _onboard_owner
- RewardService
- session-start.sh
- avant-api
- test_price_rules.py
- BaseModel
- modules/ad_tags/dto.py
- PublicAdTagService
- clients/controller.py
- test_company_image.py
- documents/controller.py
- .show
- SiteChecklistService
- Services
- uuid
- networks/service.py
- ChecklistDetailOut
- download
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
- install
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
- PriceRuleDetailsOut
- image
- PageOut
- events.py
- uuid
- .of
- internal/rewards/controller.py
- sites/service.py
- Avant: grupos na Empresa e imagem da Empresa
- reports/service.py
- PublicRewardService
- .assign
- LoaderService
- google/controller.py
- modules/price_rules/dto.py
- _csrf
- reward_public/service.py
- invoices/controller.py
- ad_tag_public/dto.py
- ClientLoaderService
- updates
- auth/controller.py
- contracts/controller.py
- SupportTaskService
- ._old_compare
- ContractService
- modules/rewards/service.py
- .page
- tasks/controller.py
- ad_units
- contracts/dto.py
- typing
- CascadeHourOut
- contracts/controller.py
- Arquitetura do MVP do Avant
- CapturingMailer
- GoalService
- get
- test_who_sees_and_changes_invoices
- modules/loaders/controller.py
- UUID
- Actor
- .__init__
- GoalTemplateIn
- .of
- mine
- company/controller.py
- ClientOut
- tasks
- TaskQueue
- image_response
- goals/service.py
- test_account.py
- UserOut
- clients/controller.py
- document_response
- .of
- team
- test_site_category_and_responsible
- Actor
- UserOut
- health/controller.py
- SiteOut
- AdTagVersionOut
- price_cascade_cache.py
- .available_months
- AdTagHealthOut
- capped
- test_report_export.py
- create
- modules/loaders/dto.py
- key_values/controller.py
- package.json
- LoaderOptionOut
- _site
- ReportQueryIn
- clients/service.py
- PriceRuleHistoryOut
- RedisRewardBuffer
- show
- .of
- avant-api
- index
- _contract_fields
- GeoLiteCountries
- TaskPatchIn
- clients/dependencies.py
- Actor

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 203 edges
2. `PageOut` - 193 edges
3. `_csrf()` - 172 edges
4. `get()` - 171 edges
5. `_onboard_owner()` - 164 edges
6. `UnitOfWorkFactory` - 163 edges
7. `Services` - 161 edges
8. `_staff()` - 80 edges
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

## Communities (239 total, 107 thin omitted)

### Community 0 - "_marketing_client"
Cohesion: 0.15
Nodes (7): client_address(), events(), icon(), leads(), page(), preflight(), read_body()

### Community 1 - "test_alerts.py"
Cohesion: 0.09
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.07
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (16): create(), delete(), events(), index(), mute(), preview(), show(), update() (+8 more)

### Community 5 - "PageOut"
Cohesion: 0.10
Nodes (30): _csrf(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _ana_id(), _report() (+22 more)

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
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.05
Nodes (36): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+28 more)

### Community 12 - "InvoiceService"
Cohesion: 0.08
Nodes (6): create_service(), services(), update_service(), InvoiceOut, InvoiceServiceOut, InvoiceService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.08
Nodes (8): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "AdTagService"
Cohesion: 0.09
Nodes (13): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+5 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.10
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.08
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "main.py"
Cohesion: 0.04
Nodes (19): engine_options(), _google(), _mailer(), NoCountries, configure_logging(), JsonFormatter, observe(), _route_template() (+11 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "PriceRuleService"
Cohesion: 0.09
Nodes (17): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+9 more)

### Community 26 - "Groone Avant: contexto do projeto"
Cohesion: 0.05
Nodes (31): Arquitetura, Como trabalhar nos repositórios, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação (+23 more)

### Community 27 - "ClientPriceRuleService"
Cohesion: 0.09
Nodes (13): cascade_hours(), history(), hours(), index(), set_floor(), settings(), show(), sites() (+5 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.06
Nodes (12): get_cookies(), confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn (+4 more)

### Community 29 - "RewardCache"
Cohesion: 0.09
Nodes (7): ad_tag_cache_key(), RewardCache, forget_tags(), forget_cascades(), forget_floors(), forget_rule(), forget_site()

### Community 30 - "reports/service.py"
Cohesion: 0.05
Nodes (16): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut, OrderIn (+8 more)

### Community 31 - "_onboard_owner"
Cohesion: 0.13
Nodes (25): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes() (+17 more)

### Community 32 - "RewardService"
Cohesion: 0.09
Nodes (5): create(), update(), RewardIn, RewardOut, RewardService

### Community 36 - "test_price_rules.py"
Cohesion: 0.15
Nodes (24): _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _present(), _rule(), _seed_caches() (+16 more)

### Community 37 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 38 - "modules/ad_tags/dto.py"
Cohesion: 0.09
Nodes (12): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagDraftIO, AdTagHealthDayOut, AdTagIn, AdTagLiveOut (+4 more)

### Community 39 - "PublicAdTagService"
Cohesion: 0.09
Nodes (10): BucketResult, BucketRule, config(), page_views(), preflight(), public_ad_tag_service(), PageViewIn, PublicAdTagService (+2 more)

### Community 40 - "clients/controller.py"
Cohesion: 0.12
Nodes (6): edit_appearance(), image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 41 - "test_company_image.py"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 42 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 44 - "SiteChecklistService"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 45 - "Services"
Cohesion: 0.03
Nodes (34): Services, CompanyChanged, CsrfFailed, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company() (+26 more)

### Community 46 - "uuid"
Cohesion: 0.11
Nodes (19): _checkouts(), test_report_requests_use_few_connections(), test_busy_export_answers_503_with_retry_after(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run(), _day(), _metrics(), _row() (+11 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "ChecklistDetailOut"
Cohesion: 0.11
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), site_checklist_service(), ChecklistDetailOut (+2 more)

### Community 49 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 52 - "MemoryCounter"
Cohesion: 0.08
Nodes (13): RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO (+5 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.14
Nodes (5): list_currencies(), update_preferences(), CurrencyOut, PreferencesIn, CurrencyService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+6 more)

### Community 56 - "typing"
Cohesion: 0.09
Nodes (7): MemoryKeyValueBuffer, RedisKeyValueBuffer, _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 57 - "clients"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "key_values/service.py"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.07
Nodes (14): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+6 more)

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
Nodes (10): SessionCookies, accept(), company_image(), do_logout(), login(), me(), set_active_company(), MeOut (+2 more)

### Community 65 - "install"
Cohesion: 0.25
Nodes (7): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error()

### Community 66 - "invoices/controller.py"
Cohesion: 0.20
Nodes (4): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 68 - "export.py"
Cohesion: 0.10
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "limits.py"
Cohesion: 0.10
Nodes (8): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter()

### Community 70 - "Actor"
Cohesion: 0.07
Nodes (15): create(), create_from_template(), delete(), export(), export_saved(), pin(), query(), query_batch() (+7 more)

### Community 71 - "ClientAdTagService"
Cohesion: 0.12
Nodes (12): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+4 more)

### Community 72 - ".of"
Cohesion: 0.09
Nodes (6): ChecklistMarkIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "networks/controller.py"
Cohesion: 0.08
Nodes (14): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+6 more)

### Community 75 - "ClientService"
Cohesion: 0.13
Nodes (9): client(), edit_client(), register_client(), remove_client_image(), ClientDetailOut, ClientIn, ClientOut, ClientPatchIn (+1 more)

### Community 76 - "test_events.py"
Cohesion: 0.12
Nodes (19): client(), engine(), mailer(), _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit() (+11 more)

### Community 77 - "test_reward_public.py"
Cohesion: 0.06
Nodes (31): FixedCountries, reward_cache_key(), _jpeg(), _png(), _put_image(), _sharpness(), _striped_logo(), test_client_changes_the_company_image() (+23 more)

### Community 78 - "PriceRuleDetailsOut"
Cohesion: 0.12
Nodes (4): set_status(), PriceRuleConfigIn, PriceRuleDetailsOut, PriceRuleStatusIn

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 81 - "PageOut"
Cohesion: 0.06
Nodes (9): UnitOfWorkFactory, AlertPageOut, results(), client_result_service(), ClientResultService, ResultsOut, default_period(), page_out() (+1 more)

### Community 82 - "events.py"
Cohesion: 0.07
Nodes (10): channel(), EventSource, NoEvents, _parse(), sse(), StreamLimiter, events(), event_service() (+2 more)

### Community 83 - "uuid"
Cohesion: 0.22
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 85 - "internal/rewards/controller.py"
Cohesion: 0.10
Nodes (14): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+6 more)

### Community 86 - "sites/service.py"
Cohesion: 0.19
Nodes (9): site_service(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn (+1 more)

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "reports/service.py"
Cohesion: 0.04
Nodes (15): CountryLookup, ExportsBusy, NoActiveCompany, QueryTooHeavy, RateLimited, KeyValueBuffer, Bucket, RewardBuffer (+7 more)

### Community 89 - "PublicRewardService"
Cohesion: 0.10
Nodes (3): public_reward_service(), public_control_percent(), PublicRewardService

### Community 91 - ".assign"
Cohesion: 0.16
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 92 - "LoaderService"
Cohesion: 0.16
Nodes (4): create(), LoaderIn, LoaderOut, LoaderService

### Community 94 - "google/controller.py"
Cohesion: 0.05
Nodes (11): GoogleUnavailable, GoogleAuth, new_verifier(), google_start(), google_status(), google_unlink(), google_redirects(), google_service() (+3 more)

### Community 95 - "modules/price_rules/dto.py"
Cohesion: 0.12
Nodes (5): CascadeTryOut, PriceRuleBlocksIn, PriceRuleConfigOut, PriceRuleOut, PriceRuleSiteSummaryOut

### Community 96 - "_csrf"
Cohesion: 0.19
Nodes (10): _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads() (+2 more)

### Community 97 - "reward_public/service.py"
Cohesion: 0.18
Nodes (13): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicRewardPriceOut (+5 more)

### Community 98 - "invoices/controller.py"
Cohesion: 0.10
Nodes (14): mine(), payment_details(), service_options(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut (+6 more)

### Community 102 - "ad_tag_public/dto.py"
Cohesion: 0.13
Nodes (6): PageViewBlockIn, PublicAdTagOut, PublicBlockOut, PublicLoaderOut, PublicMgidOut, PublicTagOut

### Community 123 - "ClientLoaderService"
Cohesion: 0.16
Nodes (7): delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService

### Community 127 - "updates"
Cohesion: 0.18
Nodes (10): imagens, patterns, interval, updates, directory, groups, package-ecosystem, schedule (+2 more)

### Community 128 - "auth/controller.py"
Cohesion: 0.10
Nodes (9): get_invitation(), auth_service(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut (+1 more)

### Community 129 - "contracts/controller.py"
Cohesion: 0.14
Nodes (7): contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), remove_contract(), contract_service()

### Community 130 - "SupportTaskService"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 131 - "._old_compare"
Cohesion: 0.08
Nodes (9): MemoryBucket, RedisBucket, RedisCounter, test_redis_limiter(), _exercise(), test_redis_bucket(), test_docs_are_closed_in_production(), test_every_response_has_the_security_headers() (+1 more)

### Community 132 - "ContractService"
Cohesion: 0.17
Nodes (5): O que já tem, new_contract(), ContractIn, ContractOut, ContractService

### Community 134 - ".page"
Cohesion: 0.13
Nodes (3): index(), audit_service(), AuditService

### Community 135 - "tasks/controller.py"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 136 - "ad_units"
Cohesion: 0.15
Nodes (5): ad_units(), link(), unlinked(), AdUnitOut, SiteService

### Community 137 - "contracts/dto.py"
Cohesion: 0.18
Nodes (6): ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut, _network_ref(), ContractClientRefOut

### Community 142 - "contracts/controller.py"
Cohesion: 0.14
Nodes (3): CostLineOut, MonthResultOut, ResultTotalsOut

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.09
Nodes (13): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+5 more)

### Community 144 - "CapturingMailer"
Cohesion: 0.13
Nodes (21): CapturingMailer, Sent, _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa() (+13 more)

### Community 145 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 146 - "get"
Cohesion: 0.07
Nodes (15): health(), metrics(), add_item(), create(), delete(), delete_service(), get(), issue() (+7 more)

### Community 147 - "test_who_sees_and_changes_invoices"
Cohesion: 0.05
Nodes (41): _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it() (+33 more)

### Community 148 - "modules/loaders/controller.py"
Cohesion: 0.16
Nodes (5): delete(), index(), show(), update(), loader_service()

### Community 149 - "UUID"
Cohesion: 0.16
Nodes (4): assign_sites(), delete(), members(), SiteMemberOut

### Community 150 - "Actor"
Cohesion: 0.06
Nodes (5): duplicate(), pinned(), SavedReportOut, export_slot(), ReportService

### Community 152 - ".__init__"
Cohesion: 0.07
Nodes (7): refresh_levels(), _error_code(), test_deployed_cookies_use_the_host_prefix(), test_every_write_route_refuses_another_site(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status()

### Community 155 - ".of"
Cohesion: 0.33
Nodes (6): POSTGRES_PASSWORD, env, image, options, ports, postgres

### Community 158 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 160 - "company/controller.py"
Cohesion: 0.18
Nodes (4): show(), CompanyDetailOut, CompanyService, image_url()

### Community 162 - "tasks"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 163 - "TaskQueue"
Cohesion: 0.06
Nodes (11): TaskQueue, confirm_network(), register_network(), reject_network(), unassigned_networks(), mcm_service(), ClientNetworkIn, McmCandidateOut (+3 more)

### Community 164 - "image_response"
Cohesion: 0.12
Nodes (3): image(), image_response(), image_upload()

### Community 166 - "test_account.py"
Cohesion: 0.33
Nodes (7): _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 167 - "UserOut"
Cohesion: 0.10
Nodes (10): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+2 more)

### Community 168 - "clients/controller.py"
Cohesion: 0.11
Nodes (12): audit(), cancel_owner(), change_status(), client_image(), client_options(), client_teams(), edit_client_image(), invite_owner() (+4 more)

### Community 172 - ".of"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 174 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 175 - "test_site_category_and_responsible"
Cohesion: 0.31
Nodes (5): _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search(), test_site_category_and_responsible(), test_sites_and_assignment()

### Community 177 - "Actor"
Cohesion: 0.17
Nodes (5): classify(), classify_many(), create(), site_options(), sites_of_member()

### Community 180 - "health/controller.py"
Cohesion: 0.16
Nodes (3): ready(), health_service(), HealthService

### Community 183 - "AdTagVersionOut"
Cohesion: 0.23
Nodes (3): versions(), AdTagVersionOut, versions()

### Community 184 - "price_cascade_cache.py"
Cohesion: 0.20
Nodes (3): is_cascade_shape(), safe_site_cascades(), site_cascades()

### Community 186 - ".available_months"
Cohesion: 0.38
Nodes (3): _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission()

### Community 191 - "test_report_export.py"
Cohesion: 0.24
Nodes (4): _result(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 195 - "key_values/controller.py"
Cohesion: 0.27
Nodes (3): cors(), preflight(), receive()

### Community 196 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 201 - "_site"
Cohesion: 0.33
Nodes (5): _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back()

### Community 204 - "clients/service.py"
Cohesion: 0.10
Nodes (7): manager_change(), ClientOptionOut, ClientProfileIn, ClientProfileOut, ClientStatusIn, ManagerChangeOut, RevenueStatusOut

### Community 216 - "avant-api"
Cohesion: 0.33
Nodes (5): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem

### Community 223 - "Actor"
Cohesion: 0.09
Nodes (4): owner_invitations(), OwnerInvitationOut, owner_invitation_out(), AuditOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2357 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **107 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `PageOut` to `auth/controller.py`, `test_alerts.py`, `SupportTaskService`, `DashboardService`, `Actor`, `ContractService`, `.page`, `GamToolService`, `modules/rewards/service.py`, `contracts/dto.py`, `tasks/controller.py`, `roles/controller.py`, `InvoiceService`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `PageOut`, `custom_metrics/controller.py`, `Actor`, `goals/controller.py`, `PriceRuleService`, `ClientPriceRuleService`, `mfa/controller.py`, `RewardCache`, `company/controller.py`, `RewardService`, `TaskQueue`, `goals/service.py`, `modules/ad_tags/dto.py`, `PublicAdTagService`, `UserOut`, `clients/controller.py`, `documents/controller.py`, `Services`, `_month`, `networks/service.py`, `ChecklistDetailOut`, `ad_units`, `Services`, `currencies/controller.py`, `members/controller.py`, `price_cascade_cache.py`, `.__init__`, `clients`, `.__init__`, `account/controller.py`, `client_documents/controller.py`, `commissions/controller.py`, `.uow`, `invoices/controller.py`, `ClientAdTagService`, `networks/controller.py`, `ClientService`, `clients/service.py`, `image`, `.__init__`, `internal/rewards/controller.py`, `sites/service.py`, `.__init__`, `reports/service.py`, `PublicRewardService`, `_contract_fields`, `LoaderService`, `google/controller.py`, `.__init__`, `.__init__`, `invoices/controller.py`, `.__init__`, `.__init__`, `reward_public/service.py`, `.__init__`, `.__init__`, `.__init__`, `ClientLoaderService`?**
  _High betweenness centrality (0.135) - this node is a cross-community bridge._
- **Are the 158 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 158 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `_marketing_client` be split into smaller, more focused modules?**
  _Cohesion score 0.14855072463768115 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `contracts/controller.py`, `test_alerts.py`, `DashboardService`, `Actor`, `ContractService`, `.page`, `GamToolService`, `goals/controller.py`, `contracts/dto.py`, `modules/rewards/service.py`, `tasks/controller.py`, `InvoiceService`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `Arquitetura do MVP do Avant`, `GoalService`, `get`, `SupportTaskService`, `PageOut`, `modules/loaders/controller.py`, `PriceRuleService`, `ClientPriceRuleService`, `RewardCache`, `reports/service.py`, `RewardService`, `tasks`, `TaskQueue`, `goals/service.py`, `modules/ad_tags/dto.py`, `UserOut`, `clients/controller.py`, `SiteChecklistService`, `ad_units`, `_month`, `ChecklistDetailOut`, `Actor`, `Services`, `SiteOut`, `members/controller.py`, `roles/controller.py`, `modules/rewards/controller.py`, `.update`, `ClientAdTagService`, `networks/controller.py`, `ClientService`, `clients/service.py`, `PriceRuleDetailsOut`, `image`, `.of`, `internal/rewards/controller.py`, `sites/service.py`, `index`, `LoaderService`, `Actor`, `invoices/controller.py`, `ClientLoaderService`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `test_alerts.py` be split into smaller, more focused modules?**
  _Cohesion score 0.0873440285204991 - nodes in this community are weakly interconnected._