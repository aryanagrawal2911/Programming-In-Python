# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed.
# Then return the number of elements in nums which are not equal to val.

def removeElement(nums, val):

    while val in nums:
        nums.remove(val)

    return len(nums)