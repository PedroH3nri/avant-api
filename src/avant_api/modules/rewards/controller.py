"""Rewards da Empresa ativa: /api/v1/rewards e /api/v1/sites/{id}/reward-ad-units.

Ver e as métricas pedem ``rewards.view``; criar, editar, pausar, apagar e trocar o ícone pedem
``rewards.manage``; os contatos (dado pessoal) pedem ``rewards.leads``. Quem tem só alguns
sites atribuídos vê e mexe só nos rewards deles (o core confere).
"""

import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.rewards.models import RewardLeadFilter
from fastapi import APIRouter, Depends, Query, Response, status

from avant_api.app.security import require
from avant_api.modules.rewards.dependencies import reward_service
from avant_api.modules.rewards.dto import (
    RewardActiveIn,
    RewardAdUnitGroupOut,
    RewardIn,
    RewardLeadOut,
    RewardMetricsOut,
    RewardOut,
)
from avant_api.modules.rewards.http import csv_response, lead_filter, period
from avant_api.modules.rewards.service import RewardService
from avant_api.shared.dto import PageOut
from avant_api.shared.http import image_upload

VIEW = "rewards.view"
MANAGE = "rewards.manage"
LEADS = "rewards.leads"

router = APIRouter(tags=["rewards"])


@router.get("/rewards")
def index(
    query: str | None = Query(alias="q", default=None, max_length=200),
    site_id: uuid.UUID | None = Query(default=None),
    page: int = Query(default=1, ge=1),
    deleted: bool = Query(default=False),
    actor: Actor = Depends(require(VIEW)),
    service: RewardService = Depends(reward_service),
) -> PageOut[RewardOut]:
    """Uma página dos rewards, o mais novo primeiro, com busca no nome e na página; com
    ``deleted=true``, só os apagados (para as métricas e os contatos deles)."""
    return service.page(actor, page, site_id, query, deleted)


@router.post("/rewards", status_code=status.HTTP_201_CREATED)
def create(
    body: RewardIn,
    actor: Actor = Depends(require(MANAGE)),
    service: RewardService = Depends(reward_service),
) -> RewardOut:
    """Cria o reward de uma página de um site."""
    return service.create(actor, body)


@router.get("/rewards/{reward_id}")
def show(
    reward_id: uuid.UUID,
    actor: Actor = Depends(require(VIEW)),
    service: RewardService = Depends(reward_service),
) -> RewardOut:
    """Um reward com as perguntas."""
    return service.get(actor, reward_id)


@router.put("/rewards/{reward_id}")
def update(
    reward_id: uuid.UUID,
    body: RewardIn,
    actor: Actor = Depends(require(MANAGE)),
    service: RewardService = Depends(reward_service),
) -> RewardOut:
    """Troca todos os campos e as perguntas do reward."""
    return service.update(actor, reward_id, body)


@router.patch("/rewards/{reward_id}")
def set_active(
    reward_id: uuid.UUID,
    body: RewardActiveIn,
    actor: Actor = Depends(require(MANAGE)),
    service: RewardService = Depends(reward_service),
) -> RewardOut:
    """Pausa ou ativa o reward."""
    return service.set_active(actor, reward_id, body.active)


@router.delete("/rewards/{reward_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(
    reward_id: uuid.UUID,
    actor: Actor = Depends(require(MANAGE)),
    service: RewardService = Depends(reward_service),
) -> None:
    """Apaga o reward; as métricas e os contatos continuam guardados."""
    service.delete(actor, reward_id)


@router.put("/rewards/{reward_id}/icon")
def set_icon(
    reward_id: uuid.UUID,
    content: bytes = Depends(image_upload),
    actor: Actor = Depends(require(MANAGE)),
    service: RewardService = Depends(reward_service),
) -> RewardOut:
    """Troca o ícone por uma imagem: o corpo é o arquivo PNG, JPEG ou WebP de até 2 MB."""
    return service.set_icon(actor, reward_id, content)


@router.get("/sites/{site_id}/reward-ad-units")
def ad_units(
    site_id: uuid.UUID,
    actor: Actor = Depends(require(VIEW)),
    service: RewardService = Depends(reward_service),
) -> list[RewardAdUnitGroupOut]:
    """Os ad units de reward do site agrupados pela data do bloco, com os aparelhos."""
    return service.ad_units(actor, site_id)


@router.get("/rewards/{reward_id}/metrics")
def metrics(
    reward_id: uuid.UUID,
    dates: tuple[date, date] = Depends(period),
    actor: Actor = Depends(require(VIEW)),
    service: RewardService = Depends(reward_service),
) -> RewardMetricsOut:
    """As métricas do período (``from`` e ``to``; sem datas, os últimos 30 dias)."""
    return service.metrics(actor, reward_id, *dates)


@router.get("/rewards/{reward_id}/leads")
def leads(
    reward_id: uuid.UUID,
    page: int = Query(default=1, ge=1),
    filters: RewardLeadFilter = Depends(lead_filter),
    actor: Actor = Depends(require(LEADS)),
    service: RewardService = Depends(reward_service),
) -> PageOut[RewardLeadOut]:
    """Uma página dos contatos, o mais novo primeiro, com busca e filtro por resposta."""
    return service.leads(actor, reward_id, filters, page)


@router.get("/rewards/{reward_id}/leads/export", response_class=Response)
def export_leads(
    reward_id: uuid.UUID,
    filters: RewardLeadFilter = Depends(lead_filter),
    actor: Actor = Depends(require(LEADS)),
    service: RewardService = Depends(reward_service),
) -> Response:
    """Os contatos em CSV, com o mesmo filtro da lista."""
    return csv_response(service.export_leads(actor, reward_id, filters), "contatos.csv")


@router.delete("/rewards/{reward_id}/leads/{lead_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_lead(
    reward_id: uuid.UUID,
    lead_id: uuid.UUID,
    actor: Actor = Depends(require(LEADS)),
    service: RewardService = Depends(reward_service),
) -> None:
    """Apaga um contato (pedido do titular, por exemplo); fica na auditoria."""
    service.delete_lead(actor, reward_id, lead_id)
