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
