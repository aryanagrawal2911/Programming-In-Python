# Equilibrium point in an array is an index (or position) such that
# the sum of all elements before that index is same as sum of elements after it.
# Method below returns both index and element of Equilibrium Point
# Return Format : index, element
# Returns -1 if there is no such element exists in array

def equilibriumPoint(arr):

    n = len(arr)

    if n == 1:
        return 0, arr[0]

    su = sum(arr)
    ls = 0

    for i in range(n):

        if ls == (su - arr[i]):
            return i, arr[i]

        ls += arr[i]
        su -= arr[i]

    return -1