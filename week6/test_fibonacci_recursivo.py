"""Week 6 - Exercícios adicionais (opcionais)."""

import pytest
from fibonacci_recursivo import fibonacci

"""
Exercício 1: Fibonacci
Implemente a função fibonacci(n), que recebe como parâmetro um número inteiro
e devolve um número inteiro correspondente ao n-ésimo elemento da sequência de
Fibonacci. Sua solução deve ser implementada utilizando recursão.
"""


@pytest.mark.parametrize('n, expected', [
    (0, 0),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (8, 21)
])
def test_fibonacci_recursivo(n, expected):
    """Teste a função fibonacci."""
    assert fibonacci(n) == expected
