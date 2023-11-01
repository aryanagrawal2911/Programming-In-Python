# Maximum value from three integers with nested function

def maxim(a, b, c):
    
    def maxi(x, y):
        return max(x, y)
    
    ab = maxi(a, b)
    return maxi(ab, c)
    
print(maxim(76427, 83783, 73873))

# One Liner

print(max(76427, 83783, 73873))