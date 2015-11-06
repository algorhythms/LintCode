"""
Given a string, find the length of the longest substring without repeating characters.

Example
For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.

Challenge
O(n) time
"""
__author__ = 'Daniel'


class Solution:
    def lengthOfLongestSubstring(self, s):
        b = 0
        e = 0
        n = len(s)
        maxa = 0
        st = set()  # window
        while e < n:
            while s[e] in st:
                st.remove(s[b])
                b += 1

            st.add(s[e])
            e += 1
            maxa = max(maxa, e-b)

        return maxa

if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3





