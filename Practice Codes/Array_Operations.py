# You are given an array nums of size n consisting of non-negative integers.
# You need to apply n - 1 operations to this array where, in the ith operation (0-indexed),
# you will apply the following on the ith element of nums:
# If nums[i] == nums[i + 1], then multiply nums[i] by 2 and set nums[i + 1] to 0.
# Otherwise, you skip this operation.
# After performing all the operations, shift all the 0's to the end of the array.

def applyOperations(self, nums):

    n = len(nums)

    for i in range(n - 1):

        if nums[i] == nums[i + 1]:
            nums[i] *= 2
            nums[i + 1] = 0

    coz = nums.count(0)
    nums[:] = [i for i in nums if (i != 0)]

    for i in range(coz):
        nums.append(0)

    return nums