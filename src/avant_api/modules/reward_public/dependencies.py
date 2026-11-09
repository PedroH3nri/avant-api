"""Monta o service das rotas públicas do reward com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.reward_public.service import PublicRewardService


def public_reward_service(services: Services = Depends(get_services)) -> PublicRewardService:
    """O service com o banco, o cache, o buffer, o limite por IP e a URL do Avant."""
    return PublicRewardService(
        services,
        services.clock,
        services.rewards,
        services.reward_events,
        services.bucket,
        base_url=services.settings.app_base_url,
        groone_network_code=services.settings.gam_groone_network_code,
    )
