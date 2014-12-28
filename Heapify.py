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
    def heapify_error(self, A, i=0):
        """

        :param A: Given an integer array
        :return:
        """
        n = len(A)
        if i>=n:
            return

        l = 2*i+1
        r = 2*i+2
        mini = i
        if l<n and A[l]<A[mini]:
            mini = l
        if r<n and A[r]<A[mini]:
            mini = r
        A[i], A[mini] = A[mini], A[i]
        self.heapify_error(A, l)
        self.heapify_error(A, r)

    def heapify(self, A):
        """
        CLRS

        every leaf in heap is already a heap

        strictly O(n) rather than O(nlg n) CLRS 6.3 Building a heap

        :param A: Given an integer array
        :return:
        """
        n = len(A)
        for i in xrange(n/2, -1, -1):
            self.heappush(A, i)

    def heappush(self, A, i):
        """
        heappush: heap push down

        :param A:
        :param i:
        :return:
        """
        n = len(A)
        if i>=n:
            return

        l = 2*i+1
        r = 2*i+2
        mini = i
        if l<n and A[l]<A[mini]:
            mini = l
        if r<n and A[r]<A[mini]:
            mini = r
        if i!=mini:
            A[i], A[mini] = A[mini], A[i]
            self.heappush(A, mini)



if __name__=="__main__":
    A = [45, 39, 32, 11]
    Solution().heapify(A)
    assert A==[11, 39, 32, 45]
