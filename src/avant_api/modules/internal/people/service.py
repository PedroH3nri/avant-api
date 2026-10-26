"""Service das pessoas no painel interno: busca, desativação e 2FA perdido."""

import uuid

from avant_core.company.application import Actor
from avant_core.internal.application import (
    PersonView,
    reset_user_mfa,
    search_users,
    set_user_status,
)
from avant_core.ports import Mailer
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.internal.people.dto import PersonOut
from avant_api.shared.dto import CompanyRefOut, UserOut


def person_out(person: PersonView) -> PersonOut:
    """Monta a resposta de uma pessoa com as Empresas em que está."""
    user = person.user
    return PersonOut(
        user=UserOut(id=user.id, email=user.email, name=user.name, locale=user.locale),
        status=user.status,
        mfa_enabled=user.mfa_enabled,
        last_login_at=user.last_login_at,
        companies=[
            CompanyRefOut(
                id=company.id, name=company.name, slug=company.slug, is_internal=company.is_internal
            )
            for company in person.companies
        ],
    )


class PeopleService:
    """Contas das pessoas vistas pela equipe Groone."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, mailer: Mailer) -> None:
        self._uows = uows
        self._clock = clock
        self._mailer = mailer

    def search(self, actor: Actor, query: str) -> list[PersonOut]:
        """Pessoas por nome ou e-mail."""
        people = search_users(self._uows.trusted_uow(), actor=actor, query=query)
        return [person_out(person) for person in people]

    def set_disabled(self, actor: Actor, user_id: uuid.UUID, disabled: bool) -> None:
        """Desativa (encerrando as sessões) ou reativa a conta de uma pessoa."""
        set_user_status(
            self._uows.trusted_uow(),
            actor=actor,
            user_id=user_id,
            disabled=disabled,
            clock=self._clock,
        )

    def reset_mfa(self, actor: Actor, user_id: uuid.UUID) -> None:
        """Desliga o 2FA de uma pessoa que perdeu o acesso."""
        reset_user_mfa(
            self._uows.trusted_uow(),
            actor=actor,
            user_id=user_id,
            clock=self._clock,
            mailer=self._mailer,
        )
