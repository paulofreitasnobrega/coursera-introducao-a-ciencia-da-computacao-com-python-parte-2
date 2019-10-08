"""Week 6 - Exercícios adicionais (opcionais)."""

import pytest
from fatorial_recursivo import fatorial

"""
Implemente a função fatorial(x), que recebe como parâmetro um número inteiro
e devolve um número inteiro correspondente ao fatorial de x.

Sua solução deve ser implementada utilizando recursão.
"""


@pytest.mark.parametrize('n, expected', [
    (0, 1),
    (1, 1),
    (2, 2),
    (4, 24),
    (5, 120),
    (8, 40320)
])
def test_fatorial_recursivo(n, expected):
    """Testa a função fatorial."""
    assert fatorial(n) == expected
