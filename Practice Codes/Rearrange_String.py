# Given a string containing uppercase alphabets and integer digits (from 0 to 9),
# the task is to print the alphabets in the lexicographical order followed by the sum of digits.
# Returns String

def arrangeString(s):

    st = ''
    su = 0

    for i in s:

        if i.isalpha():
            st = st + i

        else:
            su += int(i)

    s = ''
    s = ''.join(sorted(st))

    if su != 0:
        s = s + str(su)

    return s
