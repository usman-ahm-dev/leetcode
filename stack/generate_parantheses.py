"""22. Generate Parentheses
Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.
"""


class Solution:
    def generate_parentheses(self, n: int) -> list[str]:
        """Given n, generates all combinations of
        well-formed parentheses.

        Args:
            n (int):

        Returns:
            list[str]:
        """
        stack = []
        result = []

        def backtracking(opened, closed):
            """Recursive function to generate all combinations of
            well-formed parentheses.

            Args:
                opened (int): Number of ( paranthesis
                closed (int): Number of ) paranthesis
            """
            if opened == closed == n:
                result.append("".join(stack))
                return

            if opened < n:
                stack.append("(")
                backtracking(opened + 1, closed)
                stack.pop()

            if closed < opened:
                stack.append(")")
                backtracking(opened, closed + 1)
                stack.pop()

        backtracking(0, 0)
        return result
