def value_check(a,b):
    if not (isinstance(a, (int, float)) or not(isinstance(b, (int, float)))):
        raise ValueError("Both arguments must be numbers")


def add(a, b):
    value_check(a, b)
    return a + b


def subtract(a, b):
    value_check(a,b)
    return a - b


def multiply(a, b):
    value_check(a,b)
    return a * b


def divide(a, b):
    value_check(a,b)
    if b == 0:
        raise ValueError("Division not possible, division by 0")
    return a / b