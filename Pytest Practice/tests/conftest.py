import pytest
from source import shapes

#Fixtures for testing shapes with same or different:
@pytest.fixture
def my_circle():
    return shapes.Circle(10)

@pytest.fixture
def same_circle():
    return shapes.Circle(10)

@pytest.fixture
def different_circle():
    return shapes.Circle(7)

@pytest.fixture
def my_square():
    return shapes.Square(4)


@pytest.fixture
def same_square():
    return shapes.Square(4)


@pytest.fixture
def different_square():
    return shapes.Square(16)

@pytest.fixture
def my_equal_triangle():
    return shapes.Equalateral_Triangle(7)


@pytest.fixture
def same_equal_triangle():
    return shapes.Equalateral_Triangle(7)


@pytest.fixture
def different_equal_triangle():
    return shapes.Equalateral_Triangle(17)

@pytest.fixture
def my_scalene_triangle():
    return shapes.Isosceles_Scalene_Triangle(12, 11, 23)

@pytest.fixture
def same_scalene_triangle():
    return shapes.Isosceles_Scalene_Triangle(12, 11, 23)

@pytest.fixture
def different_scalene_triangle():
    return shapes.Isosceles_Scalene_Triangle(1, 2, 3)

@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def same_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def different_rectangle():
    return shapes.Rectangle(1, 2)

# Fixtures for My Functions testing:

@pytest.fixture
def numbers_for_addition():
    return [(1, 4), (5, 7), (10, 20)]

@pytest.fixture
def numbers_for_subtraction():
    return [(10, 5), (8, 3), (15, 8)]

@pytest.fixture
def numbers_for_multiplication():
    return [(2, 3), (4, 5), (6, 2)]

@pytest.fixture
def numbers_for_division():
    return [(12, 3), (20, 4), (30, 5)]