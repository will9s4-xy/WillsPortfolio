import pytest
from source import shapes


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