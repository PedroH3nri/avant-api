"""Contratos de revshare: /api/v1/internal/contracts."""

import uuid

from avant_core.access.models import Actor
from avant_core.gam.contracts.enums import ContractStatus
from fastapi import APIRouter, Depends, Query, status

from avant_api.app.security import require_staff
from avant_api.modules.internal.contracts.dependencies import contract_service
from avant_api.modules.internal.contracts.dto import (
    ContractIn,
    ContractNetworkOut,
    ContractOut,
    ContractPatchIn,
)
from avant_api.modules.internal.contracts.service import ContractService
from avant_api.shared.dto import ItemsOut, PageOut

router = APIRouter(prefix="/internal/contracts", tags=["internal"])


@router.get("")
def contracts(
    company_id: uuid.UUID | None = None,
    network_id: uuid.UUID | None = None,
    contract_status: ContractStatus | None = Query(default=None, alias="status"),
    page: int = Query(default=1, ge=1),
    actor: Actor = Depends(require_staff("internal.contracts.view")),
    service: ContractService = Depends(contract_service),
) -> PageOut[ContractOut]:
    """Uma página dos contratos, do mais novo para o mais antigo, com filtros."""
    return service.list_all(actor, company_id, network_id, contract_status, page)


@router.get("/networks")
def contract_networks(
    actor: Actor = Depends(require_staff("internal.contracts.view")),
    service: ContractService = Depends(contract_service),
) -> ItemsOut[ContractNetworkOut]:
    """Networks MCM ativas com o contrato em vigor e se aceitam contrato à mão."""
    return ItemsOut(items=service.networks(actor))


@router.get("/{contract_id}")
def contract(
    contract_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.contracts.view")),
    service: ContractService = Depends(contract_service),
) -> ContractOut:
    """Mostra um contrato."""
    return service.show(actor, contract_id)


@router.post("", status_code=status.HTTP_201_CREATED)
def new_contract(
    body: ContractIn,
    actor: Actor = Depends(require_staff("internal.contracts.create")),
    service: ContractService = Depends(contract_service),
) -> ContractOut:
    """Contrato à mão de uma network Manage Inventory; encerra o ativo, se houver."""
    return service.create(actor, body)


@router.patch("/{contract_id}")
def edit_contract(
    contract_id: uuid.UUID,
    body: ContractPatchIn,
    actor: Actor = Depends(require_staff("internal.contracts.update")),
    service: ContractService = Depends(contract_service),
) -> ContractOut:
    """Edita a observação; o revshare de um contrato nunca muda."""
    return service.update(actor, contract_id, body)


@router.post("/{contract_id}/end")
def finish_contract(
    contract_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.contracts.update")),
    service: ContractService = Depends(contract_service),
) -> ContractOut:
    """Encerra um contrato feito à mão."""
    return service.end(actor, contract_id)


@router.delete("/{contract_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_contract(
    contract_id: uuid.UUID,
    actor: Actor = Depends(require_staff("internal.contracts.delete")),
    service: ContractService = Depends(contract_service),
) -> None:
    """Exclui um contrato feito à mão (cadastro errado)."""
    service.delete(actor, contract_id)
