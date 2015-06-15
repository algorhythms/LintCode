"""
Given an integer array, find a continuous subarray where the sum of numbers is the biggest. Your code should return the
index of the first number and the index of the last number. (If their are duplicate answer, return anyone)

Example
Give [-3, 1, 3, -3, 4], return [1,4].
"""
__author__ = 'Daniel'
from collections import namedtuple
Sum = namedtuple("Sum", "sum i j")  # data structure to store the sum and the starting and ending index.


class Solution:
    def continuousSubarraySum(self, A):
        """
        Break at 0

        :param A: an integer array
        :return: A list of integers includes the index of the first number and the index of the last number
        """
        if len(A) < 1:
            return [-1, -1]

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

        return [ret.i, ret.j]


if __name__ == "__main__":
    assert Solution().continuousSubarraySum(
        [-101, -33, -44, -55, -67, -78, -101, -33, -44, -55, -67, -78, -100, -200, -1000, -22, -100, -200, -1000, -22]
    ) == [15, 15]
