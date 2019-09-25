"""Week 4 - Lista de exercícios - 4."""

import pytest
from busca import busca

"""
Exercício 2: Busca sequencial
Implemente a função busca(lista, elemento), que busca um determinado elemento
em uma lista e devolve o índice correspondente à posição do elemento encontrado
Utilize o algoritmo de busca sequencial. Nos casos em que o elemento buscado
não existir na lista, a função deve devolver o booleano False.
"""


@pytest.mark.parametrize('list, element, expected', [
    (['a', 'e', 'i'], 'e', 1),
    ([12, 13, 14], 15, False),
    ([], '', False)
])
def test_busca(list: list, element, expected):
    """Testa a busca de um elemento em uma lista."""
    assert busca(list, element) == expected
