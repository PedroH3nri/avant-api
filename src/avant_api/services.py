"""Os adaptadores que a API entrega aos casos de uso. Um por processo."""

import uuid
from dataclasses import dataclass

from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.identity.passwords import Argon2PasswordHasher
from avant_core.ports import Mailer, PasswordHasher
from avant_core.shared.clock import Clock, SystemClock
from sqlalchemy import Engine, create_engine

from avant_api.mail import LogMailer
from avant_api.settings import Settings


@dataclass
class Services:
    settings: Settings
    engine: Engine
    clock: Clock
    hasher: PasswordHasher
    mailer: Mailer

    @classmethod
    def build(cls, settings: Settings) -> "Services":
        engine = create_engine(
            settings.database_url, pool_size=settings.db_pool_size, pool_pre_ping=True
        )
        return cls(
            settings=settings,
            engine=engine,
            clock=SystemClock(),
            hasher=Argon2PasswordHasher(),
            mailer=LogMailer(
                base_url=settings.app_base_url,
                show_links=settings.avant_env in ("local", "test"),
            ),
        )

    def uow(self, company_id: uuid.UUID) -> SqlAlchemyUnitOfWork:
        """Transação presa à Empresa ativa (RLS)."""
        return SqlAlchemyUnitOfWork(self.engine, company_id=company_id)

    def trusted_uow(self) -> SqlAlchemyUnitOfWork:
        """Sem RLS: só para login, sessão e aceite de convite pelo token."""
        return SqlAlchemyUnitOfWork(self.engine, bypass_rls=True)
