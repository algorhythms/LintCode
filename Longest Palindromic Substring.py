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

        O(n^2) dp
        :param s:
        :return:
        """
        n = len(s)
        pa = [[False for _ in xrange(n+1)] for _ in xrange(n)]
        for i in xrange(n):
            pa[i][i] = True
            pa[i][i+1] = True

        maxa = (0, 1)
        for i in xrange(n-2, -1, -1):
            for j in xrange(i+2, n+1):
                pa[i][j] = pa[i+1][j-1] and s[i] == s[j-1]
                if pa[i][j] and j-i > maxa[1]-maxa[0]:
                    maxa = (i, j)

        return s[maxa[0]:maxa[1]]


if __name__ == "__main__":
    assert Solution().longestPalindrome("abcdzdcab") == "cdzdc"
