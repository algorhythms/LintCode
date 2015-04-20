"""
Determine the number of bits required to convert integer A to integer B

Example
Given n = 31, m = 14,return 2

(31)10=(11111)2

(14)10=(01110)2
"""
__author__ = 'Danyang'


class Solution:
    def bitSwapRequired(self, a, b):
        """

        :param a:
        :param b:
        :return: int
        """
        a = self.to_bin(a)
        b = self.to_bin(b)
        diff = len(a)-len(b)
        ret = 0
        if diff<0:
            a, b = b, a
            diff *= -1
        b = "0"*diff+b
        for i in xrange(len(b)):
            if a[i]!=b[i]:
                ret += 1

        return ret

    def to_bin(self, n):
        lst = []
        while n>0:
            lst.append(n%2)
            n /= 2
        return "".join(map(str, reversed(lst)))

if __name__=="__main__":
    assert Solution().bitSwapRequired(31, 14)==2
