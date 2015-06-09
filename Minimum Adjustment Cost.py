"""
Given an integer array, adjust each integers so that the difference of every adjcent integers are not greater than a
given number target.

If the array before adjustment is A, the array after adjustment is B, you should minimize the sum of |A[i]-B[i]|

Note
You can assume each number in the array is a positive integer and not greater than 100

Example
Given [1,4,2,3] and target=1, one of the solutions is [2,3,2,3], the adjustment cost is 2 and it's minimal. Return 2.
"""
__author__ = 'Danyang'


class Solution:
    def MinAdjustmentCost(self, A, target):
        """
        state dp

        f[i][j] = min(f[i-1][k] + |a[i]-j|, for k j-l to j+l)

        comments: similar to Vertibi algorithm (Hidden Markov Model)

        :param A: An integer array.
        :param target: An integer.
        """
        S = 100
        n = len(A)
        f = [[1<<31 for _ in xrange(S+1)] for _ in xrange(n+1)]

        for j in xrange(S+1):
            f[0][j] = 0

        for i in xrange(1, n+1):
            for j in xrange(1, S+1):
                for k in xrange(max(1, j-target), min(S, j+target)+1):
                    f[i][j] = min(f[i][j], f[i-1][k]+abs(A[i-1]-j))

        mini = 1<<31
        for j in xrange(1, S+1):
            mini = min(mini, f[n][j])

        return mini


if __name__ == "__main__":
    assert Solution().MinAdjustmentCost([12, 3, 7, 4, 5, 13, 2, 8, 4, 7, 6, 5, 7], 2) == 19

