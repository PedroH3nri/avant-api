"""DTOs de entrada e saída do domínio internal/clients. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import datetime
from decimal import Decimal

from avant_core.company.enums import CompanyStatus, InvitationStatus
from avant_core.company.models import ClientData, ClientProfile
from avant_core.company.models.client_data import CLIENT_FIELDS
from avant_core.identity.enums import Locale
from avant_core.internal.services import ClientSummary
from pydantic import BaseModel, EmailStr, Field

from avant_api.shared.dto import (
    CompanyRefOut,
    FiscalDataOut,
    InvitationOut,
    MemberOut,
    UserOut,
    image_url,
)


class ClientProfileOut(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_ddi: str | None
    phone: str | None
    locale: Locale
    account_manager_id: uuid.UUID | None
    referred_by_company_id: uuid.UUID | None
    referral_percentage: Decimal | None
    notes: str | None
    fiscal: FiscalDataOut | None

    @classmethod
    def of(cls, profile: ClientProfile) -> "ClientProfileOut":
        """Monta o cadastro do cliente para o painel interno."""
        return cls(
            **{name: getattr(profile, name) for name in CLIENT_FIELDS},
            fiscal=FiscalDataOut.of(profile),
        )


class ClientProfileIn(BaseModel):
    first_name: str = Field(min_length=1, max_length=120)
    last_name: str = Field(min_length=1, max_length=120)
    email: EmailStr
    phone_ddi: str | None = Field(default=None, max_length=8)
    phone: str | None = Field(default=None, max_length=32)
    locale: Locale = Locale.PT
    account_manager_id: uuid.UUID | None = None
    referred_by_company_id: uuid.UUID | None = None
    # Sem valor, a indicação vale 2%.
    referral_percentage: Decimal | None = Field(
        default=None, gt=0, le=100, max_digits=5, decimal_places=2
    )
    notes: str | None = Field(default=None, max_length=300)

    def to_data(self) -> ClientData:
        """Converte para os dados de cadastro do core."""
        return ClientData(**self.model_dump())


class ClientOut(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    status: CompanyStatus
    seat_limit: int
    seats_used: int
    # Vazio enquanto ninguém aceitou o convite de dono.
    owner: UserOut | None
    profile: ClientProfileOut | None
    # Vazio sem imagem: o painel mostra a inicial do nome.
    image_url: str | None

    @classmethod
    def of(cls, summary: ClientSummary) -> "ClientOut":
        """Monta a Empresa cliente com dono, cadastro e vagas para o painel interno."""
        company, owner = summary.company, summary.owner
        # Empresa de cliente sempre tem limite.
        assert company.seat_limit is not None
        return cls(
            id=company.id,
            name=company.name,
            slug=company.slug,
            status=company.status,
            seat_limit=company.seat_limit,
            seats_used=summary.seats_used,
            owner=(UserOut.of(owner) if owner else None),
            profile=ClientProfileOut.of(summary.profile) if summary.profile else None,
            image_url=image_url(f"/internal/clients/{company.id}/image", company.image_version),
        )


class ClientDetailOut(ClientOut):
    members: list[MemberOut]
    invitations: list[InvitationOut]


class ClientIn(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    seat_limit: int = Field(ge=1, le=10_000)
    profile: ClientProfileIn


class ClientPatchIn(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=120)
    seat_limit: int | None = Field(default=None, ge=1, le=10_000)
    profile: ClientProfileIn | None = None


class ClientStatusIn(BaseModel):
    status: CompanyStatus


class OwnerChangeIn(BaseModel):
    membership_id: uuid.UUID


class OwnerInvitationOut(BaseModel):
    id: uuid.UUID
    # Vazio só nos convites antigos, de antes do cadastro do cliente.
    company_id: uuid.UUID | None
    email: str
    status: InvitationStatus
    expires_at: datetime
    invited_by: uuid.UUID


class ClientMemberOut(MemberOut):
    company: CompanyRefOut


class ClientOptionOut(BaseModel):
    """O cliente nas listas inteiras para seletores e para contar as abas por situação."""

    id: uuid.UUID
    name: str
    status: CompanyStatus


class ManagerChangeOut(BaseModel):
    # Prazos do responsável de hoje que seguem com a pessoa nova e os que param na troca.
    continues: int
    stops: int
    # Prazos sem pessoa que passam para a pessoa nova.
    arrives: int
