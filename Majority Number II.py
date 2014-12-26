"""
Given an array of integers, the majority number is the number that occurs more than 1/3 of the size of the array.

Find it.

Note
There is only one majority number in the array

Example
For [1, 2, 1, 2, 1, 3, 3] return 1

Challenge
O(n) time and O(1) space
"""
__author__ = 'Danyang'
class Solution:
    def majorityNumber(self, nums):
        """
        Voting Algorithm

        reference: http://www.cnblogs.com/yuzhangcmu/p/4175779.html

        :param nums:
        :return:
        """
        n1 = None
        n2 = None
        cnt1 = 0
        cnt2 = 0

        for num in nums:
            if cnt1==0:
                n1 = num
                cnt1 += 1
            elif num!=n1 and cnt2==0:
                n2 = num
                cnt2 += 1

            elif num==n1:
                cnt1 += 1
            elif num==n2:
                cnt2 += 1
            else:  # every time --, discard 3 different numbers
                assert cnt1>0
                assert cnt2>0
                cnt1 -= 1
                cnt2 -= 1

            # again
            if cnt1==0:
                n1 = num
                cnt1 += 1
            elif num!=n1 and cnt2==0:
                n2 = num
                cnt2 += 1


        # double check
        if len(filter(lambda x: x==n1, nums))>len(nums)/3:
            return n1
        else:
            return n2


if __name__=="__main__":
    assert Solution().majorityNumber([169,43,133,93,60,29,60,104,26,60,38,52,60,118,45,183,49,42,60,0,66,67,194,127,60,60,60,60,60,60])==60