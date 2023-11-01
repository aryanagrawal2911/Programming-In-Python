# Checking if a non negative integer is a Palindrome

def isPalin(n):

    if n < 0:
        return False

    if 0 <= n <= 9:
        return True

    n = str(n)
    rev = n[::-1]

    return (rev == n)

print(isPalin(1079701))
