'''
You are given an array of integers NUM consisting of N elements.
This array represents the digits of a number. Your task is to increase the number by 1, or we can say you have to add 1 to this number.
The number will be positive, and digits are stored so that the most significant digit is at the starting of the array.

For example:
Let input array is [1.3.2.7] so basically, this array represents the number 1327, the output will be [1.3,2,8).

Note:
The input may have O at the starting of the array, e.g., [0,3,5,7] is a valid input, but the output can not have 0 before the most significant digit.
So [0,3,5,8] will be a wrong answer, and the correct answer will be [3,5,8].
'''

def addOne(array : list) -> list:

    if array[0] == 0:
        array[:] = array[1:]	# Modifying the list in place

    if array[-1] == 9:
        n = int(''.join(map(str, array)))
        n += 1
        array = [int(i) for i in str(n)]
        return array

    array[-1] += 1
    return array
