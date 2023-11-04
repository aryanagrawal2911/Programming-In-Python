# Returns the first unique chracter of a string (is Case Sensitive)
# If there is no such character, returns None

def firstNonRepeatingCharacter(str):

    dt = {}

    for i in str:
        dt[i] = dt.get(i, 0) + 1

    for i in str:
        if dt[i] == 1:
            return i

    return None