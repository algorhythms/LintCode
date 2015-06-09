"""
Given n items with size A[i] and value V[i], and a backpack with size m. What's the maximum value can you put into the
backpack?
"""
__author__ = 'Danyang'


class Solution:
    def backPackII(self, m, A, V):
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
        :param A & V: Given n items with size A[i] and value V[i]
        :return: The maximum size
        """
        n = len(A)
        f = [0 for _ in xrange(m+1)]  # plus 1 for dummy
        for i in xrange(1, n+1):
            copy = list(f)
            for j in xrange(1, m+1):
                # decide whether to put A[i-1]
                if j-A[i-1]>=0:
                    f[j] = max(copy[j], copy[j-A[i-1]]+V[i-1])
                else:
                    f[j] = copy[j]
        return f[m]