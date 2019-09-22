"""Week 3 - Exercícios em Vídeo - Classe Bhaskara."""

import pytest
from bhaskara import Bhaskara


@pytest.mark.parametrize("test_input, expected", [
    ([1, 4, 5], 0),
    ([4, -4, 1], (1, 0.5)),
    ([1, -5, 6], (2, 2.0, 3.0))
])
def test_real_roots(test_input, expected):
    """Testa o método de raízes reais na classe Bhaskara."""
    bk = Bhaskara()
    assert bk.real_roots(*test_input) == expected
