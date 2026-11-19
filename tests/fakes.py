"""Fakes em memória dos adaptadores da API, só para os testes: o ``Services`` de produção
não tem nenhum padrão, e a fábrica ``memory_services`` do conftest monta estes."""

import asyncio
import math
import threading
import time
from collections.abc import AsyncIterator
from dataclasses import dataclass, field
from datetime import date, datetime
from typing import Any

from avant_core.facebook.enums import FacebookAccountState, FacebookLevel, FacebookListKind
from avant_core.facebook.models import (
    FacebookAccountData,
    FacebookCountryRow,
    FacebookDraft,
    FacebookDraftAd,
    FacebookDraftAdset,
    FacebookInsightRow,
    FacebookObjectData,
    FacebookOption,
    FacebookToken,
)

from avant_api.app.limits import BucketResult, BucketRule


class MemoryCounter:
    def __init__(self) -> None:
        self._data: dict[str, tuple[int, float]] = {}
        self._lock = threading.Lock()

    def get(self, key: str) -> tuple[int, int]:
        """Devolve as tentativas na janela e os segundos que faltam para ela acabar."""
        with self._lock:
            count, until = self._data.get(key, (0, 0.0))
            left = until - time.monotonic()
            return (count, math.ceil(left)) if left > 0 else (0, 0)

    def incr(self, key: str, window_seconds: int) -> tuple[int, int]:
        """Soma uma tentativa, abrindo a janela se for a primeira; devolve como get."""
        with self._lock:
            count, until = self._data.get(key, (0, 0.0))
            now = time.monotonic()
            if until <= now:
                count, until = 0, now + window_seconds
            self._data[key] = (count + 1, until)
            return count + 1, math.ceil(until - now)

    def reserve(self, entries: list[tuple[str, int, int]]) -> int:
        """Confere todas as chaves e só soma se nenhuma estiver no limite, sob a mesma trava."""
        with self._lock:
            now = time.monotonic()
            for key, limit, _ in entries:
                count, until = self._data.get(key, (0, 0.0))
                if until > now and count >= limit:
                    return max(math.ceil(until - now), 1)
            for key, _, window_seconds in entries:
                count, until = self._data.get(key, (0, 0.0))
                if until <= now:
                    count, until = 0, now + window_seconds
                self._data[key] = (count + 1, until)
            return 0

    def decr(self, key: str) -> None:
        """Devolve uma tentativa reservada, sem passar de zero."""
        with self._lock:
            count, until = self._data.get(key, (0, 0.0))
            if count > 0:
                self._data[key] = (count - 1, until)

    def delete(self, key: str) -> None:
        """Zera o contador."""
        with self._lock:
            self._data.pop(key, None)


class MemoryBucket:
    """Testes: o balde em memória, um por processo."""

    def __init__(self) -> None:
        self._tokens: dict[str, tuple[float, float]] = {}
        self._denied: dict[str, tuple[int, float]] = {}
        self._blocked: dict[str, float] = {}
        self._lock = threading.Lock()

    def take(self, subject: str, rule: BucketRule, now: float) -> BucketResult:
        """Tira uma ficha do balde do sujeito, ou diz quanto esperar."""
        with self._lock:
            until = self._blocked.get(subject, 0.0)
            if until > now:
                return BucketResult(False, 0, math.ceil(until - now))
            tokens, ts = self._tokens.get(subject, (float(rule.burst), now))
            tokens = min(float(rule.burst), tokens + (now - ts) * rule.rate)
            if tokens >= 1:
                self._tokens[subject] = (tokens - 1, now)
                return BucketResult(True, math.floor(tokens - 1), 0)
            self._tokens[subject] = (tokens, now)
            count, start = self._denied.get(subject, (0, now))
            if now - start >= 60:
                count, start = 0, now
            count += 1
            self._denied[subject] = (count, start)
            if count > rule.abuse_limit:
                self._blocked[subject] = now + rule.block_seconds
                self._denied.pop(subject, None)
                return BucketResult(False, 0, rule.block_seconds)
            return BucketResult(False, 0, math.ceil((1 - tokens) / rule.rate))


@dataclass
class RecordingQueue:
    """Testes: guarda o que seria enfileirado."""

    sent: list[tuple[str, tuple[Any, ...]]] = field(default_factory=list)
    masked: list[str] = field(default_factory=list)
    offline: bool = False

    def send(self, name: str, *args: Any, masked: bool = False) -> bool:
        """Guarda a tarefa em memória, para os testes conferirem; ``offline`` simula a fila fora do
        ar. As tarefas com argumentos mascarados ficam também em ``masked``."""
        if self.offline:
            return False
        self.sent.append((name, args))
        if masked:
            self.masked.append(name)
        return True


class NoEvents:
    """Testes: a conexão fica aberta só com o heartbeat, sem evento."""

    async def listen(self, channel: str, *, timeout: float) -> AsyncIterator[str | None]:
        """Nunca tem evento: só entrega None a cada tempo limite."""
        while True:
            await asyncio.sleep(timeout)
            yield None


@dataclass
class MemoryKeyValueBuffer:
    """Testes: as networks conectadas e o buffer em memória."""

    connected: set[str] = field(default_factory=set)
    buffered: dict[str, set[str]] = field(default_factory=dict)

    def is_connected(self, network_code: str) -> bool:
        """Diz se a network está no conjunto em memória."""
        return network_code in self.connected

    def push(self, network_code: str, pairs: set[str]) -> None:
        """Guarda os pares em memória."""
        self.buffered.setdefault(network_code, set()).update(pairs)


