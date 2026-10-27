"""Aplicação FastAPI. Rodar com:

uvicorn avant_api.main:create_app --factory --host 0.0.0.0 --port 8000 --proxy-headers
"""

from fastapi import FastAPI

from avant_api.app import errors
from avant_api.app.container import Services
from avant_api.app.logs import configure_logging
from avant_api.app.middleware import observe
from avant_api.app.settings import Settings
from avant_api.modules.account.controller import router as account
from avant_api.modules.api_keys.controller import router as api_keys
from avant_api.modules.audit.controller import router as audit
from avant_api.modules.auth.controller import router as auth
from avant_api.modules.company.controller import router as company
from avant_api.modules.costs.controller import router as costs
from avant_api.modules.currencies.controller import router as currencies
from avant_api.modules.events.controller import router as events
from avant_api.modules.groups.controller import router as groups
from avant_api.modules.health.controller import router as health
from avant_api.modules.internal.router import router as internal
from avant_api.modules.invitations.controller import router as invitations
from avant_api.modules.members.controller import router as members
from avant_api.modules.mfa.controller import router as mfa
from avant_api.modules.networks.controller import router as networks
from avant_api.modules.profile.controller import router as profile
from avant_api.modules.reports.controller import router as reports
from avant_api.modules.results.controller import router as results
from avant_api.modules.roles.controller import router as roles
from avant_api.modules.sites.controller import router as sites
from avant_api.shared.dto import API_PATH

API_PREFIX = API_PATH


def create_app(services: Services | None = None) -> FastAPI:
    """Monta a aplicação FastAPI com serviços, rotas, erros e middleware."""
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
    for router in (
        health,
        auth,
        account,
        profile,
        mfa,
        company,
        members,
        invitations,
        roles,
        groups,
        audit,
        networks,
        sites,
        reports,
        currencies,
        costs,
        results,
        api_keys,
        events,
        internal,
    ):
        app.include_router(router, prefix=API_PREFIX)
    return app
