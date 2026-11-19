"""Monta o service do Google Ads dos clientes com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.google_ads.service import ClientGoogleAdsService


def client_google_ads_service(
    services: Services = Depends(get_services),
) -> ClientGoogleAdsService:
    """O service com o banco e o relógio."""
    return ClientGoogleAdsService(services, services.clock)
