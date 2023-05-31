"""242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or
phrase, typically using all the original letters exactly once.
"""


class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        """Given two strings s and t, returns true if t is an anagram of s, and false
        otherwise.

        Args:
            s (str):
            t (str):

        Returns:
            bool:
        """
        if len(s) != len(t):
            return False

        s_dict, t_dict = {}, {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

        for key in s_dict:
            if s_dict[key] != t_dict.get(key, 0):
                return False

        return True
