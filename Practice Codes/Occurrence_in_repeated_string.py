# Complete the function fun() which takes the
# string s , integer k ,integer n and the character c as input parameter and
# returns the occurence of the character c  in the first n characters of the final string.

def fun(self, s,n,c):

    co = s.count(c)

    l = len(s)

    q = n // l
    r = n % l

    t1 = q * co
    t2 = s[: r].count(c)

    return t1 + t2