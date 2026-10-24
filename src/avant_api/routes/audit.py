"""Histórico de ações da Empresa ativa: /api/v1/audit."""

import uuid
from datetime import datetime

from avant_core.audit.application import list_audit
from avant_core.company.application import Actor
from avant_core.ports import AuditFilter
from fastapi import APIRouter, Depends, Query

from avant_api.deps import get_services, require
from avant_api.schemas import AuditOut, ItemsOut
from avant_api.services import Services

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
    services: Services = Depends(get_services),
) -> ItemsOut[AuditOut]:
    """Lista a auditoria da Empresa ativa, com filtros e paginação por cursor."""
    page = list_audit(
        services.uow(actor.company_id),
        actor=actor,
        filters=AuditFilter(actor_user_id=actor_id, action=action, since=since, until=until),
        limit=limit,
        cursor=cursor,
    )
    return ItemsOut(
        items=[AuditOut.of(entry) for entry in page.items], next_cursor=page.next_cursor
    )
