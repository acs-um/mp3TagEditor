import pytest
from decimal import Decimal as D

from matematica import Calculadora, Cuadrado, Rectangulo


@pytest.fixture
def calculadora():
    """Devuelve una instancia de calculadora"""
    return Calculadora()

@pytest.mark.parametrize("a, b, result", [
    (10, 3, 13),
    (20, 2, 22),
    (D('-14.2'), D('7.2'), -7),
])
def test_suma(calculadora, a, b, result):
    assert calculadora.suma(a, b) == result

def test_resta(calculadora):
    assert calculadora.resta(11, 5) == 6

def test_division(calculadora):
    assert calculadora.division(12, 4) == 3

def test_division_por_cero(calculadora):
    with pytest.raises(ZeroDivisionError):
        calculadora.division(3, 0)

def test_multiplicacion(calculadora):
    assert calculadora.multiplicacion(4, 7) == 28


def test_cuadrado_init():
    cuadrado = Cuadrado(20)
    assert cuadrado.lado == 20

def test_cuadrado_perimetro():
    cuadrado = Cuadrado(11)
    assert cuadrado.perimetro() == 44

def test_cuadrado_area():
    cuadrado = Cuadrado(6)
    assert cuadrado.area() == 36


