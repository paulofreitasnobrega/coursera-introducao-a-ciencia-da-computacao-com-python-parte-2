"""Week 6 - Lista de exercícios - 6."""

"""
Exercício 3: Elefantes
Este exercício tem duas partes:

Implemente a função incomodam(n) que devolve uma string contendo "incomodam "
(a palavra seguida de um espaço) n vezes. Se n não for um inteiro estritamente
positivo, a função deve devolver uma string vazia. Essa função deve ser
implementada utilizando recursão.
Utilizando a função acima, implemente a função elefantes(n) que devolve uma
string contendo a letra da música "Um elefante incomoda muita gente" de 1 até
n elefantes. Se n não for maior que 1, a função deve devolver uma string vazia.
Essa função também deve ser implementada utilizando recursão.
Observe que, para um elefante, você deve escrever por extenso e no singular
("Um elefante..."); para os demais, utilize números e o plural
("2 elefantes...").

Dica: lembre-se que é possível juntar strings com o operador "+".
Lembre-se também que é possível transformar números em strings com
a função str().

Dica: Será que neste caso a base da recursão é diferente de n == 1n==1?
"""


def incomodam(n: int) -> str:
    """Retorna uma string contendo a palavra "incomodam" n vezes."""
    mstr = ""

    if n > 0:
        mstr += "incomodam "
        return mstr + incomodam(n-1)

    return mstr


def elefantes(n: int, max=None) -> str:
    """Revolve uma string contendo a letra da música."""
    if not max:
        max, n = n, 2

    if n <= max:
        if n == 2:
            mstr = "Um elefante incomoda muita gente\n"
            mstr += "{} elefantes {}muito mais\n".format(n, incomodam(n))
        else:
            mstr = "{} elefantes {}muito mais\n".format(n, incomodam(n))

        if n < max:
            mstr += "{} elefantes incomodam muita gente\n".format(n)

        return mstr + elefantes(n+1, max)

    return ""


print(elefantes(3))
