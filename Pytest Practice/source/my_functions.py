def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
     return num_1 * num_2

def divide(num_1, num_2):
    if num_2 == 0:
        raise(ValueError)
    return num_1/num_2
