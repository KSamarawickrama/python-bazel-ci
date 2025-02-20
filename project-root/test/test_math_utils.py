import pytest
from src.math_utils import add, subtract, multiply, divide


def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0