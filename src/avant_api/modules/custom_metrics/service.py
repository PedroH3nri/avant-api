"""Service das métricas personalizadas: chama os casos de uso do avant-core e devolve os DTOs."""

import uuid

from avant_core.access.models import Actor
from avant_core.metrics.models import CustomMetric
from avant_core.metrics.services import (
    CustomMetricSet,
    check_custom_metric,
    create_custom_metric,
    delete_custom_metric,
    list_custom_metrics,
    preview_custom_metric,
    update_custom_metric,
)
from avant_core.shared.clock import Clock
from avant_core.shared.errors import DomainError

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.custom_metrics.dto import (
    CustomMetricCheckIn,
    CustomMetricCheckOut,
    CustomMetricIn,
    CustomMetricOut,
)


class CustomMetricService:
    """Métricas personalizadas da Empresa ativa."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def list_all(self, actor: Actor) -> list[CustomMetricOut]:
        """Métricas personalizadas da Empresa, pelo nome."""
        metrics = list_custom_metrics(self._uows.uow(actor.company_id), actor=actor)
        return _out(metrics)

    def create(self, actor: Actor, body: CustomMetricIn) -> CustomMetricOut:
        """Cadastra uma métrica personalizada."""
        metric = create_custom_metric(
            self._uows.uow(actor.company_id), actor=actor, data=body.input(), clock=self._clock
        )
        return self._one(actor, metric.id)

    def update(self, actor: Actor, metric_id: uuid.UUID, body: CustomMetricIn) -> CustomMetricOut:
        """Troca nome, fórmula, formato, casas e descrição; a chave fica a mesma."""
        update_custom_metric(
            self._uows.uow(actor.company_id),
            actor=actor,
            metric_id=metric_id,
            data=body.input(),
            clock=self._clock,
        )
        return self._one(actor, metric_id)

    def delete(self, actor: Actor, metric_id: uuid.UUID) -> None:
        """Apaga uma métrica personalizada que nenhuma outra usa."""
        delete_custom_metric(
            self._uows.uow(actor.company_id), actor=actor, metric_id=metric_id, clock=self._clock
        )

    def check(self, actor: Actor, body: CustomMetricCheckIn) -> CustomMetricCheckOut:
        """Confere o formulário como salvar faria, sem gravar; com amostra, calcula a prévia."""
        try:
            variables = check_custom_metric(
                self._uows.uow(actor.company_id),
                actor=actor,
                data=body.input(),
                metric_id=body.metric_id,
            )
            value = None
            if body.sample is not None:
                value = preview_custom_metric(
                    self._uows.uow(actor.company_id),
                    actor=actor,
                    data=body.input(),
                    sample=body.sample,
                    metric_id=body.metric_id,
                )
        except DomainError as error:
            if error.code in ("permission_denied", "not_found"):
                raise
            return CustomMetricCheckOut(valid=False, code=error.code, error=str(error))
        return CustomMetricCheckOut(valid=True, variables=sorted(variables), value=value)

    def _one(self, actor: Actor, metric_id: uuid.UUID) -> CustomMetricOut:
        """A métrica recém-gravada, com as fontes calculadas junto das outras da Empresa."""
        metrics = list_custom_metrics(self._uows.uow(actor.company_id), actor=actor)
        return next(out for out in _out(metrics) if out.id == metric_id)


def _out(metrics: list[CustomMetric]) -> list[CustomMetricOut]:
    """As métricas com as fontes em que cada uma pode ser pedida."""
    rules = CustomMetricSet(metrics)
    return [CustomMetricOut.of(metric, rules.sources(f"custom.{metric.key}")) for metric in metrics]
