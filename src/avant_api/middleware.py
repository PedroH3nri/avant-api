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


async def observe(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    request_id = request.headers.get("X-Request-Id") or uuid.uuid4().hex
    request.state.request_id = request_id
    start = time.perf_counter()
    response = await call_next(request)
    elapsed = time.perf_counter() - start
    route = _route_template(request)
    REQUESTS.labels(request.method, route, str(response.status_code)).inc()
    LATENCY.labels(request.method, route).observe(elapsed)
    response.headers["X-Request-Id"] = request_id
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
