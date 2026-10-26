"""Painel interno da Groone: /api/v1/internal.

Estas rotas usam ``trusted_uow()`` (sem RLS) porque a Groone enxerga todas as Empresas.
A proteção fica em duas camadas: ``require_staff`` aqui (Company Groone ativa, 2FA
verificado na sessão e a permissão) e, no core, ``ensure_staff`` em cada caso de uso.
"""

import uuid
from datetime import date

from avant_core.company.application import Actor
from avant_core.company.domain import CompanyStatus, Invitation
from avant_core.gam.application import assign_mcm_candidate, list_mcm_candidates
from avant_core.gam.domain import ContractStatus
from avant_core.internal.application import (
    PersonView,
    change_owner,
    client_audit,
    create_client,
    get_client,
    invite_staff,
    list_client_teams,
    list_clients,
    list_owner_invitations,
    list_staff,
    resend_owner_invitation,
    reset_user_mfa,
    search_users,
    send_owner_invitation,
    set_client_status,
    set_user_status,
    update_client,
)
from avant_core.internal.application import (
    cancel_owner_invitation as cancel_owner_invite,
)
from avant_core.internal.contracts import (
    create_contract,
    delete_contract,
    end_contract,
    get_contract,
    list_contract_networks,
    list_contracts,
    update_contract,
)
from avant_core.money.domain import BASE_CURRENCY
from avant_core.results.application import clients_results
from fastapi import APIRouter, Depends, Query, status

from avant_api.deps import get_services, require_staff
from avant_api.routes.invitations import invitation_out
from avant_api.routes.networks import enqueue_sync
from avant_api.routes.results import default_period
from avant_api.schemas import (
    AssignNetworkIn,
    AuditOut,
    ClientDetailOut,
    ClientIn,
    ClientMemberOut,
    ClientOut,
    ClientPatchIn,
    ClientStatusIn,
    CompanyRefOut,
    ContractIn,
    ContractNetworkOut,
    ContractOut,
    ContractPatchIn,
    InvitationOut,
    ItemsOut,
    McmCandidateOut,
    MemberOut,
    NetworkOut,
    OwnerChangeIn,
    OwnerInvitationOut,
    PersonOut,
    ResultsOut,
    StaffInviteIn,
    UserOut,
)
from avant_api.services import Services

router = APIRouter(prefix="/internal", tags=["internal"])


def _owner_invitation(invitation: Invitation) -> OwnerInvitationOut:
    """Monta a resposta de um convite de dono."""
    return OwnerInvitationOut(
        id=invitation.id,
        company_id=invitation.company_id,
        email=invitation.email,
        status=invitation.status,
        expires_at=invitation.expires_at,
        invited_by=invitation.invited_by,
    )


def _person(person: PersonView) -> PersonOut:
    """Monta a resposta de uma pessoa com as Empresas em que está."""
    user = person.user
    return PersonOut(
        user=UserOut(id=user.id, email=user.email, name=user.name, locale=user.locale),
        status=user.status,
        mfa_enabled=user.mfa_enabled,
        last_login_at=user.last_login_at,
        companies=[
            CompanyRefOut(
                id=company.id, name=company.name, slug=company.slug, is_internal=company.is_internal
            )
            for company in person.companies
        ],
    )


# --- Clientes --------------------------------------------------------------------------


