"""
Given n pieces of wood with length L[i] (integer array). Cut them into small pieces to guarantee you could have equal or
more than k pieces with the same length. What is the longest length you can get from the n pieces of wood? Given L & k,
return the maximum length of the small pieces.

Have you met this question in a real interview? Yes
Example
For L=[232, 124, 456], k=7, return 114.

Note
You couldn't cut wood into float length.

Challenge
O(n log Len), where Len is the longest length of the wood.
"""
__author__ = 'Daniel'


class Solution:
    def woodCut(self, L, k):
        """

        :param L: Given n pieces of wood with length L[i]
        :param k: An integer
        :return: The maximum length of the small pieces.
        """
        if not L:
            return 0
        maxa = max(L)
        lo = 0
        hi = maxa+1
        while lo < hi:
            m = (lo+hi)/2
            if m == 0:
                return m
            cnt = 0
            for l in L:
                cnt += l/m
            if cnt >= k:
                lo = m+1
            else:
                hi = m

        return lo-1


if __name__ == "__main__":
    assert Solution().woodCut([2147483644, 2147483645, 2147483646, 2147483647], 4) == 2147483644