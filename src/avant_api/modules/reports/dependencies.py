"""Monta o service dos relatórios com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.reports.service import ReportService


def report_service(services: Services = Depends(get_services)) -> ReportService:
    """O service dos relatórios com o banco, o relógio, o limite de taxa e a fila do worker."""
    return ReportService(services, services.clock, services.bucket, services.tasks)
