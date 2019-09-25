"""Week 4 - Exercícios adicionais (opcionais)."""

import pytest

"""
Exercício 1: Gerando listas grandes
Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro
n e devolve uma lista contendo n números inteiros aleatórios.
"""


def lista_substituta(size: int) -> list:
    """Função substituta para a a chamada da lista grande."""
    return [10, 25, 30, 2, 8, 74, 85, 65, 82, 23]


@pytest.fixture
def mp(monkeypatch):
    """Mock Spy."""
    import grande
    monkeypatch.setattr(grande, 'lista_grande', lista_substituta)


@pytest.mark.parametrize('size, expected', [
    (10, [10, 25, 30, 2, 8, 74, 85, 65, 82, 23])
])
def test_lista_grande(mp, size: int, expected: list):
    """Testa se ao receber um número devolve uma lista de num aleatórios."""
    from grande import lista_grande
    assert lista_grande(size) == expected
