"""Rotas públicas do ``tag.js``, fora do /api/v1: /api/tag/*.

Sem sessão nem cookie; a configuração responde a qualquer origem e tem limite por IP.
"""

from fastapi import APIRouter, Depends, Query, Request, Response

from avant_api.modules.ad_tag_public.dependencies import public_ad_tag_service
from avant_api.modules.ad_tag_public.service import PublicAdTagService
from avant_api.modules.reward_public.controller import client_address

PREFIX = "/api/tag"
CONFIG_CACHE = "public, max-age=60"
OPEN_CORS = {"Access-Control-Allow-Origin": "*"}

router = APIRouter(prefix=PREFIX, tags=["ad-tag-public"], include_in_schema=False)


@router.get("/config")
def config(
    request: Request,
    key: str = Query(max_length=40),
    url: str = Query(max_length=2000),
    service: PublicAdTagService = Depends(public_ad_tag_service),
) -> Response:
    """A configuração da versão no ar da tag para a página da URL; ``{"tag": null}`` quando
    não há."""
    body = service.config(key, url, client_address(request))
    headers = {**OPEN_CORS, "Cache-Control": CONFIG_CACHE}
    return Response(body, media_type="application/json", headers=headers)
