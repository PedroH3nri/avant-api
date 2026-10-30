"""Monta o service das invoices com os adaptadores da aplicação."""

from fastapi import Depends

from avant_api.app.container import Services
from avant_api.app.security import get_services
from avant_api.modules.internal.invoices.service import InvoiceService


def invoice_service(services: Services = Depends(get_services)) -> InvoiceService:
    """O service das invoices com o banco, o e-mail e o relógio da aplicação."""
    return InvoiceService(services, services.mailer, services.clock)
