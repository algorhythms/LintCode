"""
Print numbers from 1 to the largest number with N digits by recursion.

Have you met this question in a real interview? Yes
Example
Given N = 1, return [1,2,3,4,5,6,7,8,9].

Given N = 2, return [1,2,3,4,5,6,7,8,9,10,11,12,...,99].

Note
It's pretty easy to do recursion like:

recursion(i) {
    if i > largest number:
        return
    results.add(i)
    recursion(i + 1)
}
however this cost a lot of recursion memory as the recursion depth maybe very large. Can you do it in another way to
recursive with at most N depth?

Challenge
Do it in recursion, not for-loop.
"""
__author__ = 'Daniel'


class Solution(object):
    def numbersByRecursion(self, n):
        return self.rec(n)

    def rec(self, n):
        if n == 0:
            return []
        if n == 1:
            return [i+1 for i in xrange(9)]
        else:
            lst = self.rec(n-1)
            l = len(lst)
            cur = []
            prev = lst[-1]+1
            for i in xrange(prev-prev/10):
                for j in xrange(10):
                   cur.append(lst[prev/10-1+i]*10+j)

            lst.extend(cur)
            return lst

if __name__ == "__main__":
    print Solution().numbersByRecursion(2)
    assert Solution().numbersByRecursion(2) == [i+1 for i in xrange(99)]