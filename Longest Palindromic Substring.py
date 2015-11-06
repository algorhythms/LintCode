"""
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000,
and there exists one unique longest palindromic substring.

Example
Given the string = "abcdzdcab", return "cdzdc".

Challenge
O(n^2) time is acceptable. Can you do it in O(n) time.
"""
__author__ = 'Daniel'


class Solution:
    def longestPalindrome(self, s):
        """
        O(n) Manacer's algorithm
        :param s:
        :return:
        """
