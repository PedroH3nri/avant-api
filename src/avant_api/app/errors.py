"""Corpo de erro do contrato: {"error": {"code", "message", "details"}}.

O frontend traduz pelo code; a mensagem é só para quem lê o log ou a API.
"""

import logging
from typing import Any

import redis
from avant_core.shared.errors import DomainError
from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException

log = logging.getLogger("avant.api")


class CsrfFailed(DomainError):
    code = "csrf_failed"


class NoActiveCompany(DomainError):
    code = "no_active_company"


class CompanyChanged(DomainError):
    """A aba fala de uma Empresa, mas a sessão já está em outra (trocada em outra aba)."""

    code = "company_changed"


class TooManyAttempts(DomainError):
    """Passou do limite de tentativas; o cabeçalho Retry-After diz quando tentar de novo."""

    code = "too_many_attempts"

    def __init__(self, message: str = "muitas tentativas", *, retry_after: int) -> None:
        super().__init__(message)
        self.retry_after = retry_after


class ExportsBusy(DomainError):
    """As exportações do processo estão todas ocupadas; o Retry-After diz quando tentar."""

    code = "exports_busy"

    def __init__(self, *, retry_after: int) -> None:
        super().__init__("muitas exportações ao mesmo tempo, tente de novo em instantes")
        self.retry_after = retry_after


class QueueUnavailable(DomainError):
    """A fila do worker está fora do ar; o Retry-After diz quando tentar de novo."""

    code = "queue_unavailable"

    def __init__(self, *, retry_after: int) -> None:
        super().__init__("a fila de tarefas está fora do ar, tente de novo em instantes")
        self.retry_after = retry_after


class RateLimited(DomainError):
    """A chave de API passou do limite de requisições."""

    code = "rate_limited"

    def __init__(self, message: str = "limite de requisições", *, retry_after: int) -> None:
        super().__init__(message)
        self.retry_after = retry_after


class QueryTooHeavy(DomainError):
    """A consulta passou do tempo máximo no banco."""

    code = "query_too_heavy"


class GoogleUnavailable(DomainError):
    code = "google_unavailable"


class GoogleFailed(DomainError):
    """O Google recusou o código ou devolveu um id_token que não confere."""

    code = "google_failed"


STATUS: dict[str, int] = {
    "exports_busy": 503,
    "queue_unavailable": 503,
    "not_authenticated": 401,
    "mfa_attempts_exceeded": 401,
    "mfa_locked": 429,
    "mfa_required": 403,
    "mfa_already_enabled": 409,
    "mfa_not_enabled": 409,
    "invalid_mfa_code": 422,
    "invalid_credentials": 401,
    "permission_denied": 403,
    "account_disabled": 403,
    "csrf_failed": 403,
    "no_active_company": 403,
    "company_changed": 409,
    "staff_only": 403,
    "seat_limit_below_usage": 409,
    "client_contact_taken": 409,
    "client_not_pending": 409,
    "commission_rule_taken": 409,
    "commission_start_locked": 409,
    "client_without_owner": 409,
    "not_found": 404,
    "seat_limit_reached": 409,
    "already_member": 409,
    "invitation_not_pending": 409,
    "invitation_expired": 409,
    "invitation_email_mismatch": 409,
    "cannot_change_owner": 409,
    "cannot_change_self": 409,
    "role_in_use": 409,
    "role_not_editable": 409,
    "group_needs_member": 409,
    "group_name_taken": 409,
    "member_in_other_group": 409,
    "invalid_input": 422,
    "invalid_image": 422,
    "image_too_large": 413,
    "invalid_document": 422,
    "document_too_large": 413,
    "checklist_not_checkable": 409,
    "gam_tool_running": 409,
    "seller_id_missing": 409,
    "gtag_install_pending": 409,
    "no_blocks_yet": 409,
    "documents_not_required": 409,
    "document_not_reviewable": 409,
    "document_already_approved": 409,
    "invalid_formula": 422,
    "custom_metric_in_use": 409,
    "company_goal_taken": 409,
    "unsupported_currency": 422,
    "currency_unavailable": 409,
    "wrong_invitation_kind": 422,
    "invalid_permission": 422,
    "weak_password": 422,
    "too_many_attempts": 429,
    "invalid_token": 422,
    "google_unavailable": 503,
    "google_failed": 502,
    "google_not_linked": 403,
    "no_access": 403,
    "email_not_verified": 403,
    "google_email_mismatch": 409,
    "google_already_linked": 409,
    "network_code_taken": 409,
    "network_disconnected": 409,
    "site_exists": 409,
    "reward_page_taken": 409,
    "reward_ad_unit_day_missing": 422,
    "site_from_gam": 409,
    "sync_too_soon": 429,
    "rate_limited": 429,
    "api_key_limit_reached": 409,
    "query_too_heavy": 422,
    "contract_not_manual": 409,
    "contract_ended": 409,
    "invoice_exists": 409,
    "commission_not_validated": 409,
    "invoice_not_draft": 409,
    "invoice_not_issued": 409,
    "item_locked": 409,
    "payee_details_missing": 409,
    "invoice_service_taken": 409,
}


