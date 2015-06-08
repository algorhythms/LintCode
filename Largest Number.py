"""
Given a list of non negative integers, arrange them such that they form the largest number.

Example
Given [1, 20, 23, 4, 8], the largest formed number is 8423201.
"""
__author__ = 'Daniel'


class Solution:
    def largestNumber(self, nums):
        """
        Start off by enumerate simple examples

        Compare digit by digit
        The comparator is the core.

        :type nums: list[int]
        :rtype: str
        """
        nums = map(str, nums)
        nums.sort(cmp=self.cmp, reverse=True)
        nums = "".join(nums)
        nums = nums.lstrip("0")
        if not nums:
            nums = "0"
        return nums

    def cmp(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        order = 1
        if len(a) > len(b):
            order = -1
            a, b = b, a

        for i in xrange(len(a)):
            if int(a[i]) != int(b[i]):
                return order*(int(a[i])-int(b[i]))

        if len(a) == len(b):
            return 0

        return order*self.cmp(a, b[len(a):])


if __name__ == "__main__":
    assert Solution().largestNumber([0, 0]) == "0"
    assert Solution().largestNumber([1, 20, 23, 4, 8]) == "8423201"