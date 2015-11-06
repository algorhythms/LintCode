"""
Given an array of strings, return all groups of strings that are anagrams.

Example
Given ["lint", "intl", "inlt", "code"], return ["lint", "inlt", "intl"].

Given ["ab", "ba", "cd", "dc", "e"], return ["ab", "ba", "cd", "dc"].

Note
All inputs will be in lower-case
"""
from collections import defaultdict
__author__ = 'Daniel'


class Solution(object):
    def anagrams(self, strs):
        ret = []
        cnt = defaultdict(int)
        for s in strs:
            enc = self.encode(s)
            cnt[enc] += 1

        for s in strs:
            enc = self.encode(s)
            if cnt[enc] > 1:
                ret.append(s)

        return ret

    def encode(self, s):
        ret = [0 for _ in xrange(26)]
        for c in s:
            ret[ord(c)-ord('a')] += 1

        return "".join(map(str, ret))