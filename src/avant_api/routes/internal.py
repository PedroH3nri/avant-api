"""Painel interno da Groone: /api/v1/internal.

Estas rotas usam ``trusted_uow()`` (sem RLS) porque a Groone enxerga todas as Empresas.
A proteção fica em duas camadas: ``require_staff`` aqui (Company Groone ativa, 2FA
verificado na sessão e a permissão) e, no core, ``ensure_staff`` em cada caso de uso.
"""

import uuid

from avant_core.company.application import Actor
from avant_core.company.domain import CompanyStatus, Invitation
from avant_core.internal.application import (
    PersonView,
    change_owner,
    client_audit,
    get_client,
    invite_client,
    invite_staff,
    list_clients,
    list_owner_invitations,
    list_staff,
    resend_owner_invitation,
    reset_user_mfa,
    search_users,
    set_client_status,
    set_user_status,
    update_client,
)
from avant_core.internal.application import (
    cancel_owner_invitation as cancel_owner_invite,
)
from fastapi import APIRouter, Depends, Query, status

from avant_api.deps import get_services, require_staff
from avant_api.routes.invitations import invitation_out
from avant_api.schemas import (
    AuditOut,
    ClientDetailOut,
    ClientIn,
    ClientOut,
    ClientPatchIn,
    CompanyRefOut,
    InvitationOut,
    ItemsOut,
    MemberOut,
    OwnerChangeIn,
    OwnerInvitationOut,
    PersonOut,
    StaffInviteIn,
    UserOut,
)
from avant_api.services import Services

router = APIRouter(prefix="/internal", tags=["internal"])


def _owner_invitation(i: Invitation) -> OwnerInvitationOut:
    return OwnerInvitationOut(
        id=i.id,
        email=i.email,
        status=i.status,
        seat_limit=i.seat_limit,
        plan=i.plan,
        expires_at=i.expires_at,
        invited_by=i.invited_by,
    )


def _person(p: PersonView) -> PersonOut:
    u = p.user
    return PersonOut(
        user=UserOut(id=u.id, email=u.email, name=u.name, locale=u.locale),
        status=u.status,
        mfa_enabled=u.mfa_enabled,
        last_login_at=u.last_login_at,
        companies=[
            CompanyRefOut(id=c.id, name=c.name, slug=c.slug, is_internal=c.is_internal)
            for c in p.companies
        ],
    )


# --- Clientes --------------------------------------------------------------------------


