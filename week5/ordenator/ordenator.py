"""Algoritmos de ordenação de listas."""


class Ordenator:
    """Fornece uma variedade de algoritmos de ordenação."""

    def bubble(self, list: list) -> list:
        """Ordena uma lista utilizando o algoritmo: Ordenação da Bolha."""
        list = list[:]

        for i in range(len(list)-1, 0, -1):
            change = False

            for j in range(i):
                if list[j] > list[j+1]:
                    change = True
                    list[j], list[j+1] = list[j+1], list[j]

            if not change:
                return list

        return list

    def insertion(self, list: list) -> list:
        """Ordena uma lista utilizando o algoritmo: Ordenação por Inserção."""
        list = list[:]

        pass

    def selection(self, list: list) -> list:
        """Ordena uma lista utilizando o algoritmo: Seleção Direta."""
        list = list[:]

        for i in range(len(list)-1):
            min_position = i

            for j in range(i+1, len(list)):
                if list[j] < list[min_position]:
                    min_position = j

            list[i], list[min_position] = list[min_position], list[i]

        return list
