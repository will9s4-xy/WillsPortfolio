class Add_Functions():
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def add(self):
        return self.num_1 + self.num_2
class Subtract_function():
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def subtract(self):
        return self.num_1 - self.num_2
class Multiply_function():
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def multiply(self):
         return self.num_1 * self.num_2

class Divide_function():
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2    
    
    def divide(self):
        if self.num_2 == 0:
            raise ValueError("Cannot divide by zero")
        return self.num_1/self.num_2
