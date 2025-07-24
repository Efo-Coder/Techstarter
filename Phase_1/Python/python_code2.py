# This script calculates the factorial of a given number using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Beispiel
number = 5
print(f"The factorial of {number} is {factorial(number)}")