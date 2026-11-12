"""Swagger (``/api/docs``) e OpenAPI (``/api/v1/openapi.json``), com a mesma regra em todo
ambiente: só a sessão da equipe Groone, com a Company Groone ativa e o 2FA verificado. O
OpenAPI lista também as rotas internas, por isso nunca fica aberto. Os arquivos do Swagger UI
saem da própria API, conferidos na subida, e a página tem CSP própria (``app/middleware``)."""

from html import escape
from typing import Any

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import HTMLResponse, Response

from avant_api.app.middleware import SWAGGER_ASSETS, SWAGGER_PAGE
from avant_api.app.security import require_staff_member
from avant_api.modules.api_docs.swagger_assets import (
    BUNDLE,
    INITIALIZER,
    STYLESHEET,
    load_assets,
)

OPENAPI_PATH = "/api/v1/openapi.json"
ASSETS = load_assets()
ASSET_CACHE = "private, no-cache"

router = APIRouter(tags=["docs"], include_in_schema=False)


def _swagger_page() -> str:
    """O HTML da página: só arquivos da própria API, com ``integrity``, e nenhum script inline."""
    stylesheet, bundle, initializer = (ASSETS[name] for name in (STYLESHEET, BUNDLE, INITIALIZER))
    return f"""<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>Groone Avant API</title>
<link rel="stylesheet" href="{SWAGGER_ASSETS}/{STYLESHEET}"
 integrity="{escape(stylesheet.integrity)}">
</head>
<body>
<div id="swagger-ui"></div>
<script src="{SWAGGER_ASSETS}/{BUNDLE}" integrity="{escape(bundle.integrity)}"></script>
<script src="{SWAGGER_ASSETS}/{INITIALIZER}" integrity="{escape(initializer.integrity)}"></script>
</body>
</html>
"""


@router.get(SWAGGER_PAGE)
def swagger(_: Actor = Depends(require_staff_member)) -> HTMLResponse:
    """A página do Swagger, que lê o OpenAPI com o mesmo cookie da sessão."""
    return HTMLResponse(_swagger_page())


@router.get(SWAGGER_ASSETS + "/{name}")
def swagger_asset(name: str, _: Actor = Depends(require_staff_member)) -> Response:
    """Um arquivo do Swagger UI (JS ou CSS), conferido na subida."""
    asset = ASSETS.get(name)
    if asset is None:
        raise HTTPException(status_code=404, detail="arquivo não encontrado")
    return Response(
        asset.content, media_type=asset.media_type, headers={"Cache-Control": ASSET_CACHE}
    )


@router.get(OPENAPI_PATH)
def openapi(request: Request, _: Actor = Depends(require_staff_member)) -> dict[str, Any]:
    """O esquema OpenAPI da API inteira."""
    schema: dict[str, Any] = request.app.openapi()
    return schema
