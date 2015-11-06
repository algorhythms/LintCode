"""
Given n, how many structurally unique BSTs (binary search trees) that store values 1...n?

Have you met this question in a real interview? Yes
Example
Given n = 3, there are a total of 5 unique BST's.

1           3    3       2      1
 \         /    /       / \      \
  3      2     1       1   3      2
 /      /       \                  \
2     1          2                  3
"""
__author__ = 'Daniel'


class Solution:
    def __init__(self):
        self.cache = {}

    def numTrees(self, n):
        return self.dfs(n)

    def dfs(self, n):
        if n not in self.cache:
            if n in (0, 1, 2):
                self.cache[n] = max(1, n)
            else:
                s = 0
                for i in xrange(1, n+1):
                    l = self.dfs(i-1)
                    r = self.dfs(n-i)
                    s += l*r  # multiplication rather than plus

                self.cache[n] = s

        return self.cache[n]


if __name__ == "__main__":
    print Solution().numTrees(3)