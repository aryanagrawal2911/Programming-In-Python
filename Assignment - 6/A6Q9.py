def reverse(string):
    return string[::-1]

def reverse_word_order(string):
    return ' '.join(string.split()[::-1])

string = input()
print(f"{reverse(string)}\n{reverse_word_order(string)}")