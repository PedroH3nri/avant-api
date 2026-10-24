# Graph Report - avant-api  (2026-10-24)

## Corpus Check
- 58 files · ~36,723 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 1082 nodes · 2615 edges · 70 communities (49 shown, 21 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 394 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `91dc5230`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- _csrf
- Services
- RateLimited
- sites.py
- schemas.py
- main.py
- .uow
- google.py
- steps
- networks.py
- Avant: models do MVP
- Limiter
- Avant: endpoints da API do MVP
- test_events.py
- audit.py
- Groone Avant: contexto do projeto
- api_keys.py
- account.py
- Arquitetura do MVP do Avant
- auth.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- conftest.py
- test_reports.py
- tasks.py
- Avant: conexão com o GAM
- clean_code.py
- main.py
- deps.py
- Avant: repositório e plano do MVP
- CapturingMailer
- health.py
- _number
- session-start.sh
- avant-api
- MemberOut
- catalog
- install
- RedisCounter
- Counter
- MemoryBucket
- google_start
- TooManyAttempts
- limits.py
- MemoryCounter
- _onboard_owner
- .take
- Authenticated
- edit
- create
- reports.py
- _csv
- test_api_keys.py
- test_networks.py
- _run
- .of
- test_sites.py
- GAM
- avant-api
- Acesso
- Suporte
- Empresa e equipe
- _person
- FakeGoogle
- McmCandidateOut
- source_files
- AcceptInvitationIn
- AdUnitPatchIn
- ServiceAccountOut

## God Nodes (most connected - your core abstractions)
1. `Services` - 129 edges
2. `CapturingMailer` - 54 edges
3. `_onboard_owner()` - 47 edges
4. `_csrf()` - 39 edges
5. `ItemsOut` - 29 edges
6. `_member_client()` - 21 edges
7. `get_services()` - 19 edges
8. `delete()` - 16 edges
9. `get_actor()` - 14 edges
10. `create_app()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/routes/company.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/routes/company.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/routes/internal.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py
- `Ambientes, deploy e backup` --references--> `main()`  [INFERRED]
  docs/decisoes/02-arquitetura.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (70 total, 21 thin omitted)

### Community 0 - "_csrf"
Cohesion: 0.19
Nodes (10): _csrf(), _staff(), test_client_owner_cannot_reach_internal(), test_internal_clients(), test_internal_people_and_staff(), _enable(), _now_code(), test_client_can_disable() (+2 more)

### Community 1 - "Services"
Cohesion: 0.06
Nodes (33): avant-api, Contexto, issues e skills, Modelo de dados, assign_network(), audit(), cancel_owner(), client(), clients() (+25 more)

### Community 2 - "RateLimited"
Cohesion: 0.25
Nodes (3): QueryTooHeavy, RateLimited, _statement_timeout()

### Community 3 - "sites.py"
Cohesion: 0.05
Nodes (20): API first e chaves de API, create(), edit(), index(), permissions(), remove(), ad_units(), assign_sites() (+12 more)

### Community 4 - "schemas.py"
Cohesion: 0.09
Nodes (34): ActiveCompanyIn, AssignNetworkIn, AuditOut, ChangePasswordIn, ClientIn, ClientPatchIn, CompanyOut, CompanyPatchIn (+26 more)

### Community 6 - ".uow"
Cohesion: 0.17
Nodes (8): edit(), index(), leave(), remove(), set_permissions(), show(), MemberDetailOut, Services

### Community 7 - "google.py"
Cohesion: 0.11
Nodes (7): GoogleFailed, challenge(), _claims(), GoogleOAuth, identity_from_id_token(), _jwt(), test_id_token_claims()

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "networks.py"
Cohesion: 0.11
Nodes (10): connect(), disconnect(), enqueue_sync(), index(), service_account(), show(), sync(), sync_runs() (+2 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.18
Nodes (10): Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade, Invitation, Membership, User (+2 more)

### Community 11 - "Limiter"
Cohesion: 0.33
Nodes (4): Limiter, Rule, _limiter_round(), test_memory_limiter()

### Community 12 - "Avant: endpoints da API do MVP"
Cohesion: 0.20
Nodes (9): Atribuição de sites, Avant: endpoints da API do MVP, Convenções, Decisões de Pedro (23/10/2026), GAM, Networks, Painel interno, Sites e ad units (+1 more)

### Community 13 - "test_events.py"
Cohesion: 0.06
Nodes (17): channel(), EventSource, _parse(), RedisEvents, sse(), observe(), _route_template(), _collect() (+9 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 17 - "account.py"
Cohesion: 0.15
Nodes (8): GoogleUnavailable, delete_session(), do_reset_password(), forgot_password(), _google(), google_callback(), _session(), _client()

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 19 - "auth.py"
Cohesion: 0.07
Nodes (20): accept(), do_logout(), _end(), get_invitation(), login(), me(), set_active_company(), _set_cookies() (+12 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "conftest.py"
Cohesion: 0.12
Nodes (9): engine(), mailer(), Sent, _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login() (+1 more)

### Community 23 - "test_reports.py"
Cohesion: 0.17
Nodes (9): _day(), _metrics(), _row(), test_catalog_hides_internal_metrics(), test_export_csv_uses_names_and_escapes_formulas(), test_query_needs_permission(), test_query_refuses_bad_definitions_and_internal_metrics(), test_query_totals_rows_and_member_sites() (+1 more)

### Community 24 - "tasks.py"
Cohesion: 0.08
Nodes (8): NoEvents, GoogleAuth, Bucket, _google(), _mailer(), CeleryQueue, RecordingQueue, TaskQueue

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 26 - "clean_code.py"
Cohesion: 0.17
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 27 - "main.py"
Cohesion: 0.10
Nodes (5): configure_logging(), create_app(), events(), Settings, client()

### Community 28 - "deps.py"
Cohesion: 0.12
Nodes (13): api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor(), get_session_auth(), optional_auth() (+5 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 30 - "CapturingMailer"
Cohesion: 0.29
Nodes (8): CapturingMailer, _member_client(), test_audit_log(), test_company_and_members(), test_leave_company(), test_requires_session(), test_resend_and_cancel_invitation(), test_roles_and_direct_permissions()

### Community 31 - "health.py"
Cohesion: 0.22
Nodes (3): health(), metrics(), ready()

### Community 36 - "MemberOut"
Cohesion: 0.15
Nodes (4): DirectPermissionOut, MemberOut, RoleRefOut, SiteMemberOut

### Community 38 - "install"
Cohesion: 0.18
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 41 - "MemoryBucket"
Cohesion: 0.33
Nodes (4): MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 42 - "google_start"
Cohesion: 0.32
Nodes (3): new_verifier(), _back(), google_start()

### Community 46 - "_onboard_owner"
Cohesion: 0.36
Nodes (8): _onboard_owner(), _owner_invite(), test_csrf_is_required_for_writes(), test_health_and_metrics(), test_owner_onboarding_and_login(), test_seat_limit(), test_team_invitation_flow(), test_validation_error_format()

### Community 48 - "Authenticated"
Cohesion: 0.18
Nodes (5): do_change_password(), get_sessions(), google_status(), google_unlink(), revoke_others()

### Community 49 - "edit"
Cohesion: 0.21
Nodes (4): Catálogo de permissões, edit(), show(), CompanyDetailOut

### Community 50 - "create"
Cohesion: 0.24
Nodes (5): create(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, UserOut

### Community 52 - "_csv"
Cohesion: 0.22
Nodes (3): _csv(), export(), dimension_text()

### Community 53 - "test_api_keys.py"
Cohesion: 0.44
Nodes (5): _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit()

### Community 54 - "test_networks.py"
Cohesion: 0.47
Nodes (6): _queue(), _second_owner(), test_connect_sync_and_disconnect(), test_internal_assigns_unowned_mcm_network(), test_networks_are_isolated_per_company(), test_networks_need_permission()

### Community 55 - "_run"
Cohesion: 0.28
Nodes (3): query(), _run(), ReportQueryIn

### Community 56 - ".of"
Cohesion: 0.25
Nodes (3): ReportRangeOut, ReportResultOut, ReportRowOut

### Community 57 - "test_sites.py"
Cohesion: 0.46
Nodes (3): _inventory(), test_manual_site(), test_sites_and_assignment()

### Community 58 - "GAM"
Cohesion: 0.33
Nodes (6): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment

### Community 59 - "avant-api"
Cohesion: 0.33
Nodes (5): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem

### Community 60 - "Acesso"
Cohesion: 0.40
Nodes (5): Acesso, MemberPermission, Permission, Role, RolePermission

### Community 61 - "Suporte"
Cohesion: 0.40
Nodes (5): ApiKey, AuditLog, PasswordReset, Session, Suporte

### Community 62 - "Empresa e equipe"
Cohesion: 0.40
Nodes (5): Convites, Empresa, Empresa e equipe, Membros, Papéis e permissões

### Community 63 - "_person"
Cohesion: 0.40
Nodes (3): _person(), CompanyRefOut, PersonOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 481 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **21 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Services` connect `.uow` to `Services`, `sites.py`, `main.py`, `networks.py`, `Limiter`, `test_events.py`, `audit.py`, `api_keys.py`, `account.py`, `auth.py`, `tasks.py`, `main.py`, `deps.py`, `health.py`, `RedisCounter`, `MemoryBucket`, `google_start`, `limits.py`, `MemoryCounter`, `Authenticated`, `edit`, `create`, `reports.py`, `_csv`, `_run`?**
  _High betweenness centrality (0.387) - this node is a cross-community bridge._
- **Are the 108 inferred relationships involving `Services` (e.g. with `api_key_actor()` and `check_csrf()`) actually correct?**
  _`Services` has 108 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Services` be split into smaller, more focused modules?**
  _Cohesion score 0.05822784810126582 - nodes in this community are weakly interconnected._
- **Why does `edit()` connect `edit` to `sites.py`, `schemas.py`, `main.py`, `.uow`, `Avant: models do MVP`, `avant-api`, `Empresa e equipe`?**
  _High betweenness centrality (0.095) - this node is a cross-community bridge._
- **Are the 38 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 38 INFERRED edges - model-reasoned connections that need verification._
- **Should `sites.py` be split into smaller, more focused modules?**
  _Cohesion score 0.05413469735720375 - nodes in this community are weakly interconnected._