"""Week 3 - Lista de exercícios - 3."""

"""
Exercício 1: Uma classe para triângulos.
Defina a classe Triangulo cujo construtor recebe 3 valores inteiros
correspondentes aos lados a, b e c de um triângulo.
A classe triângulo também deve possuir um método perimetro, que não recebe
parâmetros e devolve um valor inteiro correspondente ao perímetro do triângulo.

Exercício 2: Tipos de triângulos
Na classe triângulo, definida na Questão 1, escreva o metodo tipo_lado() que
devolve uma string dizendo se o triângulo é:
isósceles (dois lados iguais), equilátero (todos os lados iguais) ou
escaleno (todos os lados diferentes)

Aluno: Paulo Freitas Nobrega
"""


class Triangulo:
    """Triângulo é um polígono de três lados e três ângulos."""

    def __init__(self, x, y, z):
        """Recebe como parâmetro os três lados de um triângulo x, y e z."""
        self.a = x
        self.b = y
        self.c = z

    def perimetro(self):
        """Calcula o perímetro de um triangulo."""
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 0

        return self.a + self.b + self.c

    def tipo_lado(self):
        """Retorna o tipo do triângulo."""
        side_name = ''
        sides = len(set([self.a, self.b, self.c]))

        if sides == 3:
            side_name = 'escaleno'
        elif sides == 2:
            side_name = 'isósceles'
        elif sides == 1:
            side_name = 'equilátero'

        return side_name
