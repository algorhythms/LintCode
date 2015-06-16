"""
For an integer array (index from 0 to n-1, where n is the size of this array), in the corresponding SegmentTree, each
node stores an extra attribute max to denote the maximum number in the interval of the array (index from start to end).

Design a query method with three parameters root, start and end, find the maximum number in the interval [start, end] by
the given root of segment tree.
"""
__author__ = 'Danyang'
import sys


class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution:
    def query(self, root, start, end):
        """

        :param root, start, end: The root of segment tree and an segment / interval
        :return: The maximum number in the interval [start, end]
        """

        if start <= root.start and end >= root.end:  # the start and end remain unchanged during the query.
            return root.max
        if start > end:
            return -sys.maxint-1

        maxa = -sys.maxint-1
        if root.left:
            left = self.query(root.left, start, end)
            maxa = max(maxa, left)
        if root.right:
            right = self.query(root.right, start, end)
            maxa = max(maxa, right)

        return maxa

