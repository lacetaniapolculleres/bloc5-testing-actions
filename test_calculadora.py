import pytest
from calculadora import suma, resta, multiplicacio, divisio

def test_suma():
    assert suma(3, 2) == 5

def test_resta():
    assert resta(10, 4) == 6

def test_multiplicacio():
    assert multiplicacio(3, 4) == 12

def test_divisio():
    assert divisio(10, 2) == 5.0

def test_divisio_per_zero():
    with pytest.raises(ValueError):
        divisio(5, 0)
