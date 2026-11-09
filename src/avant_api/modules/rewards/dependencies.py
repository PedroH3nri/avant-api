"""Monta o service dos rewards com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.rewards.service import RewardService


def reward_service(services: Services = Depends(get_services)) -> RewardService:
    """O service dos rewards com o banco, o relógio, as imagens e o cache das páginas."""
    return RewardService(services, services.clock, services.images, services.rewards)
