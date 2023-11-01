# Check if a number is an Armstrong number
# E.g. : 370 = (3 ^ 3) + (7 ^ 3) + (0 ^ 3)

import math
def isArmstrong(n):

    assert n >= 0

    s = 0
    a = n

    while a > 0:
        d = a % 10
        s += pow(d, 3)
        a //= 10

    return s == n

li = [i for i in range(1, 1001) if isArmstrong(i)]
print(li)
