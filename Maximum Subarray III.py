"""
Given an array of integers and a number k, find k non-overlapping subarrays which have the largest sum.

The number in each subarray should be contiguous.

Return the largest sum.

Note
The subarray should contain at least one number
"""
__author__ = 'Danyang'


class Solution:
    def maxKSubArrays(self, nums, k):
        """
        state dp

        f(i, k): max sum of subproblem ending with i, with k subarrays
        g(i, k): max sum of subproblem ending with OR before i, with k subarrays

        f(i, k) = max(g(j-1, k-1)+sum(nums[j..i]), for j)
        g(i, k) = max(f(j, k), for j)

        reference: http://meetqun.com/thread-3367-1-1.html

        :param nums: A list of integers
        :param k: An integer denote to find k non-overlapping subarrays
        :return: An integer denote the sum of max k non-overlapping subarrays
        """
        n = len(nums)
        f = [[0 for _ in xrange(k+1)] for _ in xrange(n+1)]
        g = [[0 for _ in xrange(k+1)] for _ in xrange(n+1)]

        s = [0 for _ in xrange(n+1)]  # sum
        for i in xrange(1, n+1):
            s[i] = s[i-1]+nums[i-1]

        for i in xrange(1, n+1):
            for st in xrange(1, k+1):
                if st == 1:  # dummies nodes does not works well with negative numbers
                    f[i][st] = max([s[i]-s[j] for j in xrange(i)])
                else:
                    f[i][st] = max([g[j][st-1]+s[i]-s[j] for j in xrange(i)])

                g[i][st] = max([f[j][st] for j in xrange(i+1)])

        maxa = -1<<31
        for i in xrange(1, n+1):
            maxa = max(maxa, g[i][k])
        return maxa


if __name__ == "__main__":
    print Solution().maxKSubArrays([1, 2, 3], 1)
    print Solution().maxKSubArrays([-1, -2, -3, -100, -1, -50], 2)