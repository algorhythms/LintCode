"""
Given n and k, return the k-th permutation sequence.

Example
For n = 3, all permutations are listed as follows:

"123"
"132"
"213"
"231"
"312"
"321"
If k = 4, the fourth permutation is "231"

Note
n will be between 1 and 9 inclusive.

Challenge
O(n*k) in time complexity is easy, can you do it in O(n^2) or less?
"""
import math

__author__ = 'Daniel'


class Solution:
    def getPermutation(self, n, k):
        k -= 1  # start from 0

        array = range(1, n+1)
        k %= math.factorial(n)
        ret = []
        for i in xrange(n-1, -1, -1):
            idx, k = divmod(k, math.factorial(i))
            ret.append(array.pop(idx))

        return "".join(map(str, ret))