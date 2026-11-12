"""Arquivos do Swagger UI servidos pela própria API: cópia do ``swagger-ui-dist`` com versão
exata e SHA-256 conferido na subida. Arquivo alterado derruba a subida, em todo ambiente."""

import base64
import hashlib
from dataclasses import dataclass
from pathlib import Path

SWAGGER_UI_VERSION = "5.34.0"
ASSETS_DIR = Path(__file__).parent / "swagger_ui"
BUNDLE = "swagger-ui-bundle.js"
STYLESHEET = "swagger-ui.css"
INITIALIZER = "avant-init.js"
JAVASCRIPT = "text/javascript; charset=utf-8"
CSS = "text/css; charset=utf-8"


@dataclass(frozen=True)
class ExpectedAsset:
    """Um arquivo do Swagger UI: tipo de conteúdo e o SHA-256 esperado."""

    media_type: str
    sha256: str


@dataclass(frozen=True)
class SwaggerAsset:
    """Um arquivo já lido e conferido, com o ``integrity`` (SRI) para a página."""

    content: bytes
    media_type: str
    integrity: str


EXPECTED_ASSETS = {
    BUNDLE: ExpectedAsset(
        JAVASCRIPT, "3f6abf70480db7e07914df4c98a77385f22ea585eaf457a3e6415ba0eae2d167"
    ),
    STYLESHEET: ExpectedAsset(
        CSS, "c3cfe8248c4b0b89673600fb829924eafbac6de4bc4b2b06f5f5243483074d0a"
    ),
    INITIALIZER: ExpectedAsset(
        JAVASCRIPT, "767bb2dd8fc69f7d2a2584f1dcbb481295e3489903fa120754846af0cf9b144e"
    ),
}


class SwaggerAssetChanged(Exception):
    """Um arquivo do Swagger UI não confere com o SHA-256 fixado."""


def load_assets(directory: Path = ASSETS_DIR) -> dict[str, SwaggerAsset]:
    """Lê os arquivos do Swagger UI e confere o SHA-256 de cada um; recusa o que mudou."""
    loaded: dict[str, SwaggerAsset] = {}
    for name, expected in EXPECTED_ASSETS.items():
        content = (directory / name).read_bytes()
        if hashlib.sha256(content).hexdigest() != expected.sha256:
            raise SwaggerAssetChanged(f"{name} não confere com o SHA-256 fixado")
        digest = base64.b64encode(hashlib.sha384(content).digest()).decode()
        loaded[name] = SwaggerAsset(content, expected.media_type, f"sha384-{digest}")
    return loaded
