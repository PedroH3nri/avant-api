"""Swagger servido pela própria API: arquivos fixados e conferidos, página sem CDN e sem script
inline, com CSP própria."""

import base64
import hashlib
import re
import shutil
from pathlib import Path

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import Engine

from avant_api.app.middleware import DOCS_CONTENT_SECURITY_POLICY
from avant_api.modules.api_docs.swagger_assets import (
    ASSETS_DIR,
    EXPECTED_ASSETS,
    SwaggerAssetChanged,
    load_assets,
)
from tests.conftest import browser
from tests.test_internal import _staff


def test_docs_policy_allows_only_the_api_itself() -> None:
    directives = dict(
        directive.strip().split(" ", 1) for directive in DOCS_CONTENT_SECURITY_POLICY.split(";")
    )
    assert directives["script-src"] == "'self'"
    assert directives["connect-src"] == "'self'"
    assert directives["frame-ancestors"] == "'none'"
    assert directives["default-src"] == "'none'"


def test_changed_asset_stops_the_start(tmp_path: Path) -> None:
    for name in EXPECTED_ASSETS:
        shutil.copy(ASSETS_DIR / name, tmp_path / name)
    assert set(load_assets(tmp_path)) == set(EXPECTED_ASSETS)
    bundle = tmp_path / "swagger-ui-bundle.js"
    bundle.write_bytes(bundle.read_bytes() + b"\nfetch('https://exemplo.invalido');")
    with pytest.raises(SwaggerAssetChanged):
        load_assets(tmp_path)


def test_page_loads_only_checked_files_from_the_api(client: TestClient, engine: Engine) -> None:
    staff = browser(client.app, cookies=_staff(client, engine).cookies)
    page = staff.get("/api/docs")
    assert page.status_code == 200
    assert page.headers["Content-Security-Policy"] == DOCS_CONTENT_SECURITY_POLICY
    html = page.text
    assert "cdn" not in html.lower() and "http" not in html
    assert re.search(r"<script>", html) is None
    references = re.findall(r'(?:src|href)="([^"]+)"\s+integrity="([^"]+)"', html)
    assert len(references) == 3
    for path, integrity in references:
        assert path.startswith("/api/docs/assets/")
        asset = staff.get(path)
        assert asset.status_code == 200, path
        digest = base64.b64encode(hashlib.sha384(asset.content).digest()).decode()
        assert integrity == f"sha384-{digest}"
    assert staff.get("/api/docs/assets/package.json").status_code == 404
    assert browser(client.app).get("/api/docs/assets/swagger-ui.css").status_code == 401
