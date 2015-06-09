"""
The code base version is an integer and start from 1 to n. One day, someone commit a bad version in the code case, so
it caused itself and the following versions are all failed in the unit tests.
"""
__author__ = 'Danyang'


class VersionControl:
    @classmethod
    def isBadVersion(cls, id):
        return True


class Solution:
    def findFirstBadVersion(self, n):
        """

        :param n: An integers.
        :return: An integer which is the first bad version.
        """
        l = 1
        h = n+1
        while l < h:
            m = (l+h)/2
            if not VersionControl.isBadVersion(m):
                l = m+1
            else:
                h = m

        return l


