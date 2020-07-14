from re import match as re_match

# Alaa' Omar


def add(num1, num2):
    """
    Adds two numbers.
    Keyword arguments:
    num1-> float number,
    num2-> float number
    """
    return float(num1) + float(num2)


def multiply(num1, num2):
    """
    Multiplies two numbers.
    Keyword arguments:
    num1-> float number,
    num2-> float number
    """
    return float(num1) * float(num2)


def subtract(num1, num2):
    """
    Subtracts two numbers.
    Keyword arguments:
    num1-> float number,
    num2-> float number
    """
    return float(num1) - float(num2)


def divide(num1, num2):
    """
    Divides two numbers.
    Keyword arguments:
    num1-> float number,
    num2-> float number
    """
    return float(num1) / float(num2) if float(num2) else 0
