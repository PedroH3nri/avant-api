---
name: avant-nova-rota
description: Use ao criar ou mudar uma rota no avant-api (validação, permissão, caso de uso, formato de saída e testes).
---

# Rota nova no avant-api

A rota só valida a entrada, chama um caso de uso do avant-core e formata a saída. Se o caso de uso não existe, ele entra no avant-core primeiro (e a API sobe a versão do core).

Cada recurso fica em `src/avant_api/modules/<recurso>/` (veja "Estrutura" no README), com um
de cada: `controller.py` (rotas, só HTTP), `dto.py` (Pydantic), `service.py` (classe que recebe
as interfaces pelo construtor e chama o caso de uso) e `dependencies.py` (monta o service a
partir do `Services`). Recurso novo é módulo novo: crie a pasta com os arquivos e inclua o
router em `main.py`; nunca um segundo controller ou service num módulo. Apoio só do módulo vai
num arquivo com o nome do assunto (`csv_export.py`). DTO usado por mais de um módulo vai para
`shared/dto.py`. Os imports do core vêm do domínio dele (`avant_core.<domínio>.services`,
`.models`, `.errors`).

1. **Caminho** em inglês, em `/api/v1`, sem `company_id`: a Empresa ativa vem da sessão.
2. **Permissão**: `Depends(require("permissao"))` no controller e, no service, `self._uows.uow(actor.company_id)`. `trusted_uow()` (sem RLS) só para login, sessão e aceite de convite. Rotas só por sessão (conta, chaves, painel interno) usam `get_session_actor`/`require_session`.
3. **DTOs** no `dto.py` do domínio (Pydantic). Mudou o formato? O `src/lib/types.ts` do avant-web precisa acompanhar.
4. **Erros**: código novo do domínio em `errors.STATUS`. Sempre `{"error": {"code", "message", "details"}}`.
5. **Tarefas**: o que precisa do worker vai por `send_task("avant.<fila>.<nome>")` depois do commit.
6. **Testes** em `tests/` contra o Postgres: caminho feliz, sem permissão (403), outra Empresa (404) e, se houver, pessoa que só vê os sites atribuídos.
7. Atualize a tabela de rotas do README.
8. Checagens: `uv run ruff format . && uv run ruff check . && uv run mypy && uv run pytest`. Sem Postgres local, os testes de integração rodam no CI.
