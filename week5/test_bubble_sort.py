"""Week 5 - Lista de exercícios - 5."""

import pytest
from bubble_sort import bubble_sort

"""
Exercício 2: Ordenação com bubble sort
Implemente a função bubble_sort(lista), que recebe uma lista com números
inteiros como parâmetro e devolve esta lista ordenada. Utilize o algoritmo
bubble sort.

Além de devolver uma lista ordenada, ao longo do processamento sua função deve
imprimir o estado atual da lista toda vez que fizer uma alteração em seus
elementos.
"""


@pytest.mark.parametrize("input, expected", [
    ([5, 1, 4, 2], [1, 2, 4, 5])
])
def test_bubble_sort(input: list, expected: list):
    """Recebe uma lista e deve devolver a mesma ordenada crescentemente."""
    assert bubble_sort(input) == expected
