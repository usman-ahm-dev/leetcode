"""42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar
is 1, compute how much water it can trap after raining.
"""


class Solution:
    def trap(self, height: list[int]) -> int:
        """Given n non-negative integers representing an elevation map where the width
        of each bar is 1, computes how much water it can trap after raining.

        Args:
            height (list[int]):

        Returns:
            int:
        """
        left, right = 0, len(height) - 1
        max_left_height, max_right_height = height[0], height[-1]
        water = 0

        while left < right:
            if max_left_height < max_right_height:
                if height[left] < max_left_height:
                    water = water + (
                        min(max_left_height, max_right_height) - height[left]
                    )
                left += 1
                max_left_height = max(max_left_height, height[left])
            else:
                if height[right] < max_right_height:
                    water = water + (
                        min(max_left_height, max_right_height) - height[right]
                    )
                right -= 1
                max_right_height = max(max_right_height, height[right])

        return water
