"""
Given two array of integers(the first array is array A, the second array is array B), now we are going to find a element
 in array A which is A[i], and another element in array B which is B[j], so that the difference between A[i] and B[j]
 (|A[i] - B[j]|) is as small as possible, return their smallest difference.
"""
__author__ = 'Daniel'
import sys


class Solution:
    def smallestDifference(self, A, B):
        """
        O(n lg n)
        Binary search
        :param A: list[int]
        :param B: list[int]
        :return: int
        """
        A.sort()
        B.sort()
        ret = sys.maxint
        for a in A:
            idx = self.bin_search(a, B)
            ret = min(ret, abs(a-B[idx]))
            if idx+1<len(B):
                ret = min(ret, abs(a-B[idx+1]))

        return ret

    def bin_search(self, t, A):
        """
        search the element equal or just smaller than t
        :param t:
        :param A:
        :return: index
        """
        l = 0
        u = len(A)
        while l<u:
            m = (l+u)/2
            if A[m]==t:
                return m
            elif A[m]>t:
                u = m
            else:
                l = m+1  # if A[m]<t, l = m+1. The A[m-1] may be the one just smaller than t

        return l-1


if __name__=="__main__":
    print Solution().smallestDifference([3, 4, 6, 7], [2, 3, 8, 9])