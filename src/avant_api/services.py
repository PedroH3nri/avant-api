"""Os adaptadores que a API entrega aos casos de uso. Um por processo."""

import uuid
from dataclasses import dataclass, field

from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.identity.crypto import FernetSecretBox
from avant_core.identity.passwords import Argon2PasswordHasher
from avant_core.mail import LogMailer, ResendMailer
from avant_core.ports import Mailer, PasswordHasher, SecretBox
from avant_core.shared.clock import Clock, SystemClock
from sqlalchemy import Engine, create_engine

from avant_api.events import EventSource, NoEvents, RedisEvents
from avant_api.google import GoogleAuth, GoogleOAuth
from avant_api.limits import (
    Bucket,
    Limiter,
    MemoryBucket,
    MemoryCounter,
    RedisBucket,
    RedisCounter,
)
from avant_api.settings import Settings
from avant_api.tasks import CeleryQueue, RecordingQueue, TaskQueue


@dataclass
class Services:
    settings: Settings
    engine: Engine
    clock: Clock
    hasher: PasswordHasher
    mailer: Mailer
    box: SecretBox
    limiter: Limiter = field(default_factory=lambda: Limiter(MemoryCounter()))
    bucket: Bucket = field(default_factory=MemoryBucket)  # chaves de API
    google: GoogleAuth | None = None  # sem cliente OAuth configurado, não há login com Google
    tasks: TaskQueue = field(default_factory=RecordingQueue)
    events: EventSource = field(default_factory=NoEvents)

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
            mailer=_mailer(settings),
            box=FernetSecretBox(settings.mfa_encryption_key),
            limiter=Limiter(
                RedisCounter.from_url(settings.redis_url) if settings.redis_url else MemoryCounter()
            ),
            bucket=RedisBucket.from_url(settings.redis_url)
            if settings.redis_url
            else MemoryBucket(),
            google=_google(settings),
            tasks=CeleryQueue(settings.celery_broker_url)
            if settings.celery_broker_url
            else RecordingQueue(),
            events=RedisEvents(settings.redis_url) if settings.redis_url else NoEvents(),
        )

    def uow(self, company_id: uuid.UUID) -> SqlAlchemyUnitOfWork:
        """Transação presa à Empresa ativa (RLS)."""
        return SqlAlchemyUnitOfWork(self.engine, company_id=company_id)

    def trusted_uow(self) -> SqlAlchemyUnitOfWork:
        """Sem RLS: só para login, sessão e aceite de convite pelo token."""
        return SqlAlchemyUnitOfWork(self.engine, bypass_rls=True)


def _mailer(settings: Settings) -> Mailer:
    if settings.resend_api_key:
        return ResendMailer(
            api_key=settings.resend_api_key,
            sender=settings.mail_from,
            base_url=settings.app_base_url,
        )
    return LogMailer(
        base_url=settings.app_base_url, show_links=settings.avant_env in ("local", "test")
    )


def _google(settings: Settings) -> GoogleAuth | None:
    if not (settings.google_oauth_client_id and settings.google_oauth_client_secret):
        return None
    return GoogleOAuth(
        client_id=settings.google_oauth_client_id,
        client_secret=settings.google_oauth_client_secret,
        redirect_uri=f"{settings.app_base_url.rstrip('/')}/api/v1/auth/google/callback",
    )
