import math

class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius
    
    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        return self.radius == other.radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def __eq__(self, other):
        if not isinstance(other, Square):
            return False
        return self.side == other.side

    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
    
class Equalateral_Triangle(Shape):

    def __init__(self, side):
        self.side = side

    def __eq__(self, other):
        if not isinstance(other, Equalateral_Triangle):
            return False
        return self.side == other.side

    def area(self):
        return (math.sqrt(3)/4) * self.side ** 2

    def perimeter(self):
        return 3 * self.side

class Isosceles_Scalene_Triangle(Shape):

    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
    
    def __eq__(self, other):
        if not isinstance(other, Isosceles_Scalene_Triangle):
            return False
        return self.side_1 == other.side_1 and self.side_2 == other.side_2 and self.side_3 == other.side_3
    
    def area(self):
        semi_p = ((self.side_1 + self.side_2 + self.side_3)/2)
        return math.sqrt(semi_p * (semi_p - self.side_1) * (semi_p - self.side_2) * (semi_p -self.side_3))

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

    
class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.length == other.length and self.width == other.width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.length * 2) + (self.width * 2)



