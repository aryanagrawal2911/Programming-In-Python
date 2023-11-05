# Given an integer array nums, move all 0's to the end of it,
# while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.

def moveZeroes(nums):

    coz = nums.count(0)

    nums[:] = [i for i in nums if (i != 0)]

    for i in range(coz):
        nums.append(0)

    return nums