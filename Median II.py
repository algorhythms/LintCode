"""
Numbers keep coming, return the median of numbers at every time a new number added.

Example
For numbers coming list: [1, 2, 3, 4, 5], return [1, 1, 2, 2, 3]

For numbers coming list: [4, 5, 1, 3, 2, 6, 0], return [4, 4, 4, 3, 3, 3, 3]

For numbers coming list: [2, 20, 100], return [2, 2, 20]

Challenge
O(nlogn) time

Clarification
What's the definition of Median?

Median is the number that in the middle of a sorted array. If there are n numbers in a sorted array A, the median is
A[(n-1)/2].
For example, if A=[1,2,3], median is 2. If A=[1,19], median is 1.
"""
__author__ = 'Danyang'
import heapq


class DualHeap(object):
    def __init__(self):
        """
        Dual Heap is great in the case where there is no removal.

        :return:
        """
        self.min_h = []
        self.max_h = []

    def insert(self, num):
        if not self.min_h or num > self.min_h[0]:
            heapq.heappush(self.min_h, num)
        else:
            heapq.heappush(self.max_h, -num)
        self.balance()

    def balance(self):
        l1 = len(self.min_h)
        l2 = len(self.max_h)
        if l1-l2 > 1:
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))
            self.balance()
        elif l2-l1 > 1:
            heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
            self.balance()
        return

    def get_median(self):
        l1 = len(self.min_h)
        l2 = len(self.max_h)
        m = (l1+l2-1)/2
        if m == l2-1:
            return -self.max_h[0]
        elif m == l2:
            return self.min_h[0]
        raise Exception("not balanced")


class Solution:
    def medianII(self, nums):
        """

        :param nums: A list of integers.
        :return: The median of numbers
        """
        dh = DualHeap()
        ret = []
        for num in nums:
            dh.insert(num)
            ret.append(dh.get_median())
        return ret

if __name__=="__main__":
    assert Solution().medianII([4, 5, 1, 3, 2, 6, 0]) == [4, 4, 4, 3, 3, 3, 3]


