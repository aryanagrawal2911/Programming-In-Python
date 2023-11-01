c = 11
while c > -1:
    print(c)
    c -= 1
print("Donezo!!")

num = 19
inp = int(input("Try guessing the number : "))

while inp != num:
    inp = int(input("Incorrect! Try again : "))

print("Done eh?? Took you long enough...")

i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        break
    print('*')