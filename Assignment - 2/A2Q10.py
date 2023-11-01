# Sum of even digits in a number

def sumofeven(num):
    
    sum = 0

    for i in str(num):

        dig = int(i)

        sum += (1  - (dig % 2)) * dig

    return sum

print(sumofeven(1892))
