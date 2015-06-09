"""
Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find
it.

Example
For [1, 1, 1, 1, 2, 2, 2], return 1

Challenge
O(n) time and O(1) space
"""
__author__ = 'Danyang'


class Solution:
    def majorityNumber(self, nums):
        """
        Moore's Voting Algorithm

        greedy half

        :param nums: A list of integers
        :return: The majority number
        """
        cnt = 0
        maj = 0
        for ind, num in enumerate(nums):
            if num == nums[maj]:
                cnt += 1
            else:
                cnt -= 1  # every time --, discard 2 different numbers

            if cnt < 0:
                maj = ind
                cnt = 1

        # assured that the majority exists, otherwise need to double check
        return nums[maj]


if __name__ == "__main__":
    assert Solution().majorityNumber([1, 1, 1, 2, 2, 2, 2, 1, 1]) == 1



