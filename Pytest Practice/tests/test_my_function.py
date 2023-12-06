import pytest
from source import my_functions


def test_add():
    result = my_functions.add(1,4)
    assert result == 5

def test_subtract():
    result = my_functions.subtract(11,7)
    assert result == 4

def test_multiply():
    result = my_functions.multiply(2,3)
    assert result == 6

def test_divide():
    result = my_functions.divide(12,3)
    assert result == 4

def test_divide_by_zero():
    with pytest.raises(ValueError):
        result = my_functions.divide(10,0)
    