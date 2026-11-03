"""Monta o service do checklist de domínio com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.checklists.service import SiteChecklistService


def site_checklist_service(services: Services = Depends(get_services)) -> SiteChecklistService:
    """O service do checklist com o banco, o relógio e a fila do worker."""
    return SiteChecklistService(services, services.clock, services.tasks)
