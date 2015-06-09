"""
Given an integers array A.

Define B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1], calculate B without divide operation.

Example
For A=[1, 2, 3], B is [6, 3, 2]
"""
__author__ = 'Danyang'


class Solution:
    def productExcludeItself(self, A):
        """
        dp array to store the cumulative products

        :param A: Given an integers array A
        :return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
        """
        n = len(A)
        if n == 1:
            return []

        dp = [[1, 1] for _ in xrange(n)]
        for i in xrange(1, n):
            dp[i][0] = A[i-1]*dp[i-1][0]
            dp[n-i-1][1] = A[n-i]*dp[n-i][1]

        B = [dp[i][0]*dp[i][1] for i in xrange(n)]
        return B

if __name__=="__main__":
    assert Solution().productExcludeItself([1, 2, 3]) == [6, 3, 2]