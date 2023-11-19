# Program to check if or not a given non - negative integer is a term of the Fibonacci series.

def checkMember(n):

    a = 0
    i = 2
    arr = [0, 1]

    while(a <= n):

        arr.append(arr[i - 1] + arr[i - 2])

        a = arr[i]
        i += 1

    return (n in arr)

n=int(input())
print(checkMember(n)):
