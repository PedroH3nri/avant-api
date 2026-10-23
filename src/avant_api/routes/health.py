"""Saúde do processo, para o blue-green do Jenkins e o Prometheus."""

from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest
from sqlalchemy import text

from avant_api.deps import get_services
from avant_api.services import Services

router = APIRouter(tags=["ops"])


@router.get("/health")
def health() -> dict[str, str]:
    """O processo está de pé."""
    return {"status": "ok"}


@router.get("/ready", response_model=None)
def ready(services: Services = Depends(get_services)) -> JSONResponse | dict[str, object]:
    """As dependências respondem. Redis e RabbitMQ entram quando a API passar a usá-los."""
    checks: dict[str, str] = {}
    try:
        with services.engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        checks["database"] = "ok"
    except Exception as exc:
        checks["database"] = type(exc).__name__
    if any(v != "ok" for v in checks.values()):
        return JSONResponse({"status": "unavailable", "checks": checks}, status_code=503)
    return {"status": "ok", "checks": checks}


@router.get("/metrics", include_in_schema=False)
def metrics() -> Response:
    """Bloqueado no nginx: só a rede interna das VMs chega aqui."""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
