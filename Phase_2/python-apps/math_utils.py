def add(a, b):
    """Addiert zwei Zahlen."""
    return a + b

def subtract(a, b):
    """Subtrahiert zwei Zahlen."""
    return a - b

def multiply(a, b):
    """Multipliziert zwei Zahlen."""
    return a * b

def divide(a, b, isIntegerDivision=False):
    """Dividiert zwei Zahlen."""
    if isIntegerDivision:
        return a // b
    else:
        return round(a / b, 2)

def pow(a, n):
    """Berechnet die n-te Potenz aus einer Zahl."""
    return a**n

def root(a, n):
    """Berechnet die n-te Wurzel aus einer Zahl."""
    return round(a ** (1/n), 2)