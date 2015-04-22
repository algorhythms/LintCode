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
        """
        2's complement
        32-bit
        :param n:
        :return:
        """
        """
        :param n:
        :return:
        """
        a = abs(n)
        lst = []
        while a>0:
            lst.append(a%2)
            a /= 2

        # 2's complement
        if n>=0:
            lst.extend([0]*(32-len(lst)))
        else:
            pivot = -1
            for i in xrange(len(lst)):
                if pivot==-1 and lst[i]==1:
                    pivot = i
                    continue
                if pivot!=-1:
                    lst[i] ^= 1

            lst.extend([1]*(32-len(lst)))

        return "".join(map(str, reversed(lst)))

if __name__=="__main__":
    assert Solution().bitSwapRequired(1, -1)==31
    assert Solution().bitSwapRequired(31, 14)==2

