# Check if the given string S is a Panagram or not.
# A pangram is a sentence containing every letter in the English Alphabet.
# Returns Boolean

def isPanagram(s):

    s = s.lower()

    for i in range(97, 123):

        ch = chr(i)

        if ch not in s:
            return False

    return True