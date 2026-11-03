"""DTOs dos documentos da Empresa ativa; o formato fica em ``shared/documents.py`` porque o
painel interno usa o mesmo."""

from avant_api.shared.documents import DocumentOut, DocumentsOut

__all__ = ["DocumentOut", "DocumentsOut"]
