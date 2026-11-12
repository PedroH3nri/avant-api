"""Request id, log de acesso em JSON e métricas do Prometheus."""

import logging
import time
import uuid
from collections.abc import Awaitable, Callable

from fastapi import Request, Response
from prometheus_client import Counter, Histogram
from starlette.routing import Match

log = logging.getLogger("avant.access")

REQUESTS = Counter("avant_http_requests_total", "Requisições HTTP", ["method", "route", "status"])
LATENCY = Histogram(
    "avant_http_request_duration_seconds", "Duração das requisições HTTP", ["method", "route"]
)


def _route_template(request: Request) -> str:
    """O caminho com {id} no lugar dos valores, para as métricas não explodirem."""
    for route in request.app.router.routes:
        match, _ = route.matches(request.scope)
        if match is Match.FULL:
            return str(getattr(route, "path", request.url.path))
    return "unmatched"


# Em toda resposta da API: sem adivinhar o tipo, sem moldura e sem Referer para fora.
SECURITY_HEADERS = {
    "X-Content-Type-Options": "nosniff",
    "X-Frame-Options": "DENY",
    "Referrer-Policy": "no-referrer",
}
# A API só devolve JSON e arquivos para baixar: nada carrega, nada emoldura.
CONTENT_SECURITY_POLICY = "default-src 'none'; frame-ancestors 'none'"
SWAGGER_PAGE = "/api/docs"
SWAGGER_ASSETS = "/api/docs/assets"
# A página do Swagger, só para a equipe Groone com 2FA: scripts e CSS só da própria API (nenhum
# inline nem de CDN), o OpenAPI pela mesma origem e nada de moldura. O estilo inline fica
# liberado porque o Swagger UI posiciona alguns elementos pelo atributo ``style``.
DOCS_CONTENT_SECURITY_POLICY = (
    "default-src 'none'; script-src 'self'; style-src 'self' 'unsafe-inline'; "
    "img-src 'self' data:; connect-src 'self'; base-uri 'none'; form-action 'none'; "
    "frame-ancestors 'none'"
)


def _content_security_policy(request: Request, response: Response) -> str:
    """A política da página do Swagger quando ela abre; a recusa (sem sessão da equipe) e todo
    o resto levam a política da API."""
    if request.url.path == SWAGGER_PAGE and response.status_code == 200:
        return DOCS_CONTENT_SECURITY_POLICY
    return CONTENT_SECURITY_POLICY


async def observe(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    """Dá um id ao pedido, mede a duração e registra métricas e log."""
    request_id = request.headers.get("X-Request-Id") or uuid.uuid4().hex
    request.state.request_id = request_id
    start = time.perf_counter()
    response = await call_next(request)
    elapsed = time.perf_counter() - start
    route = _route_template(request)
    REQUESTS.labels(request.method, route, str(response.status_code)).inc()
    LATENCY.labels(request.method, route).observe(elapsed)
    response.headers["X-Request-Id"] = request_id
    response.headers.update(SECURITY_HEADERS)
    response.headers["Content-Security-Policy"] = _content_security_policy(request, response)
    # Chaves de API: a dependência deixa o estado do balde para o cabeçalho.
    for name, value in getattr(request.state, "rate_limit", {}).items():
        response.headers[name] = value
    if route != "/api/v1/metrics":
        log.info(
            "request",
            extra={
                "request_id": request_id,
                "method": request.method,
                "route": route,
                "status": response.status_code,
                "ms": round(elapsed * 1000, 1),
            },
        )
    return response
