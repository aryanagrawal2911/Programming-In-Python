# An element of array is leader if it is greater than or equal to all the elements to its right side.
# The rightmost element is always a leader.
# The method below contains a list containing all the Leaders of the given array.

def leaders(self, arr):

        n = len(arr)
        sol = []
        x = arr[-1]
        sol.insert(0, x)

        for i in range(n - 2, -1, -1):

            if arr[i] >= x:
                x = arr[i]
                sol.insert(0, x)

        return sol