"""Algoritmos de ordenação de listas."""


class Ordenator:
    """Fornece uma variedade de algoritmos de ordenação."""

    def bubble(self, list: list) -> list:
        """Ordena uma lista utilizando o algoritmo: Ordenação da Bolha."""
        list = list[:]

        for i in range(len(list)-1, 0, -1):
            for j in range(i):
                if list[j] > list[j+1]:
                    list[j], list[j+1] = list[j+1], list[j]

        return list

    def insertion(self, list: list) -> list:
        """Ordena uma lista utilizando o algoritmo: Ordenação por Inserção."""
        list = list[:]

        for i in range(len(list)):
            for j in range(i, 0, -1):
                if list[j] < list[j-1]:
                    list[j], list[j-1] = list[j-1], list[j]

        return list

    def _merge_divide(self, list: list, start: int, end: int):
        # if len(list) > 1:
        #     middle = len(list) // 2
        #     left, right = list[:middle], list[middle:]
        #     self._merge_divide(left)
        #     self._merge_divide(right)
        pass

    def merge(self, list: list) -> list:
        """Ordena uma lista utilizando o algoritmo: Ordenação por Mistura."""
        list = list[:]
        self._merge_divide(list, 0, len(list))
        pass

    def selection(self, list: list) -> list:
        """
        Ordena uma lista utilizando o algoritmo: Seleção Direta.
        """
        list = list[:]

        for i in range(len(list)-1):
            min_position = i

            for j in range(i+1, len(list)):
                if list[j] < list[min_position]:
                    min_position = j

            list[i], list[min_position] = list[min_position], list[i]

        return list
