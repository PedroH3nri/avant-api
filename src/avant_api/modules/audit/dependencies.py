"""Monta o service da auditoria com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.audit.service import AuditService


def audit_service(services: Services = Depends(get_services)) -> AuditService:
    """O service da auditoria com o banco da aplicação."""
    return AuditService(services)
