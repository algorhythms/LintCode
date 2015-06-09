"""
The structure of Segment Tree is a binary tree which each node has two attributes start and end denote an segment /
interval.

start and end are both integers, they should be assigned in following rules:

The root's start and end is given by build method.
The left child of node A has start=A.left, end=(A.left + A.right) / 2.
The right child of node A has start=(A.left + A.right) / 2, end=A.right.
if start equals to end, there will be no children for this node.
Implement a build method with two parameters start and end, so that we can create a corresponding segment tree with
every node has the correct start and end value, return the root of this segment tree.
"""
__author__ = 'Danyang'


class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None


class Solution:
    def build(self, start, end):
        """

        :param start, end: denote an segment / interval
        :return: The root of Segment Tree
        """
        if start > end:
            return None

        root = SegmentTreeNode(start, end)
        if start == end:
            return root

        root.left = self.build(start, (start+end)/2)
        root.right = self.build((start+end)/2+1, end)
        return root
