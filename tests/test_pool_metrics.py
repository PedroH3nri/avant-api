import pytest
from prometheus_client import REGISTRY
from sqlalchemy import Engine, create_engine, text
from sqlalchemy.exc import TimeoutError as PoolTimeout

from avant_api.app.pool_metrics import count_pool_timeout, watch_pool
from tests.conftest import APP_URL


def _sample(name: str) -> float:
    """O valor atual da métrica no registro padrão do Prometheus."""
    value = REGISTRY.get_sample_value(name)
    assert value is not None, name
    return value


def test_pool_gauges_follow_checkout_and_close(engine: Engine) -> None:
    assert APP_URL is not None
    watched = create_engine(APP_URL)
    watch_pool(watched)
    opened, borrowed = (
        _sample("avant_db_pool_open_connections"),
        _sample("avant_db_pool_checked_out"),
    )
    with watched.connect() as connection:
        connection.execute(text("SELECT 1"))
        assert _sample("avant_db_pool_checked_out") == borrowed + 1
        assert _sample("avant_db_pool_open_connections") == opened + 1
    assert _sample("avant_db_pool_checked_out") == borrowed
    watched.dispose()
    assert _sample("avant_db_pool_open_connections") == opened


@pytest.mark.parametrize(("error", "counted"), [(PoolTimeout(), 1), (RuntimeError(), 0)])
def test_pool_timeouts_count_only_the_pool_wait(error: BaseException, counted: int) -> None:
    before = _sample("avant_db_pool_timeouts_total")
    count_pool_timeout(error)
    assert _sample("avant_db_pool_timeouts_total") == before + counted
