"""
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing all 1's and return its area.

Example
For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
"""
__author__ = 'Daniel'


class Solution:
    def maxSquare(self, matrix):
        """
        Algorithm:
        O(n^2)
        let F_{i, j} represents the max square's length ended at matrix_{i, j} (lower right corner).
        F_{i, j} = min{F_{i-1, j}, F_{i, j-1}, F_{i-1, j-1}}+1 // if matrix{i, j} == 1
        F_{i, j} = 0 // otherwise

        O(n^3)
        sandwich approach

        :param matrix: a matrix of 0 and 1
        :return: an integer
        """
        M = len(matrix)
        N = len(matrix[0])
        F = [[0 for _ in xrange(N+1)] for _ in xrange(M+1)]

        gmax = 0
        for i in xrange(1, M+1):
            for j in xrange(1, N+1):
                if matrix[i-1][j-1] == 1:
                    F[i][j] = min(F[i-1][j], F[i][j-1], F[i-1][j-1])+1
                    gmax = max(gmax, F[i][j])

        return gmax*gmax

    def maxSquare_error(self, matrix):
        """
        stack
        :param matrix: a matrix of 0 and 1
        :return: an integer
        """
        M = len(matrix)
        N = len(matrix[0])
        h = [[0 for _ in xrange(N+1)] for _ in xrange(M+1)]
        for i in xrange(1, M+1):
            for j in xrange(1, N+1):
                if matrix[i-1][j-1] == 1:
                    h[i][j] = h[i-1][j]+1
                else:
                    h[i][j] = 0

        ret = 0
        for i in xrange(M):
            stk = []  # col index, inc_stk
            for j in xrange(N):
                while stk and h[i+1][stk[-1]+1] >= h[i+1][j+1]:
                    stk.pop()
                idx = -1
                if stk: idx = stk[-1]
                cur_square = min(j-idx, h[i+1][j+1])
                cur_square *= cur_square
                ret = max(ret, cur_square)
                stk.append(j)

        return ret


if __name__ == "__main__":
    assert Solution().maxSquare([[0,1,0,1,1,0],[1,0,1,0,1,1],[1,1,1,1,1,0],[1,1,1,1,1,1],[0,0,1,1,1,0],[1,1,1,0,1,1]]
    ) == 9