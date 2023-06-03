"""739. Daily Temperatures
Given an array of integers temperatures represents the daily temperatures, return an
array answer such that answer[i] is the number of days you have to wait after the ith
day to get a warmer temperature. If there is no future day for which this is possible,
keep answer[i] == 0 instead.
"""


class Solution:
    def daily_temperatures(self, temperatures: list[int]) -> list[int]:
        """Returns an array answer such that answer[i] is the number of days you have to
        wait after the ith day to get a warmer temperature.

        Args:
            temperatures (list[int]):

        Returns:
            list[int]:
        """
        answer = [0] * len(temperatures)
        stack = []  # [temp, index]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                s_temp, s_ind = stack.pop()
                answer[s_ind] = i - s_ind
            stack.append([temp, i])

        return answer
