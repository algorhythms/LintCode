"""
Given an integer array, find a continuous rotate subarray where the sum of numbers is the biggest. Your code should
return the index of the first number and the index of the last number. (If their are duplicate answer, return anyone)

Example
Give [3, 1, -100, -3, 4], return [4,0].
"""
__author__ = 'Daniel'
from collections import namedtuple

Sum = namedtuple("Sum", "sum i j")  # data structure to store the sum and the starting and ending index.


class Solution:
    def continuousSubarraySumII(self, A):
        """

        :param A:
        :return:
        """
        if len(A) < 1:
            return [-1, -1]
        linear = self.linear_max_sum(A)
        circular = self.circular_max_sum(A)
        if linear.sum > circular.sum:
            return [linear.i, linear.j]

        return [circular.i, circular.j]

    def circular_max_sum(self, A):
        """
        dp:
        left: max sum for index 0..i
        right: max sum for index i..(n-1)

        :param A:
        :return:
        """
        n = len(A)
        left = [None for _ in A]
        right = [None for _ in A]

        cur, max_sum, idx = 0, A[0], 0
        for i in xrange(n):
            cur += A[i]
            if cur > max_sum:
                idx = i
                max_sum = cur
            left[i] = (max_sum, idx)

        cur, max_sum, idx = 0, A[n-1], n-1
        for i in xrange(n-1, -1, -1):
            cur += A[i]
            if cur > max_sum:
                idx = i
                max_sum = cur
            right[i] = (max_sum, idx)

        ret = Sum(A[0], 0, 0)
        for i in xrange(1, n):
            r = right[i]
            l = left[i-1]
            if ret.sum < r[0]+l[0]:
                ret = Sum(r[0]+l[0], r[1], l[1])

        return ret

    def linear_max_sum(self, A):
        """
        Break at 0
        Same as Continuous Subrarry Sum I.

        :param A: an integer array
        :return: A list of integers includes the index of the first number and the index of the last number
        """
        ret = Sum(A[0], 0, 0)

        cur = 0  # current sum
        s = 0
        for e, v in enumerate(A):
            cur += v
            if ret.sum < cur:
                ret = Sum(cur, s, e)

            if cur < 0:
                s = e+1
                cur = 0

        return ret

if __name__ == "__main__":
    assert Solution().continuousSubarraySumII([3, 1, -100, -3, 4]) == [4, 1]
    assert Solution().continuousSubarraySumII([-5, 10, 5, -3, 1, 1, 1, -2, 3, -4]) == [1, 8]