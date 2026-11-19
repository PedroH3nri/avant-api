"""Monta o service e os redirecionamentos do Google Ads com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.google_ads.oauth import GoogleAdsRedirects
from avant_api.modules.google_ads.service import GoogleAdsService


def google_ads_service(services: Services = Depends(get_services)) -> GoogleAdsService:
    """O service do Google Ads com o banco, o relógio, a API do Google Ads e a cifra dos
    tokens."""
    return GoogleAdsService(services, services.clock, services.google_ads, services.google_ads_box)


def google_ads_redirects(services: Services = Depends(get_services)) -> GoogleAdsRedirects:
    """Os redirecionamentos do login do Google com as configurações da aplicação."""
    return GoogleAdsRedirects(services.settings)
