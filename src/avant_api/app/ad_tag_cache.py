"""A chave do cache no Redis da configuração pública de uma ad tag.

O contrato com o avant-worker (que apaga as chaves das tags de um site quando a importação traz
blocos novos): a chave é ``avant:tag:{chave da tag}``. O valor é o JSON da configuração; tag sem
configuração (pausada, apagada, sem versão) também fica, com o valor vazio, por pouco tempo. O
cache usa o mesmo Redis do reward (``RewardCache``).
"""

KEY = "avant:tag:{key}"
TTL_SECONDS = 3600
EMPTY_TTL_SECONDS = 300


def ad_tag_cache_key(key: str) -> str:
    """A chave do cache da tag."""
    return KEY.format(key=key)
