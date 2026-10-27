"""Clientes, equipes dos clientes e convites de dono: /api/v1/internal.

A proteção fica em duas camadas: ``require_staff`` aqui (Company Groone ativa, 2FA
verificado na sessão e a permissão) e, no core, ``ensure_staff`` em cada caso de uso.
"""

import uuid

from avant_core.company.model import CompanyStatus
from avant_core.company.service import Actor
from fastapi import APIRouter, Depends, Query, Request, Response, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.clients.dependencies import client_service
from avant_api.modules.internal.clients.dto import (
    ClientDetailOut,
    ClientIn,
    ClientMemberOut,
    ClientOut,
    ClientPatchIn,
    ClientStatusIn,
    OwnerChangeIn,
    OwnerInvitationOut,
)
from avant_api.modules.internal.clients.service import ClientService
from avant_api.shared.dto import AuditOut, ItemsOut
from avant_api.shared.http import image_response, image_upload

router = APIRouter(prefix="/internal", tags=["internal"])


@router.get("/clients")
def clients(
    query: str | None = Query(alias="q", default=None, max_length=120),
    company_status: CompanyStatus | None = Query(default=None, alias="status"),
    actor: Actor = Depends(require_staff("internal.clients.view")),
    service: ClientService = Depends(client_service),
) -> ItemsOut[ClientOut]:
    """Lista as Empresas de cliente, com busca e filtro de status."""
    return ItemsOut(items=service.list_all(actor, query, company_status))


@router.post("/clients", status_code=status.HTTP_201_CREATED)
def register_client(
    body: ClientIn,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    service: ClientService = Depends(client_service),
) -> ClientOut:
    """Cadastra o cliente pendente, sem e-mail: o convite de dono sai depois."""
    return service.register(actor, body)


@router.post("/clients/{company_id}/owner-invitation")
def invite_owner(
    company_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    service: ClientService = Depends(client_service),
) -> OwnerInvitationOut:
    """Envia ao contato do cadastro o convite de dono; se já houver, manda um link novo."""
    return service.invite_owner(actor, company_id)


@router.get("/teams")
def client_teams(
    query: str | None = Query(alias="q", default=None, max_length=120),
    company_id: uuid.UUID | None = None,
    actor: Actor = Depends(require_staff("internal.clients.view")),
    service: ClientService = Depends(client_service),
) -> ItemsOut[ClientMemberOut]:
    """Lista as pessoas das equipes das Empresas cliente, sem a equipe Groone."""
    return ItemsOut(items=service.teams(actor, query, company_id))


@router.get("/clients/{company_id}")
def client(
    company_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.clients.view")),
    service: ClientService = Depends(client_service),
) -> ClientDetailOut:
    """Mostra uma Empresa cliente com membros e convites."""
    return service.show(actor, company_id)


@router.get("/clients/{company_id}/audit")
def audit(
    company_id: uuid.UUID,
    limit: int = Query(default=50, ge=1, le=200),
    cursor: str | None = Query(default=None, max_length=200),
    actor: Actor = Depends(require_staff("internal.clients.view")),
    service: ClientService = Depends(client_service),
) -> ItemsOut[AuditOut]:
    """Lista a auditoria de uma Empresa cliente."""
    return service.audit(actor, company_id, limit, cursor)


@router.patch("/clients/{company_id}")
def edit_client(
    company_id: uuid.UUID,
    body: ClientPatchIn,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    service: ClientService = Depends(client_service),
) -> ClientOut:
    """Muda o nome, o limite de vagas ou o cadastro de uma Empresa cliente (sem os fiscais)."""
    return service.update(actor, company_id, body)


@router.get("/clients/{company_id}/image", response_class=Response)
def client_image(
    company_id: uuid.UUID,
    request: Request,
    actor: Actor = Depends(require_staff("internal.clients.view")),
    service: ClientService = Depends(client_service),
) -> Response:
    """Imagem de uma Empresa cliente em WebP, com cache pela URL versionada."""
    return image_response(request, service.image(actor, company_id))


@router.put("/clients/{company_id}/image")
def edit_client_image(
    company_id: uuid.UUID,
    content: bytes = Depends(image_upload),
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    service: ClientService = Depends(client_service),
) -> ClientOut:
    """Troca a imagem de uma Empresa cliente: o corpo é o arquivo de até 2 MB."""
    return service.set_image(actor, company_id, content)


@router.delete("/clients/{company_id}/image")
def remove_client_image(
    company_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    service: ClientService = Depends(client_service),
) -> ClientOut:
    """Tira a imagem de uma Empresa cliente."""
    return service.remove_image(actor, company_id)


@router.put("/clients/{company_id}/status", status_code=status.HTTP_204_NO_CONTENT)
def change_status(
    company_id: uuid.UUID,
    body: ClientStatusIn,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    service: ClientService = Depends(client_service),
) -> None:
    """Troca a situação do cliente; as networks acompanham."""
    service.set_status(actor, company_id, body.status)


@router.post("/clients/{company_id}/owner", status_code=status.HTTP_204_NO_CONTENT)
def new_owner(
    company_id: uuid.UUID,
    body: OwnerChangeIn,
    actor: Actor = Depends(require_staff("internal.owner.change")),
    service: ClientService = Depends(client_service),
) -> None:
    """Passa a posse de uma Empresa cliente para outro membro."""
    service.change_owner(actor, company_id, body.membership_id)


@router.get("/owner-invitations")
def owner_invitations(
    actor: Actor = Depends(require_staff("internal.clients.view")),
    service: ClientService = Depends(client_service),
) -> ItemsOut[OwnerInvitationOut]:
    """Lista os convites de dono pendentes e vencidos."""
    return ItemsOut(items=service.owner_invitations(actor))


@router.post("/owner-invitations/{invitation_id}/resend")
def resend_owner(
    invitation_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    service: ClientService = Depends(client_service),
) -> OwnerInvitationOut:
    """Reenvia um convite de dono com validade nova."""
    return service.resend_owner(actor, invitation_id)


@router.delete("/owner-invitations/{invitation_id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel_owner(
    invitation_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.clients.manage")),
    service: ClientService = Depends(client_service),
) -> None:
    """Cancela um convite de dono."""
    service.cancel_owner(actor, invitation_id)
