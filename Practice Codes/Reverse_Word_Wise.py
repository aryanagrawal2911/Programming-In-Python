# Houses Multiplt Versions of same code

# a.
s = input().split()

for i in reversed(s):
    print(i, end = ' ')
    

# b.
s = input().split()

for i in range(len(s) - 1, -1, -1):
    print(s[i], end = ' ')


# c.
string = input()
a = reversed(string.split())

ans = ' '.join(a)
print(ans)