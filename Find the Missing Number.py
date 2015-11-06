"""
Given an array contains N numbers of 0 .. N, find which number doesn't exist in the array.

Example
Given N = 3 and the array [0, 1, 3], return 2.

Challenge
Do it in-place with O(1) extra memory and O(n) time.
"""
__author__ = 'Daniel'


class Solution(object):
    def findMissing(self, nums):
        """
        in-place

        O(N)
        once an elt is inplace, it never moves
        """
        nth = -1
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == n:
                nth = nums[i]
                i += 1
            elif nums[i] != i:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]  # complex first
                # nums[i], nums[nums[i]] = nums[nums[i]], nums[i]  # evaluation order
            else:
                i += 1

        if nth == -1:
            return n
        else:
            return nums.index(nth)


if __name__ == "__main__":
    print Solution().findMissing([9,8,7,6,2,0,1,5,4])




