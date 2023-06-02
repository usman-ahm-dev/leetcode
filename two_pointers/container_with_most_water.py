"""11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such
that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container
contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""


class Solution:
    def max_area(self, height: list[int]) -> int:
        """Returns the maximum area within a list of integers where each
        element is considered a height.

        Args:
            height (list[int]):

        Returns:
            int:
        """
        left, right = 0, len(height) - 1
        result = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            result = max(result, area)
            if height[left] < height[right]:
                right -= 1
            else:
                left += 1

        return result
