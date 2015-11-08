"""
Given an integer array with no duplicates. A max tree building on this array is defined as follow:

The root is the maximum number in the array
The left subtree and right subtree are the max trees of the subarray divided by the root number.
Construct the max tree by the given array.
Example
Given [2, 5, 6, 0, 3, 1], the max tree is

              6

            /    \

         5       3

       /        /   \

     2        0     1


Challenge
O(n) time complexity
"""
__author__ = 'Danyang'


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution(object):
    def maxTree(self, A):
        """
        Cartesian Tree, Heap-ordered, treap, stack O(n)
        http://en.wikipedia.org/wiki/Cartesian_tree

        using stack
        1. construct left tree and maintain the Cartesian tree
        2. connect right tree
        O(n) since each node on the tree is pushed and popped out from stack once 


        :param A: Given an integer array with no duplicates.
        :return: The root of max tree.
        """
        stk = []
        for a in A:
            cur = TreeNode(a)
            while stk and stk[-1].val <= cur.val:
                pre = stk.pop()
                pre.right = cur.left
                cur.left = pre

            stk.append(cur)

        pre = None
        while stk:
            cur = stk.pop()
            cur.right = pre
            pre = cur

        return pre
