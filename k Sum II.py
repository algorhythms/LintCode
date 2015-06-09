"""
Given n unique integers, number k (1<=k<=n)  and target. Find all possible k integers where their sum is target.

Example
Given [1,2,3,4], k=2, target=5, [1,4] and [2,3] are possible solutions.
"""
__author__ = 'Danyang'


class Solution:
    def kSumII(self, A, k, target):
        """
        brute force dfs
        Branch and prune

        :param A: An integer array.
        :param k: a positive integer (k <= length(A))
        :param target: int
        :return: int
        """
        ret = []
        # self.dfs(A, k, [], target, ret)
        self.dfs_stk(A[::-1], k, [], target, ret)
        return ret

    def dfs(self, A, k, cur, remain, ret):
        if len(cur) == k and remain == 0:
            ret.append(list(cur))

        if not A or len(cur) >= k or len(A)+len(cur) < k:
            return

        # save space, but need to do the clean up
        num = A.pop(0)

        self.dfs(A, k, cur, remain, ret)
        cur.append(num)
        self.dfs(A, k, cur, remain-num, ret)
        cur.pop()

        A.push(0, num)

    def dfs_stk(self, A, k, cur, remain, ret):
        """
        since array insert takes O(n), speed up by using stack
        """
        if len(cur) == k and remain == 0:
            ret.append(list(cur))

        if not A or len(cur) >= k or len(A)+len(cur) < k:
            return

        # save space, but need to do the clean up
        num = A.pop()

        self.dfs(A, k, cur, remain, ret)
        cur.append(num)
        self.dfs(A, k, cur, remain-num, ret)
        cur.pop()

        A.append(num)


if __name__ == "__main__":
    assert Solution().kSumII([1, 2, 3, 4], 2, 5) == [[3, 2], [1, 4]]