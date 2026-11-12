"""Imagem da Empresa contra o Postgres: o cliente na Empresa ativa e a Groone no painel interno."""

import gzip
import uuid
from io import BytesIO
from pathlib import Path

import pytest
from avant_core.shared.errors import InvalidImage
from fastapi.testclient import TestClient
from PIL import Image, ImageChops, ImageStat
from sqlalchemy import Engine

from avant_api.app.images import PillowImageProcessor
from tests.conftest import CapturingMailer
from tests.test_api import _csrf, _onboard_owner
from tests.test_internal import _staff
from tests.test_team import _member_client

FIXTURES = Path(__file__).parent / "fixtures"


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


def test_upload_without_session_is_refused_before_reading_the_body(client: TestClient) -> None:
    big = b"x" * (6 * 1024 * 1024)
    for path in (
        "/api/v1/auth/me/image",
        "/api/v1/company/image",
        "/api/v1/company/documents/identity",
        f"/api/v1/internal/clients/{uuid.uuid4()}/image",
    ):
        anonymous = client.put(path, content=big, headers={"Content-Type": "image/png"})
        assert anonymous.status_code == 401, (path, anonymous.text)


def _jpeg(width: int, height: int, *, progressive: bool = False) -> bytes:
    """Uma foto JPEG de uma cor só no tamanho pedido, como a de um celular."""
    output = BytesIO()
    image = Image.new("RGB", (width, height), (40, 120, 200))
    image.save(output, format="JPEG", quality=85, progressive=progressive)
    return output.getvalue()


def _three_scans() -> bytes:
    """JPEG comum (SOF0) de 3500 x 2600 com uma varredura por componente, feito com
    ``jpegtran -scans``: o Pillow não marca ``progressive``, mas o libjpeg guarda tudo."""
    return gzip.decompress((FIXTURES / "sequential_three_scans.jpg.gz").read_bytes())


def _with_exif_thumbnail(jpeg: bytes) -> bytes:
    """O JPEG com um APP1 cuja miniatura tem SOS próprio: não pode contar como varredura."""
    thumbnail = b"Exif\x00\x00" + b"\xff\xd8\xff\xda\x00\x02\x00\xff\xda\x00\x02\xff\xd9"
    segment = b"\xff\xe1" + (len(thumbnail) + 2).to_bytes(2, "big") + thumbnail
    return jpeg[:2] + segment + jpeg[2:]


def test_sequential_jpeg_with_many_scans_has_the_progressive_limit() -> None:
    processor = PillowImageProcessor()
    with Image.open(BytesIO(_three_scans())) as opened:
        assert opened.size == (3500, 2600) and "progressive" not in opened.info
    with pytest.raises(InvalidImage, match="pixels demais"):
        processor.square_webp(_three_scans(), 256)
    photo = _with_exif_thumbnail(_jpeg(4032, 3024))
    with Image.open(BytesIO(processor.square_webp(photo, 256))) as result:
        assert result.size == (256, 256)


def _striped_logo(width: int, height: int, mode: str) -> bytes:
    """Uma logo PNG com listras verticais de 4 px, para medir a nitidez depois de reduzir."""
    image = Image.new("RGB", (width, height), (255, 255, 255))
    for x in range(0, width, 8):
        image.paste((0, 0, 0), (x, 0, x + 4, height))
    output = BytesIO()
    (image.convert("P") if mode == "P" else image).save(output, format="PNG")
    return output.getvalue()


def _sharpness(webp: bytes) -> float:
    """O desvio padrão dos tons de cinza: quanto mais borrada, menor."""
    with Image.open(BytesIO(webp)) as result:
        return float(ImageStat.Stat(result.convert("L")).stddev[0])


def test_phone_photos_pass_and_huge_pngs_are_refused() -> None:
    processor = PillowImageProcessor()
    with Image.open(BytesIO(processor.square_webp(_jpeg(4032, 3024), 256))) as result:
        assert result.size == (256, 256)
    for huge in (_jpeg(4032, 3024, progressive=True), _jpeg(6000, 5000)):
        with pytest.raises(InvalidImage):
            processor.square_webp(huge, 256)
    with pytest.raises(InvalidImage):
        processor.square_webp(_png(4000, 2600), 256)
    with Image.open(BytesIO(processor.square_webp(_png(3000, 2500), 256))) as result:
        assert result.size == (256, 256)


def test_wide_and_palette_logos_stay_sharp() -> None:
    processor = PillowImageProcessor()
    assert _sharpness(processor.square_webp(_striped_logo(2400, 300, "RGB"), 256)) > 100
    rgb = processor.square_webp(_striped_logo(4000, 1100, "RGB"), 256)
    palette = processor.square_webp(_striped_logo(4000, 1100, "P"), 256)
    with Image.open(BytesIO(rgb)) as first, Image.open(BytesIO(palette)) as second:
        difference = ImageChops.difference(first.convert("L"), second.convert("L"))
        assert ImageStat.Stat(difference).mean[0] < 3


def test_phone_rotation_from_exif_is_kept() -> None:
    photo = Image.new("RGB", (400, 200), (0, 0, 255))
    photo.paste((255, 0, 0), (0, 0, 200, 200))
    exif = Image.Exif()
    exif[0x0112] = 6
    output = BytesIO()
    photo.save(output, format="JPEG", exif=exif.tobytes())
    square = PillowImageProcessor().square_webp(output.getvalue(), 64)
    with Image.open(BytesIO(square)) as result:
        pixels = result.convert("RGB")
        top, bottom = pixels.getpixel((32, 4)), pixels.getpixel((32, 60))
    assert isinstance(top, tuple) and isinstance(bottom, tuple)
    assert top[0] > 200 and bottom[2] > 200
