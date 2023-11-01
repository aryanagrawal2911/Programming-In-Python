def primefs(n):

    i = 2
    
    while i <= n:
        
        if (n % i) == 0:
            print(i)
            n //= i

        else:
            i += 1

num = int(input('Enter an integer (2 or greater) : '))

if num < 2:
        print("Value must be greater than or equal to 2")
        exit(None)

print(f'The prime factors of {num} are : ')

primefs(num)