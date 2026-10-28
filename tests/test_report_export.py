"""Exportação de relatórios em CSV e XLSX, sem banco: escape, caracteres de controle e tempo."""

import csv
import io
import time
from datetime import date
from decimal import Decimal

from avant_core.identity.enums import Locale
from avant_core.metrics.enums import MetricSource
from avant_core.metrics.models import DateRange, Period, QueryDefinition, QueryResult
from avant_core.metrics.models.result_row import ResultRow
from openpyxl import load_workbook

from avant_api.modules.reports.export import to_csv, to_xlsx

DAY = date(2026, 10, 27)
DEFINITION = QueryDefinition(
    source=MetricSource.GAM,
    metrics=("revenue", "custom.soma"),
    period=Period(start=DAY, end=DAY),
    dimensions=("date",),
)
NAMES = {"custom.soma": '=HYPER\x01LINK("x")'}


def _result(rows: int) -> QueryResult:
    """Um resultado com ``rows`` linhas iguais."""
    row = ResultRow({"date": DAY}, {"revenue": Decimal("2"), "custom.soma": Decimal("1")})
    return QueryResult(DateRange(DAY, DAY), [row] * rows, {})


def test_csv_header_escapes_formulas() -> None:
    header = next(csv.reader(io.StringIO(to_csv(_result(1), DEFINITION, Locale.EN, NAMES))))
    assert header == ["Date", "Revenue", '\'=HYPER\x01LINK("x")']


def test_xlsx_header_is_text_without_control_characters() -> None:
    content = to_xlsx(_result(1), DEFINITION, Locale.EN, NAMES)
    sheet = load_workbook(io.BytesIO(content)).active
    assert sheet is not None
    assert sheet["C1"].value == '=HYPERLINK("x")' and sheet["C1"].data_type == "s"
    assert sheet["A2"].value == "2026-10-27" and sheet["B2"].value == 2


def test_xlsx_with_the_row_limit_is_fast() -> None:
    started = time.perf_counter()
    to_xlsx(_result(10_000), DEFINITION, Locale.EN, {"custom.soma": "Soma"})
    assert time.perf_counter() - started < 3
