# Graph Report - avant-api  (2026-11-12)

## Corpus Check
- 383 files · ~123,194 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 5421 nodes · 15358 edges · 243 communities (132 shown, 111 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2474 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `3b508195`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- PublicRewardService
- router.py
- roles/controller.py
- DashboardService
- Actor
- conftest.py
- GamToolService
- avant_core_ports
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
- test_account.py
- goals/controller.py
- verify
- image_response
- clean_code.py
- get
- mfa/controller.py
- fastapi
- ReportService
- ports.py
- RewardService
- session-start.sh
- avant-api
- test_price_rules.py
- avant_core_shared_clock
- avant_core_shared_clock
- test_account.py
- mcm/controller.py
- ClientService
- modules/loaders/controller.py
- PriceRuleService
- Actor
- security.py
- test_reports.py
- networks/service.py
- test_invitation_mail.py
- clients
- Services
- internal/results/controller.py
- MemoryCounter
- edit
- download
- MemberService
- test_api_keys.py
- clients
- main.py
- modules/rewards/controller.py
- google/controller.py
- ContractClientRefOut
- test_cache_down_does_not_break_the_page_or_the_save
- checklists/controller.py
- auth/controller.py
- ContractService
- Avant: conexão com o GAM
- export.py
- test_account.py
- google/dependencies.py
- AdTagOut
- checklists/controller.py
- avant-api
- CeleryQueue
- DashboardTemplateOut
- modules/loaders/service.py
- browser
- ClientPriceRuleService
- image
- install
- internal/results/controller.py
- test_events.py
- test_events.py
- .export_saved
- internal/rewards/controller.py
- sites/service.py
- .approve
- RedisCounter
- Groone Avant: contexto do projeto
- pydantic
- invoices/service.py
- google/controller.py
- audit/controller.py
- test_metrics.py
- reward_public/dto.py
- ClientDocumentOut
- ad_tag_public/service.py
- MemoryBucket
- updates
- Avant: repositório e plano do MVP
- documents.py
- test_alerts.py
- contracts/dto.py
- RewardCache
- mcm/service.py
- test_key_values.py
- ad_units
- client_documents/controller.py
- CommissionService
- .catalog
- settings_for_tests
- Arquitetura do MVP do Avant
- GoalService
- test_who_sees_and_changes_invoices
- ReportQueryIn
- conftest.py
- SyncRunOut
- CapturingMailer
- CompanyService
- SiteService
- floor_cache.py
- .show
- test_permission_denied.py
- package.json
- reports/service.py
- UserOut
- PriceRuleService
- edit_image
- image
- company/controller.py
- document_response
- profile/controller.py
- get
- RedisEvents
- openapi
- tasks/controller.py
- reports/controller.py
- image
- PriceRuleSiteOut
- .assign
- receive
- Services
- postgres
- create
- RateLimited
- ClientLoaderService
- _contract_fields
- health/controller.py
- Actor
- Actor
- capped
- LoaderService
- countries.py
- RedisRewardBuffer
- _BrokenAuthService
- pytest
- UserOut
- _contract_fields
- ._old_compare
- UnitOfWorkFactory
- shared/dto.py

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 233 edges
2. `PageOut` - 193 edges
3. `_csrf()` - 192 edges
4. `_onboard_owner()` - 186 edges
5. `get()` - 173 edges
6. `UnitOfWorkFactory` - 163 edges
7. `Services` - 162 edges
8. `_staff()` - 87 edges
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

## Communities (243 total, 111 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.10
Nodes (11): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body() (+3 more)

### Community 1 - "router.py"
Cohesion: 0.12
Nodes (6): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (24): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+16 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "conftest.py"
Cohesion: 0.08
Nodes (25): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request() (+17 more)

### Community 6 - "GamToolService"
Cohesion: 0.05
Nodes (20): QueueUnavailable, ads_txt(), install(), network(), networks(), run(), runs(), start() (+12 more)

### Community 8 - "test"
Cohesion: 0.07
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, jobs (+23 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.10
Nodes (20): Acesso, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade (+12 more)

### Community 11 - "conftest.py"
Cohesion: 0.19
Nodes (16): run_password_reset_tasks(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _enable(), _now_code(), _password_login(), test_client_can_disable() (+8 more)

### Community 12 - ".trusted_uow"
Cohesion: 0.09
Nodes (6): add_item(), create(), pay(), InvoiceOut, ServiceItemIn, InvoiceService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.09
Nodes (8): networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, page_out(), PageOut

### Community 15 - "AdTagService"
Cohesion: 0.11
Nodes (16): create(), units(), versions(), ad_tag_service(), AdTagActiveIn, AdTagClientOut, AdTagCreateIn, AdTagHealthDayOut (+8 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.12
Nodes (7): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.09
Nodes (9): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut (+1 more)

### Community 18 - "security.py"
Cohesion: 0.07
Nodes (20): CompanyChanged, GoogleUnavailable, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_tab_company(), get_actor() (+12 more)

### Community 19 - "CustomMetricService"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "test_account.py"
Cohesion: 0.04
Nodes (21): MemoryCounter, MemoryRewardCache, NoEvents, RecordingQueue, _google_round(), _login(), _SpyCounter, test_change_password_and_sessions() (+13 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.13
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.16
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "get"
Cohesion: 0.16
Nodes (9): cascade_hours(), history(), hours(), index(), set_floor(), sites(), update_blocks(), update_config() (+1 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (8): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut, MfaService

### Community 29 - "fastapi"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.05
Nodes (8): create(), duplicate(), update(), ReportCountsOut, SavedReportIn, SavedReportOut, export_slot(), ReportService

### Community 31 - "ports.py"
Cohesion: 0.10
Nodes (5): is_cascade_shape(), safe_site_cascades(), site_cascades(), reward_cache_key(), public_control_percent()

### Community 32 - "RewardService"
Cohesion: 0.09
Nodes (5): forget_pages(), create(), RewardIn, RewardOut, RewardService

### Community 36 - "test_price_rules.py"
Cohesion: 0.09
Nodes (33): FixedCountries, _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _cascade_rule(), _cascade_site() (+25 more)

### Community 38 - "avant_core_shared_clock"
Cohesion: 0.12
Nodes (3): AdTagBlockIO, AdTagDraftIO, AdTagSettingsIO

### Community 39 - "test_account.py"
Cohesion: 0.11
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 40 - "mcm/controller.py"
Cohesion: 0.09
Nodes (9): confirm_network(), register_network(), reject_network(), unassigned_networks(), mcm_service(), ClientNetworkIn, McmCandidateOut, McmService (+1 more)

### Community 41 - "ClientService"
Cohesion: 0.05
Nodes (20): audit(), cancel_owner(), change_status(), client(), client_image(), client_teams(), edit_client(), edit_client_image() (+12 more)

### Community 42 - "modules/loaders/controller.py"
Cohesion: 0.13
Nodes (7): create(), delete(), index(), options(), show(), update(), loader_service()

### Community 43 - "PriceRuleService"
Cohesion: 0.08
Nodes (12): cascade_hours(), history(), index(), set_floor(), set_status(), settings(), show(), sites() (+4 more)

### Community 44 - "Actor"
Cohesion: 0.14
Nodes (7): delete(), health(), index(), publish(), restore(), set_active(), update()

### Community 45 - "security.py"
Cohesion: 0.05
Nodes (6): get_services(), known_companies(), alert_service(), dashboard_service(), public_price_floor_service(), report_service()

### Community 46 - "test_reports.py"
Cohesion: 0.06
Nodes (40): _checked_out(), _checkouts(), PoolWatchingEvents, test_downloads_give_the_connection_back(), test_event_stream_holds_no_connection(), test_report_requests_use_few_connections(), test_busy_export_answers_503_with_retry_after(), _result() (+32 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (11): catalog(), create(), delete(), index(), update(), SavedViewIn, SavedViewOut, ScreenCatalogOut (+3 more)

### Community 48 - "test_invitation_mail.py"
Cohesion: 0.24
Nodes (10): _assert_mail_not_sent(), _client_with_owner_invitation(), _invite(), _owner_invitation_emails(), _pending_emails(), test_invite_answers_503_when_the_mail_fails(), test_owner_invitation_answers_503_when_the_mail_fails(), test_owner_invitation_resend_answers_503_when_the_mail_fails() (+2 more)

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "internal/results/controller.py"
Cohesion: 0.13
Nodes (3): results(), client_result_service(), ClientResultService

### Community 52 - "MemoryCounter"
Cohesion: 0.09
Nodes (12): RewardActiveIn, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO, RewardLeadOut (+4 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 55 - "MemberService"
Cohesion: 0.07
Nodes (16): edit(), index(), leave(), options(), remove(), set_permissions(), show(), member_service() (+8 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.22
Nodes (11): Sent, _bearer(), _create(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke(), test_permissions_on_keys() (+3 more)

### Community 57 - "clients"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "main.py"
Cohesion: 0.13
Nodes (6): CsrfFailed, _is_docs_page(), observe(), _route_template(), check_fetch_site(), create_app()

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.11
Nodes (11): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+3 more)

### Community 60 - "google/controller.py"
Cohesion: 0.05
Nodes (19): SessionCookies, new_verifier(), get_cookies(), delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions() (+11 more)

### Community 61 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (5): CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut, ContractClientRefOut

### Community 62 - "test_cache_down_does_not_break_the_page_or_the_save"
Cohesion: 0.14
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "checklists/controller.py"
Cohesion: 0.10
Nodes (12): add_note(), check(), checklist(), checklists(), delete_note(), edit_note(), mark(), months() (+4 more)

### Community 64 - "auth/controller.py"
Cohesion: 0.05
Nodes (18): accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company(), auth_service() (+10 more)

### Community 65 - "ContractService"
Cohesion: 0.11
Nodes (10): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+2 more)

### Community 67 - "Avant: conexão com o GAM"
Cohesion: 0.11
Nodes (16): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment, Avant: conexão com o GAM, Caminho conta de serviço (+8 more)

### Community 68 - "export.py"
Cohesion: 0.09
Nodes (8): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell()

### Community 69 - "test_account.py"
Cohesion: 0.07
Nodes (12): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _BrokenReleaseCounter, _limiter_round(), _refused_attempt_round() (+4 more)

### Community 70 - "google/dependencies.py"
Cohesion: 0.14
Nodes (4): google_redirects(), google_service(), GoogleRedirects, test_google_flow_cookie_is_always_secure()

### Community 71 - "AdTagOut"
Cohesion: 0.08
Nodes (14): AdTagOut, create(), delete(), health(), index(), publish(), restore(), set_active() (+6 more)

### Community 72 - "checklists/controller.py"
Cohesion: 0.08
Nodes (7): ChecklistMarkIn, ChecklistMonthOut, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "CeleryQueue"
Cohesion: 0.15
Nodes (5): CeleryQueue, masked_args(), _CapturingCelery, test_password_reset_task_masks_the_email_in_the_message(), test_tasks_with_ids_only_are_not_masked()

### Community 75 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 76 - "modules/loaders/service.py"
Cohesion: 0.22
Nodes (5): ClientLoaderIn, LoaderClientOut, LoaderIn, LoaderOptionOut, LoaderTagOut

### Community 77 - "browser"
Cohesion: 0.06
Nodes (35): browser(), client(), engine(), mailer(), MemoryRewardBuffer, query(), _rendered(), test_api_key_never_reaches_the_log() (+27 more)

### Community 78 - "ClientPriceRuleService"
Cohesion: 0.10
Nodes (4): set_status(), show(), ClientPriceRuleService, PriceRuleDetailsOut

### Community 79 - "image"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "install"
Cohesion: 0.07
Nodes (15): error_body(), ExportsBusy, install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error() (+7 more)

### Community 81 - "internal/results/controller.py"
Cohesion: 0.14
Nodes (3): show(), result_service(), ResultService

### Community 82 - "test_events.py"
Cohesion: 0.08
Nodes (9): channel(), EventSource, _parse(), sse(), StreamLimiter, events(), event_service(), EventService (+1 more)

### Community 83 - "test_events.py"
Cohesion: 0.29
Nodes (10): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_events_route_refuses_above_the_cap(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports() (+2 more)

### Community 86 - "sites/service.py"
Cohesion: 0.18
Nodes (11): classify(), classify_many(), link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn (+3 more)

### Community 87 - ".approve"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 91 - "pydantic"
Cohesion: 0.13
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 92 - "invoices/service.py"
Cohesion: 0.06
Nodes (12): dollars(), create_service(), services(), update_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut (+4 more)

### Community 94 - "google/controller.py"
Cohesion: 0.06
Nodes (7): GoogleAuth, google_callback(), google_start(), google_status(), google_unlink(), GoogleStatusOut, GoogleService

### Community 95 - "audit/controller.py"
Cohesion: 0.17
Nodes (3): index(), audit_service(), AuditService

### Community 96 - "test_metrics.py"
Cohesion: 0.19
Nodes (3): exposition(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 97 - "reward_public/dto.py"
Cohesion: 0.18
Nodes (11): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicRewardPriceOut (+3 more)

### Community 102 - "ad_tag_public/service.py"
Cohesion: 0.05
Nodes (16): ad_tag_cache_key(), BucketRule, RewardBuffer, config(), page_views(), preflight(), public_ad_tag_service(), PageViewBlockIn (+8 more)

### Community 123 - "MemoryBucket"
Cohesion: 0.21
Nodes (5): BucketResult, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 127 - "updates"
Cohesion: 0.11
Nodes (17): patterns, patterns, update-types, acoes, dependencias, imagens, dependency-name, patterns (+9 more)

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 130 - "documents.py"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 131 - "test_alerts.py"
Cohesion: 0.11
Nodes (11): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company() (+3 more)

### Community 132 - "contracts/dto.py"
Cohesion: 0.17
Nodes (6): ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractPatchIn, ContractSummaryOut, _network_ref()

### Community 133 - "RewardCache"
Cohesion: 0.17
Nodes (13): price_rule_service(), CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn (+5 more)

### Community 135 - "test_key_values.py"
Cohesion: 0.09
Nodes (8): KeyValueBuffer, RedisKeyValueBuffer, MemoryKeyValueBuffer, _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 137 - "client_documents/controller.py"
Cohesion: 0.16
Nodes (7): approve(), documents(), download(), reject(), ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 138 - "CommissionService"
Cohesion: 0.07
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 139 - ".catalog"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 142 - "settings_for_tests"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 145 - "GoalService"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+10 more)

### Community 147 - "test_who_sees_and_changes_invoices"
Cohesion: 0.05
Nodes (49): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+41 more)

### Community 152 - "conftest.py"
Cohesion: 0.05
Nodes (21): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), refresh_levels(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _jpeg() (+13 more)

### Community 155 - "CapturingMailer"
Cohesion: 0.11
Nodes (30): CapturingMailer, _error_code(), _onboard_owner(), test_csrf_is_required_for_writes(), test_every_write_route_refuses_another_site(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit() (+22 more)

### Community 161 - "SiteService"
Cohesion: 0.21
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 162 - "floor_cache.py"
Cohesion: 0.21
Nodes (4): forget_cascades(), forget_floors(), forget_rule(), forget_site()

### Community 163 - ".show"
Cohesion: 0.11
Nodes (11): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs(), network_service() (+3 more)

### Community 164 - "test_permission_denied.py"
Cohesion: 0.13
Nodes (12): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query(), _assert_denied(), _queue(), test_cost_writes_need_permission() (+4 more)

### Community 165 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 166 - "reports/service.py"
Cohesion: 0.05
Nodes (18): QueryTooHeavy, catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn (+10 more)

### Community 167 - "UserOut"
Cohesion: 0.12
Nodes (7): disable(), enable(), reset_mfa(), users(), PersonOut, PeopleService, person_out()

### Community 168 - "PriceRuleService"
Cohesion: 0.10
Nodes (3): hours(), PriceRuleHourOut, PriceRuleService

### Community 172 - "edit_image"
Cohesion: 0.22
Nodes (3): edit_image(), fiscal(), remove_image()

### Community 175 - "company/controller.py"
Cohesion: 0.21
Nodes (5): edit_fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 178 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 179 - "get"
Cohesion: 0.08
Nodes (18): health(), available_months(), delete(), delete_service(), get(), issue(), mine(), payment_details() (+10 more)

### Community 180 - "RedisEvents"
Cohesion: 0.27
Nodes (3): RedisEvents, test_redis_source_delivers_published_messages(), run()

### Community 184 - "tasks/controller.py"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 185 - "reports/controller.py"
Cohesion: 0.08
Nodes (13): create_from_template(), delete(), export(), export_saved(), index(), pin(), pinned(), query() (+5 more)

### Community 188 - "PriceRuleSiteOut"
Cohesion: 0.19
Nodes (3): settings(), PriceRuleSiteOut, _recommended_models()

### Community 190 - ".assign"
Cohesion: 0.40
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 191 - "receive"
Cohesion: 0.27
Nodes (3): cors(), preflight(), receive()

### Community 192 - "Services"
Cohesion: 0.04
Nodes (22): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, Services, PillowImageProcessor, TaskMailQueue (+14 more)

### Community 193 - "postgres"
Cohesion: 0.33
Nodes (6): POSTGRES_PASSWORD, env, image, options, ports, postgres

### Community 195 - "RateLimited"
Cohesion: 0.07
Nodes (4): RateLimited, KeyValueIn, receive_key_values(), prices()

### Community 197 - "ClientLoaderService"
Cohesion: 0.13
Nodes (7): delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService

### Community 201 - "health/controller.py"
Cohesion: 0.14
Nodes (4): metrics(), ready(), health_service(), HealthService

### Community 202 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), delete(), index(), show(), sites_of_member(), unlinked()

### Community 210 - "Actor"
Cohesion: 0.07
Nodes (17): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+9 more)

### Community 226 - "pytest"
Cohesion: 0.07
Nodes (19): engine_settings(), _google(), _mailer(), restricted_engine(), RedisBucket, Settings, settings_for_tests(), test_api_does_not_start_with_a_role_that_ignores_rls() (+11 more)

### Community 228 - "UserOut"
Cohesion: 0.14
Nodes (3): edit_image(), remove_image(), UserOut

### Community 231 - "_contract_fields"
Cohesion: 0.17
Nodes (3): create(), site_options(), SiteListOut

### Community 239 - "UnitOfWorkFactory"
Cohesion: 0.06
Nodes (6): CountryLookup, Bucket, UnitOfWorkFactory, RewardCache, PublicPriceFloorsOut, PublicPriceFloorService

### Community 240 - "shared/dto.py"
Cohesion: 0.07
Nodes (14): client_options(), client_service(), ClientIn, ClientMemberOut, ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+6 more)

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2439 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **111 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `.__init__`, `router.py`, `PublicRewardService`, `DashboardService`, `Actor`, `contracts/dto.py`, `GamToolService`, `mcm/service.py`, `RewardCache`, `client_documents/controller.py`, `CommissionService`, `avant_core_ports`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `settings_for_tests`, `CustomMetricService`, `.__init__`, `PageOut`, `goals/controller.py`, `mfa/controller.py`, `fastapi`, `ReportService`, `ports.py`, `RewardService`, `SiteService`, `.show`, `avant_core_shared_clock`, `reports/service.py`, `UserOut`, `mcm/controller.py`, `ClientService`, `PriceRuleService`, `_month`, `company/controller.py`, `networks/service.py`, `Services`, `internal/results/controller.py`, `profile/controller.py`, `MemberService`, `roles/controller.py`, `clients`, `google/controller.py`, `.catalog`, `checklists/controller.py`, `auth/controller.py`, `ContractService`, `.__init__`, `internal/ad_tags/service.py`, `test_account.py`, `ClientLoaderService`, `AdTagOut`, `checklists/controller.py`, `modules/loaders/service.py`, `ClientPriceRuleService`, `image`, `internal/results/controller.py`, `Actor`, `.__init__`, `sites/service.py`, `LoaderService`, `pydantic`, `.__init__`, `test_redis_buffer_follows_the_worker_contract`, `google/controller.py`, `audit/controller.py`, `invoices/service.py`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `ad_tag_public/service.py`, `shared/dto.py`?**
  _High betweenness centrality (0.118) - this node is a cross-community bridge._
- **Are the 183 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 183 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PublicRewardService` be split into smaller, more focused modules?**
  _Cohesion score 0.10256410256410256 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `inventory/dto.py` to `router.py`, `documents.py`, `DashboardService`, `Actor`, `contracts/dto.py`, `GamToolService`, `mcm/service.py`, `RewardCache`, `avant_core_ports`, `roles/controller.py`, `.catalog`, `.trusted_uow`, `.uow`, `settings_for_tests`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `Actor`, `.update`, `PageOut`, `get`, `RewardService`, `SiteService`, `.show`, `avant_core_shared_clock`, `reports/service.py`, `UserOut`, `mcm/controller.py`, `ClientService`, `modules/loaders/controller.py`, `PriceRuleService`, `Actor`, `PriceRuleService`, `_month`, `clients`, `Services`, `get`, `internal/results/controller.py`, `MemberService`, `reports/controller.py`, `modules/rewards/controller.py`, `checklists/controller.py`, `ContractService`, `internal/ad_tags/service.py`, `ClientLoaderService`, `AdTagOut`, `checklists/controller.py`, `Actor`, `modules/loaders/service.py`, `ClientPriceRuleService`, `image`, `Actor`, `.export_saved`, `internal/rewards/controller.py`, `sites/service.py`, `LoaderService`, `Actor`, `invoices/service.py`, `audit/controller.py`, `shared/dto.py`?**
  _High betweenness centrality (0.100) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `router.py` be split into smaller, more focused modules?**
  _Cohesion score 0.11576354679802955 - nodes in this community are weakly interconnected._