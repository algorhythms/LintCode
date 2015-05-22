"""
Given an interval list which are flying and landing time of the flight. How many airplanes are on the sky at most?

Example
For interval list [[1,10],[2,3],[5,8],[4,7]], return 3

Note
If landing and flying happens at the same time, we consider landing should happen at first.
"""
__author__ = 'Daniel'


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    @staticmethod
    def cmp(a, b):
        """
        :type a: Interval
        :type b: Interval
        """
        if a.start != b.start:
            return a.start-b.start
        else:
            return a.end-b.end

    def countOfAirplanes(self, airplanes):
        """

        :param airplanes: a list of Interval
        :return: an integer
        """
        return self.count_heap(airplanes)

    def count_heap(self, intervals):
        """
        Heap

        :param intervals: a list of Interval
        :return: an integer
        """
        import heapq

        intervals.sort(cmp=Solution.cmp)
        heap = []
        cnt = 0
        for intv in intervals:
            # in, with upper boundary
            heapq.heappush(heap, intv.end)
            # out, by comparing lower boundary
            while heap[0] <= intv.start:
                heapq.heappop(heap)

            cnt = max(cnt, len(heap))

        return cnt


if __name__ == "__main__":
    assert Solution().countOfAirplanes([Interval(i[0], i[1]) for i in [[1, 10], [2, 3], [5, 8], [4, 7]]]) == 3