def sumofdigits(n):

    s = sum([int(i) for i in str(n)])
    return s

print(sumofdigits(789642))
