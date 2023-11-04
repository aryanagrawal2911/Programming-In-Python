# Complete the function atoi() which takes a string as input parameter and
# returns integer value of it. if the input string is not a numerical string then returns -1.
# Note: Numerical strings are the string where either every character is in between 0-9 or
# where the first character is '-' and the rest all characters are in between 0-9.

def atoi(st):

    nflag = 0

    if st[0] == '-':
        nflag = 1
        st = st[1:]

    for i in st:
        if not(48 <= ord(i) <= 57):
            return -1

    a = 0

    for i in st:
        d = ord(i) - ord('0')
        a = (a * 10) + d

    if nflag == 1:
        return -a

    return a