# Calculating mathematical factorial of a number {with and without loops}

# Without loop - One Liner
from math import factorial
print(factorial(int(input())))

# With Loops

# Using FOR Loop
def calculateFactorial(n):

    a = 1

    if n == 0 or n == 1:
        return a

    for i in range(2, n + 1):
        a *= i

    return a

# Using WHILE Loop
def calculateFactorial(n):

    a = 1

    if n == 0 or n == 1:
        return a

    i = 2
    while i <= n:
        a *= i
        i += 1

    return a