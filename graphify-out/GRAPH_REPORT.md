# Graph Report - avant-api  (2026-10-24)

## Corpus Check
- 55 files · ~33,116 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 7 file(s) not represented in the graph (top: (none) 5, .rdb 1, .lock 1)

## Summary
- 849 nodes · 2232 edges · 34 communities (29 shown, 5 thin omitted)
- Extraction: 83% EXTRACTED · 17% INFERRED · 0% AMBIGUOUS · INFERRED: 369 edges (avg confidence: 0.93)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `350d4e37`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- CapturingMailer
- Services
- deps.py
- sites.py
- schemas.py
- company.py
- .uow
- google.py
- steps
- networks.py
- Avant: models do MVP
- limits.py
- roles.py
- test_events.py
- main.py
- Groone Avant: contexto do projeto
- api_keys.py
- invitations.py
- Arquitetura do MVP do Avant
- Avant: endpoints da API do MVP
- Requisitos do novo SaaS AdTech Groone
- Avant: fluxos de login e convite
- GAM
- avant-api
- Acesso
- Avant: conexão com o GAM
- Suporte
- Empresa e equipe
- SiteMemberOut
- Avant: repositório e plano do MVP
- delete
- session-start.sh
- avant-api

## God Nodes (most connected - your core abstractions)
1. `Services` - 125 edges
2. `CapturingMailer` - 47 edges
3. `_onboard_owner()` - 40 edges
4. `_csrf()` - 33 edges
5. `ItemsOut` - 29 edges
6. `_member_client()` - 18 edges
7. `get_services()` - 17 edges
8. `delete()` - 16 edges
9. `get_actor()` - 14 edges
10. `google_callback()` - 14 edges

## Surprising Connections (you probably didn't know these)
- `Company` --references--> `edit()`  [INFERRED]
  docs/decisoes/03-models.md → src/avant_api/routes/company.py
- `Catálogo de permissões` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/routes/company.py
- `Empresa` --references--> `edit()`  [INFERRED]
  docs/decisoes/06-endpoints-api.md → src/avant_api/routes/company.py
- `Resumo` --references--> `users()`  [INFERRED]
  docs/decisoes/04-conexao-gam.md → src/avant_api/routes/internal.py
- `O que já tem` --references--> `edit()`  [INFERRED]
  README.md → src/avant_api/routes/company.py

## Import Cycles
- None detected.

## Communities (34 total, 5 thin omitted)

### Community 0 - "CapturingMailer"
Cohesion: 0.07
Nodes (42): CapturingMailer, Sent, test_change_password_and_sessions(), _csrf(), _bearer(), _create(), test_create_use_and_revoke(), test_permissions_on_keys() (+34 more)

### Community 1 - "Services"
Cohesion: 0.06
Nodes (57): avant-api, Contexto, issues e skills, Modelo de dados, delete_session(), do_change_password(), do_reset_password(), forgot_password(), get_sessions() (+49 more)

### Community 2 - "deps.py"
Cohesion: 0.05
Nodes (30): api_key_actor(), bearer_token(), check_csrf(), get_actor(), get_auth(), get_services(), get_session_actor(), get_session_auth() (+22 more)

### Community 3 - "sites.py"
Cohesion: 0.14
Nodes (13): ad_units(), assign_sites(), create(), index(), link(), members(), show(), sites_of_member() (+5 more)

### Community 4 - "schemas.py"
Cohesion: 0.08
Nodes (33): _person(), AcceptInvitationIn, ActiveCompanyIn, AdUnitPatchIn, AssignNetworkIn, ChangePasswordIn, ClientIn, ClientPatchIn (+25 more)

### Community 5 - "company.py"
Cohesion: 0.23
Nodes (4): edit(), show(), CompanyDetailOut, CompanyPatchIn

### Community 6 - ".uow"
Cohesion: 0.15
Nodes (10): edit(), index(), leave(), remove(), set_permissions(), show(), MemberDetailOut, MemberOut (+2 more)

### Community 7 - "google.py"
Cohesion: 0.08
Nodes (15): GoogleFailed, challenge(), _claims(), GoogleAuth, GoogleOAuth, identity_from_id_token(), _google(), FakeGoogle (+7 more)

### Community 8 - "steps"
Cohesion: 0.06
Nodes (31): AVANT_CORE_ACCESS, AVANT_TEST_DATABASE_URL, AVANT_TEST_MIGRATIONS_URL, AVANT_TEST_REDIS_URL, PGPASSWORD, POSTGRES_PASSWORD, jobs, test (+23 more)

### Community 9 - "networks.py"
Cohesion: 0.18
Nodes (9): connect(), disconnect(), index(), service_account(), show(), sync(), sync_runs(), NetworkDetailOut (+1 more)

### Community 10 - "Avant: models do MVP"
Cohesion: 0.18
Nodes (10): Avant: models do MVP, Company, Decisões de Pedro (22/10/2026), Empresa e equipe, Identidade, Invitation, Membership, User (+2 more)

### Community 11 - "limits.py"
Cohesion: 0.06
Nodes (18): TooManyAttempts, Bucket, BucketResult, BucketRule, Counter, Limiter, MemoryBucket, MemoryCounter (+10 more)

### Community 12 - "roles.py"
Cohesion: 0.18
Nodes (9): API first e chaves de API, create(), edit(), index(), permissions(), remove(), RoleIn, RoleOut (+1 more)

