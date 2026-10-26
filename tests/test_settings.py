"""O e-mail em si é testado no avant-core (avant_core.mail)."""

import pytest

from avant_api.app.settings import Settings


def test_resend_key_required_outside_local() -> None:
    with pytest.raises(ValueError, match="RESEND_API_KEY"):
        Settings(avant_env="staging", database_url="postgresql://x", mfa_encryption_key="k")
    Settings(avant_env="local", database_url="postgresql://x", mfa_encryption_key="k")


def test_queue_does_not_break_the_request_without_broker() -> None:
    from avant_api.app.tasks import CeleryQueue

    # Porta fechada: a publicação falha rápido e só vai para o log.
    CeleryQueue("amqp://guest:guest@127.0.0.1:1//").send("avant.gam.sync_network", "a", "b")
