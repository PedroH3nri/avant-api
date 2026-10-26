"""Empresa ativa: /api/v1/company."""

from avant_core.company.application import Actor
from avant_core.company.team import (
    get_company,
    get_fiscal_data,
    update_company,
    update_fiscal_data,
)
from fastapi import APIRouter, Depends

from avant_api.deps import get_actor, get_services, require
from avant_api.schemas import CompanyDetailOut, CompanyFiscalOut, CompanyPatchIn, FiscalDataIn
from avant_api.services import Services

router = APIRouter(prefix="/company", tags=["company"])


@router.get("")
def show(
    actor: Actor = Depends(get_actor), services: Services = Depends(get_services)
) -> CompanyDetailOut:
    """Qualquer membro ativo: nome, cor e vagas."""
    return CompanyDetailOut.of(get_company(services.uow(actor.company_id), actor=actor))


@router.patch("")
def edit(
    body: CompanyPatchIn,
    actor: Actor = Depends(require("company.edit")),
    services: Services = Depends(get_services),
) -> CompanyDetailOut:
    """Muda nome, cor ou configurações da Empresa ativa."""
    view = update_company(
        services.uow(actor.company_id),
        actor=actor,
        clock=services.clock,
        name=body.name,
        accent_color=body.accent_color,
        settings=body.settings,
    )
    return CompanyDetailOut.of(view)


@router.get("/fiscal")
def fiscal(
    actor: Actor = Depends(require("company.edit")),
    services: Services = Depends(get_services),
) -> CompanyFiscalOut:
    """Contato do cadastro e dados fiscais de pagamento da Empresa cliente."""
    return CompanyFiscalOut.of(get_fiscal_data(services.uow(actor.company_id), actor=actor))


@router.put("/fiscal")
def edit_fiscal(
    body: FiscalDataIn,
    actor: Actor = Depends(require("company.edit")),
    services: Services = Depends(get_services),
) -> CompanyFiscalOut:
    """Só o cliente grava os dados fiscais de pagamento, todos juntos."""
    profile = update_fiscal_data(
        services.uow(actor.company_id), actor=actor, data=body.to_data(), clock=services.clock
    )
    return CompanyFiscalOut.of(profile)
