"""Week 5 - Lista de exercícios - 5."""

"""
Exercício 2: Ordenação com bubble sort
Implemente a função bubble_sort(lista), que recebe uma lista com números
inteiros como parâmetro e devolve esta lista ordenada. Utilize o algoritmo
bubble sort.

Além de devolver uma lista ordenada, ao longo do processamento sua função deve
imprimir o estado atual da lista toda vez que fizer uma alteração em seus
elementos.
"""


def bubble_sort(list: list) -> list:
    """Ordena uma lista utilizando o algoritmo: Ordenação da Bolha."""
    list = list[:]

    for i in range(len(list)-1, 0, -1):
        for j in range(i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                print(list)

    return list
