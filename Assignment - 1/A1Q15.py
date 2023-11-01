# Manual sorting of three numbers

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

ma = max(a, b, c)
mi = min(a, b, c)
mid = (a + b + c) - (ma + mi)

print("Sorted :", mi, mid, ma)
