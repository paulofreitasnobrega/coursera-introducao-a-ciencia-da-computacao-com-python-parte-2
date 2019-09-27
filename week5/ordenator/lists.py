"""Gerador de Lista."""

from random import randint


class Lists:
    """Auxilia na criação de diferentes tipos de listas com tamanho (k)."""

    def random(self, k: int) -> list:
        """Retorna lista aleatória de tamanho (k)."""
        return [randint(1, k) for i in range(k)]

    def sorted(self, k: int) -> list:
        """Retorna lista ordenada de tamanho (k)."""
        return [i for i in range(k)]

    def nearly_sorted(self, k: int, list: list = [-1, -3, -5, -7]) -> list:
        """Retorna lista semi-ordenada de tamanho (k)."""
        sorted = self.sorted(k)

        for i in list:
            sorted[randint(0, len(sorted) - 1)] = i

        return sorted
