"""Adaptador do Resend contra um transporte falso do httpx: não sai nada para a rede."""

import json

import httpx
import pytest
from avant_core.company.domain import InvitationKind

from avant_api.mail import RESEND_URL, ResendMailer, render_invitation
from avant_api.settings import Settings


def _mailer(handler: httpx.MockTransport) -> ResendMailer:
    return ResendMailer(
        api_key="re_teste",
        sender="Avant <nao-responda@avant.groone.com>",
        base_url="https://avant.groone.com/",
        client=httpx.Client(transport=handler),
    )


def test_sends_invitation_through_resend() -> None:
    requests: list[httpx.Request] = []

    def handle(request: httpx.Request) -> httpx.Response:
        requests.append(request)
        return httpx.Response(200, json={"id": "abc"})

    _mailer(httpx.MockTransport(handle)).send_invitation(
        to="ana@exemplo.com",
        token="tok123",
        kind=InvitationKind.TEAM,
        company_name="Acme <Mídia>",
        locale="pt",
    )
    (req,) = requests
    assert str(req.url) == RESEND_URL
    assert req.headers["Authorization"] == "Bearer re_teste"
    body = json.loads(req.content)
    assert body["to"] == ["ana@exemplo.com"]
    assert body["subject"] == "Convite para Acme <Mídia> no Groone Avant"
    assert "https://avant.groone.com/convite/tok123" in body["text"]
    # O nome da Empresa vem do cliente: precisa sair escapado no HTML.
    assert "Acme &lt;Mídia&gt;" in body["html"]
    assert "<Mídia>" not in body["html"]


def test_retries_once_on_server_error() -> None:
    calls = 0

    def handle(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        return httpx.Response(503 if calls == 1 else 200, json={"id": "abc"})

    _mailer(httpx.MockTransport(handle)).send_invitation(
        to="a@b.com", token="t", kind=InvitationKind.OWNER, company_name=None, locale="en"
    )
    assert calls == 2


def test_client_error_is_logged_not_raised(caplog: pytest.LogCaptureFixture) -> None:
    calls = 0

    def handle(request: httpx.Request) -> httpx.Response:
        nonlocal calls
        calls += 1
        return httpx.Response(422, json={"message": "invalid from"})

    _mailer(httpx.MockTransport(handle)).send_invitation(
        to="a@b.com", token="t", kind=InvitationKind.OWNER, company_name=None, locale="es"
    )
    assert calls == 1
    assert any(r.message == "e-mail não saiu" for r in caplog.records)


def test_network_error_is_logged_not_raised(caplog: pytest.LogCaptureFixture) -> None:
    def handle(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("sem rede")

    _mailer(httpx.MockTransport(handle)).send_invitation(
        to="a@b.com", token="t", kind=InvitationKind.OWNER, company_name=None, locale="pt"
    )
    assert any(r.message == "e-mail não saiu" for r in caplog.records)


@pytest.mark.parametrize(
    ("locale", "subject"),
    [
        ("pt", "Seu acesso ao Groone Avant"),
        ("en", "Your Groone Avant access"),
        ("es", "Tu acceso a Groone Avant"),
        ("fr", "Seu acesso ao Groone Avant"),
    ],
)
def test_owner_invitation_per_locale(locale: str, subject: str) -> None:
    msg = render_invitation(
        link="https://x/convite/t", kind=InvitationKind.OWNER, company_name=None, locale=locale
    )
    assert msg.subject == subject


def test_resend_key_required_outside_local() -> None:
    with pytest.raises(ValueError, match="RESEND_API_KEY"):
        Settings(avant_env="staging", database_url="postgresql://x", mfa_encryption_key="k")
    Settings(avant_env="local", database_url="postgresql://x", mfa_encryption_key="k")
