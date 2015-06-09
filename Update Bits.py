"""
Given two 32-bit numbers, N and M, and two bit positions, i and j. Write a method to set all bits between i and j in N
equal to M (e g , M becomes a substring of N located at i and starting at j)

Example
Given N=(10000000000)2, M=(10101)2, i=2, j=6

return N=(10001010100)2
"""
__author__ = 'Danyang'


class Solution:
    def updateBits(self, n, m, i, j):
        """
        Notice the operator precedence
        2's complement in Python

        :param n, m: Two integer
        :param i, j: Two bit positions, indexes
        :return: An integer
        """
        mask = ((1<<32)-1)-((1<<j+1)-1)+((1<<i)-1)
        ret = (n&mask)+(m<<i)
        return self.twos_comp(ret, 32)

    @staticmethod
    def twos_comp(val, bits):
        """
        compute the 2's compliment of positive int value val
        """
        if val > 0 and val&(1<<(bits-1)) != 0:  # not ==1
            val -= 1<<bits
        return val


if __name__ == "__main__":
    assert Solution().updateBits(-2147483648, 2147483647, 0, 30) == -1
    assert Solution().updateBits(1, -1, 0, 31) == -1
    n = int("10000000000", 2)
    m = int("10101", 2)
    assert bin(Solution().updateBits(n, m, 2, 6)) == "0b10001010100"

