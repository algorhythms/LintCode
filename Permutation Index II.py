"""
Given a permutation which may contain repeated numbers, find its index in all the permutations of these numbers, which
are ordered in lexicographical order. The index begins at 1.

Example
Given the permutation [1, 4, 2, 2], return 3.
"""
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def permutationIndexII(self, A):
        """
        TODO
        """
        idx = 0
        factor = 1
        cnt = defaultdict(int)

        cnt[A[-1]] += 1
        n = len(A)
        for i in xrange(n-2, -1, -1):
            cnt[A[i]] += 1  # counter at current position, not full A.
            for k, v in cnt.items():
                if k < A[i]:
                    idx += v * factor / cnt[A[i]]

            factor = factor * (n-i) / cnt[A[i]]

        return idx+1

if __name__ == "__main__":
    print Solution().permutationIndexII([1, 4, 2, 2])
