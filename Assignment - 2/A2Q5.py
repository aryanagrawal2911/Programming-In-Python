# Star like pattern with asterisks in a single loop

for i in range(1, 6):

    j = (5 // 2) + 1

    if i <= j:
        
        print(('\t' * abs(j - i) + ('*\t' * ((2 * i) - 1))))
        
    else:
        
        print(('\t' * abs(j - i) + ('*\t' * ((2 * abs(6 - i)) - 1))))
        

print("$  $  $  $  $")
print("$           $")
print("$           $")
print("$           $")
print("$  $  $  $  $")
