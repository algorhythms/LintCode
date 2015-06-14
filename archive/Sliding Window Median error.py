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
__author__ = 'Daniel'
from collections import defaultdict


class Heap(object):
    def __init__(self, A):
        """
        min-heap with set() to mimic multi-set
        index refers to index for self._A
        position refers to index for self._h
        """
        self._A = A  # the original array
        self._h = []  # store the index
        self._pos = defaultdict(set)  # val -> set(pos)

    def _pos2pos_set(self, ind):
        return self._pos[self._A[self._h[ind]]]

    def _swap_heap_node(self, i, j):
        if self._cmp_by_pos(i, j) == 0:
            return

        self._pos2pos_set(i).remove(i)
        self._pos2pos_set(j).remove(j)
        self._pos2pos_set(i).add(j)
        self._pos2pos_set(j).add(i)
        self._h[i], self._h[j] = self._h[j], self._h[i]

    def _pi(self, pos):
        """
        get the parent
        left = 2*pi + 1
        right = 2*pi + 2
        :param pos:
        :return:
        """
        if pos%2 == 0:
            return max(0, pos/2-1)
        else:
            return pos/2

    def push(self, i):
        pos = len(self._h)
        self._h.append(i)
        self._pos[self._A[i]].add(pos)

        pi = self._pi(pos)
        while pi != pos and self._cmp_by_pos(pos, pi) < 0:
            self._swap_heap_node(pi, pos)

            pos = pi
            pi = self._pi(pos)

    def _val2pos(self, val):
        return next(iter(self._pos[val]))

    def _pos2val(self, pos):
        return self._A[self._h[pos]]

    def _cmp_by_pos(self, i, j):
        return self._pos2val(i) - self._pos2val(j)

    def remove(self, i):
        try:
            pos = self._val2pos(self._A[i])
            self.pop(pos)
        except StopIteration:
            # TODO
            pass

    def _heappush(self, pos):
        """
        Swap to the target position and push down

        :param pos: the index of self._h
        :return:
        """
        n = len(self._h)
        if pos >= n:
            return

        l = 2*pos+1
        r = 2*pos+2
        mini = pos
        if l < n and self._cmp_by_pos(l, mini) < 0:
            mini = l
        if r < n and self._cmp_by_pos(r, mini) < 0:
            mini = r
        if pos != mini:
            self._swap_heap_node(pos, mini)
            self._heappush(mini)

    def peek(self):
        return self._h[0]

    def pop(self, pos=0):
        # swap head and last
        last_pos = len(self._h)-1
        self._swap_heap_node(pos, last_pos)

        # pop out head
        self._pos2pos_set(last_pos).remove(last_pos)
        head = self._h.pop()

        # rebalance
        self._heappush(pos)
        return head

    def __len__(self):
        return len(self._h)

    def __repr__(self):
        return repr(map(lambda x: self._A[x], self._h))


class DualHeap(object):
    def __init__(self, A):
        self._A = A
        self.min_h = Heap(A)  # represent right side
        self.max_h = Heap(map(lambda x: -x, A))  # represent left side

    def _rebalance(self):
        r = len(self.min_h)
        l = len(self.max_h)
        if abs(l-r) <= 1:
            return

        if r > l:
            self.max_h.push(self.min_h.pop())
        else:
            self.min_h.push(self.max_h.pop())

        self._rebalance()

    def add(self, i):
        if len(self.min_h) > 0 and self._A[i] > self._A[self.min_h.peek()]:
            self.min_h.push(i)
        else:
            self.max_h.push(i)

        self._rebalance()

    def remove(self, i):
        if len(self.min_h) > 0 and self._A[i] >= self._A[self.min_h.peek()]:
            self.min_h.remove(i)
        else:
            self.max_h.remove(i)

        self._rebalance()

    def median(self):
        r = len(self.min_h)
        l = len(self.max_h)
        if r > l:
            return self._A[self.min_h.peek()]
        else:
            return self._A[self.max_h.peek()]

    def __repr__(self):
        return repr(self.max_h)+repr(self.min_h)


class Solution:
    def medianSlidingWindow(self, nums, k):
        """
        Use heap

        TLE
        """
        if len(nums) < 1:
            return []

        ret = []
        dh = DualHeap(nums)
        for i in xrange(k):
            dh.add(i)
        ret.append(dh.median())

        for i in xrange(k, len(nums)):
            dh.remove(i-k)
            dh.add(i)
            ret.append(dh.median())

        return ret


if __name__ == "__main__":
    assert Solution().medianSlidingWindow([1, 1, 1, 1], 3) == [1, 1]
    assert Solution().medianSlidingWindow([1, 2, 7, 8, 5], 3) == [2, 7, 7]