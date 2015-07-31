"""
On one line there are n houses. Give you an array of integer means the the position of each house. Now you need to pick
k position to build k post office, so that the sum distance of each house to the nearest post office is the smallest.
Return the least possible sum of all distances between each village and its nearest post office.

Example
Given array a = [1,2,3,4,5], k = 2. return 3.

Challenge
Could you solve this problem in O(n^2) time ?
"""
__author__ = 'Daniel'


class Solution:
    def postOffice_TLE(self, A, K):
        """
        dp
        O(n^3), TLE
        :type A: list[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        N = len(A)
        F = [[0 for _ in xrange(K+1)] for _ in xrange(N+1)]
        c = [[0 for _ in xrange(N+1)] for _ in xrange(N+1)]  # [i, j)

        for i in xrange(N):
            for j in xrange(i+1, N+1):
                m = (i+j)/2
                for l in xrange(i, j):
                    c[i][j] += abs(A[m]-A[l])

        for n in xrange(1, N+1):
            F[n][1] = c[0][n]

        for n in xrange(1, N+1):
            for k in xrange(2, K+1):
                F[n][k] = min(
                    F[l][k-1]+c[l][n] for l in xrange(n)
                )

        return F[N][K]

    def postOffice_TLE(self, A, K):
        """
        dp
        O(n^2) using quadratic inequality
        :type A: list[int]
        :type K: int
        :rtype: int
        """
        # TODO


if __name__ == "__main__":
    assert Solution().postOffice([112,122,360,311,85,225,405,53,405,43,342,13,588,424,299,37,104,289,404,414], 3) == 673