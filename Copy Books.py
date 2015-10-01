"""
Given an array A of integer with size of n( means n books and number of pages of each book) and k people to copy the
book. You must distribute the continuous id books to one people to copy. (You can give book A[1],A[2] to one people, but
you cannot give book A[1], A[3] to one people, because book A[1] and A[3] is not continuous.) Each person have can copy
one page per minute. Return the number of smallest minutes need to copy all the books.

Example
Given array A = [3,2,4], k = 2.

Return 5 (First person spends 5 minutes to copy book 1 and book 2 and second person spends 4 minutes to copy book 3.)

Challenge
Could you do this in O(n*k) time ?
"""
__author__ = 'Daniel'


class Solution:
    def copyBooks(self, pages, k):
        """
        DP:
        let F[i][j] be the smallest page count with the person[:i] copying the pages[:j]

        F[i][j] = min(
           max(F[i-1][t], sum(pages[t:j]) \forall t \in [0, j))
        )

        F[i][j] is monotonous w.r.t. both i and j

        left r pointers
        move left pointer if the previous people assigned less compared to current person
        move r pointer otherwise

        Complexity analysis:
        for each people,
          r forward at most n
          l backward at most n
          l forward at most 2n
        thus, O(n k)
        :type pages: List[int]
        :type k: int
        :rtype: int
        """
        n = len(pages)
        s = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            s[i] = s[i-1] + pages[i-1]

        F = [[s[j] for j in xrange(n+1)] for _ in xrange(k+1)]  # initialize to upper limit

        for i in xrange(2, k+1):
            l = 0  # left
            r = 1  # right
            while r < n+1:
                F[i][r] = min(F[i][r],
                    max(F[i-1][l], s[r]-s[l])
                )
                if F[i-1][l] < s[r]-s[l] and l < r:
                    # assign less to current people
                    l += 1
                else:
                    # assign more to current people
                    if l > 0: l -= 1
                    r += 1

        return F[-1][-1]


class Solution_TLE:
    def copyBooks(self, pages, k):
        """
        DP:
        let F[i][j] be the smallest page count with the person[:i] copying the pages[:j]

        F[i][j] = min(
           max(F[i-1][t], sum(pages[t:j]) \forall t \in [0, j))
        )

        O(n^2 k)
        :type pages: List[int]
        :type k: int
        :rtype: int
        """
        n = len(pages)
        s = [0 for _ in xrange(n+1)]
        for i in xrange(1, n+1):
            s[i] = s[i-1] + pages[i-1]

        F = [[s[j] for j in xrange(n+1)] for _ in xrange(k+1)]  # initialize to upper limit

        for i in xrange(2, k+1):
            for j in xrange(1, n+1):
                F[i][j] = min(
                    max(F[i-1][t], s[j]-s[t]) for t in xrange(j)
                )

        return F[-1][-1]


class Solution_search:
    def copyBooks(self, pages, k):
        """
        :type pages: List[int]
        :type k: int
        :rtype: int
        """
        return self.bisect(pages, k, sum(pages)/k, sum(pages))

    def bisect(self, pages, k, lower, upper):
        """
        O(n lg sum(p))
        """
        while lower < upper:
            mid = (lower+upper)/2
            if self.valid(pages, k, mid):
                upper = mid
            else:
                lower = mid+1

        return lower

    def valid(self, pages, k, limit):
        cnt = 0
        k -= 1
        for p in pages:
            if p > limit: return False

            cnt += p
            if cnt > limit:
                cnt = p
                k -= 1

            if k < 0: return False

        return True


if __name__ == "__main__":
    assert Solution().copyBooks([3, 2], 5) == 3