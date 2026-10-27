"""GET /api/v1/events: avisos em tempo real da Empresa ativa (Server-Sent Events).

No proxy, esta rota precisa de ``proxy_buffering off`` (avant-infra).
"""

from avant_core.company.service import Actor
from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from avant_api.app.security import get_actor
from avant_api.modules.events.dependencies import event_service
from avant_api.modules.events.service import EventService

router = APIRouter(tags=["events"])


@router.get("/events", response_class=StreamingResponse)
async def events(
    actor: Actor = Depends(get_actor),
    service: EventService = Depends(event_service),
) -> StreamingResponse:
    """Abre o fluxo SSE com os eventos da Empresa ativa."""
    return StreamingResponse(
        service.stream(actor),
        media_type="text/event-stream",
        headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
    )
