# Multiplication table upto 10 of a number

def table(num):
    for i in range(1, 11):
        print(f'{n} * {i} = {n * i}')

n = int(input("Enter the number for its table : "))
table(n)
