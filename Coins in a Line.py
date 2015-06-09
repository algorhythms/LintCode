"""
There are n coins in a line. Two players take turns to take one or two coins from right side until there are no more
coins left. The player who take the last coin wins.

Could you please decide the first play will win or lose?

Example
n = 1, return true.
n = 2, return true.
n = 3, return false.
n = 4, return true.
n = 5, return true.

Challenge
O(1) time and O(1) memory
"""
__author__ = 'Daniel'


class Solution:
    def firstWillWin(self, n):
        """
        Starting from the easiest cases.
        Enumerate the cases and find the pattern

        :param n: an integer
        :return: a boolean which equals to True if the first player will win
        """
        return not n%3 == 0