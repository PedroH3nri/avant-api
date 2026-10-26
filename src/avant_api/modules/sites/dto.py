"""DTOs de entrada e saída do domínio sites. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import datetime

from avant_core.gam.domain import (
    AdUnit,
    InventoryStatus,
    Site,
)
from avant_core.gam.inventory import SiteDetail, SiteMember, SiteView
from pydantic import BaseModel, Field

from avant_api.shared.dto import MemberOut


class SiteIn(BaseModel):
    domain: str = Field(min_length=1, max_length=300)


class SiteOut(BaseModel):
    id: uuid.UUID
    # Vazio enquanto aguarda o GAM.
    network_id: uuid.UUID | None
    domain: str
    approval_status: str | None
    status: InventoryStatus
    synced_at: datetime | None
    # Cadastrado à mão, o GAM ainda não trouxe.
    awaiting_gam: bool

    @classmethod
    def of(cls, site: Site) -> "SiteOut":
        """Monta o site."""
        return cls(
            id=site.id,
            network_id=site.network_id,
            domain=site.domain,
            approval_status=site.approval_status,
            status=site.status,
            synced_at=site.synced_at,
            awaiting_gam=site.awaiting_gam,
        )


class SiteListOut(SiteOut):
    # Quantos ad units ativos o site tem.
    ad_units: int

    @classmethod
    def of_view(cls, view: SiteView) -> "SiteListOut":
        """Monta o site da listagem com a contagem de ad units ativos."""
        return cls(**SiteOut.of(view.site).model_dump(), ad_units=view.ad_units)


class AdUnitOut(BaseModel):
    id: uuid.UUID
    network_id: uuid.UUID
    parent_id: uuid.UUID | None
    site_id: uuid.UUID | None
    site_manual: bool
    name: str
    code: str | None
    status: InventoryStatus
    synced_at: datetime

    @classmethod
    def of(cls, unit: AdUnit) -> "AdUnitOut":
        """Monta o ad unit."""
        return cls(
            id=unit.id,
            network_id=unit.network_id,
            parent_id=unit.parent_id,
            site_id=unit.site_id,
            site_manual=unit.site_manual,
            name=unit.name,
            code=unit.ad_unit_code,
            status=unit.status,
            synced_at=unit.synced_at,
        )


class SiteDetailOut(SiteOut):
    ad_units: list[AdUnitOut]
    # Ids das Memberships com o site atribuído; só para quem tem sites.assign.
    assigned_to: list[uuid.UUID] | None

    @classmethod
    def of_detail(cls, detail: SiteDetail) -> "SiteDetailOut":
        """Monta o site com seus ad units e quem o tem atribuído."""
        return cls(
            **SiteOut.of(detail.site).model_dump(),
            ad_units=[AdUnitOut.of(unit) for unit in detail.ad_units],
            assigned_to=detail.assigned_to,
        )


class AdUnitPatchIn(BaseModel):
    """``site_id`` liga (ou ``null`` desliga) à mão; ``automatic: true`` volta a ligar pelo
    nome na próxima importação."""

    site_id: uuid.UUID | None = None
    automatic: bool = False


class MemberSitesIn(BaseModel):
    site_ids: list[uuid.UUID] = Field(max_length=1000)


class SiteMemberOut(MemberOut):
    # "assigned" (atribuído) ou "all" (vê todos os sites).
    via: str

    @classmethod
    def of_site_member(cls, view: SiteMember) -> "SiteMemberOut":
        """Monta quem vê o site e por quê (atribuído ou todos)."""
        return cls(**MemberOut.of(view.member).model_dump(), via=view.via)
