"""Week 5 - Lista de exercícios - 5."""

"""
Exercício 1: Busca binária
Implemente a função busca(lista, elemento), que busca um determinado elemento
em uma lista e devolve o índice correspondente à posição do elemento encontrado
Utilize o algoritmo de busca binária. Nos casos em que o elemento buscado não
existir na lista, a função deve devolver o booleano False.

Além de devolver o índice correspondente à posição do elemento encontrado,
sua função deve imprimir cada um dos índices testados pelo algoritmo.
"""


def busca(list: list, element):
    """Busca por um valor utilizando o algoritmo: Binário."""
    first = 0
    last = len(list) - 1

    while first <= last:
        middle = (first + last) // 2

        print(middle)

        if list[middle] == element:
            return middle
        else:
            if element < list[middle]:
                last = middle - 1
            else:
                first = middle + 1

    return False
