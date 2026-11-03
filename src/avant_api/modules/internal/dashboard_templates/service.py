"""Service dos modelos prontos de dashboard: listar, criar, editar, apagar e marcar o início.

Os modelos não são de uma Empresa; os casos de uso conferem a Company Groone e a permissão
``internal.dashboard_templates.manage``.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.dashboards.services import (
    create_template,
    delete_template,
    get_template,
    list_all_templates,
    set_home_template,
    template_roles,
    update_template,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.internal.dashboard_templates.dto import (
    DashboardTemplateIn,
    ManagedTemplateOut,
    TemplateRolesOut,
)


class DashboardTemplateService:
    """Modelos prontos de dashboard da Groone e dos clientes."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def list(self, actor: Actor) -> list[ManagedTemplateOut]:
        """Todos os modelos, os da Groone primeiro e o de início no topo de cada público."""
        found = list_all_templates(self._uows.uow(actor.company_id), actor=actor)
        return [ManagedTemplateOut.of(template) for template in found]

    def roles(self, actor: Actor) -> TemplateRolesOut:
        """Os papéis que podem limitar quem vê um modelo."""
        return TemplateRolesOut.of(template_roles(self._uows.uow(actor.company_id), actor=actor))

    def get(self, actor: Actor, template_id: uuid.UUID) -> ManagedTemplateOut:
        """Um modelo, para editar."""
        found = get_template(self._uows.uow(actor.company_id), actor=actor, template_id=template_id)
        return ManagedTemplateOut.of(found)

    def create(self, actor: Actor, body: DashboardTemplateIn) -> ManagedTemplateOut:
        """Salva um modelo novo."""
        created = create_template(
            self._uows.uow(actor.company_id), actor=actor, data=body.input(), clock=self._clock
        )
        return ManagedTemplateOut.of(created)

    def update(
        self, actor: Actor, template_id: uuid.UUID, body: DashboardTemplateIn
    ) -> ManagedTemplateOut:
        """Troca tudo do modelo; os dashboards já copiados dele não mudam."""
        updated = update_template(
            self._uows.uow(actor.company_id),
            actor=actor,
            template_id=template_id,
            data=body.input(),
            clock=self._clock,
        )
        return ManagedTemplateOut.of(updated)

    def delete(self, actor: Actor, template_id: uuid.UUID) -> None:
        """Apaga um modelo."""
        delete_template(
            self._uows.uow(actor.company_id),
            actor=actor,
            template_id=template_id,
            clock=self._clock,
        )

    def set_home(self, actor: Actor, template_id: uuid.UUID) -> ManagedTemplateOut:
        """Marca o modelo que abre no início de quem ainda não tem dashboard, no público dele."""
        marked = set_home_template(
            self._uows.uow(actor.company_id),
            actor=actor,
            template_id=template_id,
            clock=self._clock,
        )
        return ManagedTemplateOut.of(marked)
