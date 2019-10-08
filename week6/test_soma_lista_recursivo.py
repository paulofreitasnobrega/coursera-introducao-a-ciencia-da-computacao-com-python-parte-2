"""Week 6 - Lista de exercícios - 6."""

import pytest
from soma_lista_recursivo import soma_lista

"""
Exercício 1: Soma dos elementos de uma lista
Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de
números inteiros e devolve um número inteiro correspondente à soma dos
elementos desta lista.

Sua solução deve ser implementada utilizando recursão.
"""


@pytest.mark.parametrize('list, expected', [
    ([0, 1, 2, 3], 6),
    ([-5, -1, 0, 1, 2, 3], 0),
    ([0], 0),
    ([-5, 2], -3)
])
def test_soma_lista_recursivo(list: list, expected: int):
    """Testa a função de soma de uma lista de inteiros."""
    assert soma_lista(list) == expected
