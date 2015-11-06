"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example
For example, given the array [2,3,-2,4], the contiguous subarray [2,3] has the largest product = 6.
"""
__author__ = 'Daniel'


class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0

        n = len(nums)
        smallest = list(nums)
        largest = list(nums)
        maxa = nums[0]
        for i in xrange(1, n):
            v = nums[i]
            smallest[i] = min(v, smallest[i-1]*v, largest[i-1]*v)
            largest[i] = max(v, smallest[i-1]*v, largest[i-1]*v)
            maxa = max(maxa, largest[i])

        return maxa


if __name__ == "__main__":
    assert Solution().maxProduct([2, 3, -2, 4]) == 6