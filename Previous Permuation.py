"""
Given a list of integers, which denote a permutation.

Find the previous permutation in ascending order.

Note
The list may contains duplicate integers.

Example
For [1,3,2,3], the previous permutation is [1,2,3,3]

For [1,2,3,4], the previous permutation is [4,3,2,1]
"""
__author__ = 'Danyang'


class Solution:
    def previousPermuation(self, num):
        """
        permutation, reverse operation of next permutation
        :param num: a list of integer
        :return: a list of integer
        """
        n = len(num)

        partition = n-2
        while partition >= 0 and num[partition] <= num[partition+1]:
            partition -= 1

        if partition < 0:
            return num[::-1]

        change = n-1
        while change >= 0 and num[change] >= num[partition]:
            change -= 1

        num[partition], num[change] = num[change], num[partition]

        # num = num[:partition+1]+num[n-1:partition:-1]
        num[partition+1:] = reversed(num[partition+1:])  # direct slice assignment
        return num


if __name__ == "__main__":
    print Solution().previousPermuation([1, 3, 2, 3])






