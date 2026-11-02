"""Monta o service dos dashboards com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.dashboards.service import DashboardService
from avant_api.modules.reports.dependencies import report_service
from avant_api.modules.reports.service import ReportService


def dashboard_service(
    services: Services = Depends(get_services),
    reports: ReportService = Depends(report_service),
) -> DashboardService:
    """O service dos dashboards com o banco, o relógio e o service dos relatórios."""
    return DashboardService(services, services.clock, reports)
