# Easy python syntax for sum of digits of integer

n = int(input("Enter the number : "))

s = sum([int(i) for i in str(n)])
print(s)
