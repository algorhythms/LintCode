"""
Given string A representative a positive integer which has N digits, remove any k digits of the number, the remaining
digits are arranged according to the original order to become a new positive integer. Make this new positive integers
as small as possible.
N <= 240 and k <=N,
Example
Given an integer A = 178542, k = 4

return a string "12"
"""
import heapq

__author__ = 'Danyang'


class Solution:
    def DeleteDigits(self, A, k):
        """
        greedy algorithm:
        compare in pairs, if the 1st is larger than 2nd, then remove it

        be careful when index i becomes negative

        :param A: A positive integer which has N digits, A is a string.
        :param k: Remove k digits.
        :return: A string
        """
        lst = map(int, list(str(A)))
        i = 0
        while i+1 < len(lst) and k > 0:
            if lst[i] > lst[i+1]:
                del lst[i]
                i -= 1
                if i < 0:
                    i = 0
                k -= 1
            else:
                i += 1
        if k > 0:
            lst = lst[:len(lst)-k]

        return "".join(map(str, lst)).lstrip("0")

    def DeleteDigits_error(self, A, k):
        """
        Remove and keep the n-k largest numbers
        heap: O(n lg (n-k))

        error in case: 254193, 1

        :param A: A positive integer which has N digits, A is a string.
        :param k: Remove k digits.
        :return: A string
        """
        lst = map(int, list(str(A)))
        m = len(lst)-k

        tuples = [(-lst[i], i) for i in xrange(m)]  # negative sign for max heap
        heapq.heapify(tuples)
        for i in xrange(m, len(lst)):
            if -tuples[0][0] > lst[i]:
                heapq.heappop(tuples)
                heapq.heappush(tuples, (-lst[i], i))

        rets = [elt[1] for elt in tuples]
        rets.sort()
        rets = map(lambda x: str(lst[x]), rets)
        return "".join(rets)


if __name__ == "__main__":
    assert Solution().DeleteDigits(10009876091, 4) == "6091"


