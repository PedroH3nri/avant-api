"""Esqueci a senha pela fila do worker, em todo ambiente: a requisição só agenda, sem banco nem
e-mail, e responde igual exista ou não a conta."""

import pytest
from avant_core.ports import UnitOfWork
from avant_core.shared.clock import SystemClock
from fastapi.testclient import TestClient
from sqlalchemy import Engine, create_engine

from avant_api.app.container import Services
from avant_api.app.errors import QueueUnavailable
from avant_api.app.limits import Limiter, MemoryCounter
from avant_api.app.mail_queue import MAIL_QUEUE_RETRY_AFTER, TaskMailQueue
from avant_api.app.tasks import REQUEST_PASSWORD_RESET, RecordingQueue
from avant_api.main import create_app
from avant_api.modules.account.service import AccountService
from tests.conftest import CapturingMailer, settings_for_tests
from tests.test_api import _onboard_owner

EMAIL = "dono@acai.com"
NOBODY = "ninguem@x.com"
NO_DATABASE = "postgresql+psycopg://ninguem@127.0.0.1:1/nada"


class _NoDatabase:
    """Fábrica de transações que falha se alguém abrir uma."""

    def uow(self, company_id: object) -> UnitOfWork:
        """Recusa a transação da Empresa: o esqueci a senha não pode ler o banco."""
        raise AssertionError("o esqueci a senha abriu uma transação")

    def trusted_uow(self) -> UnitOfWork:
        """Recusa a transação sem RLS: o esqueci a senha não pode ler o banco."""
        raise AssertionError("o esqueci a senha abriu uma transação")


class _NoMail(CapturingMailer):
    """Mailer que falha se alguém mandar o link de nova senha na requisição."""

    def send_password_reset(self, *, to: str, token: str, locale: str) -> None:
        """Recusa o envio: o e-mail sai pelo worker."""
        raise AssertionError("o esqueci a senha mandou e-mail na requisição")


def _account(tasks: RecordingQueue) -> AccountService:
    """O service da conta sem banco e sem e-mail, só com a fila do worker."""
    return AccountService(
        _NoDatabase(),
        SystemClock(),
        None,  # type: ignore[arg-type]
        None,  # type: ignore[arg-type]
        _NoMail(),
        Limiter(MemoryCounter()),
        TaskMailQueue(tasks),
    )


def _services(env: str) -> Services:
    """Serviços cujo banco não abre: qualquer consulta derrubaria o pedido."""
    return Services(
        settings=settings_for_tests(
            avant_env=env, database_url=NO_DATABASE, resend_api_key="re_teste"
        ),
        engine=create_engine(NO_DATABASE),
        clock=SystemClock(),
        hasher=None,  # type: ignore[arg-type]
        mailer=_NoMail(),
        box=None,  # type: ignore[arg-type]
    )


def test_forgot_password_only_queues_the_normalized_email() -> None:
    tasks = RecordingQueue()
    account = _account(tasks)
    account.forgot_password(" Dono@Acai.com ", "203.0.113.7")
    account.forgot_password(NOBODY, "203.0.113.7")
    assert tasks.sent == [
        (REQUEST_PASSWORD_RESET, (EMAIL,)),
        (REQUEST_PASSWORD_RESET, (NOBODY,)),
    ]


def test_password_reset_task_goes_to_the_mail_queue() -> None:
    assert REQUEST_PASSWORD_RESET == "avant.mail.request_password_reset"
    assert REQUEST_PASSWORD_RESET.split(".")[1] == "mail"


def test_queue_down_is_a_503_for_everyone() -> None:
    account = _account(RecordingQueue(offline=True))
    for email in (EMAIL, NOBODY):
        with pytest.raises(QueueUnavailable) as refused:
            account.forgot_password(email, "203.0.113.7")
        assert refused.value.retry_after == MAIL_QUEUE_RETRY_AFTER


@pytest.mark.parametrize("env", ["local", "test", "staging", "production"])
def test_forgot_route_queues_without_database_or_mail_in_every_env(env: str) -> None:
    services = _services(env)
    app = TestClient(create_app(services))
    answers = [
        app.post("/api/v1/auth/password/forgot", json={"email": email}) for email in (EMAIL, NOBODY)
    ]
    assert [(answer.status_code, answer.content) for answer in answers] == [(202, b"null")] * 2
    tasks = services.tasks
    assert isinstance(tasks, RecordingQueue)
    assert tasks.sent == [
        (REQUEST_PASSWORD_RESET, (EMAIL,)),
        (REQUEST_PASSWORD_RESET, (NOBODY,)),
    ]


def test_forgot_route_never_sends_the_link_itself(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    services = client.app.state.services  # type: ignore[attr-defined]
    assert client.post("/api/v1/auth/password/forgot", json={"email": EMAIL}).status_code == 202
    assert mailer.resets == []
    assert services.tasks.sent == [(REQUEST_PASSWORD_RESET, (EMAIL,))]
