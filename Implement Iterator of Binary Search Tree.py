"""
Design an iterator over a binary search tree with the following properties:
Elements are visited in ascending order (i.e. an inorder traversal)
next() and hasNext() queries run in O(1) time in average.
Example
For the following binary search tree, inorder traversal by using iterator is [1, 6, 10, 11, 12]

      10

    /     \

 1          11

    \           \

       6           12



Challenge
Extra memory usage O(h), h is the height of the tree.
Super Star: Extra memory usage O(1)
"""
__author__ = 'Danyang'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def __init__(self, root):
        """
        O(h) memory
        memory usage 2h


        :param root:
        :return:
        """
        self.stk = []
        self.cur = root

    def hasNext(self):
        """

        :return: True if there has next node, or False
        """
        return self.cur or self.stk

    def next(self):
        """
        In-order traversal: 1 stack
        reference:
        https://github.com/zhangdanyangg/LeetCode/blob/master/095%20Binary%20Tree%20Inorder%20Traversal.py

        :return: next node
        """
        if not self.hasNext():
            return None

        while self.cur:
            self.stk.append(self.cur)
            self.cur = self.cur.left

        node = self.stk.pop()  # left_most
        self.cur = node.right
        return node