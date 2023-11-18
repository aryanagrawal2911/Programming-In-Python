words = input().split()
new_array = []

for word in words:
    new_array.append((word[0]).upper() + (word[1:]).lower())

string = ' '.join(new_array)
print(string)