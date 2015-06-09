"""
Given an array with integers.

Find two non-overlapping subarrays A and B, which |SUM(A) - SUM(B)| is the largest.

Return the largest difference.

Note
The subarray should contain at least one number

Example
For [1, 2, -3, 1], return 6

Challenge
O(n) time and O(n) space.
"""
__author__ = 'Danyang'


class Solution:
    def maxDiffSubArrays(self, nums):
        """
        Algorithm: dp
        Maximum Subarray Difference
        <= largest difference, max sum - min sum
        <= max subarray sum and min subarray sum
        <= because non-overlapping max/min subarray sum on one side, the other on the other side
        <= split the array into half

        :param nums: A list of integers
        :return: An integer indicate the value of maximum difference between two Subarrays
        """
        n = len(nums)
        min_left = list(nums)
        max_left = list(nums)
        min_right = list(nums)
        max_right = list(nums)


        # min subarray
        current = 0
        for i in xrange(n):
            current += nums[i]
            if i-1 >= 0:
                min_left[i] = min(current, min_left[i-1], min_left[i])
            else:
                min_left[i] = min(current, min_left[i])

            if current > 0:
                current = 0

        # max subarray
        current = 0
        for i in xrange(n):
            current += nums[i]
            if i-1 >= 0:
                max_left[i] = max(current, max_left[i-1], max_left[i])
            else:
                max_left[i] = max(current, max_left[i])

            if current < 0:
                current = 0

        current = 0
        for i in xrange(n-1, -1, -1):
            current += nums[i]
            if i+1 <= n-1:
                max_right[i] = max(current, max_right[i+1], max_right[i])
            else:
                max_right[i] = max(current, max_right[i])

            if current < 0:
                current = 0

        current = 0
        for i in xrange(n-1, -1, -1):
            current += nums[i]
            if i+1 <= n-1:
                min_right[i] = min(current, min_right[i+1], min_right[i])
            else:
                min_right[i] = min(current, min_right[i])

            if current > 0:
                current = 0

        maxa = 0
        for i in xrange(n-1):
            maxa = max(maxa, abs(max_left[i]-min_right[i+1]), abs(min_left[i]-max_right[i+1]))

        return maxa


if __name__ == "__main__":
    print Solution().maxDiffSubArrays([-4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -4, 5, -1000])



