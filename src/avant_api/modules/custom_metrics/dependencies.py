"""Monta o service das métricas personalizadas com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.custom_metrics.service import CustomMetricService


def custom_metric_service(services: Services = Depends(get_services)) -> CustomMetricService:
    """O service das métricas personalizadas com o banco e o relógio da aplicação."""
    return CustomMetricService(services, services.clock)
