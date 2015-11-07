"""
Given an array with positive and negative integers. Re-range it to interleaving with positive and negative integers.

Have you met this question in a real interview? Yes
Example
Given [-1, -2, -3, 4, 5, 6], after re-range, it will be [-1, 5, -2, 4, -3, 6] or any other reasonable answer.

Note
You are not necessary to keep the original order of positive integers or negative integers.

Challenge
Do it in-place and without extra memory.
"""
__author__ = 'Daniel'


class Solution(object):
    def rerange(self, A):
        """
        Algorithm: Two Pointers
        :type A: List[int]
        :rtype: None, in-place
        """
        n = len(A)
        pos_cnt = len(filter(lambda x: x > 0, A))
        # expecting positive
        pos_expt = True if pos_cnt*2 > n else False

        neg = 0  # next negative
        pos = 0  # next positive
        for i in xrange(n):
            while neg < n and A[neg] > 0: neg += 1
            while pos < n and A[pos] < 0: pos += 1
            if pos_expt:
                A[i], A[pos] = A[pos], A[i]
            else:
                A[i], A[neg] = A[neg], A[i]

            if i == neg: neg += 1
            if i == pos: pos += 1

            pos_expt = not pos_expt


if __name__ == "__main__":
    A = [-33, -19, 30, 26, 21, -9]
    Solution().rerange(A)
    assert A == [-33, 30, -19, 26, -9, 21]