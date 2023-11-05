# For a given array and an integer, returns the index of two elements such that
# their sum is equal to given integer, assuming that there exists only one such pair


def twoSum(arr, x):

    dt = {}

    for i, v in enumerate(arr):

        rem = x - arr[i]

        if rem in dt:
            return [i, dt[rem]]

        else:
            dt[v] = i

print(twoSum([3,2,3], 6))