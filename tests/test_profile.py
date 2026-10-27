"""Aparência do painel e foto de perfil contra o Postgres."""

from io import BytesIO

from fastapi.testclient import TestClient
from PIL import Image
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_team import _member_client


def _png() -> bytes:
    """Uma foto PNG pequena de uma cor só."""
    output = BytesIO()
    Image.new("RGB", (300, 200), (20, 120, 220)).save(output, format="PNG")
    return output.getvalue()


def test_appearance_belongs_to_the_person(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    ana = _member_client(client, mailer, "ana@acai.com")
    me = client.get("/api/v1/auth/me").json()
    assert (me["theme"], me["accent"]) == ("system", "default")
    assert "accent_color" not in client.get("/api/v1/company").json()

    changed = ana.patch(
        "/api/v1/auth/appearance", json={"theme": "dark", "accent": "green"}, headers=_csrf(ana)
    )
    assert changed.status_code == 200
    assert changed.json() == {"theme": "dark", "accent": "green", "locale": "pt"}
    me = ana.get("/api/v1/auth/me").json()
    assert (me["theme"], me["accent"]) == ("dark", "green")
    language = ana.patch("/api/v1/auth/appearance", json={"locale": "es"}, headers=_csrf(ana))
    assert language.json()["locale"] == "es"
    assert ana.get("/api/v1/auth/me").json()["user"]["locale"] == "es"
    assert client.get("/api/v1/auth/me").json()["accent"] == "default"

    invalid = ana.patch("/api/v1/auth/appearance", json={"accent": "#ff0000"}, headers=_csrf(ana))
    assert invalid.status_code == 422
    assert TestClient(client.app).patch("/api/v1/auth/appearance", json={}).status_code == 401


def test_profile_picture(client: TestClient, engine: Engine, mailer: CapturingMailer) -> None:
    _onboard_owner(client, engine, mailer)
    ana = _member_client(client, mailer, "ana@acai.com")
    me = ana.get("/api/v1/auth/me").json()
    assert me["user"]["image_url"] is None

    response = ana.put(
        "/api/v1/auth/me/image",
        content=_png(),
        headers={**_csrf(ana), "Content-Type": "image/png"},
    )
    assert response.status_code == 200, response.text
    image_url = response.json()["image_url"]
    assert image_url.startswith(f"/api/v1/users/{me['user']['id']}/image?v=")

    own = ana.get(image_url)
    assert own.status_code == 200 and own.headers["content-type"] == "image/webp"
    with Image.open(BytesIO(own.content)) as stored:
        assert stored.size == (256, 256)
    assert client.get(image_url).content == own.content
    members = client.get("/api/v1/members").json()["items"]
    assert [member["user"]["image_url"] for member in members] == [None, image_url]

    outsider = TestClient(client.app)
    assert outsider.get(image_url).status_code == 401

    invalid = ana.put("/api/v1/auth/me/image", content=b"%PDF-1.4", headers=_csrf(ana))
    assert invalid.status_code == 422 and invalid.json()["error"]["code"] == "invalid_image"

    removed = ana.delete("/api/v1/auth/me/image", headers=_csrf(ana))
    assert removed.status_code == 200 and removed.json()["image_url"] is None
    assert ana.get(image_url).status_code == 404
