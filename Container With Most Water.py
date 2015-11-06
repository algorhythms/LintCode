"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are
drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a
container, such that the container contains the most water.

Example
Given [1,3,2], the max area of the container is 2.

Note
You may not slant the container.
"""
__author__ = 'Daniel'


class Solution(object):
    def maxArea(self, H):
        maxa = 0
        s = 0
        e = len(H) - 1
        while s < e:
            maxa = max(maxa, min(H[s], H[e])*(e-s))
            if H[s] < H[e]:
                s += 1
            else:
                e -= 1

        return maxa


