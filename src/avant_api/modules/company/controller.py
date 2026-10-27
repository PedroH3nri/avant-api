"""Empresa ativa: /api/v1/company."""

from avant_core.company.service import Actor
from fastapi import APIRouter, Depends

from avant_api.app.security import get_actor, require
from avant_api.modules.company.dependencies import company_service
from avant_api.modules.company.dto import (
    CompanyDetailOut,
    CompanyFiscalOut,
    CompanyPatchIn,
    FiscalDataIn,
)
from avant_api.modules.company.service import CompanyService

router = APIRouter(prefix="/company", tags=["company"])


@router.get("")
def show(
    actor: Actor = Depends(get_actor), service: CompanyService = Depends(company_service)
) -> CompanyDetailOut:
    """Qualquer membro ativo: nome, cor e vagas."""
    return service.show(actor)


@router.patch("")
def edit(
    body: CompanyPatchIn,
    actor: Actor = Depends(require("company.edit")),
    service: CompanyService = Depends(company_service),
) -> CompanyDetailOut:
    """Muda nome, cor ou configurações da Empresa ativa."""
    return service.update(actor, body)


@router.get("/fiscal")
def fiscal(
    actor: Actor = Depends(require("company.edit")),
    service: CompanyService = Depends(company_service),
) -> CompanyFiscalOut:
    """Contato do cadastro e dados fiscais de pagamento da Empresa cliente."""
    return service.fiscal(actor)


@router.put("/fiscal")
def edit_fiscal(
    body: FiscalDataIn,
    actor: Actor = Depends(require("company.edit")),
    service: CompanyService = Depends(company_service),
) -> CompanyFiscalOut:
    """Só o cliente grava os dados fiscais de pagamento, todos juntos."""
    return service.update_fiscal(actor, body)
