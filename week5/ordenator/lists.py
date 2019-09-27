"""Gerador de Lista."""

from random import randint, sample


class Lists:
    """Auxilia na criação de diferentes tipos de listas com tamanho (k)."""

    def random(self, k: int) -> list:
        """Retorna lista aleatória de tamanho (k)."""
        return sample(self.sorted(k), k)

    def sorted(self, k: int) -> list:
        """Retorna lista ordenada de tamanho (k)."""
        return [i for i in range(k)]

    def nearly_sorted(self, k: int, random_ratio: float = 0.1) -> list:
        """Retorna lista semi-ordenada de tamanho (k)."""
        list = self.sorted(k)
        amount_random_elements = int((len(list) * (random_ratio*100)) / 100)

        for i in range(amount_random_elements):
            list[randint(0, len(list)-1)] = randint(-50, 50)

        return list
