"""DTOs de entrada e saída do domínio company. Datas sempre em ISO 8601 UTC."""

import uuid

from avant_core.company.model import (
    CompanyStatus,
)
from avant_core.company.profile_model import (
    ClientProfile,
    FiscalData,
)
from avant_core.company.team_service import CompanyOverview
from pydantic import BaseModel, Field

from avant_api.shared.dto import FiscalDataOut, image_url

HEX_COLOR = r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$"


class CompanyDetailOut(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    accent_color: str | None
    status: CompanyStatus
    # Vazio na Company Groone: limites valem só para clientes.
    seat_limit: int | None
    seats_used: int
    settings: dict[str, object]
    # Vazio sem imagem: o painel mostra a inicial do nome sobre a cor da Empresa.
    image_url: str | None

    @classmethod
    def of(cls, overview: CompanyOverview) -> "CompanyDetailOut":
        """Monta o detalhe da Empresa com as vagas ocupadas."""
        company = overview.company
        return cls(
            id=company.id,
            name=company.name,
            slug=company.slug,
            accent_color=company.accent_color,
            status=company.status,
            seat_limit=company.seat_limit,
            seats_used=overview.seats_used,
            settings=company.settings,
            image_url=image_url("/company/image", company.image_version),
        )


class CompanyPatchIn(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=120)
    accent_color: str | None = Field(default=None, pattern=HEX_COLOR)
    settings: dict[str, object] | None = None


class FiscalDataIn(BaseModel):
    tax_type: str = Field(min_length=4, max_length=8)
    tax_id: str = Field(min_length=1, max_length=30)
    legal_name: str = Field(min_length=1, max_length=300)
    billing_phone_ddi: str = Field(min_length=1, max_length=8)
    billing_phone: str = Field(min_length=1, max_length=32)
    billing_address: str = Field(min_length=1, max_length=300)
    bank_name: str = Field(min_length=1, max_length=300)
    swift_code: str = Field(min_length=8, max_length=14)
    account_number: str = Field(min_length=1, max_length=300)
    routing_number: str = Field(min_length=1, max_length=300)

    def to_data(self) -> FiscalData:
        """Converte para os dados fiscais do core."""
        return FiscalData(**self.model_dump())


class CompanyFiscalOut(BaseModel):
    """O cadastro visto pelo próprio cliente em Configurações."""

    first_name: str
    last_name: str
    email: str
    fiscal: FiscalDataOut | None

    @classmethod
    def of(cls, profile: ClientProfile) -> "CompanyFiscalOut":
        """Monta o contato e os dados fiscais do cadastro."""
        return cls(
            first_name=profile.first_name,
            last_name=profile.last_name,
            email=profile.email,
            fiscal=FiscalDataOut.of(profile),
        )
