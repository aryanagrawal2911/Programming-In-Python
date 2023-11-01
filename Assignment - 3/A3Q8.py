# Checking if a number is a "Perfect" number
# The sum of all divisors of a number (except for itself, obviously) must be equal to it

def isPerfect(n):
    
    s = sum([i for i in range(1, n) if (not(n % i))])
          
    return (n == s)

print(isPerfect(int(input('Enter a positive integer : '))))