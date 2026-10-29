"""Service da auditoria da Empresa ativa."""

from avant_core.access.models import Actor
from avant_core.audit.interfaces import AuditFilter
from avant_core.audit.services import page_audit

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.shared.dto import AuditOut, PageOut, page_out


class AuditService:
    """Leitura do histórico de ações da Empresa ativa."""

    def __init__(self, uows: UnitOfWorkFactory) -> None:
        self._uows = uows

    def page(self, actor: Actor, filters: AuditFilter, page: int) -> PageOut[AuditOut]:
        """Uma página da auditoria com os filtros pedidos."""
        found = page_audit(
            self._uows.uow(actor.company_id), actor=actor, filters=filters, page=page
        )
        return page_out(found, AuditOut.of)
