
"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example
Given [1, 9, 2, 5], the sorted form of it is [1, 2, 5, 9], the maximum gap is between 5 and 9 = 4.

Note
You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.

Challenge
Sort is easy but will cost O(nlogn) time. Try to solve it in linear time and space.
"""
__author__ = 'Daniel'
import sys


class Solution:
    def maximumGap(self, nums):
        """
        O(n lg n) algorithm is trivial, need to speed up to the next possible complexity, i.e. O(n)

        Bucket (histogram bin) algorithm O(n)
        The LOWER bound of gap is (max-min)/(n-1), which can be proved by consider evenly distributed numbers and
        non-evenly distributed numbers.

        Cluster the numbers into bins like the histogram
        Find the maximum gap by examine the maximum distance between elements in neighboring bins.

        :param nums: a list of integers
        :return: the maximum difference
        """
        n = len(nums)
        if n < 2:
            return 0

        gmax = max(nums)
        gmin = min(nums)
        bin_width = max(1, (gmax-gmin)/(n-1))  # lower bound of the max gap

        bins_max = {}  # use hash map instead of array since possible empty bin
        bins_min = {}

        for elt in nums:
            bin_num = (elt-gmin)/bin_width
            bins_min[bin_num] = min(bins_min.get(bin_num, sys.maxint), elt)
            bins_max[bin_num] = max(bins_max.get(bin_num, -sys.maxint-1), elt)

        max_gap = -1
        pre_bin_max = gmin
        for i in xrange((gmax-gmin)/bin_width+1):
            if i in bins_min:
                max_gap = max(max_gap, bins_min[i]-pre_bin_max)
                pre_bin_max = bins_max[i]

        return max_gap

if __name__ == "__main__":
    assert Solution().maximumGap([1, 9, 2, 5]) == 4