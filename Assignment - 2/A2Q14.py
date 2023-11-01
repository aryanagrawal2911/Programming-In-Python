# Convert lowercase input to uppercase with user-defined function

def uppercase(string):

    return string.upper()

s = input('Enter lowercase input :')
x = ord(s)
assert 97 <= x <= 122
print(uppercase(s))

# Two-Liner short code :

s = input('Enter lowercase input :').upper()
print(s)