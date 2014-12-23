"""
Given a string which contains only letters. Sort it by lower case first and upper case second.

Note
It's not necessary to keep the original order of lower-case letters and upper case letters.

Example
For "abAcD", a reasonable answer is "acbAD"
"""
__author__ = 'Danyang'
class Solution:
    def sortLetters(self, chars):
        """

        :param chars: The letters array you should sort.
        :return: NIL, in-place
        """
        closed = -1
        for ind, val in enumerate(chars):
            if ord(val)<ord('a'):  # ASCII A-Za-z
                continue
            else:
                closed += 1
                chars[ind], chars[closed] = chars[closed], chars[ind]


if __name__=="__main__":
    chars = list("abAcD")
    Solution().sortLetters(chars)
    assert "".join(chars)=="abcAD"