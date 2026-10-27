"""Empresa ativa: /api/v1/company."""

from avant_core.company.service import Actor
from fastapi import APIRouter, Depends, Request, Response

from avant_api.app.security import get_actor, require
from avant_api.modules.company.dependencies import company_service
from avant_api.modules.company.dto import (
    CompanyDetailOut,
    CompanyFiscalOut,
    CompanyPatchIn,
    FiscalDataIn,
)
from avant_api.modules.company.service import CompanyService
from avant_api.shared.http import image_response, image_upload

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


@router.get("/image", response_class=Response)
def image(
    request: Request,
    actor: Actor = Depends(get_actor),
    service: CompanyService = Depends(company_service),
) -> Response:
    """Qualquer membro ativo: a imagem da Empresa em WebP, com cache pela URL versionada."""
    return image_response(request, service.image(actor))


@router.put("/image")
def edit_image(
    content: bytes = Depends(image_upload),
    actor: Actor = Depends(require("company.edit")),
    service: CompanyService = Depends(company_service),
) -> CompanyDetailOut:
    """Troca a imagem: o corpo é o arquivo PNG, JPEG ou WebP de até 2 MB."""
    return service.set_image(actor, content)


@router.delete("/image")
def remove_image(
    actor: Actor = Depends(require("company.edit")),
    service: CompanyService = Depends(company_service),
) -> CompanyDetailOut:
    """Tira a imagem da Empresa ativa."""
    return service.remove_image(actor)


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
