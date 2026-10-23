# avant-api

API FastAPI do Groone Avant. Leia o README antes de mudar algo.

- Regra de negócio fica no avant-core. Rota aqui só valida a entrada, chama um caso de uso
  e formata a saída. Se faltar um caso de uso, ele entra no avant-core primeiro.
- Rotas em inglês, em `/api/v1`, sem `company_id` no caminho: a Empresa vem da sessão.
- Toda rota de Empresa usa `Depends(require("permissao"))` e `services.uow(actor.company_id)`.
  `trusted_uow()` (sem RLS) só para login, sessão e aceite de convite.
- Erro novo do domínio: um `code` em `errors.STATUS`. Nunca devolver erro fora do formato
  `{"error": {...}}`.
- Rota nova: teste em `tests/` contra o Postgres, incluindo o caso sem permissão.
- Antes de abrir PR: `uv run ruff format . && uv run ruff check . && uv run mypy && uv run pytest`.
- Nada de segredos no repositório. Mensagens e comentários em português.
- PRs vão para `develop`.

## Contexto, issues e skills

- Comece por `docs/contexto.md`: produto, decisões, estado dos cinco repositórios e onde está cada coisa. Decisões antigas em `docs/decisoes/`.
- Todo trabalho parte de uma issue com milestone neste repositório (`gh issue list --milestone ...`). Pedido sem issue vira issue antes.
- Skills em `docs/skills/` (índice em `docs/skills/README.md`); `.claude/skills` aponta para lá. Comece pela `avant-fluxo-de-trabalho`.
- Grafo do código em `graphify-out/` (comece pelo `GRAPH_REPORT.md`, ou `graphify query "..."`). Mudou código: `graphify update .` e commite o grafo no mesmo PR.
