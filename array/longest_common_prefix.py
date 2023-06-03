"""14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longest_common_prefix(self, strs: list[str]) -> str:
        """Finds the longest common prefix string amongst an array of strings.

        Args:
            strs (list[str]):

        Returns:
            str:
        """
        result = []
        for i in range(len(strs[0])):
            for string in strs:
                if i == len(string) or string[i] != strs[0][i]:
                    return "".join(result)
            result.append(strs[0][i])
        return "".join(result)
