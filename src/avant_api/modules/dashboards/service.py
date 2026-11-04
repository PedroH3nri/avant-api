"""Service dos dashboards: listar, editar, o padrão e rodar cada widget pelo motor do core.

Rodar um widget segue as regras das consultas de relatório: o mesmo limite de taxa por pessoa e
Empresa, o tempo máximo do Postgres e, na Company Groone, um Unit of Work sem RLS
(``trusted_uow``), porque a soma passa por todas as Empresas cliente que a pessoa vê.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.dashboards.models import Dashboard
from avant_core.dashboards.services import (
    choose_my_dashboard,
    create_dashboard,
    create_from_template,
    delete_dashboard,
    duplicate_dashboard,
    get_dashboard,
    home_dashboard,
    home_template,
    list_dashboard_templates,
    page_dashboards,
    run_dashboard,
    run_template,
    run_template_widget,
    run_widget,
    set_company_default,
    update_dashboard,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.dashboards.dto import (
    DashboardIn,
    DashboardOut,
    DashboardPageOut,
    DashboardRunOut,
    DashboardTemplateOut,
    HomeDashboardOut,
    WidgetRunIn,
)
from avant_api.modules.reports.dto import ReportResultOut
from avant_api.modules.reports.service import ReportService

MANAGE = "dashboards.manage"


class DashboardService:
    """Dashboards da Empresa ativa; as consultas dos widgets passam pelo service dos relatórios."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, reports: ReportService) -> None:
        self._uows = uows
        self._clock = clock
        self._reports = reports

    def page(self, actor: Actor, query: str | None, page: int) -> DashboardPageOut:
        """Uma página dos dashboards que a pessoa vê, o padrão primeiro."""
        found = page_dashboards(
            self._uows.uow(actor.company_id), actor=actor, query=query, page=page
        )
        return DashboardPageOut(
            items=[self._out(actor, item) for item in found.page.items],
            total=found.page.total,
            page=found.page.page,
            pages=found.page.pages,
            page_size=found.page.page_size,
            default_id=found.default_id,
            chosen_id=found.chosen_id,
        )

    def get(self, actor: Actor, dashboard_id: uuid.UUID) -> DashboardOut:
        """Um dashboard que a pessoa vê."""
        found = get_dashboard(
            self._uows.uow(actor.company_id), actor=actor, dashboard_id=dashboard_id
        )
        return self._out(actor, found)

    def home(self, actor: Actor) -> HomeDashboardOut:
        """O dashboard que abre para a pessoa (o escolhido, senão o padrão da Empresa); sem
        nenhum, o modelo de início do público dela."""
        found = home_dashboard(self._uows.uow(actor.company_id), actor=actor)
        if found is not None:
            return HomeDashboardOut(dashboard=self._out(actor, found))
        template = home_template(self._uows.uow(actor.company_id), actor=actor)
        return HomeDashboardOut(
            dashboard=None, template=DashboardTemplateOut.of(template) if template else None
        )

    def choose(self, actor: Actor, dashboard_id: uuid.UUID | None) -> None:
        """Guarda o dashboard que a pessoa quer abrir, ou volta para o padrão."""
        choose_my_dashboard(
            self._uows.uow(actor.company_id),
            actor=actor,
            dashboard_id=dashboard_id,
            clock=self._clock,
        )

    def set_default(self, actor: Actor, dashboard_id: uuid.UUID | None) -> None:
        """Marca o dashboard padrão da Empresa, ou tira o padrão."""
        set_company_default(
            self._uows.uow(actor.company_id),
            actor=actor,
            dashboard_id=dashboard_id,
            clock=self._clock,
        )

    def create(self, actor: Actor, body: DashboardIn) -> DashboardOut:
        """Salva um dashboard novo, de quem cria."""
        created = create_dashboard(
            self._uows.uow(actor.company_id), actor=actor, data=body.input(), clock=self._clock
        )
        return self._out(actor, created)

    def update(self, actor: Actor, dashboard_id: uuid.UUID, body: DashboardIn) -> DashboardOut:
        """Troca tudo do dashboard, menos o dono."""
        updated = update_dashboard(
            self._uows.uow(actor.company_id),
            actor=actor,
            dashboard_id=dashboard_id,
            data=body.input(),
            clock=self._clock,
        )
        return self._out(actor, updated)

    def delete(self, actor: Actor, dashboard_id: uuid.UUID) -> None:
        """Apaga um dashboard que a pessoa pode editar."""
        delete_dashboard(
            self._uows.uow(actor.company_id),
            actor=actor,
            dashboard_id=dashboard_id,
            clock=self._clock,
        )

    def duplicate(self, actor: Actor, dashboard_id: uuid.UUID) -> DashboardOut:
        """Faz uma cópia privada, da pessoa, de um dashboard que ela vê."""
        copy = duplicate_dashboard(
            self._uows.uow(actor.company_id),
            actor=actor,
            dashboard_id=dashboard_id,
            clock=self._clock,
        )
        return self._out(actor, copy)

    def templates(self, actor: Actor) -> list[DashboardTemplateOut]:
        """Os modelos prontos que a pessoa vê, pelo público da Empresa e pelo papel."""
        found = list_dashboard_templates(self._uows.uow(actor.company_id), actor=actor)
        return [DashboardTemplateOut.of(template) for template in found]

    def create_from_template(self, actor: Actor, template_id: uuid.UUID) -> DashboardOut:
        """Cria um dashboard privado a partir de um modelo, no idioma da pessoa."""
        created = create_from_template(
            self._uows.uow(actor.company_id),
            actor=actor,
            template_id=template_id,
            clock=self._clock,
        )
        return self._out(actor, created)

    def run(
        self, actor: Actor, dashboard_id: uuid.UUID, widget_id: str, body: WidgetRunIn
    ) -> ReportResultOut:
        """Roda um widget com os filtros da tela ou os do dashboard, com o limite de taxa."""
        result = self._reports.run_guarded(
            actor,
            lambda uow: run_widget(
                uow,
                actor=actor,
                dashboard_id=dashboard_id,
                widget_id=widget_id,
                clock=self._clock,
                filters=body.filters,
            ),
        )
        return ReportResultOut.of(result)

    def run_template(
        self, actor: Actor, template_id: uuid.UUID, widget_id: str, body: WidgetRunIn
    ) -> ReportResultOut:
        """Roda um widget de um modelo pronto, para a tela inicial de quem não tem dashboard."""
        result = self._reports.run_guarded(
            actor,
            lambda uow: run_template_widget(
                uow,
                actor=actor,
                template_id=template_id,
                widget_id=widget_id,
                clock=self._clock,
                filters=body.filters,
            ),
        )
        return ReportResultOut.of(result)

    def run_all(self, actor: Actor, dashboard_id: uuid.UUID, body: WidgetRunIn) -> DashboardRunOut:
        """Roda todos os widgets do dashboard numa requisição, gastando uma consulta do limite."""
        run = self._reports.run_guarded(
            actor,
            lambda uow: run_dashboard(
                uow, actor=actor, dashboard_id=dashboard_id, clock=self._clock, filters=body.filters
            ),
        )
        return DashboardRunOut.of(run)

    def run_template_all(
        self, actor: Actor, template_id: uuid.UUID, body: WidgetRunIn
    ) -> DashboardRunOut:
        """Roda todos os widgets de um modelo pronto numa requisição, com uma consulta do limite."""
        run = self._reports.run_guarded(
            actor,
            lambda uow: run_template(
                uow, actor=actor, template_id=template_id, clock=self._clock, filters=body.filters
            ),
        )
        return DashboardRunOut.of(run)

    def _out(self, actor: Actor, dashboard: Dashboard) -> DashboardOut:
        """O dashboard com o que diz se a pessoa pode editá-lo."""
        editable = dashboard.owner_user_id == actor.user_id or actor.grants.can(MANAGE)
        return DashboardOut.of(dashboard, editable)
