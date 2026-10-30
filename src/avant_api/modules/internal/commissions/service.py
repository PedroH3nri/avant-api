"""Service da comissão da equipe Groone: chama os casos de uso do avant-core e devolve os DTOs.

As consultas leem os clientes, as networks e os sites de todas as Empresas, então tudo usa o
Unit of Work sem RLS, como o resultado dos clientes; o core confere a Company Groone e as
permissões.
"""

import uuid
from datetime import date

from avant_core.access.models import Actor
from avant_core.commissions.services import (
    add_adjustment,
    commission_start,
    delete_rule,
    list_rules,
    my_commissions,
    person_commissions,
    save_rule,
    set_commission_start,
    team_commissions,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.internal.commissions.dto import (
    AdjustmentIn,
    CommissionRuleIn,
    CommissionRuleOut,
    CommissionSettingsOut,
    MyCommissionsOut,
    PersonMonthOut,
    WindowMonthOut,
)


class CommissionService:
    """Regras no papel, data de início, consultas e desconto."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def current_month(self) -> date:
        """O primeiro dia do mês corrente."""
        return self._clock.now().date().replace(day=1)

    def rules(self, actor: Actor, role_id: uuid.UUID) -> list[CommissionRuleOut]:
        """As regras de um papel da equipe Groone."""
        found = list_rules(self._uows.trusted_uow(), actor=actor, role_id=role_id)
        return [CommissionRuleOut.of(rule) for rule in found]

    def save_rule(
        self, actor: Actor, role_id: uuid.UUID, body: CommissionRuleIn, rule_id: uuid.UUID | None
    ) -> CommissionRuleOut:
        """Cria ou troca uma regra do papel."""
        rule = save_rule(
            self._uows.trusted_uow(),
            actor=actor,
            role_id=role_id,
            data=body.input(),
            clock=self._clock,
            rule_id=rule_id,
        )
        return CommissionRuleOut.of(rule)

    def delete_rule(self, actor: Actor, rule_id: uuid.UUID) -> None:
        """Apaga uma regra."""
        delete_rule(self._uows.trusted_uow(), actor=actor, rule_id=rule_id, clock=self._clock)

    def settings(self, actor: Actor) -> CommissionSettingsOut:
        """A data de início da comissão no Avant."""
        return CommissionSettingsOut(
            starts_on=commission_start(self._uows.trusted_uow(), actor=actor)
        )

    def set_start(self, actor: Actor, starts_on: date) -> CommissionSettingsOut:
        """Grava a data de início e abre os prazos do que já existia."""
        set_commission_start(
            self._uows.trusted_uow(), actor=actor, starts_on=starts_on, clock=self._clock
        )
        return CommissionSettingsOut(starts_on=starts_on)

    def mine(self, actor: Actor, month: date) -> MyCommissionsOut:
        """A comissão de quem pede."""
        found = my_commissions(
            self._uows.trusted_uow(), actor=actor, month=month, clock=self._clock
        )
        return MyCommissionsOut.of(found)

    def team(self, actor: Actor, month: date) -> list[PersonMonthOut]:
        """A comissão de cada pessoa da equipe Groone no mês."""
        found = team_commissions(self._uows.trusted_uow(), actor=actor, month=month)
        return [PersonMonthOut.of(person) for person in found]

    def person(self, actor: Actor, user_id: uuid.UUID, month: date) -> list[WindowMonthOut]:
        """Os prazos de uma pessoa com o que geraram no mês."""
        found = person_commissions(
            self._uows.trusted_uow(), actor=actor, user_id=user_id, month=month
        )
        return [WindowMonthOut.of(item) for item in found]

    def adjust(self, actor: Actor, user_id: uuid.UUID, body: AdjustmentIn) -> None:
        """Lança um desconto na comissão do mês de uma pessoa."""
        add_adjustment(
            self._uows.trusted_uow(),
            actor=actor,
            user_id=user_id,
            month=body.first_day(),
            amount=body.amount,
            reason=body.reason,
            clock=self._clock,
        )
