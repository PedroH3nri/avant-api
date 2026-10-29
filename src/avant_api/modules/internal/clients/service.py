"""Service dos clientes no painel interno: cadastro, equipes, situação, dono e convites.

Usa ``trusted_uow()`` (sem RLS) porque a Groone enxerga todas as Empresas; o core confere
``ensure_staff`` em cada caso de uso.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.company.enums import CompanyStatus
from avant_core.company.models import CompanyImage, Invitation
from avant_core.internal.services import cancel_owner_invitation as cancel_owner_invite
from avant_core.internal.services import (
    change_owner,
    create_client,
    get_client,
    get_client_image,
    list_clients,
    page_client_audit,
    page_client_teams,
    page_clients,
    page_owner_invitations,
    remove_client_image,
    resend_owner_invitation,
    send_owner_invitation,
    set_client_image,
    set_client_status,
    update_client,
)
from avant_core.ports import ImageProcessor, Mailer
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.internal.clients.dto import (
    ClientDetailOut,
    ClientIn,
    ClientMemberOut,
    ClientOptionOut,
    ClientOut,
    ClientPatchIn,
    OwnerInvitationOut,
)
from avant_api.shared.dto import (
    AuditOut,
    CompanyRefOut,
    InvitationOut,
    MemberOut,
    PageOut,
    page_out,
)


def owner_invitation_out(invitation: Invitation) -> OwnerInvitationOut:
    """Monta a resposta de um convite de dono."""
    return OwnerInvitationOut(
        id=invitation.id,
        company_id=invitation.company_id,
        email=invitation.email,
        status=invitation.status,
        expires_at=invitation.expires_at,
        invited_by=invitation.invited_by,
    )


class ClientService:
    """Empresas cliente vistas pela equipe Groone."""

    def __init__(
        self, uows: UnitOfWorkFactory, clock: Clock, mailer: Mailer, images: ImageProcessor
    ) -> None:
        self._uows = uows
        self._clock = clock
        self._mailer = mailer
        self._images = images

    def page(
        self, actor: Actor, query: str | None, status: CompanyStatus | None, page: int
    ) -> PageOut[ClientOut]:
        """Uma página das Empresas de cliente, a mais recente primeiro, com busca e status."""
        found = page_clients(
            self._uows.trusted_uow(), actor=actor, query=query, status=status, page=page
        )
        return page_out(found, ClientOut.of)

    def options(self, actor: Actor) -> list[ClientOptionOut]:
        """Todas as Empresas de cliente, pelo nome, para seletores."""
        items = list_clients(self._uows.trusted_uow(), actor=actor)
        return [ClientOptionOut(id=item.company.id, name=item.company.name) for item in items]

    def register(self, actor: Actor, body: ClientIn) -> ClientOut:
        """Cadastra o cliente pendente, sem e-mail: o convite de dono sai depois."""
        summary = create_client(
            self._uows.trusted_uow(),
            actor=actor,
            name=body.name,
            seat_limit=body.seat_limit,
            data=body.profile.to_data(),
            clock=self._clock,
        )
        return ClientOut.of(summary)

    def invite_owner(self, actor: Actor, company_id: uuid.UUID) -> OwnerInvitationOut:
        """Envia ao contato do cadastro o convite de dono, ou um link novo."""
        invitation = send_owner_invitation(
            self._uows.trusted_uow(),
            actor=actor,
            company_id=company_id,
            clock=self._clock,
            mailer=self._mailer,
        )
        return owner_invitation_out(invitation)

    def teams(
        self, actor: Actor, query: str | None, company_id: uuid.UUID | None, page: int
    ) -> PageOut[ClientMemberOut]:
        """Uma página das pessoas das equipes das Empresas cliente, a mais recente primeiro."""
        found = page_client_teams(
            self._uows.trusted_uow(), actor=actor, query=query, company_id=company_id, page=page
        )
        return page_out(
            found,
            lambda row: ClientMemberOut(
                **MemberOut.of(row.member).model_dump(),
                company=CompanyRefOut(
                    id=row.company.id,
                    name=row.company.name,
                    slug=row.company.slug,
                    is_internal=row.company.is_internal,
                ),
            ),
        )

    def show(self, actor: Actor, company_id: uuid.UUID) -> ClientDetailOut:
        """Uma Empresa cliente com membros e convites."""
        detail = get_client(self._uows.trusted_uow(), actor=actor, company_id=company_id)
        return ClientDetailOut(
            **ClientOut.of(detail).model_dump(),
            members=[MemberOut.of(member) for member in detail.members],
            invitations=[InvitationOut.of(invitation) for invitation in detail.invitations],
        )

    def audit(self, actor: Actor, company_id: uuid.UUID, page: int) -> PageOut[AuditOut]:
        """Uma página numerada da auditoria de uma Empresa cliente, a mais nova primeiro."""
        found = page_client_audit(
            self._uows.trusted_uow(), actor=actor, company_id=company_id, page=page
        )
        return page_out(found, AuditOut.of)

    def update(self, actor: Actor, company_id: uuid.UUID, body: ClientPatchIn) -> ClientOut:
        """Muda o nome, o limite de vagas ou o cadastro (sem os dados fiscais)."""
        view = update_client(
            self._uows.trusted_uow(),
            actor=actor,
            company_id=company_id,
            clock=self._clock,
            name=body.name,
            seat_limit=body.seat_limit,
            data=body.profile.to_data() if body.profile else None,
        )
        return ClientOut.of(view)

    def image(self, actor: Actor, company_id: uuid.UUID) -> CompanyImage:
        """Imagem de uma Empresa cliente."""
        return get_client_image(self._uows.trusted_uow(), actor=actor, company_id=company_id)

    def set_image(self, actor: Actor, company_id: uuid.UUID, content: bytes) -> ClientOut:
        """Troca a imagem de uma Empresa cliente e devolve o cliente com a URL nova."""
        set_client_image(
            self._uows.trusted_uow(),
            actor=actor,
            company_id=company_id,
            content=content,
            images=self._images,
            clock=self._clock,
        )
        return self.show(actor, company_id)

    def remove_image(self, actor: Actor, company_id: uuid.UUID) -> ClientOut:
        """Tira a imagem de uma Empresa cliente."""
        remove_client_image(
            self._uows.trusted_uow(), actor=actor, company_id=company_id, clock=self._clock
        )
        return self.show(actor, company_id)

    def set_status(self, actor: Actor, company_id: uuid.UUID, status: CompanyStatus) -> None:
        """Troca a situação do cliente; as networks acompanham."""
        set_client_status(
            self._uows.trusted_uow(),
            actor=actor,
            company_id=company_id,
            status=status,
            clock=self._clock,
        )

    def change_owner(self, actor: Actor, company_id: uuid.UUID, membership_id: uuid.UUID) -> None:
        """Passa a posse de uma Empresa cliente para outro membro."""
        change_owner(
            self._uows.trusted_uow(),
            actor=actor,
            company_id=company_id,
            membership_id=membership_id,
            clock=self._clock,
        )

    def owner_invitations(self, actor: Actor, page: int) -> PageOut[OwnerInvitationOut]:
        """Uma página dos convites de dono pendentes e vencidos."""
        found = page_owner_invitations(
            self._uows.trusted_uow(), actor=actor, clock=self._clock, page=page
        )
        return page_out(found, owner_invitation_out)

    def resend_owner(self, actor: Actor, invitation_id: uuid.UUID) -> OwnerInvitationOut:
        """Reenvia um convite de dono com validade nova."""
        invitation = resend_owner_invitation(
            self._uows.trusted_uow(),
            actor=actor,
            invitation_id=invitation_id,
            clock=self._clock,
            mailer=self._mailer,
        )
        return owner_invitation_out(invitation)

    def cancel_owner(self, actor: Actor, invitation_id: uuid.UUID) -> None:
        """Cancela um convite de dono."""
        cancel_owner_invite(self._uows.trusted_uow(), actor=actor, invitation_id=invitation_id)
