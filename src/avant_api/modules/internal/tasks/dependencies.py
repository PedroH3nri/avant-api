"""Monta o service das tarefas de suporte com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.tasks.service import SupportTaskService


def support_task_service(services: Services = Depends(get_services)) -> SupportTaskService:
    """O service das tarefas com o banco, o relógio e o e-mail da aplicação."""
    return SupportTaskService(services, services.clock, services.mailer)
