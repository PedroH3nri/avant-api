"""Grupos de funcionários contra o Postgres: criar, mexer nas pessoas e excluir."""

from fastapi.testclient import TestClient
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_team import _member_client


def _membership_ids(client: TestClient) -> dict[str, str]:
    """Os vínculos da Empresa ativa, pelo email de cada pessoa."""
    items = client.get("/api/v1/members").json()["items"]
    return {item["user"]["email"]: item["id"] for item in items}


def test_groups_lifecycle(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    _onboard_owner(client, engine, mailer)
    ana = _member_client(client, mailer, "ana@acai.com")
    _member_client(client, mailer, "bia@acai.com")
    ids = _membership_ids(client)
    owner_id, ana_id, bia_id = ids["dono@acai.com"], ids["ana@acai.com"], ids["bia@acai.com"]

    assert ana.get("/api/v1/groups").status_code == 403
    denied = ana.post(
        "/api/v1/groups", json={"name": "Tráfego", "membership_ids": [ana_id]}, headers=_csrf(ana)
    )
    assert denied.status_code == 403

    empty = client.post(
        "/api/v1/groups", json={"name": "Tráfego", "membership_ids": []}, headers=_csrf(client)
    )
    assert empty.status_code == 422

    created = client.post(
        "/api/v1/groups",
        json={"name": "Tráfego", "description": "Compra de mídia", "membership_ids": [ana_id]},
        headers=_csrf(client),
    )
    assert created.status_code == 201, created.text
    group = created.json()
    assert group["status"] == "active"
    assert [member["membership_id"] for member in group["members"]] == [ana_id]

    taken = client.post(
        "/api/v1/groups",
        json={"name": "tráfego", "membership_ids": [bia_id]},
        headers=_csrf(client),
    )
    assert taken.status_code == 409 and taken.json()["error"]["code"] == "group_name_taken"
    other = client.post(
        "/api/v1/groups", json={"name": "Vendas", "membership_ids": [ana_id]}, headers=_csrf(client)
    )
    assert other.status_code == 409
    assert other.json()["error"]["code"] == "member_in_other_group"

    path = f"/api/v1/groups/{group['id']}"
    last = client.delete(f"{path}/members/{ana_id}", headers=_csrf(client))
    assert last.status_code == 409 and last.json()["error"]["code"] == "group_needs_member"

    added = client.post(
        f"{path}/members", json={"membership_ids": [bia_id, owner_id]}, headers=_csrf(client)
    )
    assert added.status_code == 200, added.text
    assert len(added.json()["members"]) == 3
    removed = client.delete(f"{path}/members/{bia_id}", headers=_csrf(client))
    assert [member["membership_id"] for member in removed.json()["members"]] == [ana_id, owner_id]

    renamed = client.patch(path, json={"name": "Mídia paga"}, headers=_csrf(client))
    assert renamed.status_code == 200 and renamed.json()["name"] == "Mídia paga"
    assert renamed.json()["description"] is None
    assert [item["name"] for item in client.get("/api/v1/groups").json()["items"]] == ["Mídia paga"]
    assert client.get(path).json()["id"] == group["id"]

    assert ana.delete(path, headers=_csrf(ana)).status_code == 403
    assert client.delete(path, headers=_csrf(client)).status_code == 204
    assert client.get(path).status_code == 404
    actions = [
        entry["action"]
        for entry in client.get("/api/v1/audit").json()["items"]
        if entry["action"].startswith("group.")
    ]
    assert actions[0] == "group.deleted" and actions[-1] == "group.created"
