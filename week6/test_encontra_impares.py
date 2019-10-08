"""Week 6 - Lista de exercícios - 6."""

import pytest
from encontra_impares import encontra_impares

"""
Exercício 2: Encontrando ímpares em uma lista
Implemente a função encontra_impares(lista), que recebe como parâmetro uma
lista de números inteiros e devolve uma outra lista apenas com os números
ímpares da lista dada.

Sua solução deve ser implementada utilizando recursão.

Dica: você vai precisar do método extend() que as listas possuem.
"""


@pytest.mark.parametrize('list, expected', [
    ([1, 2, 3, 4, 5, 6], [1, 3, 5]),
    ([0], []),
    ([-5, -3, 0, 1], [-5, -3, 1])
])
def test_encontra_impares(list: list, expected: list):
    """Testa uma função recursiva que recebe uma lista e devolve os ímpares."""
    assert encontra_impares(list) == expected
