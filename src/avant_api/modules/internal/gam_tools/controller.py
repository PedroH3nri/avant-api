"""Ferramentas do GAM no painel interno: /api/v1/internal/gam-tools.

Tudo pede ``internal.gam_tools.view``; abrir uma execução que escreve no GAM (configuração
completa, setup de anúncio e key values) pede também ``internal.gam_tools.run``, conferida
no core. A execução roda no worker; a tela acompanha pelo evento ``gam_tool_run.updated``.
"""

import uuid
from urllib.parse import quote

from avant_core.access.models import Actor
from fastapi import APIRouter, Depends, Query, Response, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.gam_tools.dependencies import gam_tool_service
from avant_api.modules.internal.gam_tools.dto import (
    AdsTxtOut,
    Domain,
    GamToolNetworkDetailOut,
    GamToolNetworkOut,
    GamToolRunIn,
    GamToolRunOut,
)
from avant_api.modules.internal.gam_tools.service import GamToolService
from avant_api.shared.dto import PageOut

router = APIRouter(prefix="/internal/gam-tools", tags=["internal"])
PERMISSION = "internal.gam_tools.view"


@router.get("/networks")
def networks(
    query: str | None = Query(default=None, alias="q", max_length=200),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: GamToolService = Depends(gam_tool_service),
) -> PageOut[GamToolNetworkOut]:
    """Uma página das networks dos clientes, pelo nome ou pelo network code."""
    return service.networks(actor, query, page)


@router.get("/networks/{network_id}")
def network(
    network_id: uuid.UUID,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: GamToolService = Depends(gam_tool_service),
) -> GamToolNetworkDetailOut:
    """A network com os sites e os blocos que o Avant já importou."""
    return service.network(actor, network_id)


@router.get("/runs")
def runs(
    network: uuid.UUID | None = None,
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: GamToolService = Depends(gam_tool_service),
) -> PageOut[GamToolRunOut]:
    """As execuções da network, ou de todas sem ``network``, a mais recente primeiro."""
    return service.runs(actor, network, page)


@router.post("/runs", status_code=status.HTTP_202_ACCEPTED)
def start(
    body: GamToolRunIn,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: GamToolService = Depends(gam_tool_service),
) -> GamToolRunOut:
    """Abre a execução com os passos pendentes e enfileira no worker."""
    return service.start(actor, body)


@router.get("/runs/{run_id}")
def run(
    run_id: uuid.UUID,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: GamToolService = Depends(gam_tool_service),
) -> GamToolRunOut:
    """Uma execução com os passos."""
    return service.run(actor, run_id)


@router.get("/ads-txt")
def ads_txt(
    network: uuid.UUID,
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: GamToolService = Depends(gam_tool_service),
) -> AdsTxtOut:
    """As linhas do ads.txt da network."""
    return service.ads_txt(actor, network)


@router.get("/install")
def install(
    network: uuid.UUID,
    sites: list[Domain] = Query(min_length=1, max_length=20),
    language: str = Query(default="pt", pattern="^(pt|en|es)$"),
    label: str = Query(default="pt", pattern="^(pt|en|es)$"),
    actor: Actor = Depends(require_staff(PERMISSION)),
    service: GamToolService = Depends(gam_tool_service),
) -> Response:
    """O arquivo de instalação Tag Light: .txt de um site ou .zip com vários."""
    name, content, media_type = service.install(actor, network, sites, language, label)
    safe = quote(name)
    headers = {"Content-Disposition": f"attachment; filename=\"{safe}\"; filename*=UTF-8''{safe}"}
    return Response(content=content, media_type=media_type, headers=headers)
