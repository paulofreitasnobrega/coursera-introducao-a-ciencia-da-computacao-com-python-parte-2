"""Week 4 - Exercício em vídeo - Ordenador de Seleção Direta."""


class Ordenator:
    """Possui métodos de ordenação de elementos."""

    def __init__(self, list: list):
        """Método construtor."""
        self.list = list

    def _get(self) -> list:
        return self.list[:]

    def direct_selection(self) -> list:
        """Ordena em forma crescente uma lista de números."""
        list = self._get()

        for i in range(len(list)-1):
            min_position = i

            for j in range(i+1, len(list)):
                if list[j] < list[min_position]:
                    min_position = j

            list[i], list[min_position] = list[min_position], list[i]

        return list
