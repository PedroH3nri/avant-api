"""Métricas personalizadas da Empresa: /api/v1/custom-metrics.

Ver pede ``reports.view``; criar, editar, apagar e conferir pedem ``metrics.manage``. A
conferência responde o erro da fórmula (com a posição) sem gravar nada.
"""

import uuid

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, status

from avant_api.app.security import require
from avant_api.modules.custom_metrics.dependencies import custom_metric_service
from avant_api.modules.custom_metrics.dto import (
    CustomMetricCheckIn,
    CustomMetricCheckOut,
    CustomMetricIn,
    CustomMetricOut,
)
from avant_api.modules.custom_metrics.service import CustomMetricService
from avant_api.shared.dto import ItemsOut

router = APIRouter(tags=["custom-metrics"])


@router.get("/custom-metrics")
def index(
    actor: Actor = Depends(require("reports.view")),
    service: CustomMetricService = Depends(custom_metric_service),
) -> ItemsOut[CustomMetricOut]:
    """Métricas personalizadas da Empresa, pelo nome."""
    return ItemsOut(items=service.list_all(actor))


@router.post("/custom-metrics", status_code=status.HTTP_201_CREATED)
def create(
    body: CustomMetricIn,
    actor: Actor = Depends(require("metrics.manage")),
    service: CustomMetricService = Depends(custom_metric_service),
) -> CustomMetricOut:
    """Cadastra uma métrica personalizada; a chave nasce do nome."""
    return service.create(actor, body)


@router.post("/custom-metrics/validate")
def check(
    body: CustomMetricCheckIn,
    actor: Actor = Depends(require("metrics.manage")),
    service: CustomMetricService = Depends(custom_metric_service),
) -> CustomMetricCheckOut:
    """Confere o formulário como salvar faria, sem gravar."""
    return service.check(actor, body)


@router.put("/custom-metrics/{metric_id}")
def update(
    metric_id: uuid.UUID,
    body: CustomMetricIn,
    actor: Actor = Depends(require("metrics.manage")),
    service: CustomMetricService = Depends(custom_metric_service),
) -> CustomMetricOut:
    """Troca nome, fórmula, formato, casas e descrição; a chave fica a mesma."""
    return service.update(actor, metric_id, body)


@router.delete("/custom-metrics/{metric_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    metric_id: uuid.UUID,
    actor: Actor = Depends(require("metrics.manage")),
    service: CustomMetricService = Depends(custom_metric_service),
) -> None:
    """Apaga uma métrica personalizada; recusa (409) se outra a usa."""
    service.delete(actor, metric_id)
