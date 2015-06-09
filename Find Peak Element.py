"""
There is an integer array which has the following features:

    * The numbers in adjacent positions are different.

    * A[0] < A[1] && A[A.length - 2] > A[A.length - 1].

We define a position P is a peek if A[P] > A[P-1] && A[P] > A[P+1].

Find a peak in this array. Return the index of the peak.

Note
The array may contains multiple peeks, find any of them.

Example
[1, 2, 1, 3, 4, 5, 7, 6]

return index 1 (which is number 2)  or 6 (which is number 7)

Challenge
Time complexity O(logN)
"""
__author__ = 'Danyang'


class Solution:
    def findPeak(self, A):
        """
        Binary search
        Microsoft Interview, Oct 2014

        To reduce the complexity of dealing the edge cases:
        * add two anti-peak dummies on the both ends

        :param A: An integers list. A[0] and A[-1] are dummies.
        :return: return any of peek positions.
        """
        n = len(A)
        l = 0
        h = n
        while l < h:
            m = (l+h)/2
            if A[m-1] < A[m] > A[m+1]:
                return m
            elif A[m+1] > A[m]:
                l = m+1
            else:
                h = m

        raise Exception  # will not raise if there are DUMMIES at the both ends.


if __name__ == "__main__":
    assert Solution().findPeak([1, 2, 1, 3, 4, 5, 7, 6]) in (1, 6)

