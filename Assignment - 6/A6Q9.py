string = input()

def reverse(string):
    return string[::-1]


def reverse_word_order(string):
    return ' '.join(string.split()[::-1])


def palindrome(string):
    return string == string[::-1]


def  delete(string, index):
    return string[:index] + string[index + 1:]


def count(string):

    string = string.lower()
    v, co = 0, 0
    vow = "aeiou"

    for ch in string:
        if ch in vow:
            v += 1
        else:
            co += 1

    return f"Vowels : {v} and Consonants : {co}"


def length(string):
    co = 0
    for i in string:
        co += 1
    return co


def removeDuplicates(string : str):
    sset = set(string)
    string = ""
    for ch in sset:
        string += ch
    return string


