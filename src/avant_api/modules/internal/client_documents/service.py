"""Service dos documentos dos clientes no painel interno: lista, download e decisão.

Usa ``trusted_uow()`` (sem RLS) porque a Groone enxerga todas as Empresas; o core confere
``ensure_staff`` em cada caso de uso.
"""

import uuid

from avant_core.access.models import Actor
from avant_core.documents.enums import DocumentKind
from avant_core.documents.models import CompanyDocument
from avant_core.internal.services import (
    approve_client_document,
    get_client_document_file,
    get_client_documents,
    reject_client_document,
)
from avant_core.ports import Mailer
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.modules.internal.client_documents.dto import ClientDocumentOut, ClientDocumentsOut


class ClientDocumentService:
    """Documentos que a equipe Groone confere e aprova ou recusa."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock, mailer: Mailer) -> None:
        self._uows = uows
        self._clock = clock
        self._mailer = mailer

    def overview(self, actor: Actor, company_id: uuid.UUID) -> ClientDocumentsOut:
        """Os documentos do cliente e se ele precisa enviá-los."""
        overview = get_client_documents(
            self._uows.trusted_uow(), actor=actor, company_id=company_id
        )
        return ClientDocumentsOut.of(overview)

    def file(
        self, actor: Actor, company_id: uuid.UUID, kind: DocumentKind
    ) -> tuple[CompanyDocument, bytes]:
        """O arquivo de um documento do cliente."""
        return get_client_document_file(
            self._uows.trusted_uow(),
            actor=actor,
            company_id=company_id,
            kind=kind,
            clock=self._clock,
        )

    def approve(self, actor: Actor, company_id: uuid.UUID, kind: DocumentKind) -> ClientDocumentOut:
        """Aprova o documento em análise e avisa quem enviou por e-mail."""
        document = approve_client_document(
            self._uows.trusted_uow(),
            actor=actor,
            company_id=company_id,
            kind=kind,
            clock=self._clock,
            mailer=self._mailer,
        )
        return ClientDocumentOut.of(document)

    def reject(
        self, actor: Actor, company_id: uuid.UUID, kind: DocumentKind, reason: str
    ) -> ClientDocumentOut:
        """Recusa o documento com o motivo e avisa quem enviou por e-mail."""
        document = reject_client_document(
            self._uows.trusted_uow(),
            actor=actor,
            company_id=company_id,
            kind=kind,
            reason=reason,
            clock=self._clock,
            mailer=self._mailer,
        )
        return ClientDocumentOut.of(document)
