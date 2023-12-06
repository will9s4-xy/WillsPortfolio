import math

class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass

class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
    
class Equalateral_Triangle(Shape):

    def __init__(self, side):
        self.side = side

    def area(self):
        return (math.sqrt(3)/4) * self.side ** 2

    def perimeter(self):
        return 3 * self.side

class Isosceles_Scalene_Triangle(Shape):

    def __init__(self, side_1, side_2, side_3):
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3
    
    def area(self):
        semi_p = ((self.side_1 + self.side_2 + self.side_3)/2)
        return math.sqrt(semi_p * (semi_p - self.side_1) * (semi_p - self.side_2) * (semi_p -self.side_3))

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3

