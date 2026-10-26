"""Interfaces que os services da API recebem: o service depende delas, nunca do container."""

import uuid
from typing import Protocol

from avant_core.ports import UnitOfWork


class UnitOfWorkFactory(Protocol):
    def uow(self, company_id: uuid.UUID) -> UnitOfWork:
        """Transação presa à Empresa ativa (RLS)."""
        ...

    def trusted_uow(self) -> UnitOfWork:
        """Transação sem RLS, para login, conta, convite e painel interno."""
        ...
