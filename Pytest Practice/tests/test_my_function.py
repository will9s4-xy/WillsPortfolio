import pytest
from source import my_functions
@pytest.mark.parametrize("num1, num2, expected_result", [(10, 5, 5), (8, 3, 5), (15, 8, 7)])
def test_subtract(numbers_for_subtraction, num1, num2, expected_result):
    result = my_functions.Subtract_function(num1, num2).subtract()
    assert result == expected_result

@pytest.mark.parametrize("num1, num2, expected_result", [(2, 3, 6), (4, 5, 20), (6, 2, 12)])
def test_multiply(numbers_for_multiplication, num1, num2, expected_result):
    result = my_functions.Multiply_function(num1, num2).multiply()
    assert result == expected_result

@pytest.mark.parametrize("num1, num2, expected_result", [(12, 3, 4), (20, 4, 5), (30, 5, 6)])
def test_divide(numbers_for_division, num1, num2, expected_result):
    result = my_functions.Divide_function(num1, num2).divide()
    assert result == expected_result

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide_instance = my_functions.Divide_function(10, 0)
        divide_instance.divide()

