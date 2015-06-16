"""
Given an integer array (index from 0 to n-1, where n is the size of this array), and an query list. Each query has two
integers [start, end]. For each query, calculate the sum number between index start and end in the given array, return
the result list.

Have you met this question in a real interview? Yes
Example
For array [1,2,7,8,5], and queries [(1,2),(0,4),(2,4)], return [9,23,20]

Note
We suggest you finish problem Segment Tree Build, Segment Tree Query and Segment Tree Modify first.

Challenge
O(logN) time for each query
"""
__author__ = 'Daniel'


class SumSegmentTreeNode(object):
    def __init__(self, start, end, s):
        self.start, self.end, self.s = start, end, s
        self.left, self.right = None, None


class SumSegmentTree(object):
    def __init__(self, A):
        self.A = A
        self.root = self.build_tree(0, len(self.A))

    def build_tree(self, s, e):
        """
        segment: [s, e)
        """
        if s >= e:
            return None

        if s+1 == e:
            return SumSegmentTreeNode(s, e, self.A[s])

        left = self.build_tree(s, (s+e)/2)
        right = self.build_tree((s+e)/2, e)
        sm = 0
        if left: sm += left.s
        if right: sm += right.s
        root = SumSegmentTreeNode(s, e, sm)
        root.left = left
        root.right = right

        return root

    def query(self, root, s, e):
        if not root:
            return 0

        if s <= root.start and e >= root.end:
            return root.s

        if s >= root.end or e <= root.start:
            return 0

        l = self.query(root.left, s, e)
        r = self.query(root.right, s, e)
        return l+r


class Solution:
    def intervalSum(self, A, queries):
        """
        Interval Tree

        Alternative method: dp
        :param A: integer array
        :param queries: The ith query is [queries[i-1].start, queries[i-1].end]
        :return: The result list
        """
        ret = []
        tree = SumSegmentTree(A)
        for q in queries:
            ret.append(tree.query(tree.root, q.start, q.end+1))

        return ret


