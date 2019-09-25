"""Week 4 - Exercício em vídeo - Ordenador de Seleção Direta [tests]."""

import pytest
from ordenator import Ordenator


@pytest.mark.parametrize("input, expected", [
    ([1, 3, 2, 5, 4], [1, 2, 3, 4, 5])
])
def test_direct_selection(input, expected):
    """Testa a ordenação de uma lista de números."""
    ord = Ordenator(input)
    assert ord.direct_selection() == expected
