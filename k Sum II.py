"""
Given n unique integers, number k (1<=k<=n)  and target. Find all possible k integers where their sum is target.

Example
Given [1,2,3,4], k=2, target=5, [1,4] and [2,3] are possible solutions.
"""
__author__ = 'Danyang'


class Solution(object):
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
        self.dfs(A, 0, k, [], target, ret)
        return ret

    def dfs(self, A, i, k, cur, remain, ret):
        """self.dfs(A, 0, k, [], target, ret)"""
        if len(cur) == k and remain == 0:
            ret.append(list(cur))
            return

        if i >= len(A) or len(cur) > k or len(A)-i+len(cur) < k:
            return

        self.dfs(A, i+1, k, cur, remain, ret)
        cur.append(A[i])
        self.dfs(A, i+1, k, cur, remain-A[i], ret)
        cur.pop()

    def dfs_array(self, A, k, cur, remain, ret):
        """
        self.dfs_array(A, k, [], target, ret)
        """
        if len(cur) == k and remain == 0:
            ret.append(list(cur))

        if not A or len(cur) >= k or len(A)+len(cur) < k:
            return

        # save space
        num = A.pop(0)  # possible optimized by stack

        self.dfs_array(A, k, cur, remain, ret)
        cur.append(num)
        self.dfs_array(A, k, cur, remain-num, ret)
        cur.pop()

        A.push(0, num)

    def dfs_stk(self, A, k, cur, remain, ret):
        """
        self.dfs_stk(A[::-1], k, [], target, ret)
        since array insert takes O(n), speed up by using stack
        """
        if len(cur) == k and remain == 0:
            ret.append(list(cur))

        if not A or len(cur) >= k or len(A)+len(cur) < k:
            return

        # save space
        num = A.pop()

        self.dfs(A, k, cur, remain, ret)
        cur.append(num)
        self.dfs(A, k, cur, remain-num, ret)
        cur.pop()

        A.append(num)


if __name__ == "__main__":
    print Solution().kSumII([1, 2, 3, 4], 2, 5)
    assert Solution().kSumII([1, 2, 3, 4], 2, 5) == [[3, 2], [1, 4]]