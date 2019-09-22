"""Week 3 - Lista de exercícios - 3 > 1: Uma classe para triângulos."""

import pytest
from triangulo import Triangulo


@pytest.mark.parametrize("input_perimetro, expected_perimetro", [
    ([2, 3, 6], 11),
    ([2, 2, 2], 6),
    ([1, -2, 2], 0)
])
def test_perimetro(input_perimetro, expected_perimetro):
    """Testa o método perimetro na classe Triangulo."""
    t = Triangulo(*input_perimetro)
    assert t.perimetro() == expected_perimetro


@pytest.mark.parametrize("input_tipo_lado, expected_tipo_lado", [
    ([2, 3, 6], 'escaleno'),
    ([1, 2, 2], 'isósceles'),
    ([2, 2, 2], 'equilátero')
])
def test_tipo_lado(input_tipo_lado, expected_tipo_lado):
    """Testa o nome do triângulo."""
    t = Triangulo(*input_tipo_lado)
    assert t.tipo_lado() == expected_tipo_lado


@pytest.mark.parametrize("input_retangulo, expected_retangulo", [
    ([1, 3, 5], False),
    ([3, 4, 5], True)
])
def test_retangulo(input_retangulo, expected_retangulo):
    """Testa se o triângulo é retângulo."""
    t = Triangulo(*input_retangulo)
    assert t.retangulo() == expected_retangulo


@pytest.mark.parametrize("input_t1, input_t2, expected_semelhantes", [
    ([1, 2, 3], [2, 4, 6], True),
    ([1, 2, 3], [1, 3, 6], False)
])
def test_semelhantes(input_t1, input_t2, expected_semelhantes):
    """Retorna se dois triângulos são semelhantes - comp. dos lados."""
    t1 = Triangulo(*input_t1)
    t2 = Triangulo(*input_t2)
    assert t1.semelhantes(t2) == expected_semelhantes
