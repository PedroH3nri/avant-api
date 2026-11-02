"""Monta o service dos envios agendados com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.schedules.service import ScheduleService


def schedule_service(services: Services = Depends(get_services)) -> ScheduleService:
    """O service dos envios agendados com o banco e o relógio."""
    return ScheduleService(services, services.clock)
