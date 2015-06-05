"""
Write a method to replace all spaces in a string with %20. The string is given in a characters array, you can assume it
has enough space for replacement and you are given the true length of the string.

Example
Given "Mr John Smith", length = 13.

The string after replacement should be "Mr%20John%20Smith".

Note
If you are using Java or Python, please use characters array instead of string.

Challenge
Do it in-place.
"""
__author__ = 'Daniel'


class Solution:
    def replaceBlank(self, string, length):
        """

        :param string: An array of Char
        :param length: The true length of the string
        :return: The true length of new string
        """
        i = 0
        while i < length:
            if string[i] == " ":
                string.append("")
                string.append("")
                length += 2
                for j in xrange(length-1, i, -1):
                    string[j] = string[j-2]

                string[i:i+3] = list("%20")
                i += 2
            i += 1

        return length

if __name__ == "__main__":
    assert Solution().replaceBlank(list("Mr John Smith"), 13) == 17