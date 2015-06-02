"""
Given n x m non-negative integers representing an elevation map 2d where the area of each cell is 1 x 1, compute how
much water it is able to trap after raining.

Example
Given 5*4 matrix

[12,13,0,12]
[13,4,13,12]
[13,8,10,12]
[12,13,12,12]
[13,13,13,13]
return 14.
"""
__author__ = 'Daniel'
import heapq


class Cell:
    def __init__(self, i, j, h):
        self.i = i
        self.j = j
        self.h = h

    def __cmp__(self, other):
        return self.h - other.h


class Solution:
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.trapped = 0
        self.h = []

    def trapRainWater(self, heights):
        """
        Find the min height with no water that higher than the current height and keep it.
        Starting from the min height with no water

        Do BFS with heap (similar to Dijkstra's algorithm)

        Python TLE

        :param heights: a matrix of integers
        :return: an integer
        """
        m = len(heights)
        n = len(heights[0])

        visited = [[False for _ in xrange(n)] for _ in xrange(m)]

        # add cells at the four edges
        for i in xrange(m):
            heapq.heappush(self.h, Cell(i, 0, heights[i][0]))
            heapq.heappush(self.h, Cell(i, n-1, heights[i][n-1]))

        for j in xrange(1, n-1):
            heapq.heappush(self.h, Cell(0, j, heights[0][j]))
            heapq.heappush(self.h, Cell(m-1, j, heights[m-1][j]))

        # BFS with heap
        while self.h:
            cur = heapq.heappop(self.h)
            visited[cur.i][cur.j] = True
            for dir in self.dirs:
                next_i = cur.i+dir[0]
                next_j = cur.j+dir[1]
                if 0 <= next_i < m and 0 <= next_j < n:
                    nex = Cell(next_i, next_j, heights[next_i][next_j])
                    if not visited[nex.i][nex.j]:
                        visited[nex.i][nex.j] = True  # additional, to avoid TLE
                        if nex.h < cur.h:  # fill
                            self.trapped += cur.h-nex.h
                            nex.h = cur.h
                        heapq.heappush(self.h, nex)

        return self.trapped

if __name__ == "__main__":
    assert Solution().trapRainWater([
        [12, 13, 0, 12],
        [13, 4, 13, 12],
        [13, 8, 10, 12],
        [12, 13, 12, 12],
        [13, 13, 13, 13]]
    ) == 14
    assert Solution().trapRainWater([[9, 1, 10, 10], [9, 1, 2, 8], [2, 6, 5, 0], [6, 0, 9, 0]]) == 0