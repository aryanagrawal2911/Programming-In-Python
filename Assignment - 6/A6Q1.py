def replaceConsecutiveDuplicates(s : str) -> str:

    res = s[0]
    rch = s[0]
    i = 1

    while i < len(s):

        if s[i] != rch:
            res += s[i]
            rch = s[i]

        else:
            res += "*"

        i += 1

    return res


string = input()
print(replaceConsecutiveDuplicates(string))