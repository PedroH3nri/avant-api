"""Rota pública da g-tag, no mesmo caminho do Genius: trocar o domínio basta para a tag."""

from fastapi import APIRouter, Body, Depends, Request, Response, status

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.key_values.dto import KeyValueIn
from avant_api.modules.key_values.service import receive_key_values

PATH = "/api/admanager/keyvalue"
MAX_ITEMS = 20
CORS = {
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Max-Age": "86400",
    "Vary": "Origin",
}

router = APIRouter(tags=["key-values"], include_in_schema=False)


def cors(request: Request) -> dict[str, str]:
    """Os cabeçalhos de CORS com a origem do próprio pedido: o sendBeacon manda credenciais, e o
    navegador recusa ``*`` nesse caso. A rota não lê cookie, então devolver a origem é seguro."""
    return {**CORS, "Access-Control-Allow-Origin": request.headers.get("Origin", "*")}


@router.options(PATH)
def preflight(request: Request) -> Response:
    """Preflight do beacon ou do fetch da g-tag, que vem do site do cliente."""
    return Response(status_code=status.HTTP_204_NO_CONTENT, headers=cors(request))


@router.post(PATH)
def receive(
    request: Request,
    items: list[KeyValueIn] = Body(max_length=MAX_ITEMS),
    services: Services = Depends(get_services),
) -> Response:
    """Guarda os key-values da página para o worker criar os novos no GAM; sempre 202."""
    client = request.client.host if request.client else "desconhecido"
    receive_key_values(items, client=client, bucket=services.bucket, buffer=services.key_values)
    return Response(status_code=status.HTTP_202_ACCEPTED, headers=cors(request))
