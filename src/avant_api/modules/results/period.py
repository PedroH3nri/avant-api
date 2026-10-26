"""Período padrão dos relatórios de resultado."""

from datetime import date

DEFAULT_MONTHS = 6


def default_period(start: date | None, end: date | None, today: date) -> tuple[date, date]:
    """O período pedido, ou os ``DEFAULT_MONTHS`` meses até o atual."""
    last = end or today
    if start is not None:
        return start, last
    index = last.year * 12 + last.month - DEFAULT_MONTHS
    return date(index // 12, index % 12 + 1, 1), last
