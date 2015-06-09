"""
Given a unsorted array with integers, find the median of it.

A median is the middle number of the array after it is sorted.

If there are even numbers in the array, return the N/2-th number after sorted.

Example
Given [4, 5, 1, 2, 3], return 3

Given [7, 9, 4, 5], return 5

Challenge
O(n) time.
"""
__author__ = 'Danyang'


class Solution:
    def median(self, nums):
        """
        O(n), to find k-th number
        partial quick sort

        :param nums: A list of integers.
        :return: An integer denotes the middle number of the array.
        """
        n = len(nums)
        return self.find_kth(nums, 0, n, (n-1)/2)

    def find_kth(self, A, i, j, k):
        p = self.pivot(A, i, j)
        if k == p:
            return A[p]
        elif k > p:
            return self.find_kth(A, p+1, j, k)
        else:
            return self.find_kth(A, i, p, k)

    def pivot(self, A, i, j):
        """
        Fix the pivot as the 1st element
        In the end, move the pivot to the end of closed set but still inside the closed set, in order to bisect

        pivoting algorithm:
        p | closed set | open set |
        | closed set p | open set |
        """
        p = i
        closed = p
        for ptr in xrange(i, j):
            if A[ptr] < A[p]:
                closed += 1
                A[ptr], A[closed] = A[closed], A[ptr]

        A[closed], A[p] = A[p], A[closed]
        return closed


if __name__ == "__main__":
    assert Solution().median([4, 5, 1, 2, 3]) == 3
    assert Solution().median([7, 9, 4, 5]) == 5
