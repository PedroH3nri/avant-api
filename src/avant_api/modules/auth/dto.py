"""DTOs de entrada e saída do domínio auth. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import datetime

from avant_core.access.domain import SiteScope
from avant_core.company.domain import (
    InvitationKind,
    InvitationStatus,
)
from avant_core.identity.application import Authenticated
from avant_core.identity.domain import Locale
from pydantic import BaseModel, EmailStr, Field

from avant_api.shared.dto import UserOut


class CompanyOut(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    accent_color: str | None
    is_owner: bool
    # A Company Groone: o painel mostra o painel interno.
    is_internal: bool


class MeOut(BaseModel):
    user: UserOut
    companies: list[CompanyOut]
    active_company_id: uuid.UUID | None
    permissions: list[str]
    site_scope: SiteScope | None
    is_staff: bool
    mfa_enabled: bool
    # Equipe Groone sem 2FA: o painel só mostra a configuração.
    mfa_setup_required: bool
    # Moeda em que a pessoa vê os valores do painel.
    display_currency: str

    @classmethod
    def of(cls, auth: Authenticated) -> "MeOut":
        """Monta a resposta de /me com a pessoa, as Empresas e as permissões na ativa."""
        user = auth.user
        return cls(
            user=UserOut(id=user.id, email=user.email, name=user.name, locale=user.locale),
            companies=[
                CompanyOut(
                    id=access.company.id,
                    name=access.company.name,
                    slug=access.company.slug,
                    accent_color=access.company.accent_color,
                    is_owner=access.company.owner_user_id == user.id,
                    is_internal=access.company.is_internal,
                )
                for access in auth.companies
            ],
            active_company_id=auth.active.company.id if auth.active else None,
            permissions=sorted(auth.grants.permissions) if auth.grants else [],
            site_scope=auth.grants.site_scope if auth.grants else None,
            is_staff=auth.is_staff,
            mfa_enabled=user.mfa_enabled,
            mfa_setup_required=auth.mfa_setup_required,
            display_currency=user.display_currency,
        )


class LoginIn(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=1024)


class LoginOut(BaseModel):
    mfa_required: bool
    # Vazio enquanto falta o código do 2FA.
    me: MeOut | None


class ActiveCompanyIn(BaseModel):
    company_id: uuid.UUID


class InvitationPreviewOut(BaseModel):
    kind: InvitationKind
    email: str
    status: InvitationStatus
    expires_at: datetime
    company_name: str | None
    role_name: dict[str, str] | None
    account_exists: bool


class AcceptInvitationIn(BaseModel):
    """Sem sessão: name e password criam a conta. Com sessão: a conta logada aceita."""

    name: str | None = Field(default=None, min_length=1, max_length=120)
    password: str | None = Field(default=None, max_length=1024)
    locale: Locale = Locale.PT
