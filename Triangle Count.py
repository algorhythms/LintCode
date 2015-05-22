"""
Given an array of integers, how many three numbers can be found in the array, so that we can build an triangle whose
three edges length is the three numbers that we find?

Example
Given array S = [3,4,6,7], return 3. They are:

[3,4,6]
[3,6,7]
[4,6,7]
Given array S = [4,4,4,4], return 4. They are:

[4(1),4(2),4(3)]
[4(1),4(2),4(4)]
[4(1),4(3),4(4)]
[4(2),4(3),4(4)]
"""
__author__ = 'Daniel'


class Solution:
    def triangleCount(self, S):
        """
        Brute force: O(n^3)
        Two pointers with binary search: O(n^2 lg n)

        Two-pointer algorithm: O(n^2)
        Triangle inequality a+b>c
        Fix the higher pointer; two other pointers are set at start and end respectively and converge them.
        The converging two pointers should be in the same side of triangle inequality

        :param S: a list of integers
        :return: a integer
        """
        S.sort()
        cnt = 0
        for h in xrange(len(S)-1, 1, -1):
            s = 0
            e = h-1
            while s<e:
                if S[s]+S[e]>S[h]:
                    cnt += e-s
                    e -= 1
                else:
                    s += 1

        return cnt

if __name__ == "__main__":
    assert Solution().triangleCount([3, 4, 6, 7]) == 3