"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.
"""
__author__ = 'Daniel'


class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ret = []
        self.backtrack(s, [], ret)
        return ret

    def backtrack(self, s, cur_lvl, ret):
        """
        Expand the search tree horizontally.
        i be the scanning index
        If s[:i] is palindrome, then palindrome partition the s[i:]

        :param s: the current temp string
        :param cur_lvl: the current temp result at current level
        :param ret: result
        :return:
        """
        if not s:
            ret.append(list(cur_lvl))

        for i in xrange(1, len(s)+1):
            if self.predicate(s[:i]):
                cur_lvl.append(s[:i])
                self.backtrack(s[i:], cur_lvl, ret)
                cur_lvl.pop()

    def predicate(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    assert Solution().partition("aabbc") == [['a', 'a', 'b', 'b', 'c'], ['a', 'a', 'bb', 'c'], ['aa', 'b', 'b', 'c'], ['aa', 'bb', 'c']]