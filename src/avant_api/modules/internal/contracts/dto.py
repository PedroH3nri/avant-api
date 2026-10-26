"""DTOs de entrada e saída do domínio internal/contracts. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import datetime
from decimal import Decimal

from avant_core.gam.domain import (
    Contract,
    ContractSource,
    ContractStatus,
    Delegation,
    Network,
)
from avant_core.internal.contracts import ContractNetworkView, ContractView
from pydantic import BaseModel, Field

from avant_api.shared.dto import ContractClientRefOut


class ContractNetworkRefOut(BaseModel):
    id: uuid.UUID
    network_code: str
    display_name: str | None
    delegation: Delegation | None


class ContractOut(BaseModel):
    id: uuid.UUID
    revshare: Decimal
    status: ContractStatus
    source: ContractSource
    started_at: datetime
    ended_at: datetime | None
    notes: str | None
    created_by: uuid.UUID | None
    network: ContractNetworkRefOut
    company: ContractClientRefOut

    @classmethod
    def of(cls, view: ContractView) -> "ContractOut":
        """Monta o contrato com a network e a Empresa."""
        contract = view.contract
        return cls(
            **_contract_fields(contract),
            network=_network_ref(view.network),
            company=ContractClientRefOut(id=view.company.id, name=view.company.name),
        )


class ContractSummaryOut(BaseModel):
    id: uuid.UUID
    revshare: Decimal
    source: ContractSource
    started_at: datetime


class ContractNetworkOut(BaseModel):
    network: ContractNetworkRefOut
    company: ContractClientRefOut
    active: ContractSummaryOut | None
    manual: bool

    @classmethod
    def of(cls, view: ContractNetworkView) -> "ContractNetworkOut":
        """Monta a network MCM com o contrato em vigor."""
        active = view.active
        return cls(
            network=_network_ref(view.network),
            company=ContractClientRefOut(id=view.company.id, name=view.company.name),
            active=None
            if active is None
            else ContractSummaryOut(
                id=active.id,
                revshare=active.revshare,
                source=active.source,
                started_at=active.started_at,
            ),
            manual=view.manual,
        )


def _contract_fields(contract: Contract) -> dict[str, object]:
    """Os campos do próprio contrato."""
    return {
        "id": contract.id,
        "revshare": contract.revshare,
        "status": contract.status,
        "source": contract.source,
        "started_at": contract.started_at,
        "ended_at": contract.ended_at,
        "notes": contract.notes,
        "created_by": contract.created_by,
    }


def _network_ref(network: Network) -> ContractNetworkRefOut:
    """A network resumida, para os contratos."""
    return ContractNetworkRefOut(
        id=network.id,
        network_code=network.network_code,
        display_name=network.display_name,
        delegation=network.delegation,
    )


class ContractIn(BaseModel):
    network_id: uuid.UUID
    revshare: Decimal = Field(ge=0, le=100, max_digits=6, decimal_places=3)
    notes: str | None = Field(default=None, max_length=2000)


class ContractPatchIn(BaseModel):
    notes: str | None = Field(default=None, max_length=2000)
