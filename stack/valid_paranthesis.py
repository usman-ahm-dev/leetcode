"""20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
"""


class Solution:
    def is_valid(self, s: str) -> bool:
        """Determines if parantheses are valid.

        Args:
            s (str):

        Returns:
            bool:
        """
        mapping = {")": "(", "}": "{", "]": "["}
        stack = []
        for paranthesis in s:
            if paranthesis not in mapping:
                stack.append(paranthesis)
            elif stack and stack.pop() != mapping[paranthesis]:
                return False
        return not stack
