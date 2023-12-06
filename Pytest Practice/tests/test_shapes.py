import pytest
import math
from source import shapes

class Test_Circle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def test_area(self):
        result = self.circle.area()
        expected_result = math.pi * self.circle.radius ** 2
        assert result == expected_result       
    
    def test_perimeter(self):
        result = self.circle.perimeter()
        expected_Result = 2 * math.pi * self.circle.radius
        assert result == expected_Result

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.circle


class Test_Square():
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.square = shapes.Square(4)
    
    def test_area(self):
        result = self.square.area()
        expected_result = self.square.side ** 2
        assert result == expected_result       
    
    def test_perimeter(self):
        result = self.square.perimeter()
        expected_Result = 4 * self.square.side
        assert result == expected_Result

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.square

class Test_Equalateral_Triangle():
    def setup_method(self, method):
        print(f"Setting up {method}")
        self.equal_triangle = shapes.Equalateral_Triangle(7)

    def test_area(self):
        result = self.equal_triangle.area()
        expected_result = (math.sqrt(3)/4) * self.equal_triangle.side ** 2
        assert result == expected_result       
    
    def test_perimeter(self):
        result = self.equal_triangle.perimeter()
        expected_Result = 3 * self.equal_triangle.side
        assert result == expected_Result

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.equal_triangle
    
class Test_Scalene_Triangle():

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.Isosceles_Scalene_Triangle = shapes.Isosceles_Scalene_Triangle(12,11,23)

    def test_area(self):
        semi_p = ((self.Isosceles_Scalene_Triangle.side_1 + self.Isosceles_Scalene_Triangle.side_2 + self.Isosceles_Scalene_Triangle.side_3)/2)
        result = self.Isosceles_Scalene_Triangle.area()
        expected_result = math.sqrt(semi_p * (semi_p - self.Isosceles_Scalene_Triangle.side_1) * (semi_p - self.Isosceles_Scalene_Triangle.side_2) * (semi_p -self.Isosceles_Scalene_Triangle.side_3))
        assert result == expected_result       
    
    def test_perimeter(self):
        result = self.Isosceles_Scalene_Triangle.perimeter()
        expected_Result = self.Isosceles_Scalene_Triangle.side_1 + self.Isosceles_Scalene_Triangle.side_2 + self.Isosceles_Scalene_Triangle.side_3
        assert result == expected_Result

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        del self.Isosceles_Scalene_Triangle