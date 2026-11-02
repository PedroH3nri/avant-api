"""Alertas de métrica: /api/v1/alerts.

Ver pede ``reports.view`` (sem ``alerts.manage``, só os alertas que a pessoa criou ou recebe);
criar e a prévia pedem ``alerts.manage``. Editar, silenciar e apagar são do dono ou de quem tem
``alerts.manage``, conferido no avant-core. Como os relatórios, na Company Groone só abrem pela
sessão com 2FA. A conferência e o e-mail rodam no worker, de hora em hora.
"""

import uuid

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require_report
from avant_api.modules.alerts.dependencies import alert_service
from avant_api.modules.alerts.dto import (
    AlertEventOut,
    AlertIn,
    AlertMuteIn,
    AlertOut,
    AlertPageOut,
    AlertPreviewIn,
    AlertPreviewOut,
)
from avant_api.modules.alerts.service import AlertService
from avant_api.shared.dto import PageOut

router = APIRouter(prefix="/alerts", tags=["alerts"])


@router.get("")
def index(
    query: str | None = Query(alias="q", default=None, max_length=200),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_report("reports.view")),
    service: AlertService = Depends(alert_service),
) -> AlertPageOut:
    """Os alertas que a pessoa vê, o mais novo primeiro; ``q`` busca no nome."""
    return service.page(actor, query, page)


@router.post("", status_code=status.HTTP_201_CREATED)
def create(
    body: AlertIn,
    actor: Actor = Depends(require_report("alerts.manage")),
    service: AlertService = Depends(alert_service),
) -> AlertOut:
    """Cria um alerta, de quem cria, na moeda dela."""
    return service.create(actor, body)


@router.post("/preview")
def preview(
    body: AlertPreviewIn,
    actor: Actor = Depends(require_report("alerts.manage")),
    service: AlertService = Depends(alert_service),
) -> AlertPreviewOut:
    """Confere a definição com os dados do último dia fechado, sem gravar nada."""
    return service.preview(actor, body.definition)


@router.get("/{alert_id}")
def show(
    alert_id: uuid.UUID,
    actor: Actor = Depends(require_report("reports.view")),
    service: AlertService = Depends(alert_service),
) -> AlertOut:
    """Um alerta que a pessoa vê; o de outra pessoa, sem ``alerts.manage``, é 404."""
    return service.get(actor, alert_id)


@router.put("/{alert_id}")
def update(
    alert_id: uuid.UUID,
    body: AlertIn,
    actor: Actor = Depends(require_report("reports.view")),
    service: AlertService = Depends(alert_service),
) -> AlertOut:
    """Troca nome, regra e quem recebe; regra nova recomeça os disparos."""
    return service.update(actor, alert_id, body)


@router.put("/{alert_id}/mute")
def mute(
    alert_id: uuid.UUID,
    body: AlertMuteIn,
    actor: Actor = Depends(require_report("reports.view")),
    service: AlertService = Depends(alert_service),
) -> AlertOut:
    """Silencia o alerta até ``until`` (no máximo 90 dias); vazio tira o silêncio."""
    return service.mute(actor, alert_id, body.until)


@router.delete("/{alert_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    alert_id: uuid.UUID,
    actor: Actor = Depends(require_report("reports.view")),
    service: AlertService = Depends(alert_service),
) -> None:
    """Apaga o alerta e os disparos dele."""
    service.delete(actor, alert_id)


@router.get("/{alert_id}/events")
def events(
    alert_id: uuid.UUID,
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_report("reports.view")),
    service: AlertService = Depends(alert_service),
) -> PageOut[AlertEventOut]:
    """Os disparos do alerta, o mais recente primeiro."""
    return service.events(actor, alert_id, page)
