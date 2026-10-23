# Graph Report - avant-api  (2026-10-23)

## Corpus Check
- 55 files · ~32,696 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 5, .rdb 1, .lock 1)

## Summary
- 849 nodes · 2204 edges · 36 communities (28 shown, 8 thin omitted)
- Extraction: 84% EXTRACTED · 16% INFERRED · 0% AMBIGUOUS · INFERRED: 361 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `0128453d`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- CapturingMailer
- Services
- deps.py
- .uow
- schemas.py
- company.py
- account.py
- google.py
- steps
- networks.py
- Avant: models do MVP
- limits.py
- roles.py
- services.py
- main.py
- Groone Avant: contexto do projeto
- .build
- test_events.py
- Arquitetura do MVP do Avant
- avant_api/events.py
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- Limiter
- test_account.py
- fastapi
- Avant: conexão com o GAM
- pytest
- RedisCounter
- audit.py
- Avant: repositório e plano do MVP
- ready
- Counter
- events
- session-start.sh
- avant-api

## God Nodes (most connected - your core abstractions)
1. `Services` - 123 edges
2. `CapturingMailer` - 46 edges
3. `_onboard_owner()` - 39 edges
4. `_csrf()` - 32 edges
5. `ItemsOut` - 29 edges
6. `get_services()` - 17 edges
7. `_member_client()` - 17 edges
8. `get_actor()` - 14 edges
9. `google_callback()` - 14 edges
10. `login()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/routes/company.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/routes/internal.py
- `API first e chaves de API` --references--> `permissions()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/routes/roles.py
- `Catálogo de permissões` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/routes/company.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/routes/company.py

## Import Cycles
- None detected.

## Communities (36 total, 8 thin omitted)

### Community 0 - "CapturingMailer"
Cohesion: 0.06
Nodes (43): CapturingMailer, client(), engine(), mailer(), Sent, _csrf(), _bearer(), _create() (+35 more)

### Community 1 - "Services"
Cohesion: 0.07
Nodes (47): avant-api, Contexto, issues e skills, Modelo de dados, assign_network(), audit(), cancel_owner(), client(), clients() (+39 more)

### Community 2 - "deps.py"
Cohesion: 0.05
Nodes (28): api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_services(), get_session_actor(), get_session_auth() (+20 more)

### Community 3 - ".uow"
Cohesion: 0.06
Nodes (26): edit(), index(), leave(), remove(), set_permissions(), show(), ad_units(), assign_sites() (+18 more)

### Community 4 - "schemas.py"
Cohesion: 0.08
Nodes (27): accept(), _client(), do_logout(), _end(), get_invitation(), login(), me(), set_active_company() (+19 more)

### Community 5 - "company.py"
Cohesion: 0.07
Nodes (25): API first e chaves de API, Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Convites, Decisões de Pedro (23/10/2026), Empresa (+17 more)

### Community 6 - "account.py"
Cohesion: 0.11
Nodes (20): GoogleUnavailable, _back(), delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions(), _google() (+12 more)

### Community 7 - "google.py"
Cohesion: 0.10
Nodes (10): GoogleFailed, challenge(), _claims(), GoogleAuth, GoogleOAuth, identity_from_id_token(), new_verifier(), FakeGoogle (+2 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "networks.py"
Cohesion: 0.17
Nodes (12): connect(), disconnect(), enqueue_sync(), index(), service_account(), show(), sync(), sync_runs() (+4 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.07
Nodes (26): Acesso, AdUnit, ApiKey, AuditLog, Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe (+18 more)

### Community 11 - "limits.py"
Cohesion: 0.14
Nodes (8): Bucket, BucketResult, BucketRule, MemoryBucket, RedisBucket, _exercise(), test_memory_bucket(), test_redis_bucket()

### Community 12 - "roles.py"
Cohesion: 0.18
Nodes (9): create(), edit(), index(), permissions(), remove(), PermissionOut, RoleIn, RoleOut (+1 more)

### Community 13 - "services.py"
Cohesion: 0.13
Nodes (3): CeleryQueue, RecordingQueue, TaskQueue

### Community 14 - "main.py"
Cohesion: 0.13
Nodes (3): configure_logging(), JsonFormatter, create_app()

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (15): Arquitetura, Como trabalhar nos repositórios, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação (+7 more)

### Community 16 - ".build"
Cohesion: 0.14
Nodes (5): NoEvents, MemoryCounter, _google(), _mailer(), Settings

### Community 17 - "test_events.py"
Cohesion: 0.27
Nodes (6): _collect(), _event(), ListEvents, test_events_route(), test_stream_closes_after_the_limit(), test_stream_filters_by_permission_and_sends_heartbeats()

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Ambientes, deploy e backup, Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões (+4 more)

### Community 19 - "avant_api/events.py"
Cohesion: 0.26
Nodes (4): channel(), EventSource, _parse(), sse()

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "Limiter"
Cohesion: 0.35
Nodes (5): TooManyAttempts, Limiter, Rule, _limiter_round(), test_memory_limiter()

### Community 23 - "test_account.py"
Cohesion: 0.40
Nodes (6): _google_round(), _login(), test_change_password_and_sessions(), test_forgot_and_reset_password(), test_google_link_and_login(), test_login_attempts_are_limited()

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 26 - "pytest"
Cohesion: 0.27
Nodes (5): RedisEvents, test_redis_source_delivers_published_messages(), run(), test_queue_does_not_break_the_request_without_broker(), test_resend_key_required_outside_local()

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.22
Nodes (8): Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11), Resumo, Serviços e ferramentas

### Community 30 - "ready"
Cohesion: 0.22
Nodes (3): health(), metrics(), ready()

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 326 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **8 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Services` connect `Services` to `CapturingMailer`, `deps.py`, `.uow`, `schemas.py`, `company.py`, `account.py`, `google.py`, `networks.py`, `limits.py`, `roles.py`, `services.py`, `main.py`, `.build`, `avant_api/events.py`, `Limiter`, `pytest`, `RedisCounter`, `audit.py`, `ready`, `events`?**
  _High betweenness centrality (0.337) - this node is a cross-community bridge._
- **Are the 103 inferred relationships involving `Services` (e.g. with `api_key_actor()` and `check_csrf()`) actually correct?**
  _`Services` has 103 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `CapturingMailer` be split into smaller, more focused modules?**
  _Cohesion score 0.06198019801980198 - nodes in this community are weakly interconnected._
- **Why does `edit()` connect `company.py` to `Services`, `Avant: models do MVP`, `.uow`?**
  _High betweenness centrality (0.093) - this node is a cross-community bridge._
- **Are the 31 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 31 INFERRED edges - model-reasoned connections that need verification._
- **Should `Services` be split into smaller, more focused modules?**
  _Cohesion score 0.075 - nodes in this community are weakly interconnected._