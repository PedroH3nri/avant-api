"""Envios agendados: /api/v1/schedules.

Ver pede ``reports.view`` (sem ``schedules.manage``, só os envios que a pessoa criou ou recebe);
criar pede ``schedules.manage`` e que a pessoa veja o relatório ou o dashboard. Editar, pausar e
apagar são do dono ou de quem tem ``schedules.manage``, conferido no avant-core. Como os
relatórios, na Company Groone só abrem pela sessão com 2FA. O envio roda no worker.
"""

import uuid

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require_report
from avant_api.modules.schedules.dependencies import schedule_service
from avant_api.modules.schedules.dto import (
    ScheduleIn,
    ScheduleOut,
    SchedulePageOut,
    SchedulePauseIn,
)
from avant_api.modules.schedules.service import ScheduleService

router = APIRouter(prefix="/schedules", tags=["schedules"])


@router.get("")
def index(
    query: str | None = Query(alias="q", default=None, max_length=200),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_report("reports.view")),
    service: ScheduleService = Depends(schedule_service),
) -> SchedulePageOut:
    """Os envios que a pessoa vê, o mais novo primeiro; ``q`` busca no nome."""
    return service.page(actor, query, page)


@router.post("", status_code=status.HTTP_201_CREATED)
def create(
    body: ScheduleIn,
    actor: Actor = Depends(require_report("schedules.manage")),
    service: ScheduleService = Depends(schedule_service),
) -> ScheduleOut:
    """Cria um envio; o primeiro sai no próximo horário."""
    return service.create(actor, body)


@router.get("/{schedule_id}")
def show(
    schedule_id: uuid.UUID,
    actor: Actor = Depends(require_report("reports.view")),
    service: ScheduleService = Depends(schedule_service),
) -> ScheduleOut:
    """Um envio que a pessoa vê; o de outra pessoa, sem ``schedules.manage``, é 404."""
    return service.get(actor, schedule_id)


@router.put("/{schedule_id}")
def update(
    schedule_id: uuid.UUID,
    body: ScheduleIn,
    actor: Actor = Depends(require_report("reports.view")),
    service: ScheduleService = Depends(schedule_service),
) -> ScheduleOut:
    """Troca o que manda, quando e para quem; o próximo envio é recalculado."""
    return service.update(actor, schedule_id, body)


@router.put("/{schedule_id}/pause")
def pause(
    schedule_id: uuid.UUID,
    body: SchedulePauseIn,
    actor: Actor = Depends(require_report("reports.view")),
    service: ScheduleService = Depends(schedule_service),
) -> ScheduleOut:
    """Pausa o envio ou volta a mandar no próximo horário."""
    return service.pause(actor, schedule_id, body.paused)


@router.delete("/{schedule_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    schedule_id: uuid.UUID,
    actor: Actor = Depends(require_report("reports.view")),
    service: ScheduleService = Depends(schedule_service),
) -> None:
    """Apaga o envio e o histórico dele."""
    service.delete(actor, schedule_id)
