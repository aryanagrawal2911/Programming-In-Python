from sympy import divisors
import random

def iscoprime(x, y):
    
    assert (x > 0) and (y > 0)

    xs = set(divisors(x))
    ys = set(divisors(y))
    
    a = list(xs.intersection(ys))
    
    if (len(a) == 1) and (a[0] == 1):
        return True
    
    return False

a, b = random.randint(1, 100), random.randint(1, 100)
print(a, b, iscoprime(a, b))