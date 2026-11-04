"""Conexões da API com o banco: pool contado e consultas com prazo."""

import pytest
from sqlalchemy import create_engine, text

from avant_api.app.container import engine_options
from avant_api.app.settings import Settings
from tests.conftest import APP_URL


def _settings() -> Settings:
    return Settings(database_url=APP_URL or "", avant_env="test", mfa_encryption_key="x" * 44)


def test_pool_is_bounded_and_waits_little() -> None:
    options = engine_options(_settings())
    assert (options["pool_size"], options["max_overflow"], options["pool_timeout"]) == (10, 5, 10)
    assert options["pool_pre_ping"] is True


@pytest.mark.skipif(not APP_URL, reason="defina AVANT_TEST_DATABASE_URL")
def test_every_connection_has_a_statement_and_idle_timeout() -> None:
    engine = create_engine(APP_URL or "", **engine_options(_settings()))
    with engine.connect() as conn:
        statement = conn.execute(text("SHOW statement_timeout")).scalar()
        idle = conn.execute(text("SHOW idle_in_transaction_session_timeout")).scalar()
    engine.dispose()
    assert (statement, idle) == ("30s", "1min")
