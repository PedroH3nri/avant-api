"""Monta o service dos membros com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.members.service import MemberService


def member_service(services: Services = Depends(get_services)) -> MemberService:
    """O service dos membros com o banco e o relógio da aplicação."""
    return MemberService(services, services.clock)
