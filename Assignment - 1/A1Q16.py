# Total no. of seconds in given time duration

d = int(input("Enter days : "))
h = int(input("Enter hours : "))
m = int(input("Enter minutes : "))
s = int(input("Enter seconds : "))

ts = (d * 24 * 3600) + (h * 3600) + (m * 60) + s
print("Total seconds =", ts)
