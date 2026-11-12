"""Conexões da API com o banco: engine do core, prazos na conexão, papel restrito e a conta."""

import pytest
from avant_core.db.app_role import UnsafeDatabaseRole
from avant_core.db.connection_budget import ServiceConnections, check_connection_budget
from avant_core.db.engine import EngineSettings
from sqlalchemy import Engine, text

from avant_api.app.container import Services, engine_settings, restricted_engine
from tests.conftest import OWNER_URL, settings_for_tests

# Números padrão do avant-infra (compose/vm): max_connections do Postgres, as duas cores da API
# (blue e green sobem juntas na troca) e os filhos do worker (fila default/mail e fila gam).
POSTGRES_MAX_CONNECTIONS = 200
RESERVED_CONNECTIONS = 10
API_COLORS = 2
# WEB_CONCURRENCY da imagem (Dockerfile), fixo aqui para o teste não depender do ambiente.
API_PROCESSES_PER_COLOR = 2
API_POOL_SIZE = 10
API_MAX_OVERFLOW = 5
WORKER_PROCESSES = 4 + 2
WORKER_POOL_SIZE = 5
WORKER_MAX_OVERFLOW = 0


def test_engine_settings_come_from_the_settings() -> None:
    assert engine_settings(settings_for_tests()) == EngineSettings(
        application_name="avant-api",
        pool_size=10,
        max_overflow=5,
        pool_timeout_seconds=10,
        pool_recycle_seconds=1800,
        statement_timeout_ms=30_000,
        idle_in_transaction_timeout_ms=60_000,
        lock_timeout_ms=10_000,
    )


@pytest.mark.parametrize(
    "override",
    [
        {"db_statement_timeout_ms": 0},
        {"db_idle_in_transaction_timeout_ms": 300_001},
        {"db_lock_timeout_ms": 60_001},
        {"db_pool_timeout_seconds": 61},
        {"db_pool_size": 0},
    ],
)
def test_engine_settings_refuse_zero_and_above_the_ceiling(override: dict[str, object]) -> None:
    with pytest.raises(ValueError):
        engine_settings(settings_for_tests(**override))


def test_database_url_cannot_override_the_timeouts() -> None:
    url = "postgresql+psycopg://avant_app:x@localhost/avant?options=-c%20statement_timeout%3D0"
    with pytest.raises(ValueError, match="options"):
        restricted_engine(settings_for_tests(database_url=url))


def test_default_numbers_fit_the_connection_budget() -> None:
    settings = settings_for_tests()
    assert (settings.db_pool_size, settings.db_max_overflow) == (API_POOL_SIZE, API_MAX_OVERFLOW)
    services = [
        ServiceConnections(
            name="api",
            processes=API_COLORS * API_PROCESSES_PER_COLOR,
            pool_size=API_POOL_SIZE,
            max_overflow=API_MAX_OVERFLOW,
        ),
        ServiceConnections(
            name="worker",
            processes=WORKER_PROCESSES,
            pool_size=WORKER_POOL_SIZE,
            max_overflow=WORKER_MAX_OVERFLOW,
        ),
    ]
    total = check_connection_budget(
        services, max_connections=POSTGRES_MAX_CONNECTIONS, reserved=RESERVED_CONNECTIONS
    )
    assert total == 90


def test_every_connection_has_the_timeouts_and_the_service_name(engine: Engine) -> None:
    api_engine = restricted_engine(settings_for_tests())
    with api_engine.connect() as conn:
        shown = [
            conn.execute(text(f"SHOW {name}")).scalar()
            for name in (
                "statement_timeout",
                "idle_in_transaction_session_timeout",
                "lock_timeout",
                "application_name",
            )
        ]
    api_engine.dispose()
    assert shown == ["30s", "1min", "10s", "avant-api"]


def test_api_does_not_start_with_a_role_that_ignores_rls(engine: Engine) -> None:
    with pytest.raises(UnsafeDatabaseRole):
        Services.build(settings_for_tests(database_url=OWNER_URL or ""))
