"""
Given two strings, find the longest common substring.

Return the length of it.
"""
__author__ = 'Danyang'


class Solution:
    def longestCommonSubstring(self, A, B):
        """
        let f(i, j) represents the LCS END WITH A[i], B[j]
        f(i, j) = f(i-1, j-1)+1 if A[i] == B[j]
        f(i, j) = 0 otherwise

        notice:
        * return the maxa rather than f[-1]

        Compared to LC Subsequence, LC Substring:
        * f(i, j) second dp function is different
        * return the global maximum length rather than the last one.

        :param A: str
        :param B: str
        :return: the length of the longest common substring.
        """
        m = len(A)
        n = len(B)
        f = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]

        if m == 0 or n == 0:
            return 0

        maxa = -1
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if A[i-1] == B[j-1]:
                    f[i][j] = f[i-1][j-1]+1
                else:
                    f[i][j] = 0
                maxa = max(maxa, f[i][j])

        return maxa  # rather than f[-1][-1]
