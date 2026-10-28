"""Exportação do resultado de uma consulta de relatório em CSV e XLSX."""

import csv
import io
from collections.abc import Mapping
from decimal import Decimal

from avant_core.identity.enums import Locale
from avant_core.metrics.catalog import DIMENSIONS_BY_KEY, METRICS_BY_KEY
from avant_core.metrics.models import QueryDefinition, QueryResult
from openpyxl import Workbook

from avant_api.modules.reports.dto import dimension_text

FORMULA_PREFIXES = ("=", "+", "-", "@", "\t", "\r")
Cell = str | Decimal | None


def to_csv(
    result: QueryResult, definition: QueryDefinition, locale: Locale, names: Mapping[str, str]
) -> str:
    """Uma linha por grupo: dimensões (sites e networks pelo nome) e depois as métricas."""
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(_header(definition, locale, names))
    for row in _rows(result, definition):
        writer.writerow([_csv_cell(cell) for cell in row])
    return buffer.getvalue()


def to_xlsx(
    result: QueryResult, definition: QueryDefinition, locale: Locale, names: Mapping[str, str]
) -> bytes:
    """A mesma tabela numa planilha: números como números e texto sempre como texto."""
    workbook = Workbook()
    sheet = workbook.active
    assert sheet is not None
    sheet.append(_header(definition, locale, names))
    for row in _rows(result, definition):
        sheet.append(row)
        for cell in sheet[sheet.max_row]:
            if isinstance(cell.value, str):
                cell.data_type = "s"
    buffer = io.BytesIO()
    workbook.save(buffer)
    return buffer.getvalue()


def _header(definition: QueryDefinition, locale: Locale, names: Mapping[str, str]) -> list[str]:
    """Dimensões e métricas no idioma pedido; a personalizada pelo nome dela."""
    metrics = [_metric_label(key, locale, names) for key in definition.metrics]
    header = [DIMENSIONS_BY_KEY[key].label.text(locale) for key in definition.dimensions]
    header += metrics
    if definition.compare:
        header += [f"{label} (anterior)" for label in metrics]
    return header


def _metric_label(key: str, locale: Locale, names: Mapping[str, str]) -> str:
    """O texto da métrica do catálogo ou o nome da personalizada (``custom.<chave>``)."""
    metric = METRICS_BY_KEY.get(key)
    return metric.label.text(locale) if metric is not None else names.get(key, key)


def _rows(result: QueryResult, definition: QueryDefinition) -> list[list[Cell]]:
    """As linhas com o nome de sites e networks e os valores das métricas."""
    rows: list[list[Cell]] = []
    for row in result.rows:
        cells: list[Cell] = []
        for key in definition.dimensions:
            text = dimension_text(row.dimensions.get(key))
            cells.append(result.labels.get(key, {}).get(text or "", text or ""))
        cells += [row.metrics.get(key) for key in definition.metrics]
        if definition.compare:
            previous = row.previous or {}
            cells += [previous.get(key) for key in definition.metrics]
        rows.append(cells)
    return rows


def _csv_cell(cell: Cell) -> str:
    """Texto escapado ou número sem notação científica; vazio quando não há valor."""
    if isinstance(cell, Decimal):
        return format(cell.normalize(), "f")
    if cell is None:
        return ""
    return f"'{cell}" if cell.startswith(FORMULA_PREFIXES) else cell
