"""Histórico de ações da Empresa ativa: /api/v1/audit."""

import uuid
from datetime import datetime

from avant_core.audit.repository import AuditFilter
from avant_core.company.service import Actor
from fastapi import APIRouter, Depends, Query

from avant_api.app.security import require
from avant_api.modules.audit.dependencies import audit_service
from avant_api.modules.audit.service import AuditService
from avant_api.shared.dto import AuditOut, ItemsOut

router = APIRouter(prefix="/audit", tags=["audit"])


@router.get("")
def index(
    actor_id: uuid.UUID | None = Query(default=None, alias="actor"),
    action: str | None = Query(default=None, max_length=64),
    since: datetime | None = Query(default=None, alias="from"),
    until: datetime | None = Query(default=None, alias="to"),
    limit: int = Query(default=50, ge=1, le=200),
    cursor: str | None = Query(default=None, max_length=200),
    actor: Actor = Depends(require("audit.view")),
    service: AuditService = Depends(audit_service),
) -> ItemsOut[AuditOut]:
    """Lista a auditoria da Empresa ativa, com filtros e paginação por cursor."""
    filters = AuditFilter(actor_user_id=actor_id, action=action, since=since, until=until)
    return service.list_all(actor, filters, limit, cursor)
