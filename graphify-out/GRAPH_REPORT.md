# Graph Report - avant-api  (2026-10-24)

## Corpus Check
- 59 files · ~38,033 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 8 file(s) not represented in the graph (top: (none) 6, .rdb 1, .lock 1)

## Summary
- 1124 nodes · 2755 edges · 69 communities (43 shown, 26 thin omitted)
- Extraction: 85% EXTRACTED · 15% INFERRED · 0% AMBIGUOUS · INFERRED: 421 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `a669e97d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- CapturingMailer
- Services
- edit
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
- avant_api/events.py
- audit.py
- Groone Avant: contexto do projeto
- api_keys.py
- account.py
- Arquitetura do MVP do Avant
- auth.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- test_account.py
- .uow
- tasks.py
- Avant: conexão com o GAM
- clean_code.py
- create_app
- deps.py
- Avant: repositório e plano do MVP
- Settings
- health.py
- logs.py
- session-start.sh
- avant-api
- SiteMemberOut
- catalog
- install
- RedisCounter
- Counter
- MemoryBucket
- google_callback
- limits.py
- limits.py
- MemoryCounter
- .build
- .take
- uuid
- edit
- create
- reports.py
- pytest
- require
- ad_units
- permissions
- .of
- show
- observe
- avant-api
- AuditOut
- GoogleAuth
- Empresa e equipe
- _contract_fields
- GoogleFailed
- McmCandidateOut
- source_files
- .of

## God Nodes (most connected - your core abstractions)
1. `Services` - 136 edges
2. `CapturingMailer` - 57 edges
3. `_onboard_owner()` - 50 edges
4. `_csrf()` - 42 edges
5. `ItemsOut` - 31 edges
6. `_member_client()` - 21 edges
7. `get_services()` - 19 edges
8. `delete()` - 17 edges
9. `get_actor()` - 14 edges
10. `create_app()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/routes/company.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/routes/company.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/routes/internal.py
- `GAM` --references--> `contracts()`  [INFERRED]
  docs/contexto.md → src/avant_api/routes/internal.py
- `Como trabalhar nos repositórios` --references--> `main()`  [INFERRED]
  docs/contexto.md → scripts/clean_code.py

## Import Cycles
- None detected.

## Communities (69 total, 26 thin omitted)

### Community 0 - "CapturingMailer"
Cohesion: 0.05
Nodes (53): CapturingMailer, Sent, _csrf(), _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys(), test_rate_limit() (+45 more)

### Community 1 - "Services"
Cohesion: 0.06
Nodes (43): avant-api, Contexto, issues e skills, Modelo de dados, assign_network(), audit(), cancel_owner(), client(), clients() (+35 more)

### Community 2 - "edit"
Cohesion: 0.17
Nodes (5): create(), edit(), index(), remove(), RoleOut

### Community 3 - "sites.py"
Cohesion: 0.18
Nodes (4): assign_sites(), create(), SiteListOut, SiteOut

### Community 4 - "schemas.py"
Cohesion: 0.08
Nodes (33): AcceptInvitationIn, ActiveCompanyIn, AdUnitPatchIn, AssignNetworkIn, ClientIn, ClientPatchIn, CompanyDetailOut, CompanyOut (+25 more)

