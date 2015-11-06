"""
Given n, generate all structurally unique BST's (binary search trees) that store values 1...n.

Have you met this question in a real interview? Yes
Example
Given n = 3, your program should return all 5 unique BST's shown below.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
__author__ = 'Daniel'


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.dfs(1, n+1)

    def dfs(self, s, e):
        ret = []
        if s >= e:
            return [None]

        for i in xrange(s, e):
            ls = self.dfs(s, i)
            rs = self.dfs(i+1, e)
            for l in ls:
                for r in rs:
                    root = TreeNode(i)
                    root.left = l
                    root.right = r
                    ret.append(root)

        return ret