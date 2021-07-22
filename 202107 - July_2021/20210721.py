"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""

        smallest_word = min(strs)
        largest_word = max(strs)

        if smallest_word == None:
            return ""
        else:
            for char in range(len(smallest_word)):
                if largest_word[char] != smallest_word[char]:
                    return largest_word[:char]

        return smallest_word[:]