"""
58. Length of Last Word

Given a string s consists of some words separated by spaces, return the length of the last word in the string. If the last word does not exist, return 0.

A word is a maximal substring consisting of non-space characters only.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split the string by the empty spaces
        # and store every word in a list
        s_list = list(s.split(" "))

        # loop through the list backwards
        for word in range(len(s_list) - 1, -1, -1):
            # if there is a word (not empty space)
            # return the length of that word
            if s_list[word]:
                return len(s_list[word])

        return 0