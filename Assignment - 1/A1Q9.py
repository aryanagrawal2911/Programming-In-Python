import math


a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

root1 = ((-b) + pow(pow(b, 2) - (4 * a * c), 0.5)) / (2 * a)
print(root1)


x = int(input("Enter x : "))
y = int(input("Enter y : "))
v = int(input("Enter v : "))

result = (((2 * x * y) - (9 * y)) / (2 * x * pow(y, 3))) - ((4 * y * pow(x, 2)) / (2 * y))
print(result)


result = (2 * (math.cos(0.5 * (x + y))) * (math.cos(0.5 * (x - y)))) + math.exp(x) - 1 - (x / 4) + math.tan(x) - math.log(v)
print(result)
