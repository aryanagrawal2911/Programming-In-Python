'''
You have given two positive integers N and K.
Your task is to print a series of numbers i.e subtract K from N until it becomes O or negative
then add K until it becomes N.
For Example:
	For N=5, K=2
	Series = [5, 3, 1, -1, 1, 3, 5]
'''

def printSeries(n : int, k : int) -> list:

    sol = []
    val = n

    while val > 0:
        sol.append(val)
        val -= k

    while val <= n:
        sol.append(val)
        val += k

    return sol

n, k = map(int, input().split())
print(printSeries(n, k))
