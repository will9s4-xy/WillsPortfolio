import pytest
import math
from source import shapes


class Test_Circle:
    def setup_method(self, method):
        print(f"Setting up {method}")

    def test_area(self, my_circle):
        result = my_circle.area()
        expected_result = math.pi * my_circle.radius ** 2
        assert result == expected_result

    def test_perimeter(self, my_circle):
        result = my_circle.perimeter()
        expected_Result = 2 * math.pi * my_circle.radius
        assert result == expected_Result
    
    def test_similar_circle(self, my_circle, same_circle):
        assert my_circle == same_circle
    
    def test_different_circle(self, my_circle, different_circle):
        assert my_circle != different_circle

    def teardown_method(self, method):
        print(f"Tearing down {method}")

class Test_Square:
    def setup_method(self, method):
        print(f"Setting up {method}")
        
    
    def test_area(self, my_square):
        result = my_square.area()
        expected_result = my_square.side ** 2
        assert result == expected_result

    def test_perimeter(self, my_square):
        result = my_square.perimeter()
        expected_Result = 4 * my_square.side
        assert result == expected_Result
    
    def test_same_square(self, my_square, same_square):
        assert my_square == same_square
    
    def test_different_square(self, my_square, different_square):
        assert my_square != different_square

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        # No need to delete the square instance

class Test_Equalateral_Triangle:
    def setup_method(self, method):
        print(f"Setting up {method}")
        

    def test_area(self, my_equal_triangle):
        result = my_equal_triangle.area()
        expected_result = (math.sqrt(3)/4) * my_equal_triangle.side ** 2
        assert result == expected_result

    def test_perimeter(self, my_equal_triangle):
        result = my_equal_triangle.perimeter()
        expected_result = 3 * my_equal_triangle.side
        assert result == expected_result
    
    def test_same_equal_triangle(self, my_equal_triangle, same_equal_triangle):
        assert my_equal_triangle == same_equal_triangle
    
    def test_different_equal_triangle(self, my_equal_triangle, different_equal_triangle):
        assert my_equal_triangle != different_equal_triangle

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        # No need to delete the equal_triangle instance

class Test_Scalene_Triangle:
    def setup_method(self, method):
        print(f"Setting up {method}")
        

    def test_area(self, my_scalene_triangle):
        semi_p = ((my_scalene_triangle.side_1 + my_scalene_triangle.side_2 + my_scalene_triangle.side_3)/2)

        result = my_scalene_triangle.area()
        expected_result = math.sqrt(semi_p * (semi_p - my_scalene_triangle.side_1) * (semi_p - my_scalene_triangle.side_2) * (semi_p - my_scalene_triangle.side_3))
        assert result == expected_result

    def test_perimeter(self, my_scalene_triangle):
        result = my_scalene_triangle.perimeter()
        expected_Result = my_scalene_triangle.side_1 + my_scalene_triangle.side_2 + my_scalene_triangle.side_3
        assert result == expected_Result
    
    def test_same_scalene_triangle(self, my_scalene_triangle, same_scalene_triangle):
        assert my_scalene_triangle == same_scalene_triangle
    
    def test_different_scalene_triangle(self, my_scalene_triangle, different_scalene_triangle):
        assert my_scalene_triangle != different_scalene_triangle


    def teardown_method(self, method):
        print(f"Tearing down {method}")
        # No need to delete the scalene_triangle instance
class Test_Rectangle():

    def setup_method(self, method):
        print(f"Setting up {method}")

    def test_area(self, my_rectangle):
        result = my_rectangle.area()
        expected_result = my_rectangle.length * my_rectangle.width
        assert result == expected_result

    def test_perimeter(self, my_rectangle):
        result = my_rectangle.perimeter()
        expected_result = (my_rectangle.length * 2) + (my_rectangle.width * 2)
        assert result == expected_result
    
    def test_same_rectangle(self, my_rectangle, same_rectangle):
        assert my_rectangle == same_rectangle
    
    def test_different_rectangle(self, my_rectangle, different_rectangle):
        assert my_rectangle != different_rectangle
    
    def teardown_method(self, method):
        print(f"Tearing down {method}")
