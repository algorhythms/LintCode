"""
Give you an integer array (index from 0 to n-1, where n is the size of this array, value from 0 to 10000) . For each
element Ai in the array, count the number of element before this element Ai is smaller than it and return count number
array.

Example
For array [1,2,7,8,5], return [0,1,2,3,2]

Note
We suggest you finish problem Segment Tree Build, Segment Tree Query II and Count of Smaller Number before itself I first.
"""
__author__ = 'Daniel'


class Node(object):
    def __init__(self, val):
        self.val = val
        self.count_left = 0
        self.count = 0
        self.left, self.right = None, None

    def __repr__(self):
        return repr(self.val)


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        if not self.root:
            self.root = Node(val)
            root = self.root

        assert root is not None

        if root.val == val:
            root.count += 1
        elif val < root.val:
            root.count_left += 1
            if not root.left: root.left = Node(val)
            self.insert(root.left, val)
        else:
            if not root.right: root.right = Node(val)
            self.insert(root.right, val)

    def query(self, root, val):
        """
        query number of items smaller than val
        """
        if not root:
            return 0
        if root.val < val:
            return root.count+root.count_left+self.query(root.right, val)
        elif root.val == val:
            return root.count_left
        else:
            return self.query(root.left, val)


class Solution:
    def countOfSmallerNumberII(self, A):
        """
        TLE

        :param A: A list of integer
        :return: Count the number of element before this element 'ai' is smaller than it and return count number list
        """
        tree = BST()
        ret = []
        for a in A:
            tree.insert(tree.root, a)
            ret.append(tree.query(tree.root, a))

        return ret


if __name__ == "__main__":
    assert Solution().countOfSmallerNumberII(
        [26, 78, 27, 100, 33, 67, 90, 23, 66, 5, 38, 7, 35, 23, 52, 22, 83, 51, 98, 69, 81, 32, 78, 28, 94, 13, 2, 97,
         3, 76, 99, 51, 9, 21, 84, 66, 65, 36, 100, 41]) == [0, 1, 1, 3, 2, 3, 5, 0, 4, 0, 5, 1, 6, 2, 9, 2, 14, 10, 17,
                                                             14, 16, 7, 16, 7, 22, 2, 0, 25, 1, 20, 29, 15, 4, 6, 28,
                                                             20, 20, 16, 37, 18]
