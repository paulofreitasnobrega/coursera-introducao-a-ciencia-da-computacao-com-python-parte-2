"""Week 4 - Exercícios adicionais (opcionais)."""

import random

"""
Exercício 1: Gerando listas grandes
Escreva a função lista_grande(n), que recebe como parâmetro um número inteiro
n e devolve uma lista contendo n números inteiros aleatórios.
"""


def lista_grande(size: int) -> list:
    """Recebe um número e devolve uma lista de elementos aleatórios."""
    list = []

    for x in range(size):
        list.append(random.randint(1, 100))

    return list
