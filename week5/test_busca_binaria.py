"""Week 5 - Lista de exercícios - 5."""

import pytest
from busca_binaria import busca

"""
Exercício 1: Busca binária
Implemente a função busca(lista, elemento), que busca um determinado elemento
em uma lista e devolve o índice correspondente à posição do elemento encontrado
Utilize o algoritmo de busca binária. Nos casos em que o elemento buscado não
existir na lista, a função deve devolver o booleano False.

Além de devolver o índice correspondente à posição do elemento encontrado,
sua função deve imprimir cada um dos índices testados pelo algoritmo.
"""


@pytest.mark.parametrize('list, element, expected', [
    (['a', 'e', 'i'], 'e', 1),
    ([1, 2, 3, 4, 5], 6, False),
    ([1, 2, 3, 4, 5, 6], 4, 3)
])
def test_busca(list: list, element: int, expected):
    """Deve encontrar um elemento na lista e retornar seu índice."""
    assert busca(list, element) == expected