@router.get("/clients")
def clients(
    q: str | None = Query(default=None, max_length=120),
    company_status: CompanyStatus | None = Query(default=None, alias="status"),
    actor: Actor = Depends(require_staff("internal.clients.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[ClientOut]:
    items = list_clients(services.trusted_uow(), actor=actor, q=q, status=company_status)
    return ItemsOut(items=[ClientOut.of(c) for c in items])


@router.post("/clients", status_code=status.HTTP_201_CREATED)
def create_client(
    body: ClientIn,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    services: Services = Depends(get_services),
) -> OwnerInvitationOut:
    """Cadastra o cliente enviando o convite de dono. A Empresa nasce no aceite."""
    invitation = invite_client(
        services.trusted_uow(),
        actor=actor,
        email=body.email,
        seat_limit=body.seat_limit,
        plan=body.plan,
        clock=services.clock,
        mailer=services.mailer,
    )
    return _owner_invitation(invitation)


@router.get("/clients/{company_id}")
def client(
    company_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.clients.view")),
    services: Services = Depends(get_services),
) -> ClientDetailOut:
    d = get_client(services.trusted_uow(), actor=actor, company_id=company_id)
    return ClientDetailOut(
        **ClientOut.of(d).model_dump(),
        members=[MemberOut.of(m) for m in d.members],
        invitations=[invitation_out(i) for i in d.invitations],
    )


@router.get("/clients/{company_id}/audit")
def audit(
    company_id: uuid.UUID,
    limit: int = Query(default=50, ge=1, le=200),
    cursor: str | None = Query(default=None, max_length=200),
    actor: Actor = Depends(require_staff("internal.clients.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[AuditOut]:
    page = client_audit(
        services.trusted_uow(), actor=actor, company_id=company_id, limit=limit, cursor=cursor
    )
    return ItemsOut(items=[AuditOut.of(e) for e in page.items], next_cursor=page.next_cursor)


@router.patch("/clients/{company_id}")
def edit_client(
    company_id: uuid.UUID,
    body: ClientPatchIn,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    services: Services = Depends(get_services),
) -> ClientOut:
    view = update_client(
        services.trusted_uow(),
        actor=actor,
        company_id=company_id,
        clock=services.clock,
        seat_limit=body.seat_limit,
        plan=body.plan,
    )
    return ClientOut.of(view)


@router.post("/clients/{company_id}/suspend", status_code=status.HTTP_204_NO_CONTENT)
def suspend(
    company_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    services: Services = Depends(get_services),
) -> None:
    set_client_status(
        services.trusted_uow(),
        actor=actor,
        company_id=company_id,
        suspended=True,
        clock=services.clock,
    )


@router.post("/clients/{company_id}/reactivate", status_code=status.HTTP_204_NO_CONTENT)
def reactivate(
    company_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    services: Services = Depends(get_services),
) -> None:
    set_client_status(
        services.trusted_uow(),
        actor=actor,
        company_id=company_id,
        suspended=False,
        clock=services.clock,
    )


@router.post("/clients/{company_id}/owner", status_code=status.HTTP_204_NO_CONTENT)
def new_owner(
    company_id: uuid.UUID,
    body: OwnerChangeIn,
    actor: Actor = Depends(require_staff("internal.owner.change")),
    services: Services = Depends(get_services),
) -> None:
    change_owner(
        services.trusted_uow(),
        actor=actor,
        company_id=company_id,
        membership_id=body.membership_id,
        clock=services.clock,
    )


# --- Convites de dono ------------------------------------------------------------------


@router.get("/owner-invitations")
def owner_invitations(
    actor: Actor = Depends(require_staff("internal.clients.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[OwnerInvitationOut]:
    items = list_owner_invitations(services.trusted_uow(), actor=actor, clock=services.clock)
    return ItemsOut(items=[_owner_invitation(i) for i in items])


@router.post("/owner-invitations/{invitation_id}/resend")
def resend_owner(
    invitation_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    services: Services = Depends(get_services),
) -> OwnerInvitationOut:
    invitation = resend_owner_invitation(
        services.trusted_uow(),
        actor=actor,
        invitation_id=invitation_id,
        clock=services.clock,
        mailer=services.mailer,
    )
    return _owner_invitation(invitation)


@router.delete("/owner-invitations/{invitation_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel_owner(
    invitation_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    services: Services = Depends(get_services),
) -> None:
    cancel_owner_invite(services.trusted_uow(), actor=actor, invitation_id=invitation_id)


# --- Pessoas ---------------------------------------------------------------------------


@router.get("/users")
def users(
    q: str = Query(min_length=3, max_length=120),
    actor: Actor = Depends(require_staff("internal.users.manage")),
    services: Services = Depends(get_services),
) -> ItemsOut[PersonOut]:
    people = search_users(services.trusted_uow(), actor=actor, q=q)
    return ItemsOut(items=[_person(p) for p in people])


@router.post("/users/{user_id}/disable", status_code=status.HTTP_204_NO_CONTENT)
def disable(
    user_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.users.manage")),
    services: Services = Depends(get_services),
) -> None:
    set_user_status(
        services.trusted_uow(), actor=actor, user_id=user_id, disabled=True, clock=services.clock
    )


@router.post("/users/{user_id}/enable", status_code=status.HTTP_204_NO_CONTENT)
def enable(
    user_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.users.manage")),
    services: Services = Depends(get_services),
) -> None:
    set_user_status(
        services.trusted_uow(), actor=actor, user_id=user_id, disabled=False, clock=services.clock
    )


@router.post("/users/{user_id}/reset-mfa", status_code=status.HTTP_204_NO_CONTENT)
def reset_mfa(
    user_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.users.manage")),
    services: Services = Depends(get_services),
) -> None:
    reset_user_mfa(services.trusted_uow(), actor=actor, user_id=user_id, clock=services.clock)


# --- Equipe Groone ---------------------------------------------------------------------


@router.get("/staff")
def staff(
    actor: Actor = Depends(require_staff("internal.staff.manage")),
    services: Services = Depends(get_services),
) -> ItemsOut[MemberOut]:
    return ItemsOut(
        items=[MemberOut.of(m) for m in list_staff(services.trusted_uow(), actor=actor)]
    )


@router.post("/staff/invitations", status_code=status.HTTP_201_CREATED)
def invite(
    body: StaffInviteIn,
    actor: Actor = Depends(require_staff("internal.staff.manage")),
    services: Services = Depends(get_services),
) -> InvitationOut:
    invitation = invite_staff(
        services.trusted_uow(),
        actor=actor,
        email=body.email,
        role_id=body.role_id,
        clock=services.clock,
        mailer=services.mailer,
    )
    return invitation_out(invitation)
