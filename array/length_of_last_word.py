"""58. Length of Last Word
Given a string s consisting of words and spaces, return the length of the last word in
the string.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    def length_of_last_word(self, s: str) -> int:
        """Returns the length of the last word in
        the string.

        Args:
            s (str):

        Returns:
            int:
        """
        length = 0
        i = len(s) - 1
        while i >= 0:
            if s[i] == " ":
                i -= 1
                continue
            while s[i] != " " and i >= 0:
                length += 1
                i -= 1
            return length
