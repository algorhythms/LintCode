"""
Given an integer array, find a continuous rotate subarray where the sum of numbers is the biggest. Your code should
return the index of the first number and the index of the last number. (If their are duplicate answer, return anyone)

Have you met this question in a real interview? Yes
Example
Give [3, 1, -100, -3, 4], return [4,0].
"""
__author__ = 'Daniel'
import sys


class Solution:
    def continuousSubarraySumII(self, A):
        """

        :param A:
        :return:
        """


    def continuousSubarraySumII_TLE(self, A):
        """

        :param A: A an integer array
        :return: A list of integers includes the index of the first number and the index of the last number
        """
        max_a = max(A)
        max_sum = -sys.maxint-1
        m_s = -1
        m_e = -1

        cur = 0  # current sum
        s = 0
        e = 0

        rotated = False
        while s < len(A):
            if not rotated and e >= len(A):
                e = 0
                rotated = True

            if rotated and e >= s:
                s += 1
                cur = 0
                if s >= len(A):
                    break
                e = s
                rotated = False

            cur += A[e]

            if max_sum < cur:
                m_s = s
                m_e = e
                max_sum = cur

            if max_a > 0 > cur or 0 >= max_a > cur:  # 2nd condition for all negative arrays
                s = max(s+1, e+1)
                cur = 0

            e += 1

        return [m_s, m_e]


if __name__ == "__main__":
    print Solution().continuousSubarraySumII([-5, 10, 5, -3, 1, 1, 1, -2, 3, -4])