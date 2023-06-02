"""15. 3Sum
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such
that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Returns all triplets [nums[i], nums[j], nums[k]] such
        that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

        Args:
            nums (list[int]):

        Returns:
            list[list[int]]:
        """
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                three_sum = num + nums[left] + nums[right]
                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([nums[left], nums[right], num])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                    right -= 1
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
        return result
