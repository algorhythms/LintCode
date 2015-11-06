"""
Given two values k1 and k2 (where k1 < k2) and a root pointer to a Binary Search Tree. Find all the keys of tree in
range k1 to k2. i.e. print all x such that k1<=x<=k2 and x is a key of given BST. Return all the keys in ascending
order.

Example
If k1 = 10 and k2 = 22, then your function should return [12, 20, 22].

    20
   /  \
  8   22
 / \
4   12
"""
__author__ = 'Daniel'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution(object):
    def searchRange(self, root, k1, k2):
        ret = []
        self.dfs(root, k1, k2, ret)
        return ret

    def dfs(self, root, k1, k2, ret):
        if not root:
            return

        if root.val < k1:
            self.dfs(root.right, k1, k2, ret)
        elif root.val > k2:
            self.dfs(root.left, k1, k2, ret)
        else:
            self.dfs(root.left, k1, k2, ret)
            ret.append(root.val)
            self.dfs(root.right, k1, k2, ret)