"""
There is an integer matrix which has the following features:

The numbers in adjacent positions are different.
The matrix has n rows and m columns.
For all i < m, A[0][i] < A[1][i] && A[n - 2][i] > A[n - 1][i].
For all j < n, A[j][0] < A[j][1] && A[j][m - 2] > A[j][m - 1].
We define a position P is a peek if A[j][i] > A[j+1][i] && A[j][i] > A[j-1][i] && A[j][i] > A[j][i+1] && A[j][i] >
A[j][i-1].

Find a peak element in this matrix. Return the index of the peak.

Example
Given a matrix:

[
  [1 ,2 ,3 ,6 ,5],
  [16,41,23,22,6],
  [15,17,24,21,7],
  [14,18,19,20,10],
  [13,14,11,10,9]
]
return index of 41 (which is [1,1]) or index of 24 (which is [2,2])

Note
The matrix may contains multiple peeks, find any of them.

Challenge
Solve it in O(n+m) time.

If you come up with an algorithm that you thought it is O(n log m) or O(m log n), can you prove it is actually O(n+m) or
propose a similar but O(n+m) algorithm?
"""
import sys

__author__ = 'Daniel'


class Solution:
    def findPeakII(self, A):
        """
        T(m, n) = T(m, n/2) + O(m) = T(m/2, n/2) + O(m) + O(n/2) = ... = O(m+n)

        Dimension reduction: Project 2D to 1D by representing the column vector using the representative item

        :param A: An list of list integer
        :return: The index of position is a list of integer, for example [2,2]
        """
        minint = -sys.maxint-1

        left = 0
        right = len(A[0])
        top = 0
        bottom = len(A)

        while left < right and top < bottom:
            if right-left > bottom-top:
                mid = (right+left)/2
                l_max = minint  # left
                r_max = minint  # right
                c_max = minint  # center
                c_i, c_j = -1, -1  # for c_max
                for i in xrange(top, bottom):
                    l_max = max(l_max, A[i][mid-1])
                    r_max = max(r_max, A[i][mid+1])
                    c_max = max(c_max, A[i][mid])
                    if c_max == A[i][mid]:
                        c_i, c_j = i, mid

                if l_max > c_max and l_max > r_max:
                    right = mid
                elif r_max > c_max and r_max > l_max:
                    left = mid+1
                else:
                    return [c_i, c_j]

            else:
                mid = (top+bottom)/2
                u_max = minint  # up
                d_max = minint  # down
                c_max = minint  # center
                c_i, c_j = -1, -1
                for j in xrange(left, right):
                    u_max = max(u_max, A[mid-1][j])
                    d_max = max(d_max, A[mid+1][j])
                    c_max = max(c_max, A[mid][j])
                    if c_max == A[mid][j]:
                        c_i, c_j = mid, j

                if u_max > c_max and u_max > d_max:
                    bottom = mid
                elif d_max > c_max and d_max > u_max:
                    top = mid+1
                else:
                    return [c_i, c_j]

        return [-1, -1]


if __name__ == "__main__":
    A = [
        [1,  2,  3,  4,   5, 6],
        [14, 15, 16, 17, 18, 8],
        [12, 13, 11, 10,  9, 7]
    ]

    print Solution().findPeakII(A)