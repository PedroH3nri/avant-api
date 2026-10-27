"""Exportação do resultado de uma consulta de relatório em CSV."""

import csv
import io
from decimal import Decimal

from avant_core.identity.model import Locale
from avant_core.metrics.catalog import DIMENSIONS_BY_KEY, METRICS_BY_KEY
from avant_core.metrics.query import QueryResult

from avant_api.modules.reports.dto import ReportQueryIn, dimension_text

FORMULA_PREFIXES = ("=", "+", "-", "@", "\t", "\r")


def to_csv(result: QueryResult, body: ReportQueryIn, locale: Locale) -> str:
    """Uma linha por grupo: dimensões (sites e networks pelo nome) e depois as métricas."""
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    header = [DIMENSIONS_BY_KEY[key].label.text(locale) for key in body.dimensions]
    header += [METRICS_BY_KEY[key].label.text(locale) for key in body.metrics]
    if body.compare:
        header += [f"{METRICS_BY_KEY[key].label.text(locale)} (anterior)" for key in body.metrics]
    writer.writerow(header)
    for row in result.rows:
        cells = []
        for key in body.dimensions:
            text = dimension_text(row.dimensions.get(key))
            cells.append(_safe_cell(result.labels.get(key, {}).get(text or "", text or "")))
        cells += [_number(row.metrics.get(key)) for key in body.metrics]
        if body.compare:
            previous = row.previous or {}
            cells += [_number(previous.get(key)) for key in body.metrics]
        writer.writerow(cells)
    return buffer.getvalue()


def _safe_cell(text: str) -> str:
    """Evita que a planilha rode como fórmula um texto vindo de fora (key-value, domínio)."""
    return f"'{text}" if text.startswith(FORMULA_PREFIXES) else text


def _number(value: Decimal | None) -> str:
    """Número sem notação científica; vazio quando a razão não tem denominador."""
    return "" if value is None else format(value.normalize(), "f")
