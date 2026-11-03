"""Monta o service dos modelos prontos de dashboard com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.dashboard_templates.service import DashboardTemplateService


def dashboard_template_service(
    services: Services = Depends(get_services),
) -> DashboardTemplateService:
    """O service dos modelos com o banco e o relógio da aplicação."""
    return DashboardTemplateService(services, services.clock)
