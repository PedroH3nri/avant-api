"""Monta o service dos rewards dos clientes com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.rewards.service import ClientRewardService


def client_reward_service(services: Services = Depends(get_services)) -> ClientRewardService:
    """O service com o banco, o relógio, as imagens e o cache das páginas."""
    return ClientRewardService(services, services.clock, services.images, services.rewards)
