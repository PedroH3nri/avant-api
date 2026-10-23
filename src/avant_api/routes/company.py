"""Empresa ativa: /api/v1/company."""

from avant_core.company.application import Actor
from avant_core.company.team import get_company, update_company
from fastapi import APIRouter, Depends

from avant_api.deps import get_actor, get_services, require
from avant_api.schemas import CompanyDetailOut, CompanyPatchIn
from avant_api.services import Services

router = APIRouter(prefix="/company", tags=["company"])


@router.get("")
def show(
    actor: Actor = Depends(get_actor), services: Services = Depends(get_services)
) -> CompanyDetailOut:
    """Qualquer membro ativo: nome, cor, plano e vagas."""
    return CompanyDetailOut.of(get_company(services.uow(actor.company_id), actor=actor))


@router.patch("")
def edit(
    body: CompanyPatchIn,
    actor: Actor = Depends(require("company.edit")),
    services: Services = Depends(get_services),
) -> CompanyDetailOut:
    view = update_company(
        services.uow(actor.company_id),
        actor=actor,
        clock=services.clock,
        name=body.name,
        accent_color=body.accent_color,
        settings=body.settings,
    )
    return CompanyDetailOut.of(view)
