"""Week 4 - Lista de exercícios - 4 [tests]."""

import pytest
from ordenada import ordenada

"""
Exercício 1: Lista ordenada
Escreva a função ordenada(lista), que recebe uma lista com números inteiros
como parâmetro e devolve o booleano True se a lista estiver ordenada e False
se a lista não estiver ordenada.
"""


@pytest.mark.parametrize('input, expected', [
    ([1, 5, 4, 2, 3], False),
    ([1, 2, 3, 4, 5], True),
    ([1, 1, 1, 1], True),
    ([], False)
])
def test_ordenada(input: list, expected: bool):
    """Testa se uma lista é ordenada."""
    assert ordenada(input) == expected
