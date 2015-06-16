"""
For a Maximum Segment Tree, which each node has an extra value max to store the maximum value in this node's interval.

Implement a modify function with three parameter root, index and value to change the node's value with [start, end] =
[index, index] to the new given value. Make sure after this change, every node in segment tree still has the max
attribute with the correct value.
"""
__author__ = 'Danyang'


class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None


class Solution:
    def modify(self, root, index, value):
        """
        need bottom-up update the max
        :type root: SegmentTreeNode
        :param root: The root of segment tree and
        :param index: change the node's value with [index, index] to the new given value
        :param value: the new given value
        :return: void
        """
        if root is None:
            return
        if index < root.start or index > root.end:
            return
        if root.start == index and root.end == index:
            root.max = value
            return

        # bottom up 
        self.modify(root.left, index, value)
        self.modify(root.right, index, value)

        m = value
        if root.left:
            m = max(m, root.left.max)
        if root.right:
            m = max(m, root.right.max)
        root.max = m



