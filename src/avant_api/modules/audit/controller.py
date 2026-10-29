"""Histórico de ações da Empresa ativa: /api/v1/audit."""

import uuid
from datetime import datetime

from avant_core.access.models import Actor
from avant_core.audit.interfaces import AuditFilter
from fastapi import APIRouter, Depends, Query

from avant_api.app.security import require
from avant_api.modules.audit.dependencies import audit_service
from avant_api.modules.audit.service import AuditService
from avant_api.shared.dto import AuditOut, PageOut

router = APIRouter(prefix="/audit", tags=["audit"])


@router.get("")
def index(
    actor_id: uuid.UUID | None = Query(default=None, alias="actor"),
    action: str | None = Query(default=None, max_length=64),
    since: datetime | None = Query(default=None, alias="from"),
    until: datetime | None = Query(default=None, alias="to"),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require("audit.view")),
    service: AuditService = Depends(audit_service),
) -> PageOut[AuditOut]:
    """A auditoria da Empresa ativa em páginas de 10, a mais nova primeiro, com filtros."""
    filters = AuditFilter(actor_user_id=actor_id, action=action, since=since, until=until)
    return service.page(actor, filters, page)
