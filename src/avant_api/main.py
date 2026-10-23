"""Aplicação FastAPI. Rodar com:

uvicorn avant_api.main:create_app --factory --host 0.0.0.0 --port 8000 --proxy-headers
"""

from fastapi import FastAPI

from avant_api import errors
from avant_api.logs import configure_logging
from avant_api.middleware import observe
from avant_api.routes import auth, health, invitations, mfa
from avant_api.services import Services
from avant_api.settings import Settings

API_PREFIX = "/api/v1"


def create_app(services: Services | None = None) -> FastAPI:
    if services is None:
        configure_logging()
        services = Services.build(Settings())
    app = FastAPI(
        title="Groone Avant API",
        version="1",
        docs_url="/api/docs",
        openapi_url="/api/v1/openapi.json",
        redoc_url=None,
    )
    app.state.services = services
    errors.install(app)
    app.middleware("http")(observe)
    for module in (health, auth, mfa, invitations):
        app.include_router(module.router, prefix=API_PREFIX)
    return app
