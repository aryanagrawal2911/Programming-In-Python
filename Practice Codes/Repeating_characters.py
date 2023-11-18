'''
Given a input string, remove all consecutively repeating characters.
'''

def removeConsecutiveDuplicates(s : str) -> str:

    res = s[0]
    rch = s[0]
    i = 1

    while i < len(s):

        if s[i] != rch:
            res += s[i]
            rch = s[i]

        i += 1

    return res


string = input()
print(removeConsecutiveDuplicates(string))
