"""O país do visitante pelo IP, com a base GeoLite2 Country da MaxMind (o mesmo .mmdb do worker).

O caminho vem de ``GEOLITE2_COUNTRY_FILE``. Sem o arquivo, ninguém tem país e a rota dos floors
devolve só o grupo de controle. O IP só passa por aqui e não é gravado.
"""

import ipaddress
from typing import Any, Protocol

import maxminddb


class CountryLookup(Protocol):
    def country_code(self, ip: str | None) -> str | None:
        """O código ISO do país do IP (``BR``), ou vazio."""
        ...


class NoCountries:
    """Sem base: nenhum IP tem país."""

    def country_code(self, ip: str | None) -> str | None:
        """Sempre vazio."""
        return None


class FixedCountries:
    """Para os testes: o país de cada IP vem de um dicionário."""

    def __init__(self, countries: dict[str, str]) -> None:
        self._countries = countries

    def country_code(self, ip: str | None) -> str | None:
        """O país guardado para o IP."""
        return self._countries.get(ip or "")


class GeoLiteCountries:
    """Lê o código ISO do país no arquivo .mmdb."""

    def __init__(self, path: str) -> None:
        self._reader = maxminddb.open_database(path)

    def country_code(self, ip: str | None) -> str | None:
        """O código do país do IP, ou vazio quando o IP não vale ou não está na base."""
        if not ip:
            return None
        try:
            ipaddress.ip_address(ip)
            found: Any = self._reader.get(ip)
        except ValueError:
            return None
        if not isinstance(found, dict):
            return None
        country = found.get("country") or found.get("registered_country") or {}
        code = country.get("iso_code") if isinstance(country, dict) else None
        return code if isinstance(code, str) else None
