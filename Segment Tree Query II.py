"""
For an array, we can build a SegmentTree for it, each node stores an extra attribute count to denote the number of
elements in the the array which value is between interval start and end. (The array may not fully filled by elements)

Design a query method with three parameters root, start and end, find the number of elements in the in array's interval
[start, end] by the given root of value SegmentTree.

Have you met this question in a real interview? Yes
Example
For array [0, empty, 2, 3], the corresponding value Segment Tree is:

                     [0, 3, count=3]
                     /             \
          [0,1,count=1]             [2,3,count=2]
          /         \               /            \
   [0,0,count=1] [1,1,count=0] [2,2,count=1], [3,3,count=1]
query(1, 1), return 0

query(1, 2), return 1

query(2, 3), return 2

query(0, 2), return 2
"""
__author__ = 'Daniel'
DEFAULT = 0
f = lambda x, y: x+y


class Solution:
    def query(self, root, s, e):
        """
        Segment: [s, e]

        :param root: The root of segment tree
        :param start: start of segment/interval
        :param end: end of segment/interval
        :return: The count number in the interval [start, end]
        """
        if not root:
            return DEFAULT

        if s <= root.start and e >= root.end:
            return root.count

        if s > root.end or e < root.start:
            return DEFAULT

        l = self.query(root.left, s, e)
        r = self.query(root.right, s, e)
        return f(l, r)