def error_body(code: str, message: str, details: dict[str, Any] | None = None) -> dict[str, Any]:
    """Monta o corpo de erro no formato ``{"error": {...}}``."""
    return {"error": {"code": code, "message": message, "details": details or {}}}


def install(app: FastAPI) -> None:
    """Registra na aplicação os tratadores que devolvem erros no formato da API."""

    @app.exception_handler(DomainError)
    async def domain_error(_: Request, exc: DomainError) -> JSONResponse:
        """Traduz um erro do domínio para o status e o código da API."""
        # TooManyAttempts, SyncTooSoon, RateLimited.
        retry_after = getattr(exc, "retry_after", None)
        headers = {"Retry-After": str(retry_after)} if retry_after is not None else None
        details = {"retry_after": retry_after} if retry_after is not None else None
        return JSONResponse(
            error_body(exc.code, str(exc), details),
            status_code=STATUS.get(exc.code, 400),
            headers=headers,
        )

    @app.exception_handler(RequestValidationError)
    async def validation_error(_: Request, exc: RequestValidationError) -> JSONResponse:
        """Devolve 422 com os campos que não passaram na validação."""
        fields = [
            {"loc": list(error_item["loc"]), "type": error_item["type"], "msg": error_item["msg"]}
            for error_item in exc.errors()
        ]
        return JSONResponse(
            error_body("validation_error", "dados inválidos", {"fields": fields}),
            status_code=422,
        )

    @app.exception_handler(HTTPException)
    async def http_error(_: Request, exc: HTTPException) -> JSONResponse:
        """Devolve 404, 405 e outros erros HTTP no formato da API."""
        code = {404: "not_found", 405: "method_not_allowed"}.get(exc.status_code, "http_error")
        return JSONResponse(error_body(code, str(exc.detail)), status_code=exc.status_code)

    @app.exception_handler(redis.RedisError)
    async def redis_unavailable(request: Request, exc: redis.RedisError) -> JSONResponse:
        """Redis fora do ar (limites, chaves de API, relatórios): 503 para tentar de novo."""
        log.warning(
            "redis indisponível",
            extra={"path": request.url.path, "error": type(exc).__name__},
        )
        return JSONResponse(
            error_body("service_unavailable", "serviço indisponível, tente de novo"),
            status_code=503,
            headers={"Retry-After": "5"},
        )

    @app.exception_handler(Exception)
    async def unexpected(request: Request, exc: Exception) -> JSONResponse:
        """Registra o erro inesperado no log e devolve 500 sem detalhes."""
        log.error(
            "erro inesperado",
            exc_info=exc,
            extra={
                "path": request.url.path,
                "request_id": getattr(request.state, "request_id", None),
            },
        )
        return JSONResponse(error_body("internal_error", "erro interno"), status_code=500)
