"""392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by
deleting some (can be none) of the characters without disturbing the relative positions
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is
not).
"""


class Solution:
    def is_subsequence(self, s: str, t: str) -> bool:
        """Returns true if s is a subsequence of t, or false otherwise.

        Args:
            s (str):
            t (str):

        Returns:
            bool:
        """
        if not s:
            return True

        i = 0
        for char in t:
            if s[i] == char:
                i += 1
            if i == len(s):
                return True
        return False
