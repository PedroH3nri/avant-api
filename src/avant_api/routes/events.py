"""GET /api/v1/events: avisos em tempo real da Empresa ativa (Server-Sent Events).

No proxy, esta rota precisa de ``proxy_buffering off`` (avant-infra).
"""

from avant_core.company.application import Actor
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from avant_api.deps import get_actor, get_services
from avant_api.events import sse
from avant_api.services import Services

router = APIRouter(tags=["events"])


@router.get("/events", response_class=StreamingResponse)
async def events(
    actor: Actor = Depends(get_actor),
    services: Services = Depends(get_services),
) -> StreamingResponse:
    body = sse(services.events, company_id=actor.company_id, can=actor.grants.can)
    return StreamingResponse(
        body,
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
