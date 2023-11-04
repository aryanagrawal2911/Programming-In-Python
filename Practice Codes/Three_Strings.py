# Given three strings, check if the characters and number of their occurrence in the first and second string,
# combined is contained in the third string

# Easy to understand logic, using dictionary(Hashmap)
def amazingStrings(first, second, third):
    
    dt = {}
    df = {}

    for i in first:
        dt[i] = dt.get(i, 0) + 1

    for i in second:
        dt[i] = dt.get(i, 0) + 1

    for i in third:
        df[i] = df.get(i, 0) + 1

    for i in dt:

        if i not in df:
            return False

        else:
            if dt[i] != df[i]:
                return False

    return True