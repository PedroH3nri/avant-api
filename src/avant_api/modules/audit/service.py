"""Service da auditoria da Empresa ativa."""

from avant_core.audit.repository import AuditFilter
from avant_core.audit.service import list_audit
from avant_core.company.service import Actor

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.shared.dto import AuditOut, ItemsOut


class AuditService:
    """Leitura do histórico de ações da Empresa ativa."""

    def __init__(self, uows: UnitOfWorkFactory) -> None:
        self._uows = uows

    def list_all(
        self, actor: Actor, filters: AuditFilter, limit: int, cursor: str | None
    ) -> ItemsOut[AuditOut]:
        """Uma página da auditoria com os filtros pedidos."""
        page = list_audit(
            self._uows.uow(actor.company_id),
            actor=actor,
            filters=filters,
            limit=limit,
            cursor=cursor,
        )
        return ItemsOut(
            items=[AuditOut.of(entry) for entry in page.items], next_cursor=page.next_cursor
        )
