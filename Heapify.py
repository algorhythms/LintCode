"""
Given an integer array, heapify it into a min-heap array.
For a heap array A, A[0] is the root of heap, and for each A[i], A[i * 2 + 1] is the left child of A[i] and A[i * 2 + 2]
is the right child of A[i].
Example
Given [3,2,1,4,5], return [1,2,3,4,5] or any legal heap array.

Challenge
O(n) time complexity
"""
__author__ = 'Danyang'


class Solution:
    def heapify(self, A):
        """
        CLRS

        Min-heap generally is more common

        Heapify got multiple heappush
        Bottom up construction
        * Every leaf in heap is already a heap

        Strictly O(n) rather than O(nlg n) CLRS 6.3 building a heap
        for understanding: http://www.zhihu.com/question/20729324

        :param A: Given an integer array
        :return:
        """
        n = len(A)
        for i in xrange(n/2, -1, -1):
            self.heappush(A, i)

    def heappush(self, A, i):
        """
        heappush: heap push down

        Swap to the target position and push down

        T(n) = T(2n/3)+O(1)

        :param A: the array
        :param i: the index
        :return:
        """
        n = len(A)
        if i >= n:
            return

        l = 2*i+1
        r = 2*i+2
        mini = i
        if l < n and A[l] < A[mini]:
            mini = l
        if r < n and A[r] < A[mini]:
            mini = r
        if i != mini:
            A[i], A[mini] = A[mini], A[i]
            swapped = mini
            self.heappush(A, swapped)

    def heapify_error(self, A, i=0):
        """
        Erroneous solution

        :param A: Given an integer array
        :return:
        """
        n = len(A)
        if i >= n:
            return

        l = 2*i+1
        r = 2*i+2
        mini = i
        if l < n and A[l] < A[mini]:
            mini = l
        if r < n and A[r] < A[mini]:
            mini = r
        A[i], A[mini] = A[mini], A[i]
        self.heapify_error(A, l)
        self.heapify_error(A, r)


if __name__ == "__main__":
    A = [45, 39, 32, 11]
    Solution().heapify(A)
    assert A == [11, 39, 32, 45]
