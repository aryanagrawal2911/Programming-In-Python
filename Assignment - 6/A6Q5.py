import re

string = input()
count = len(re. findall(r'\w+', string))
print(count)