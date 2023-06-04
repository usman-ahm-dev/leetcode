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

        """Subtract nums[i] from target (complement) and check if it exists in nums. Use
        dictionary for O(1) lookups.

        METHOD 1: T = O(N) S = O(N) 
        (a) Create a dictionary that stores nums[i] : index
        (b) Iterate through nums
        (c) Subtract nums[i] from target
        (d) Check if it exists in dictionary. If it does, return [i, i of complement]
            IMPORTANT: Same index cannot be used, so check for complement before adding
            next element (this way i of complement will always be different than i
            because of the former being i of next value in next iteration).
            OR do it in 2 passes; Add all indices, then find complement and check if
            i & i of complement are different.
        """

        hashmap = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                return [i, hashmap[complement]]
            hashmap[num] = i
