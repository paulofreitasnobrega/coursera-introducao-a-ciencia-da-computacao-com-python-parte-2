"""Week 4 - Lista de exercícios - 4."""

"""
Exercício 1: Lista ordenada
Escreva a função ordenada(lista), que recebe uma lista com números inteiros
como parâmetro e devolve o booleano True se a lista estiver ordenada e False
se a lista não estiver ordenada.
"""


def ordenada(list: list) -> bool:
    """Verifica se uma lista esta ordenada."""
    if not list:
        return False

    ordered_list = sorted(list)
    return True if ordered_list == list else False
