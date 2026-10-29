"""DTOs usados por mais de um domínio."""

import uuid
from collections.abc import Callable
from datetime import datetime

from avant_core.audit.enums import ActorKind
from avant_core.audit.models import AuditEntry
from avant_core.company.enums import InvitationStatus, MembershipStatus
from avant_core.company.models import ClientProfile, Invitation
from avant_core.company.models.fiscal_data import FISCAL_FIELDS
from avant_core.company.services import MemberView
from avant_core.identity.enums import Locale
from avant_core.identity.models import User
from avant_core.shared.models import Page
from pydantic import BaseModel

# Prefixo das rotas, para montar as URLs que o painel usa direto (como a da imagem).
API_PATH = "/api/v1"


def image_url(path: str, version: str | None) -> str | None:
    """URL da imagem com a versão, que muda a cada imagem nova; vazia sem imagem."""
    return f"{API_PATH}{path}?v={version}" if version else None


class UserOut(BaseModel):
    id: uuid.UUID
    email: str
    name: str
    locale: Locale
    image_url: str | None = None

    @classmethod
    def of(cls, user: User) -> "UserOut":
        """Monta a pessoa com a URL versionada da foto de perfil."""
        return cls(
            id=user.id,
            email=user.email,
            name=user.name,
            locale=user.locale,
            image_url=image_url(f"/users/{user.id}/image", user.image_version),
        )


class InvitationOut(BaseModel):
    id: uuid.UUID
    email: str
    role_id: uuid.UUID | None
    status: InvitationStatus
    expires_at: datetime
    invited_by: uuid.UUID

    @classmethod
    def of(cls, invitation: Invitation) -> "InvitationOut":
        """Monta a resposta de um convite de equipe."""
        return cls(
            id=invitation.id,
            email=invitation.email,
            role_id=invitation.role_id,
            status=invitation.status,
            expires_at=invitation.expires_at,
            invited_by=invitation.invited_by,
        )


class ItemsOut[T](BaseModel):
    items: list[T]
    next_cursor: str | None = None


class PageOut[T](BaseModel):
    """Uma página de 10 itens de uma listagem, com o total e quantas páginas há."""

    items: list[T]
    total: int
    page: int
    pages: int
    page_size: int


def page_out[S, T](found: Page[S], convert: Callable[[S], T]) -> PageOut[T]:
    """A página do core convertida para o DTO, item a item."""
    return PageOut[T](
        items=[convert(item) for item in found.items],
        total=found.total,
        page=found.page,
        pages=found.pages,
        page_size=found.page_size,
    )


class RoleRefOut(BaseModel):
    id: uuid.UUID
    key: str
    name: dict[str, str]


class MemberOut(BaseModel):
    # O id é o da Membership.
    id: uuid.UUID
    user: UserOut
    role: RoleRefOut | None
    status: MembershipStatus
    is_owner: bool
    joined_at: datetime

    @classmethod
    def of(cls, view: MemberView) -> "MemberOut":
        """Monta o membro com pessoa e papel."""
        user, membership, role = view.user, view.membership, view.role
        return cls(
            id=membership.id,
            user=UserOut.of(user),
            role=RoleRefOut(id=role.id, key=role.key, name=role.name) if role else None,
            status=membership.status,
            is_owner=view.is_owner,
            joined_at=membership.joined_at,
        )


class AuditOut(BaseModel):
    id: uuid.UUID
    action: str
    actor_kind: ActorKind
    actor_user_id: uuid.UUID | None
    target_type: str | None
    target_id: uuid.UUID | None
    data: dict[str, object]
    created_at: datetime

    @classmethod
    def of(cls, entry: AuditEntry) -> "AuditOut":
        """Monta uma entrada da auditoria."""
        return cls(
            id=entry.id,
            action=entry.action,
            actor_kind=entry.actor_kind,
            actor_user_id=entry.actor_user_id,
            target_type=entry.target_type,
            target_id=entry.target_id,
            data=entry.data,
            created_at=entry.created_at,
        )


class FiscalDataOut(BaseModel):
    """Dados fiscais de pagamento: o cliente preenche, a equipe Groone só lê."""

    tax_type: str
    tax_id: str
    legal_name: str
    billing_phone_ddi: str
    billing_phone: str
    billing_address: str
    bank_name: str
    swift_code: str
    account_number: str
    routing_number: str

    @classmethod
    def of(cls, profile: ClientProfile) -> "FiscalDataOut | None":
        """Monta os dados fiscais do cadastro, ou nada se o cliente ainda não preencheu."""
        if not profile.has_fiscal_data:
            return None
        return cls(**{name: getattr(profile, name) for name in FISCAL_FIELDS})


class CompanyRefOut(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    is_internal: bool


class ContractClientRefOut(BaseModel):
    id: uuid.UUID
    name: str
