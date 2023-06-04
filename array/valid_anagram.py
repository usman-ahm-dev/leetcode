"""242. Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or
phrase, typically using all the original letters exactly once.
"""


from collections import defaultdict


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

        """Frequence of every element in both strings needs to be the same.

        METHOD 1: T = O(N) S = O(N) 
        (a) Use two dictionaries (hash tables).
        (b) Add elements from both s and t to dict_s and dict_t respectively
        (c) Compare values (frequency count) of both dicts
            (c1) If equal, valid anagrams, else not.
            IMPORTANT: Frequency can still be same if comparing solely that. Must
            compare frequence of same elements.
            EDGE: Length must be s == t.

        METHOD 2: T = O(NLogN) S = O(1) or O(N)
        (a) Sort both strings.
        (b) Iterate both and compare.
            (b1) If characters are different at same index, invalid anagram.
        """

        # METHOD 1
        if len(s) != len(t):
            return False

        frequency_s = defaultdict(int)
        frequency_t = defaultdict(int)
        for i in range(len(s)):
            frequency_s[s[i]] += 1
            frequency_t[t[i]] += 1
        for char in s:
            if frequency_s[char] != frequency_t[char]:
                return False
        return True
