"""
Given two strings, find the longest comment subsequence (LCS).

Your code should return the length of LCS.
"""
__author__ = 'Danyang'


class Solution:
    def longestCommonSubsequence(self, A, B):
        """
        let f(i, j) represents the LCS END WITH A[i], B[j]
        f(i, j) = f(i-1, j-1)+1, if A[i] == A[j]
        f(i, j) = max{f(i-1, j), f(i, j-1)}, otherwise

        :param A: str
        :param B: str
        :return: The length of longest common subsequence of A and B.
        """
        m = len(A)
        n = len(B)
        f = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]

        if m == 0 or n == 0:
            return 0

        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                if A[i-1] == B[j-1]:
                    f[i][j] = f[i-1][j-1]+1
                else:
                    f[i][j] = max(f[i][j-1], f[i-1][j])

        return f[-1][-1]