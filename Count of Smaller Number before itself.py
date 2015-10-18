"""
Give you an integer array (index from 0 to n-1, where n is the size of this array, value from 0 to 10000) . For each
element Ai in the array, count the number of element before this element Ai is smaller than it and return count number
array.

Example
For array [1,2,7,8,5], return [0,1,2,3,2]

Note
We suggest you finish problem Segment Tree Build, Segment Tree Query II and Count of Smaller Number before itself I
first.
"""
__author__ = 'Daniel'


class Node(object):
    def __init__(self, val):
        """Records the left subtree size"""
        self.val = val
        self.cnt_left = 0
        self.cnt_this = 0
        self.left, self.right = None, None

    def __repr__(self):
        return repr(self.val)


class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, root, val):
        """
        :return: subtree's root after insertion
        """
        if not root:
            root = Node(val)

        if root.val == val:
            root.cnt_this += 1
        elif val < root.val:
            root.cnt_left += 1
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        return root

    def rank(self, root, val):
        """
        Rank in the root's subtree
        :return: number of items smaller than val
        """
        if not root:
            return 0
        if root.val < val:
            return root.cnt_this+root.cnt_left+self.rank(root.right, val)
        elif root.val == val:
            return root.cnt_left
        else:
            return self.rank(root.left, val)


class Solution(object):
    def countOfSmallerNumberII(self, A):
        """
        TLE in python but the same algorithm in java passed the test cases. 

        :param A: A list of integer
        :return: Count the number of element before this element 'ai' is smaller than it and return count number list
        """
        tree = BST()
        ret = []
        for a in A:
            tree.root = tree.insert(tree.root, a)
            ret.append(tree.rank(tree.root, a))

        return ret


if __name__ == "__main__":
    assert Solution().countOfSmallerNumberII(
        [26, 78, 27, 100, 33, 67, 90, 23, 66, 5, 38, 7, 35, 23, 52, 22, 83, 51, 98, 69, 81, 32, 78, 28, 94, 13, 2, 97,
         3, 76, 99, 51, 9, 21, 84, 66, 65, 36, 100, 41]) == [0, 1, 1, 3, 2, 3, 5, 0, 4, 0, 5, 1, 6, 2, 9, 2, 14, 10, 17,
                                                             14, 16, 7, 16, 7, 22, 2, 0, 25, 1, 20, 29, 15, 4, 6, 28,
                                                             20, 20, 16, 37, 18]
