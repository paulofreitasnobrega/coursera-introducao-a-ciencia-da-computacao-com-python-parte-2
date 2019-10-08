"""Week 6 - Lista de exercícios - 6."""

"""
Exercício 2: Encontrando ímpares em uma lista
Implemente a função encontra_impares(lista), que recebe como parâmetro uma
lista de números inteiros e devolve uma outra lista apenas com os números
ímpares da lista dada.

Sua solução deve ser implementada utilizando recursão.

Dica: você vai precisar do método extend() que as listas possuem.
"""


def encontra_impares(list: list) -> list:
    """Retorna lista contendo apenas os números ímpares contidos em list."""
    odd = []

    if len(list) > 0:
        if list[0] % 2 > 0:
            odd.append(list[0])

        odd.extend(encontra_impares(list[1:]))

    return odd
