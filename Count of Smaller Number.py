"""
Give you an integer array (index from 0 to n-1, where n is the size of this array, value from 0 to 10000) and an query
list. For each query, give you an integer, return the number of element in the array that are smaller that the given
integer.

Example
For array [1,2,7,8,5], and queries [1,8,5], return [0,4,2]

Note
We suggest you finish problem Segment Tree Build and Segment Tree Query II first.

Challenge
Could you use three ways to do it.

Just loop
Sort and binary search
Build Segment Tree and Search.

"""
__author__ = 'Daniel'


class Solution:
    def countOfSmallerNumber(self, A, queries):
        # return self.loop(A, queries)
        return self.search(A, queries)

    def loop(self, A, queries):
        """
        O(N*k)
        """
        cnt = dict(zip(queries, [0 for _ in queries]))
        for elt in A:
            for k in cnt.keys():
                if elt<k:
                    cnt[k] += 1

        return [cnt[i] for i in queries]

    def search(self, A, queries):
        """
        O(nlgn + klgn)
        """
        A.sort()
        ret = []
        for q in queries:
            ind = self.bin_search(A, q)
            while ind>=0 and A[ind]==q:
                ind -= 1
            ret.append(ind+1)

        return ret

    def bin_search(self, A, t):
        b = 0
        e = len(A)
        while b<e:
            m = (b+e)/2
            if t==A[m]:
                return m
            elif t < A[m]:
                e = m
            else:
                b = m+1
        return b-1


    def segment_tree(self, A, queries):
        # TODO 
        pass