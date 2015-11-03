"""
Given n items with size A[i], an integer m denotes the size of a backpack. How full you can fill this backpack?
"""
__author__ = 'Danyang'


class Solution(object):
    def backPack(self, m, A):
        """
        Left f_{i, c} represents the maximum value the bag has at the index i for a bag with capacity c.

        dp:
        f[i][c]=max{f[i-1][c],  # not choose the i-th item
                    f[i-1][c-w[i]] + v[i]  # choose the i-th item
                }

        optimized the data structure to
        f[v]=max{f[v],f[v-c[i]]+w[i]}

        NEED TO KEEP A COPY OF (i-1) STATE.

        :param m: An integer m denotes the size of a backpack
        :param A: Given n items with size A[i]
        :return: The maximum size
        """
        n = len(A)
        f = [0 for _ in xrange(m+1)]  # plus 1 for dummy
        for i in xrange(1, n+1):
            copy = list(f)
            for j in xrange(1, m+1):
                # decide whether to put A[i-1]
                if j-A[i-1] >= 0:
                    f[j] = max(copy[j], copy[j-A[i-1]]+A[i-1])
                else:
                    f[j] = copy[j]
        return f[m]


class Solution_TLE(object):
    def backPack(self, m, A):
        """
        search, brute force
        :param m: An integer m denotes the size of a backpack
        :param A: Given n items with size A[i]
        :return: The maximum size
        """
        result = [0]
        self.dfs(A, 0, m, result)
        return result[0]

    def dfs(self, seq, cur, m, result):
        if cur > m:
            return

        result[0] = max(result[0], cur)
        if seq:
            self.dfs(seq[1:], cur+seq[0], m, result)
            self.dfs(seq[1:], cur, m, result)


class Solution_MLE(object):
    def backPack(self, m, A):
        """
        dp
        f[i][v]=max{f[i-1][v],f[i-1][v-c[i]]+w[i]}

        :param m: An integer m denotes the size of a backpack
        :param A: Given n items with size A[i]
        :return: The maximum size
        """
        n = len(A)
        f = [[0 for _ in xrange(m+1)] for _ in xrange(n+1)]  # plus 1 for dummy
        for i in xrange(1, n+1):
            for j in xrange(1, m+1):
                # decide whether to put A[i-1]
                if j-A[i-1] >= 0:
                    f[i][j] = max(f[i-1][j], f[i-1][j-A[i-1]]+A[i-1])
                else:
                    f[i][j] = f[i-1][j]
        return f[n][m]


if __name__ == "__main__":
    print Solution().backPack(11, [2, 3, 5, 7])