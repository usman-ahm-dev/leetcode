"""347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You
may return the answer in any order.
"""


from collections import defaultdict


class Solution:
    def top_k_frequent(self, nums: list[int], k: int) -> list[int]:
        """Returns the k most frequent elements from a list of numbers.

        Args:
            nums (list[int]):
            k (int):

        Returns:
            list[int]:
        """

        """
        Create a list of lists where each index represents a frequency and
        elements at that position occur index number of times. List of lists because
        multiple elements can occur the same number of times.

        METHOD 1: T = O(N) S = O(N)
        (a) Create a frequency map for counting and list of size len(nums) +1 for doing
        the aforementioned thing.
        (b) Count frequencies, and then iterate over it and insert in the list where
        frequency is the index and num is the value.
        (c) Iterate in reverse throught the freq list and then nest another iteration
        inside and iterate again to insert each num from each list at every index.
            (c1) Stop when result len == k

        METHOD 2: Quickselect - Not yet understood.
        """

        # METHOD 1
        frequency_map = defaultdict(int)
        frequency_list = [[] for i in range(len(nums) + 1)]
        result = []

        for num in nums:
            frequency_map[num] += 1
        for num, frequency in frequency_map.items():
            frequency_list[frequency].append(num)

        for i in range(len(frequency_list) - 1, -1, -1):
            for num in frequency_list[i]:
                result.append(num)
                if len(result) == k:
                    return result
