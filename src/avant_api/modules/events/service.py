"""Service dos avisos em tempo real da Empresa ativa."""

from collections.abc import AsyncIterator

from avant_core.access.models import Actor

from avant_api.app.events import EventSource, StreamLimiter, sse


class EventService:
    """Fluxo Server-Sent Events filtrado pelas permissões de quem escuta, com teto de streams."""

    def __init__(self, source: EventSource, limiter: StreamLimiter) -> None:
        self._source = source
        self._limiter = limiter

    def stream(self, actor: Actor) -> AsyncIterator[str]:
        """O corpo ``text/event-stream`` com os eventos da Empresa ativa; recusa com 429 acima
        do teto de streams da pessoa ou do processo."""
        self._limiter.acquire(actor.user_id)
        return self._released(actor)

    async def _released(self, actor: Actor) -> AsyncIterator[str]:
        """Repassa os eventos e devolve o stream ao teto quando a conexão acaba."""
        try:
            async for chunk in sse(self._source, company_id=actor.company_id, can=actor.grants.can):
                yield chunk
        finally:
            self._limiter.release(actor.user_id)
