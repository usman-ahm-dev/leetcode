"""128. Longest Consecutive Sequence
Given an unsorted array of integers nums, return the length of the longest consecutive
elements sequence.

You must write an algorithm that runs in O(n) time.
"""


class Solution:
    def longest_consecutive(self, nums: list[int]) -> int:
        """Returns the length of the longest consecutive
        elements sequence.

        Args:
            nums (list[int]):

        Returns:
            int:
        """
        nums_set = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in nums_set:
                length = 0
                while (num + length) in nums_set:
                    length += 1
                longest = max(longest, length)
        return longest
