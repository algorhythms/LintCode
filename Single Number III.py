"""
Given 2*n + 2 numbers, every numbers occurs twice except two, find them.

Example
Given [1,2,2,3,4,4,5,3] return 1 and 5

Challenge
O(n) time, O(1) extra space.
"""
__author__ = 'Danyang'


class Solution:
    def singleNumberIII(self, A):
        """
        Bit manipulation
        If two numbers are different, \exists 1 bit set in one while unset in the other.

        To get the rightmost set bit: n&(~n+1), which is equivalent to n&-n (2's complement)

        :param A: An integer array
        :return: Two integer
        """
        bits = 0
        for a in A:
            bits ^= a

        rightmost_set_bit = bits&-bits

        bits1 = 0
        bits2 = 0
        for a in A:
            if a&rightmost_set_bit:
                bits1 ^= a
            else:
                bits2 ^= a

        return bits1, bits2


