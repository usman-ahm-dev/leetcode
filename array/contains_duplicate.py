"""217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the
array, and return false if every element is distinct.
"""


class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        """Returns true if any value appears at least twice in a given array, and
        returns false if every element is distinct.

        Args:
            nums (list[int]):

        Returns:
            bool:
        """
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False
