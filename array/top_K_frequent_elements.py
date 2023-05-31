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
        freq_count = defaultdict(int)
        freq_list = [[] for i in range(len(nums) + 1)]  # Index represents frequency

        for num in nums:
            freq_count[num] += 1

        for num, freq in freq_count.items():
            freq_list[freq].append(num)

        result = []
        for i in range(len(freq_list) - 1, 0, -1):
            for num in freq_list[i]:
                result.append(num)
                if len(result) == k:
                    return result
