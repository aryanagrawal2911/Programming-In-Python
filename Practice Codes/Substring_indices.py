# Given two strings, one is a text string, txt and other is a pattern string, pat.
# The task is to print the indexes of all the occurences of pattern string in the text string.
# Returns a list containing all occurrence indices or else -1

def search(pat, txt):

    if pat not in txt:
        return [-1]

    so = []
    index = 0

    while index < len(txt):

        a = txt.find(pat, index)

        if a == -1:
            break

        so.append(a + 1)
        index = a + 1

    return so