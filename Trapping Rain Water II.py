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

__author__ = 'Daniel'


class Cell:
    def __init__(self, i, j, h):
        self.i = i
        self.j = j
        self.h = h

    def __cmp__(self, other):
        return self.h - other.h


class Solution(object):
    def __init__(self):
        self.dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def trapRainWater(self, mat):
        """
        Find the min height with no water that higher than the current height and keep it.
        Starting from the min height with no water
        Do BFS with heap (similar to Dijkstra's algorithm)

        :param mat: List[List[int]]
        :return: an integer
        """
        if not mat: return 0

        m, n = len(mat), len(mat[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        h = []
        # add cells at the four edges
        for i in xrange(m):
            visited[i][0] = True
            heapq.heappush(h, Cell(i, 0, mat[i][0]))
            visited[i][n-1] = True
            heapq.heappush(h, Cell(i, n-1, mat[i][n-1]))

        for j in xrange(1, n-1):
            visited[0][j] = True
            heapq.heappush(h, Cell(0, j, mat[0][j]))
            visited[m-1][j] = True
            heapq.heappush(h, Cell(m-1, j, mat[m-1][j]))

        # BFS with heap
        trapped = 0
        while h:
            cur = heapq.heappop(h)
            for dir in self.dirs:
                I, J = cur.i+dir[0], cur.j+dir[1]
                if 0 <= I < m and 0 <= J < n and not visited[I][J]:
                    nxt = Cell(I, J, mat[I][J])
                    if nxt.h < cur.h:  # fill
                        trapped += cur.h - nxt.h
                        nxt.h = cur.h

                    visited[I][J] = True
                    heapq.heappush(h, nxt)

        return trapped

if __name__ == "__main__":
    assert Solution().trapRainWater([
        [12, 13, 0, 12],
        [13, 4, 13, 12],
        [13, 8, 10, 12],
        [12, 13, 12, 12],
        [13, 13, 13, 13]]
    ) == 14
    assert Solution().trapRainWater([[9, 1, 10, 10], [9, 1, 2, 8], [2, 6, 5, 0], [6, 0, 9, 0]]) == 0