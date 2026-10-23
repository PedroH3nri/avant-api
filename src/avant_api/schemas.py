"""Formatos de entrada e saída. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import datetime

from avant_core.access.catalog import PermissionDef
from avant_core.access.domain import Effect, MemberPermission, Role, SiteScope
from avant_core.audit.domain import ActorKind, AuditEntry
from avant_core.company.domain import (
    CompanyPlan,
    CompanyStatus,
    InvitationKind,
    InvitationStatus,
    MembershipStatus,
)
from avant_core.company.team import CompanyOverview, MemberDetail, MemberView, RoleView
from avant_core.gam.application import NetworkView
from avant_core.gam.domain import (
    AdUnit,
    ConnectionType,
    Delegation,
    InventoryStatus,
    McmCandidate,
    Network,
    NetworkStatus,
    NetworkSyncRun,
    Site,
    SyncKind,
    SyncStatus,
)
from avant_core.gam.inventory import SiteDetail, SiteMember, SiteView
from avant_core.identity.application import Authenticated
from avant_core.identity.domain import Locale, UserStatus
from avant_core.internal.application import ClientSummary
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


HEX_COLOR = r"^#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})$"


class CompanyDetailOut(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    accent_color: str | None
    plan: CompanyPlan
    status: CompanyStatus
    seat_limit: int
    seats_used: int
    settings: dict[str, object]

    @classmethod
    def of(cls, v: CompanyOverview) -> "CompanyDetailOut":
        c = v.company
        return cls(
            id=c.id,
            name=c.name,
            slug=c.slug,
            accent_color=c.accent_color,
            plan=c.plan,
            status=c.status,
            seat_limit=c.seat_limit,
            seats_used=v.seats_used,
            settings=c.settings,
        )


class CompanyPatchIn(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=120)
    accent_color: str | None = Field(default=None, pattern=HEX_COLOR)
    settings: dict[str, object] | None = None


class RoleRefOut(BaseModel):
    id: uuid.UUID
    key: str
    name: dict[str, str]


class MemberOut(BaseModel):
    id: uuid.UUID  # id da Membership
    user: UserOut
    role: RoleRefOut | None
    status: MembershipStatus
    is_owner: bool
    joined_at: datetime

    @classmethod
    def of(cls, v: MemberView) -> "MemberOut":
        u, m, r = v.user, v.membership, v.role
        return cls(
            id=m.id,
            user=UserOut(id=u.id, email=u.email, name=u.name, locale=u.locale),
            role=RoleRefOut(id=r.id, key=r.key, name=r.name) if r else None,
            status=m.status,
            is_owner=v.is_owner,
            joined_at=m.joined_at,
        )


class DirectPermissionOut(BaseModel):
    permission: str
    effect: Effect
    expires_at: datetime | None

    @classmethod
    def of(cls, p: MemberPermission) -> "DirectPermissionOut":
        return cls(permission=p.permission_key, effect=p.effect, expires_at=p.expires_at)


class MemberDetailOut(MemberOut):
    permissions: list[DirectPermissionOut]

    @classmethod
    def of(cls, v: MemberView) -> "MemberDetailOut":
        assert isinstance(v, MemberDetail)
        base = MemberOut.of(v).model_dump()
        return cls(**base, permissions=[DirectPermissionOut.of(p) for p in v.permissions])


class MemberPatchIn(BaseModel):
    role_id: uuid.UUID | None = None
    status: MembershipStatus | None = None


class DirectPermissionIn(BaseModel):
    permission: str
    effect: Effect
    expires_at: datetime | None = None


class MemberPermissionsIn(BaseModel):
    permissions: list[DirectPermissionIn] = Field(max_length=64)


class PermissionOut(BaseModel):
    key: str
    group: str
    name: dict[str, str]

    @classmethod
    def of(cls, p: PermissionDef) -> "PermissionOut":
        return cls(key=p.key, group=p.group, name=p.label)


class RoleOut(BaseModel):
    id: uuid.UUID
    key: str
    name: dict[str, str]
    permissions: list[str]
    site_scope: SiteScope
    is_system: bool
    member_count: int

    @classmethod
    def of(cls, v: RoleView) -> "RoleOut":
        r: Role = v.role
        return cls(
            id=r.id,
            key=r.key,
            name=r.name,
            permissions=sorted(r.permissions),
            site_scope=r.site_scope,
            is_system=r.company_id is None,
            member_count=v.member_count,
        )


class RoleIn(BaseModel):
    name: str = Field(min_length=1, max_length=60)
    permissions: list[str] = Field(default_factory=list, max_length=32)
    site_scope: SiteScope = SiteScope.ASSIGNED


class RolePatchIn(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=60)
    permissions: list[str] | None = Field(default=None, max_length=32)
    site_scope: SiteScope | None = None


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
    def of(cls, e: AuditEntry) -> "AuditOut":
        return cls(
            id=e.id,
            action=e.action,
            actor_kind=e.actor_kind,
            actor_user_id=e.actor_user_id,
            target_type=e.target_type,
            target_id=e.target_id,
            data=e.data,
            created_at=e.created_at,
        )


class ClientOut(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    plan: CompanyPlan
    status: CompanyStatus
    seat_limit: int
    seats_used: int
    owner: UserOut

    @classmethod
    def of(cls, v: ClientSummary) -> "ClientOut":
        c, o = v.company, v.owner
        return cls(
            id=c.id,
            name=c.name,
            slug=c.slug,
            plan=c.plan,
            status=c.status,
            seat_limit=c.seat_limit,
            seats_used=v.seats_used,
            owner=UserOut(id=o.id, email=o.email, name=o.name, locale=o.locale),
        )


class ClientDetailOut(ClientOut):
    members: list[MemberOut]
    invitations: list[InvitationOut]


class ClientIn(BaseModel):
    email: EmailStr
    seat_limit: int = Field(ge=1, le=10_000)
    plan: CompanyPlan


class ClientPatchIn(BaseModel):
    seat_limit: int | None = Field(default=None, ge=1, le=10_000)
    plan: CompanyPlan | None = None


class OwnerChangeIn(BaseModel):
    membership_id: uuid.UUID


class OwnerInvitationOut(BaseModel):
    id: uuid.UUID
    email: str
    status: InvitationStatus
    seat_limit: int | None
    plan: CompanyPlan | None
    expires_at: datetime
    invited_by: uuid.UUID


class CompanyRefOut(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    is_internal: bool


class PersonOut(BaseModel):
    user: UserOut
    status: UserStatus
    mfa_enabled: bool
    last_login_at: datetime | None
    companies: list[CompanyRefOut]


class StaffInviteIn(BaseModel):
    email: EmailStr
    role_id: uuid.UUID


# --- Conta ---------------------------------------------------------------------------


class ForgotPasswordIn(BaseModel):
    email: EmailStr


class ResetPasswordIn(BaseModel):
    token: str = Field(min_length=10, max_length=200)
    password: str = Field(min_length=1, max_length=1024)
    mfa_code: str | None = Field(default=None, min_length=6, max_length=16)  # só com 2FA


class ChangePasswordIn(BaseModel):
    current_password: str = Field(min_length=1, max_length=1024)
    new_password: str = Field(min_length=1, max_length=1024)


class SessionOut(BaseModel):
    id: uuid.UUID
    created_at: datetime
    last_seen_at: datetime
    expires_at: datetime
    user_agent: str | None
    ip: str | None
    current: bool


class RevokedOut(BaseModel):
    revoked: int


class GoogleStatusOut(BaseModel):
    available: bool  # a Groone configurou o cliente OAuth
    linked: bool


# --- GAM -------------------------------------------------------------------------------


class SyncRunOut(BaseModel):
    id: uuid.UUID
    kind: SyncKind
    status: SyncStatus
    started_at: datetime
    finished_at: datetime | None
    counts: dict[str, int]
    error_code: str | None
    error_message: str | None

    @classmethod
    def of(cls, r: NetworkSyncRun) -> "SyncRunOut":
        return cls(
            id=r.id,
            kind=r.kind,
            status=r.status,
            started_at=r.started_at,
            finished_at=r.finished_at,
            counts=dict(r.counts),
            error_code=r.error_code,
            error_message=r.error_message,
        )


class NetworkOut(BaseModel):
    id: uuid.UUID
    network_code: str
    display_name: str | None
    connection_type: ConnectionType
    delegation: Delegation | None
    status: NetworkStatus
    last_error: str | None
    failures: int
    last_checked_at: datetime | None
    last_synced_at: datetime | None
    sync_requested_at: datetime | None
    created_at: datetime

    @classmethod
    def of(cls, n: Network) -> "NetworkOut":
        return cls(
            id=n.id,
            network_code=n.network_code,
            display_name=n.display_name,
            connection_type=n.connection_type,
            delegation=n.delegation,
            status=n.status,
            last_error=n.last_error,
            failures=n.failures,
            last_checked_at=n.last_checked_at,
            last_synced_at=n.last_synced_at,
            sync_requested_at=n.sync_requested_at,
            created_at=n.created_at,
        )


class NetworkDetailOut(NetworkOut):
    sites: int  # ativos
    last_runs: dict[SyncKind, SyncRunOut]

    @classmethod
    def of_view(cls, v: NetworkView) -> "NetworkDetailOut":
        return cls(
            **NetworkOut.of(v.network).model_dump(),
            sites=v.sites,
            last_runs={k: SyncRunOut.of(r) for k, r in v.last_runs.items()},
        )


class NetworkIn(BaseModel):
    network_code: str = Field(min_length=1, max_length=20)


class ServiceAccountOut(BaseModel):
    """O que o guia de conexão mostra: o e-mail a adicionar como administrador no GAM."""

    email: str
    role: str = "Administrator"


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
    def of(cls, c: McmCandidate) -> "McmCandidateOut":
        return cls(
            id=c.id,
            network_code=c.network_code,
            display_name=c.display_name,
            email=c.email,
            delegation=c.delegation,
            account_status=c.account_status,
            first_seen_at=c.first_seen_at,
            last_seen_at=c.last_seen_at,
        )


class AssignNetworkIn(BaseModel):
    company_id: uuid.UUID


class SiteOut(BaseModel):
    id: uuid.UUID
    network_id: uuid.UUID
    domain: str
    approval_status: str | None
    status: InventoryStatus
    synced_at: datetime

    @classmethod
    def of(cls, s: Site) -> "SiteOut":
        return cls(
            id=s.id,
            network_id=s.network_id,
            domain=s.domain,
            approval_status=s.approval_status,
            status=s.status,
            synced_at=s.synced_at,
        )


class SiteListOut(SiteOut):
    ad_units: int  # ativos

    @classmethod
    def of_view(cls, v: SiteView) -> "SiteListOut":
        return cls(**SiteOut.of(v.site).model_dump(), ad_units=v.ad_units)


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
    def of(cls, u: AdUnit) -> "AdUnitOut":
        return cls(
            id=u.id,
            network_id=u.network_id,
            parent_id=u.parent_id,
            site_id=u.site_id,
            site_manual=u.site_manual,
            name=u.name,
            code=u.ad_unit_code,
            status=u.status,
            synced_at=u.synced_at,
        )


class SiteDetailOut(SiteOut):
    ad_units: list[AdUnitOut]
    # Ids das Memberships com o site atribuído; só para quem tem sites.assign.
    assigned_to: list[uuid.UUID] | None

    @classmethod
    def of_detail(cls, d: SiteDetail) -> "SiteDetailOut":
        return cls(
            **SiteOut.of(d.site).model_dump(),
            ad_units=[AdUnitOut.of(u) for u in d.ad_units],
            assigned_to=d.assigned_to,
        )


class AdUnitPatchIn(BaseModel):
    """``site_id`` liga (ou ``null`` desliga) à mão; ``automatic: true`` volta a ligar pelo
    nome na próxima importação."""

    site_id: uuid.UUID | None = None
    automatic: bool = False


class MemberSitesIn(BaseModel):
    site_ids: list[uuid.UUID] = Field(max_length=1000)


class SiteMemberOut(MemberOut):
    via: str  # "assigned" ou "all"

    @classmethod
    def of_site_member(cls, v: SiteMember) -> "SiteMemberOut":
        return cls(**MemberOut.of(v.member).model_dump(), via=v.via)
