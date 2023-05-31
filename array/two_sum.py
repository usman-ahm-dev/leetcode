"""1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.

You can return the answer in any order.
"""


class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        """Returns indices of the two numbers in the form of a list
        such that they add up to the target.

        Args:
            nums (list[int]):
            target (int):

        Returns:
            list[int]:
        """
        hashmap = {}  # value : index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [i, hashmap[diff]]
            hashmap[num] = i
