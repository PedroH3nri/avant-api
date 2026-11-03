"""Checklist de domínio no painel interno, contra o Postgres."""

import uuid
from datetime import UTC, date, datetime

from avant_core.db.uow import SqlAlchemyUnitOfWork
from avant_core.gam.inventory.models import Site
from avant_core.gam.networks.enums import ConnectionType
from avant_core.gam.networks.models import Network
from avant_core.site_checklists.models import ChecklistResult, SiteChecklist
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.app.tasks import CHECK_CHECKLIST, RecordingQueue
from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_internal import _staff
from tests.test_support_tasks import _agent

BASE = "/api/v1/internal/checklists"
ITEMS = "/api/v1/internal/checklist-items"
NOW = datetime.now(UTC)
MONTH = NOW.date().replace(day=1)
PAST = date(2026, 1, 1)


def _checklists(engine: Engine, company_id: uuid.UUID) -> tuple[str, str]:
    """Um site com o checklist do mês atual e o de janeiro, com todos os itens ativos."""
    with SqlAlchemyUnitOfWork(engine, bypass_rls=True) as uow:
        network = Network(company_id, "4242", ConnectionType.MCM, NOW, "Rede Açaí")
        uow.networks.add(network)
        site = Site(company_id, "acai.com", network_id=network.id, gam_site_id="9", synced_at=NOW)
        uow.sites.add(site)
        current = SiteChecklist(site.id, company_id, MONTH, 900_000_000, NOW)
        past = SiteChecklist(site.id, company_id, PAST, 300_000_000, NOW)
        for checklist in (current, past):
            uow.site_checklists.add(checklist)
            for item in uow.site_checklists.items():
                uow.site_checklists.add_result(ChecklistResult(checklist.id, item.id))
        uow.commit()
        return str(current.id), str(past.id)


def test_staff_marks_checks_and_writes_notes(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    current_id, past_id = _checklists(engine, uuid.UUID(me["companies"][0]["id"]))
    staff = _staff(client, engine)

    months = staff.get(f"{BASE}/months")
    assert months.status_code == 200, months.text
    assert months.json()["items"] == [MONTH.isoformat(), PAST.isoformat()]
    page = staff.get(BASE, params={"month": MONTH.isoformat(), "q": "acai"}).json()
    (row,) = page["items"]
    assert (row["id"], row["revenue"], row["site"]["domain"]) == (current_id, "900.00", "acai.com")
    assert row["progress"] == {"done": 0, "total": 13, "complete": False}
    assert (
        staff.get(BASE, params={"month": MONTH.isoformat(), "state": "done"}).json()["total"] == 0
    )

    detail = staff.get(f"{BASE}/{current_id}").json()
    assert detail["current"] is True and len(detail["rows"]) == 13
    item_id = detail["rows"][0]["item"]["id"]
    marked = staff.put(
        f"{BASE}/{current_id}/items/{item_id}", json={"ok": True}, headers=_csrf(staff)
    )
    assert marked.status_code == 200, marked.text
    first = marked.json()["rows"][0]
    assert first["ok"] is True and first["marked_by"]["name"] == "Admin"
    assert marked.json()["progress"]["done"] == 1

    checked = staff.post(f"{BASE}/{current_id}/check", headers=_csrf(staff))
    assert checked.status_code == 202, checked.text
    queue = client.app.state.services.tasks  # type: ignore[attr-defined]
    assert isinstance(queue, RecordingQueue)
    assert queue.sent[-1] == (CHECK_CHECKLIST, (current_id,))
    old = staff.post(f"{BASE}/{past_id}/check", headers=_csrf(staff))
    assert old.status_code == 409 and old.json()["error"]["code"] == "checklist_not_checkable"

    written = staff.post(
        f"{BASE}/{current_id}/notes", json={"message": "Falta o aviso legal."}, headers=_csrf(staff)
    )
    assert written.status_code == 204, written.text
    (note,) = staff.get(f"{BASE}/{current_id}").json()["notes"]
    assert note["author"]["name"] == "Admin" and note["editable"] is True
    edited = staff.patch(
        f"{BASE}/{current_id}/notes/{note['id']}",
        json={"message": "Falta o aviso legal no rodapé."},
        headers=_csrf(staff),
    )
    assert edited.status_code == 204, edited.text
    deleted = staff.delete(f"{BASE}/{current_id}/notes/{note['id']}", headers=_csrf(staff))
    assert deleted.status_code == 204
    assert staff.get(f"{BASE}/{current_id}").json()["notes"] == []

    summary = staff.get(f"{BASE}/summary", params={"month": MONTH.isoformat()}).json()
    assert (summary["sites"], summary["done"]) == (1, 0)
    (site,) = staff.get("/api/v1/internal/sites").json()["items"]
    assert site["checklist"] == {"id": current_id, "done": 1, "total": 13, "complete": False}


def test_checklists_need_permission(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    me = _onboard_owner(client, engine, mailer)
    current_id, _ = _checklists(engine, uuid.UUID(me["companies"][0]["id"]))
    staff = _staff(client, engine)
    agent = _agent(client, staff, mailer)

    assert agent.get(f"{BASE}/months").status_code == 403
    assert agent.get(f"{BASE}/{current_id}").status_code == 403
    assert agent.post(f"{BASE}/{current_id}/check", headers=_csrf(agent)).status_code == 403
    assert agent.get(ITEMS).status_code == 403
    assert client.get(f"{BASE}/months").status_code == 403


def test_staff_edits_the_item_list(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    staff = _staff(client, engine)
    listed = staff.get(ITEMS)
    assert listed.status_code == 200, listed.text
    assert len(listed.json()["items"]) == 13

    created = staff.post(
        ITEMS, json={"name": "Página de anúncios", "kind": "manual"}, headers=_csrf(staff)
    )
    assert created.status_code == 201, created.text
    item = created.json()
    assert item["position"] == 14
    blank = staff.post(ITEMS, json={"name": " ", "kind": "manual"}, headers=_csrf(staff))
    assert blank.status_code == 422
    updated = staff.put(
        f"{ITEMS}/{item['id']}",
        json={"name": "Página de anúncios", "kind": "manual", "active": False},
        headers=_csrf(staff),
    )
    assert updated.status_code == 200 and updated.json()["active"] is False
    moved = staff.post(f"{ITEMS}/{item['id']}/move", json={"step": -1}, headers=_csrf(staff))
    assert moved.status_code == 200, moved.text
    positions = {entry["id"]: entry["position"] for entry in staff.get(ITEMS).json()["items"]}
    assert positions[item["id"]] == 13
    staff.post(f"{ITEMS}/{item['id']}/move", json={"step": 1}, headers=_csrf(staff))
