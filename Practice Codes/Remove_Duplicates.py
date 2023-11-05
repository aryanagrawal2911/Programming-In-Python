# Given an integer array "arr" sorted in non-decreasing order,
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Then return the number of unique elements in "arr", and the array itself.

# Easy short code with basic "Set" data structure

def removeDuplicates(arr):

    arr[:] = sorted(set(arr))   # ":" used for in place replacement
    return len(arr), arr