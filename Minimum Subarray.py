"""
Given an array of integers, find the subarray with smallest sum.

Return the sum of the subarray.

Note
The subarray should contain at least one integer.

Example
For [1, -1, -2, 1], return -3
"""
__author__ = 'Danyang'


class Solution:
    def minSubArray(self, nums):
        """
        Greedy, dp

        :param nums: a list of integers
        :return: A integer denote the sum of minimum subarray
        """

        mini = min(nums)
        current = 0
        for a in nums:
            current += a
            mini = min(mini, current)
            if current > 0:
                current = 0

        return mini


if __name__ == "__main__":
    assert Solution().minSubArray([1, -1, -2, 1]) == -3


