"""
Given a (decimal - e.g. 3.72) number that is passed in as a string, return the binary representation that is passed in
as a string. If the number can not be represented accurately in binary, return ERROR

Example
For n=3.72, return ERROR

For n=3.5, return 11.1
"""
from decimal import *

__author__ = 'Danyang'


class Solution:
    def binaryRepresentation(self, n):
        """
        NOTICE: As of 14 April 2015, LintCode OJ has bug in test case 12 of this question since 0.6418459415435791
        cannot be represented as binary representation because 0.6418459415435791 becomes
        0.10100100010100000000001111111111111111111111111111111111111000...


        difficult part: determine whether the fraction can be represented in binary
        if cannot represent, repeat forever, then cut-off at 32bit as in int

        One may check whether the last digit of decimal part is 5, but it does not work for 0.12345

        :param n: Given a decimal number that is passed in as a string
        :return: A string
        """
        dec_part = ""
        if "." in n:
            int_part, dec_part = n.split(".")
            getcontext().prec = len(dec_part)+1
            dec_part = "."+dec_part
            if not self.is_representable(Decimal(dec_part)):
                return "ERROR"
        else:
            int_part = n

        a = self.natural_num_to_bin(int(int_part))
        b = self.fraction_to_bin(Decimal(dec_part))

        if a == "":
            a = "0"
        if b == "":
            return a
        else:
            return a+"."+b

    @staticmethod
    def natural_num_to_bin(n):
        """

        :type n: int
        :param n:
        :return: string representation
        """
        sb = []  # string buffer
        while n > 0:
            sb.append(n&1)
            n >>= 1

        return "".join(map(str, reversed(sb)))

    @staticmethod
    def fraction_to_bin(n):
        """
        To convert fractional part of binary representation: x2 can take the whole part.
        :type n: Decimal
        :param n:
        :return: string representation
        """
        sb = []
        while n > 0:
            if len(sb) > 32:
                return "ERROR"
            n *= Decimal(2)
            cur = int(n)
            sb.append(cur)
            n -= Decimal(cur)
        return "".join(map(str, sb))

    @staticmethod
    def is_representable(frac):
        """
        to test whether the fraction part is representable in binary

        :type frac: Decimal
        :param frac:
        :return:
        """
        while True:
            temp = str(frac).rstrip("0")
            if temp.endswith("."):
                return True
            if not temp.endswith("5"):
                return False
            frac *= Decimal(2)


if __name__ == "__main__":
    assert Solution().binaryRepresentation("0.72") == "ERROR"
    assert Solution().binaryRepresentation("0.125") == "0.001"
    assert Solution().binaryRepresentation("0.6418459415435791") == "ERROR"
