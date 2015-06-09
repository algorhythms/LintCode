"""
Given a sequence of integers, find the longest increasing subsequence (LIS).

You code should return the length of the LIS.
"""
__author__ = 'Danyang'


class Solution:
    def longestIncreasingSubsequence(self, nums):
        """
        let f(i) be the LIS END WITH A[i]
        f(i) = max(f(j)+1) if A[i]>=A[j] \forall j, j<i

        notice:
        * return the maximum rather than f[-1]
        * O(n^2)

        :param nums: The integer array
        :return: The length of LIS
        """
        n = len(nums)
        if n == 0:
            return 0

        maxa = 1
        f = [1 for _ in xrange(n)]
        for i in xrange(n):
            for j in xrange(i):
                if nums[i] >= nums[j]:
                    f[i] = max(f[i], f[j]+1)

            maxa = max(maxa, f[i])

        return maxa  # rather than f[-1]


if __name__ == "__main__":
    assert Solution().longestIncreasingSubsequence(
        [88, 4, 24, 82, 86, 1, 56, 74, 71, 9, 8, 18, 26, 53, 77, 87, 60, 27, 69, 17, 76, 23, 67, 14, 98, 13, 10, 83, 20,
         43, 39, 29, 92, 31, 0, 30, 90, 70, 37, 59]) == 10