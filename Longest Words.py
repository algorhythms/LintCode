"""
Given a dictionary, find all of the longest words in the dictionary.

Have you met this question in a real interview? Yes
Example
Given

{
  "dog",
  "google",
  "facebook",
  "internationalization",
  "blabla"
}
the longest words are(is) ["internationalization"].

Given

{
  "like",
  "love",
  "hate",
  "yes"
}
the longest words are ["like", "love", "hate"].
"""
__author__ = 'Daniel'


class Solution:
    def longestWords(self, dictionary):
        """

        :param dictionary: a list of strings
        :return: a list of strings
        """
        ret = []
        for word in dictionary:
            if not ret or len(word) > len(ret[0]):
                ret = [word]

            elif len(word) == len(ret[0]):
                ret.append(word)

        return ret
