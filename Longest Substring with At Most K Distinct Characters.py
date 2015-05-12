"""
Given a string s, find the length of the longest substring T that contains at most k distinct characters.

Example
For example, Given s = "eceba", k = 3,

T is "eceb" which its length is 4.

Challenge
O(n), n is the size of the string s.
"""
__author__ = 'Daniel'


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        Sliding window
        :param s: A string
        :param k: An integer
        :return:
        """
        if len(s)<1 or k<1:
            return 0

        cnt = {}
        b = 0
        e = 1
        cnt[s[b]] = 1
        maxa = 1
        while e<len(s):
            # next
            if s[e] not in cnt:
                cnt[s[e]] = 0
            cnt[s[e]] += 1
            e += 1

            # adjust
            while len(cnt)>k:
                cnt[s[b]] -= 1
                if cnt[s[b]]<=0:
                    del cnt[s[b]]
                b += 1

            maxa = max(maxa, e-b)

        return maxa

if __name__=="__main__":
    assert Solution().lengthOfLongestSubstringKDistinct("eceba", 3)==4
