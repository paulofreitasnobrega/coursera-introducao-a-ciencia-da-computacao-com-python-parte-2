"""Week 5 - Exercícios adicionais (opcionais)."""


import pytest
from insertion_sort import insertion_sort

"""
Exercício 1: Ordenação com insertion sort
Implemente a função insertion_sort(lista), que recebe uma lista com números
inteiros como parâmetro e devolve esta lista ordenada. Utilize o algoritmo
insertion sort.
"""


@pytest.mark.parametrize("input, expected", [
    ([1, 3, 2, 4, 6, 5], [1, 2, 3, 4, 5, 6])
])
def test_insertion_sort(input: list, expected: list):
    """Recebe uma lista e deve devolver a mesma ordenada crescentemente."""
    assert insertion_sort(input) == expected
