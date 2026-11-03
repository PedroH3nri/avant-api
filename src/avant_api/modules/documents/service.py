"""Service dos documentos da Empresa ativa: lista, envio e download."""

from avant_core.access.models import Actor
from avant_core.documents.enums import DocumentKind
from avant_core.documents.models import CompanyDocument, DocumentFile
from avant_core.documents.services import (
    get_company_document_file,
    get_company_documents,
    upload_company_document,
)
from avant_core.shared.clock import Clock

from avant_api.app.ports import UnitOfWorkFactory
from avant_api.shared.documents import DocumentOut, DocumentsOut


class DocumentService:
    """Documentos que o cliente Manage Inventory envia para a equipe Groone aprovar."""

    def __init__(self, uows: UnitOfWorkFactory, clock: Clock) -> None:
        self._uows = uows
        self._clock = clock

    def overview(self, actor: Actor) -> DocumentsOut:
        """Os documentos enviados e se a Empresa precisa enviá-los."""
        return DocumentsOut.of(get_company_documents(self._uows.uow(actor.company_id), actor=actor))

    def upload(self, actor: Actor, kind: DocumentKind, name: str, content: bytes) -> DocumentOut:
        """Envia ou troca um documento; ele volta para em análise."""
        document = upload_company_document(
            self._uows.uow(actor.company_id),
            actor=actor,
            kind=kind,
            file=DocumentFile(name, content),
            clock=self._clock,
        )
        return DocumentOut.of(document)

    def file(self, actor: Actor, kind: DocumentKind) -> tuple[CompanyDocument, bytes]:
        """O arquivo de um documento da Empresa ativa."""
        return get_company_document_file(
            self._uows.uow(actor.company_id), actor=actor, kind=kind, clock=self._clock
        )
