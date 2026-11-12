"""Convite salvo cujo e-mail não sai: as rotas de convite respondem 503 com mensagem fixa."""

from typing import Any

import httpx
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import FINANCE, CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_internal import _staff

MESSAGE = "O convite foi salvo, mas o e-mail não saiu. Tente reenviar."


def _assert_mail_not_sent(response: httpx.Response) -> None:
    """Confere o 503 com o código e a mensagem fixa do convite que ficou sem e-mail."""
    assert response.status_code == 503, response.text
    assert response.json()["error"]["code"] == "invitation_mail_not_sent"
    assert response.json()["error"]["message"] == MESSAGE


def _invite(client: TestClient) -> httpx.Response:
    """Convida a Bia com o papel Financeiro."""
    response: httpx.Response = client.post(
        "/api/v1/invitations",
        json={"email": "bia@acai.com", "role_id": str(FINANCE)},
        headers=_csrf(client),
    )
    return response


def _pending_emails(client: TestClient) -> list[str]:
    """Os e-mails dos convites de equipe pendentes da Empresa ativa."""
    items: list[dict[str, Any]] = client.get("/api/v1/invitations").json()["items"]
    return [item["email"] for item in items]


def _client_with_owner_invitation(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> tuple[TestClient, str]:
    """Cadastra um cliente pendente pela equipe Groone e devolve a sessão e o id do cliente."""
    staff = _staff(client, engine)
    profile = {"first_name": "Ana", "last_name": "Souza", "email": "dono@novo.com"}
    created = staff.post(
        "/api/v1/internal/clients",
        json={"name": "Novo Portal", "seat_limit": 2, "profile": profile},
        headers=_csrf(staff),
    )
    assert created.status_code == 201, created.text
    return staff, created.json()["id"]


def _owner_invitation_emails(staff: TestClient) -> list[str]:
    """Os e-mails dos convites de dono pendentes."""
    items: list[dict[str, Any]] = staff.get("/api/v1/internal/owner-invitations").json()["items"]
    return [item["email"] for item in items]


def test_invite_answers_503_when_the_mail_fails(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    mailer.invitations_fail = True
    _assert_mail_not_sent(_invite(client))
    assert _pending_emails(client) == ["bia@acai.com"]


def test_resend_answers_503_when_the_mail_fails(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    invitation = _invite(client).json()
    mailer.invitations_fail = True
    resent = client.post(f"/api/v1/invitations/{invitation['id']}/resend", headers=_csrf(client))
    _assert_mail_not_sent(resent)
    assert _pending_emails(client) == ["bia@acai.com"]


def test_owner_invitation_answers_503_when_the_mail_fails(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    staff, company_id = _client_with_owner_invitation(client, engine, mailer)
    mailer.invitations_fail = True
    sent = staff.post(
        f"/api/v1/internal/clients/{company_id}/owner-invitation", headers=_csrf(staff)
    )
    _assert_mail_not_sent(sent)
    assert _owner_invitation_emails(staff) == ["dono@novo.com"]


def test_owner_invitation_resend_answers_503_when_the_mail_fails(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    staff, company_id = _client_with_owner_invitation(client, engine, mailer)
    sent = staff.post(
        f"/api/v1/internal/clients/{company_id}/owner-invitation", headers=_csrf(staff)
    )
    assert sent.status_code == 200, sent.text
    mailer.invitations_fail = True
    resent = staff.post(
        f"/api/v1/internal/owner-invitations/{sent.json()['id']}/resend", headers=_csrf(staff)
    )
    _assert_mail_not_sent(resent)
    assert _owner_invitation_emails(staff) == ["dono@novo.com"]


def test_staff_invitation_answers_503_when_the_mail_fails(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    staff = _staff(client, engine)
    roles = staff.get("/api/v1/roles").json()["items"]
    support_role = next(role for role in roles if role["key"] == "groone_support")
    mailer.invitations_fail = True
    invited = staff.post(
        "/api/v1/internal/staff/invitations",
        json={"email": "suporte@groone.com", "role_id": support_role["id"]},
        headers=_csrf(staff),
    )
    _assert_mail_not_sent(invited)
