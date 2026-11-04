"""DTOs das ferramentas do GAM no painel interno."""

import uuid
from datetime import date, datetime

from avant_core.gam.networks.enums import Delegation, NetworkStatus
from avant_core.gam.tools.enums import GamFormat, GamRunState, GamStepState, GamToolKind
from avant_core.gam.tools.models import GamStep, GamToolNetwork, GamToolRun, GamToolSite
from avant_core.identity.models import User
from pydantic import BaseModel, Field


class GamToolClientOut(BaseModel):
    id: uuid.UUID
    name: str


class GamToolPersonOut(BaseModel):
    id: uuid.UUID
    name: str


class GamToolRunNetworkOut(BaseModel):
    id: uuid.UUID
    network_code: str
    display_name: str | None
    client_name: str


class GamToolNetworkOut(BaseModel):
    id: uuid.UUID
    network_code: str
    display_name: str | None
    delegation: Delegation | None
    status: NetworkStatus
    seller_id: str | None
    client: GamToolClientOut

    @classmethod
    def of(cls, view: GamToolNetwork) -> "GamToolNetworkOut":
        """A network com o cliente."""
        network = view.network
        return cls(
            id=network.id,
            network_code=network.network_code,
            display_name=network.display_name,
            delegation=network.delegation,
            status=network.status,
            seller_id=network.seller_id,
            client=GamToolClientOut(id=view.company.id, name=view.company.name),
        )


class GamToolSiteOut(BaseModel):
    id: uuid.UUID
    domain: str
    has_parent: bool
    blocks: int
    format: GamFormat | None
    blocks_date: date | None

    @classmethod
    def of(cls, site: GamToolSite) -> "GamToolSiteOut":
        """O site com os blocos que o Avant já importou."""
        return cls(
            id=site.site_id,
            domain=site.domain,
            has_parent=site.has_parent,
            blocks=site.blocks,
            format=site.format,
            blocks_date=site.blocks_date,
        )


class GamToolNetworkDetailOut(GamToolNetworkOut):
    sites: list[GamToolSiteOut]

    @classmethod
    def of_detail(cls, view: GamToolNetwork) -> "GamToolNetworkDetailOut":
        """A network, o cliente e os sites."""
        base = GamToolNetworkOut.of(view)
        return cls(**base.model_dump(), sites=[GamToolSiteOut.of(site) for site in view.sites])


class GamStepOut(BaseModel):
    key: str
    state: GamStepState
    site: str | None
    count: int | None
    gam_id: str | None
    error: str | None

    @classmethod
    def of(cls, step: GamStep) -> "GamStepOut":
        """Um passo da execução."""
        return cls(
            key=step.key,
            state=step.state,
            site=step.site,
            count=step.count,
            gam_id=step.gam_id,
            error=step.error,
        )


class GamToolRunOut(BaseModel):
    id: uuid.UUID
    network_id: uuid.UUID
    kind: GamToolKind
    format: GamFormat | None
    domains: list[str]
    state: GamRunState
    error_code: str | None
    requested_by: GamToolPersonOut | None
    network: GamToolRunNetworkOut | None = None
    created_at: datetime
    updated_at: datetime | None
    finished_at: datetime | None
    steps: list[GamStepOut]

    @classmethod
    def of(
        cls,
        run: GamToolRun,
        people: dict[uuid.UUID, User] | None = None,
        networks: dict[uuid.UUID, GamToolRunNetworkOut] | None = None,
    ) -> "GamToolRunOut":
        """A execução com os passos, quem pediu e, na lista, a network e o cliente."""
        person = (people or {}).get(run.requested_by)
        return cls(
            id=run.id,
            network_id=run.network_id,
            kind=run.kind,
            format=run.format,
            domains=list(run.domains),
            state=run.state,
            error_code=run.error_code,
            requested_by=GamToolPersonOut(id=person.id, name=person.name) if person else None,
            network=(networks or {}).get(run.network_id),
            created_at=run.created_at,
            updated_at=run.updated_at,
            finished_at=run.finished_at,
            steps=[GamStepOut.of(step) for step in run.step_list()],
        )


class GamToolRunIn(BaseModel):
    network_id: uuid.UUID
    kind: GamToolKind
    domains: list[str] = Field(default_factory=list, max_length=20)
    format: GamFormat | None = None


class AdsTxtOut(BaseModel):
    lines: list[str]
