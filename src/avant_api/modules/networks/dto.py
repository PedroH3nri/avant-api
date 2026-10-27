"""DTOs de entrada e saída do domínio networks. Datas sempre em ISO 8601 UTC."""

import uuid
from datetime import datetime

from avant_core.gam.model import (
    ConnectionType,
    Delegation,
    Network,
    NetworkStatus,
    NetworkSyncRun,
    SyncKind,
    SyncStatus,
)
from avant_core.gam.service import NetworkView
from pydantic import BaseModel, Field


class SyncRunOut(BaseModel):
    id: uuid.UUID
    kind: SyncKind
    status: SyncStatus
    started_at: datetime
    finished_at: datetime | None
    counts: dict[str, int]
    error_code: str | None
    error_message: str | None

    @classmethod
    def of(cls, run: NetworkSyncRun) -> "SyncRunOut":
        """Monta uma execução de sincronização."""
        return cls(
            id=run.id,
            kind=run.kind,
            status=run.status,
            started_at=run.started_at,
            finished_at=run.finished_at,
            counts=dict(run.counts),
            error_code=run.error_code,
            error_message=run.error_message,
        )


class NetworkOut(BaseModel):
    id: uuid.UUID
    network_code: str
    display_name: str | None
    connection_type: ConnectionType
    delegation: Delegation | None
    status: NetworkStatus
    last_error: str | None
    failures: int
    last_checked_at: datetime | None
    last_synced_at: datetime | None
    sync_requested_at: datetime | None
    created_at: datetime

    @classmethod
    def of(cls, network: Network) -> "NetworkOut":
        """Monta a network."""
        return cls(
            id=network.id,
            network_code=network.network_code,
            display_name=network.display_name,
            connection_type=network.connection_type,
            delegation=network.delegation,
            status=network.status,
            last_error=network.last_error,
            failures=network.failures,
            last_checked_at=network.last_checked_at,
            last_synced_at=network.last_synced_at,
            sync_requested_at=network.sync_requested_at,
            created_at=network.created_at,
        )


class NetworkDetailOut(NetworkOut):
    # Quantos sites ativos a network tem.
    sites: int
    last_runs: dict[SyncKind, SyncRunOut]

    @classmethod
    def of_view(cls, view: NetworkView) -> "NetworkDetailOut":
        """Monta a network com os sites ativos e as últimas sincronizações."""
        return cls(
            **NetworkOut.of(view.network).model_dump(),
            sites=view.sites,
            last_runs={kind: SyncRunOut.of(run) for kind, run in view.last_runs.items()},
        )


class NetworkIn(BaseModel):
    network_code: str = Field(min_length=1, max_length=20)


class ServiceAccountOut(BaseModel):
    """O que o guia de conexão mostra: o e-mail a adicionar como administrador no GAM."""

    email: str
    role: str = "Administrator"
