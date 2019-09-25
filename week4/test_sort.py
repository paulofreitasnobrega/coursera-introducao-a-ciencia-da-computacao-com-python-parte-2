"""Week 4 - Exercícios adicionais (opcionais)."""

import pytest
from sort import ordena

"""
Exercício 2: Ordenação com selection sort
Implemente a função ordena(lista), que recebe uma lista com números inteiros
como parâmetro e devolve esta lista ordenada em ordem crescente. Utilize o
algoritmo selection sort.
"""


@pytest.mark.parametrize('list, expected', [
    ([1, 3, 2, 5, 4], [1, 2, 3, 4, 5])
])
def test_ordena(list: list, expected):
    """Recebe uma lista e deve devolver a mesma ordenada crescentemente."""
    assert ordena(list) == expected
