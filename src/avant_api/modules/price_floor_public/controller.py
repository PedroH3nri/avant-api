"""Rota pública dos floors das regras de preço: GET /api/tag/prices.

Sem sessão nem cookie, com limite por IP e CORS aberto. O ``tag.js`` pede com a chave da tag e
o ``content_hash`` da página e põe o resultado nas keys ``groone_prices`` e ``groone_group``.
"""

from fastapi import APIRouter, Depends, Query, Request, Response

from avant_api.modules.price_floor_public.dependencies import public_price_floor_service
from avant_api.modules.price_floor_public.dto import PublicPriceFloorsOut
from avant_api.modules.price_floor_public.service import PublicPriceFloorService
from avant_api.modules.reward_public.controller import client_address

PREFIX = "/api/tag"
OPEN_HEADERS = {"Access-Control-Allow-Origin": "*", "Cache-Control": "private, max-age=300"}

router = APIRouter(prefix=PREFIX, tags=["price-floor-public"], include_in_schema=False)


@router.get("/prices")
def prices(
    request: Request,
    response: Response,
    key: str = Query(max_length=40),
    content_hash: str = Query(alias="hash", pattern=r"^[A-Za-z0-9_-]{1,64}$"),
    service: PublicPriceFloorService = Depends(public_price_floor_service),
) -> PublicPriceFloorsOut:
    """O grupo de controle e os floors por bloco do hash, no país de quem pede; sem regra na
    tag, ``control_percent`` vazio."""
    response.headers.update(OPEN_HEADERS)
    return service.floors(key, content_hash, client_address(request))
