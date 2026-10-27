"""Imagem da Empresa contra o Postgres: o cliente na Empresa ativa e a Groone no painel interno."""

from io import BytesIO

from fastapi.testclient import TestClient
from PIL import Image
from sqlalchemy import Engine

from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_internal import _staff
from tests.test_team import _member_client


def _png(width: int, height: int) -> bytes:
    """Uma imagem PNG de uma cor só no tamanho pedido."""
    output = BytesIO()
    Image.new("RGB", (width, height), (200, 40, 40)).save(output, format="PNG")
    return output.getvalue()


def _put_image(client: TestClient, path: str, content: bytes) -> dict[str, object]:
    """Envia a imagem crua no corpo do PUT e devolve a resposta em JSON."""
    response = client.put(
        path, content=content, headers={**_csrf(client), "Content-Type": "image/png"}
    )
    assert response.status_code == 200, response.text
    return response.json()  # type: ignore[no-any-return]


def test_client_changes_the_company_image(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    _onboard_owner(client, engine, mailer)
    ana = _member_client(client, mailer, "ana@acai.com")
    assert client.get("/api/v1/company").json()["image_url"] is None
    assert client.get("/api/v1/company/image").status_code == 404

    denied = ana.put("/api/v1/company/image", content=_png(10, 10), headers=_csrf(ana))
    assert denied.status_code == 403

    company = _put_image(client, "/api/v1/company/image", _png(400, 200))
    image_url = str(company["image_url"])
    assert image_url.startswith("/api/v1/company/image?v=")
    image = client.get(image_url)
    assert image.status_code == 200 and image.headers["content-type"] == "image/webp"
    assert "immutable" in image.headers["cache-control"]
    with Image.open(BytesIO(image.content)) as stored:
        assert stored.format == "WEBP" and stored.size == (256, 256)
    cached = client.get(image_url, headers={"If-None-Match": image.headers["etag"]})
    assert cached.status_code == 304

    me = ana.get("/api/v1/auth/me").json()
    picture_url = me["companies"][0]["image_url"]
    assert picture_url.startswith(f"/api/v1/auth/me/companies/{company['id']}/image?v=")
    assert ana.get(picture_url).content == image.content
    assert ana.get("/api/v1/company/image").status_code == 200

    invalid = client.put("/api/v1/company/image", content=b"%PDF-1.4", headers=_csrf(client))
    assert invalid.status_code == 422 and invalid.json()["error"]["code"] == "invalid_image"
    too_large = client.put(
        "/api/v1/company/image", content=b"0" * (2 * 1024 * 1024 + 1), headers=_csrf(client)
    )
    assert too_large.status_code == 413
    assert too_large.json()["error"]["code"] == "image_too_large"

    removed = client.delete("/api/v1/company/image", headers=_csrf(client))
    assert removed.status_code == 200 and removed.json()["image_url"] is None
    assert client.get("/api/v1/company/image").status_code == 404
    actions = [
        entry["action"]
        for entry in client.get("/api/v1/audit").json()["items"]
        if entry["action"].startswith("company.image")
    ]
    assert actions == ["company.image_removed", "company.image_changed"]


def test_groone_changes_the_image_of_a_client(
    client: TestClient, engine: Engine, mailer: CapturingMailer
) -> None:
    staff = _staff(client, engine)
    owner = TestClient(client.app)
    company_id = _onboard_owner(owner, engine, mailer)["companies"][0]["id"]

    assert owner.put(
        f"/api/v1/internal/clients/{company_id}/image", content=_png(5, 5), headers=_csrf(owner)
    ).status_code in (403, 404)

    detail = _put_image(staff, f"/api/v1/internal/clients/{company_id}/image", _png(64, 64))
    image_url = str(detail["image_url"])
    assert image_url.startswith(f"/api/v1/internal/clients/{company_id}/image?v=")
    assert staff.get(image_url).status_code == 200
    listed = staff.get("/api/v1/internal/clients").json()["items"]
    assert [item["image_url"] for item in listed] == [image_url]
    assert owner.get("/api/v1/company").json()["image_url"] is not None

    removed = staff.delete(f"/api/v1/internal/clients/{company_id}/image", headers=_csrf(staff))
    assert removed.status_code == 200 and removed.json()["image_url"] is None
    assert staff.get(image_url).status_code == 404
