import pytest
import nizchain.pseudo_function as pseudo_function


def test_add():
    result = pseudo_function.add(1, 4)
    assert result == 5


def test_divide():
    result = pseudo_function.divide(10, 5)
    assert result == 2
