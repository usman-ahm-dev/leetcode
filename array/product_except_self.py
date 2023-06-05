"""238. Product of Array Except Self
Given an integer array nums, return an array answer such that answer[i] is equal to the
product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division
operation.
"""


class Solution:
    def product_except_self(self, nums: list[int]) -> list[int]:
        """Returns an array answer such that answer[i] is equal to the
        product of all the elements of nums except nums[i].

        Args:
            nums (list[int]):

        Returns:
            list[int]:
        """

        """
        At each index of a list, store the result up to that point. And then
        do the same in reverse but combine the two.
        """

        answer = []
        prefix_sum = 1
        for num in nums:
            answer.append(prefix_sum)
            prefix_sum *= num
        postfix_sum = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= postfix_sum
            postfix_sum *= nums[i]
        return answer
