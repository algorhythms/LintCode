__author__ = 'Danyang'
class Solution:
    def kSumII(self, A, k, target):
        """
        brute force

        :param A: An integer array.
        :param k: a positive integer (k <= length(A))
        :param target: int
        :return: int
        """
        ret = []
        self.dfs(A, k, target, [], 0, 0, len(A), ret)
        return ret


    def dfs(self, A, k, target, cur, s, l, la, ret):
        if l==k and s==target:
            ret.append(list(cur))

        if not A or l>=k or la+l<k:
            return

        # if save space, you need to do the clean up
        num = A.pop(0)
        self.dfs(A, k, target, cur, s, l, la-1, ret)

        cur.append(num)
        self.dfs(A, k, target, cur, s+num, l+1, la-1, ret)
        cur.pop()
        A.insert(0, num)

if __name__=="__main__":
    print Solution().kSumII([1,2,3,4], 2, 5)