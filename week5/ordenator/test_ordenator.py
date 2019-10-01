"""Week 4 - Exercício em vídeo - Ordenador de Seleção Direta [tests]."""

import pytest
from ordenator import Ordenator


@pytest.mark.parametrize("input, expected", [
    ([1, 3, 2, 4, 6, 5], [1, 2, 3, 4, 5, 6])
])
def test_bubble(input, expected):
    """Testa a ordenação através do algorítmo: Ordenação da Bolha."""
    ord = Ordenator()
    assert ord.bubble(input) == expected


@pytest.mark.parametrize("input, expected", [
    ([1, 3, 2, 4, 6, 5], [1, 2, 3, 4, 5, 6])
])
def test_insertion(input, expected):
    """Testa a ordenação através do algorítmo: Ordenação por Inserção."""
    ord = Ordenator()
    assert ord.insertion(input) == expected


@pytest.mark.parametrize("input, expected", [
    ([1, 3, 2, 4, 6, 5], [1, 2, 3, 4, 5, 6])
])
def test_merge(input, expected):
    """Testa a ordenação através do algorítmo: Ordenação por Mistura."""
    ord = Ordenator()
    assert ord.merge(input) == expected


@pytest.mark.parametrize("input, expected", [
    ([1, 3, 2, 4, 6, 5], [1, 2, 3, 4, 5, 6])
])
def test_selection(input, expected):
    """Testa a ordenação através do algorítmo: Seleção Direta."""
    ord = Ordenator()
    assert ord.selection(input) == expected
