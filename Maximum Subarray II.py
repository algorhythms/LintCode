"""
Given an array of integers, find two non-overlapping subarrays which have the largest sum.

The number in each subarray should be contiguous.

Return the largest sum.

Note
The subarray should contain at least one number

Example
For given [1, 3, -1, 2, -1, 2], the two subarrays are [1, 3] and [2, -1, 2] or [1, 3, -1, 2] and [2], they both have
the largest sum 7.

Challenge
Can you do it in time complexity O(n) ?
"""
__author__ = 'Danyang'


class Solution:
    def maxTwoSubArrays(self, nums):
        """
        dp max subarray

        fi for subarry that ends WITH OR BEFORE i
         
        f1 for forward sweeping
        f2 for backward sweeping
        :param nums: A list of integers
        :return: An integer denotes the sum of max two non-overlapping subarrays
        """
        n = len(nums)

        f = [[-1<<31 for _ in xrange(n+1)] for _ in xrange(2)]

        cur = 0
        for i in xrange(1, n+1):
            cur += nums[i-1]
            f[0][i] = max(nums[i-1], f[0][i-1], cur)
            if cur < 0:
                cur = 0

        cur = 0
        for i in xrange(n-1, -1, -1):
            cur += nums[i]
            f[1][i] = max(nums[i], f[1][i+1], cur)
            if cur < 0:
                cur = 0

        maxa = -1<<31
        for i in xrange(1, n):
            maxa = max(maxa, f[0][i]+f[1][i])
        return maxa


if __name__ == "__main__":
    print Solution().maxTwoSubArrays([1, 3, -1, 2, -1, 2])