@dataclass
class MemoryRewardCache:
    """Testes: o cache em memória, sem prazo."""

    values: dict[str, str] = field(default_factory=dict)

    def get(self, key: str) -> str | None:
        """Lê da memória."""
        return self.values.get(key)

    def set(self, key: str, value: str, ttl_seconds: int) -> None:
        """Grava na memória."""
        self.values[key] = value

    def delete(self, *keys: str) -> None:
        """Apaga da memória."""
        for key in keys:
            self.values.pop(key, None)


@dataclass
class MemoryRewardBuffer:
    """Testes: a lista em memória."""

    items: list[str] = field(default_factory=list)

    def push(self, items: list[str]) -> bool:
        """Guarda na memória."""
        self.items.extend(items)
        return bool(items)


class FakeFacebook:
    """A Graph API com uma conta, uma campanha com um conjunto e um anúncio e os números."""

    def __init__(self) -> None:
        self.codes: list[tuple[str, str]] = []
        self.revoked: list[str] = []
        self.calls: list[tuple[str, ...]] = []

    def exchange_code(self, code: str, redirect_uri: str) -> FacebookToken:
        """Guarda o código e devolve um token de longa duração."""
        self.codes.append((code, redirect_uri))
        return FacebookToken("token-1", None, "fb-1", "Dono no Facebook")

    def ad_accounts(self, token: str) -> list[FacebookAccountData]:
        """Uma conta em reais."""
        return [
            FacebookAccountData(
                "act_123",
                "CA 01",
                "bm-1",
                "BM Blog",
                "BRL",
                "America/Sao_Paulo",
                FacebookAccountState.ACTIVE,
            )
        ]

    def objects(
        self, token: str, account_external_id: str, currency: str, since: datetime | None
    ) -> list[FacebookObjectData]:
        """Campanha, conjunto e anúncio ativos."""
        return [
            FacebookObjectData(
                FacebookLevel.CAMPAIGN,
                "c1",
                "Bolo",
                None,
                "c1",
                "ACTIVE",
                "ACTIVE",
                None,
                daily_budget_micros=100_000_000,
            ),
            FacebookObjectData(
                FacebookLevel.ADSET, "s1", "Bolo BR", "c1", "c1", "ACTIVE", "ACTIVE", None
            ),
            FacebookObjectData(
                FacebookLevel.AD, "a1", "Carrossel", "s1", "c1", "ACTIVE", "ACTIVE", None
            ),
        ]

    def insights(
        self, token: str, account_external_id: str, since: date, until: date
    ) -> list[FacebookInsightRow]:
        """R$ 5 de gasto no último dia."""
        return [FacebookInsightRow("a1", "s1", "c1", until, 5_000_000, 1000, 800, 30, 20, 15)]

    def country_insights(
        self, token: str, account_external_id: str, since: date, until: date
    ) -> list[FacebookCountryRow]:
        """Sem números por país."""
        return []

    def revoke(self, token: str) -> None:
        """Guarda o token revogado."""
        self.revoked.append(token)

    def set_status(self, token: str, external_id: str, status: str) -> None:
        """Guarda a troca de situação."""
        self.calls.append(("status", external_id, status))

    def set_budget(
        self,
        token: str,
        external_id: str,
        currency: str,
        *,
        daily_budget_micros: int | None,
        lifetime_budget_micros: int | None,
    ) -> None:
        """Guarda a troca de orçamento."""
        self.calls.append(("budget", external_id, str(daily_budget_micros)))

    def copy(self, token: str, external_id: str, level: FacebookLevel, *, paused: bool) -> str:
        """Guarda a cópia e devolve o id novo."""
        self.calls.append(("copy", external_id))
        return f"{external_id}-copia"

    def options(
        self, token: str, account_external_id: str, kind: FacebookListKind, query: str
    ) -> list[FacebookOption]:
        """Uma Página fixa (ou o termo buscado) e conta as buscas, para testar o cache."""
        self.calls.append(("options", kind.value, query))
        return [FacebookOption("page-1", query or "Página", "")]

    def upload_image(
        self, token: str, account_external_id: str, filename: str, content: bytes
    ) -> str:
        """Guarda o envio e devolve um hash."""
        self.calls.append(("image", filename))
        return "hash-1"

    def upload_video(
        self, token: str, account_external_id: str, filename: str, content: bytes
    ) -> str:
        """Guarda o envio e devolve um id de vídeo."""
        self.calls.append(("video", filename))
        return "video-1"

    def create_campaign(
        self, token: str, account_external_id: str, currency: str, draft: FacebookDraft
    ) -> str:
        """Não usado na API (o worker cria)."""
        return "campaign-1"

    def create_adset(
        self,
        token: str,
        account_external_id: str,
        currency: str,
        draft: FacebookDraft,
        adset: FacebookDraftAdset,
        campaign_id: str,
    ) -> str:
        """Não usado na API (o worker cria)."""
        return "adset-1"

    def create_creative(
        self, token: str, account_external_id: str, ad: FacebookDraftAd, link: str
    ) -> str:
        """Não usado na API (o worker cria)."""
        return "creative-1"

    def create_ad(
        self, token: str, account_external_id: str, name: str, adset_id: str, creative_id: str
    ) -> str:
        """Não usado na API (o worker cria)."""
        return "ad-1"

    def update_object(
        self,
        token: str,
        external_id: str,
        currency: str,
        *,
        name: str | None,
        spend_cap_micros: int | None,
    ) -> None:
        """Não usado na API (o worker edita)."""

    def update_adset(self, token: str, external_id: str, adset: FacebookDraftAdset) -> None:
        """Não usado na API (o worker edita)."""

    def set_creative(self, token: str, ad_external_id: str, creative_id: str) -> None:
        """Não usado na API (o worker edita)."""
