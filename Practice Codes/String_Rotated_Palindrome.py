# Given a string s, check if it can be rotated to form a palindrome.
# Method below returns boolean value

def isRotatedPalindrome(s):
    n = len(s)

    for i in range(n):
        r = s[-1] + s[:-1]  # String Rotation by Slicing

        if r == r[::-1]:    # Palindrome Check
            return True

        s = r

    return False
