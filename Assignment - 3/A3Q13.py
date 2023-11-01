import math

# code a. Math Sin Series
def sin_series(x, n):
    
    sum = 0.0
    i = 0
    
    while i <= n:
        
        if ((i // 2) % 2) == 0:
            
            sum = sum + (math.pow(x, i) / math.factorial(i))
            
        else:
            
            sum = sum - (((math.pow(x, i)) / math.factorial(i)))
            
        i += 2
        
    return sum

print(f'{sin_series(2, 20)}\t{math.sin(2)}')

# code b. Math Exponent (e ^ x)
def expo(x, n):
    
    sum = 0
    
    for i in range(n + 1):
        
        sum += (math.pow(x, i) / math.factorial(i))
        
    return sum

print(f'{expo(2,22)}\t{math.exp(2)}')
