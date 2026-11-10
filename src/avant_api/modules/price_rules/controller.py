"""Regras de preço de um site da Empresa ativa: /api/v1/sites/{id}/price-rules.

Ver pede ``price_rules.view``; ligar, marcar blocos e mexer nas regras pede
``price_rules.manage``. Quem tem só alguns sites atribuídos mexe só nos deles (o core confere).
Os valores vão em micros, na moeda da network do site.
"""

import uuid
from datetime import date

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query

from avant_api.app.security import require
from avant_api.modules.price_rules.dependencies import price_rule_service
from avant_api.modules.price_rules.dto import (
    PriceRuleBlocksIn,
    PriceRuleConfigIn,
    PriceRuleDetailsOut,
    PriceRuleFloorIn,
    PriceRuleHistoryOut,
    PriceRuleOut,
    PriceRuleSettingsIn,
    PriceRuleSiteOut,
    PriceRuleStatusIn,
)
from avant_api.modules.price_rules.service import PriceRuleService
from avant_api.shared.dto import PageOut

VIEW = "price_rules.view"
MANAGE = "price_rules.manage"
BASE = "/sites/{site_id}/price-rules"

router = APIRouter(tags=["price-rules"])


@router.get(f"{BASE}/settings")
def settings(
    site_id: uuid.UUID,
    actor: Actor = Depends(require(VIEW)),
    service: PriceRuleService = Depends(price_rule_service),
) -> PriceRuleSiteOut:
    """A configuração, os blocos marcados e os blocos que o site tem no GAM."""
    return service.site(actor, site_id)


@router.put(f"{BASE}/settings")
def update_settings(
    site_id: uuid.UUID,
    body: PriceRuleSettingsIn,
    actor: Actor = Depends(require(MANAGE)),
    service: PriceRuleService = Depends(price_rule_service),
) -> PriceRuleSiteOut:
    """Liga ou desliga as regras do site e grava o grupo de controle (0 a 50%)."""
    return service.update_settings(actor, site_id, body)


@router.put(f"{BASE}/blocks")
def update_blocks(
    site_id: uuid.UUID,
    body: PriceRuleBlocksIn,
    actor: Actor = Depends(require(MANAGE)),
    service: PriceRuleService = Depends(price_rule_service),
) -> PriceRuleSiteOut:
    """Troca os blocos marcados; cada bloco roda um modelo."""
    return service.update_blocks(actor, site_id, body.blocks)


@router.get(BASE)
def index(
    site_id: uuid.UUID,
    page: int = Query(default=1, ge=1),
    content_hash: str | None = Query(default=None, max_length=64),
    country: str | None = Query(default=None, max_length=2),
    actor: Actor = Depends(require(VIEW)),
    service: PriceRuleService = Depends(price_rule_service),
) -> PageOut[PriceRuleOut]:
    """Uma página das regras do site, com filtro por hash e país."""
    return service.page(actor, site_id, page, content_hash, country)


@router.get(f"{BASE}/{{rule_id}}")
def show(
    site_id: uuid.UUID,
    rule_id: uuid.UUID,
    actor: Actor = Depends(require(VIEW)),
    service: PriceRuleService = Depends(price_rule_service),
) -> PriceRuleDetailsOut:
    """Uma regra com os limites do motor."""
    return service.get(actor, site_id, rule_id)


@router.get(f"{BASE}/{{rule_id}}/history")
def history(
    site_id: uuid.UUID,
    rule_id: uuid.UUID,
    start: date = Query(),
    end: date = Query(),
    actor: Actor = Depends(require(VIEW)),
    service: PriceRuleService = Depends(price_rule_service),
) -> list[PriceRuleHistoryOut]:
    """As decisões da regra hora a hora no período (até 31 dias), a mais nova primeiro."""
    return service.history(actor, site_id, rule_id, start, end)


@router.put(f"{BASE}/{{rule_id}}/config")
def update_config(
    site_id: uuid.UUID,
    rule_id: uuid.UUID,
    body: PriceRuleConfigIn,
    actor: Actor = Depends(require(MANAGE)),
    service: PriceRuleService = Depends(price_rule_service),
) -> PriceRuleDetailsOut:
    """Grava os limites; com ``automatic`` o motor volta a calcular sozinho."""
    return service.update_config(actor, site_id, rule_id, body)


@router.patch(f"{BASE}/{{rule_id}}")
def set_status(
    site_id: uuid.UUID,
    rule_id: uuid.UUID,
    body: PriceRuleStatusIn,
    actor: Actor = Depends(require(MANAGE)),
    service: PriceRuleService = Depends(price_rule_service),
) -> PriceRuleDetailsOut:
    """Ativa, pausa ou desliga a regra."""
    return service.set_status(actor, site_id, rule_id, body)


@router.put(f"{BASE}/{{rule_id}}/floor")
def set_floor(
    site_id: uuid.UUID,
    rule_id: uuid.UUID,
    body: PriceRuleFloorIn,
    actor: Actor = Depends(require(MANAGE)),
    service: PriceRuleService = Depends(price_rule_service),
) -> PriceRuleDetailsOut:
    """Troca o floor à mão (vai para o degrau mais perto da moeda)."""
    return service.set_floor(actor, site_id, rule_id, body)
