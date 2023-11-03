# Given a pattern string and a test string,
# If the pattern is preceded by a ^,
# the pattern(excluding the ^) will be matched with the starting position of the text string.
# Similarly, if it is preceded by a $,
# the pattern(excluding the $) will be matched with the ending position of the text string.
# If no such markers are present, it will be checked whether pattern is a substring of test.

# Returns Boolean value


# s ---> String
# sus --> Substring
def isPresent(s, sus):

    if sus[0] == '^':

        sus = sus[1 :]
        pl = len(sus)

        if s[: pl] == sus:
            return True

    elif sus[-1] == '$':

        sus = sus[: -1]
        pl = len(sus)

        if s[-pl :] == sus:
            return True

    else:

        if sus in s:
            return True

    return False


# Easy Short code for those with module and inbuilt method know-how

import re

def isPatternPresent(s, sus):

    if re.search(sus, s):
        return True

    return False