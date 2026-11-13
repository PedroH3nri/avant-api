"""Os adaptadores que a API entrega aos casos de uso. Um por processo."""

import uuid
from dataclasses import dataclass

from avant_core.db.app_role import ensure_app_role_is_restricted
from avant_core.db.engine import EngineSettings, new_engine
from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.identity.security.crypto import FernetSecretBox
from avant_core.identity.security.passwords import Argon2PasswordHasher
from avant_core.mail import build_mailer
from avant_core.ports import ImageProcessor, Mailer, MailQueue, PasswordHasher, SecretBox
from avant_core.shared.clock import Clock, SystemClock
from sqlalchemy import Engine

from avant_api.app.countries import CountryLookup, GeoLiteCountries, NoCountries
from avant_api.app.events import EventSource, RedisEvents, StreamLimiter
from avant_api.app.google import GoogleAuth, GoogleOAuth
from avant_api.app.images import PillowImageProcessor
from avant_api.app.key_value_buffer import KeyValueBuffer, RedisKeyValueBuffer
from avant_api.app.limits import Bucket, Limiter, RedisBucket, RedisCounter
from avant_api.app.mail_queue import TaskMailQueue
from avant_api.app.pool_metrics import watch_pool
from avant_api.app.reward_buffer import PAGE_VIEWS_BUFFER, RedisRewardBuffer, RewardBuffer
from avant_api.app.reward_cache import RedisRewardCache, RewardCache
from avant_api.app.settings import Settings
from avant_api.app.tasks import CeleryQueue, TaskQueue

APPLICATION_NAME = "avant-api"


def engine_settings(settings: Settings) -> EngineSettings:
    """Pool e prazos do engine da API, lidos das settings; o core recusa zero e o que passa
    dos tetos."""
    return EngineSettings(
        application_name=APPLICATION_NAME,
        pool_size=settings.db_pool_size,
        max_overflow=settings.db_max_overflow,
        pool_timeout_seconds=settings.db_pool_timeout_seconds,
        pool_recycle_seconds=settings.db_pool_recycle_seconds,
        statement_timeout_ms=settings.db_statement_timeout_ms,
        idle_in_transaction_timeout_ms=settings.db_idle_in_transaction_timeout_ms,
        lock_timeout_ms=settings.db_lock_timeout_ms,
    )


def restricted_engine(settings: Settings) -> Engine:
    """Monta o engine com as métricas do pool e recusa a subida se o papel do banco puder
    ignorar o RLS."""
    engine = new_engine(settings.database_url, engine_settings(settings))
    watch_pool(engine)
    try:
        ensure_app_role_is_restricted(engine)
    except Exception:
        engine.dispose()
        raise
    return engine


@dataclass
class Services:
    """Todos os adaptadores são obrigatórios: nenhum fake em memória entra por padrão. O build
    monta Redis, RabbitMQ e Resend; os testes montam os fakes na fábrica deles."""

    settings: Settings
    engine: Engine
    clock: Clock
    hasher: PasswordHasher
    mailer: Mailer
    box: SecretBox
    limiter: Limiter
    # Balde de fichas que limita as chaves de API.
    bucket: Bucket
    # Sem cliente OAuth configurado, não há login com Google.
    google: GoogleAuth | None
    tasks: TaskQueue
    events: EventSource
    stream_limiter: StreamLimiter
    images: ImageProcessor
    key_values: KeyValueBuffer
    rewards: RewardCache
    reward_events: RewardBuffer
    page_views: RewardBuffer
    countries: CountryLookup

    @classmethod
    def build(cls, settings: Settings) -> "Services":
        """Monta banco, Redis, email, Google e fila a partir das configurações; sem Redis ou sem a
        fila as Settings recusam a subida, e com papel do banco que ignora o RLS também."""
        return cls(
            settings=settings,
            engine=restricted_engine(settings),
            clock=SystemClock(),
            hasher=Argon2PasswordHasher(),
            mailer=_mailer(settings),
            box=FernetSecretBox(settings.mfa_encryption_key),
            limiter=Limiter(RedisCounter.from_url(settings.redis_url)),
            bucket=RedisBucket.from_url(settings.redis_url),
            google=_google(settings),
            tasks=CeleryQueue(settings.celery_broker_url),
            events=RedisEvents(settings.redis_url),
            stream_limiter=StreamLimiter(),
            images=PillowImageProcessor(),
            key_values=RedisKeyValueBuffer.from_url(settings.redis_url),
            rewards=RedisRewardCache.from_url(settings.redis_url),
            reward_events=RedisRewardBuffer.from_url(settings.redis_url),
            page_views=RedisRewardBuffer.from_url(settings.redis_url, PAGE_VIEWS_BUFFER),
            countries=GeoLiteCountries(settings.geolite2_country_file)
            if settings.geolite2_country_file
            else NoCountries(),
        )

    def uow(self, company_id: uuid.UUID) -> SqlAlchemyUnitOfWork:
        """Transação presa à Empresa ativa (RLS)."""
        return SqlAlchemyUnitOfWork(self.engine, company_id=company_id)

    def trusted_uow(self) -> SqlAlchemyUnitOfWork:
        """Sem RLS: só para login, sessão e aceite de convite pelo token."""
        return SqlAlchemyUnitOfWork(self.engine, bypass_rls=True)

    def mail_queue(self) -> MailQueue:
        """Os e-mails da conta que saem pela fila do worker, em todo ambiente."""
        return TaskMailQueue(self.tasks)


def _mailer(settings: Settings) -> Mailer:
    """O mailer do MAIL_TRANSPORT (Resend ou SMTP), montado pelo core sem olhar o ambiente:
    nenhum e-mail nem link com token vai para o log."""
    return build_mailer(
        transport=settings.mail_transport,
        sender=settings.mail_from,
        base_url=settings.app_base_url,
        resend_api_key=settings.resend_api_key,
        smtp_url=settings.smtp_url,
    )


def _google(settings: Settings) -> GoogleAuth | None:
    """Monta o cliente OAuth do Google, se estiver configurado."""
    if not (settings.google_oauth_client_id and settings.google_oauth_client_secret):
        return None
    return GoogleOAuth(
        client_id=settings.google_oauth_client_id,
        client_secret=settings.google_oauth_client_secret,
        redirect_uri=f"{settings.app_base_url.rstrip('/')}/api/v1/auth/google/callback",
    )
