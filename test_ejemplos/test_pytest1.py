import pytest


from matematica import Calculadora


@pytest.fixture
def calculadora():
    """Devuelve una instancia de calculadora"""
    return Calculadora()


def test_suma(calculadora):
    assert calculadora.suma(10, 3) == 13

def test_resta(calculadora):
    assert calculadora.resta(11, 5) == 6

def test_division(calculadora):
    assert calculadora.division(12, 4) == 3

def test_division_por_cero(calculadora):
    with pytest.raises(ZeroDivisionError):
        calculadora.division(3, 0)

def test_multiplicacion(calculadora):
    assert calculadora.multiplicacion(4, 7) == 28
