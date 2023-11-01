import random

def repaddmul(x, y):
    
    if x == 0 or y == 0:
        return 0
    
    if y < x:
        x, y = y, x
        
    a = y
        
    for i in range(x - 1):
        y += a
        
    return y

a, b = random.randint(1, 100), random.randint(1, 100)
print(a, b, repaddmul(a, b))