"""Rotas públicas do ``tag.js``, fora do /api/v1: /api/tag/*.

Sem sessão nem cookie; as duas têm limite por IP. A configuração responde a qualquer origem; a
página vista (por ``sendBeacon``, que manda credenciais) devolve a origem do pedido no CORS e lê
o corpo como JSON mesmo em ``text/plain``.
"""

from fastapi import APIRouter, Depends, Query, Request, Response, status

from avant_api.modules.ad_tag_public.dependencies import public_ad_tag_service
from avant_api.modules.ad_tag_public.dto import PageViewIn
from avant_api.modules.ad_tag_public.service import PublicAdTagService
from avant_api.modules.reward_public.controller import client_address, cors, read_body

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


@router.options("/page-views")
def preflight(request: Request) -> Response:
    """Preflight do fetch da tag, que vem do site do cliente."""
    return Response(status_code=status.HTTP_204_NO_CONTENT, headers=cors(request))


@router.post("/page-views")
async def page_views(
    request: Request, service: PublicAdTagService = Depends(public_ad_tag_service)
) -> Response:
    """Guarda a página vista para o worker; 202, ou 422 fora do formato."""
    body = await read_body(request, PageViewIn)
    service.page_view(body, client_address(request))
    return Response(status_code=status.HTTP_202_ACCEPTED, headers=cors(request))
