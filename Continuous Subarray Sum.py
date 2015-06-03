"""
Given an integer array, find a continuous subarray where the sum of numbers is the biggest. Your code should return the
index of the first number and the index of the last number. (If their are duplicate answer, return anyone)

Example
Give [-3, 1, 3, -3, 4], return [1,4].
"""
__author__ = 'Daniel'


class Solution:
    def continuousSubarraySum(self, A):
        """
        Break at 0

        :param A: an integer array
        :return: A list of integers includes the index of the first number and the index of the last number
        """
        if len(A) < 1:
            return [-1, -1]

        m_s, m_e = 0, 0  # inclusive index
        max_sum = A[0]

        cur = 0  # current sum
        s = 0
        for e, v in enumerate(A):
            cur += v
            if max_sum < cur:
                m_s, m_e = s, e
                max_sum = cur

            if cur < 0:
                s = e+1
                cur = 0

        return [m_s, m_e]


if __name__ == "__main__":
    assert Solution().continuousSubarraySum(
        [-101, -33, -44, -55, -67, -78, -101, -33, -44, -55, -67, -78, -100, -200, -1000, -22, -100, -200, -1000, -22]
    ) == [15, 15]
