# Graph Report - avant-api  (2026-11-12)

## Corpus Check
- 381 files · ~121,738 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 5361 nodes · 15181 edges · 252 communities (135 shown, 117 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2459 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d79fbdcc`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- PublicRewardService
- invoices/controller.py
- roles/controller.py
- DashboardService
- Actor
- conftest.py
- GamToolService
- Actor
- test
- _month
- Avant: models do MVP
- conftest.py
- .trusted_uow
- .uow
- inventory/dto.py
- AdTagService
- api_keys/controller.py
- PageOut
- security.py
- CustomMetricService
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- test_mail_queue.py
- goals/controller.py
- verify
- .of
- clean_code.py
- get
- mfa/controller.py
- fastapi
- ReportService
- AdTagOut
- RewardService
- session-start.sh
- avant-api
- test_price_rules.py
- .trusted_uow
- avant_core_shared_clock
- test_account.py
- mcm/controller.py
- test_gam_tools.py
- datetime
- PriceRuleService
- AuthService
- Services
- test_reports.py
- networks/service.py
- company/controller.py
- io
- Services
- .run_guarded
- MemoryCounter
- edit
- test_company_image.py
- MemberService
- test_api_keys.py
- clients
- ContractService
- modules/rewards/controller.py
- account/controller.py
- pydantic
- test_cache_down_does_not_break_the_page_or_the_save
- checklists/controller.py
- auth/controller.py
- test_hardening.py
- SessionCookies
- export.py
- test_account.py
- ClientAdTagService
- checklists/controller.py
- avant-api
- test_metrics.py
- DashboardTemplateOut
- mcm/service.py
- test_reward_public.py
- PriceRuleDetailsOut
- image
- install
- results/dto.py
- test_events.py
- test_events.py
- .export_saved
- internal/rewards/controller.py
- sites/service.py
- .approve
- RedisCounter
- Groone Avant: contexto do projeto
- .assign
- InvoiceService
- google/controller.py
- audit/controller.py
- health/controller.py
- reward_public/dto.py
- commissions/dto.py
- ad_tag_public/dto.py
- MemoryBucket
- updates
- SupportTaskService
- Avant: repositório e plano do MVP
- documents.py
- test_dashboards.py
- contracts/controller.py
- RewardCache
- _month
- CapturingMailer
- AdUnitOut
- .of
- .save_rule
- settings_for_tests
- Arquitetura do MVP do Avant
- commissions/controller.py
- GoalService
- get
- test_who_sees_and_changes_invoices
- test_documents_need_company_edit
- client_documents/service.py
- ReportQueryIn
- conftest.py
- test_networks.py
- edit_image
- CompanyService
- SiteService
- modules/loaders/controller.py
- .show
- Actor
- package.json
- reports/service.py
- UserOut
- .update_config
- internal/rewards/controller.py
- test_networks.py
- .save_payee_details
- .of
- commissions/controller.py
- UserOut
- openapi
- .build
- test_key_values.py
- tasks/controller.py
- person
- document_response
- forget_site
- image
- client_image
- postgres
- TaskQueue
- router.py
- errors.py
- document_response
- ClientLoaderService
- _month
- Actor
- ClientService
- Actor
- _out
- SiteOut
- capped
- LoaderOut
- GeoLiteCountries
- modules/loaders/dto.py
- reports/dependencies.py
- LoaderOptionOut
- RedisRewardBuffer
- _BrokenAuthService
- typing
- .available_months
- _contract_fields
- ._old_compare
- UnitOfWorkFactory
- FiscalDataOut
- .of
- .uow
- PriceRuleHistoryOut
- .of
- create

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 224 edges
2. `PageOut` - 193 edges
3. `_csrf()` - 184 edges
4. `_onboard_owner()` - 181 edges
5. `get()` - 173 edges
6. `UnitOfWorkFactory` - 163 edges
7. `Services` - 161 edges
8. `_staff()` - 84 edges
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

## Communities (252 total, 117 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.09
Nodes (12): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body() (+4 more)

### Community 1 - "invoices/controller.py"
Cohesion: 0.11
Nodes (6): mine(), InvoiceItemOut, InvoiceSummaryOut, ReturnedOut, ReturnIn, ServiceItemIn

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (12): create(), edit(), index(), options(), permissions(), remove(), PermissionOut, RoleIn (+4 more)

### Community 3 - "DashboardService"
Cohesion: 0.06
Nodes (25): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+17 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "conftest.py"
Cohesion: 0.07
Nodes (23): MemoryRewardBuffer, _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _membership_ids(), test_groups_lifecycle() (+15 more)

### Community 6 - "GamToolService"
Cohesion: 0.06
Nodes (20): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+12 more)

### Community 7 - "Actor"
Cohesion: 0.09
Nodes (4): ad_tag_cache_key(), reward_cache_key(), forget_tag(), forget_tags()

### Community 8 - "test"
Cohesion: 0.07
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, jobs (+23 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (21): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+13 more)

### Community 11 - "conftest.py"
Cohesion: 0.19
Nodes (16): run_password_reset_tasks(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable() (+8 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.09
Nodes (10): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, PageOut (+2 more)

### Community 15 - "AdTagService"
Cohesion: 0.10
Nodes (20): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+12 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.12
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.06
Nodes (13): invite(), options(), staff_service(), StaffInviteIn, StaffService, cancel(), create_invitation(), list_invitations() (+5 more)

### Community 18 - "security.py"
Cohesion: 0.07
Nodes (22): CompanyChanged, CsrfFailed, NoActiveCompany, RateLimited, api_key_actor(), bearer_token(), check_csrf(), check_tab_company() (+14 more)

### Community 19 - "CustomMetricService"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "test_mail_queue.py"
Cohesion: 0.06
Nodes (11): memory_services(), MemoryCounter, _BrokenReleaseCounter, _SpyCounter, _account(), _NoDatabase, _NoMail, _services() (+3 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.13
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.20
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "get"
Cohesion: 0.12
Nodes (12): cascade_hours(), history(), hours(), index(), set_floor(), settings(), sites(), update_blocks() (+4 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (10): confirm(), disable(), new_recovery_codes(), setup(), verify(), mfa_service(), MfaCodeIn, MfaSetupOut (+2 more)

### Community 29 - "fastapi"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.05
Nodes (19): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+11 more)

### Community 32 - "RewardService"
Cohesion: 0.12
Nodes (5): create(), forget_pages(), create(), update(), RewardIn

### Community 36 - "test_price_rules.py"
Cohesion: 0.12
Nodes (28): FixedCountries, _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _offerwall_unit(), _present() (+20 more)

### Community 38 - "avant_core_shared_clock"
Cohesion: 0.10
Nodes (3): AdTagBlockIO, AdTagDraftIO, AdTagSettingsIO

### Community 39 - "test_account.py"
Cohesion: 0.08
Nodes (15): _google(), GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _google_round() (+7 more)

### Community 40 - "mcm/controller.py"
Cohesion: 0.12
Nodes (7): confirm_network(), register_network(), reject_network(), unassigned_networks(), mcm_service(), McmService, NetworkOut

### Community 41 - "test_gam_tools.py"
Cohesion: 0.11
Nodes (15): RecordingQueue, _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites() (+7 more)

### Community 42 - "datetime"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 43 - "PriceRuleService"
Cohesion: 0.13
Nodes (9): index(), set_floor(), set_status(), settings(), show(), sites(), update_blocks(), update_config() (+1 more)

### Community 45 - "Services"
Cohesion: 0.04
Nodes (20): Services, NoCountries, RedisBucket, get_services(), ad_tag_service(), api_key_service(), auth_service(), cost_service() (+12 more)

### Community 46 - "test_reports.py"
Cohesion: 0.08
Nodes (46): _csrf(), _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session() (+38 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "company/controller.py"
Cohesion: 0.14
Nodes (6): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, image_url()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - ".run_guarded"
Cohesion: 0.11
Nodes (3): QueryTooHeavy, ReportRowOut, _statement_timeout()

### Community 52 - "MemoryCounter"
Cohesion: 0.07
Nodes (11): set_active(), RewardActiveIn, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO (+3 more)

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "test_company_image.py"
Cohesion: 0.06
Nodes (22): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, _jpeg(), _put_image(), _sharpness(), _striped_logo() (+14 more)

### Community 55 - "MemberService"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+7 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.30
Nodes (9): _bearer(), _create(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit() (+1 more)

### Community 57 - "clients"
Cohesion: 0.11
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "ContractService"
Cohesion: 0.14
Nodes (5): _is_docs_page(), observe(), _route_template(), check_fetch_site(), create_app()

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.07
Nodes (15): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+7 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "pydantic"
Cohesion: 0.13
Nodes (3): document_service(), DocumentService, document_upload()

### Community 62 - "test_cache_down_does_not_break_the_page_or_the_save"
Cohesion: 0.16
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "checklists/controller.py"
Cohesion: 0.10
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), site_checklist_service(), ChecklistDetailOut (+2 more)

### Community 64 - "auth/controller.py"
Cohesion: 0.12
Nodes (13): accept(), company_image(), do_logout(), login(), me(), set_active_company(), AcceptInvitationIn, ActiveCompanyIn (+5 more)

### Community 65 - "test_hardening.py"
Cohesion: 0.16
Nodes (11): _rendered(), test_api_key_never_reaches_the_log(), test_docs_only_for_the_groone_session_with_2fa(), test_every_response_has_the_content_security_policy(), test_every_response_has_the_security_headers(), test_invalid_bearer_is_limited_per_ip_before_the_database(), counting(), test_old_docs_paths_do_not_exist() (+3 more)

### Community 67 - "SessionCookies"
Cohesion: 0.15
Nodes (3): SessionCookies, get_cookies(), test_cookies_are_always_secure_with_the_host_prefix()

### Community 68 - "export.py"
Cohesion: 0.12
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "test_account.py"
Cohesion: 0.10
Nodes (10): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter() (+2 more)

### Community 71 - "ClientAdTagService"
Cohesion: 0.12
Nodes (12): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+4 more)

### Community 72 - "checklists/controller.py"
Cohesion: 0.09
Nodes (6): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 75 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 77 - "test_reward_public.py"
Cohesion: 0.09
Nodes (21): browser(), MemoryRewardCache, test_change_password_and_sessions(), _png(), _buffer(), _cascade_reward(), test_events_and_leads_go_to_the_buffer(), test_icon_route_has_the_ip_limit() (+13 more)

### Community 78 - "PriceRuleDetailsOut"
Cohesion: 0.11
Nodes (3): set_status(), show(), PriceRuleDetailsOut

### Community 79 - "image"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "install"
Cohesion: 0.11
Nodes (11): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), configure_logging() (+3 more)

### Community 81 - "results/dto.py"
Cohesion: 0.05
Nodes (11): results(), client_result_service(), ClientResultService, show(), result_service(), CostLineOut, MonthResultOut, ResultsOut (+3 more)

### Community 82 - "test_events.py"
Cohesion: 0.09
Nodes (9): TooManyAttempts, channel(), EventSource, _parse(), sse(), StreamLimiter, events(), EventService (+1 more)

### Community 83 - "test_events.py"
Cohesion: 0.15
Nodes (11): NoEvents, _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_events_route_refuses_above_the_cap(), test_gam_tool_runs_reach_who_sees_the_gam_tools() (+3 more)

### Community 85 - "internal/rewards/controller.py"
Cohesion: 0.11
Nodes (4): index(), show(), ClientRewardService, RewardOut

### Community 86 - "sites/service.py"
Cohesion: 0.19
Nodes (6): site_service(), AdUnitPatchIn, MemberSitesIn, SiteIn, SitePatchIn, SitesPatchIn

### Community 87 - ".approve"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "RedisCounter"
Cohesion: 0.09
Nodes (4): ExportsBusy, RedisCounter, test_redis_decr_without_key_creates_nothing(), test_redis_down_is_a_503_not_a_500()

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 91 - ".assign"
Cohesion: 0.11
Nodes (4): documents(), download(), upload(), DocumentsOut

### Community 92 - "InvoiceService"
Cohesion: 0.13
Nodes (8): create_service(), service_options(), update_service(), invoice_service(), InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceServiceOut, InvoiceService

### Community 94 - "google/controller.py"
Cohesion: 0.06
Nodes (11): GoogleUnavailable, GoogleAuth, new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), google_redirects() (+3 more)

### Community 95 - "audit/controller.py"
Cohesion: 0.12
Nodes (4): index(), audit_service(), AuditService, AuditOut

### Community 96 - "health/controller.py"
Cohesion: 0.10
Nodes (6): metrics(), ready(), health_service(), exposition(), HealthService, test_metrics_of_a_single_process()

### Community 97 - "reward_public/dto.py"
Cohesion: 0.13
Nodes (12): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicRewardPriceOut (+4 more)

### Community 98 - "commissions/dto.py"
Cohesion: 0.24
Nodes (3): CommissionMonthOut, CommissionSettingsIn, dollars()

### Community 102 - "ad_tag_public/dto.py"
Cohesion: 0.06
Nodes (14): BucketRule, RewardBuffer, config(), page_views(), preflight(), public_ad_tag_service(), PageViewBlockIn, PageViewIn (+6 more)

### Community 123 - "MemoryBucket"
Cohesion: 0.21
Nodes (5): BucketResult, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 127 - "updates"
Cohesion: 0.12
Nodes (15): patterns, update-types, dependencias, imagens, dependency-name, patterns, interval, updates (+7 more)

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 130 - "documents.py"
Cohesion: 0.25
Nodes (6): change(), comment(), create(), task(), TaskCommentIn, TaskDetailOut

### Community 131 - "test_dashboards.py"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 132 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 133 - "RewardCache"
Cohesion: 0.15
Nodes (13): CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn, PriceRuleOut (+5 more)

### Community 134 - "_month"
Cohesion: 0.18
Nodes (3): _month(), team(), PersonMonthOut

### Community 135 - "CapturingMailer"
Cohesion: 0.12
Nodes (16): CapturingMailer, client(), engine(), mailer(), Sent, test_forgot_route_never_sends_the_link_itself(), test_forgot_route_with_the_queue_down_answers_the_same_for_everyone(), test_costs_and_reports_come_in_pages() (+8 more)

### Community 136 - "AdUnitOut"
Cohesion: 0.21
Nodes (3): ad_units(), link(), AdUnitOut

### Community 137 - ".of"
Cohesion: 0.19
Nodes (7): approve(), documents(), download(), reject(), ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 138 - ".save_rule"
Cohesion: 0.12
Nodes (7): adjust(), create_rule(), delete_rule(), rules(), update_rule(), CommissionRuleIn, CommissionRuleOut

### Community 142 - "settings_for_tests"
Cohesion: 0.21
Nodes (3): TaskDataIn, TaskIn, TaskOut

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "commissions/controller.py"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 145 - "GoalService"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+10 more)

### Community 146 - "get"
Cohesion: 0.11
Nodes (14): health(), add_item(), create(), delete(), delete_service(), get(), issue(), pay() (+6 more)

### Community 147 - "test_who_sees_and_changes_invoices"
Cohesion: 0.07
Nodes (35): _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions() (+27 more)

### Community 148 - "test_documents_need_company_edit"
Cohesion: 0.22
Nodes (8): _manage_inventory(), _assert_denied(), _queue(), test_cost_writes_need_permission(), test_documents_need_company_edit(), test_member_writes_need_permission(), test_network_sync_and_disconnect_need_permission(), test_role_writes_need_permission()

### Community 152 - "conftest.py"
Cohesion: 0.06
Nodes (12): refresh_levels(), _error_code(), test_every_write_route_refuses_another_site(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _marketing_client(), _month_of_revenue() (+4 more)

### Community 155 - "test_networks.py"
Cohesion: 0.38
Nodes (8): _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission(), test_staff_without_permission_and_other_clients()

### Community 160 - "CompanyService"
Cohesion: 0.18
Nodes (4): remove_image(), show(), CompanyDetailOut, CompanyService

### Community 161 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 162 - "modules/loaders/controller.py"
Cohesion: 0.21
Nodes (4): delete(), index(), show(), update()

### Community 163 - ".show"
Cohesion: 0.12
Nodes (11): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+3 more)

### Community 164 - "Actor"
Cohesion: 0.16
Nodes (4): set_settings(), settings(), CommissionSettingsOut, CommissionService

### Community 165 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 166 - "reports/service.py"
Cohesion: 0.05
Nodes (16): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+8 more)

### Community 167 - "UserOut"
Cohesion: 0.11
Nodes (9): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+1 more)

### Community 168 - ".update_config"
Cohesion: 0.09
Nodes (5): cascade_hours(), hours(), price_rule_service(), PriceRuleHourOut, PriceRuleService

### Community 171 - "internal/rewards/controller.py"
Cohesion: 0.10
Nodes (5): client_reward_service(), csv_response(), lead_filter(), period(), image_upload()

### Community 172 - "test_networks.py"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo

### Community 175 - ".save_payee_details"
Cohesion: 0.21
Nodes (3): payment_details(), save_payment_details(), PayeeDetailsOut

### Community 177 - "commissions/controller.py"
Cohesion: 0.19
Nodes (3): commission_service(), AdjustmentIn, MonthIn

### Community 178 - "UserOut"
Cohesion: 0.10
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 180 - ".build"
Cohesion: 0.09
Nodes (5): _mailer(), RedisEvents, CeleryQueue, test_redis_source_delivers_published_messages(), run()

### Community 183 - "test_key_values.py"
Cohesion: 0.19
Nodes (5): MemoryKeyValueBuffer, _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_the_preflight_answers_with_cors()

### Community 184 - "tasks/controller.py"
Cohesion: 0.11
Nodes (5): TaskClientOut, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 188 - "forget_site"
Cohesion: 0.14
Nodes (4): _recommended_models(), forget_cascades(), forget_floors(), forget_site()

### Community 191 - "postgres"
Cohesion: 0.33
Nodes (6): POSTGRES_PASSWORD, env, image, options, ports, postgres

### Community 192 - "TaskQueue"
Cohesion: 0.07
Nodes (7): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, TaskMailQueue, TaskQueue

### Community 195 - "errors.py"
Cohesion: 0.07
Nodes (11): Network, Segurança e limites, KeyValueBuffer, RedisKeyValueBuffer, cors(), preflight(), receive(), KeyValueIn (+3 more)

### Community 197 - "ClientLoaderService"
Cohesion: 0.17
Nodes (7): create(), delete(), index(), options(), show(), update(), ClientLoaderService

### Community 202 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), classify(), classify_many(), delete(), show(), unlinked()

### Community 204 - "ClientService"
Cohesion: 0.05
Nodes (29): audit(), cancel_owner(), change_status(), client(), client_options(), client_teams(), clients(), edit_client() (+21 more)

### Community 210 - "Actor"
Cohesion: 0.13
Nodes (8): ad_units(), delete(), delete_lead(), export_leads(), leads(), metrics(), set_icon(), update()

### Community 213 - "SiteOut"
Cohesion: 0.13
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 215 - "LoaderOut"
Cohesion: 0.20
Nodes (4): create(), LoaderIn, LoaderOut, LoaderService

### Community 218 - "modules/loaders/dto.py"
Cohesion: 0.16
Nodes (3): ClientLoaderIn, LoaderClientOut, LoaderTagOut

### Community 226 - "typing"
Cohesion: 0.08
Nodes (12): engine_options(), Settings, GoogleRedirects, settings_for_tests(), test_google_flow_cookie_is_always_secure(), _settings(), test_every_connection_has_a_statement_and_idle_timeout(), test_pool_is_bounded_and_waits_little() (+4 more)

### Community 231 - "_contract_fields"
Cohesion: 0.18
Nodes (3): index(), site_options(), SiteListOut

### Community 239 - "UnitOfWorkFactory"
Cohesion: 0.05
Nodes (10): CountryLookup, Bucket, UnitOfWorkFactory, is_cascade_shape(), safe_site_cascades(), site_cascades(), RewardCache, prices() (+2 more)

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2418 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **117 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `SupportTaskService`, `invoices/controller.py`, `PublicRewardService`, `DashboardService`, `Actor`, `contracts/controller.py`, `GamToolService`, `Actor`, `RewardCache`, `.of`, `roles/controller.py`, `_month`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `PageOut`, `CustomMetricService`, `settings_for_tests`, `client_documents/service.py`, `goals/controller.py`, `get`, `mfa/controller.py`, `fastapi`, `ReportService`, `CompanyService`, `SiteService`, `.show`, `Actor`, `.trusted_uow`, `reports/service.py`, `UserOut`, `mcm/controller.py`, `.update_config`, `internal/rewards/controller.py`, `AuthService`, `networks/service.py`, `company/controller.py`, `commissions/controller.py`, `Services`, `UserOut`, `MemberService`, `clients`, `modules/rewards/controller.py`, `account/controller.py`, `pydantic`, `checklists/controller.py`, `auth/controller.py`, `TaskQueue`, `.__init__`, `ClientLoaderService`, `ClientAdTagService`, `ClientService`, `mcm/service.py`, `image`, `results/dto.py`, `.__init__`, `internal/rewards/controller.py`, `sites/service.py`, `LoaderOut`, `InvoiceService`, `test_redis_buffer_follows_the_worker_contract`, `google/controller.py`, `audit/controller.py`, `reward_public/dto.py`, `.__init__`, `ad_tag_public/dto.py`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `.__init__`?**
  _High betweenness centrality (0.111) - this node is a cross-community bridge._
- **Are the 175 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 175 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PublicRewardService` be split into smaller, more focused modules?**
  _Cohesion score 0.08888888888888889 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `inventory/dto.py` to `SupportTaskService`, `invoices/controller.py`, `documents.py`, `DashboardService`, `Actor`, `contracts/controller.py`, `GamToolService`, `Actor`, `RewardCache`, `roles/controller.py`, `_month`, `.catalog`, `.trusted_uow`, `.uow`, `settings_for_tests`, `AdTagService`, `api_keys/controller.py`, `commissions/controller.py`, `GoalService`, `get`, `security.py`, `PageOut`, `get`, `ReportService`, `AdTagOut`, `SiteService`, `modules/loaders/controller.py`, `.show`, `.trusted_uow`, `reports/service.py`, `UserOut`, `mcm/controller.py`, `.update_config`, `internal/rewards/controller.py`, `PriceRuleService`, `Services`, `MemberService`, `modules/rewards/controller.py`, `checklists/controller.py`, `router.py`, `ClientLoaderService`, `ClientAdTagService`, `Actor`, `ClientService`, `mcm/service.py`, `image`, `results/dto.py`, `Actor`, `.export_saved`, `internal/rewards/controller.py`, `sites/service.py`, `LoaderOut`, `SiteOut`, `InvoiceService`, `audit/controller.py`, `_contract_fields`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `invoices/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11255411255411256 - nodes in this community are weakly interconnected._