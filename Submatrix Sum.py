"""
Given an integer matrix, find a submatrix where the sum of numbers is zero. Your code should return the coordinate of
the left-up and right-down number.

Example
Given matrix

[
  [1 ,5 ,7],
  [3 ,7 ,-8],
  [4 ,-8 ,9],
]
return [(1,1), (2,2)]

Challenge
O(n^3) time.
"""
__author__ = 'Daniel'


class Solution:
    def submatrixSum(self, matrix):
        """
        dp O(n^3)
        Set the floor and ceiling inside the matrix, and then scan the subcolumns in between the ceiling and the floor

        :param matrix: an integer matrix
        :return: the coordinate of the left-up and right-down number
        """
        m = len(matrix)
        n = len(matrix[0])
        to_top = [[0 for _ in xrange(n+1)] for _ in xrange(m+1)]  # the sum of sub-column starting from row=0 to row=i
        for i in xrange(1, m+1):
            for j in xrange(1, n+1):
                to_top[i][j] = to_top[i-1][j] + matrix[i-1][j-1]

        for up in xrange(m):
            for down in xrange(up, m):
                h = {}  # map to store the previous sub-column sum
                s = 0
                h[s] = -1  # edge case
                for j in xrange(n):
                    s += to_top[down+1][j+1] - to_top[up][j+1]
                    if s in h:
                        return [[up, h[s]+1], [down, j]]
                    h[s] = j

        return [[-1, -1], [-1, -1]]

if __name__ == "__main__":
    assert Solution().submatrixSum([
        [1, 5, 7],
        [3, 7, -8],
        [4, -8, 9],
    ]) == [[1, 1], [2, 2]]



