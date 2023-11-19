string = input()

def reverse(string : str) -> str:
    return string[::-1]


def reverse_word_order(string : str) -> str:
    return ' '.join(string.split()[::-1])


def palindrome(string : str) -> bool:
    return string == string[::-1]


def delete(string : str, index : int) -> str:
    return string[:index] + string[index + 1:]


def count(string : str) -> str:

    string = string.lower()
    v, co = 0, 0
    vow = "aeiou"

    for ch in string:
        if ch in vow:
            v += 1
        else:
            co += 1

    return f"Vowels : {v} and Consonants : {co}"


def length(string : str) -> int:

    co = 0

    for i in string:
        co += 1
    return co


def removeDuplicates(string : str) -> str:

    sset = set(string)
    string = ""

    for ch in sset:
        string += ch
    return string


def symmetric(string : str) -> bool:

    mid = len(string) // 2
    return string[:mid] == string[mid:]


def maxfrequency(string : str) -> chr:

    dt = {}

    for ch in string:
        dt[ch] = dt.get(ch, 0) + 1

    return max(dt, key = dt.get)


def  countfrequency(string : str) -> dict:

    dt = {}

    for ch in string:
        dt[ch] = dt.get(ch, 0) + 1

    return dt


def atleastone(string : str) -> bool:
    return string.isalnum()
