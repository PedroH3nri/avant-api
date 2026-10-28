"""DTOs de entrada e saída do domínio internal/mcm. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import datetime

from avant_core.gam.mcm.models import McmCandidate
from avant_core.gam.networks.enums import Delegation
from pydantic import BaseModel


class McmCandidateOut(BaseModel):
    id: uuid.UUID
    network_code: str
    display_name: str | None
    email: str
    delegation: Delegation | None
    account_status: str
    first_seen_at: datetime
    last_seen_at: datetime

    @classmethod
    def of(cls, candidate: McmCandidate) -> "McmCandidateOut":
        """Monta uma network do MCM que espera Empresa."""
        return cls(
            id=candidate.id,
            network_code=candidate.network_code,
            display_name=candidate.display_name,
            email=candidate.email,
            delegation=candidate.delegation,
            account_status=candidate.account_status,
            first_seen_at=candidate.first_seen_at,
            last_seen_at=candidate.last_seen_at,
        )


class AssignNetworkIn(BaseModel):
    company_id: uuid.UUID
