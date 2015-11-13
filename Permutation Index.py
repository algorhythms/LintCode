"""
Given a permutation which contains no repeated number, find its index in all the permutations of these numbers, which
are ordered in lexicographical order. The index begins at 1.

Given [1,2,4], return 1.
"""
import math

__author__ = 'Daniel'


class Solution:
    def permutationIndex(self, A):
        """
        Cantor expansion

        Inversions: O(n^2) or O(n lg n)
        O(n) count
        """
        n = len(A)
        idx = 0
        for i, v in enumerate(A):
            inv = 0
            for j in xrange(i+1, n):
                if A[i] > A[j]:
                    inv += 1

            idx += inv * math.factorial(n-1-i)

        return idx+1
