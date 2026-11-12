"""O e-mail em si é testado no avant-core (avant_core.mail)."""

import pytest
from pydantic import ValidationError

from avant_api.app.settings import Settings
from tests.conftest import settings_for_tests

REDIS = "redis://localhost:6379/0"
BROKER = "amqp://guest:guest@localhost:5672//"


@pytest.mark.parametrize("env", ["local", "test", "staging", "production"])
def test_resend_key_required_in_every_env(env: str) -> None:
    with pytest.raises(ValueError, match="RESEND_API_KEY é obrigatória em todo ambiente"):
        settings_for_tests(avant_env=env, resend_api_key=" ")
    base = {"avant_env": env, "database_url": "postgresql://x", "mfa_encryption_key": "k"}
    with pytest.raises(ValidationError, match="resend_api_key"):
        Settings(**base, redis_url=REDIS, celery_broker_url=BROKER)  # type: ignore[arg-type]


@pytest.mark.parametrize("env", ["local", "test", "staging", "production"])
def test_api_does_not_start_without_redis_or_queue_in_any_env(env: str) -> None:
    base = {
        "avant_env": env,
        "database_url": "postgresql://x",
        "mfa_encryption_key": "k",
        "resend_api_key": "re_teste",
    }
    with pytest.raises(ValidationError, match="redis_url"):
        Settings(**base, celery_broker_url=BROKER)  # type: ignore[arg-type]
    with pytest.raises(ValidationError, match="celery_broker_url"):
        Settings(**base, redis_url=REDIS)  # type: ignore[arg-type]
    with pytest.raises(ValidationError, match="REDIS_URL é obrigatória em todo ambiente"):
        Settings(**base, redis_url=" ", celery_broker_url=BROKER)  # type: ignore[arg-type]
    with pytest.raises(ValidationError, match="CELERY_BROKER_URL é obrigatória em todo ambiente"):
        Settings(**base, redis_url=REDIS, celery_broker_url="")  # type: ignore[arg-type]


def test_queue_does_not_break_the_request_without_broker() -> None:
    from avant_api.app.tasks import CeleryQueue

    # Porta fechada: a publicação falha rápido e só vai para o log.
    CeleryQueue("amqp://guest:guest@127.0.0.1:1//").send("avant.gam.sync_network", "a", "b")


def test_many_processes_need_the_prometheus_directory() -> None:
    with pytest.raises(ValueError, match="PROMETHEUS_MULTIPROC_DIR"):
        settings_for_tests(web_concurrency=2)
    settings_for_tests(web_concurrency=2, prometheus_multiproc_dir="/tmp/avant-metrics")
    settings_for_tests(web_concurrency=1)
