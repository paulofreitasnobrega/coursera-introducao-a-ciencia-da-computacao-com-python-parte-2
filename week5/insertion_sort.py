"""Week 5 - Exercícios adicionais (opcionais)."""


"""
Exercício 1: Ordenação com insertion sort
Implemente a função insertion_sort(lista), que recebe uma lista com números
inteiros como parâmetro e devolve esta lista ordenada. Utilize o algoritmo
insertion sort.
"""


def insertion_sort(list: list) -> list:
    """Ordena uma lista utilizando o algoritmo: Ordenação por Inserção."""
    list = list[:]

    for i in range(len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]

    return list
