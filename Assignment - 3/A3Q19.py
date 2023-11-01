t = 0
c = 0

value = int(input("Enter a value (0 to quit): "))

if value == 0:
    print("Error: The first value cannot be 0.")

else:

    while value != 0:

        t += value
        c += 1
        value = int(input("Enter a value (0 to quit): "))

    avg = t / c
    print("Average :", avg)