"""
Hard Interval Minimum Number

Given an integer array (index from 0 to n-1, where n is the size of this array), and an query list. Each query has two
integers [start, end]. For each query, calculate the minimum number between index start and end in the given array,
return the result list.

Example
For array [1,2,7,8,5], and queries [(1,2),(0,4),(2,4)], return [2,1,5]

Note
We suggest you finish problem Segment Tree Build, Segment Tree Query and Segment Tree Modify first.

Challenge
O(logN) time for each query
"""
__author__ = 'Daniel'
import sys

DEFAULT = sys.maxint
f = lambda x, y: min(x, y)


class Node(object):
    def __init__(self, start, end, m):
        self.start, self.end, self.m = start, end, m
        self.left, self.right = None, None


class SegmentTree(object):
    def __init__(self, A):
        self.A = A
        self.root = self.build_tree(0, len(self.A))

    def build_tree(self, s, e):
        """
        segment: [s, e)
        """
        if s >= e:
            return None

        if s+1 == e:
            return Node(s, e, self.A[s])

        left = self.build_tree(s, (s+e)/2)
        right = self.build_tree((s+e)/2, e)
        val = DEFAULT
        if left: val = f(val, left.m)
        if right: val = f(val, right.m)
        root = Node(s, e, val)
        root.left = left
        root.right = right

        return root

    def query(self, root, s, e):
        """
        :type root: Node
        """
        if not root:
            return DEFAULT

        if s <= root.start and e >= root.end:
            return root.m

        if s >= root.end or e <= root.start:
            return DEFAULT

        l = self.query(root.left, s, e)
        r = self.query(root.right, s, e)
        return f(l, r)


class Solution:
    def intervalMinNumber(self, A, queries):
        """
        Interval Tree

        :param A: integer array
        :param queries: The ith query is [queries[i-1].start, queries[i-1].end]
        :return: The result list
        """
        ret = []
        tree = SegmentTree(A)
        for q in queries:
            ret.append(tree.query(tree.root, q.start, q.end+1))

        return ret