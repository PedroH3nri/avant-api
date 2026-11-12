# Graph Report - wt-avant-api-seguranca  (2026-11-11)

## Corpus Check
- 375 files · ~120,831 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 13 file(s) not represented in the graph (top: (none) 8, .ttf 2, .toml 1)

## Summary
- 5323 nodes · 15002 edges · 248 communities (134 shown, 114 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 2466 edges (avg confidence: 0.91)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `28b248dd`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- PublicRewardService
- conftest.py
- roles/controller.py
- DashboardService
- AlertService
- _member_client
- GamToolService
- goals/controller.py
- steps
- schedules/controller.py
- Avant: models do MVP
- edit_client
- .trusted_uow
- GroupService
- PageOut
- AdTagService
- api_keys/controller.py
- InvitationOut
- security.py
- custom_metrics/controller.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- test_mail_queue.py
- dashboard_templates/controller.py
- invoice_pdf.py
- clients/controller.py
- clean_code.py
- ClientPriceRuleService
- mfa/controller.py
- currencies/controller.py
- reports/service.py
- _onboard_owner
- .uow
- session-start.sh
- avant-api
- test_price_rules.py
- MemberOut
- modules/ad_tags/dto.py
- time
- mcm/controller.py
- _staff
- download
- PriceRuleService
- AuthService
- Services
- uuid
- views/controller.py
- checklists
- .show
- client_notes/controller.py
- modules/rewards/service.py
- edit
- PillowImageProcessor
- members/controller.py
- test_api_keys.py
- ItemsOut
- test_alerts.py
- RewardService
- account/controller.py
- client_documents/controller.py
- RedisRewardCache
- MemberService
- auth/controller.py
- main.py
- company/controller.py
- SessionCookies
- export.py
- Limiter
- documents/controller.py
- ClientAdTagService
- checklists/dto.py
- avant-api
- modules/rewards/controller.py
- .of
- test_reward_public.py
- forget_rule
- costs/controller.py
- errors.py
- UnitOfWorkFactory
- events.py
- test_dashboards.py
- AdTagOut
- RewardIn
- sites/controller.py
- Avant: grupos na Empresa e imagem da Empresa
- limits.py
- Groone Avant: contexto do projeto
- modules/results/controller.py
- test_events.py
- google/controller.py
- audit/controller.py
- events/controller.py
- reward_public/service.py
- invoices/service.py
- ad_tag_public/service.py
- RateLimited
- updates
- SupportTaskService
- Avant: repositório e plano do MVP
- tasks/controller.py
- MemoryCounter
- contracts/controller.py
- modules/price_rules/controller.py
- test_account.py
- CapturingMailer
- SiteService
- .run_guarded
- commissions/controller.py
- TaskDetailOut
- tasks/dto.py
- Arquitetura do MVP do Avant
- UserOut
- GoalService
- get
- _csrf
- ad_tag_public/dto.py
- index
- ReportService
- datetime
- GoalTemplateIn
- checklists/controller.py
- mine
- CompanyService
- UUID
- images.py
- networks/controller.py
- reports/dependencies.py
- goals/service.py
- .owner_invitations
- router.py
- PriceRuleHistoryOut
- typing
- image
- team
- Avant: conexão com o GAM
- AdTagUnitDayOut
- test_database.py
- profile/controller.py
- image
- image_response
- document_response
- BaseModel
- settings_for_tests
- postgres
- AdTagHealthOut
- RewardStyleIO
- metrics
- key_values/controller.py
- LoaderService
- clients
- show
- Actor
- internal/rewards/controller.py
- Actor
- .assign
- metrics
- Actor
- reward_buffer.py
- .of
- test_key_values.py
- shared/http.py
- capped
- TaskPatchIn
- PublicPriceFloorService
- NoEvents
- ClientService
- source_files
- RewardCache

## God Nodes (most connected - your core abstractions)
1. `CapturingMailer` - 221 edges
2. `PageOut` - 193 edges
3. `_csrf()` - 184 edges
4. `_onboard_owner()` - 178 edges
5. `get()` - 171 edges
6. `Services` - 165 edges
7. `UnitOfWorkFactory` - 163 edges
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
- `Onde está o trabalho` --references--> `PriceRuleSiteOut`  [INFERRED]
  docs/contexto.md → src/avant_api/modules/price_rules/dto.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (248 total, 114 thin omitted)

### Community 0 - "PublicRewardService"
Cohesion: 0.11
Nodes (12): client_address(), cors(), events(), icon(), leads(), page(), preflight(), read_body() (+4 more)

### Community 1 - "conftest.py"
Cohesion: 0.10
Nodes (20): client(), engine(), mailer(), run_password_reset_tasks(), Sent, _networks(), test_contract_crud(), test_contracts_need_staff_and_their_permission() (+12 more)

### Community 2 - "roles/controller.py"
Cohesion: 0.07
Nodes (13): create(), edit(), index(), options(), permissions(), remove(), role_service(), PermissionOut (+5 more)

### Community 3 - "DashboardService"
Cohesion: 0.05
Nodes (27): choose(), create(), create_from_template(), delete(), duplicate(), home(), index(), run() (+19 more)

### Community 4 - "AlertService"
Cohesion: 0.06
Nodes (18): create(), delete(), events(), index(), mute(), preview(), show(), update() (+10 more)

### Community 5 - "_member_client"
Cohesion: 0.08
Nodes (17): _form(), test_staff_manage_templates_and_clients_see_them_by_role(), test_templates_need_the_permission_and_the_groone_company(), _membership_ids(), test_groups_lifecycle(), _inventory(), test_manual_site(), test_options_have_a_ceiling_and_a_search() (+9 more)

### Community 6 - "GamToolService"
Cohesion: 0.06
Nodes (18): ads_txt(), install(), network(), networks(), run(), runs(), start(), AdsTxtOut (+10 more)

### Community 7 - "goals/controller.py"
Cohesion: 0.18
Nodes (5): delete_template(), role_goals(), set_role_goal(), update_template(), RoleGoalIn

### Community 8 - "steps"
Cohesion: 0.07
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, GITLEAKS_SHA256, GITLEAKS_VERSION, PGPASSWORD, jobs (+23 more)

### Community 9 - "schedules/controller.py"
Cohesion: 0.07
Nodes (12): create(), delete(), index(), pause(), show(), update(), ScheduleDeliveryOut, ScheduleIn (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.10
Nodes (20): Acesso, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade (+12 more)

### Community 13 - "GroupService"
Cohesion: 0.07
Nodes (15): add_members(), create(), edit(), index(), options(), remove(), remove_member(), show() (+7 more)

### Community 14 - "PageOut"
Cohesion: 0.09
Nodes (8): networks(), sites(), ClientNetworkOut, ClientRefOut, ClientSiteChecklistOut, ClientSiteOut, ClientInventoryService, PageOut

### Community 15 - "AdTagService"
Cohesion: 0.11
Nodes (12): create(), delete(), health(), publish(), restore(), set_active(), show(), units() (+4 more)

### Community 16 - "api_keys/controller.py"
Cohesion: 0.10
Nodes (8): create(), index(), revoke(), api_key_service(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, ApiKeyService

### Community 17 - "InvitationOut"
Cohesion: 0.11
Nodes (8): cancel(), create_invitation(), list_invitations(), resend(), invitation_service(), InviteIn, InvitationService, InvitationOut

### Community 18 - "security.py"
Cohesion: 0.07
Nodes (22): CompanyChanged, CsrfFailed, NoActiveCompany, api_key_actor(), bearer_token(), check_csrf(), check_fetch_site(), check_tab_company() (+14 more)

### Community 19 - "custom_metrics/controller.py"
Cohesion: 0.07
Nodes (12): check(), create(), delete(), index(), update(), custom_metric_service(), CustomMetricCheckIn, CustomMetricCheckOut (+4 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "test_mail_queue.py"
Cohesion: 0.09
Nodes (9): RecordingQueue, _account(), _NoDatabase, _NoMail, _services(), test_forgot_password_only_queues_the_normalized_email(), test_forgot_route_never_sends_the_link_itself(), test_forgot_route_queues_without_database_or_mail_in_every_env() (+1 more)

### Community 23 - "dashboard_templates/controller.py"
Cohesion: 0.06
Nodes (14): create(), delete(), index(), roles(), set_home(), show(), update(), dashboard_template_service() (+6 more)

### Community 24 - "invoice_pdf.py"
Cohesion: 0.13
Nodes (11): _block(), _dates(), _footer(), _header(), _items(), _line(), _logo(), money() (+3 more)

### Community 25 - "clients/controller.py"
Cohesion: 0.16
Nodes (13): client_service(), ClientDetailOut, ClientIn, ClientOptionOut, ClientOut, ClientPatchIn, ClientProfileIn, ClientProfileOut (+5 more)

### Community 26 - "clean_code.py"
Cohesion: 0.18
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "ClientPriceRuleService"
Cohesion: 0.08
Nodes (15): cascade_hours(), history(), hours(), index(), set_floor(), set_status(), settings(), show() (+7 more)

### Community 28 - "mfa/controller.py"
Cohesion: 0.10
Nodes (9): confirm(), disable(), new_recovery_codes(), setup(), mfa_service(), MfaCodeIn, MfaSetupOut, RecoveryCodesOut (+1 more)

### Community 29 - "currencies/controller.py"
Cohesion: 0.13
Nodes (6): list_currencies(), update_preferences(), currency_service(), CurrencyOut, PreferencesIn, CurrencyService

### Community 30 - "reports/service.py"
Cohesion: 0.05
Nodes (18): catalog(), templates(), CustomCatalogMetricOut, DimensionOut, FilterIn, LabelOut, MetricCatalogOut, MetricOut (+10 more)

### Community 31 - "_onboard_owner"
Cohesion: 0.11
Nodes (20): _error_code(), _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_deployed_cookies_use_the_host_prefix(), test_every_write_route_refuses_another_site(), test_health_and_metrics(), test_owner_onboarding_and_login() (+12 more)

### Community 36 - "test_price_rules.py"
Cohesion: 0.11
Nodes (31): _site(), test_ad_tags_and_loaders_panel(), test_internal_ad_tags_and_loaders(), test_page_views_go_to_the_buffer_and_health_reads_back(), _cascade_rule(), _cascade_site(), _company_of(), _config() (+23 more)

### Community 37 - "MemberOut"
Cohesion: 0.12
Nodes (7): invite(), options(), staff(), staff_service(), StaffInviteIn, StaffService, MemberOut

### Community 38 - "modules/ad_tags/dto.py"
Cohesion: 0.10
Nodes (12): AdTagActiveIn, AdTagBlockIO, AdTagClientOut, AdTagCreateIn, AdTagDraftIO, AdTagHealthDayOut, AdTagIn, AdTagLiveOut (+4 more)

### Community 39 - "time"
Cohesion: 0.14
Nodes (6): GoogleFailed, _claims(), identity_from_id_token(), FakeGoogle, _jwt(), test_id_token_claims()

### Community 40 - "mcm/controller.py"
Cohesion: 0.09
Nodes (9): confirm_network(), register_network(), reject_network(), unassigned_networks(), mcm_service(), ClientNetworkIn, McmCandidateOut, McmService (+1 more)

### Community 41 - "_staff"
Cohesion: 0.09
Nodes (24): _gam_viewer(), _network(), _network_of(), test_a_run_the_queue_did_not_take_frees_the_network(), test_gam_tool_runs_refuse_what_they_should(), test_gam_tools_need_permission(), test_install_zip_for_several_sites(), test_staff_lists_runs_and_downloads() (+16 more)

### Community 42 - "download"
Cohesion: 0.13
Nodes (3): documents(), download(), upload()

### Community 43 - "PriceRuleService"
Cohesion: 0.06
Nodes (13): cascade_hours(), hours(), index(), set_floor(), set_status(), settings(), show(), sites() (+5 more)

### Community 44 - "AuthService"
Cohesion: 0.08
Nodes (4): get_invitation(), auth_service(), InvitationPreviewOut, AuthService

### Community 45 - "Services"
Cohesion: 0.04
Nodes (18): avant-api, Como funciona, Desenvolvimento, Estrutura, Imagem, Services, TaskMailQueue, MemoryRewardCache (+10 more)

### Community 46 - "uuid"
Cohesion: 0.08
Nodes (35): test_change_password_and_sessions(), _checkouts(), test_report_requests_use_few_connections(), query(), test_busy_export_answers_503_with_retry_after(), test_busy_export_is_refused_without_holding_the_thread(), test_export_slots_refuse_a_third_export_while_two_run(), _day() (+27 more)

### Community 47 - "views/controller.py"
Cohesion: 0.07
Nodes (12): catalog(), create(), delete(), index(), update(), saved_view_service(), SavedViewIn, SavedViewOut (+4 more)

### Community 48 - "checklists"
Cohesion: 0.14
Nodes (4): checklists(), months(), summary(), ChecklistMonthOut

### Community 49 - ".show"
Cohesion: 0.09
Nodes (4): show(), CostLineOut, MonthResultOut, ResultTotalsOut

### Community 50 - "client_notes/controller.py"
Cohesion: 0.08
Nodes (9): add(), delete(), edit(), notes(), client_note_service(), ClientNoteIn, ClientNoteOut, NotePersonOut (+1 more)

### Community 52 - "modules/rewards/service.py"
Cohesion: 0.11
Nodes (12): RewardActiveIn, RewardAdUnitGroupOut, RewardAdUnitOut, RewardAnswerOut, RewardClientOut, RewardDayOut, RewardLeadAnswerOut, RewardLeadIO (+4 more)

### Community 53 - "edit"
Cohesion: 0.12
Nodes (14): API first e chaves de API, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa, Empresa e equipe (+6 more)

### Community 54 - "PillowImageProcessor"
Cohesion: 0.14
Nodes (9): PillowImageProcessor, _jpeg(), _sharpness(), _striped_logo(), test_phone_photos_pass_and_huge_pngs_are_refused(), test_phone_rotation_from_exif_is_kept(), test_sequential_jpeg_with_many_scans_has_the_progressive_limit(), test_wide_and_palette_logos_stay_sharp() (+1 more)

### Community 55 - "members/controller.py"
Cohesion: 0.16
Nodes (7): edit(), remove(), set_permissions(), DirectPermissionIn, DirectPermissionOut, MemberPatchIn, MemberPermissionsIn

### Community 56 - "test_api_keys.py"
Cohesion: 0.30
Nodes (9): _bearer(), _create(), _insert_key(), _keys_in_two_companies(), test_change_password_revokes_keys_in_every_company(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit() (+1 more)

### Community 57 - "ItemsOut"
Cohesion: 0.12
Nodes (10): create(), items(), move(), update(), checklist_item_service(), ChecklistItemIn, ChecklistItemMoveIn, ChecklistItemOut (+2 more)

### Community 58 - "test_alerts.py"
Cohesion: 0.15
Nodes (8): _definition(), _form(), test_alerts_of_a_client(), test_groone_alerts_preview_every_client(), test_members_without_alerts_manage_only_see_what_they_receive(), _form(), test_members_without_schedules_manage_only_see_what_they_receive(), test_schedules_of_a_client()

### Community 59 - "RewardService"
Cohesion: 0.11
Nodes (11): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), set_active(), set_icon() (+3 more)

### Community 60 - "account/controller.py"
Cohesion: 0.09
Nodes (13): delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), revoke_others(), account_service(), ChangePasswordIn (+5 more)

### Community 61 - "client_documents/controller.py"
Cohesion: 0.14
Nodes (9): approve(), documents(), download(), reject(), client_document_service(), ClientDocumentOut, ClientDocumentsOut, RejectDocumentIn (+1 more)

### Community 62 - "RedisRewardCache"
Cohesion: 0.16
Nodes (3): RedisRewardCache, _BrokenRedis, test_cache_down_does_not_break_the_page_or_the_save()

### Community 63 - "MemberService"
Cohesion: 0.16
Nodes (3): show(), MemberDetailOut, MemberService

### Community 64 - "auth/controller.py"
Cohesion: 0.11
Nodes (12): accept(), company_image(), do_logout(), login(), me(), set_active_company(), AcceptInvitationIn, ActiveCompanyIn (+4 more)

### Community 65 - "main.py"
Cohesion: 0.06
Nodes (17): configure_logging(), JsonFormatter, _is_docs_page(), observe(), _route_template(), create_app(), _BrokenAuthService, _rendered() (+9 more)

### Community 66 - "company/controller.py"
Cohesion: 0.16
Nodes (5): edit_fiscal(), company_service(), CompanyFiscalOut, CompanyPatchIn, FiscalDataIn

### Community 67 - "SessionCookies"
Cohesion: 0.09
Nodes (3): SessionCookies, verify(), test_closing_deployed_cookies_keeps_them_secure()

### Community 68 - "export.py"
Cohesion: 0.06
Nodes (15): ExportsBusy, dimension_text(), _csv_cell(), _header(), _metric_label(), _rows(), export_slot(), to_csv() (+7 more)

### Community 69 - "Limiter"
Cohesion: 0.10
Nodes (9): Counter, Limiter, Rule, _attempt_round(), _limiter_round(), _refused_attempt_round(), test_memory_limiter(), test_refused_reserve_never_touches_the_other_keys() (+1 more)

### Community 70 - "documents/controller.py"
Cohesion: 0.14
Nodes (5): document_service(), DocumentService, document_upload(), DocumentOut, DocumentsOut

### Community 71 - "ClientAdTagService"
Cohesion: 0.08
Nodes (12): create(), delete(), health(), index(), publish(), restore(), set_active(), show() (+4 more)

### Community 72 - "checklists/dto.py"
Cohesion: 0.09
Nodes (6): ChecklistMarkIn, ChecklistNoteOut, ChecklistOut, ChecklistPersonOut, ChecklistProgressOut, ChecklistRowOut

### Community 74 - "modules/rewards/controller.py"
Cohesion: 0.15
Nodes (4): reward_service(), csv_response(), lead_filter(), period()

### Community 76 - ".of"
Cohesion: 0.12
Nodes (4): index(), leave(), options(), RoleRefOut

### Community 77 - "test_reward_public.py"
Cohesion: 0.07
Nodes (25): FixedCountries, reward_cache_key(), _png(), _put_image(), test_client_changes_the_company_image(), test_groone_changes_the_image_of_a_client(), test_upload_without_session_is_refused_before_reading_the_body(), _three_scans() (+17 more)

### Community 78 - "forget_rule"
Cohesion: 0.17
Nodes (4): update_config(), PriceRuleConfigIn, forget_rule(), stored_drop_tiers()

### Community 79 - "costs/controller.py"
Cohesion: 0.08
Nodes (12): check_formula(), create(), delete(), index(), update(), cost_service(), CostIn, CostOut (+4 more)

### Community 80 - "errors.py"
Cohesion: 0.10
Nodes (11): error_body(), install(), domain_error(), http_error(), redis_unavailable(), unexpected(), validation_error(), QueryTooHeavy (+3 more)

### Community 81 - "UnitOfWorkFactory"
Cohesion: 0.04
Nodes (9): UnitOfWorkFactory, TaskQueue, results(), client_result_service(), ClientResultService, enqueue_sync(), ResultsOut, default_period() (+1 more)

### Community 82 - "events.py"
Cohesion: 0.08
Nodes (9): TooManyAttempts, channel(), EventSource, _parse(), sse(), StreamLimiter, events(), EventService (+1 more)

### Community 83 - "test_dashboards.py"
Cohesion: 0.29
Nodes (8): _form(), _kpi(), _run(), _template(), test_dashboards_of_a_client(), test_groone_dashboards_sum_every_client(), test_members_see_shared_dashboards_but_need_manage_to_edit(), test_whole_dashboard_runs_in_one_request()

### Community 84 - "AdTagOut"
Cohesion: 0.14
Nodes (3): forget_tag(), index(), AdTagOut

### Community 85 - "RewardIn"
Cohesion: 0.14
Nodes (4): create(), update(), create(), RewardIn

### Community 86 - "sites/controller.py"
Cohesion: 0.19
Nodes (9): site_service(), AdUnitPatchIn, MemberSitesIn, SiteDetailOut, SiteIn, SiteListOut, SiteOut, SitePatchIn (+1 more)

### Community 87 - "Avant: grupos na Empresa e imagem da Empresa"
Cohesion: 0.22
Nodes (8): Avant: grupos na Empresa e imagem da Empresa, Decisões do Pedro (26/10), Herança de comissão e meta, Issues, Modelo de dados, Regras, Resumo, Telas

### Community 88 - "limits.py"
Cohesion: 0.12
Nodes (3): RedisCounter, test_redis_decr_without_key_creates_nothing(), test_redis_limiter()

### Community 89 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 92 - "test_events.py"
Cohesion: 0.26
Nodes (10): _collect(), _event(), ListEvents, test_events_route(), test_events_route_is_session_only_and_frees_the_slot(), test_gam_tool_runs_reach_who_sees_the_gam_tools(), test_metrics_updates_reach_who_sees_reports(), test_redis_source_delivers_published_messages() (+2 more)

### Community 94 - "google/controller.py"
Cohesion: 0.04
Nodes (16): _google(), GoogleUnavailable, challenge(), GoogleAuth, GoogleOAuth, new_verifier(), Settings, google_callback() (+8 more)

### Community 95 - "audit/controller.py"
Cohesion: 0.14
Nodes (3): index(), audit_service(), AuditService

### Community 96 - "events/controller.py"
Cohesion: 0.11
Nodes (4): event_service(), ready(), health_service(), HealthService

### Community 97 - "reward_public/service.py"
Cohesion: 0.12
Nodes (12): CachedPage, PublicAdUnitsOut, PublicIconOut, PublicLeadOut, PublicPageOut, PublicQuestionOut, PublicRewardOut, PublicRewardPriceOut (+4 more)

### Community 98 - "invoices/service.py"
Cohesion: 0.10
Nodes (6): dollars(), AvailableMonthOut, InvoiceItemOut, PayeeDetailsOut, ReturnedOut, FiscalDataOut

### Community 102 - "ad_tag_public/service.py"
Cohesion: 0.10
Nodes (7): Bucket, config(), page_views(), preflight(), public_ad_tag_service(), PageViewIn, PublicAdTagService

### Community 123 - "RateLimited"
Cohesion: 0.10
Nodes (7): RateLimited, BucketResult, BucketRule, MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 127 - "updates"
Cohesion: 0.12
Nodes (15): patterns, update-types, dependencias, imagens, dependency-name, patterns, interval, updates (+7 more)

### Community 128 - "SupportTaskService"
Cohesion: 0.15
Nodes (4): tasks(), support_task_service(), TaskOut, SupportTaskService

### Community 129 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 130 - "tasks/controller.py"
Cohesion: 0.22
Nodes (4): change(), comment(), create(), task()

### Community 132 - "contracts/controller.py"
Cohesion: 0.07
Nodes (19): O que já tem, contract(), contract_networks(), contracts(), edit_contract(), finish_contract(), new_contract(), remove_contract() (+11 more)

### Community 133 - "modules/price_rules/controller.py"
Cohesion: 0.15
Nodes (14): CascadeHourOut, CascadeTryOut, PriceRuleBlockOut, PriceRuleBlocksIn, PriceRuleConfigOut, PriceRuleFloorIn, PriceRuleHourOut, PriceRuleOut (+6 more)

### Community 134 - "test_account.py"
Cohesion: 0.23
Nodes (7): _BrokenReleaseCounter, _google_round(), _login(), test_change_password_attempts_are_limited(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 135 - "CapturingMailer"
Cohesion: 0.15
Nodes (18): CapturingMailer, _clients_viewer(), _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_registers_the_network_of_a_client(), test_networks_are_isolated_per_company(), test_networks_need_permission() (+10 more)

### Community 136 - "SiteService"
Cohesion: 0.15
Nodes (5): ad_units(), link(), unlinked(), AdUnitOut, SiteService

### Community 138 - "commissions/controller.py"
Cohesion: 0.06
Nodes (23): adjust(), create_rule(), delete_rule(), mine(), _month(), person(), rules(), set_settings() (+15 more)

### Community 143 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Modelo de dados (+4 more)

### Community 144 - "UserOut"
Cohesion: 0.14
Nodes (3): edit_image(), remove_image(), UserOut

### Community 145 - "GoalService"
Cohesion: 0.16
Nodes (5): template_options(), templates(), goal_service(), GoalTemplateOut, GoalService

### Community 146 - "get"
Cohesion: 0.08
Nodes (28): health(), add_item(), available_months(), create(), create_service(), delete(), delete_service(), get() (+20 more)

### Community 147 - "_csrf"
Cohesion: 0.11
Nodes (21): _csrf(), _admin_role(), NextMonthClock, _support(), test_client_edit_without_the_manager_keeps_it(), test_client_owner_cannot_touch_commissions(), test_commission_input_is_checked(), test_groone_role_with_internal_permissions() (+13 more)

### Community 148 - "ad_tag_public/dto.py"
Cohesion: 0.13
Nodes (6): PageViewBlockIn, PublicAdTagOut, PublicBlockOut, PublicLoaderOut, PublicMgidOut, PublicTagOut

### Community 150 - "ReportService"
Cohesion: 0.05
Nodes (22): create(), create_from_template(), delete(), duplicate(), export(), export_saved(), index(), pin() (+14 more)

### Community 152 - "datetime"
Cohesion: 0.06
Nodes (20): refresh_levels(), _manage_inventory(), _send(), test_client_sends_documents_and_staff_reviews(), test_staff_writes_notes_and_only_author_or_manager_changes(), _scaling_client(), test_client_owner_cannot_list_client_networks_or_sites(), test_staff_sees_client_networks_sites_and_revenue_status() (+12 more)

### Community 155 - "checklists/controller.py"
Cohesion: 0.11
Nodes (10): add_note(), check(), checklist(), delete_note(), edit_note(), mark(), site_checklist_service(), ChecklistDetailOut (+2 more)

### Community 158 - "mine"
Cohesion: 0.18
Nodes (3): mine(), _month(), PersonGoalOut

### Community 160 - "CompanyService"
Cohesion: 0.16
Nodes (5): remove_image(), show(), CompanyDetailOut, CompanyService, image_url()

### Community 161 - "UUID"
Cohesion: 0.16
Nodes (4): assign_sites(), delete(), members(), SiteMemberOut

### Community 162 - "images.py"
Cohesion: 0.22
Nodes (3): _check_jpeg_size(), _end_of_scan_data(), _has_many_scans()

### Community 163 - "networks/controller.py"
Cohesion: 0.09
Nodes (14): connect(), disconnect(), index(), options(), service_account(), show(), sync(), sync_runs() (+6 more)

### Community 167 - "router.py"
Cohesion: 0.10
Nodes (8): require_staff(), disable(), enable(), reset_mfa(), users(), PersonOut, PeopleService, person_out()

### Community 171 - "typing"
Cohesion: 0.06
Nodes (7): _mailer(), GeoLiteCountries, NoCountries, RedisEvents, RedisBucket, CeleryQueue, run()

### Community 172 - "image"
Cohesion: 0.15
Nodes (3): edit_image(), fiscal(), image()

### Community 174 - "team"
Cohesion: 0.19
Nodes (3): team(), GoalProgressOut, TeamGoalsOut

### Community 175 - "Avant: conexão com o GAM"
Cohesion: 0.11
Nodes (16): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment, Avant: conexão com o GAM, Caminho conta de serviço (+8 more)

### Community 177 - "test_database.py"
Cohesion: 0.31
Nodes (4): engine_options(), _settings(), test_every_connection_has_a_statement_and_idle_timeout(), test_pool_is_bounded_and_waits_little()

### Community 178 - "profile/controller.py"
Cohesion: 0.19
Nodes (5): edit_appearance(), profile_service(), AppearanceIn, AppearanceOut, ProfileService

### Community 184 - "BaseModel"
Cohesion: 0.11
Nodes (6): TaskClientOut, TaskCommentIn, TaskEventOut, TaskNetworkOut, TaskPersonOut, TaskSiteOut

### Community 185 - "settings_for_tests"
Cohesion: 0.29
Nodes (4): settings_for_tests(), test_api_does_not_start_without_redis_or_queue_in_any_env(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 186 - "postgres"
Cohesion: 0.33
Nodes (6): POSTGRES_PASSWORD, env, image, options, ports, postgres

### Community 195 - "key_values/controller.py"
Cohesion: 0.12
Nodes (6): KeyValueBuffer, cors(), preflight(), receive(), KeyValueIn, receive_key_values()

### Community 197 - "LoaderService"
Cohesion: 0.05
Nodes (21): create(), delete(), index(), options(), show(), update(), ClientLoaderService, create() (+13 more)

### Community 204 - "Actor"
Cohesion: 0.10
Nodes (11): cancel_owner(), change_status(), client(), client_image(), edit_client_image(), invite_owner(), manager_change(), new_owner() (+3 more)

### Community 210 - "internal/rewards/controller.py"
Cohesion: 0.07
Nodes (11): ad_units(), delete(), delete_lead(), export_leads(), index(), leads(), metrics(), set_active() (+3 more)

### Community 213 - ".assign"
Cohesion: 0.16
Nodes (4): Atribuição de sites, GAM, Networks, Sites e ad units

### Community 219 - "Actor"
Cohesion: 0.17
Nodes (5): classify(), classify_many(), create(), site_options(), sites_of_member()

### Community 220 - "reward_buffer.py"
Cohesion: 0.12
Nodes (4): MemoryRewardBuffer, RedisRewardBuffer, RewardBuffer, _page_views()

### Community 226 - "test_key_values.py"
Cohesion: 0.09
Nodes (7): MemoryKeyValueBuffer, RedisKeyValueBuffer, _buffer(), test_clean_values_of_connected_networks_go_to_the_buffer(), test_four_requests_per_second_per_ip(), test_redis_buffer_follows_the_worker_contract(), test_the_preflight_answers_with_cors()

### Community 239 - "PublicPriceFloorService"
Cohesion: 0.12
Nodes (4): CountryLookup, prices(), PublicPriceFloorsOut, PublicPriceFloorService

### Community 244 - "ClientService"
Cohesion: 0.18
Nodes (6): audit(), client_teams(), ClientMemberOut, ClientService, AuditOut, CompanyRefOut

### Community 250 - "RewardCache"
Cohesion: 0.08
Nodes (6): ad_tag_cache_key(), is_cascade_shape(), safe_site_cascades(), site_cascades(), RewardCache, forget_tags()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 2398 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **114 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `UnitOfWorkFactory` connect `UnitOfWorkFactory` to `PublicRewardService`, `roles/controller.py`, `DashboardService`, `AlertService`, `GamToolService`, `schedules/controller.py`, `.trusted_uow`, `GroupService`, `PageOut`, `AdTagService`, `api_keys/controller.py`, `InvitationOut`, `custom_metrics/controller.py`, `dashboard_templates/controller.py`, `clients/controller.py`, `ClientPriceRuleService`, `mfa/controller.py`, `currencies/controller.py`, `reports/service.py`, `.uow`, `MemberOut`, `modules/ad_tags/dto.py`, `mcm/controller.py`, `PriceRuleService`, `AuthService`, `views/controller.py`, `client_notes/controller.py`, `modules/rewards/service.py`, `members/controller.py`, `ItemsOut`, `RewardService`, `account/controller.py`, `client_documents/controller.py`, `MemberService`, `auth/controller.py`, `company/controller.py`, `documents/controller.py`, `ClientAdTagService`, `costs/controller.py`, `sites/controller.py`, `modules/results/controller.py`, `google/controller.py`, `audit/controller.py`, `reward_public/service.py`, `invoices/service.py`, `ad_tag_public/service.py`, `SupportTaskService`, `contracts/controller.py`, `modules/price_rules/controller.py`, `SiteService`, `commissions/controller.py`, `tasks/dto.py`, `GoalService`, `get`, `ReportService`, `checklists/controller.py`, `CompanyService`, `networks/controller.py`, `goals/service.py`, `router.py`, `profile/controller.py`, `.__init__`, `.__init__`, `LoaderService`, `internal/rewards/controller.py`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `.__init__`, `PublicPriceFloorService`, `.__init__`, `ClientService`, `.__init__`, `RewardCache`, `.__init__`?**
  _High betweenness centrality (0.118) - this node is a cross-community bridge._
- **Are the 172 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_change_password_attempts_are_limited()`) actually correct?**
  _`CapturingMailer` has 172 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `PublicRewardService` be split into smaller, more focused modules?**
  _Cohesion score 0.10960960960960961 - nodes in this community are weakly interconnected._
- **Why does `PageOut` connect `PageOut` to `SupportTaskService`, `tasks/controller.py`, `DashboardService`, `AlertService`, `contracts/controller.py`, `GamToolService`, `goals/controller.py`, `modules/price_rules/controller.py`, `roles/controller.py`, `schedules/controller.py`, `SiteService`, `.trusted_uow`, `GroupService`, `tasks/dto.py`, `AdTagService`, `api_keys/controller.py`, `GoalService`, `get`, `InvitationOut`, `index`, `ReportService`, `clients/controller.py`, `checklists/controller.py`, `ClientPriceRuleService`, `reports/service.py`, `.uow`, `networks/controller.py`, `goals/service.py`, `modules/ad_tags/dto.py`, `.owner_invitations`, `mcm/controller.py`, `router.py`, `MemberOut`, `PriceRuleService`, `checklists`, `client_notes/controller.py`, `modules/rewards/service.py`, `members/controller.py`, `RewardService`, `MemberService`, `LoaderService`, `ClientAdTagService`, `clients`, `modules/rewards/controller.py`, `Actor`, `.of`, `costs/controller.py`, `UnitOfWorkFactory`, `internal/rewards/controller.py`, `AdTagOut`, `sites/controller.py`, `audit/controller.py`, `invoices/service.py`, `ClientService`?**
  _High betweenness centrality (0.084) - this node is a cross-community bridge._
- **Are the 79 inferred relationships involving `PageOut` (e.g. with `index()` and `AdTagService`) actually correct?**
  _`PageOut` has 79 INFERRED edges - model-reasoned connections that need verification._
- **Should `conftest.py` be split into smaller, more focused modules?**
  _Cohesion score 0.10077519379844961 - nodes in this community are weakly interconnected._