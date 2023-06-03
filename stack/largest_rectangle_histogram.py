"""84. Largest Rectangle in Histogram
Given an array of integers heights representing the histogram's bar height where the
width of each bar is 1, return the area of the largest rectangle in the histogram.
"""


class Solution:
    def largest_rectangle_area(self, heights: list[int]) -> int:
        """Returns the area of the largest rectangle in the histogram.

        Args:
            heights (list[int]):

        Returns:
            int:
        """
        stack = []  # (index, height)
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append([start, h])

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))
        return max_area
