"""Métricas do pool de conexões com o Postgres para o Prometheus (core#370).

Os gauges somam todos os processos do uvicorn (``livesum`` no modo multiprocesso). A espera por
conexão aparece como esgotamento: um pedido que passa do ``pool_timeout`` conta em
``avant_db_pool_timeouts_total``.
"""

from typing import Any

from prometheus_client import Counter, Gauge
from sqlalchemy import Engine, event
from sqlalchemy.exc import TimeoutError as PoolTimeout

POOL_CHECKED_OUT = Gauge(
    "avant_db_pool_checked_out",
    "Conexões do pool emprestadas a um pedido agora",
    multiprocess_mode="livesum",
)
POOL_OPEN = Gauge(
    "avant_db_pool_open_connections",
    "Conexões abertas com o Postgres, emprestadas ou paradas no pool",
    multiprocess_mode="livesum",
)
POOL_TIMEOUTS = Counter(
    "avant_db_pool_timeouts_total", "Pedidos que esperaram uma conexão além do pool_timeout"
)


def watch_pool(engine: Engine) -> None:
    """Liga os eventos do pool do engine aos gauges de conexões abertas e emprestadas."""
    pool = engine.pool
    event.listen(pool, "connect", _opened)
    event.listen(pool, "close", _closed)
    event.listen(pool, "close_detached", _closed)
    event.listen(pool, "checkout", _checked_out)
    event.listen(pool, "checkin", _checked_in)


def count_pool_timeout(error: BaseException) -> None:
    """Conta a espera esgotada por uma conexão; outros erros passam sem contar."""
    if isinstance(error, PoolTimeout):
        POOL_TIMEOUTS.inc()


def _opened(*_args: Any) -> None:
    """Uma conexão nova com o Postgres."""
    POOL_OPEN.inc()


def _closed(*_args: Any) -> None:
    """Uma conexão fechada com o Postgres."""
    POOL_OPEN.dec()


def _checked_out(*_args: Any) -> None:
    """Uma conexão saiu do pool para um pedido."""
    POOL_CHECKED_OUT.inc()


def _checked_in(*_args: Any) -> None:
    """Uma conexão voltou ao pool."""
    POOL_CHECKED_OUT.dec()
