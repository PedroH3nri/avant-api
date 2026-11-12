"""Settings da API: o que é obrigatório em todo ambiente, o transporte do e-mail e o erro de
subida que mostra só os nomes das variáveis. O e-mail em si é testado no avant-core."""

import pytest
from avant_core.mail import ResendMailer, SmtpMailer
from pydantic import ValidationError

from avant_api.app.container import _mailer
from avant_api.app.settings import Settings, load_settings
from tests.conftest import settings_for_tests

REDIS = "redis://localhost:6379/0"
BROKER = "amqp://guest:guest@localhost:5672//"
SECRET = "senha-muito-secreta-123"

REQUIRED_ENVIRONMENT = {
    "DATABASE_URL": "postgresql://x",
    "MFA_ENCRYPTION_KEY": "k",
    "REDIS_URL": REDIS,
    "CELERY_BROKER_URL": BROKER,
    "MAIL_TRANSPORT": "resend",
    "RESEND_API_KEY": "re_teste",
    "FORWARDED_ALLOW_IPS": "172.30.0.10",
}
OPTIONAL_ENVIRONMENT = ("SMTP_URL", "WEB_CONCURRENCY", "PROMETHEUS_MULTIPROC_DIR", "AVANT_ENV")


def _environment(monkeypatch: pytest.MonkeyPatch, values: dict[str, str]) -> None:
    """Deixa no ambiente só as variáveis pedidas, para o teste não depender da máquina."""
    for name in (*REQUIRED_ENVIRONMENT, *OPTIONAL_ENVIRONMENT):
        monkeypatch.delenv(name, raising=False)
    for name, value in values.items():
        monkeypatch.setenv(name, value)


def _refused_names(monkeypatch: pytest.MonkeyPatch, values: dict[str, str]) -> str:
    """Sobe as Settings com estas variáveis e devolve a mensagem da recusa."""
    _environment(monkeypatch, values)
    with pytest.raises(SystemExit) as refused:
        load_settings()
    return str(refused.value)


def test_each_transport_builds_its_mailer() -> None:
    resend = settings_for_tests(mail_transport="resend", resend_api_key="re_teste")
    smtp = settings_for_tests(
        mail_transport="smtp", resend_api_key=None, smtp_url="smtp://mailpit:1025"
    )
    assert isinstance(_mailer(resend), ResendMailer)
    assert isinstance(_mailer(smtp), SmtpMailer)


def test_api_starts_with_each_transport(monkeypatch: pytest.MonkeyPatch) -> None:
    _environment(monkeypatch, REQUIRED_ENVIRONMENT)
    assert load_settings().mail_transport == "resend"
    without_resend = {
        name: value for name, value in REQUIRED_ENVIRONMENT.items() if name != "RESEND_API_KEY"
    }
    _environment(
        monkeypatch,
        without_resend | {"MAIL_TRANSPORT": "smtp", "SMTP_URL": "smtp://mailpit:1025"},
    )
    assert load_settings().mail_transport == "smtp"


@pytest.mark.parametrize(
    ("changes", "missing"),
    [
        ({"MAIL_TRANSPORT": None}, "MAIL_TRANSPORT"),
        ({"MAIL_TRANSPORT": "sendmail"}, "MAIL_TRANSPORT"),
        ({"RESEND_API_KEY": None}, "RESEND_API_KEY"),
        ({"RESEND_API_KEY": " "}, "RESEND_API_KEY"),
        ({"MAIL_TRANSPORT": "smtp"}, "SMTP_URL"),
        ({"MAIL_TRANSPORT": "smtp", "SMTP_URL": ""}, "SMTP_URL"),
        ({"REDIS_URL": ""}, "REDIS_URL"),
        ({"REDIS_URL": " "}, "REDIS_URL"),
        ({"CELERY_BROKER_URL": " "}, "CELERY_BROKER_URL"),
        ({"FORWARDED_ALLOW_IPS": None}, "FORWARDED_ALLOW_IPS"),
        ({"FORWARDED_ALLOW_IPS": "*"}, "FORWARDED_ALLOW_IPS"),
        ({"FORWARDED_ALLOW_IPS": "127.0.0.1,*"}, "FORWARDED_ALLOW_IPS"),
        ({"FORWARDED_ALLOW_IPS": "nginx"}, "FORWARDED_ALLOW_IPS"),
        ({"WEB_CONCURRENCY": "2"}, "PROMETHEUS_MULTIPROC_DIR"),
    ],
)
def test_missing_or_invalid_configuration_stops_the_api(
    changes: dict[str, str | None], missing: str, monkeypatch: pytest.MonkeyPatch
) -> None:
    values = {
        name: value for name, value in (REQUIRED_ENVIRONMENT | changes).items() if value is not None
    }
    message = _refused_names(monkeypatch, values)
    assert message == f"configuração da API incompleta: {missing}"


def test_start_error_shows_names_and_never_values(monkeypatch: pytest.MonkeyPatch) -> None:
    values = REQUIRED_ENVIRONMENT | {
        "DATABASE_URL": f"postgresql+psycopg://avant_app:{SECRET}@db:5432/avant",
        "CELERY_BROKER_URL": f"amqp://avant:{SECRET}@rabbitmq:5672//",
        "RESEND_API_KEY": f"re_{SECRET}",
        "FORWARDED_ALLOW_IPS": f"{SECRET}",
    }
    without_key = {name: value for name, value in values.items() if name != "MFA_ENCRYPTION_KEY"}
    missing_key = _refused_names(monkeypatch, without_key)
    assert missing_key == "configuração da API incompleta: MFA_ENCRYPTION_KEY"
    invalid_proxy = _refused_names(monkeypatch, values)
    assert invalid_proxy == "configuração da API incompleta: FORWARDED_ALLOW_IPS"
    for message in (missing_key, invalid_proxy):
        assert SECRET not in message and "input_value" not in message


def test_proxy_addresses_accept_ips_and_networks() -> None:
    accepted = settings_for_tests(forwarded_allow_ips="172.30.0.0/24, ::1")
    assert accepted.forwarded_allow_ips == "172.30.0.0/24, ::1"


def test_environment_name_changes_nothing(monkeypatch: pytest.MonkeyPatch) -> None:
    assert "avant_env" not in Settings.model_fields
    _environment(monkeypatch, REQUIRED_ENVIRONMENT | {"AVANT_ENV": "production"})
    production = load_settings()
    _environment(monkeypatch, REQUIRED_ENVIRONMENT | {"AVANT_ENV": "local"})
    assert load_settings() == production


def test_many_processes_need_the_prometheus_directory() -> None:
    with pytest.raises(ValidationError, match="PROMETHEUS_MULTIPROC_DIR"):
        settings_for_tests(web_concurrency=2)
    settings_for_tests(web_concurrency=2, prometheus_multiproc_dir="/tmp/avant-metrics")


def test_queue_does_not_break_the_request_without_broker() -> None:
    from avant_api.app.tasks import CeleryQueue

    # Porta fechada: a publicação falha rápido e só vai para o log.
    CeleryQueue("amqp://guest:guest@127.0.0.1:1//").send("avant.gam.sync_network", "a", "b")