### Community 13 - "test_events.py"
Cohesion: 0.05
Nodes (19): channel(), EventSource, NoEvents, _parse(), RedisEvents, sse(), observe(), _route_template() (+11 more)

### Community 14 - "main.py"
Cohesion: 0.06
Nodes (12): configure_logging(), JsonFormatter, create_app(), index(), events(), AuditOut, Settings, client() (+4 more)

### Community 15 - "Groone Avant: contexto do projeto"
Cohesion: 0.12
Nodes (15): Arquitetura, Como trabalhar nos repositórios, Dicas de ambiente para o agente, Documentos de decisão, GAM, Groone Avant: contexto do projeto, Identidade visual, Infraestrutura e operação (+7 more)

### Community 16 - "api_keys.py"
Cohesion: 0.19
Nodes (6): create(), index(), revoke(), ApiKeyCreatedOut, ApiKeyIn, ApiKeyOut

### Community 17 - "invitations.py"
Cohesion: 0.27
Nodes (7): cancel(), create_invitation(), invitation_out(), list_invitations(), resend(), InvitationOut, InviteIn

### Community 18 - "Arquitetura do MVP do Avant"
Cohesion: 0.15
Nodes (12): Ambientes, deploy e backup, Arquitetura do MVP do Avant, Controle de acesso no estilo do Defender, Decisões e perguntas em aberto, Endpoints da API REST, Estrutura do repositório, Fluxos, Isolamento, autenticação e permissões (+4 more)

### Community 19 - "Avant: endpoints da API do MVP"
Cohesion: 0.18
Nodes (10): Atribuição de sites, Avant: endpoints da API do MVP, Catálogo de permissões, Convenções, Decisões de Pedro (23/10/2026), GAM, Networks, Painel interno (+2 more)

### Community 20 - "Requisitos do novo SaaS AdTech Groone"
Cohesion: 0.17
Nodes (11): Conta e equipe, Escopo herdado do Genius, Integrações e onboarding no Google Ad Manager, Modelo de cobrança, MVP, Opções de nome, Perguntas em aberto, Problemas a resolver (+3 more)

### Community 21 - "Avant: fluxos de login e convite"
Cohesion: 0.17
Nodes (11): 2FA, Avant: fluxos de login e convite, Com Google, Com senha, Convite e primeiro acesso, Decisões de Pedro (23/10/2026), Endpoints de autenticação, Escolha da Empresa ativa (+3 more)

### Community 22 - "GAM"
Cohesion: 0.33
Nodes (6): AdUnit, GAM, Network, NetworkSyncRun, Site, SiteAssignment

### Community 23 - "avant-api"
Cohesion: 0.33
Nodes (5): avant-api, Como funciona, Desenvolvimento, Imagem, O que já tem

### Community 24 - "Acesso"
Cohesion: 0.40
Nodes (5): Acesso, MemberPermission, Permission, Role, RolePermission

### Community 25 - "Avant: conexão com o GAM"
Cohesion: 0.20
Nodes (9): Avant: conexão com o GAM, Caminho conta de serviço, Caminho MCM, Decisões de Pedro (23/10/2026), Erros e estados, Fontes, Importação, Resumo (+1 more)

### Community 26 - "Suporte"
Cohesion: 0.40
Nodes (5): ApiKey, AuditLog, PasswordReset, Session, Suporte

### Community 27 - "Empresa e equipe"
Cohesion: 0.40
Nodes (5): Convites, Empresa, Empresa e equipe, Membros, Papéis e permissões

### Community 29 - "Avant: repositório e plano do MVP"
Cohesion: 0.22
Nodes (8): Avant: repositório e plano do MVP, Decisões de Pedro (23/10/2026), Estrutura de pastas, Pipeline, Plano até 31/12, Primeira semana (23/10 a 02/11), Resumo, Serviços e ferramentas

## Knowledge Gaps
- **1 isolated node(s):** `avant-api`
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 322 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Services` connect `Services` to `CapturingMailer`, `deps.py`, `sites.py`, `company.py`, `.uow`, `google.py`, `networks.py`, `limits.py`, `roles.py`, `test_events.py`, `main.py`, `api_keys.py`, `invitations.py`, `delete`?**
  _High betweenness centrality (0.335) - this node is a cross-community bridge._
- **Are the 105 inferred relationships involving `Services` (e.g. with `api_key_actor()` and `check_csrf()`) actually correct?**
  _`Services` has 105 INFERRED edges - model-reasoned connections that need verification._
- **What connects `avant-api` to the rest of the system?**
  _1 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `CapturingMailer` be split into smaller, more focused modules?**
  _Cohesion score 0.06505050505050505 - nodes in this community are weakly interconnected._
- **Why does `edit()` connect `company.py` to `Services`, `.uow`, `Avant: models do MVP`, `Avant: endpoints da API do MVP`, `avant-api`, `Empresa e equipe`?**
  _High betweenness centrality (0.093) - this node is a cross-community bridge._
- **Are the 32 inferred relationships involving `CapturingMailer` (e.g. with `test_change_password_and_sessions()` and `test_forgot_and_reset_password()`) actually correct?**
  _`CapturingMailer` has 32 INFERRED edges - model-reasoned connections that need verification._
- **Should `Services` be split into smaller, more focused modules?**
  _Cohesion score 0.05711022272986865 - nodes in this community are weakly interconnected._