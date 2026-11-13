# Graph Report - avant-api  (2026-11-13)

## Corpus Check
- 384 files · ~125,191 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 12 file(s) not represented in the graph (top: (none) 7, .ttf 2, .toml 1)

## Summary
- 5462 nodes · 15485 edges · 246 communities (136 shown, 110 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2480 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `f159815a`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- InvoiceService
- roles/controller.py
- sites/controller.py
- clients/controller.py
- _member_client
- commissions/controller.py
- conftest.py
- steps
- _month
- Avant: models do MVP
- _member_client
- team
- GroupService
- networks/controller.py
- Groone Avant: contexto do projeto
- api_keys/service.py
- InvitationOut
- Arquitetura do MVP do Avant
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- conftest.py
- goals/controller.py
- invoice_pdf.py
- Actor
- clean_code.py
- mfa/controller.py
- Avant: repositório e plano do MVP
- Actor
- metrics
- .uow
- session-start.sh
- avant-api
- clients/service.py
- test_api_keys.py
- PriceRuleSiteOut
- export.py
- test_account.py
- company/controller.py
- ContractClientRefOut
- install
- _onboard_owner
- InvoiceService
- test_alerts.py
- networks/service.py
- io
- .of_view
- Services
- BaseModel
- UnitOfWorkFactory
- .assign
- currencies/controller.py
- members/controller.py
- test_api_keys.py
- router.py
- RedisBucket
- GoalTemplateIn
- account/controller.py
- CommissionService
- mine
- goals/service.py
- ItemsOut
- mcm/controller.py
- test_permission_denied.py
- test_mfa.py
- ReportService
- limits.py
- auth/controller.py
- test_costs_results.py
- google/controller.py
- avant-api
- TaskQueue
- UnitOfWorkFactory
- people/controller.py
- test_hardening.py
- commissions/dto.py
- ContractOut
- install
- shared/dto.py
- events.py
- test_events.py
- api_keys/controller.py
- .of
- AdUnitOut
- Avant: grupos na Empresa e imagem da Empresa
- google_status
- ._mail_in_deployed_envs
- UserOut
- ContractService
- ClientOut
- .page_saved
- _staff
- PublicRewardService
- dollars
- reports/__init__.py
- SiteService
- reward_public/service.py
- templates
- .export_saved
- clients/dependencies.py
- ClientService
- GoogleAuth
- test_api.py
- test_key_values.py
- Actor
- GoalService
- commissions/controller.py
- CommissionRuleOut
- avant-api
- PageOut
- company/controller.py
- .page
- .list_all
- _csrf
- .exchange
- test_invitation_mail.py
- .create
- .of
- ProfileService
- CapturingMailer
- test_ad_tags.py
- sites/controller.py
- networks/controller.py
- SiteService
- internal/ad_tags/service.py
- ReportService
- people/controller.py
- observe
- internal/loaders/service.py
- Avant: conexão com o GAM
- modules/rewards/service.py
- PageOut
- .upload
- postgres
- UserOut
- PayeeDetailsOut
- RedisEvents
- LoaderService
- BaseModel
- checklists
- CompanyService
- _xlsx_cell
- ._required_services
- TaskQueue
- image
- capped
- create
- events
- key_values/controller.py
- test_metrics.py
- RewardBuffer
- modules/loaders/dto.py
- internal/rewards/controller.py
- modules/price_rules/dependencies.py
- PriceRuleService
- GamToolRunOut
- Counter
- health/controller.py
- _BrokenAuthService
- settings_for_tests
- TaskPatchIn
- .assign
- price_floor_public/service.py
- NetworkDetailOut
- ports.py

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
- `Onde está o trabalho` --references--> `PriceRuleSiteOut`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/price_rules/dto.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (246 total, 110 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.16
Nodes (8): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body()

### Community 1 - "InvoiceService"
Cohesion: 0.07
Nodes (23): add_item(), create(), create_service(), delete(), delete_service(), issue(), mine(), pay() (+15 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "sites/controller.py"
Cohesion: 0.05
Nodes (25): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+17 more)

### Community 4 - "clients/controller.py"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "_member_client"
Cohesion: 0.06
Nodes (23): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company(), _membership_ids(), test_groups_lifecycle(), _png(), test_appearance_belongs_to_the_person(), test_profile_picture() (+15 more)

### Community 6 - "commissions/controller.py"
Cohesion: 0.21
Nodes (7): GamStepOut, GamToolClientOut, GamToolNetworkDetailOut, GamToolNetworkOut, GamToolPersonOut, GamToolRunNetworkOut, GamToolSiteOut

### Community 7 - "conftest.py"
Cohesion: 0.08
Nodes (16): challenge(), ExpectedAsset, load_assets(), SwaggerAsset, SwaggerAssetChanged, _BrokenReleaseCounter, _google_round(), _jwt() (+8 more)

### Community 8 - "steps"
Cohesion: 0.07
Nodes (33): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, jobs (+25 more)

### Community 9 - "_month"
Cohesion: 0.07
Nodes (13): create(), delete(), index(), pause(), show(), update(), schedule_service(), ScheduleDeliveryOut (+5 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.10
Nodes (20): Acesso, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade (+12 more)

### Community 11 - "_member_client"
Cohesion: 0.28
Nodes (13): run_password_reset_tasks(), _enable(), _now_code(), _password_login(), test_client_can_disable(), test_login_counter_waits_for_the_code(), test_login_with_mfa(), test_new_recovery_codes_send_a_notice() (+5 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (14): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+6 more)

### Community 14 - "networks/controller.py"
Cohesion: 0.15
Nodes (6): networks(), sites(), ClientNetworkOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.10
Nodes (12): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagDraftIO, AdTagHealthDayOut, AdTagIn, AdTagLiveOut (+4 more)

### Community 16 - "api_keys/service.py"
Cohesion: 0.09
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.11
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.05
Nodes (26): CompanyChanged, CsrfFailed, NoActiveCompany, QueryTooHeavy, RateLimited, api_key_actor(), bearer_token(), check_csrf() (+18 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "conftest.py"
Cohesion: 0.03
Nodes (21): client(), engine(), mailer(), memory_services(), MemoryCounter, MemoryKeyValueBuffer, MemoryRewardBuffer, MemoryRewardCache (+13 more)

### Community 23 - "goals/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.12
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "Actor"
Cohesion: 0.09
Nodes (12): catalog(), create(), create_from_template(), delete(), duplicate(), export(), export_saved(), pin() (+4 more)

### Community 26 - "clean_code.py"
Cohesion: 0.16
Nodes (6): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names(), source_files()

### Community 28 - "mfa/controller.py"
Cohesion: 0.08
Nodes (8): confirm(), disable(), new_recovery_codes(), setup(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut, MfaService

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.15
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "Actor"
Cohesion: 0.05
Nodes (3): pinned(), SavedReportOut, _statement_timeout()

### Community 31 - "metrics"
Cohesion: 0.08
Nodes (23): FixedCountries, NoCountries, browser(), _buffer(), _cascade_reward(), test_events_and_leads_go_to_the_buffer(), test_icon_route_has_the_ip_limit(), test_price_rule_settings_forget_reward_page() (+15 more)

### Community 36 - "clients/service.py"
Cohesion: 0.14
Nodes (27): _cascade_rule(), _cascade_site(), _company_of(), _config(), _hours(), _offerwall_unit(), _present(), _rule() (+19 more)

### Community 37 - "test_api_keys.py"
Cohesion: 0.07
Nodes (12): config(), page_views(), preflight(), public_ad_tag_service(), PageViewBlockIn, PageViewIn, PublicAdTagOut, PublicBlockOut (+4 more)

### Community 39 - "export.py"
Cohesion: 0.16
Nodes (4): NetworkIn, ServiceAccountOut, SyncRunOut, enqueue_sync()

### Community 40 - "test_account.py"
Cohesion: 0.14
Nodes (6): confirm_network(), register_network(), reject_network(), ClientNetworkIn, McmService, NetworkOut

### Community 41 - "company/controller.py"
Cohesion: 0.05
Nodes (30): audit(), cancel_owner(), change_status(), client(), client_image(), client_options(), edit_client(), edit_client_image() (+22 more)

### Community 42 - "ContractClientRefOut"
Cohesion: 0.17
Nodes (3): create(), LoaderIn, LoaderOut

### Community 43 - "install"
Cohesion: 0.11
Nodes (10): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), sites() (+2 more)

### Community 44 - "_onboard_owner"
Cohesion: 0.09
Nodes (13): create(), delete(), index(), publish(), restore(), set_active(), show(), units() (+5 more)

### Community 45 - "InvoiceService"
Cohesion: 0.03
Nodes (21): Services, get_services(), audit_service(), company_service(), cost_service(), group_service(), client_ad_tag_service(), checklist_item_service() (+13 more)

### Community 46 - "test_alerts.py"
Cohesion: 0.35
Nodes (5): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive()

### Community 47 - "networks/service.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "io"
Cohesion: 0.31
Nodes (5): _result(), test_compare_header_follows_the_mode(), test_csv_header_escapes_formulas(), test_xlsx_header_is_text_without_control_characters(), test_xlsx_with_the_row_limit_is_fast()

### Community 50 - "Services"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 51 - "BaseModel"
Cohesion: 0.13
Nodes (8): ads_txt(), install(), network(), networks(), run(), runs(), gam_tool_service(), AdsTxtOut

### Community 52 - "UnitOfWorkFactory"
Cohesion: 0.14
Nodes (13): RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO (+5 more)

### Community 53 - ".assign"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): create_app(), documents(), download(), upload(), document_service(), DocumentService

### Community 55 - "members/controller.py"
Cohesion: 0.07
Nodes (15): edit(), index(), leave(), options(), remove(), set_permissions(), show(), DirectPermissionIn (+7 more)

### Community 56 - "test_api_keys.py"
Cohesion: 0.16
Nodes (13): BucketResult, MemoryBucket, _bearer(), _create(), _exercise(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company() (+5 more)

### Community 57 - "router.py"
Cohesion: 0.13
Nodes (9): create(), items(), move(), update(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut, ChecklistItemService (+1 more)

### Community 59 - "GoalTemplateIn"
Cohesion: 0.10
Nodes (14): ad_units(), create(), delete(), delete_lead(), export_leads(), index(), leads(), metrics() (+6 more)

### Community 60 - "account/controller.py"
Cohesion: 0.08
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "CommissionService"
Cohesion: 0.07
Nodes (8): results(), client_result_service(), ClientResultService, show(), result_service(), ResultsOut, default_period(), ResultService

### Community 62 - "mine"
Cohesion: 0.14
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "goals/service.py"
Cohesion: 0.18
Nodes (5): add_note(), check(), delete_note(), edit_note(), mark()

### Community 64 - "ItemsOut"
Cohesion: 0.04
Nodes (22): SessionCookies, get_cookies(), accept(), company_image(), do_logout(), get_invitation(), login(), me() (+14 more)

### Community 65 - "mcm/controller.py"
Cohesion: 0.05
Nodes (21): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+13 more)

### Community 66 - "test_permission_denied.py"
Cohesion: 0.13
Nodes (12): _marketing_client(), _month_of_revenue(), test_costs_crud_and_formula_check(), test_results_for_the_company_and_for_groone(), test_custom_metrics_crud_check_catalog_and_query(), _assert_denied(), _queue(), test_cost_writes_need_permission() (+4 more)

### Community 67 - "test_mfa.py"
Cohesion: 0.10
Nodes (4): create(), index(), ClientRewardService, RewardOut

### Community 68 - "ReportService"
Cohesion: 0.14
Nodes (6): dimension_text(), _header(), _metric_label(), _rows(), to_csv(), to_xlsx()

### Community 69 - "limits.py"
Cohesion: 0.13
Nodes (8): Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_refused_reserve_never_touches_the_other_keys(), test_release_failure_does_not_break_a_good_attempt()

### Community 70 - "auth/controller.py"
Cohesion: 0.17
Nodes (3): comment(), TaskDetailOut, SupportTaskService

### Community 71 - "test_costs_results.py"
Cohesion: 0.09
Nodes (13): AdTagOut, create(), delete(), health(), index(), publish(), restore(), set_active() (+5 more)

### Community 72 - "google/controller.py"
Cohesion: 0.09
Nodes (7): ChecklistMarkIn, ChecklistNoteIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "TaskQueue"
Cohesion: 0.15
Nodes (5): CeleryQueue, masked_args(), _CapturingCelery, test_password_reset_task_masks_the_email_in_the_message(), test_tasks_with_ids_only_are_not_masked()

### Community 77 - "test_hardening.py"
Cohesion: 0.11
Nodes (14): configure_logging(), JsonFormatter, _rendered(), test_api_key_never_reaches_the_log(), test_docs_only_for_the_groone_session_with_2fa(), test_every_response_has_the_content_security_policy(), test_every_response_has_the_security_headers(), test_invalid_bearer_is_limited_per_ip_before_the_database() (+6 more)

### Community 78 - "commissions/dto.py"
Cohesion: 0.11
Nodes (13): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+5 more)

### Community 79 - "ContractOut"
Cohesion: 0.08
Nodes (11): check_formula(), create(), delete(), index(), update(), CostIn, CostOut, FormulaCheckIn (+3 more)

### Community 80 - "install"
Cohesion: 0.21
Nodes (9): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), masked_path() (+1 more)

### Community 81 - "shared/dto.py"
Cohesion: 0.09
Nodes (3): ClientProfileOut, FiscalDataOut, image_url()

### Community 82 - "events.py"
Cohesion: 0.10
Nodes (8): TooManyAttempts, channel(), EventSource, _parse(), sse(), StreamLimiter, EventService, test_stream_limiter_caps_each_person_and_the_process()

### Community 83 - "test_events.py"
Cohesion: 0.27
Nodes (11): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_events_route_refuses_above_the_cap(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports() (+3 more)

### Community 86 - "AdUnitOut"
Cohesion: 0.21
Nodes (3): ad_units(), link(), AdUnitOut

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "google_status"
Cohesion: 0.21
Nodes (3): RedisCounter, test_redis_decr_without_key_creates_nothing(), test_redis_limiter()

### Community 89 - "._mail_in_deployed_envs"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 91 - "UserOut"
Cohesion: 0.19
Nodes (3): document_upload(), DocumentOut, DocumentsOut

### Community 92 - "ContractService"
Cohesion: 0.17
Nodes (3): checklist(), ChecklistDetailOut, SiteChecklistService

### Community 94 - "ClientOut"
Cohesion: 0.03
Nodes (21): _google(), GoogleFailed, GoogleUnavailable, _claims(), GoogleAuth, GoogleOAuth, identity_from_id_token(), new_verifier() (+13 more)

### Community 95 - ".page_saved"
Cohesion: 0.17
Nodes (4): support_task_service(), TaskDataIn, TaskIn, TaskOut

### Community 96 - "_staff"
Cohesion: 0.06
Nodes (31): refresh_levels(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status(), _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission(), _gam_viewer() (+23 more)

### Community 97 - "PublicRewardService"
Cohesion: 0.10
Nodes (3): BucketRule, public_control_percent(), PublicRewardService

### Community 102 - "dollars"
Cohesion: 0.07
Nodes (5): dollars(), available_months(), AvailableMonthOut, InvoiceItemOut, ReturnedOut

### Community 127 - "SiteService"
Cohesion: 0.11
Nodes (17): patterns, patterns, update-types, acoes, dependencias, imagens, dependency-name, patterns (+9 more)

### Community 128 - "reward_public/service.py"
Cohesion: 0.15
Nodes (14): safe_site_cascades(), CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut (+6 more)

### Community 129 - "templates"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 130 - ".export_saved"
Cohesion: 0.11
Nodes (4): ExportsBusy, export_slot(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run()

### Community 131 - "clients/dependencies.py"
Cohesion: 0.26
Nodes (5): client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn, ClientDocumentService

### Community 132 - "ClientService"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 133 - "GoogleAuth"
Cohesion: 0.12
Nodes (18): reward_cache_key(), RewardCache, CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigIn, PriceRuleConfigOut (+10 more)

### Community 134 - "test_api.py"
Cohesion: 0.14
Nodes (15): _error_code(), test_cookies_are_always_secure_with_the_host_prefix(), test_csrf_is_required_for_writes(), test_every_write_route_refuses_another_site(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_tab_company_must_match_the_session() (+7 more)

### Community 135 - "test_key_values.py"
Cohesion: 0.18
Nodes (5): _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 136 - "Actor"
Cohesion: 0.15
Nodes (6): assign_sites(), delete(), index(), show(), sites_of_member(), unlinked()

### Community 137 - "GoalService"
Cohesion: 0.23
Nodes (4): approve(), documents(), download(), reject()

### Community 138 - "commissions/controller.py"
Cohesion: 0.06
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 139 - "CommissionRuleOut"
Cohesion: 0.10
Nodes (7): openapi(), swagger(), swagger_asset(), _swagger_page(), health(), get(), pdf()

### Community 142 - "avant-api"
Cohesion: 0.19
Nodes (10): invalid_variable_names(), load_settings(), _environment(), _refused_names(), test_api_starts_with_each_transport(), test_environment_name_changes_nothing(), test_malformed_smtp_url_never_shows_the_value(), test_missing_or_invalid_configuration_stops_the_api() (+2 more)

### Community 143 - "PageOut"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 144 - "company/controller.py"
Cohesion: 0.14
Nodes (5): edit_fiscal(), fiscal(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 145 - ".page"
Cohesion: 0.05
Nodes (18): create_template(), delete_template(), mine(), _month(), role_goals(), set_role_goal(), team(), template_options() (+10 more)

### Community 146 - ".list_all"
Cohesion: 0.16
Nodes (4): change(), create(), task(), tasks()

### Community 147 - "_csrf"
Cohesion: 0.10
Nodes (22): _csrf(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _admin_role(), NextMonthClock, _support() (+14 more)

### Community 148 - ".exchange"
Cohesion: 0.12
Nodes (7): delete(), index(), options(), show(), update(), client_loader_service(), ClientLoaderService

### Community 149 - "test_invitation_mail.py"
Cohesion: 0.24
Nodes (10): _assert_mail_not_sent(), _client_with_owner_invitation(), _invite(), _owner_invitation_emails(), _pending_emails(), test_invite_answers_503_when_the_mail_fails(), test_owner_invitation_answers_503_when_the_mail_fails(), test_owner_invitation_resend_answers_503_when_the_mail_fails() (+2 more)

### Community 150 - ".create"
Cohesion: 0.12
Nodes (3): _mailer(), GeoLiteCountries, test_each_transport_builds_its_mailer()

### Community 152 - ".of"
Cohesion: 0.08
Nodes (20): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans(), PillowImageProcessor, _after_first_segment(), _jpeg(), _png(), _put_image() (+12 more)

### Community 153 - "ProfileService"
Cohesion: 0.38
Nodes (8): _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission(), test_staff_without_permission_and_other_clients()

### Community 155 - "CapturingMailer"
Cohesion: 0.07
Nodes (48): CapturingMailer, Sent, _onboard_owner(), _owner_invite(), _checked_out(), _checkouts(), PoolWatchingEvents, test_downloads_give_the_connection_back() (+40 more)

### Community 158 - "test_ad_tags.py"
Cohesion: 0.21
Nodes (7): is_cascade_shape(), site_cascades(), _page_views(), _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back()

### Community 161 - "sites/controller.py"
Cohesion: 0.16
Nodes (11): classify(), classify_many(), site_options(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut (+3 more)

### Community 163 - "networks/controller.py"
Cohesion: 0.17
Nodes (9): connect(), disconnect(), options(), service_account(), show(), sync(), sync_runs(), network_service() (+1 more)

### Community 164 - "SiteService"
Cohesion: 0.13
Nodes (4): members(), site_service(), SiteMemberOut, SiteService

### Community 166 - "ReportService"
Cohesion: 0.06
Nodes (27): index(), query(), query_batch(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut (+19 more)

### Community 167 - "people/controller.py"
Cohesion: 0.11
Nodes (9): Resumo, disable(), enable(), reset_mfa(), users(), people_service(), PersonOut, PeopleService (+1 more)

### Community 168 - "observe"
Cohesion: 0.36
Nodes (3): _content_security_policy(), observe(), _route_template()

### Community 172 - "Avant: conexão com o GAM"
Cohesion: 0.12
Nodes (15): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment, Avant: conexão com o GAM, Caminho conta de serviço (+7 more)

### Community 175 - "PageOut"
Cohesion: 0.06
Nodes (11): Modelo de dados, index(), AuditService, client_teams(), clients(), ClientMemberOut, unassigned_networks(), McmCandidateOut (+3 more)

### Community 177 - "postgres"
Cohesion: 0.33
Nodes (6): POSTGRES_PASSWORD, env, image, options, ports, postgres

### Community 178 - "UserOut"
Cohesion: 0.09
Nodes (8): edit_appearance(), edit_image(), image(), remove_image(), AppearanceIn, AppearanceOut, ProfileService, UserOut

### Community 179 - "PayeeDetailsOut"
Cohesion: 0.21
Nodes (3): payment_details(), save_payment_details(), PayeeDetailsOut

### Community 183 - "LoaderService"
Cohesion: 0.12
Nodes (8): delete(), index(), options(), show(), update(), loader_service(), LoaderOptionOut, LoaderService

### Community 184 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 185 - "checklists"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 186 - "CompanyService"
Cohesion: 0.15
Nodes (5): edit_image(), remove_image(), show(), CompanyDetailOut, CompanyService

### Community 190 - "._required_services"
Cohesion: 0.18
Nodes (3): _are_proxy_addresses(), InvalidVariables, _is_smtp_url()

### Community 192 - "TaskQueue"
Cohesion: 0.12
Nodes (8): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, QueueUnavailable, TaskMailQueue, TaskQueue

### Community 198 - "key_values/controller.py"
Cohesion: 0.10
Nodes (7): KeyValueBuffer, RedisKeyValueBuffer, cors(), preflight(), receive(), KeyValueIn, receive_key_values()

### Community 201 - "test_metrics.py"
Cohesion: 0.15
Nodes (4): metrics(), exposition(), test_metrics_add_up_every_process(), test_metrics_of_a_single_process()

### Community 210 - "internal/rewards/controller.py"
Cohesion: 0.08
Nodes (13): ad_units(), delete(), delete_lead(), export_leads(), leads(), metrics(), set_active(), set_icon() (+5 more)

### Community 212 - "PriceRuleService"
Cohesion: 0.07
Nodes (6): show(), update_config(), PriceRuleDetailsOut, forget_rule(), PriceRuleService, stored_drop_tiers()

### Community 215 - "GamToolRunOut"
Cohesion: 0.38
Nodes (3): start(), GamToolRunIn, GamToolRunOut

### Community 223 - "health/controller.py"
Cohesion: 0.17
Nodes (3): ready(), health_service(), HealthService

### Community 226 - "settings_for_tests"
Cohesion: 0.13
Nodes (11): engine_settings(), restricted_engine(), settings_for_tests(), test_api_does_not_start_with_a_role_that_ignores_rls(), test_database_url_cannot_override_the_timeouts(), test_default_numbers_fit_the_connection_budget(), test_engine_settings_come_from_the_settings(), test_engine_settings_refuse_zero_and_above_the_ceiling() (+3 more)

### Community 231 - ".assign"
Cohesion: 0.13
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 239 - "price_floor_public/service.py"
Cohesion: 0.09
Nodes (5): CountryLookup, Bucket, prices(), PublicPriceFloorsOut, PublicPriceFloorService

### Community 265 - "ports.py"
Cohesion: 0.08
Nodes (7): InvitationMailNotSent, invite(), options(), staff(), StaffInviteIn, StaffService, invitation_mail()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2455 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **110 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `reward_public/service.py`, `InvoiceService`, `roles/controller.py`, `sites/controller.py`, `clients/controller.py`, `clients/dependencies.py`, `commissions/controller.py`, `GoogleAuth`, `.__init__`, `ports.py`, `commissions/controller.py`, `_month`, `GroupService`, `networks/controller.py`, `api_keys/service.py`, `company/controller.py`, `.page`, `custom_metrics/controller.py`, `.exchange`, `InvitationOut`, `conftest.py`, `goals/controller.py`, `mfa/controller.py`, `Avant: repositório e plano do MVP`, `test_ad_tags.py`, `Actor`, `sites/controller.py`, `networks/controller.py`, `SiteService`, `test_api_keys.py`, `internal/ad_tags/service.py`, `export.py`, `test_account.py`, `company/controller.py`, `people/controller.py`, `internal/loaders/service.py`, `_onboard_owner`, `ReportService`, `modules/rewards/service.py`, `PageOut`, `networks/service.py`, `Services`, `UserOut`, `currencies/controller.py`, `LoaderService`, `members/controller.py`, `router.py`, `CompanyService`, `GoalTemplateIn`, `account/controller.py`, `CommissionService`, `ItemsOut`, `mcm/controller.py`, `TaskQueue`, `test_mfa.py`, `auth/controller.py`, `test_costs_results.py`, `google/controller.py`, `commissions/dto.py`, `ContractOut`, `PriceRuleService`, `UserOut`, `.__init__`, `.__init__`, `ClientOut`, `ContractService`, `.__init__`, `.page_saved`, `PublicRewardService`, `price_floor_public/service.py`, `.__init__`, `reports/__init__.py`?**
  _High betweenness centrality (0.121) - this node is a cross-community bridge._
- **Are the 186 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 186 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `InvoiceService` be split into smaller, more focused modules?**
  _Cohesion score 0.06593707250341997 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `InvoiceService`, `roles/controller.py`, `sites/controller.py`, `clients/controller.py`, `GoogleAuth`, `commissions/controller.py`, `Actor`, `ports.py`, `_month`, `team`, `GroupService`, `networks/controller.py`, `api_keys/service.py`, `.page`, `Arquitetura do MVP do Avant`, `.list_all`, `.exchange`, `InvitationOut`, `test_reports.py`, `.uow`, `sites/controller.py`, `networks/controller.py`, `SiteService`, `internal/ad_tags/service.py`, `PriceRuleSiteOut`, `export.py`, `test_account.py`, `company/controller.py`, `people/controller.py`, `internal/loaders/service.py`, `_onboard_owner`, `InvoiceService`, `modules/rewards/service.py`, `ContractClientRefOut`, `install`, `Services`, `BaseModel`, `LoaderService`, `members/controller.py`, `checklists`, `GoalTemplateIn`, `CommissionService`, `goals/service.py`, `mcm/controller.py`, `test_mfa.py`, `ReportService`, `auth/controller.py`, `test_costs_results.py`, `google/controller.py`, `commissions/dto.py`, `ContractOut`, `shared/dto.py`, `internal/rewards/controller.py`, `PriceRuleService`, `ContractService`, `.page_saved`, `NetworkDetailOut`, `reports/__init__.py`?**
  _High betweenness centrality (0.075) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `roles/controller.py` be split into smaller, more focused modules?**
  _Cohesion score 0.07481005260081823 - nodes in this community are weakly interconnected._