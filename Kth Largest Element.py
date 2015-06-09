"""
Find K-th largest element in an array.
Note

You can swap elements in the array
Example

In array [9,3,2,4,8], the 3th largest element is 4
Challenge

O(n) time, O(1) space
"""
__author__ = 'Danyang'


class Solution:
    def kthLargestElement(self, k, A):
        """
        partial quick sort

        :param k: int
        :param A: lst
        :return: int
        """
        k = len(A)-k
        return self.find_kth(A, 0, len(A), k)

    def find_kth(self, A, i, j, k):
        p = self.pivot(A, i, j)
        if k == p:
            return A[p]
        elif k < p:
            return self.find_kth(A, i, p, k)
        else:
            return self.find_kth(A, p+1, j, k)

    def pivot(self, A, i, j):
        p = i
        closed = p
        for ptr in xrange(i, j):
            if A[ptr] < A[p]:
                closed += 1
                A[closed], A[ptr] = A[ptr], A[closed]

        A[closed], A[p] = A[p], A[closed]
        return closed

if __name__ == "__main__":
    assert Solution().kthLargestElement(10, range(1, 11)) == 1

