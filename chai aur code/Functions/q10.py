# Recursive Function

# Problem: Create a recursive function to calculate the factorial of a number.

# def add(a, b):
#     add(2, 3)

def factorial(n):
    if n == 0:
        return 1
    else:
        git return n * factorial(n-1)
