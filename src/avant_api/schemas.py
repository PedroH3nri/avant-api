"""Formatos de entrada e saída. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import datetime

from avant_core.access.domain import SiteScope
from avant_core.company.domain import InvitationKind, InvitationStatus
from avant_core.identity.application import Authenticated
from avant_core.identity.domain import Locale
from pydantic import BaseModel, EmailStr, Field


class UserOut(BaseModel):
    id: uuid.UUID
    email: str
    name: str
    locale: Locale


class CompanyOut(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    accent_color: str | None
    is_owner: bool


class MeOut(BaseModel):
    user: UserOut
    companies: list[CompanyOut]
    active_company_id: uuid.UUID | None
    permissions: list[str]
    site_scope: SiteScope | None
    is_staff: bool
    mfa_enabled: bool
    mfa_setup_required: bool  # equipe Groone sem 2FA: o painel só mostra a configuração

    @classmethod
    def of(cls, auth: Authenticated) -> "MeOut":
        u = auth.user
        return cls(
            user=UserOut(id=u.id, email=u.email, name=u.name, locale=u.locale),
            companies=[
                CompanyOut(
                    id=c.company.id,
                    name=c.company.name,
                    slug=c.company.slug,
                    accent_color=c.company.accent_color,
                    is_owner=c.company.owner_user_id == u.id,
                )
                for c in auth.companies
            ],
            active_company_id=auth.active.company.id if auth.active else None,
            permissions=sorted(auth.grants.permissions) if auth.grants else [],
            site_scope=auth.grants.site_scope if auth.grants else None,
            is_staff=auth.is_staff,
            mfa_enabled=u.mfa_enabled,
            mfa_setup_required=auth.mfa_setup_required,
        )


class LoginIn(BaseModel):
    email: EmailStr
    password: str = Field(min_length=1, max_length=1024)


class LoginOut(BaseModel):
    mfa_required: bool
    me: MeOut | None  # vazio enquanto falta o código do 2FA


class MfaCodeIn(BaseModel):
    """Código de 6 dígitos do app ou um código de recuperação (xxxx-xxxx)."""

    code: str = Field(min_length=6, max_length=16)


class MfaSetupOut(BaseModel):
    secret: str
    uri: str  # otpauth://..., para o QR code


class RecoveryCodesOut(BaseModel):
    recovery_codes: list[str]  # aparecem só nesta resposta


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


class NewCompanyIn(BaseModel):
    name: str = Field(min_length=2, max_length=120)
    accent_color: str | None = Field(default=None, pattern=r"^#[0-9a-fA-F]{6}$")


class AcceptInvitationIn(BaseModel):
    """Sem sessão: name e password criam a conta. Com sessão: a conta logada aceita."""

    name: str | None = Field(default=None, min_length=1, max_length=120)
    password: str | None = Field(default=None, max_length=1024)
    locale: Locale = Locale.PT
    company: NewCompanyIn | None = None  # obrigatório no convite de dono


class InviteIn(BaseModel):
    email: EmailStr
    role_id: uuid.UUID


class InvitationOut(BaseModel):
    id: uuid.UUID
    email: str
    role_id: uuid.UUID | None
    status: InvitationStatus
    expires_at: datetime
    invited_by: uuid.UUID


class ItemsOut[T](BaseModel):
    items: list[T]
    next_cursor: str | None = None
