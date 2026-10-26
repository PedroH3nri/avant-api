"""Service da Empresa ativa: dados, cor, configurações e dados fiscais."""

from avant_core.company.application import Actor
from avant_core.company.team import (
    get_company,
    get_fiscal_data,
    update_company,
    update_fiscal_data,
)
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

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

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
            accent_color=body.accent_color,
            settings=body.settings,
        )
        return CompanyDetailOut.of(view)

    def fiscal(self, actor: Actor) -> CompanyFiscalOut:
        """Contato do cadastro e dados fiscais de pagamento da Empresa cliente."""
        return CompanyFiscalOut.of(get_fiscal_data(self._uows.uow(actor.company_id), actor=actor))

    def update_fiscal(self, actor: Actor, body: FiscalDataIn) -> CompanyFiscalOut:
        """Grava os dados fiscais de pagamento, todos juntos."""
        profile = update_fiscal_data(
            self._uows.uow(actor.company_id), actor=actor, data=body.to_data(), clock=self._clock
        )
        return CompanyFiscalOut.of(profile)
