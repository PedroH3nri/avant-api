# avant-api

API REST do Groone Avant, em FastAPI. Todas as rotas ficam em `/api/v1`, e a
documentação OpenAPI em `/api/docs` (só para a equipe Groone com 2FA). O domínio, os casos de uso e o banco vêm do
[avant-core](https://github.com/PedroH3nri/avant-core): esta API só traduz HTTP.

Outros repositórios: avant-core, avant-worker, avant-web, avant-infra.

## O que já tem

| Rota | Faz | Permissão |
| --- | --- | --- |
| `GET /health` | o processo está de pé | nenhuma |
| `GET /ready` | o banco responde | nenhuma |
| `GET /metrics` | Prometheus; bloqueado no nginx. Com `WEB_CONCURRENCY` > 1, `PROMETHEUS_MULTIPROC_DIR` é obrigatória (a imagem já traz `/tmp/avant-metrics`, limpo a cada subida) e a resposta soma todos os processos | rede interna |
| `POST /auth/login` | e-mail e senha; abre a sessão | nenhuma |
| `POST /auth/logout` | encerra a sessão | sessão |
| `GET /auth/me` | pessoa, Empresas, Empresa ativa e permissões | sessão |
| `POST /auth/me/active-company` | troca a Empresa ativa | sessão |
| `GET /auth/me/companies/{id}/image` | imagem de uma Empresa da pessoa, para o seletor | membro ativo |
| `GET /auth/invitations/{token}` | dados do convite para a tela do link | nenhuma |
| `POST /auth/invitations/{token}/accept` | aceita: cria conta (e a Empresa, no convite de dono) ou usa a sessão | conforme o caso |
| `POST /auth/mfa/verify` | código do 2FA depois da senha; troca a pré-sessão pela sessão | pré-sessão |
| `POST /auth/mfa/setup` e `/confirm` | ativa o 2FA; o confirm devolve os 10 códigos de recuperação | sessão |
| `POST /auth/mfa/recovery-codes` | gera novos códigos de recuperação | sessão + código |
| `DELETE /auth/mfa` | desliga o 2FA (só clientes) | sessão + código |
| `POST /auth/password/forgot` | agenda o link de nova senha no worker; responde 202 exista ou não a conta | nenhuma |
| `POST /auth/password/reset` | nova senha pelo link (com 2FA, pede o código); encerra todas as sessões | nenhuma |
| `POST /auth/password/change` | troca a senha; encerra as outras sessões | sessão |
| `GET /auth/sessions` | sessões ativas, com a atual marcada | sessão |
| `DELETE /auth/sessions/{id}` | encerra uma sessão | sessão |
| `POST /auth/sessions/revoke-others` | encerra todas menos a atual | sessão |
| `GET /auth/google/start?mode=login\|link` | manda para o Google; `link` liga a conta em Configurações | nenhuma ou sessão |
| `GET /auth/google/callback` | volta do Google e redireciona para o painel | nenhuma |
| `GET /auth/google` e `DELETE /auth/google` | se o Google está ligado; desligar | sessão |
| `GET /invitations?page=` | convites pendentes em páginas de 10, o mais recente primeiro | `team.view` |
| `POST /invitations` | convida por e-mail e papel | `team.invite` |
| `POST /invitations/{id}/resend` | token novo e mais 1 dia | `team.invite` |
| `DELETE /invitations/{id}` | cancela e libera a vaga | `team.invite` |
| `GET /company` | Empresa ativa, com vagas usadas | membro |
| `PATCH /company` | nome, cor e preferências | `company.edit` |
| `GET /company/image` | imagem da Empresa ativa em WebP 256x256, com `ETag` e cache pela URL `?v=` | membro |
| `PUT /company/image`, `DELETE /company/image` | troca (corpo = arquivo PNG, JPEG ou WebP até 2 MB) ou tira a imagem | `company.edit` |
| `GET /company/documents` | identidade e comprovante de residência enviados e `required` (a Empresa tem network Manage Inventory) | `company.edit` |
| `PUT /company/documents/{identity\|address}?name=` | envia ou troca o documento (corpo = arquivo JPG, PNG ou PDF até 5 MB); volta para em análise, aprovado não se troca | `company.edit` |
| `GET /company/documents/{kind}/file` | baixa o arquivo (sem cache; vai para o histórico) | `company.edit` |
| `GET /company/fiscal`, `PUT /company/fiscal` | dados fiscais de pagamento; só o cliente grava, todos juntos | `company.edit` |
| `GET /members?page=` | equipe em páginas de 10 (`items`, `total`, `page`, `pages`, `page_size`), mais recente primeiro; filtros `status`, `role`, `q` no banco | `team.view` |
| `GET /members/options` | a equipe inteira, sem paginar, para seletores e telas que juntam pessoas (grupos, donos de relatório) | `team.view` |
| `GET /members/{id}` | detalhe com permissões diretas | `team.view` |
| `PATCH /members/{id}` | troca papel, suspende ou reativa | `team.manage` |
| `DELETE /members/{id}` | remove e libera a vaga | `team.manage` |
| `POST /members/me/leave` | sai da Empresa (o dono não pode) | membro |
| `PUT /members/{id}/permissions` | lista inteira de permissões diretas | `permissions.grant` |
| `GET /permissions` | catálogo de cliente com nomes PT/EN/ES | `roles.view` |
| `GET /roles/options` | papéis só com `id` e `name`, inteiros, para os seletores | `roles.view` |
| `GET /roles?page=` | predefinidos e personalizados, com contagem, em páginas de 10 | `roles.view` |
| `POST /roles`, `PATCH /roles/{id}`, `DELETE /roles/{id}` | papéis personalizados | `roles.manage` |
| `GET /groups?page=`, `GET /groups/{id}` | grupos de funcionários com as pessoas, em páginas de 10, o mais recente primeiro; `GET /groups/options` traz todos para telas que juntam pessoas e grupos | `groups.view` |
| `POST /groups`, `PATCH /groups/{id}`, `DELETE /groups/{id}` | criar (com pelo menos uma pessoa), renomear, excluir | `groups.manage` |
| `POST /groups/{id}/members`, `DELETE /groups/{id}/members/{membership_id}` | pôr e tirar pessoas; a última não sai (409) | `groups.manage` |
| `GET /audit?page=` | histórico em páginas de 10, o mais recente primeiro; filtros `actor`, `action`, `from`, `to` | `audit.view` |
| `GET /networks` | uma página (`page`) das networks do GAM, a mais recente primeiro, com as últimas etapas e os sites ativos | `network.view` |
| `GET /networks/options` | todas as networks, para seletores | `network.view` |
| `GET /networks/service-account` | e-mail da conta de serviço para o guia de conexão | `network.connect` |
| `POST /networks` | conecta pelo network code; 202, nasce `pending` e o worker testa | `network.connect` |
| `GET /networks/{id}`, `/sync-runs` | detalhe e histórico das etapas (em páginas, `page`) | `network.view` |
| `POST /networks/{id}/sync` | "sincronizar agora"; 1 vez a cada 10 minutos (429 com `Retry-After`) | `network.sync` |
| `POST /networks/{id}/disconnect` | para as sincronizações; o histórico fica | `network.disconnect` |
| `GET /api-keys?page=` | chaves da Empresa (com `api_keys.manage`) ou só as próprias, em páginas de 10, as ativas primeiro | membro |
| `POST /api-keys` | cria uma chave; o valor `avk_...` volta só nesta resposta; só pela sessão | `api_keys.manage` |
| `DELETE /api-keys/{id}` | revoga; a dona da chave ou quem gerencia | membro |
| `GET /sites` | uma página (`page`) dos sites da Empresa, o mais recente primeiro (filtros `network_id`, `approval_status`, `q`, `include_archived`); quem não vê todos recebe só os atribuídos | `sites.view` |
| `GET /sites/options` | todos os sites não arquivados que a pessoa vê, para seletores | `sites.view` |
| `POST /sites` | cadastra site pelo domínio, aguardando o GAM (`awaiting_gam`); a importação junta ao site do GAM com o mesmo domínio | `sites.manage` |
| `GET /sites/{id}` | detalhe com os ad units; `assigned_to` só para quem atribui | `sites.view` |
| `DELETE /sites/{id}` | remove o site que ainda aguarda o GAM (o do GAM responde `site_from_gam`) | `sites.manage` |
| `GET /sites/{id}/members` | quem vê o site: atribuído ou por ver todos | `sites.assign` |
| `GET /ad-units` | lista plana (`parent_id` monta a árvore); filtros `network_id`, `site_id`, `status`, `unlinked` | `sites.view` |
| `GET /ad-units/unlinked` | uma página dos ad units sem site (filtro `network_id`); só quem vê todos os sites | `sites.view` |
| `PATCH /ad-units/{id}` | liga a um site à mão (os filhos seguem) ou volta ao automático | `sites.assign` |
| `GET /members/{id}/sites` | sites atribuídos ao membro | `team.view` |
| `PUT /members/{id}/sites` | troca a lista inteira de sites do membro | `sites.assign` |
| `GET /metrics/catalog` | métricas e dimensões que dá para pedir, com os textos em PT, EN e ES (sem as métricas internas da Groone), e as métricas personalizadas da Empresa (`custom_metrics`, com a `query_key` e as fontes) | `reports.view` |
| `GET /custom-metrics` | métricas personalizadas da Empresa, pelo nome, com a chave da consulta (`custom.<chave>`) e as fontes em que cada uma pode ser pedida | `reports.view` |
| `POST /custom-metrics`, `PUT /custom-metrics/{id}`, `DELETE /custom-metrics/{id}` | cadastra, edita ou apaga uma métrica personalizada (fórmula sobre as métricas do catálogo; erro `invalid_formula`; `409 custom_metric_in_use` se outra usa); a chave nasce do nome e não muda | `metrics.manage` |
| `POST /custom-metrics/validate` | confere o formulário como salvar faria, sem gravar: `valid`, `code`, `error` (com a posição) e as variáveis; com `sample` (valores de exemplo das métricas do catálogo; as personalizadas aninhadas são calculadas), devolve em `value` a fórmula calculada no core (vazio sem denominador) | `metrics.manage` |
| `POST /reports/query` | roda uma consulta sem salvar: métricas, período (fixo ou relativo), dimensões, filtros, comparação (`compare`: `none`, `previous`, `last_year` ou `custom` com `compare_start` e `compare_end`; `true`/`false` antigos ainda valem), ordem e limite; `currency` converte o dinheiro pela cotação de cada dia (padrão `USD`; sem cotação, `currency_unavailable`); decimais como texto; só os sites que a pessoa vê; 10 seguidas e depois 1 a cada 2 s (`rate_limited`, com `details.retry_after` e o cabeçalho `Retry-After`); passou de 15 s no banco, `query_too_heavy` | `reports.view` |
| `POST /reports/query/batch` | as consultas de uma tela juntas (`sections`, de 1 a 8, no formato de `/reports/query`); devolve `results` na mesma ordem e gasta uma consulta do limite pela tela inteira | `reports.view` |
| `POST /reports/query/export?locale=` | a mesma consulta em CSV, sites e networks pelo nome, texto que parece fórmula escapado com `'` | `reports.view` |
| `GET /reports`, `GET /reports/{id}` | relatórios salvos que a pessoa vê, em páginas (`page`, o mais recente primeiro, `scope` `mine`/`shared`, `q` no nome, `counts` de cada aba) (os dela, os da Empresa e os dos papéis dela; o privado de outra pessoa é 404), com a consulta, o gráfico, a visibilidade e `editable` | `reports.view` |
| `POST /reports`, `PUT /reports/{id}`, `DELETE /reports/{id}` | salva, edita ou apaga um relatório: nome, descrição, consulta (a de `/reports/query`, sem a moeda), `chart_type` e opções (`stacked`; `metrics` com a cor de cada métrica, `lime`/`cyan`/`magenta`/`violet`/`orange`/`yellow`/`red`, e a aparência `green_red`/`red_green` com `from` < `to`), `visibility` (`private`, `company`, `roles` com `role_ids`); editar e apagar são do dono ou de quem tem `reports.manage` | `reports.manage` para criar |
| `POST /reports/{id}/duplicate` | cópia privada de quem duplica, com " (cópia)" no nome | `reports.manage` |
| `GET /reports/templates`, `POST /reports/templates/{key}` | modelos prontos da Groone (nome em PT, EN e ES) e um relatório privado novo a partir de um deles | `reports.view` / `reports.manage` |
| `GET /dashboards/templates`, `POST /dashboards/templates/{id}`, `POST /dashboards/templates/{id}/widgets/{widget_id}/run`, `POST /dashboards/templates/{id}/run` | modelos prontos de dashboard que a pessoa vê (pelo público da Empresa e pelo papel), um dashboard privado novo a partir de um deles e os widgets do modelo de início | `reports.view` / `dashboards.manage` |
| `POST /dashboards/{id}/run` | roda todos os widgets com consulta do dashboard numa requisição, com os `filters` da tela ou os gravados; devolve `results` e `errors` pelo id do widget (um widget que não roda não derruba os outros) e gasta uma consulta do limite | `reports.view` |
| `POST /reports/{id}/run` | roda o relatório salvo na moeda de visualização de quem roda, só nos sites que a pessoa vê; mesmo limite de taxa de `/reports/query` | `reports.view` |
| `GET /reports/{id}/export?format=csv\|xlsx&locale=` | o relatório salvo em CSV ou XLSX (números como números, texto sempre como texto), personalizadas pelo nome | `reports.view` |
| `GET /currencies` | as moedas do painel, com `available` quando já há cotação | sessão |
| `GET /costs` | uma página (`page`) dos custos da aba Custos, do mês mais novo para o mais antigo | `costs.view` |
| `POST /costs`, `PUT /costs/{id}`, `DELETE /costs/{id}` | cadastra, troca ou apaga um custo: `one_time` (um mês), `recurring` (do início até o fim, se tiver) ou `formula` (sobre `faturamento` e `receita` do mês; erro `invalid_formula`) | `costs.manage` |
| `POST /costs/formula` | confere a fórmula e calcula com valores de exemplo, sem gravar | `costs.view` |
| `GET /rewards?q=&site_id=&deleted=&page=` | uma página dos rewards, o mais novo primeiro, só nos sites que a pessoa vê; `deleted=true` lista só os apagados (as métricas e os contatos continuam) | `rewards.view` |
| `POST /rewards`, `PUT /rewards/{id}`, `PATCH /rewards/{id}` (`{active}`), `DELETE /rewards/{id}`, `PUT /rewards/{id}/icon` | cria, troca, pausa ou ativa, apaga (`deleted_at`) e troca o ícone (imagem crua de até 2 MB); `reward_page_taken` (409) e `reward_ad_unit_day_missing` (422). Cada mudança apaga o cache público da página (`avant:reward:{domínio}/{caminho}`) | `rewards.manage` |
| `GET /rewards/{id}`, `GET /sites/{id}/reward-ad-units`, `GET /rewards/{id}/metrics?from=&to=` | o reward com as perguntas; os ad units de reward do site por data do bloco, com os aparelhos; as métricas do período (padrão: os últimos 30 dias) | `rewards.view` |
| `GET /rewards/{id}/leads?q=&question_id=&answer=&page=`, `GET /rewards/{id}/leads/export`, `DELETE /rewards/{id}/leads/{lead_id}` | contatos (dado pessoal), o mais novo primeiro, o CSV com o mesmo filtro e apagar um contato (os dois últimos na auditoria); continuam à vista depois que o reward é apagado | `rewards.leads` |
| `GET /results?start=&end=&currency=` | faturamento, deduções (parte do cliente), receita, custos e resultado de cada mês, até 24 meses (padrão: os 6 até o atual); `deductions_pending` enquanto o GAM não fecha o mês | `results.view` |
| `PUT /auth/preferences` | troca a moeda de visualização da pessoa (`display_currency`, que também vem em `/auth/me`) | sessão |
| `PATCH /auth/appearance` | tema (`light`, `dark`, `system`), cor (`default`, `blue`, `green`, `purple`, `orange`) e idioma (`pt`, `en`, `es`) da pessoa, também em `/auth/me` | sessão |
| `PUT /auth/me/image`, `DELETE /auth/me/image` | troca ou tira a foto de perfil (corpo é o arquivo PNG, JPEG ou WebP de até 2 MB) | sessão |
| `GET /users/{id}/image` | foto de perfil da própria pessoa ou de alguém da Empresa ativa (`user.image_url` nas respostas) | sessão |
| `GET /events` | avisos em tempo real (SSE) da Empresa ativa, filtrados pela permissão | membro |

Painel interno, em `/api/v1/internal` (Company Groone ativa e 2FA verificado na sessão):

| Rota | Faz | Permissão |
| --- | --- | --- |
| `GET /internal/clients`, `POST /internal/clients` | lista clientes em páginas (`page`, `q`, `status`, `manager` repetível, `sort` = `created_at` ou `name`, `direction` = `asc` ou `desc`; padrão o mais recente primeiro); cadastra o cliente pendente, com contato e indicação, sem mandar e-mail | `internal.clients.view` / `.manage` |
| `POST /internal/clients/{id}/owner-invitation` | envia (ou manda de novo) o convite de dono para o e-mail do cadastro | `internal.clients.manage` |
| `GET /internal/clients/options` | todos os clientes (`id`, `name`, `status`), para seletores e para contar as abas por situação | `internal.clients.view` |
| `GET /internal/clients/{id}`, `/audit` | página de suporte e histórico (em páginas numeradas), só leitura | `internal.clients.view` |
| `GET /internal/clients/{id}/manager-change?user_id=` | o que trocar o responsável para essa pessoa (sem `user_id`: tirar o responsável) faria: prazos que seguem, que param e os sem pessoa que chegam para ela; não muda nada | `internal.clients.view` |
| `GET /internal/views?screen=`, `POST /internal/views`, `PUT`/`DELETE /internal/views/{id}`, `GET /internal/views/catalog/{screen}` | visões salvas das tabelas internas (`clients`, `contracts`, `client_results`, `commissions`, `invoices`): colunas, filtros e ordem, privadas, da Empresa ou de papéis; só o dono edita. O catálogo diz o que cada tela aceita | equipe Groone; a permissão de ver a tela |
| `GET /internal/dashboard-templates`, `POST`, `GET`/`PUT`/`DELETE /{id}`, `PUT /{id}/home`, `GET /roles` | modelos prontos de dashboard: público `groone` ou `clients`, papéis que veem (da equipe Groone ou predefinidos), um modelo de início por público. Mudar um modelo não mexe nos dashboards copiados dele | `internal.dashboard_templates.manage` |
| `PATCH /internal/clients/{id}` | nome, vagas e cadastro (contato e indicação; os fiscais só o cliente muda); cadastro sem `account_manager_id` mantém o responsável, e trocar um responsável que já existia pede `internal.commissions.manage` | `internal.clients.manage` |
| `GET`, `PUT`, `DELETE /internal/clients/{id}/image` | imagem do cliente (ver, trocar, tirar) | `internal.clients.view` / `.manage` |
| `PUT /internal/clients/{id}/status` | situação `active`, `inactive` ou `banned`; as networks acompanham | `internal.clients.manage` |
| `POST /internal/clients/{id}/owner` | troca o dono | `internal.owner.change` |
| `GET /internal/clients/{id}/documents`, `/documents/{kind}/file` | documentos do cliente e download (vai para o histórico do cliente) | `internal.clients.documents` |
| `POST /internal/clients/{id}/documents/{kind}/approve`, `/reject` | aprova o documento em análise ou recusa com `reason`; quem enviou recebe e-mail | `internal.clients.documents` |
| `GET`, `POST /internal/clients/{id}/notes` | observações do cliente (páginas de 10, mais nova primeiro, com autor, quem editou e `editable`) e nova observação | `internal.clients.notes` |
| `PATCH`, `DELETE /internal/clients/{id}/notes/{note_id}` | edita (guarda quem e quando) ou apaga; o autor ou quem tem `internal.clients.notes.manage` | `internal.clients.notes` |
| `GET`, `POST /internal/tasks` | tarefas de suporte (páginas de 10, mudada por último primeiro; filtros `scope` (`mine` ou `all`), `status` repetível, `priority`, `assignee`, `client`, `q`) e nova tarefa (o responsável recebe e-mail) | `internal.tasks.view`; `scope=all` pede `internal.tasks.all` |
| `GET`, `PATCH /internal/tasks/{id}` | tarefa com a linha do tempo; muda situação, prioridade, responsável (`assignee_id: null` tira) ou `data`; quem criou, o responsável ou quem tem `internal.tasks.all` | `internal.tasks.view` |
| `POST /internal/tasks/{id}/comments` | comenta; e-mail para quem criou e para o responsável, menos quem escreveu | `internal.tasks.view` |
| `GET /internal/checklists/months`, `GET /internal/checklists/summary?month=` | meses com checklist de domínio (o atual sempre aparece) e o resumo do mês: sites, feitos e a última conferência | `internal.checklists.view` |
| `GET /internal/checklists?month=` | checklists do mês (páginas de 10, maior faturamento do mês anterior primeiro; filtros `q` e `state` `all`, `pending` ou `done`) | `internal.checklists.view` |
| `GET /internal/checklists/{id}` | checklist do site com os itens ativos (automático, prova e "ok" marcado), as observações e o idioma do cliente | `internal.checklists.view` |
| `PUT /internal/checklists/{id}/items/{item_id}` | marca o item como ok (`{"ok": true}`) ou tira a marcação; só no mês atual (`checklist_not_checkable`) | `internal.checklists.check` |
| `POST /internal/checklists/{id}/check` | pede ao worker uma conferência nova (202); só no mês atual | `internal.checklists.check` |
| `POST /internal/checklists/{id}/notes`, `PATCH`, `DELETE .../notes/{note_id}` | observações (entram no relatório do cliente, no idioma dele); editar e apagar a de outra pessoa pede `internal.checklists.manage` | `internal.checklists.check` |
| `GET`, `POST /internal/checklist-items`, `PUT /internal/checklist-items/{id}`, `POST .../{id}/move` | itens do checklist (uma lista para todos os sites): nome, tipo de conferência, palavras do tipo link, ativo e ordem (`step` -1 ou 1) | ver: `internal.checklists.view`; mudar: `internal.checklists.manage` |
| `GET /internal/gam-tools/networks`, `GET /internal/gam-tools/networks/{id}` | ferramentas do GAM: networks dos clientes (páginas de 10, `q` no nome ou no network code) e a network com os sites e os blocos que o Avant já importou | `internal.gam_tools.view` |
| `GET`, `POST /internal/gam-tools/runs` | execuções da network (`?network=`; sem ele, de todas as networks), a mais recente primeiro, cada uma com a network e o cliente; e nova execução `{network_id, kind, domains, format}` → 202, enfileira `avant.gam.run_tool`; `gam_tool_running` (409) com outra rodando | `internal.gam_tools.view`; `config`, `setup` e `key_values` escrevem no GAM e pedem `internal.gam_tools.run` |
| `/internal/rewards...`, `GET /internal/sites/{id}/reward-ad-units` | as mesmas rotas dos rewards para todos os clientes, cada reward com o `client`; a auditoria vai para o cliente | `internal.rewards.view`, `.manage` e `.leads` |
| `GET /internal/gam-tools/runs/{id}` | execução com os passos; a tela atualiza pelo evento `gam_tool_run.updated` | `internal.gam_tools.view` |
| `GET /internal/gam-tools/ads-txt?network=`, `GET /internal/gam-tools/install?network=&sites=&language=&label=` | linhas do ads.txt e o arquivo de instalação Tag Light (.txt de um site, .zip de vários); `seller_id_missing`, `no_blocks_yet` e `gtag_install_pending` (409) | `internal.gam_tools.view` |
| `GET /internal/owner-invitations`, `POST .../{id}/resend`, `DELETE .../{id}` | convites de dono (a lista em páginas) | `internal.clients.view` / `.manage` |
| `GET /internal/teams?q=&company_id=` | pessoas das equipes das Empresas cliente (sem a equipe Groone), em páginas | `internal.clients.view` |
| `GET /internal/users?q=`, `POST /internal/users/{id}/disable`, `/enable`, `/reset-mfa` | pessoas (a busca em páginas, a mais recente primeiro) | `internal.users.manage` |
| `GET /internal/staff`, `POST /internal/staff/invitations` | equipe Groone (em páginas); o convite só com papel cujas permissões quem convida tem | `internal.staff.manage` |
| `GET /internal/staff/options` | a equipe Groone inteira (sem os removidos), para os seletores, como o responsável do cliente | `internal.clients.view`, `internal.commissions.view` ou `.manage` |
| `GET /internal/networks/unassigned`, `POST .../{id}/assign` | MCM sem dono, em páginas: a Groone escolhe a Empresa | `internal.networks.assign` |
| `GET /internal/results?start=&end=&currency=` | o resultado de cada Empresa cliente no período, em páginas, do maior resultado para o menor | `internal.results.view` |
| `GET /internal/goal-templates`, `POST`, `PUT /{id}`, `DELETE /{id}` | modelos de meta da equipe Groone (a lista em páginas; `/options` traz todos): nome, ano e 12 valores em dólar; `is_company_goal` marca a meta da Groone (uma por ano, senão `409 company_goal_taken`) | ver: quem edita ou vê as metas; editar: `internal.commissions.manage` |
| `GET /internal/roles/{id}/commission-rules`, `POST`, `PUT /{rule_id}`; `DELETE /internal/commission-rules/{rule_id}` | regras de comissão do papel da equipe Groone, uma por evento (`client_created`, `client_reactivated`, `network_created`, `network_reactivated`, `site_created`, `site_reactivated`): percentual, dias de espera, dias recebendo (vazio: sem prazo) e, só nos de cliente, o papel de destino; repetido dá `409 commission_rule_taken`; o evento não muda na edição | ver: `internal.commissions.view` ou `.manage`; editar: `internal.commissions.manage` |
| `GET /internal/commissions/settings`, `PUT` | data de início da comissão no Avant (o dia seguinte ao último pago pelo Genius); gravar abre os prazos de cadastro do que já existia e apaga os rascunhos anteriores; depois do primeiro mês fechado dá `409 commission_start_locked` | ver: `internal.commissions.view` ou `.manage`; gravar: `internal.commissions.manage` |
| `GET /internal/commissions/me?month=` | minha comissão: prazos com o alvo e o fim, o mês (base, comissão, dedução, descontos, total, situação) e o histórico | equipe Groone |
| `GET /internal/commissions?month=`, `GET /internal/commissions/people/{user_id}?month=` | a comissão de cada pessoa no mês e o detalhe por prazo (a própria pessoa vê o dela); mês de 2000 a 2099 | `internal.commissions.view` ou `.manage` |
| `POST /internal/commissions/people/{user_id}/issue`, `/adjustments` | marca o mês fechado como emitido (422 se ainda não fechou); desconto com valor e motivo no mês ainda não emitido | `internal.commissions.manage` |
| `GET /internal/role-goals`, `PUT /internal/roles/{id}/goal` | a meta de cada papel da equipe Groone (`goal_template_id` vazio tira), `per_member` ou `split` | ver: quem edita ou vê as metas; editar: `internal.commissions.manage` |
| `GET /internal/goals?month=AAAA-MM` | a meta da Groone e a de cada pessoa no mês: realizado (receita da Groone dos clientes, menos a parte dela nas deduções fechadas), meta, fração, ritmo e projeção | `internal.commissions.view` |
| `GET /internal/goals/me?month=AAAA-MM` | a meta do mês de quem pergunta | qualquer pessoa da equipe Groone |
| `GET /internal/contracts`, `GET .../{id}` | contratos em páginas, com filtros `company_id`, `network_id` e `status` | `internal.contracts.view` |
| `GET /internal/contracts/networks` | networks MCM com o contrato ativo e se aceitam contrato à mão | `internal.contracts.view` |
| `POST /internal/contracts` | contrato à mão (só MCM Manage Inventory; encerra o ativo) | `internal.contracts.create` |
| `PATCH /internal/contracts/{id}`, `POST .../{id}/end` | observação e encerramento (o revshare nunca muda) | `internal.contracts.update` |
| `DELETE /internal/contracts/{id}` | exclui contrato feito à mão | `internal.contracts.delete` |

## Estrutura

Organizado por domínio (objeto → arquivos), com a regra de negócio no avant-core:

```
src/avant_api/
  main.py              monta a aplicação e inclui o router de cada domínio
  app/                 infraestrutura: settings, container (Services), security
                       (autenticação e permissões), cookies, errors, middleware,
                       logs, limits, events, tasks, google e ports
  shared/              DTOs usados por mais de um domínio (dto.py) e leitura do pedido (http.py)
  modules/<recurso>/    um módulo por recurso (members, roles, networks, google...), com
    controller.py      um só: as rotas do recurso, só HTTP (validação, status, cookies,
                       redirecionamento)
    dto.py             um só: modelos Pydantic de entrada e saída (sem DTO, não tem o arquivo)
    service.py         um só: chama os casos de uso do avant-core e devolve os DTOs
    dependencies.py    um só: monta o service com os adaptadores do container
    <assunto>.py       apoio só deste módulo, com o nome do assunto (google/redirects.py,
                       reports/export.py, results/period.py); nunca um segundo controller
                       ou service: recurso novo é módulo novo
  modules/internal/    painel interno, um subdomínio por assunto (clients, people,
                       staff, mcm, results, contracts), cada um com os mesmos arquivos, e
                       router.py que junta todos
```

- **Model e repository** ficam no avant-core, organizado por domínio: entidades em
  `<domínio>/models/`, interfaces em `<domínio>/interfaces/`, implementação SQL em
  `<domínio>/repositories/` e casos de uso em `<domínio>/services/`. A API e o worker usam
  os mesmos.
- **Inversão de dependência**: o service recebe interfaces (`app/ports.UnitOfWorkFactory`,
  `Clock`, `Mailer`, `TaskQueue`...) pelo construtor, nunca o container. Só o
  `dependencies.py` conhece o `Services`; nos testes, dá para montar o service com fakes.
- O controller não chama caso de uso nem abre Unit of Work: fala só com o service.

## Como funciona

- **Sessão**: cookie `__Host-avant_session` (`httpOnly`, `SameSite=Lax`, `Secure`), igual
  em todo ambiente. Chrome e Firefox aceitam `Secure` em `http://localhost`; para os outros
  navegadores, o HTTPS local vem do avant-infra. O banco guarda só o hash.
- **CSRF**: no login, a API grava também o cookie `__Host-avant_csrf`, que o Vue lê e manda no
  cabeçalho `X-CSRF-Token` em todo POST, PATCH, PUT e DELETE.
- **Empresa ativa**: vem da sessão, nunca da URL. Cada rota abre o Unit of Work do
  avant-core com essa Empresa, e o RLS do Postgres garante o isolamento.
- **2FA**: com o 2FA ligado, o login responde `{"mfa_required": true}` e o cookie leva
  só uma pré-sessão de 5 minutos. A equipe Groone sem 2FA recebe `mfa_required` (403) em
  tudo menos `/auth/me`, `/auth/logout` e `/auth/mfa/*`. O segredo é cifrado com
  `MFA_ENCRYPTION_KEY`.
- **E-mail**: os convites saem pelo Resend (`RESEND_API_KEY`, remetente em `MAIL_FROM`), em
  português, inglês ou espanhol conforme o idioma da pessoa. A chave é obrigatória em todo
  ambiente (sem ela a API não sobe) e nenhum e-mail nem link com token vai para o log. Em
  desenvolvimento, use uma chave de teste do Resend ou um destino escolhido de propósito. Falha no envio vai para o log e para `avant_mail_failures_total`,
  e o convite continua pendente: o core levanta `MailNotSent` e as rotas de convite (equipe,
  reenvio, convite de dono, reenvio do convite de dono e equipe Groone) respondem 503
  `invitation_mail_not_sent`, "O convite foi salvo, mas o e-mail não saiu. Tente reenviar."
- **Banco**: o engine sai do `new_engine` do core com `EngineSettings` (`application_name`
  `avant-api`), lidas de `DB_POOL_SIZE`, `DB_MAX_OVERFLOW`, `DB_POOL_TIMEOUT_SECONDS`,
  `DB_POOL_RECYCLE_SECONDS`, `DB_STATEMENT_TIMEOUT_MS`, `DB_IDLE_IN_TRANSACTION_TIMEOUT_MS` e
  `DB_LOCK_TIMEOUT_MS`, com os mesmos padrões em todo ambiente; zero ou acima dos tetos do core,
  a API não sobe. Na subida, `ensure_app_role_is_restricted` recusa o papel que ignora o RLS
  (superusuário, `BYPASSRLS` ou dono de tabela). As respostas em streaming (SSE e downloads) não
  seguram conexão do pool, e `tests/test_database.py` confere a conta das conexões
  (`check_connection_budget`) com os números padrão.
- **Limite de tentativas**: 5 senhas erradas por e-mail e 20 por IP em 15 minutos no
  login; 20 pedidos por IP em 15 minutos em `/auth/password/*`. Passou, 429
  `too_many_attempts` com `Retry-After`. Os contadores ficam no Redis (`REDIS_URL`), em
  todo ambiente: sem `REDIS_URL` ou sem `CELERY_BROKER_URL` a API não sobe, para nenhum
  limite valer só em staging e produção. O `Services` não tem fake por padrão: os testes montam
  os fakes em memória (`tests/fakes.py`) na fábrica `memory_services` do `tests/conftest.py`.
- **Esqueci a senha**: a rota só normaliza o e-mail e agenda
  `avant.mail.request_password_reset(email)` na fila `mail` (`queue_password_reset` do
  core, adaptador `TaskMailQueue`), sem ler o banco nem mandar e-mail, para o tempo de
  resposta não dizer se a conta existe. O worker gera o link e manda o e-mail; o token não
  passa pela fila; o e-mail vai mascarado (`argsrepr="('***',)"`) no cabeçalho da mensagem e no
  evento `task-sent`. Com o RabbitMQ fora do ar, 503 `queue_unavailable` para qualquer e-mail.
- **Google**: OpenID Connect com PKCE, tratado aqui (`GOOGLE_OAUTH_CLIENT_ID` e
  `GOOGLE_OAUTH_CLIENT_SECRET`; URI de redirecionamento
  `{APP_BASE_URL}/api/v1/auth/google/callback`). Só entra com Google quem ligou a conta
  em Configurações. O callback sempre redireciona para o painel: `/` ou `/entrar/2fa`
  quando deu certo, `/entrar?erro=<code>` ou `/configuracoes/conta?erro=<code>` quando
  não.
- **Avisos por e-mail**: senha trocada, Google ligado e 2FA zerado pela Groone. Os
  e-mails vêm de `avant_core.mail`, o mesmo módulo do worker.
- **GAM**: a API não fala com o Ad Manager. Conectar, "sincronizar agora" e atribuir uma
  network MCM gravam o pedido e enfileiram `avant.gam.sync_network` no RabbitMQ
  (`CELERY_BROKER_URL`, obrigatória em todo ambiente) depois do commit. Se o
  RabbitMQ não responder, a rota não falha: o erro vai para o log e o agendador do worker
  passa pela network no ciclo seguinte. O guia mostra `GAM_SERVICE_ACCOUNT_EMAIL`.
- **Tempo real**: `GET /events` é um `text/event-stream`. O worker publica
  `{"type", "data"}` no canal Redis `avant:events:{company_id}` e qualquer instância da
  API repassa; cada tipo de evento exige uma permissão (`app/events.PERMISSION_FOR`) e o que
  não está no mapa não sai. Heartbeat a cada 15 s; depois de 30 minutos a API fecha e o
  EventSource reconecta, conferindo a sessão de novo. O proxy precisa de
  `proxy_buffering off` nessa rota (a resposta também manda `X-Accel-Buffering: no`).
  Eventos de agora: `network.updated` (`network.view`), com `network_id`.
- **Chaves de API**: `Authorization: Bearer avk_...` vale nas rotas de Empresa, sem CSRF,
  com as permissões da chave que o membro ainda tem. Login, 2FA, conta, sessões, criar
  chave, sair da Empresa e o painel interno são só pela sessão. Cada chave tem um balde de
  2 requisições por segundo com rajada de 20 (`X-RateLimit-Limit` e
  `X-RateLimit-Remaining`); passou, 429 `rate_limited` com `Retry-After`, e mais de 20
  recusas em um minuto bloqueiam a chave por 30 s. O balde fica no Redis. Chave que não
  confere conta por IP: 20 em 15 minutos e o IP leva 429 `too_many_attempts` antes de a
  chave chegar ao banco. Só a falha conta (o limite confere antes da consulta e soma depois
  do `not_authenticated`), então uma chave válida nunca ocupa vaga do limite do IP; em
  rajada, chaves erradas em paralelo podem passar um pouco das 20 antes do bloqueio.
- **Reward no site** (`modules/reward_public/`, fora de `/api/v1`, sem sessão): o script
  `reward.js` lê `GET /api/reward/v2?url=` (a configuração da página, com o `id` de cada
  pergunta, guardada no Redis em `avant:reward:{domínio}/{caminho}` por 1 hora, ou 5 minutos
  quando a página não tem reward), `GET /api/reward/icon/{id}` (o ícone, com cache longo),
  `POST /api/reward/events` (até 20 eventos; a resposta leva `question_id`) e
  `POST /api/reward/leads` (o contato com `answers: [{question_id, answer}]`). Os dois POST
  aceitam outro site e qualquer `Content-Type` (`sendBeacon`), têm limite por IP e só gravam
  na lista `avant:reward:buffer`, que o worker esvazia a cada minuto; o dia do evento é o de
  São Paulo. Salvar, pausar ou apagar um reward apaga a chave da página.
- **Permissão**: declarada na rota com `Depends(require("team.invite"))`.
- **Erros**: sempre `{"error": {"code", "message", "details"}}`; o mapa de código para
  status HTTP está em `app/errors.py`.
- **Logs**: JSON em uma linha por requisição, com `request_id` (também no cabeçalho
  `X-Request-Id`). Erro inesperado sai com o stack trace. O log de acesso leva a rota com
  `{token}`, nunca o valor, e o log de erro mascara o token do convite no caminho
  (`/auth/invitations/***`). A chave de API e os cookies nunca vão para o log.
- **Cabeçalhos**: toda resposta leva `X-Content-Type-Options: nosniff`,
  `X-Frame-Options: DENY`, `Referrer-Policy: no-referrer` e
  `Content-Security-Policy: default-src 'none'; frame-ancestors 'none'`. A página do Swagger
  (`/api/docs`), quando é entregue, leva uma política própria (`DOCS_CONTENT_SECURITY_POLICY` em
  `app/middleware.py`): `script-src 'self'`, `connect-src 'self'`, `frame-ancestors 'none'` e
  nenhum script inline. O Swagger UI não vem de CDN: o `swagger-ui-dist` 5.34.0 está copiado em
  `modules/api_docs/swagger_ui/` (conferido pelo `integrity` do npm ao copiar) e sai por
  `/api/docs/assets/{arquivo}`, com o SHA-256 de cada arquivo conferido na subida
  (`swagger_assets.py`; arquivo alterado, a API não sobe) e `integrity` (SRI) na página. Para
  atualizar, troque os arquivos e os SHA-256 juntos. O Swagger, os arquivos dele e o
  `/api/v1/openapi.json` (que lista também as rotas internas) têm a mesma regra em todo
  ambiente: só a sessão da equipe Groone, com a Company Groone ativa e o 2FA verificado;
  quem não é recebe o erro de sempre (401, `staff_only` ou `mfa_required`), com a política.
- **Proxy**: o uvicorn só aceita `X-Forwarded-For` de `FORWARDED_ALLOW_IPS` (endereços ou redes
  do nginx do compose, separados por vírgula). A variável é obrigatória em todo ambiente e não
  aceita `*`: o IP do cliente sustenta os limites por IP. Sem ela, a API não sobe. No
  desenvolvimento, sem proxy na frente, use `127.0.0.1`.

## Desenvolvimento

Para subir o Avant inteiro na máquina (banco, API, worker e painel), siga o [guia de desenvolvimento](https://github.com/PedroH3nri/avant-infra/blob/develop/docs/desenvolvimento.md) do avant-infra.

```bash
uv sync
uv run ruff format . && uv run ruff check . && uv run mypy
export AVANT_TEST_MIGRATIONS_URL=postgresql+psycopg://avant_owner:SENHA@localhost:5432/avant_test
export AVANT_TEST_DATABASE_URL=postgresql+psycopg://avant_app:SENHA@localhost:5432/avant_test
export AVANT_TEST_REDIS_URL=redis://localhost:6379/0  # opcional: testa o contador no Redis
uv run pytest
```

Os testes recriam o schema do banco de testes com as migrations do avant-core.

A CI (`.github/workflows/ci.yml`) roda tudo isso em todo PR, com um Postgres 16 e um
Redis 7. Para
baixar o avant-core, que é privado, ela usa o secret `AVANT_CORE_ACCESS`: um token
*fine-grained* só com leitura do avant-core.

Para rodar a API, com o compose do avant-infra no ar:

```bash
DATABASE_URL=postgresql+psycopg://avant_app:SENHA@localhost:5432/avant \
REDIS_URL=redis://localhost:6379/0 CELERY_BROKER_URL=amqp://USUARIO:SENHA@localhost:5672// \
  uv run uvicorn avant_api.main:create_app --factory --reload
```

## Imagem

```bash
docker build --secret id=github_token,env=GITHUB_TOKEN -t ghcr.io/pedroh3nri/avant-api .
```

O token só precisa ler o avant-core e não fica na imagem.
