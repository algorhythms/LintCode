"""
Give you an integer array (index from 0 to n-1, where n is the size of this array), find the longest increasing
continuous subsequence in this array. (The definition of the longest increasing continuous subsequence here can be from
right to left or from left to right)

Example
For [5, 4, 2, 1, 3], the LICS is [5, 4, 2, 1], return 4.

For [5, 1, 2, 3, 4], the LICS is [1, 2, 3, 4], return 4.

Note
O(n) time and O(1) extra space.
"""
__author__ = 'Daniel'


class Solution:
    def longestIncreasingContinuousSubsequence(self, A):
        """
        Trivial
        :rtype: int
        """
        n = len(A)
        if n < 1:
            return 0

        maxa = 1
        cur = 1
        for i in xrange(1, n):  # from left
            if A[i] > A[i-1]:
                cur += 1
                maxa = max(maxa, cur)
            else:
                cur = 1

        cur = 1
        for i in xrange(1, n):  # from right
            if A[n-1-i] > A[n-1-i+1]:
                cur += 1
                maxa = max(maxa, cur)
            else:
                cur = 1

        return maxa
