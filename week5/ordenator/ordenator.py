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

    def heap(self, list: list) -> list:
        """Ordena uma lista utilizando o algoritmo: Ordenação por Pilha."""
        pass

    def insertion(self, list: list) -> list:
        """Ordena uma lista utilizando o algoritmo: Ordenação por Inserção."""
        list = list[:]

        for i in range(len(list)):
            for j in range(i, 0, -1):
                if list[j] < list[j-1]:
                    list[j], list[j-1] = list[j-1], list[j]

        return list

    def _merge_sort(self, list: list):
        i = j = k = 0

        if len(list) > 1:
            middle = len(list) // 2
            left = list[:middle]
            right = list[middle:]

            self._merge_sort(left)
            self._merge_sort(right)

            # quando houver elementos em ambos "montes" (esquerdo e direito)
            while(i < len(left) and j < len(right)):
                if left[i] < right[j]:
                    list[k] = left[i]
                    i += 1
                else:
                    list[k] = right[j]
                    j += 1

                k += 1

            # quando hover elementos apenas no "monte" esquerdo
            while(i < len(left)):
                list[k] = left[i]
                i += 1
                k += 1

            # quando hover elementos apenas no "monte" direito
            while(j < len(right)):
                list[k] = right[j]
                j += 1
                k += 1

        return list

    def merge(self, list: list) -> list:
        """Ordena uma lista utilizando o algoritmo: Ordenação por Mistura."""
        return self._merge_sort(list[:])

    def quick(self, list: list) -> list:
        """Ordena uma lista utilizando o algoritmo: Ordenação rápida."""
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

    def shell(self, list: list) -> list:
        """Ordena uma lista utilizando o algoritmo: Shell."""
        pass
