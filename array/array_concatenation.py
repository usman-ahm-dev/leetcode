"""1929. Concatenation of Array
Given an integer array nums of length n, you want to create an array ans of length 2n
where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

Specifically, ans is the concatenation of two nums arrays.

Return the array ans.
"""


class Solution:
    def get_concatenation(self, nums: list[int]) -> list[int]:
        """Returns an array as the concatenation of two nums arrays.

        Args:
            nums (list[int]):

        Returns:
            list[int]:
        """
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)

        return ans
