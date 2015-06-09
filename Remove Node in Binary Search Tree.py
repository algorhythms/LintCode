"""
Given a root of Binary Search Tree with unique value for each node.  Remove the node with given value. If there is no
such a node with given value in the binary search tree, do nothing. You should keep the tree still a binary search tree
after removal.
"""
__author__ = 'Danyang'


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    def removeNode(self, root, value):
        """
        BST: L<cur<=R (entire subtree)
        1. if no child, remove
        2. if one child, directly concatenate
        3. if two child, choose to substitute with left MAX and recursively delete it.

        need information regarding parent
        reference: http://www.meetqun.com/thread-3565-1-1.html

        :type root: TreeNode
        :type value: int
        :param root: The root of the binary search tree.
        :param value: Remove the node with given value.
        :return: The root of the binary search tree after removal.
        """
        return self.__removeNode(root, None, value)

    def __removeNode(self, root, parent, value):
        """
        need to keep track of the parent when deletion
        :param root:
        :param parent:
        :param value:
        :return:
        """
        if not root:
            return

        if root.val > value:
            self.__removeNode(root.left, root, value)
        elif root.val < value:
            self.__removeNode(root.right, root, value)
        else:
            if not root.left and not root.right:  # no child
                if parent:
                    if parent.left == root:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    root = None
            elif root.left and not root.right or root.right and not root.left:  # single child
                if root.left:
                    if parent:
                        if parent.left == root:
                            parent.left = root.left
                        else:
                            parent.right = root.left
                    else:  # when val at root of entire tree
                        root = root.left
                else:
                    if parent:
                        if parent.left == root:
                            parent.left = root.right
                        else:
                            parent.right = root.right
                    else:  # when val at root of entire tree
                        root = root.right
            else:  # two children
                cur = root.left
                while cur.right:
                    cur = cur.right
                root.val = cur.val
                # go down again
                self.__removeNode(root.left, root, cur.val)

        return root