"""Service dos envios agendados: listar, ver, criar, editar, pausar e apagar.

Os envios são da Empresa ativa e usam o Unit of Work dela. O envio em si roda no worker, de
hora em hora, com os números de cada pessoa da lista.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.schedules.services import (
    create_schedule,
    delete_schedule,
    get_schedule,
    page_schedules,
    pause_schedule,
    update_schedule,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.schedules.dto import ScheduleIn, ScheduleOut, SchedulePageOut


class ScheduleService:
    """Envios agendados da Empresa ativa."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def page(self, actor: Actor, query: str | None, page: int) -> SchedulePageOut:
        """Uma página dos envios que a pessoa vê, o mais novo primeiro."""
        found = page_schedules(
            self._uows.uow(actor.company_id), actor=actor, query=query, page=page
        )
        return SchedulePageOut(
            items=[ScheduleOut.of(view) for view in found.items],
            total=found.total,
            page=found.page,
            pages=found.pages,
            page_size=found.page_size,
        )

    def get(self, actor: Actor, schedule_id: uuid.UUID) -> ScheduleOut:
        """Um envio que a pessoa vê."""
        return ScheduleOut.of(
            get_schedule(self._uows.uow(actor.company_id), actor=actor, schedule_id=schedule_id)
        )

    def create(self, actor: Actor, body: ScheduleIn) -> ScheduleOut:
        """Cria o envio, com a pessoa como dona."""
        schedule = create_schedule(
            self._uows.uow(actor.company_id), actor=actor, data=body.input(), clock=self._clock
        )
        return self.get(actor, schedule.id)

    def update(self, actor: Actor, schedule_id: uuid.UUID, body: ScheduleIn) -> ScheduleOut:
        """Troca o que manda, quando e para quem."""
        update_schedule(
            self._uows.uow(actor.company_id),
            actor=actor,
            schedule_id=schedule_id,
            data=body.input(),
            clock=self._clock,
        )
        return self.get(actor, schedule_id)

    def pause(self, actor: Actor, schedule_id: uuid.UUID, paused: bool) -> ScheduleOut:
        """Pausa o envio ou volta a mandar."""
        pause_schedule(
            self._uows.uow(actor.company_id),
            actor=actor,
            schedule_id=schedule_id,
            paused=paused,
            clock=self._clock,
        )
        return self.get(actor, schedule_id)

    def delete(self, actor: Actor, schedule_id: uuid.UUID) -> None:
        """Apaga o envio e o histórico dele."""
        delete_schedule(
            self._uows.uow(actor.company_id),
            actor=actor,
            schedule_id=schedule_id,
            clock=self._clock,
        )
