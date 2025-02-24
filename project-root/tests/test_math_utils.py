import pytest
from src.math_utils import add, subtract, multiply, divide

def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(12, 4) == 8
    assert subtract(15, -15) == 0

def test_multiply():
    assert multiply(4, 5) == 20
    assert multiply(-3, 3) == -9
    assert multiply(-3, -3) == 9

def test_divide():
    assert divide(100, 25) == 4
    assert divide(-25, 5) == -5
    
    
    