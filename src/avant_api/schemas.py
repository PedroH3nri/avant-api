"""Formatos de entrada e saída. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import date, datetime
from decimal import Decimal
from typing import Annotated

from avant_core.access.api_keys import MAX_DAYS, ApiKeyView
from avant_core.access.catalog import PermissionDef
from avant_core.access.domain import Effect, MemberPermission, Role, SiteScope
from avant_core.audit.domain import ActorKind, AuditEntry
from avant_core.company.domain import (
    CompanyStatus,
    InvitationKind,
    InvitationStatus,
    MembershipStatus,
)
from avant_core.company.profile import (
    CLIENT_FIELDS,
    FISCAL_FIELDS,
    ClientData,
    ClientProfile,
    FiscalData,
)
from avant_core.company.team import CompanyOverview, MemberDetail, MemberView, RoleView
from avant_core.costs.domain import MICROS, Cost, CostKind
from avant_core.gam.application import NetworkView
from avant_core.gam.domain import (
    AdUnit,
    ConnectionType,
    Contract,
    ContractSource,
    ContractStatus,
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
from avant_core.internal.contracts import ContractNetworkView, ContractView
from avant_core.metrics.catalog import (
    Dimension,
    Label,
    Metric,
    MetricFormat,
    MetricKind,
    MetricSource,
)
from avant_core.metrics.query import (
    MAX_FILTER_VALUES,
    MAX_LIMIT,
    UNFILTERABLE_DIMENSIONS,
    DateRange,
    DimensionValue,
    Filter,
    FilterOperator,
    Order,
    Period,
    QueryDefinition,
    QueryResult,
    RelativePeriod,
)
from avant_core.money.domain import BASE_CURRENCY
from avant_core.results.application import CompanyResults, Totals
from avant_core.results.domain import CostLine, MonthResult
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


class MfaCodeIn(BaseModel):
    """Código de 6 dígitos do app ou um código de recuperação (xxxx-xxxx)."""

    code: str = Field(min_length=6, max_length=16)


class MfaSetupOut(BaseModel):
    secret: str
    # O link otpauth://..., para o QR code.
    uri: str


class RecoveryCodesOut(BaseModel):
    # Aparecem só nesta resposta.
    recovery_codes: list[str]


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
    status: CompanyStatus
    # Vazio na Company Groone: limites valem só para clientes.
    seat_limit: int | None
    seats_used: int
    settings: dict[str, object]

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
            user=UserOut(id=user.id, email=user.email, name=user.name, locale=user.locale),
            role=RoleRefOut(id=role.id, key=role.key, name=role.name) if role else None,
            status=membership.status,
            is_owner=view.is_owner,
            joined_at=membership.joined_at,
        )


class DirectPermissionOut(BaseModel):
    permission: str
    effect: Effect
    expires_at: datetime | None

    @classmethod
    def of(cls, permission: MemberPermission) -> "DirectPermissionOut":
        """Monta uma permissão direta do membro."""
        return cls(
            permission=permission.permission_key,
            effect=permission.effect,
            expires_at=permission.expires_at,
        )


class MemberDetailOut(MemberOut):
    permissions: list[DirectPermissionOut]

    @classmethod
    def of(cls, view: MemberView) -> "MemberDetailOut":
        """Monta o membro com as permissões diretas."""
        assert isinstance(view, MemberDetail)
        base = MemberOut.of(view).model_dump()
        return cls(
            **base,
            permissions=[DirectPermissionOut.of(permission) for permission in view.permissions],
        )


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
    def of(cls, definition: PermissionDef) -> "PermissionOut":
        """Monta uma permissão do catálogo."""
        return cls(key=definition.key, group=definition.group, name=definition.label)


class RoleOut(BaseModel):
    id: uuid.UUID
    key: str
    name: dict[str, str]
    permissions: list[str]
    site_scope: SiteScope
    is_system: bool
    member_count: int

    @classmethod
    def of(cls, view: RoleView) -> "RoleOut":
        """Monta o papel com quantos membros o usam."""
        role: Role = view.role
        return cls(
            id=role.id,
            key=role.key,
            name=role.name,
            permissions=sorted(role.permissions),
            site_scope=role.site_scope,
            is_system=role.company_id is None,
            member_count=view.member_count,
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
            owner=(
                UserOut(id=owner.id, email=owner.email, name=owner.name, locale=owner.locale)
                if owner
                else None
            ),
            profile=ClientProfileOut.of(summary.profile) if summary.profile else None,
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
    # Só quando a pessoa tem 2FA ligado.
    mfa_code: str | None = Field(default=None, min_length=6, max_length=16)


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
    # A Groone configurou o cliente OAuth.
    available: bool
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
    def of(cls, run: NetworkSyncRun) -> "SyncRunOut":
        """Monta uma execução de sincronização."""
        return cls(
            id=run.id,
            kind=run.kind,
            status=run.status,
            started_at=run.started_at,
            finished_at=run.finished_at,
            counts=dict(run.counts),
            error_code=run.error_code,
            error_message=run.error_message,
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
    def of(cls, network: Network) -> "NetworkOut":
        """Monta a network."""
        return cls(
            id=network.id,
            network_code=network.network_code,
            display_name=network.display_name,
            connection_type=network.connection_type,
            delegation=network.delegation,
            status=network.status,
            last_error=network.last_error,
            failures=network.failures,
            last_checked_at=network.last_checked_at,
            last_synced_at=network.last_synced_at,
            sync_requested_at=network.sync_requested_at,
            created_at=network.created_at,
        )


class NetworkDetailOut(NetworkOut):
    # Quantos sites ativos a network tem.
    sites: int
    last_runs: dict[SyncKind, SyncRunOut]

    @classmethod
    def of_view(cls, view: NetworkView) -> "NetworkDetailOut":
        """Monta a network com os sites ativos e as últimas sincronizações."""
        return cls(
            **NetworkOut.of(view.network).model_dump(),
            sites=view.sites,
            last_runs={kind: SyncRunOut.of(run) for kind, run in view.last_runs.items()},
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


class ContractNetworkRefOut(BaseModel):
    id: uuid.UUID
    network_code: str
    display_name: str | None
    delegation: Delegation | None


class ContractClientRefOut(BaseModel):
    id: uuid.UUID
    name: str


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


class AssignNetworkIn(BaseModel):
    company_id: uuid.UUID


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


class ApiKeyOut(BaseModel):
    id: uuid.UUID
    name: str
    # Para reconhecer: avk_{prefix}...
    prefix: str
    permissions: list[str]
    owner: UserOut
    created_at: datetime
    expires_at: datetime
    last_used_at: datetime | None
    revoked_at: datetime | None

    @classmethod
    def of(cls, view: ApiKeyView) -> "ApiKeyOut":
        """Monta a chave de API com o dono, sem o token."""
        key, owner = view.key, view.owner
        return cls(
            id=key.id,
            name=key.name,
            prefix=key.prefix,
            permissions=list(key.permissions),
            owner=UserOut(id=owner.id, email=owner.email, name=owner.name, locale=owner.locale),
            created_at=key.created_at,
            expires_at=key.expires_at,
            last_used_at=key.last_used_at,
            revoked_at=key.revoked_at,
        )


class ApiKeyCreatedOut(ApiKeyOut):
    # Aparece só nesta resposta.
    token: str


class ApiKeyIn(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    permissions: list[str] = Field(min_length=1, max_length=50)
    expires_in_days: int = Field(default=MAX_DAYS, ge=1, le=MAX_DAYS)


class LabelOut(BaseModel):
    pt: str
    en: str
    es: str

    @classmethod
    def of(cls, label: Label) -> "LabelOut":
        """Monta o texto nos três idiomas."""
        return cls(pt=label.pt, en=label.en, es=label.es)


class MetricOut(BaseModel):
    key: str
    label: LabelOut
    kind: MetricKind
    format: MetricFormat
    # Fontes onde a métrica existe: as visitas (page_views) têm a sua.
    sources: list[MetricSource]

    @classmethod
    def of(cls, metric: Metric) -> "MetricOut":
        """Monta a métrica do catálogo."""
        return cls(
            key=metric.key,
            label=LabelOut.of(metric.label),
            kind=metric.kind,
            format=metric.format,
            sources=sorted(metric.sources),
        )


class DimensionOut(BaseModel):
    key: str
    label: LabelOut
    sources: list[MetricSource]
    # Data, semana, mês e hora agrupam, mas não filtram: o período já faz isso.
    filterable: bool

    @classmethod
    def of(cls, dimension: Dimension) -> "DimensionOut":
        """Monta a dimensão do catálogo."""
        return cls(
            key=dimension.key,
            label=LabelOut.of(dimension.label),
            sources=sorted(dimension.sources),
            filterable=dimension.key not in UNFILTERABLE_DIMENSIONS,
        )


class MetricCatalogOut(BaseModel):
    metrics: list[MetricOut]
    dimensions: list[DimensionOut]
    operators: list[FilterOperator]
    periods: list[RelativePeriod]
    max_days: int
    max_limit: int


class PeriodIn(BaseModel):
    preset: RelativePeriod | None = None
    start: date | None = None
    end: date | None = None


class FilterIn(BaseModel):
    field: str = Field(min_length=1, max_length=60)
    operator: FilterOperator
    values: list[Annotated[str, Field(max_length=300)]] = Field(
        min_length=1, max_length=MAX_FILTER_VALUES
    )


class OrderIn(BaseModel):
    field: str = Field(min_length=1, max_length=60)
    descending: bool = True


class ReportQueryIn(BaseModel):
    source: MetricSource = MetricSource.GAM
    metrics: list[str] = Field(min_length=1, max_length=30)
    period: PeriodIn
    dimensions: list[str] = Field(default_factory=list, max_length=6)
    filters: list[FilterIn] = Field(default_factory=list, max_length=20)
    # Soma também o período de mesmo tamanho logo antes.
    compare: bool = False
    order: list[OrderIn] = Field(default_factory=list, max_length=5)
    limit: int = Field(default=1000, ge=1, le=MAX_LIMIT)
    # Moeda do dinheiro na resposta; o painel manda a moeda de visualização da pessoa.
    currency: str = Field(default=BASE_CURRENCY, min_length=3, max_length=3)

    def definition(self) -> QueryDefinition:
        """A definição do motor de consulta do avant-core."""
        return QueryDefinition(
            source=self.source,
            metrics=tuple(self.metrics),
            period=Period(self.period.preset, self.period.start, self.period.end),
            dimensions=tuple(self.dimensions),
            filters=tuple(
                Filter(item.field, item.operator, tuple(item.values)) for item in self.filters
            ),
            compare=self.compare,
            order=tuple(Order(item.field, item.descending) for item in self.order),
            limit=self.limit,
            currency=self.currency.upper(),
        )


class ReportRowOut(BaseModel):
    # Datas em ISO, sites e networks pelo id (o nome vem em ``labels``).
    dimensions: dict[str, str | None]
    # Valores decimais como texto, para não perder centavos no caminho.
    metrics: dict[str, Decimal | None]
    previous: dict[str, Decimal | None] | None


class ReportRangeOut(BaseModel):
    start: date
    end: date

    @classmethod
    def of(cls, date_range: DateRange) -> "ReportRangeOut":
        """Monta o período."""
        return cls(start=date_range.start, end=date_range.end)


class ReportResultOut(BaseModel):
    period: ReportRangeOut
    rows: list[ReportRowOut]
    totals: dict[str, Decimal | None]
    previous_period: ReportRangeOut | None
    previous_totals: dict[str, Decimal | None] | None
    # Havia mais linhas que o limite.
    truncated: bool
    labels: dict[str, dict[str, str]]
    currency: str

    @classmethod
    def of(cls, result: QueryResult) -> "ReportResultOut":
        """Monta o resultado do motor de consulta."""
        return cls(
            period=ReportRangeOut.of(result.date_range),
            rows=[
                ReportRowOut(
                    dimensions={
                        key: dimension_text(value) for key, value in row.dimensions.items()
                    },
                    metrics=row.metrics,
                    previous=row.previous,
                )
                for row in result.rows
            ],
            totals=result.totals,
            previous_period=ReportRangeOut.of(result.previous_range)
            if result.previous_range is not None
            else None,
            previous_totals=result.previous_totals,
            truncated=result.truncated,
            labels=result.labels,
            currency=result.currency,
        )


class CurrencyOut(BaseModel):
    code: str
    name: str
    symbol: str
    decimals: int
    # Já existe cotação para converter (o dólar sempre tem).
    available: bool


class PreferencesIn(BaseModel):
    display_currency: str = Field(min_length=3, max_length=3)


def dimension_text(value: DimensionValue) -> str | None:
    """Valor de uma dimensão como texto: data em ISO, id como texto."""
    if value is None:
        return None
    if isinstance(value, date):
        return value.isoformat()
    return str(value)


# --- Custos e resultado ------------------------------------------------------------------


class CostIn(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    kind: CostKind
    currency: str = Field(min_length=3, max_length=3)
    # Qualquer dia do mês vale; o avant-core guarda o primeiro.
    start_month: date
    end_month: date | None = None
    # Valor na moeda do custo (de um mês só e recorrente).
    amount: Decimal | None = Field(default=None, ge=0, max_digits=18, decimal_places=6)
    # Conta sobre ``faturamento`` e ``receita`` do mês (tipo fórmula).
    formula: str | None = Field(default=None, max_length=300)


class CostOut(BaseModel):
    id: uuid.UUID
    name: str
    kind: CostKind
    currency: str
    start_month: date
    end_month: date | None
    amount: Decimal | None
    formula: str | None
    created_at: datetime
    updated_at: datetime

    @classmethod
    def of(cls, cost: Cost) -> "CostOut":
        """Monta o custo com o valor fora de micros."""
        return cls(
            id=cost.id,
            name=cost.name,
            kind=cost.kind,
            currency=cost.currency,
            start_month=cost.start_month,
            end_month=cost.end_month,
            amount=None if cost.amount_micros is None else Decimal(cost.amount_micros) / MICROS,
            formula=cost.formula,
            created_at=cost.created_at,
            updated_at=cost.updated_at,
        )


class FormulaCheckIn(BaseModel):
    formula: str = Field(max_length=300)
    # Valores de exemplo para a prévia do formulário.
    billing: Decimal = Field(default=Decimal(10000), max_digits=18, decimal_places=6)
    revenue: Decimal = Field(default=Decimal(9000), max_digits=18, decimal_places=6)


class FormulaCheckOut(BaseModel):
    valid: bool
    value: Decimal | None = None
    # Onde a fórmula quebrou, em português.
    error: str | None = None
    variables: list[str] = Field(default_factory=list)


class CostLineOut(BaseModel):
    cost_id: uuid.UUID
    name: str
    kind: CostKind
    amount: Decimal

    @classmethod
    def of(cls, line: CostLine) -> "CostLineOut":
        """Monta a linha de um custo no mês."""
        return cls(cost_id=line.cost_id, name=line.name, kind=line.kind, amount=line.amount)


class MonthResultOut(BaseModel):
    month: date
    billing: Decimal
    deductions: Decimal
    revenue: Decimal
    costs: Decimal
    result: Decimal
    # O GAM ainda não fechou o mês (por volta do dia 15 do mês seguinte).
    deductions_pending: bool
    cost_lines: list[CostLineOut]

    @classmethod
    def of(cls, month: MonthResult) -> "MonthResultOut":
        """Monta o resultado de um mês."""
        return cls(
            month=month.month,
            billing=month.billing,
            deductions=month.deductions,
            revenue=month.revenue,
            costs=month.costs,
            result=month.result,
            deductions_pending=month.deductions_pending,
            cost_lines=[CostLineOut.of(line) for line in month.cost_lines],
        )


class ResultTotalsOut(BaseModel):
    billing: Decimal
    deductions: Decimal
    revenue: Decimal
    costs: Decimal
    result: Decimal

    @classmethod
    def of(cls, totals: Totals) -> "ResultTotalsOut":
        """Monta o total do período."""
        return cls(
            billing=totals.billing,
            deductions=totals.deductions,
            revenue=totals.revenue,
            costs=totals.costs,
            result=totals.result,
        )


class ResultsOut(BaseModel):
    company: ContractClientRefOut
    currency: str
    months: list[MonthResultOut]
    totals: ResultTotalsOut

    @classmethod
    def of(cls, results: CompanyResults) -> "ResultsOut":
        """Monta o resultado de uma Empresa no período."""
        return cls(
            company=ContractClientRefOut(id=results.company_id, name=results.company_name),
            currency=results.currency,
            months=[MonthResultOut.of(month) for month in results.months],
            totals=ResultTotalsOut.of(results.totals),
        )
