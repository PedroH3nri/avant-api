"""Service da Empresa ativa: dados, cor, imagem, configurações e dados fiscais."""

from avant_core.access.models import Actor
from avant_core.company.models import CompanyImage
from avant_core.company.services import (
    get_company,
    get_company_image,
    get_fiscal_data,
    remove_company_image,
    set_company_image,
    update_company,
    update_fiscal_data,
)
from avant_core.ports import ImageProcessor
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.company.dto import (
    CompanyDetailOut,
    CompanyFiscalOut,
    CompanyPatchIn,
    FiscalDataIn,
)


class CompanyService:
    """A Empresa ativa de quem age."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, images: ImageProcessor) -> None:
        self._uows = uows
        self._clock = clock
        self._images = images

    def show(self, actor: Actor) -> CompanyDetailOut:
        """Nome, cor e vagas da Empresa ativa."""
        return CompanyDetailOut.of(get_company(self._uows.uow(actor.company_id), actor=actor))

    def update(self, actor: Actor, body: CompanyPatchIn) -> CompanyDetailOut:
        """Muda nome, cor ou configurações da Empresa ativa."""
        view = update_company(
            self._uows.uow(actor.company_id),
            actor=actor,
            clock=self._clock,
            name=body.name,
            settings=body.settings,
        )
        return CompanyDetailOut.of(view)

    def image(self, actor: Actor) -> CompanyImage:
        """Imagem da Empresa ativa."""
        return get_company_image(
            self._uows.uow(actor.company_id), user_id=actor.user_id, company_id=actor.company_id
        )

    def set_image(self, actor: Actor, content: bytes) -> CompanyDetailOut:
        """Troca a imagem da Empresa ativa e devolve a Empresa com a URL nova."""
        set_company_image(
            self._uows.uow(actor.company_id),
            actor=actor,
            content=content,
            images=self._images,
            clock=self._clock,
        )
        return self.show(actor)

    def remove_image(self, actor: Actor) -> CompanyDetailOut:
        """Tira a imagem da Empresa ativa."""
        remove_company_image(self._uows.uow(actor.company_id), actor=actor, clock=self._clock)
        return self.show(actor)

    def fiscal(self, actor: Actor) -> CompanyFiscalOut:
        """Contato do cadastro e dados fiscais de pagamento da Empresa cliente."""
        return CompanyFiscalOut.of(get_fiscal_data(self._uows.uow(actor.company_id), actor=actor))

    def update_fiscal(self, actor: Actor, body: FiscalDataIn) -> CompanyFiscalOut:
        """Grava os dados fiscais de pagamento, todos juntos."""
        profile = update_fiscal_data(
            self._uows.uow(actor.company_id), actor=actor, data=body.to_data(), clock=self._clock
        )
        return CompanyFiscalOut.of(profile)
