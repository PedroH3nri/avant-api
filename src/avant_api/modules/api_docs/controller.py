"""Swagger (``/api/docs``) e OpenAPI (``/api/v1/openapi.json``), com a mesma regra em todo
ambiente: só a sessão da equipe Groone, com a Company Groone ativa e o 2FA verificado. O
OpenAPI lista também as rotas internas, por isso nunca fica aberto."""

from typing import Any

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Request
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import HTMLResponse

from avant_api.app.middleware import SWAGGER_PAGE
from avant_api.app.security import require_staff_member

OPENAPI_PATH = "/api/v1/openapi.json"

router = APIRouter(tags=["docs"], include_in_schema=False)


@router.get(SWAGGER_PAGE)
def swagger(_: Actor = Depends(require_staff_member)) -> HTMLResponse:
    """A página do Swagger, que lê o OpenAPI com o mesmo cookie da sessão."""
    return get_swagger_ui_html(openapi_url=OPENAPI_PATH, title="Groone Avant API")


@router.get(OPENAPI_PATH)
def openapi(request: Request, _: Actor = Depends(require_staff_member)) -> dict[str, Any]:
    """O esquema OpenAPI da API inteira."""
    schema: dict[str, Any] = request.app.openapi()
    return schema
