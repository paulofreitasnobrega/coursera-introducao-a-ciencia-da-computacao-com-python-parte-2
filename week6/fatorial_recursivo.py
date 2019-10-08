"""Week 6 - Exercícios adicionais (opcionais)."""

"""
Implemente a função fatorial(x), que recebe como parâmetro um número inteiro
e devolve um número inteiro correspondente ao fatorial de x.

Sua solução deve ser implementada utilizando recursão.
"""


def fatorial(n: int) -> int:
    """Fatorial utilizando chamadas recursivas."""
    return 1 if n < 1 else n * fatorial(n-1)
