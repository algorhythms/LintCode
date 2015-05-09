"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example
Given [1, 20, 23, 4, 8], the largest formed number is 8423201.
"""
__author__ = 'Daniel'


class Solution:
    def largestNumber(self, num):
        """
        Compare digit by digit

        :param num: A list of non negative integers
        :return: A string
        """
        num.sort(cmp=self.cmp, reverse=True)
        ret = "".join(map(str, num))
        ret = ret.lstrip("0")
        if not ret:
            return "0"
        return ret

    def cmp(self, a, b):
        a = str(a)
        b = str(b)

        pre = int(a[0])
        while len(a)>0 and len(b)>0:
            if a[0]!=b[0]:
                return int(a[0])-int(b[0])

            pre = int(a[0])
            a = a[1:]
            b = b[1:]

        if len(a)>0:
            return int(a[0])-pre
        if len(b)>0:
            return -(int(b[0])-pre)

        return 0

if __name__=="__main__":
    assert Solution().largestNumber([0, 0])=="0"
    assert Solution().largestNumber([1, 20, 23, 4, 8])=="8423201"