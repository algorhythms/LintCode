"""
Given n distinct positive integers, integer k (k <= n) and a number target.

Find k numbers where sum is target. Calculate how many solutions there are?

Example
Given [1,2,3,4], k=2, target=5. There are 2 solutions:

[1,4] and [2,3], return 2.
"""
__author__ = 'Danyang'


class Solution(object):
    def kSum(self, A, k, target):
        """
        brute force O(n^k)

        :param A: An integer array.
        :param k: a positive integer (k <= length(A))
        :param target: int
        :return: int
        """
        return self.dp(A, k, target)

    def dp(self, A, K, target):
        """
        DP:
        jCi = v

        f[i][j][v] = f[i-1][j-1][v-A[j-1]] + f[i][j-1][v]

        f[i][j][v] means the way of selecting i elements from the first j elements so that their sum equals to v
        j is the scanning pointer
        you can either select A[j-1] or not select A[j-1]

        O(n^2 k)

        :param A:
        :param K:
        :param target:
        :return:
        """
        n = len(A)

        f = [[[0 for _ in xrange(target+1)] for _ in xrange(n+1)] for _ in xrange(K+1)]
        for ind, val in enumerate(A):
            if val <= target:
                for j in xrange(ind+1, n+1):  # non-trivial
                    f[1][j][val] = 1

        for i in xrange(2, K+1):
            for j in xrange(i, n+1):
                for v in xrange(1, target+1):
                    f[i][j][v] = 0
                    if v-A[j-1] >= 0:
                        f[i][j][v] += f[i-1][j-1][v-A[j-1]]
                    if j-1 >= i:
                        f[i][j][v] += f[i][j-1][v]

        return f[K][n][target]

    def dfs_TLE(self, A, k, target, cur, ret):
        if len(cur) == k and sum(cur) == target:  # possible to optimized
            ret[0] += 1

        if not A or len(cur) >= k:
            return

        # if save space, you need to do the clean up
        num = A.pop(0)
        self.dfs_TLE(A, k, target, cur, ret)
        A.push(0, num)

        num = A.pop(0)
        cur.append(num)
        self.dfs_TLE(A, k, target, cur, ret)
        cur.pop()
        A.push(0, num)

    def dfs_TLE_2(self, A, k, target, s, l, la, ret):
        """
        Optimized version of dfs
        acceptable in k Sum II but TLE in k Sum
        """
        if l == k and s == target:
            ret[0] += 1

        if not A or l >= k or la+l < k:
            return

        # if save space, you need to do the clean up
        num = A.pop(0)
        self.dfs_TLE_2(A, k, target, s, l, la-1, ret)
        self.dfs_TLE_2(A, k, target, s+num, l+1, la-1, ret)
        A.push(0, num)


if __name__ == "__main__":
    assert Solution().kSum([1, 2, 3, 4], 2, 5) == 2
    assert Solution().kSum(
        [1, 3, 4, 5, 8, 10, 11, 12, 14, 17, 20, 22, 24, 25, 28, 30, 31, 34, 35, 37, 38, 40, 42, 44, 45, 48, 51, 54, 56,
         59, 60, 61, 63, 66], 24, 842) == 453474