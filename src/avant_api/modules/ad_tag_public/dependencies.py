"""Monta o service da rota pública da ad tag com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.ad_tag_public.service import PublicAdTagService


def public_ad_tag_service(services: Services = Depends(get_services)) -> PublicAdTagService:
    """O service com o banco, o cache, o buffer das visitas e o limite por IP."""
    return PublicAdTagService(
        services,
        services.clock,
        services.rewards,
        services.page_views,
        services.bucket,
        groone_network_code=services.settings.gam_groone_network_code,
    )
