"""Week 6 - Lista de exercícios - 6."""

import pytest
from elefantes import elefantes, incomodam

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


@pytest.mark.parametrize('n, expected', [
    (-10, ""),
    (0, ""),
    (2, "incomodam incomodam ")
])
def test_indomodam(n: int, expected: str):
    """Retorna a quantidade n da palavra imcomodam."""
    assert incomodam(n) == expected


@pytest.mark.parametrize('n, expected', [
    (1, ""),
    (3, "Um elefante incomoda muita gente\n2 elefantes incomodam incomodam muito mais\n2 elefantes incomodam muita gente\n3 elefantes incomodam incomodam incomodam muito mais\n")
])
def test_elefantes(n: int, expected: str):
    """Retorna a letra da musica."""
    assert elefantes(n) == expected
