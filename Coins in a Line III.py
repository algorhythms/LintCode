"""
There are n coins in a line. Two players take turns to take a coin from one of the ends of the line until there are no
more coins left. The player with the larger amount of money wins.

Could you please decide the first player will win or lose?

Have you met this question in a real interview? Yes
Example
Given array A = [3,2,2], return true.

Given array A = [1,2,4], return true.

Given array A = [1,20,4], return false.

Challenge
Follow Up Question:

If n is even. Is there any hacky algorithm that can decide whether first player will win or lose in O(1) memory and O(n)
time?
"""
__author__ = 'Daniel'


class Solution:
    def firstWillWin_MLE(self, values):
        """
        DP with Game theory

        Let F_{i, j}^{p} represents the max value he can get in sub-array A[i..j] for person p.

        DP formula:
        F_{i, j}^{0} = max(A_i + sum - F_{i+1, j}^{1},
                           A_j + sum - F_{i, j-1}^{1}
                           )

        Sometimes assuming the opponent will carry out the best strategy eliminate stochastic process
        Memory Limit Exceeded
        :param values: a list of integers
        :return: a boolean which equals to True if the first player will win
        """
        n = len(values)
        if n == 1:
            return True

        F = [[[0 for _ in xrange(n)] for _ in xrange(n)] for _ in xrange(2)]
        s = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            s[i] = s[i-1]+values[i-1]

        for i in xrange(n):
            for p in xrange(2):
                F[p][i][i] = values[i]

        for i in xrange(n-2, -1, -1):
            for j in xrange(i+1, n):
                for p in xrange(2):
                    F[p][i][j] = max(
                        values[i]+s[j+1]-s[i+1]-F[1^p][i+1][j],
                        values[j]+s[j]-s[i]-F[1^p][i][j-1]
                    )

        return F[0][0][n-1]>min(F[1][0][n-2], F[1][1][n-1])

    def firstWillWinNormalCase(self, values):
        """
        optimize data structure

        General solution to this question, but it can be optimized further by using tricks when the number of coins is
        even number.

        Time Limit Exceeded
        :param values: a list of integers
        :return: a boolean which equals to True if the first player will win
        """
        n = len(values)
        if n == 1:
            return True

        SZ = 4
        F = [[[0 for _ in xrange(SZ)] for _ in xrange(SZ)] for _ in xrange(2)]
        s = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            s[i] = s[i-1]+values[i-1]

        for i in xrange(n-2, -1, -1):
            for j in xrange(i+1, n):
                for p in xrange(2):
                    if j == i+1:
                        a = values[i+1]
                        b = values[i]
                    else:
                        a = F[1^p][(i+1)%SZ][j%SZ]
                        b = F[1^p][i%SZ][(j-1)%SZ]

                    F[p][i%SZ][j%SZ] = max(
                        values[i]+s[j+1]-s[i+1]-a,
                        values[j]+s[j]-s[i]-b
                    )

        return F[0][0][(n-1)%SZ] > min(F[1][0][(n-2)%SZ], F[1][1][(n-1)%SZ])

    def firstWillWin(self, values):
        """

        :param values: a list of integers
        :return: a boolean which equals to True if the first player will win
        """
        n = len(values)
        if n%2 == 0 and self.firstWillWinEven(values):
            return True

        return self.firstWillWinNormalCase(values)

    def firstWillWinEven(self, values):
        """
        odd_s: sum of values at odd position
        even_s: sum of values at even position

        if odd_s == even_s, the first mover cannot win if the other player mimics the first player

        if odd_s > even_s, the first mover chooses the odd position values, and FORCE the other player choose the even
        position values. The strategy and outcome are similar when even_s > odd_s.
          
        :param values:
        :return:
        """
        odd_s = 0
        even_s = 0
        for i in xrange(len(values)):
            if i%2 == 0:
                even_s += values[i]
            else:
                odd_s += values[i]

        return odd_s != even_s


if __name__ == "__main__":
    assert Solution().firstWillWin([3, 2, 2]) is True
    assert Solution().firstWillWin([1, 20, 4]) is False
    assert Solution().firstWillWin([1, 2, 3, 4, 5, 6, 7, 8, 13, 11, 10, 9]) is True