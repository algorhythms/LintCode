"""
Given a binary search tree  and a new tree node, insert the node into the tree. You should keep the tree still be a
valid binary search tree.

Example
Given binary search tree as follow:

     2

  /    \

1        4

         /

       3

after Insert node 6, the tree should be:

     2

  /    \

1        4

         /   \

       3        6

Challenge
Do it without recursion
"""
__author__ = 'Danyang'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def insertNode(self, root, node):
        """
        Insertion without balance should be straightforward

        :param root: The root of the binary search tree.
        :param node: insert this node into the binary search tree.
        :return: The root of the new binary search tree.
        """
        cur = root
        if not root:
            root = node
            return root

        while cur:
            if cur.val == node.val:
                return root
            elif cur.val > node.val:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = node
                    return root
            else:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = node
                    return root


