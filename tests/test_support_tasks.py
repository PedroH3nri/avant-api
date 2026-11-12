"""Tarefas de suporte da equipe Groone, contra o Postgres."""

import uuid

from avant_core.ports import Notice
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer, browser
from tests.test_api import PASSWORD, _csrf, _onboard_owner
from tests.test_internal import _staff
from tests.test_mfa import _enable

BASE = "/api/v1/internal/tasks"


def _agent(client: TestClient, staff: TestClient, mailer: CapturingMailer) -> TestClient:
    """Uma pessoa da equipe Groone com um papel que só vê as próprias tarefas."""
    role = staff.post(
        "/api/v1/roles",
        json={"name": "Atendimento", "permissions": ["internal.tasks.view"], "site_scope": "all"},
        headers=_csrf(staff),
    )
    assert role.status_code == 201, role.text
    invited = staff.post(
        "/api/v1/internal/staff/invitations",
        json={"email": "bruno@groone.com", "role_id": role.json()["id"]},
        headers=_csrf(staff),
    )
    assert invited.status_code == 201, invited.text
    agent = browser(client.app)
    accepted = agent.post(
        f"/api/v1/auth/invitations/{mailer.sent[-1].token}/accept",
        json={"name": "Bruno", "password": PASSWORD},
    )
    assert accepted.status_code == 200, accepted.text
    _enable(agent)
    return agent


def test_staff_opens_assigns_and_comments_on_tasks(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    company_id = me["companies"][0]["id"]
    staff = _staff(client, engine)
    agent = _agent(client, staff, mailer)
    agent_id = agent.get("/api/v1/auth/me").json()["user"]["id"]

    short = staff.post(BASE, json={"subject": "oi"}, headers=_csrf(staff))
    assert short.status_code == 422
    created = staff.post(
        BASE,
        json={
            "subject": "Anúncio âncora sobre o menu",
            "priority": "high",
            "client_id": company_id,
            "domain": "https://www.blog-do-acai.com/post",
            "assignee_id": agent_id,
        },
        headers=_csrf(staff),
    )
    assert created.status_code == 201, created.text
    task = created.json()
    assert (task["status"], task["domain"]) == ("open", "blog-do-acai.com")
    assert task["assignee"]["name"] == "Bruno" and task["client"]["id"] == company_id
    assert [event["kind"] for event in task["events"]] == ["created"]
    assert mailer.notices[-1] == ("bruno@groone.com", Notice.TASK_ASSIGNED)

    staff.post(BASE, json={"subject": "Só da Admin"}, headers=_csrf(staff))
    mine = agent.get(BASE).json()
    assert mine["total"] == 1 and mine["items"][0]["id"] == task["id"]
    assert staff.get(BASE, params={"scope": "all"}).json()["total"] == 2
    assert staff.get(BASE, params={"scope": "all", "priority": "high"}).json()["total"] == 1
    assert agent.get(BASE, params={"scope": "all"}).status_code == 403
    others = staff.get(BASE, params={"q": "Admin"}).json()["items"]
    assert agent.get(f"{BASE}/{others[0]['id']}").status_code == 404

    moved = agent.patch(f"{BASE}/{task['id']}", json={"status": "working"}, headers=_csrf(agent))
    assert moved.status_code == 200, moved.text
    assert moved.json()["events"][-1]["kind"] == "status_changed"
    commented = agent.post(
        f"{BASE}/{task['id']}/comments",
        json={"message": "Era o z-index do tema."},
        headers=_csrf(agent),
    )
    assert commented.status_code == 201, commented.text
    assert commented.json()["events"][-1]["message"] == "Era o z-index do tema."
    assert mailer.notices[-1] == ("admin@groone.com", Notice.TASK_COMMENTED)

    released = staff.patch(f"{BASE}/{task['id']}", json={"assignee_id": None}, headers=_csrf(staff))
    assert released.status_code == 200 and released.json()["assignee"] is None
    assert agent.get(f"{BASE}/{task['id']}").status_code == 404
    assert staff.get(f"{BASE}/{uuid.uuid4()}").status_code == 404
    assert client.get(BASE).status_code == 403
