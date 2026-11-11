"""Rotas públicas do script do reward, fora do /api/v1: /api/reward/*.

Sem sessão nem cookie. A configuração e o ícone respondem a qualquer origem; os eventos (por
``sendBeacon``, que manda credenciais) e o contato devolvem a origem do pedido no CORS. Todas
têm limite por IP. O corpo dos POSTs é lido como JSON mesmo em ``text/plain`` (o beacon sem
preflight).
"""

import uuid

from fastapi import APIRouter, Depends, Query, Request, Response, status
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, ValidationError

from avant_api.modules.reward_public.dependencies import public_reward_service
from avant_api.modules.reward_public.dto import RewardEventsIn, RewardLeadIn
from avant_api.modules.reward_public.service import PublicRewardService
from avant_api.shared.http import image_response

PREFIX = "/api/reward"
MAX_BODY = 16 * 1024
CONFIG_CACHE = "private, max-age=60"
OPEN_CORS = {"Access-Control-Allow-Origin": "*"}
CORS = {
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "86400",
    "Vary": "Origin",
}

router = APIRouter(prefix=PREFIX, tags=["reward-public"], include_in_schema=False)


def cors(request: Request) -> dict[str, str]:
    """Os cabeçalhos de CORS com a origem do pedido: a rota não lê cookie, então é seguro."""
    return {**CORS, "Access-Control-Allow-Origin": request.headers.get("Origin", "*")}


def client_address(request: Request) -> str:
    """O IP de quem pede (atrás do nginx, o uvicorn já traz o real)."""
    return request.client.host if request.client else "desconhecido"


async def read_body[Model: BaseModel](request: Request, model: type[Model]) -> Model:
    """Lê o corpo como JSON do modelo, com qualquer Content-Type e até ``MAX_BODY`` bytes; fora
    do formato, o mesmo 422 das outras rotas."""
    body = bytearray()
    async for chunk in request.stream():
        body.extend(chunk)
        if len(body) > MAX_BODY:
            break
    try:
        return model.model_validate_json(bytes(body))
    except ValidationError as error:
        raise RequestValidationError(error.errors()) from error


@router.get("/v2")
def page(
    request: Request,
    url: str = Query(max_length=2000),
    service: PublicRewardService = Depends(public_reward_service),
) -> Response:
    """A configuração do reward da página da URL; ``{"reward": null}`` quando não há."""
    body = service.page(url, client_address(request))
    headers = {**OPEN_CORS, "Cache-Control": CONFIG_CACHE}
    return Response(body, media_type="application/json", headers=headers)


@router.get("/icon/{reward_id}", response_class=Response)
def icon(
    request: Request,
    reward_id: uuid.UUID,
    service: PublicRewardService = Depends(public_reward_service),
) -> Response:
    """O ícone em imagem do reward, com cache longo (a URL leva a versão)."""
    response = image_response(request, service.icon(reward_id, client_address(request)))
    response.headers["Cache-Control"] = "public, max-age=31536000, immutable"
    response.headers.update(OPEN_CORS)
    return response


@router.options("/events")
@router.options("/leads")
def preflight(request: Request) -> Response:
    """Preflight do fetch do script, que vem do site do cliente."""
    return Response(status_code=status.HTTP_204_NO_CONTENT, headers=cors(request))


@router.post("/events")
async def events(
    request: Request, service: PublicRewardService = Depends(public_reward_service)
) -> Response:
    """Guarda o lote de eventos do script para o worker; sempre 202."""
    body = await read_body(request, RewardEventsIn)
    service.events(body, client_address(request))
    return Response(status_code=status.HTTP_202_ACCEPTED, headers=cors(request))


@router.post("/leads")
async def leads(
    request: Request, service: PublicRewardService = Depends(public_reward_service)
) -> Response:
    """Confere o contato do visitante e guarda para o worker; 202, ou 422 no formato errado."""
    body = await read_body(request, RewardLeadIn)
    service.lead(body, client_address(request))
    return Response(status_code=status.HTTP_202_ACCEPTED, headers=cors(request))
