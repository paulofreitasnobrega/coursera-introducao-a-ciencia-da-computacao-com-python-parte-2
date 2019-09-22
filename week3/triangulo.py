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

Exercícios adicionais (opcionais)
Exercício 1: Triângulos retângulos
Escreva, na classe Triangulo, o método retangulo() que devolve True se o
triângulo for retângulo, e False caso contrário.

Exercício 2: Triângulos semelhantes
Ainda na classe Triangulo, escreva um método semelhantes(triangulo) que recebe
um objeto do tipo Triangulo como parâmetro e verifica se o triângulo atual é
semelhante ao triângulo passado como parâmetro. Caso positivo, o método deve
devolver True. Caso negativo, deve devolver False.

Aluno: Paulo Freitas Nobrega
"""


class Triangulo:
    """Triângulo é um polígono de três lados e três ângulos."""

    def __init__(self, a, b, c):
        """Recebe como parâmetro os três lados de um triângulo a, b e c."""
        self.a = a
        self.b = b
        self.c = c

    def side_list(self):
        """Retorna os lados em formato de lista."""
        return [self.a, self.b, self.c]

    def perimetro(self):
        """Calcula o perímetro de um triangulo."""
        if self.a <= 0 or self.b <= 0 or self.c <= 0:
            return 0

        return self.a + self.b + self.c

    def tipo_lado(self):
        """Retorna o tipo do triângulo."""
        side_name = ''
        sides = len(set(self.side_list()))

        if sides == 3:
            side_name = 'escaleno'
        elif sides == 2:
            side_name = 'isósceles'
        elif sides == 1:
            side_name = 'equilátero'

        return side_name

    def retangulo(self):
        """Retorna se o triânguo é retângulo."""
        *side, hypotenuse = sorted(self.side_list())
        side_sum = (side[0] ** 2 + side[1] ** 2)

        return True if hypotenuse ** 2 == side_sum else False

    def semelhantes(self, triangulo):
        """Retorna se dois triângulos são semelhantes - comp. dos lados."""
        t1 = self.side_list()
        t2 = triangulo.side_list()
        proportions = set([x[0]/x[1] for x in zip(t1, t2)])

        return True if len(proportions) == 1 else False
