"""
Given a set of n nuts of different sizes and n bolts of different sizes. There is a one-one mapping between nuts and bolts. Comparison of a nut to another nut or a bolt to another bolt is not allowed. It means nut can only be compared with bolt and bolt can only be compared with nut to see which one is bigger/smaller.

We will give you a compare function to compare nut with bolt.

Example
Given nuts = ['ab','bc','dd','gg'], bolts = ['AB','GG', 'DD', 'BC'].

Your code should find the matching bolts and nuts.

one of the possible return:

nuts = ['ab','bc','dd','gg'], bolts = ['AB','BC','DD','GG'].

The order of the nuts or bolts does not matter. You just need to find the matching bolt for each nut.
"""
__author__ = 'Daniel'
try:
    from lintcode import Compare
except ImportError:
    class Compare:
        @classmethod
        def cmp(cls, a, b):
            """
            THIS IS A SAMPLE CMP FOR TESTING.

            You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
            if "a" is bigger than "b", it will return 1, else if they are equal,
            it will return 0, else if "a" is smaller than "b", it will return -1.
            When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
            :param a:
            :param b:
            :return:
            """
            a = a.lower()
            b = b.lower()

            diff = ord(a)-ord(b)
            if diff < 0:
                return -1
            elif diff > 0:
                return 1
            else:
                return 0


class Solution:
    def sortNutsAndBolts(self, nuts, bolts):
        """
        :param nuts: a list of nuts
        :param bolts: a list of bolts
        :return:
        """
        assert len(nuts) == len(bolts)
        self.quick_sort(nuts, bolts, 0, len(nuts))

    def quick_sort(self, nuts, bolts, start, end):
        """
        Quick sort over two arrays
        :param nuts:
        :param bolts:
        :param start:
        :param end:
        :return:
        """
        if start >= end:
            return

        pivot = self.partition(nuts, bolts[start], start, end)
        self.partition(bolts, nuts[pivot], start, end)
        self.quick_sort(nuts, bolts, start, pivot)
        self.quick_sort(nuts, bolts, pivot+1, end)

    def partition(self, A, pivot, start, end):
        """
        Use bolt to partition nuts/ Use nut to partition nuts
        Bolt and nut are swappable in the parameter

        In-place partition

        :param A: nuts or bolts, the counterpart of pivot
        :param pivot: bolt or nut
        :param start:
        :param end:
        :return: pivot
        """
        left = start  # save for the counterpart's pivot
        i = start+1
        while i < end:
            if Compare.cmp(A[i], pivot) == -1 or Compare.cmp(pivot, A[i]) == 1:
                left += 1
                A[left], A[i] = A[i], A[left]
                i += 1
            elif Compare.cmp(A[i], pivot) == 0 or Compare.cmp(pivot, A[i]) == 0:
                A[start], A[i] = A[i], A[start]
            else:
                i += 1

        # move the counterpart's pivot from start to left
        A[start], A[left] = A[left], A[start]

        return left


if __name__ == "__main__":
    nuts = ['a', 'b', 'd', 'g']
    bolts = ['A', 'G', 'D', 'B']
    Solution().sortNutsAndBolts(nuts, bolts)
    assert nuts == ['a', 'b', 'd', 'g']
    assert bolts == ['A', 'B', 'D', 'G']