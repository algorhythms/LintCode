"""
Binary search is a famous question in algorithm.

For a given sorted array (ascending order) and a target number, find the first index of this number in O(log n) time
complexity.

If the target number does not exist in the array, return -1.
"""
__author__ = 'Danyang'


class Solution:
    def binarySearch(self, nums, target):
        """
        basics

        :param nums: The integer array
        :param target: Target number to find
        :return the first position of target in nums, position start from 0
        """
        l = 0
        h = len(nums)
        while l < h:
            mid = (l+h)/2
            if nums[mid] == target:
                while mid >= 0 and nums[mid-1] == nums[mid]: mid -= 1
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                h = mid
        return -1

