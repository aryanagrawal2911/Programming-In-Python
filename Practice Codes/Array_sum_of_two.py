# Given an array Arr of N positive integers and another number X.
# Determine whether or not there exist two elements in Arr whose sum is exactly X.
# Method below returns boolean value

def hasTwo(arr, x):

        s = set()

        for i in arr:

            if (x - i) in s:
                return True

            else:
                s.add(i)

        return False