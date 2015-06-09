"""
Compare two strings A and B, determine whether A contains all of the characters in B.
"""
__author__ = 'Danyang'


class Solution:
    def compareStrings(self, A, B):
        """
        Straightforward

        :param A : A string includes Upper Case letters
        :param B : A string includes Upper Case letters
        :return :  if string A contains all of the characters in B return True else return False
        """
        cnt = [0 for _ in xrange(26)]
        for c in A:
            cnt[ord(c)-ord('A')] += 1
        for c in B:
            cnt[ord(c)-ord('A')] -= 1
            if cnt[ord(c)-ord('A')]<0:
                return False
        return True

if __name__=="__main__":
    assert Solution().compareStrings("A", "")==True