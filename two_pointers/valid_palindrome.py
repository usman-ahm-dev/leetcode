"""125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase
letters and removing all non-alphanumeric characters, it reads the same forward and
backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""


class Solution:
    def is_palindrome(self, s: str) -> bool:
        """Returns true if a given string is a palindrome, or false otherwise.

        Args:
            s (str):

        Returns:
            bool:
        """
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not self.alpha_numeric(s[left]):
                left += 1
            while right > left and not self.alpha_numeric(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def alpha_numeric(self, char: str):
        """Returns true if a given character is alphanumeric, or false otherwise

        Args:
            char (str):

        Returns:
            bool:
        """
        return (
            ord("A") <= ord(char) <= ord("Z")
            or ord("a") <= ord(char) <= ord("z")
            or ord("0") <= ord(char) <= ord("9")
        )
