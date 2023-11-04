# Given a string encodes it as the character followed by the number of times it consecutively appears
# Example : string = "aaaabbbccbbaa"
# Answer = "a4b3c2b2a2"
# No libraray module or data structure used, only string concatenation

def encode(string):

    co = 1
    rs = ''
    curr = string[0]

    for i in range(1, len(string)):

        if string[i] == curr:
            co += 1

        else:
            rs += (curr + str(co))
            curr = string[i]
            co = 1

    rs += (curr + str(co))

    return rs