"""Monta o service das metas com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.goals.service import GoalService


def goal_service(services: Services = Depends(get_services)) -> GoalService:
    """O service das metas com o banco e o relógio da aplicação."""
    return GoalService(services, services.clock)
