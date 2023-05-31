"""49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer
in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or
phrase, typically using all the original letters exactly once.
"""

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        """Given an array of strings strs, groups the anagrams together

        Args:
            strs (list[str]):

        Returns:
            list[list[str]]: List of grouped anagrams (List of strings)
        """
        anagram_dict = defaultdict(list)

        for s in strs:
            char_key = [0] * 26
            for char in s:
                char_key[ord(char) - ord("a")] += 1
            anagram_dict[tuple(char_key)].append(s)

        return anagram_dict.values()
