# math_functions.py

def add(a, b):
    """Adds two numbers and returns the sum."""
    return a + b

def subtract(a, b):
    """Subtracts the second number from the first and returns the result."""
    return a - b

def multiply(a, b):
    """Multiplies two numbers and returns the product."""
    return a * b

def divide(a, b):
    """Divides the first number by the second and returns the result.
    
    Raises:
        ZeroDivisionError: If the second number is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
