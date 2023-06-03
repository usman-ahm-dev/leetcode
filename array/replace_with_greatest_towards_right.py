"""1299. Replace Elements with Greatest Element on Right Side
Given an array arr, replace every element in that array with the greatest element among
the elements to its right, and replace the last element with -1.

After doing so, return the array.
"""


class Solution:
    def replace_elements(self, arr: list[int]) -> list[int]:
        """Replaces every element in a given array with the greatest element among
        the elements to its right, and replace the last element with -1.

        Args:
            arr (list[int]):

        Returns:
            list[int]:
        """
        max_yet = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(max_yet, arr[i])
            arr[i] = max_yet
            max_yet = new_max

        return arr
