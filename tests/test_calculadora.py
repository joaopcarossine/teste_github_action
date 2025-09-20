# tests/test_calculadora.py
import pytest
from src.calculadora import somar, dividir, multiplicar, subtrair

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_multiplicar():
    assert multiplicar(1, 5) == 5
    assert multiplicar(-1, 5) == -5

def test_subtrair():
    assert subtrair(5, 2) == 3
    assert subtrair(3, 10) == -7