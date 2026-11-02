"""Service dos alertas de métrica: listar, editar, silenciar, os disparos e a prévia.

Os alertas são da Empresa ativa e usam o Unit of Work dela. A prévia roda o motor de consulta
como uma consulta de relatório: o mesmo limite de taxa e, na Company Groone, sem RLS para somar
as Empresas cliente que a pessoa vê.
"""

import uuid
from datetime import datetime
from typing import Any

from avant_core.access.models import Actor
from avant_core.alerts.services import (
    create_alert,
    delete_alert,
    get_alert,
    mute_alert,
    page_alert_events,
    page_alerts,
    preview_alert,
    update_alert,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.alerts.dto import (
    AlertEventOut,
    AlertIn,
    AlertOut,
    AlertPageOut,
    AlertPreviewOut,
)
from avant_api.modules.reports.service import ReportService
from avant_api.shared.dto import PageOut, page_out


class AlertService:
    """Alertas da Empresa ativa; a prévia passa pelo service dos relatórios."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, reports: ReportService) -> None:
        self._uows = uows
        self._clock = clock
        self._reports = reports

    def page(self, actor: Actor, query: str | None, page: int) -> AlertPageOut:
        """Uma página dos alertas que a pessoa vê, o mais novo primeiro."""
        found = page_alerts(self._uows.uow(actor.company_id), actor=actor, query=query, page=page)
        return AlertPageOut(
            items=[AlertOut.of(view) for view in found.items],
            total=found.total,
            page=found.page,
            pages=found.pages,
            page_size=found.page_size,
        )

    def get(self, actor: Actor, alert_id: uuid.UUID) -> AlertOut:
        """Um alerta que a pessoa vê, com o estado dele."""
        return AlertOut.of(
            get_alert(self._uows.uow(actor.company_id), actor=actor, alert_id=alert_id)
        )

    def create(self, actor: Actor, body: AlertIn) -> AlertOut:
        """Cria o alerta, com a pessoa como dona."""
        alert = create_alert(
            self._uows.uow(actor.company_id), actor=actor, data=body.input(), clock=self._clock
        )
        return self.get(actor, alert.id)

    def update(self, actor: Actor, alert_id: uuid.UUID, body: AlertIn) -> AlertOut:
        """Troca nome, regra e quem recebe."""
        update_alert(
            self._uows.uow(actor.company_id),
            actor=actor,
            alert_id=alert_id,
            data=body.input(),
            clock=self._clock,
        )
        return self.get(actor, alert_id)

    def mute(self, actor: Actor, alert_id: uuid.UUID, until: datetime | None) -> AlertOut:
        """Silencia o alerta até a data dada, ou tira o silêncio."""
        mute_alert(
            self._uows.uow(actor.company_id),
            actor=actor,
            alert_id=alert_id,
            until=until,
            clock=self._clock,
        )
        return self.get(actor, alert_id)

    def delete(self, actor: Actor, alert_id: uuid.UUID) -> None:
        """Apaga o alerta e os disparos dele."""
        delete_alert(
            self._uows.uow(actor.company_id), actor=actor, alert_id=alert_id, clock=self._clock
        )

    def events(self, actor: Actor, alert_id: uuid.UUID, page: int) -> PageOut[AlertEventOut]:
        """Uma página dos disparos do alerta, o mais recente primeiro."""
        found = page_alert_events(
            self._uows.uow(actor.company_id), actor=actor, alert_id=alert_id, page=page
        )
        return page_out(found, AlertEventOut.of)

    def preview(self, actor: Actor, definition: dict[str, Any]) -> AlertPreviewOut:
        """O que o alerta mostraria se valesse hoje, com o limite de taxa das consultas."""
        preview = self._reports.run_guarded(
            actor,
            lambda uow: preview_alert(uow, actor=actor, definition=definition, clock=self._clock),
        )
        return AlertPreviewOut.of(preview)
