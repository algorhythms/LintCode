"""
Given an integer array, find a subarray where the sum of numbers is between two given interval. Your code should return
the number of possible answer.

Have you met this question in a real interview? Yes
Example
Given [1,2,3,4] and interval = [1,3], return 4. The possible answers are:

[0, 0]
[0, 1]
[1, 1]
[3, 3]

"""
__author__ = 'Daniel'
from bisect import bisect_left, bisect_right


class Solution:
    def subarraySumII(self, A, start, end):
        """
        O(n lg n) Binary Search
        Bound:
        f[i] - f[j] = start
        f[i] - f[j'] = end
        start < end
        f[j] > f[j']

        :param A: an integer array
        :param start: start an integer
        :param end: end an integer
        :return:
        """
        n = len(A)
        cnt = 0
        f = [0 for _ in xrange(n+1)]

        for i in xrange(1, n+1):
            f[i] = f[i-1]+A[i-1]  # from left

        f.sort()
        for i in xrange(n+1):
            lo = bisect_left(f, f[i]-end, 0, i)
            hi = bisect_right(f, f[i]-start, 0, i)
            cnt += hi-lo  # 0----lo----hi-----END

        return cnt

    def subarraySumII_TLE(self, A, start, end):
        """
        O(n^2)

        :param A: an integer array
        :param start: start an integer
        :param end: end an integer
        :return:
        """
        n = len(A)
        cnt = 0
        f = [0 for _ in xrange(n+1)]

        for i in xrange(1, n+1):
            f[i] = f[i-1]+A[i-1]  # from left

        for i in xrange(0, n+1):
            for j in xrange(i+1, n+1):
                s = f[j]-f[i]
                if start <= s <= end:
                    cnt += 1

        return cnt


if __name__ == "__main__":
    assert Solution().subarraySumII([1, 2, 3, 4], 1, 3) == 4



