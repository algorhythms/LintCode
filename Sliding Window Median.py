"""
Given an array of n integer, and a moving window(size k), move the window at each iteration from the start of the array,
find the median of the element inside the window at each moving. (If there are even numbers in the array, return the
N/2-th number after sorting the element in the window. )

Have you met this question in a real interview? Yes
Example
For array [1,2,7,8,5], moving window size k = 3. return [2,7,7]

At first the window is at the start of the array like this

[ | 1,2,7 | ,8,5] , return the median 2;

then the window move one step forward.

[1, | 2,7,8 | ,5], return the median 7;

then the window move one step forward again.

[1,2, | 7,8,5 | ], return the median 7;

Challenge
O(nlog(n)) time


"""
from bisect import bisect_left
__author__ = 'Daniel'


class PriorityQueue(object):
    def __init__(self):
        self.lst = []

    def bisect(self, t):
        """
        you can use bisect.bisect_left module
        If t is already present in lst, the insertion point will be before (to the left of) any existing entries.
        """
        l = 0
        h = len(self.lst)
        while l < h:
            m = (l+h)/2
            if self.lst[m] < t:
                l = m+1
            else:
                h = m

        return l

    def insert(self, t):
        pos = self.bisect(t)
        self.lst.insert(pos, t)

    def remove(self, t):
        pos = self.bisect(t)
        if self.lst[pos] != t:
            raise ValueError("%s not found in the queue" % str(t))
        del self.lst[pos]

    def __getitem__(self, item):
        return self.lst[item]


class Solution:
    def medianSlidingWindow(self, nums, k):
        """

        :param nums: A list of integers.
        :param k: size of window
        :return: The median of element inside the window at each moving.
        """
        if len(nums)<1:
            return []

        pq = PriorityQueue()
        for i in xrange(k):
            pq.insert(nums[i])

        ret = []
        mid = k/2
        if k%2 == 0:
            mid -= 1

        ret.append(pq[mid])
        for i in xrange(k, len(nums)):
            pq.remove(nums[i-k])
            pq.insert(nums[i])
            ret.append(pq[mid])

        return ret


if __name__ == "__main__":
    print Solution().medianSlidingWindow([1, 2, 7, 8, 5], 3)