"""Monta o service dos alertas com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.alerts.service import AlertService
from avant_api.modules.reports.dependencies import report_service
from avant_api.modules.reports.service import ReportService


def alert_service(
    services: Services = Depends(get_services),
    reports: ReportService = Depends(report_service),
) -> AlertService:
    """O service dos alertas com o banco, o relógio e o service dos relatórios."""
    return AlertService(services, services.clock, reports)
