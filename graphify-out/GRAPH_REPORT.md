# Graph Report - avant-api  (2026-11-12)

## Corpus Check
- 381 files · ~121,813 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 5365 nodes · 15188 edges · 245 communities (135 shown, 110 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2460 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `5c95c9ba`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- PublicRewardService
- ad_tag_public/dto.py
- roles/controller.py
- DashboardService
- Actor
- conftest.py
- GamToolService
- ad_tag_public/service.py
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
- image_response
- clean_code.py
- get
- mfa/controller.py
- fastapi
- ReportService
- RewardService
- session-start.sh
- avant-api
- test_price_rules.py
- PageOut
- avant_core_shared_clock
- test_account.py
- mcm/controller.py
- Actor
- ClientService
- PriceRuleService
- AuthService
- Services
- test_reports.py
- networks/service.py
- GoalService
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
- ContractClientRefOut
- test_cache_down_does_not_break_the_page_or_the_save
- checklists/controller.py
- auth/controller.py
- ContractOut
- SessionCookies
- export.py
- test_account.py
- contracts/controller.py
- ClientAdTagService
- checklists/controller.py
- avant-api
- test_account.py
- DashboardTemplateOut
- ClientOut
- browser
- ClientPriceRuleService
- image
- install
- internal/results/controller.py
- test_events.py
- test_events.py
- .export_saved
- sites/service.py
- .approve
- RedisCounter
- Groone Avant: contexto do projeto
- documents/controller.py
- invoices/controller.py
- google/controller.py
- audit/controller.py
- test_metrics.py
- reward_public/dto.py
- GoalTemplateIn
- PublicAdTagService
- MemoryBucket
- updates
- SupportTaskService
- Avant: repositório e plano do MVP
- documents.py
- test_dashboards.py
- contracts/dto.py
- RewardCache
- mine
- RedisKeyValueBuffer
- AdUnitOut
- client_documents/controller.py
- CommissionService
- .catalog
- settings_for_tests
- Arquitetura do MVP do Avant
- commissions/controller.py
- goals/controller.py
- Actor
- test_who_sees_and_changes_invoices
- ContractService
- goals/service.py
- ReportQueryIn
- conftest.py
- team
- test_networks.py
- CompanyFiscalOut
- CompanyService
- SiteService
- floor_cache.py
- .show
- _marketing_client
- package.json
- reports/service.py
- UserOut
- UUID
- AdTagHealthOut
- client_info
- _SpyCounter
- .save_payee_details
- modules/ad_tags/dto.py
- UserOut
- get
- RedisEvents
- tasks/controller.py
- .page_saved
- document_response
- PriceRuleSiteOut
- clients
- UUID
- receive
- TaskQueue
- delete_session
- .classify
- RateLimited
- avant-api
- ClientLoaderService
- .of
- ready
- Actor
- Actor
- Actor
- change_status
- SiteOut
- capped
- LoaderService
- GeoLiteCountries
- RedisRewardBuffer
- _BrokenAuthService
- pytest
- .of
- _contract_fields
- ._old_compare
- UnitOfWorkFactory
- clients/controller.py
- PriceRuleHistoryOut

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

## Communities (245 total, 110 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.09
Nodes (11): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body() (+3 more)

### Community 1 - "ad_tag_public/dto.py"
Cohesion: 0.13
Nodes (6): PageViewBlockIn, PublicAdTagOut, PublicBlockOut, PublicLoaderOut, PublicMgidOut, PublicTagOut

### Community 2 - "roles/controller.py"
Cohesion: 0.08
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.06
Nodes (24): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+16 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (17): create(), delete(), events(), index(), mute(), preview(), show(), update() (+9 more)

### Community 5 - "conftest.py"
Cohesion: 0.08
Nodes (24): _membership_ids(), test_groups_lifecycle(), _assert_denied(), _queue(), test_cost_writes_need_permission(), test_documents_need_company_edit(), test_member_writes_need_permission(), test_network_sync_and_disconnect_need_permission() (+16 more)

### Community 6 - "GamToolService"
Cohesion: 0.06
Nodes (19): ads_txt(), install(), network(), networks(), run(), runs(), start(), gam_tool_service() (+11 more)

### Community 7 - "ad_tag_public/service.py"
Cohesion: 0.12
Nodes (3): ad_tag_cache_key(), RewardBuffer, forget_tags()

### Community 8 - "test"
Cohesion: 0.07
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, jobs (+23 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.05
Nodes (36): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+28 more)

### Community 11 - "conftest.py"
Cohesion: 0.31
Nodes (13): run_password_reset_tasks(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice() (+5 more)

### Community 12 - ".trusted_uow"
Cohesion: 0.08
Nodes (13): add_item(), create(), delete(), delete_service(), issue(), pay(), pdf(), remove_item() (+5 more)

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.11
Nodes (7): networks(), sites(), client_inventory_service(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "AdTagService"
Cohesion: 0.10
Nodes (14): create(), delete(), publish(), restore(), set_active(), show(), units(), update() (+6 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.06
Nodes (11): invite(), StaffInviteIn, StaffService, cancel(), create_invitation(), list_invitations(), resend(), invitation_service() (+3 more)

### Community 18 - "security.py"
Cohesion: 0.05
Nodes (24): CompanyChanged, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company() (+16 more)

### Community 19 - "CustomMetricService"
Cohesion: 0.08
Nodes (11): check(), create(), delete(), index(), update(), CustomMetricCheckIn, CustomMetricCheckOut, CustomMetricIn (+3 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "test_mail_queue.py"
Cohesion: 0.07
Nodes (12): memory_services(), MemoryCounter, RecordingQueue, _account(), _NoDatabase, _NoMail, _services(), test_forgot_password_only_queues_the_normalized_email() (+4 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "image_response"
Cohesion: 0.12
Nodes (3): image(), image_response(), image_upload()

### Community 26 - "clean_code.py"
Cohesion: 0.16
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 27 - "get"
Cohesion: 0.14
Nodes (10): cascade_hours(), history(), hours(), index(), set_floor(), sites(), update_blocks(), update_config() (+2 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "fastapi"
Cohesion: 0.14
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.06
Nodes (20): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned() (+12 more)

### Community 32 - "RewardService"
Cohesion: 0.09
Nodes (6): forget_pages(), create(), update(), RewardIn, RewardOut, RewardService

### Community 36 - "test_price_rules.py"
Cohesion: 0.10
Nodes (32): _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _cascade_rule(), _cascade_site(), _company_of() (+24 more)

### Community 37 - "PageOut"
Cohesion: 0.05
Nodes (4): UnitOfWorkFactory, default_period(), page_out(), PageOut

### Community 39 - "test_account.py"
Cohesion: 0.09
Nodes (9): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), new_verifier(), FakeGoogle, _jwt() (+1 more)

### Community 40 - "mcm/controller.py"
Cohesion: 0.08
Nodes (10): confirm_network(), register_network(), reject_network(), unassigned_networks(), mcm_service(), ClientNetworkIn, McmCandidateOut, McmService (+2 more)

### Community 41 - "Actor"
Cohesion: 0.15
Nodes (6): invite_owner(), new_owner(), owner_invitations(), resend_owner(), OwnerInvitationOut, owner_invitation_out()

### Community 42 - "ClientService"
Cohesion: 0.16
Nodes (6): client_teams(), manager_change(), client_service(), ClientMemberOut, ManagerChangeOut, ClientService

### Community 43 - "PriceRuleService"
Cohesion: 0.12
Nodes (14): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+6 more)

### Community 44 - "AuthService"
Cohesion: 0.13
Nodes (8): get_invitation(), AcceptInvitationIn, ActiveCompanyIn, CompanyOut, InvitationPreviewOut, LoginIn, LoginOut, AuthService

### Community 45 - "Services"
Cohesion: 0.03
Nodes (25): engine_options(), _google(), _mailer(), Services, NoCountries, KeyValueBuffer, RedisBucket, get_services() (+17 more)

### Community 46 - "test_reports.py"
Cohesion: 0.05
Nodes (62): ExportsBusy, CapturingMailer, Sent, test_change_password_attempts_are_limited(), _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client() (+54 more)

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 49 - "io"
Cohesion: 0.14
Nodes (3): ClientRefOut, image_url(), RevenueStatusOut

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 52 - "MemoryCounter"
Cohesion: 0.08
Nodes (13): RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO (+5 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "test_company_image.py"
Cohesion: 0.08
Nodes (18): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, _jpeg(), _png(), _put_image(), _sharpness() (+10 more)

### Community 55 - "MemberService"
Cohesion: 0.06
Nodes (16): options(), edit(), index(), leave(), options(), remove(), set_permissions(), show() (+8 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.17
Nodes (13): _bearer(), _create(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit() (+5 more)

### Community 57 - "clients"
Cohesion: 0.12
Nodes (8): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService

### Community 58 - "ContractService"
Cohesion: 0.27
Nodes (3): _is_docs_page(), observe(), _route_template()

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.08
Nodes (13): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+5 more)

### Community 60 - "account/controller.py"
Cohesion: 0.12
Nodes (10): do_change_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn, ForgotPasswordIn, ResetPasswordIn, RevokedOut (+2 more)

### Community 61 - "ContractClientRefOut"
Cohesion: 0.13
Nodes (4): CostLineOut, MonthResultOut, ResultTotalsOut, ContractClientRefOut

### Community 62 - "test_cache_down_does_not_break_the_page_or_the_save"
Cohesion: 0.14
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "checklists/controller.py"
Cohesion: 0.16
Nodes (8): add_note(), check(), checklist(), edit_note(), mark(), ChecklistDetailOut, ChecklistMarkIn, ChecklistNoteIn

### Community 64 - "auth/controller.py"
Cohesion: 0.10
Nodes (7): accept(), company_image(), do_logout(), login(), me(), set_active_company(), MeOut

### Community 68 - "export.py"
Cohesion: 0.09
Nodes (12): _csv_cell(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx(), _xlsx_cell(), _result() (+4 more)

### Community 69 - "test_account.py"
Cohesion: 0.10
Nodes (10): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_redis_limiter() (+2 more)

### Community 70 - "contracts/controller.py"
Cohesion: 0.20
Nodes (5): contract(), contracts(), finish_contract(), new_contract(), remove_contract()

### Community 71 - "ClientAdTagService"
Cohesion: 0.12
Nodes (11): create(), delete(), health(), index(), publish(), restore(), show(), units() (+3 more)

### Community 72 - "checklists/controller.py"
Cohesion: 0.09
Nodes (5): ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "test_account.py"
Cohesion: 0.23
Nodes (6): _BrokenReleaseCounter, _google_round(), _login(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 75 - "DashboardTemplateOut"
Cohesion: 0.21
Nodes (3): templates(), DashboardTemplateOut, LabelOut

### Community 76 - "ClientOut"
Cohesion: 0.19
Nodes (5): edit_client(), register_client(), ClientIn, ClientOut, ClientPatchIn

### Community 77 - "browser"
Cohesion: 0.05
Nodes (37): FixedCountries, browser(), client(), engine(), mailer(), MemoryRewardBuffer, test_change_password_and_sessions(), query() (+29 more)

### Community 78 - "ClientPriceRuleService"
Cohesion: 0.10
Nodes (5): set_status(), show(), ClientPriceRuleService, PriceRuleDetailsOut, forget_rule()

### Community 79 - "image"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "install"
Cohesion: 0.12
Nodes (11): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), configure_logging() (+3 more)

### Community 81 - "internal/results/controller.py"
Cohesion: 0.11
Nodes (7): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, ResultService

### Community 82 - "test_events.py"
Cohesion: 0.11
Nodes (6): TooManyAttempts, EventSource, StreamLimiter, events(), EventService, test_stream_limiter_caps_each_person_and_the_process()

### Community 83 - "test_events.py"
Cohesion: 0.15
Nodes (14): channel(), _parse(), sse(), _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot() (+6 more)

### Community 84 - ".export_saved"
Cohesion: 0.14
Nodes (3): forget_tag(), index(), AdTagOut

### Community 86 - "sites/service.py"
Cohesion: 0.19
Nodes (8): site_service(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteIn, SiteOut, SitePatchIn, SitesPatchIn

### Community 87 - ".approve"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 91 - "documents/controller.py"
Cohesion: 0.07
Nodes (9): documents(), download(), upload(), document_service(), DocumentService, document_response(), document_upload(), DocumentOut (+1 more)

### Community 92 - "invoices/controller.py"
Cohesion: 0.11
Nodes (14): FiscalDataIn, create_service(), update_service(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut (+6 more)

### Community 94 - "google/controller.py"
Cohesion: 0.04
Nodes (15): GoogleUnavailable, GoogleAuth, get_auth(), get_cookies(), auth_service(), google_callback(), google_start(), google_status() (+7 more)

### Community 95 - "audit/controller.py"
Cohesion: 0.14
Nodes (3): index(), audit_service(), AuditService

### Community 96 - "test_metrics.py"
Cohesion: 0.14
Nodes (4): metrics(), exposition(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 97 - "reward_public/dto.py"
Cohesion: 0.13
Nodes (12): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicRewardPriceOut (+4 more)

### Community 102 - "PublicAdTagService"
Cohesion: 0.14
Nodes (6): config(), page_views(), preflight(), public_ad_tag_service(), PageViewIn, PublicAdTagService

### Community 123 - "MemoryBucket"
Cohesion: 0.19
Nodes (6): BucketResult, BucketRule, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 127 - "updates"
Cohesion: 0.11
Nodes (17): patterns, patterns, update-types, acoes, dependencias, imagens, dependency-name, patterns (+9 more)

### Community 128 - "SupportTaskService"
Cohesion: 0.15
Nodes (4): tasks(), support_task_service(), TaskOut, SupportTaskService

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 130 - "documents.py"
Cohesion: 0.22
Nodes (4): change(), comment(), create(), task()

### Community 131 - "test_dashboards.py"
Cohesion: 0.15
Nodes (11): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request() (+3 more)

### Community 132 - "contracts/dto.py"
Cohesion: 0.13
Nodes (7): contract_networks(), _contract_fields(), ContractIn, ContractNetworkOut, ContractNetworkRefOut, ContractSummaryOut, _network_ref()

### Community 133 - "RewardCache"
Cohesion: 0.22
Nodes (12): CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn, PriceRuleHourOut (+4 more)

### Community 134 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 137 - "client_documents/controller.py"
Cohesion: 0.08
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 138 - "CommissionService"
Cohesion: 0.05
Nodes (22): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+14 more)

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "commissions/controller.py"
Cohesion: 0.13
Nodes (6): checklists(), months(), summary(), site_checklist_service(), ChecklistMonthOut, SiteChecklistService

### Community 145 - "goals/controller.py"
Cohesion: 0.18
Nodes (5): delete_template(), role_goals(), set_role_goal(), update_template(), RoleGoalIn

### Community 147 - "test_who_sees_and_changes_invoices"
Cohesion: 0.05
Nodes (53): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+45 more)

### Community 148 - "ContractService"
Cohesion: 0.19
Nodes (4): edit_contract(), contract_service(), ContractPatchIn, ContractService

### Community 150 - "ReportQueryIn"
Cohesion: 0.08
Nodes (3): query(), ReportQueryIn, export_slot()

### Community 152 - "conftest.py"
Cohesion: 0.05
Nodes (12): refresh_levels(), MemoryKeyValueBuffer, MemoryRewardCache, NoEvents, _error_code(), test_cookies_are_always_secure_with_the_host_prefix(), test_every_write_route_refuses_another_site(), _scaling_client() (+4 more)

### Community 153 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 155 - "test_networks.py"
Cohesion: 0.34
Nodes (8): _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission(), test_staff_without_permission_and_other_clients()

### Community 158 - "CompanyFiscalOut"
Cohesion: 0.14
Nodes (3): edit_fiscal(), fiscal(), CompanyFiscalOut

### Community 160 - "CompanyService"
Cohesion: 0.15
Nodes (6): edit_image(), remove_image(), show(), CompanyDetailOut, CompanyPatchIn, CompanyService

### Community 161 - "SiteService"
Cohesion: 0.25
Nodes (3): members(), SiteMemberOut, SiteService

### Community 162 - "floor_cache.py"
Cohesion: 0.26
Nodes (3): forget_cascades(), forget_floors(), forget_site()

### Community 163 - ".show"
Cohesion: 0.08
Nodes (14): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+6 more)

### Community 164 - "_marketing_client"
Cohesion: 0.23
Nodes (5): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query()

### Community 165 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 166 - "reports/service.py"
Cohesion: 0.05
Nodes (16): catalog(), CustomCatalogMetricOut, dimension_text(), DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn (+8 more)

### Community 167 - "UserOut"
Cohesion: 0.09
Nodes (11): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+3 more)

### Community 172 - "client_info"
Cohesion: 0.22
Nodes (3): do_reset_password(), forgot_password(), client_info()

### Community 175 - ".save_payee_details"
Cohesion: 0.16
Nodes (3): payment_details(), save_payment_details(), PayeeDetailsOut

### Community 176 - "modules/ad_tags/dto.py"
Cohesion: 0.10
Nodes (9): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagHealthDayOut, AdTagLiveOut, AdTagPublishIn, AdTagUnitDayOut, AdTagUnitOut (+1 more)

### Community 178 - "UserOut"
Cohesion: 0.09
Nodes (7): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService

### Community 179 - "get"
Cohesion: 0.11
Nodes (7): openapi(), swagger(), health(), get(), mine(), service_options(), services()

### Community 184 - "tasks/controller.py"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 188 - "PriceRuleSiteOut"
Cohesion: 0.17
Nodes (3): settings(), PriceRuleSiteOut, _recommended_models()

### Community 190 - "UUID"
Cohesion: 0.12
Nodes (5): audit(), cancel_owner(), client_image(), remove_client_image(), AuditOut

### Community 191 - "receive"
Cohesion: 0.16
Nodes (9): POSTGRES_PASSWORD, env, image, options, ports, postgres, cors(), preflight() (+1 more)

### Community 192 - "TaskQueue"
Cohesion: 0.08
Nodes (3): QueueUnavailable, TaskMailQueue, TaskQueue

### Community 195 - "RateLimited"
Cohesion: 0.13
Nodes (3): RateLimited, KeyValueIn, receive_key_values()

### Community 196 - "avant-api"
Cohesion: 0.33
Nodes (5): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem

### Community 197 - "ClientLoaderService"
Cohesion: 0.09
Nodes (8): create(), delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService

### Community 202 - "Actor"
Cohesion: 0.16
Nodes (7): ad_units(), assign_sites(), delete(), site_options(), sites_of_member(), unlinked(), ItemsOut

### Community 210 - "Actor"
Cohesion: 0.09
Nodes (14): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+6 more)

### Community 213 - "SiteOut"
Cohesion: 0.15
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 215 - "LoaderService"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), options(), show(), update(), ClientLoaderIn, LoaderClientOut (+5 more)

### Community 226 - "pytest"
Cohesion: 0.19
Nodes (9): settings_for_tests(), _settings(), test_every_connection_has_a_statement_and_idle_timeout(), test_pool_is_bounded_and_waits_little(), test_api_does_not_start_without_redis_or_queue_in_any_env(), test_empty_variable_stops_the_api(), test_many_processes_need_the_prometheus_directory(), test_queue_does_not_break_the_request_without_broker() (+1 more)

### Community 231 - "_contract_fields"
Cohesion: 0.15
Nodes (3): create(), index(), SiteListOut

### Community 239 - "UnitOfWorkFactory"
Cohesion: 0.05
Nodes (10): CountryLookup, Bucket, is_cascade_shape(), safe_site_cascades(), site_cascades(), reward_cache_key(), RewardCache, prices() (+2 more)

### Community 240 - "clients/controller.py"
Cohesion: 0.14
Nodes (6): client_options(), ClientOptionOut, ClientProfileIn, ClientProfileOut, ClientStatusIn, OwnerChangeIn

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2420 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **110 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `PageOut` to `SupportTaskService`, `PublicRewardService`, `roles/controller.py`, `DashboardService`, `Actor`, `contracts/dto.py`, `GamToolService`, `ad_tag_public/service.py`, `RewardCache`, `client_documents/controller.py`, `CommissionService`, `_month`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `commissions/controller.py`, `PageOut`, `CustomMetricService`, `ContractService`, `goals/service.py`, `settings_for_tests`, `goals/controller.py`, `mfa/controller.py`, `fastapi`, `ReportService`, `CompanyService`, `RewardService`, `SiteService`, `.show`, `reports/service.py`, `UserOut`, `mcm/controller.py`, `ClientService`, `PriceRuleService`, `AuthService`, `networks/service.py`, `GoalService`, `Services`, `UserOut`, `MemoryCounter`, `MemberService`, `clients`, `account/controller.py`, `TaskQueue`, `.__init__`, `ClientLoaderService`, `ClientAdTagService`, `ClientPriceRuleService`, `image`, `internal/results/controller.py`, `Actor`, `.__init__`, `sites/service.py`, `LoaderService`, `documents/controller.py`, `invoices/controller.py`, `test_redis_buffer_follows_the_worker_contract`, `google/controller.py`, `audit/controller.py`, `.__init__`, `reward_public/dto.py`, `.__init__`, `.__init__`, `PublicAdTagService`, `UnitOfWorkFactory`, `.__init__`?**
  _High betweenness centrality (0.139) - this node is a cross-community bridge._
- **Are the 175 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 175 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PublicRewardService` be split into smaller, more focused modules?**
  _Cohesion score 0.09302325581395349 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `SupportTaskService`, `documents.py`, `DashboardService`, `Actor`, `contracts/dto.py`, `GamToolService`, `RewardCache`, `roles/controller.py`, `_month`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `AdTagService`, `api_keys/controller.py`, `commissions/controller.py`, `goals/controller.py`, `security.py`, `ContractService`, `goals/service.py`, `PageOut`, `settings_for_tests`, `get`, `Actor`, `RewardService`, `SiteService`, `.show`, `reports/service.py`, `UserOut`, `mcm/controller.py`, `Actor`, `ClientService`, `PriceRuleService`, `UUID`, `GoalService`, `Services`, `get`, `MemoryCounter`, `MemberService`, `.page_saved`, `modules/rewards/controller.py`, `clients`, `UUID`, `checklists/controller.py`, `ContractOut`, `ClientLoaderService`, `contracts/controller.py`, `ClientAdTagService`, `Actor`, `ClientPriceRuleService`, `image`, `internal/results/controller.py`, `Actor`, `.export_saved`, `internal/rewards/controller.py`, `sites/service.py`, `LoaderService`, `SiteOut`, `invoices/controller.py`, `audit/controller.py`, `_contract_fields`, `clients/controller.py`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `ad_tag_public/dto.py` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._