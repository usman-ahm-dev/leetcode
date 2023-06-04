"""49. Group Anagrams
Given an array of strings strs, group the anagrams together. You can return the answer
in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or
phrase, typically using all the original letters exactly once.
"""

from collections import defaultdict


class Solution:
    def group_anagrams(self, strs: list[str]) -> list[list[str]]:
        """Given an array of strings strs, groups the anagrams together

        Args:
            strs (list[str]):

        Returns:
            list[list[str]]: List of grouped anagrams (List of strings)
        """

        """Create N lists that each store character frequency per string
        (e.g [0, 0, 1, 3, 0, 1] = "cdddf"). Treat each list as a key and insert
        strings accordingly.

        METHOD 1: T = O(N) S = O(N) 
        (a) Create N lists of size 26 by iterating over N strings.
        (b) Iterate over each string, and +1 count at the proper index in the list for
        each character.
            (ba) Index for each character is decided by subtracting ASCII of char from
            ASCII of "a" by ord() function (e.g A = 0, B = 1, C = 2 etc.).
        (c) Insert into dictionary with the list (converted to tuple because of hash
        issues) as key and the string as value.

        METHOD 2: T = O(MNLogN) S = O(N)
        (a) Sort all strings.
        (b) Iterate and insert same strings in the same list of strings.
        """

        # METHOD 1
        result = defaultdict(list)
        for string in strs:
            key = [0] * 26
            for char in string:
                key[ord(char) - ord("a")] += 1
            result[tuple(key)].append(string)

        return result.values()
