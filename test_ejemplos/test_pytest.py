import pytest

from matematica import Calculadora


def test_suma():
    calc = Calculadora()
    assert calc.suma(10, 3) == 13

def test_resta():
    calc = Calculadora()
    assert calc.resta(11, 5) == 6

def test_division():
    calc = Calculadora()
    assert calc.division(12, 4) == 3

def test_division_por_cero():
    calc = Calculadora()
    with pytest.raises(ZeroDivisionError):
        calc.division(3,0)

def test_multiplicacion():
    calc = Calculadora()
    assert calc.multiplicacion(4, 7) == 28
