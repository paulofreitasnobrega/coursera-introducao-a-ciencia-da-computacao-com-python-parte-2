"""Week 6 - Exercícios adicionais (opcionais)."""

"""
Exercício 1: Fibonacci
Implemente a função fibonacci(n), que recebe como parâmetro um número inteiro
e devolve um número inteiro correspondente ao n-ésimo elemento da sequência de
Fibonacci. Sua solução deve ser implementada utilizando recursão.
"""


def fibonacci(n: int) -> int:
    """Fibonacci utilizando chamadas recursivas."""
    return n if n < 2 else fibonacci(n-1) + fibonacci(n-2)
