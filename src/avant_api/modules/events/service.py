"""Service dos avisos em tempo real da Empresa ativa."""

from collections.abc import AsyncIterator

from avant_core.company.application import Actor

from avant_api.app.events import EventSource, sse


class EventService:
    """Fluxo Server-Sent Events filtrado pelas permissões de quem escuta."""

    def __init__(self, source: EventSource) -> None:
        self._source = source

    def stream(self, actor: Actor) -> AsyncIterator[str]:
        """O corpo ``text/event-stream`` com os eventos da Empresa ativa."""
        return sse(self._source, company_id=actor.company_id, can=actor.grants.can)
