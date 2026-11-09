"""Leitura dos filtros e resposta do CSV, usadas pelo painel do cliente e pelo interno."""

from datetime import date, timedelta

from avant_core.rewards.models import RewardLeadFilter
from fastapi import Query, Response

DEFAULT_DAYS = 30


def lead_filter(
    query: str | None = Query(alias="q", default=None, max_length=200),
    question: int | None = Query(default=None, ge=1, le=5),
    answer: int | None = Query(default=None, ge=0, le=2),
) -> RewardLeadFilter:
    """A busca e o filtro por resposta da lista de contatos."""
    return RewardLeadFilter(query=query, question=question, answer=answer)


def period(
    start: date | None = Query(alias="from", default=None),
    end: date | None = Query(alias="to", default=None),
) -> tuple[date, date]:
    """O período das métricas; sem datas, os últimos 30 dias até hoje."""
    last = end or date.today()
    return start or last - timedelta(days=DEFAULT_DAYS - 1), last


def csv_response(content: str, name: str) -> Response:
    """O CSV com BOM (o Excel lê os acentos) para baixar."""
    return Response(
        "﻿" + content,
        media_type="text/csv; charset=utf-8",
        headers={"Content-Disposition": f'attachment; filename="{name}"'},
    )
