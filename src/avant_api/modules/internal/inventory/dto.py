"""Formatos das networks e dos sites dos clientes no painel interno."""

import uuid

from avant_core.company.models import Company
from avant_core.internal.services import ClientNetworkView, ClientSiteView
from pydantic import BaseModel

from avant_api.modules.networks.dto import NetworkOut
from avant_api.modules.sites.dto import SiteOut
from avant_api.shared.dto import ContractClientRefOut, RevenueStatusOut, image_url


class ClientRefOut(ContractClientRefOut):
    # Vazio sem imagem: o painel mostra a inicial do nome.
    image_url: str | None

    @classmethod
    def of(cls, company: Company) -> "ClientRefOut":
        """Monta o cliente da linha, com a imagem."""
        return cls(
            id=company.id,
            name=company.name,
            image_url=image_url(f"/internal/clients/{company.id}/image", company.image_version),
        )


class ClientNetworkOut(NetworkOut):
    client: ClientRefOut
    # Quantos sites ativos a network tem.
    sites: int
    # Vazio sem receita nos últimos 60 dias.
    revenue_status: RevenueStatusOut | None
    # E-mail do child no MCM, só nas que aguardam a confirmação da equipe.
    mcm_email: str | None

    @classmethod
    def of_view(cls, view: ClientNetworkView) -> "ClientNetworkOut":
        """Monta a network do cliente com os sites ativos e o status de faturamento."""
        return cls(
            **NetworkOut.of(view.network).model_dump(),
            client=ClientRefOut.of(view.company),
            sites=view.sites,
            revenue_status=RevenueStatusOut.of(view.revenue),
            mcm_email=view.mcm_email,
        )


class ClientSiteChecklistOut(BaseModel):
    id: uuid.UUID
    done: int
    total: int
    complete: bool


class ClientSiteOut(SiteOut):
    client: ClientRefOut
    # Nome da network; vazio enquanto o site aguarda o GAM.
    network_name: str | None
    # Quantos ad units ativos o site tem.
    ad_units: int
    # Vazio sem receita nos últimos 60 dias.
    revenue_status: RevenueStatusOut | None
    # Checklist do mês atual; vazio sem faturamento no mês anterior ou sem a permissão.
    checklist: ClientSiteChecklistOut | None = None

    @classmethod
    def of_view(cls, view: ClientSiteView) -> "ClientSiteOut":
        """Monta o site do cliente com a network, os ad units ativos e o status."""
        network = view.network
        return cls(
            **SiteOut.of(view.site).model_dump(),
            client=ClientRefOut.of(view.company),
            network_name=(network.display_name or network.network_code) if network else None,
            ad_units=view.ad_units,
            revenue_status=RevenueStatusOut.of(view.revenue),
        )
