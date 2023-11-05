# Given an integer, checks if it is a Palindrome
# Negative integers yield False in both ways

# With string conversion
def checkPalindrome(x: int) -> bool:
    s = str(x)
    return s == s[::-1]


# Without string conversion and by actually reversing the integer
def checkPalindrome(x: int) -> bool:

    if x < 0:
        return False

    a, b = 0, x

    while b > 0:

        a = (a * 10) + (b % 10)
        b //= 10

    return a == x