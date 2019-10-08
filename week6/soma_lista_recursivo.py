"""Week 6 - Lista de exercícios - 6."""

"""
Exercício 1: Soma dos elementos de uma lista
Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de
números inteiros e devolve um número inteiro correspondente à soma dos
elementos desta lista.

Sua solução deve ser implementada utilizando recursão.
"""


def soma_lista(list: list) -> int:
    """Recebe uma lista de inteiros e retorna a soma dos elementos."""
    if len(list) == 1:
        return list[0]

    return list[0] + soma_lista(list[1:])