### Community 6 - ".uow"
Cohesion: 0.13
Nodes (8): edit(), index(), leave(), remove(), set_permissions(), show(), MemberDetailOut, MemberOut

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "networks.py"
Cohesion: 0.12
Nodes (10): connect(), disconnect(), enqueue_sync(), index(), service_account(), show(), sync(), sync_runs() (+2 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "Limiter"
Cohesion: 0.33
Nodes (4): Limiter, Rule, _limiter_round(), test_memory_limiter()

### Community 12 - "Avant: endpoints da API do MVP"
Cohesion: 0.20
Nodes (9): Atribuição de sites, Avant: endpoints da API do MVP, Convenções, Decisões de Pedro (23/10/2026), GAM, Networks, Painel interno, Sites e ad units (+1 more)

### Community 13 - "avant_api/events.py"
Cohesion: 0.15
Nodes (5): channel(), EventSource, NoEvents, _parse(), sse()

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (14): Arquitetura, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação, Modelo de contas (+6 more)

### Community 17 - "account.py"
Cohesion: 0.11
Nodes (14): delete_session(), do_change_password(), do_reset_password(), forgot_password(), google_status(), google_unlink(), revoke_others(), _session() (+6 more)

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.17
Nodes (11): Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões, Observabilidade (+3 more)

### Community 19 - "auth.py"
Cohesion: 0.08
Nodes (18): accept(), _client(), do_logout(), get_invitation(), login(), me(), set_active_company(), _set_cookies() (+10 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "test_account.py"
Cohesion: 0.27
Nodes (8): _google_round(), _jwt(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_id_token_claims(), test_login_attempts_are_limited()

### Community 23 - ".uow"
Cohesion: 0.21
Nodes (4): delete(), index(), members(), sites_of_member()

### Community 24 - "tasks.py"
Cohesion: 0.12
Nodes (3): CeleryQueue, RecordingQueue, TaskQueue

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 26 - "clean_code.py"
Cohesion: 0.18
Nodes (5): check_file(), docstring_problems(), inline_comments(), is_exempt(), single_letter_names()

### Community 28 - "deps.py"
Cohesion: 0.13
Nodes (11): api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_session_actor(), get_session_auth(), optional_auth() (+3 more)

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.17
Nodes (11): Como trabalhar nos repositórios, Ambientes, deploy e backup, Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11) (+3 more)

### Community 31 - "health.py"
Cohesion: 0.22
Nodes (3): health(), metrics(), ready()

### Community 37 - "catalog"
Cohesion: 0.16
Nodes (4): catalog(), DimensionOut, LabelOut, MetricOut

### Community 38 - "install"
Cohesion: 0.18
Nodes (6): error_body(), install(), domain_error(), http_error(), unexpected(), validation_error()

### Community 41 - "MemoryBucket"
Cohesion: 0.28
Nodes (4): MemoryBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 42 - "google_callback"
Cohesion: 0.17
Nodes (7): GoogleUnavailable, new_verifier(), _back(), get_sessions(), _google(), google_callback(), google_start()

### Community 46 - ".build"
Cohesion: 0.20
Nodes (5): RedisEvents, _google(), _mailer(), test_redis_source_delivers_published_messages(), run()

### Community 48 - "uuid"
Cohesion: 0.25
Nodes (6): _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 49 - "edit"
Cohesion: 0.20
Nodes (3): Catálogo de permissões, edit(), show()

### Community 50 - "create"
Cohesion: 0.15
Nodes (8): create(), _person(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut, CompanyRefOut, PersonOut, UserOut

### Community 51 - "reports.py"
Cohesion: 0.09
Nodes (10): QueryTooHeavy, _csv(), export(), _number(), query(), _run(), _safe_cell(), _statement_timeout() (+2 more)

### Community 52 - "pytest"
Cohesion: 0.24
Nodes (5): client(), engine(), mailer(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 53 - "require"
Cohesion: 0.24
Nodes (4): require(), dependency(), require_session(), require_staff()

### Community 54 - "ad_units"
Cohesion: 0.28
Nodes (3): ad_units(), link(), AdUnitOut

### Community 56 - ".of"
Cohesion: 0.18
Nodes (4): dimension_text(), ReportRangeOut, ReportResultOut, ReportRowOut

### Community 59 - "avant-api"
Cohesion: 0.33
Nodes (5): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem

### Community 62 - "Empresa e equipe"
Cohesion: 0.40
Nodes (5): Convites, Empresa, Empresa e equipe, Membros, Papéis e permissões

### Community 64 - "GoogleFailed"
Cohesion: 0.15
Nodes (4): GoogleFailed, _claims(), identity_from_id_token(), FakeGoogle

### Community 68 - ".of"
Cohesion: 0.17
Nodes (6): ContractClientRefOut, ContractNetworkOut, ContractNetworkRefOut, ContractSummaryOut, _network_ref(), NetworkOut

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 494 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **26 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Services` connect `Services` to `CapturingMailer`, `edit`, `sites.py`, `main.py`, `.uow`, `networks.py`, `Limiter`, `avant_api/events.py`, `audit.py`, `api_keys.py`, `account.py`, `auth.py`, `.uow`, `tasks.py`, `create_app`, `deps.py`, `Settings`, `health.py`, `RedisCounter`, `Counter`, `MemoryBucket`, `google_callback`, `limits.py`, `MemoryCounter`, `.build`, `edit`, `create`, `reports.py`, `pytest`, `ad_units`, `show`, `GoogleAuth`?**
  _High betweenness centrality (0.399) - this node is a cross-community bridge._
- **Are the 115 inferred relationships involving `Services` (e.g. with `api_key_actor()` and `check_csrf()`) actually correct?**
  _`Services` has 115 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `CapturingMailer` be split into smaller, more focused modules?**
  _Cohesion score 0.050694919115971744 - nodes in this community are weakly interconnected._
- **Why does `edit()` connect `edit` to `Services`, `schemas.py`, `main.py`, `Avant: models do MVP`, `.uow`, `avant-api`, `Empresa e equipe`?**
  _High betweenness centrality (0.063) - this node is a cross-community bridge._
- **Are the 40 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 40 INFERRED edges - model-reasoned connections that need verification._
- **Should `Services` be split into smaller, more focused modules?**
  _Cohesion score 0.055353535353535356 - nodes in this community are weakly interconnected._