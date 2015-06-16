"""
Given N buildings in a x-axis, each building is a rectangle and can be represented by a triple (start, end, height),
where start is the start position on x-axis, end is the end position on x-axis and height is the height of the building.
Buildings may overlap if you see them from far away, find the outline of them.

An outline can be represented by a triple, (start, end, height), where start is the start position on x-axis of the
outline, end is the end position on x-axis and height is the height of the outline.

Building Outline

Example
Given 3 buildings:

[
  [1, 3, 3],
  [2, 4, 4],
  [5, 6, 1]
]
The outlines are:

[
  [1, 2, 3],
  [2, 4, 4],
  [5, 6, 1]
]
Note
Please merge the adjacent outlines if they have the same height and make sure different outlines cant overlap on x-axis.
"""
__author__ = 'Daniel'
import heapq
from collections import defaultdict


class Building(object):
    def __init__(self, h):
        self.h = h
        self.deleted = False

    def __cmp__(self, other):
        # max-heap
        return other.h - self.h


class Event(object):
    def __init__(self):
        """
        Event at certain x-coordinate
        Event for the building starting and the building ending
        """
        self.starts = []
        self.ends = []


class Solution:
    def buildingOutline(self, buildings):
        """
        MLE

        :param buildings: A list of lists of integers
        :return: A list of lists of integers
        """
        events = defaultdict(Event)
        for start, end, height in buildings:
            building = Building(height)
            events[start].starts.append(building)
            events[end].ends.append(building)

        ret = []
        cur_heap = []
        cur_max_hi = 0
        begin = None
        for x, event in sorted(events.items()):
            for building in event.starts:  # beginning
                heapq.heappush(cur_heap, building)
            for building in event.ends:  # finishing
                building.deleted = True

            while cur_heap and cur_heap[0].deleted:
                heapq.heappop(cur_heap)

            new_hi = cur_heap[0].h if cur_heap else 0
            if cur_max_hi != new_hi:
                if cur_max_hi != 0:
                    ret.append([begin, x, cur_max_hi])
                begin = x

                cur_max_hi = new_hi

        return ret

if __name__ == "__main__":
    assert Solution().buildingOutline([
        [1, 3, 3],
        [2, 4, 4],
        [5, 6, 1]
    ]) == [[1, 2, 3], [2, 4, 4], [5, 6, 1]]