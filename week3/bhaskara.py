"""Week 3 - Exercícios em Vídeo - Classe Bhaskara."""

from math import sqrt

"""
Refatore o código Bhaskara desenvolvido no módulo 1 - Semana 3 transformando
as funções isoladas em métodos de uma classe Bhaskara. Ao final escreva um
arquivo de teste chamado test_bhaskara.py que implemente a função parametrize
do framework pytest

Aluno: Paulo Freitas Nobrega
"""


class Bhaskara:
    """Fórmula de Bhaskara."""

    def delta(self, a, b, c):
        """Calcula o delta através dos coeficientes a, b e c."""
        return (b**2) - (4*a*c)

    def real_roots(self, a, b, c):
        """Encontra as raízes reais de uma equação do segundo grau."""
        delta = self.delta(a, b, c)

        if delta >= 0:
            x1 = (-b + sqrt(delta)) / (2*a)
            x2 = (-b - sqrt(delta)) / (2*a)
            roots = sorted([x1, x2])

            if delta > 0:
                return 2, roots[0], roots[1]
            else:
                return 1, roots[0]
        else:
            return 0
