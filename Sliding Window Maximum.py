"""
Given an array of n integer with duplicate number, and a moving window(size k), move the window at each iteration from
the start of the array, find the maximum number inside the window at each moving.

Example
For array [1, 2, 7, 7, 8], moving window size k = 3. return [7, 7, 8]


"""
__author__ = 'Daniel'


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        Sliding window + queue
        The queue keeps only the valuable information, while useless information is deleted

        http://articles.leetcode.com/2011/01/sliding-window-maximum.html
        The more recent the index is, the more valuable the data is

        Notice:
        * Loop invariant: the queue is keeping the index of max elements TO THE RIGHT under the window
        * the queue is storing the index

        :param nums: A list of integers.
        :param k:
        :return: The maximum number inside the window at each moving.
        """
        if not nums or k == 0:
            return []

        q = []
        ret = []
        for i in xrange(k):
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            q.append(i)
        ret.append(nums[q[0]])  # init

        for i in xrange(k, len(nums)):  # starting from k for the end of window
            while q and nums[i] >= nums[q[-1]]:
                q.pop()
            while q and q[0] < i-k+1:  # plus 1
                q.pop(0)
            q.append(i)
            ret.append(nums[q[0]])

        return ret


if __name__ == "__main__":
    print Solution().maxSlidingWindow([1, 2, 7, 7, 8], 3)