@router.get("/clients")
def clients(
    query: str | None = Query(alias="q", default=None, max_length=120),
    company_status: CompanyStatus | None = Query(default=None, alias="status"),
    actor: Actor = Depends(require_staff("internal.clients.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[ClientOut]:
    """Lista as Empresas de cliente, com busca e filtro de status."""
    items = list_clients(services.trusted_uow(), actor=actor, query=query, status=company_status)
    return ItemsOut(items=[ClientOut.of(client) for client in items])


@router.post("/clients", status_code=status.HTTP_201_CREATED)
def register_client(
    body: ClientIn,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    services: Services = Depends(get_services),
) -> ClientOut:
    """Cadastra o cliente pendente, sem e-mail: o convite de dono sai depois."""
    summary = create_client(
        services.trusted_uow(),
        actor=actor,
        name=body.name,
        seat_limit=body.seat_limit,
        data=body.profile.to_data(),
        clock=services.clock,
    )
    return ClientOut.of(summary)


@router.post("/clients/{company_id}/owner-invitation")
def invite_owner(
    company_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    services: Services = Depends(get_services),
) -> OwnerInvitationOut:
    """Envia ao contato do cadastro o convite de dono; se já houver, manda um link novo."""
    invitation = send_owner_invitation(
        services.trusted_uow(),
        actor=actor,
        company_id=company_id,
        clock=services.clock,
        mailer=services.mailer,
    )
    return _owner_invitation(invitation)


@router.get("/teams")
def client_teams(
    query: str | None = Query(alias="q", default=None, max_length=120),
    company_id: uuid.UUID | None = None,
    actor: Actor = Depends(require_staff("internal.clients.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[ClientMemberOut]:
    """Lista as pessoas das equipes das Empresas cliente, sem a equipe Groone."""
    rows = list_client_teams(
        services.trusted_uow(), actor=actor, query=query, company_id=company_id
    )
    return ItemsOut(
        items=[
            ClientMemberOut(
                **MemberOut.of(row.member).model_dump(),
                company=CompanyRefOut(
                    id=row.company.id,
                    name=row.company.name,
                    slug=row.company.slug,
                    is_internal=row.company.is_internal,
                ),
            )
            for row in rows
        ]
    )


@router.get("/clients/{company_id}")
def client(
    company_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.clients.view")),
    services: Services = Depends(get_services),
) -> ClientDetailOut:
    """Mostra uma Empresa cliente com membros e convites."""
    detail = get_client(services.trusted_uow(), actor=actor, company_id=company_id)
    return ClientDetailOut(
        **ClientOut.of(detail).model_dump(),
        members=[MemberOut.of(member) for member in detail.members],
        invitations=[invitation_out(invitation) for invitation in detail.invitations],
    )


@router.get("/clients/{company_id}/audit")
def audit(
    company_id: uuid.UUID,
    limit: int = Query(default=50, ge=1, le=200),
    cursor: str | None = Query(default=None, max_length=200),
    actor: Actor = Depends(require_staff("internal.clients.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[AuditOut]:
    """Lista a auditoria de uma Empresa cliente."""
    page = client_audit(
        services.trusted_uow(), actor=actor, company_id=company_id, limit=limit, cursor=cursor
    )
    return ItemsOut(
        items=[AuditOut.of(entry) for entry in page.items], next_cursor=page.next_cursor
    )


@router.patch("/clients/{company_id}")
def edit_client(
    company_id: uuid.UUID,
    body: ClientPatchIn,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    services: Services = Depends(get_services),
) -> ClientOut:
    """Muda o nome, o limite de vagas ou o cadastro de uma Empresa cliente (sem os fiscais)."""
    view = update_client(
        services.trusted_uow(),
        actor=actor,
        company_id=company_id,
        clock=services.clock,
        name=body.name,
        seat_limit=body.seat_limit,
        data=body.profile.to_data() if body.profile else None,
    )
    return ClientOut.of(view)


@router.put("/clients/{company_id}/status", status_code=status.HTTP_204_NO_CONTENT)
def change_status(
    company_id: uuid.UUID,
    body: ClientStatusIn,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    services: Services = Depends(get_services),
) -> None:
    """Troca a situação do cliente; as networks acompanham."""
    set_client_status(
        services.trusted_uow(),
        actor=actor,
        company_id=company_id,
        status=body.status,
        clock=services.clock,
    )


@router.post("/clients/{company_id}/owner", status_code=status.HTTP_204_NO_CONTENT)
def new_owner(
    company_id: uuid.UUID,
    body: OwnerChangeIn,
    actor: Actor = Depends(require_staff("internal.owner.change")),
    services: Services = Depends(get_services),
) -> None:
    """Passa a posse de uma Empresa cliente para outro membro."""
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
    """Lista os convites de dono pendentes e vencidos."""
    items = list_owner_invitations(services.trusted_uow(), actor=actor, clock=services.clock)
    return ItemsOut(items=[_owner_invitation(invitation) for invitation in items])


@router.post("/owner-invitations/{invitation_id}/resend")
def resend_owner(
    invitation_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    services: Services = Depends(get_services),
) -> OwnerInvitationOut:
    """Reenvia um convite de dono com validade nova."""
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
    """Cancela um convite de dono."""
    cancel_owner_invite(services.trusted_uow(), actor=actor, invitation_id=invitation_id)


# --- Pessoas ---------------------------------------------------------------------------


@router.get("/users")
def users(
    query: str = Query(alias="q", min_length=3, max_length=120),
    actor: Actor = Depends(require_staff("internal.users.manage")),
    services: Services = Depends(get_services),
) -> ItemsOut[PersonOut]:
    """Busca pessoas por nome ou email."""
    people = search_users(services.trusted_uow(), actor=actor, query=query)
    return ItemsOut(items=[_person(person) for person in people])


@router.post("/users/{user_id}/disable", status_code=status.HTTP_204_NO_CONTENT)
def disable(
    user_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.users.manage")),
    services: Services = Depends(get_services),
) -> None:
    """Desativa a conta de uma pessoa e encerra as sessões dela."""
    set_user_status(
        services.trusted_uow(), actor=actor, user_id=user_id, disabled=True, clock=services.clock
    )


@router.post("/users/{user_id}/enable", status_code=status.HTTP_204_NO_CONTENT)
def enable(
    user_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.users.manage")),
    services: Services = Depends(get_services),
) -> None:
    """Reativa a conta de uma pessoa."""
    set_user_status(
        services.trusted_uow(), actor=actor, user_id=user_id, disabled=False, clock=services.clock
    )


@router.post("/users/{user_id}/reset-mfa", status_code=status.HTTP_204_NO_CONTENT)
def reset_mfa(
    user_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.users.manage")),
    services: Services = Depends(get_services),
) -> None:
    """Desliga o 2FA de uma pessoa que perdeu o acesso."""
    reset_user_mfa(
        services.trusted_uow(),
        actor=actor,
        user_id=user_id,
        clock=services.clock,
        mailer=services.mailer,
    )


# --- Equipe Groone ---------------------------------------------------------------------


@router.get("/staff")
def staff(
    actor: Actor = Depends(require_staff("internal.staff.manage")),
    services: Services = Depends(get_services),
) -> ItemsOut[MemberOut]:
    """Lista a equipe Groone."""
    return ItemsOut(
        items=[MemberOut.of(member) for member in list_staff(services.trusted_uow(), actor=actor)]
    )


@router.post("/staff/invitations", status_code=status.HTTP_201_CREATED)
def invite(
    body: StaffInviteIn,
    actor: Actor = Depends(require_staff("internal.staff.manage")),
    services: Services = Depends(get_services),
) -> InvitationOut:
    """Convida alguém para a equipe Groone com um papel interno."""
    invitation = invite_staff(
        services.trusted_uow(),
        actor=actor,
        email=body.email,
        role_id=body.role_id,
        clock=services.clock,
        mailer=services.mailer,
    )
    return invitation_out(invitation)


# --- MCM sem dono ----------------------------------------------------------------------


@router.get("/networks/unassigned")
def unassigned_networks(
    actor: Actor = Depends(require_staff("internal.networks.assign")),
    services: Services = Depends(get_services),
) -> ItemsOut[McmCandidateOut]:
    """Networks MCM aprovadas cujo e-mail não é dono de nenhuma Empresa."""
    candidates = list_mcm_candidates(services.trusted_uow(), actor=actor)
    return ItemsOut(items=[McmCandidateOut.of(candidate) for candidate in candidates])


@router.post("/networks/{candidate_id}/assign", status_code=status.HTTP_202_ACCEPTED)
def assign_network(
    candidate_id: uuid.UUID,
    body: AssignNetworkIn,
    actor: Actor = Depends(require_staff("internal.networks.assign")),
    services: Services = Depends(get_services),
) -> NetworkOut:
    """Liga uma network do MCM a uma Empresa e agenda a primeira sincronização."""
    network = assign_mcm_candidate(
        services.trusted_uow(),
        actor=actor,
        candidate_id=candidate_id,
        company_id=body.company_id,
        clock=services.clock,
    )
    enqueue_sync(services, network)
    return NetworkOut.of(network)


# --- Resultado dos clientes ------------------------------------------------------------


@router.get("/results")
def results(
    start: date | None = None,
    end: date | None = None,
    currency: str = Query(default=BASE_CURRENCY, min_length=3, max_length=3),
    actor: Actor = Depends(require_staff("internal.results.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[ResultsOut]:
    """O resultado de cada Empresa cliente no período, por nome."""
    first, last = default_period(start, end, services.clock.now().date())
    items = clients_results(
        services.trusted_uow(),
        actor=actor,
        start=first,
        end=last,
        currency=currency,
        clock=services.clock,
    )
    return ItemsOut(items=[ResultsOut.of(item) for item in items])


# --- Contratos -------------------------------------------------------------------------


@router.get("/contracts")
def contracts(
    company_id: uuid.UUID | None = None,
    network_id: uuid.UUID | None = None,
    contract_status: ContractStatus | None = Query(default=None, alias="status"),
    actor: Actor = Depends(require_staff("internal.contracts.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[ContractOut]:
    """Lista os contratos, do mais novo para o mais antigo, com filtros."""
    views = list_contracts(
        services.trusted_uow(),
        actor=actor,
        company_id=company_id,
        network_id=network_id,
        status=contract_status,
    )
    return ItemsOut(items=[ContractOut.of(view) for view in views])


@router.get("/contracts/networks")
def contract_networks(
    actor: Actor = Depends(require_staff("internal.contracts.view")),
    services: Services = Depends(get_services),
) -> ItemsOut[ContractNetworkOut]:
    """Networks MCM ativas com o contrato em vigor e se aceitam contrato à mão."""
    views = list_contract_networks(services.trusted_uow(), actor=actor)
    return ItemsOut(items=[ContractNetworkOut.of(view) for view in views])


@router.get("/contracts/{contract_id}")
def contract(
    contract_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.contracts.view")),
    services: Services = Depends(get_services),
) -> ContractOut:
    """Mostra um contrato."""
    return ContractOut.of(
        get_contract(services.trusted_uow(), actor=actor, contract_id=contract_id)
    )


@router.post("/contracts", status_code=status.HTTP_201_CREATED)
def new_contract(
    body: ContractIn,
    actor: Actor = Depends(require_staff("internal.contracts.create")),
    services: Services = Depends(get_services),
) -> ContractOut:
    """Contrato à mão de uma network Manage Inventory; encerra o ativo, se houver."""
    view = create_contract(
        services.trusted_uow(),
        actor=actor,
        network_id=body.network_id,
        revshare=body.revshare,
        notes=body.notes,
        clock=services.clock,
    )
    return ContractOut.of(view)


@router.patch("/contracts/{contract_id}")
def edit_contract(
    contract_id: uuid.UUID,
    body: ContractPatchIn,
    actor: Actor = Depends(require_staff("internal.contracts.update")),
    services: Services = Depends(get_services),
) -> ContractOut:
    """Edita a observação; o revshare de um contrato nunca muda."""
    view = update_contract(
        services.trusted_uow(),
        actor=actor,
        contract_id=contract_id,
        notes=body.notes,
        clock=services.clock,
    )
    return ContractOut.of(view)


@router.post("/contracts/{contract_id}/end")
def finish_contract(
    contract_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.contracts.update")),
    services: Services = Depends(get_services),
) -> ContractOut:
    """Encerra um contrato feito à mão."""
    view = end_contract(
        services.trusted_uow(), actor=actor, contract_id=contract_id, clock=services.clock
    )
    return ContractOut.of(view)


@router.delete("/contracts/{contract_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_contract(
    contract_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.contracts.delete")),
    services: Services = Depends(get_services),
) -> None:
    """Exclui um contrato feito à mão (cadastro errado)."""
    delete_contract(
        services.trusted_uow(), actor=actor, contract_id=contract_id, clock=services.clock
    )
