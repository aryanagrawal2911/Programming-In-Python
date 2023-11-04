# Given a string, returns a list containing all the palindromic words in a string, else gives 0 in a list

def PalindromeWords(s):

    words = s.split()
    ans = ['0']

    for word in words:

        lword = word.lower()

        if len(word) == 1:
            ans.append(word)

        elif lword == lword[::-1]:
            ans.append(word)

    return ans