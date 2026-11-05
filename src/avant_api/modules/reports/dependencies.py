"""Monta o service dos relatórios com os adaptadores da aplicação."""

from fastapi import Depends, Request

from avant_api.app.container import Services
from avant_api.app.security import get_services, known_companies
from avant_api.modules.reports.service import ReportService


def report_service(request: Request, services: Services = Depends(get_services)) -> ReportService:
    """O service dos relatórios com o banco, o relógio, o limite de taxa, a fila do worker e o
    que a autenticação já sabe da Empresa ativa."""
    return ReportService(
        services, services.clock, services.bucket, services.tasks, lambda: known_companies(request)
    )
