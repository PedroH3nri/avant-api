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
