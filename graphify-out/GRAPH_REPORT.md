# Graph Report - avant-api  (2026-11-12)

## Corpus Check
- 385 files · ~124,246 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 5454 nodes · 15439 edges · 241 communities (126 shown, 115 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2478 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d16a706b`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- PublicRewardService
- router.py
- roles/controller.py
- DashboardService
- Actor
- conftest.py
- gam_tools/dto.py
- clients/controller.py
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
- AdTagOut
- mfa/controller.py
- fastapi
- ReportService
- .icon
- RewardService
- session-start.sh
- avant-api
- test_price_rules.py
- PublicAdTagService
- avant_core_shared_clock
- test_account.py
- mcm/controller.py
- ClientService
- modules/loaders/controller.py
- PriceRuleService
- Actor
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
- limits.py
- modules/rewards/controller.py
- google/controller.py
- avant_core_access_models
- test_cache_down_does_not_break_the_page_or_the_save
- checklists/controller.py
- auth/controller.py
- ContractService
- Avant: conexão com o GAM
- export.py
- test_account.py
- api_docs/controller.py
- AdTagOut
- checklists/controller.py
- avant-api
- CeleryQueue
- DashboardTemplateOut
- create
- browser
- ClientPriceRuleService
- image
- install
- checklists
- test_events.py
- test_events.py
- .export_saved
- .uow
- sites/service.py
- .approve
- RedisCounter
- Groone Avant: contexto do projeto
- pydantic
- invoices/service.py
- google/controller.py
- audit/controller.py
- GamToolService
- reward_public/dto.py
- ClientDocumentOut
- ad_tag_public/service.py
- MemoryBucket
- updates
- SupportTaskService
- Avant: repositório e plano do MVP
- documents.py
- test_alerts.py
- test_dashboards.py
- RewardCache
- mine
- RedisKeyValueBuffer
- SiteService
- client_documents/controller.py
- CommissionService
- .catalog
- settings_for_tests
- Arquitetura do MVP do Avant
- GoalTemplateOut
- SiteChecklistService
- test_who_sees_and_changes_invoices
- SessionCookies
- test_reward_public.py
- goals/controller.py
- CapturingMailer
- .update_fiscal
- .show
- SiteService
- GoalService
- networks/controller.py
- test_permission_denied.py
- package.json
- reports/service.py
- UserOut
- internal/loaders/service.py
- edit_image
- company/controller.py
- document_response
- AdTagUnitDayOut
- profile/controller.py
- get
- RedisEvents
- .of_detail
- tasks/controller.py
- .page_saved
- image
- Actor
- rewards/http.py
- TaskQueue
- postgres
- key_values/controller.py
- delete_template
- ClientLoaderService
- health/controller.py
- sites/controller.py
- modules/loaders/dto.py
- Actor
- Actor
- LoaderOptionOut
- typing
- _BrokenAuthService
- pytest
- _contract_fields
- ._old_compare
- UnitOfWorkFactory
- shared/dto.py

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

## Communities (241 total, 115 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.14
Nodes (9): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body() (+1 more)

### Community 1 - "router.py"
Cohesion: 0.07
Nodes (9): InvitationMailNotSent, invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, InvitationOut (+1 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (25): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+17 more)

### Community 4 - "Actor"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "conftest.py"
Cohesion: 0.08
Nodes (20): _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client() (+12 more)

### Community 6 - "gam_tools/dto.py"
Cohesion: 0.12
Nodes (6): start(), GamStepOut, GamToolPersonOut, GamToolRunIn, GamToolRunNetworkOut, GamToolRunOut

### Community 7 - "clients/controller.py"
Cohesion: 0.08
Nodes (18): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), client_teams(), edit_client() (+10 more)

### Community 8 - "test"
Cohesion: 0.07
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, jobs (+23 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.09
Nodes (21): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Decisões de Pedro (22/10/2026), GAM, Identidade (+13 more)

### Community 11 - "test_mfa.py"
Cohesion: 0.12
Nodes (23): run_password_reset_tasks(), _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites() (+15 more)

### Community 12 - ".trusted_uow"
Cohesion: 0.07
Nodes (7): save_payment_details(), services(), update_item(), update_service(), InvoiceOut, InvoiceServiceOut, InvoiceService

### Community 13 - ".uow"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "inventory/dto.py"
Cohesion: 0.13
Nodes (6): networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "modules/ad_tags/dto.py"
Cohesion: 0.11
Nodes (7): AdTagClientOut, AdTagCreateIn, AdTagHealthDayOut, AdTagHealthOut, AdTagLiveOut, AdTagSettingsIO, AdTagUnitOut

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "PageOut"
Cohesion: 0.11
Nodes (7): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService

### Community 18 - "security.py"
Cohesion: 0.07
Nodes (21): CompanyChanged, CsrfFailed, NoActiveCompany, RateLimited, api_key_actor(), bearer_token(), check_csrf(), check_tab_company() (+13 more)

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
Nodes (24): client(), engine(), mailer(), memory_services(), MemoryCounter, MemoryKeyValueBuffer, MemoryRewardBuffer, MemoryRewardCache (+16 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "verify"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 26 - "clean_code.py"
Cohesion: 0.16
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 28 - "mfa/controller.py"
Cohesion: 0.07
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "fastapi"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "ReportService"
Cohesion: 0.05
Nodes (20): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin(), pinned() (+12 more)

### Community 32 - "RewardService"
Cohesion: 0.07
Nodes (6): create(), show(), forget_pages(), create(), RewardIn, RewardOut

### Community 36 - "test_price_rules.py"
Cohesion: 0.09
Nodes (33): FixedCountries, _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _cascade_rule(), _cascade_site() (+25 more)

### Community 37 - "PublicAdTagService"
Cohesion: 0.14
Nodes (6): config(), page_views(), preflight(), public_ad_tag_service(), PageViewIn, PublicAdTagService

### Community 38 - "avant_core_shared_clock"
Cohesion: 0.13
Nodes (3): AdTagBlockIO, AdTagDraftIO, AdTagVersionOut

### Community 39 - "test_account.py"
Cohesion: 0.10
Nodes (8): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 40 - "mcm/controller.py"
Cohesion: 0.08
Nodes (9): confirm_network(), register_network(), reject_network(), unassigned_networks(), ClientNetworkIn, McmCandidateOut, McmService, page_out() (+1 more)

### Community 41 - "ClientService"
Cohesion: 0.07
Nodes (8): clients(), owner_invitations(), ClientDetailOut, ClientOut, OwnerInvitationOut, ClientService, owner_invitation_out(), RevenueStatusOut

### Community 42 - "modules/loaders/controller.py"
Cohesion: 0.14
Nodes (8): create(), delete(), index(), show(), update(), LoaderIn, LoaderOut, LoaderService

### Community 43 - "PriceRuleService"
Cohesion: 0.07
Nodes (15): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+7 more)

### Community 44 - "Actor"
Cohesion: 0.14
Nodes (10): create(), delete(), health(), publish(), restore(), set_active(), show(), units() (+2 more)

### Community 45 - "Services"
Cohesion: 0.04
Nodes (14): Services, get_services(), company_service(), cost_service(), client_document_service(), client_inventory_service(), mcm_service(), client_result_service() (+6 more)

### Community 46 - "test_reports.py"
Cohesion: 0.07
Nodes (37): _checked_out(), _checkouts(), PoolWatchingEvents, test_downloads_give_the_connection_back(), test_event_stream_holds_no_connection(), test_report_requests_use_few_connections(), test_busy_export_answers_503_with_retry_after(), test_busy_export_is_refused_without_holding_the_thread() (+29 more)

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
Cohesion: 0.17
Nodes (6): ads_txt(), install(), network(), run(), runs(), AdsTxtOut

### Community 52 - "MemoryCounter"
Cohesion: 0.10
Nodes (13): RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO (+5 more)

### Community 53 - "edit"
Cohesion: 0.10
Nodes (18): Company, Empresa e equipe, Invitation, Membership, API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções (+10 more)

### Community 54 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 55 - "MemberService"
Cohesion: 0.07
Nodes (14): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+6 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.13
Nodes (15): Sent, _bearer(), _create(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke(), test_permissions_on_keys() (+7 more)

### Community 57 - "clients"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "limits.py"
Cohesion: 0.12
Nodes (4): RedisBucket, _content_security_policy(), observe(), _route_template()

### Community 59 - "modules/rewards/controller.py"
Cohesion: 0.09
Nodes (14): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+6 more)

### Community 60 - "google/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "avant_core_access_models"
Cohesion: 0.05
Nodes (9): results(), ClientResultService, show(), CostLineOut, MonthResultOut, ResultsOut, ResultTotalsOut, default_period() (+1 more)

### Community 62 - "test_cache_down_does_not_break_the_page_or_the_save"
Cohesion: 0.12
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "checklists/controller.py"
Cohesion: 0.16
Nodes (7): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), ChecklistNoteIn

### Community 64 - "auth/controller.py"
Cohesion: 0.05
Nodes (20): get_session_auth(), accept(), company_image(), do_logout(), get_invitation(), login(), me(), set_active_company() (+12 more)

### Community 65 - "ContractService"
Cohesion: 0.06
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 67 - "Avant: conexão com o GAM"
Cohesion: 0.22
Nodes (8): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo

### Community 68 - "export.py"
Cohesion: 0.06
Nodes (14): dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), export_slot(), to_csv(), to_xlsx() (+6 more)

### Community 69 - "test_account.py"
Cohesion: 0.05
Nodes (13): TooManyAttempts, Counter, Limiter, Rule, _attempt_round(), _BrokenReleaseCounter, _limiter_round(), _refused_attempt_round() (+5 more)

### Community 70 - "api_docs/controller.py"
Cohesion: 0.09
Nodes (6): openapi(), swagger(), swagger_asset(), _swagger_page(), google_redirects(), google_service()

### Community 71 - "AdTagOut"
Cohesion: 0.12
Nodes (13): AdTagActiveIn, create(), delete(), health(), index(), publish(), restore(), set_active() (+5 more)

### Community 72 - "checklists/controller.py"
Cohesion: 0.14
Nodes (6): ChecklistMarkIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "CeleryQueue"
Cohesion: 0.17
Nodes (4): masked_args(), _CapturingCelery, test_password_reset_task_masks_the_email_in_the_message(), test_tasks_with_ids_only_are_not_masked()

### Community 75 - "DashboardTemplateOut"
Cohesion: 0.15
Nodes (5): templates(), DashboardTemplateOut, templates(), LabelOut, ReportTemplateOut

### Community 77 - "browser"
Cohesion: 0.11
Nodes (21): browser(), _rendered(), test_api_key_never_reaches_the_log(), test_docs_only_for_the_groone_session_with_2fa(), test_every_response_has_the_content_security_policy(), test_every_response_has_the_security_headers(), test_invalid_bearer_is_limited_per_ip_before_the_database(), counting() (+13 more)

### Community 78 - "ClientPriceRuleService"
Cohesion: 0.07
Nodes (15): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+7 more)

### Community 79 - "image"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "install"
Cohesion: 0.10
Nodes (13): error_body(), ExportsBusy, install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error() (+5 more)

### Community 81 - "checklists"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 82 - "test_events.py"
Cohesion: 0.08
Nodes (9): channel(), EventSource, _parse(), sse(), StreamLimiter, events(), event_service(), EventService (+1 more)

### Community 83 - "test_events.py"
Cohesion: 0.09
Nodes (17): ExpectedAsset, load_assets(), SwaggerAsset, SwaggerAssetChanged, _collect(), _event(), ListEvents, test_events_route() (+9 more)

### Community 84 - ".export_saved"
Cohesion: 0.12
Nodes (5): forget_tag(), update(), ad_tag_service(), AdTagIn, AdTagService

### Community 86 - "sites/service.py"
Cohesion: 0.15
Nodes (5): link(), AdUnitOut, AdUnitPatchIn, MemberSitesIn, SiteIn

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
Cohesion: 0.09
Nodes (12): dollars(), invoice_service(), AvailableMonthOut, InvoiceItemOut, InvoiceServiceIn, InvoiceServiceOptionOut, InvoiceSummaryOut, PayeeDetailsOut (+4 more)

### Community 94 - "google/controller.py"
Cohesion: 0.05
Nodes (11): GoogleUnavailable, GoogleAuth, new_verifier(), google_callback(), google_start(), google_status(), google_unlink(), GoogleStatusOut (+3 more)

### Community 95 - "audit/controller.py"
Cohesion: 0.15
Nodes (3): index(), audit_service(), AuditService

### Community 96 - "GamToolService"
Cohesion: 0.18
Nodes (5): networks(), gam_tool_service(), GamToolNetworkDetailOut, GamToolNetworkOut, GamToolService

### Community 97 - "reward_public/dto.py"
Cohesion: 0.13
Nodes (14): public_reward_service(), CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut (+6 more)

### Community 102 - "ad_tag_public/service.py"
Cohesion: 0.11
Nodes (6): PageViewBlockIn, PublicAdTagOut, PublicBlockOut, PublicLoaderOut, PublicMgidOut, PublicTagOut

### Community 123 - "MemoryBucket"
Cohesion: 0.15
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

### Community 131 - "test_alerts.py"
Cohesion: 0.25
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 132 - "test_dashboards.py"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 133 - "RewardCache"
Cohesion: 0.09
Nodes (19): CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut, PriceRuleFloorIn, PriceRuleHistoryOut (+11 more)

### Community 134 - "mine"
Cohesion: 0.16
Nodes (3): mine(), GoalProgressOut, PersonGoalOut

### Community 136 - "SiteService"
Cohesion: 0.17
Nodes (4): show(), site_service(), SiteDetailOut, SiteService

### Community 137 - "client_documents/controller.py"
Cohesion: 0.19
Nodes (7): approve(), documents(), download(), reject(), ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 138 - "CommissionService"
Cohesion: 0.06
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 145 - "GoalTemplateOut"
Cohesion: 0.13
Nodes (5): create_template(), template_options(), templates(), GoalTemplateIn, GoalTemplateOut

### Community 146 - "SiteChecklistService"
Cohesion: 0.15
Nodes (3): site_checklist_service(), ChecklistDetailOut, SiteChecklistService

### Community 147 - "test_who_sees_and_changes_invoices"
Cohesion: 0.06
Nodes (41): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+33 more)

### Community 152 - "test_reward_public.py"
Cohesion: 0.05
Nodes (37): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, _after_first_segment(), _jpeg(), _png(), _put_image() (+29 more)

### Community 153 - "goals/controller.py"
Cohesion: 0.19
Nodes (4): set_role_goal(), update_template(), goal_service(), RoleGoalIn

### Community 155 - "CapturingMailer"
Cohesion: 0.11
Nodes (30): CapturingMailer, _google_round(), _login(), test_change_password_and_sessions(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited() (+22 more)

### Community 162 - "GoalService"
Cohesion: 0.19
Nodes (4): _month(), team(), TeamGoalsOut, GoalService

### Community 163 - "networks/controller.py"
Cohesion: 0.05
Nodes (17): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+9 more)

### Community 164 - "test_permission_denied.py"
Cohesion: 0.07
Nodes (16): refresh_levels(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone() (+8 more)

### Community 165 - "package.json"
Cohesion: 0.20
Nodes (9): author, description, keywords, license, main, name, scripts, test (+1 more)

### Community 166 - "reports/service.py"
Cohesion: 0.05
Nodes (15): catalog(), CustomCatalogMetricOut, DimensionOut, FilterIn, MetricCatalogOut, MetricOut, OrderIn, PeriodIn (+7 more)

### Community 167 - "UserOut"
Cohesion: 0.11
Nodes (9): disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService, person_out() (+1 more)

### Community 175 - "company/controller.py"
Cohesion: 0.25
Nodes (6): show(), CompanyDetailOut, CompanyFiscalOut, CompanyPatchIn, FiscalDataIn, CompanyService

### Community 178 - "profile/controller.py"
Cohesion: 0.10
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 179 - "get"
Cohesion: 0.07
Nodes (17): health(), add_item(), available_months(), create(), create_service(), delete(), delete_service(), get() (+9 more)

### Community 184 - "tasks/controller.py"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 192 - "TaskQueue"
Cohesion: 0.09
Nodes (8): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, QueueUnavailable, TaskMailQueue, TaskQueue

### Community 193 - "postgres"
Cohesion: 0.33
Nodes (6): POSTGRES_PASSWORD, env, image, options, ports, postgres

### Community 195 - "key_values/controller.py"
Cohesion: 0.10
Nodes (9): Network, Segurança e limites, KeyValueBuffer, cors(), preflight(), receive(), KeyValueIn, network_code() (+1 more)

### Community 197 - "ClientLoaderService"
Cohesion: 0.18
Nodes (7): delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService

### Community 201 - "health/controller.py"
Cohesion: 0.09
Nodes (7): metrics(), ready(), health_service(), exposition(), HealthService, test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 202 - "sites/controller.py"
Cohesion: 0.12
Nodes (10): ad_units(), assign_sites(), classify(), classify_many(), delete(), index(), site_options(), unlinked() (+2 more)

### Community 210 - "Actor"
Cohesion: 0.08
Nodes (11): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+3 more)

### Community 213 - "Actor"
Cohesion: 0.13
Nodes (6): Atribuição de sites, GAM, Networks, Sites e ad units, sites_of_member(), SiteOut

### Community 217 - "typing"
Cohesion: 0.09
Nodes (4): GeoLiteCountries, NoCountries, RedisRewardBuffer, RewardBuffer

### Community 226 - "pytest"
Cohesion: 0.06
Nodes (24): engine_settings(), _google(), _mailer(), restricted_engine(), check_fetch_site(), _check_proxy_addresses(), Settings, CeleryQueue (+16 more)

### Community 239 - "UnitOfWorkFactory"
Cohesion: 0.05
Nodes (11): CountryLookup, Bucket, UnitOfWorkFactory, is_cascade_shape(), safe_site_cascades(), site_cascades(), reward_cache_key(), RewardCache (+3 more)

### Community 240 - "shared/dto.py"
Cohesion: 0.08
Nodes (10): ClientMemberOut, ClientOptionOut, ClientPatchIn, ClientProfileIn, ClientProfileOut, ClientStatusIn, ManagerChangeOut, AuditOut (+2 more)

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2455 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **115 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `SupportTaskService`, `router.py`, `roles/controller.py`, `DashboardService`, `Actor`, `RewardCache`, `SiteService`, `client_documents/controller.py`, `CommissionService`, `_month`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `settings_for_tests`, `api_keys/controller.py`, `PageOut`, `SiteChecklistService`, `CustomMetricService`, `goals/controller.py`, `mfa/controller.py`, `fastapi`, `ReportService`, `GoalService`, `networks/controller.py`, `PublicAdTagService`, `reports/service.py`, `UserOut`, `mcm/controller.py`, `ClientService`, `modules/loaders/controller.py`, `internal/loaders/service.py`, `PriceRuleService`, `company/controller.py`, `networks/service.py`, `Services`, `profile/controller.py`, `MemberService`, `clients`, `modules/rewards/controller.py`, `google/controller.py`, `avant_core_access_models`, `goals/service.py`, `auth/controller.py`, `TaskQueue`, `.__init__`, `ContractService`, `test_account.py`, `ClientLoaderService`, `AdTagOut`, `checklists/controller.py`, `ClientPriceRuleService`, `image`, `Actor`, `.__init__`, `.export_saved`, `.uow`, `.__init__`, `sites/service.py`, `.__init__`, `pydantic`, `.__init__`, `test_redis_buffer_follows_the_worker_contract`, `google/controller.py`, `audit/controller.py`, `GamToolService`, `.__init__`, `invoices/service.py`, `.__init__`, `.__init__`, `reward_public/dto.py`, `ad_tag_public/service.py`, `shared/dto.py`?**
  _High betweenness centrality (0.127) - this node is a cross-community bridge._
- **Are the 183 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 183 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PublicRewardService` be split into smaller, more focused modules?**
  _Cohesion score 0.14245014245014245 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `mcm/controller.py` to `SupportTaskService`, `router.py`, `documents.py`, `DashboardService`, `Actor`, `RewardCache`, `roles/controller.py`, `clients/controller.py`, `SiteService`, `_month`, `.trusted_uow`, `.uow`, `inventory/dto.py`, `settings_for_tests`, `api_keys/controller.py`, `GoalTemplateOut`, `SiteChecklistService`, `.update`, `PageOut`, `goals/controller.py`, `AdTagOut`, `RewardService`, `GoalService`, `networks/controller.py`, `reports/service.py`, `UserOut`, `ClientService`, `modules/loaders/controller.py`, `internal/loaders/service.py`, `Actor`, `PriceRuleService`, `.runs`, `Services`, `gam_tools/controller.py`, `get`, `MemberService`, `.page_saved`, `modules/rewards/controller.py`, `avant_core_access_models`, `checklists/controller.py`, `goals/service.py`, `ContractService`, `ClientLoaderService`, `AdTagOut`, `checklists/controller.py`, `sites/controller.py`, `ClientPriceRuleService`, `image`, `checklists`, `Actor`, `.export_saved`, `Actor`, `sites/service.py`, `invoices/service.py`, `audit/controller.py`, `GamToolService`, `UnitOfWorkFactory`, `shared/dto.py`?**
  _High betweenness centrality (0.076) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `router.py` be split into smaller, more focused modules?**
  _Cohesion score 0.06857142857142857 - nodes in this community are weakly interconnected._