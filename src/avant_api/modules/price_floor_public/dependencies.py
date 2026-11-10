"""Monta o service da rota pública dos floors com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.price_floor_public.service import PublicPriceFloorService


def public_price_floor_service(
    services: Services = Depends(get_services),
) -> PublicPriceFloorService:
    """O service com o banco, o cache, o limite por IP e o país pelo IP."""
    return PublicPriceFloorService(services, services.rewards, services.bucket, services.countries)
